class Engine:
    def __init__(self, player):
        self.player = player
        self.missions = self.load_missions()

    def load_missions(self):
        missions = []
        if not os.path.exists(MISSIONS_DIR):
            os.makedirs(MISSIONS_DIR)
            console.print(f"[yellow]Created {MISSIONS_DIR}/ directory. Please add mission JSON files.[/yellow]")
            return missions

        for filename in sorted(os.listdir(MISSIONS_DIR)):
            if filename.endswith(".json"):
                with open(os.path.join(MISSIONS_DIR, filename), 'r') as f:
                    missions.append(json.load(f))
        return sorted(missions, key=lambda x: x.get("number", 999))

    def run_mission(self, mission):
        console.clear()
        console.print(Panel(f"[bold cyan]{mission['title']}[/bold cyan]", expand=False))
        
        # Progressive Disclosure: Beginner vs Deep Dive
        console.print(f"\n[bold green]🌱 Philosophy (Beginner):[/bold green] {mission['philosophy_beginner']}")
        
        if Confirm.ask("\n[bold]Engage Deep Dive?[/bold] (Explore Uta Hagen, Economics, and Systems Thinking)"):
            deep_dive_text = f"**Philosophy:** {mission['philosophy_deep_dive']}\n\n**Economics:** {mission['economics']}"
            console.print(Panel(Markdown(deep_dive_text), border_style="blue"))

        console.print(f"\n[bold magenta]💻 Technical Concept:[/bold magenta] {mission['tech_concept']}")
        console.print(f"\n[bold red]⚔️ Challenge:[/bold red] {mission['challenge']}")

        # Action-Based Challenge with Retry Loop & Forgiving Parsing
        while True:
            attempt = Prompt.ask("\n[bold yellow]Enter your code (or type 'retreat')[/bold yellow]")
            
            if attempt.strip().lower() == 'retreat':
                console.print("[dim]Retreating to the Dojo hub. Re-evaluate your strategy.[/dim]")
                break
            
            # Normalize whitespaces to prevent frustration over a single space
            normalized_attempt = " ".join(attempt.strip().split())
            normalized_answers = [" ".join(a.strip().split()) for a in mission['answer']]

            if normalized_attempt in normalized_answers:
                console.print("\n[bold green]✅ Ecology sustained. Mission passed.[/bold green]")
                self.award_competency(mission)
                self.uta_hagen_reflection(mission)
                break
            else:
                console.print("[bold red]❌ Syntax misalignment. The ecosystem rejects this input. Try again.[/bold red]")

    def award_competency(self, mission):
        skill = mission.get("skill_target", "python")
        # Ensure we don't hit a KeyError if a community member adds a rogue skill
        if skill in self.player.competencies:
            self.player.competencies[skill] += 1
        self.player.honor += 10
        self.player.completed_missions.append(mission["id"])
        console.print(f"[green]+10 Honor | +1 {skill.capitalize()} Competency[/green]")

    def uta_hagen_reflection(self, mission):
        console.print("\n[bold blue]📔 Uta Hagen Systems Thinking Journal[/bold blue]")
        reflection = Prompt.ask("What part of this system surprised you, or what remains confusing? (Persisted to ledger)")
        
        entry = {
            "mission_id": mission["id"],
            "reflection": reflection
        }
        self.player.journal.append(entry)
        self.player.save_state()
        console.print("[dim]Journal serialized to save_state.json.[/dim]")

    def start(self):
        # Persistent Hub Loop
        while True:
            console.clear()
            console.print(Panel("[bold green]Welcome to DOJO ASCENSION[/bold green]\n[dim]Initializing Digital Ecology...[/dim]"))
            self.player.display_stats()

            # Refresh available missions on every loop iteration
            available_missions = [m for m in self.missions if m["id"] not in self.player.completed_missions]

            if not available_missions:
                console.print("\n[bold cyan]All available ecosystems restored. Await new JSON packs from the community.[/bold cyan]")
                break

            next_mission = available_missions[0]
            
            console.print("\n[bold]Dojo Options:[/bold]")
            console.print(f"1. Engage Mission {next_mission['number']}: {next_mission['title']}")
            console.print("2. Exit Dojo (Save State)")
            
            choice = Prompt.ask("\nSelect an action", choices=["1", "2"])

            if choice == "2":
                console.print("[dim]Suspending digital ecology... Farewell.[/dim]")
                break

            # Execute mission, then pause before resetting the loop
            self.run_mission(next_mission)
            Prompt.ask("\n[dim]Press Enter to return to the Dojo Hub...[/dim]")

if __name__ == "__main__":
    player = Player()
    engine = Engine(player)
    engine.start()
