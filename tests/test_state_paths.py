import json
import os
import tempfile
import unittest
from pathlib import Path

import dojo_classroom


class StatePathTests(unittest.TestCase):
    def test_default_missions_file_points_to_repo_index(self):
        expected = Path(dojo_classroom.__file__).resolve().parent / "missions" / "missions.json"
        self.assertEqual(dojo_classroom.MISSIONS_FILE.resolve(), expected)

    def test_load_missions_falls_back_to_folder_files_when_index_is_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            mission_dir = Path(tmpdir) / "missions"
            mission_dir.mkdir()
            mission_path = mission_dir / "mission01.json"
            mission_path.write_text(
                json.dumps({
                    "id": "demo_mission",
                    "number": 1,
                    "title": "Demo Mission",
                    "skill": "python",
                    "challenge": "What is 2 + 2?",
                    "answer": "4"
                }),
                encoding="utf-8"
            )

            original_missions_file = dojo_classroom.MISSIONS_FILE
            try:
                dojo_classroom.MISSIONS_FILE = mission_dir / "missions.json"
                missions = dojo_classroom.load_missions()
            finally:
                dojo_classroom.MISSIONS_FILE = original_missions_file

            self.assertEqual(len(missions), 1)
            self.assertEqual(missions[0]["id"], "demo_mission")

    def test_state_paths_follow_environment_overrides(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            custom_dir = Path(tmpdir) / "alice-dojo"
            save_path = custom_dir / "player-save.json"
            journal_path = custom_dir / "player-journal.json"

            os.environ["DOJO_DATA_DIR"] = str(custom_dir)
            os.environ["DOJO_SAVE_FILE"] = str(save_path)
            os.environ["DOJO_JOURNAL_FILE"] = str(journal_path)

            self.addCleanup(os.environ.pop, "DOJO_DATA_DIR", None)
            self.addCleanup(os.environ.pop, "DOJO_SAVE_FILE", None)
            self.addCleanup(os.environ.pop, "DOJO_JOURNAL_FILE", None)

            resolved_save, resolved_journal = dojo_classroom.get_state_paths()

            self.assertEqual(resolved_save, save_path)
            self.assertEqual(resolved_journal, journal_path)


if __name__ == "__main__":
    unittest.main()
