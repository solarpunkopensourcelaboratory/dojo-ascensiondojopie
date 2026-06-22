# 🃏 Dojo Ascension — 52-Card Memory Deck (v2)

> **Covers:** Python · JSON · JavaScript · HTML · GitHub Workflows  
> **For:** Young learners, Dojo Ascension curriculum, physical or digital flashcard play

***

## How to Play

**Memory Match** — Lay all cards face-down. Flip two at a time. Match concept card to its code/answer card.

**Solo Drill** — Read the **Front** (concept + visual + snippet). Flip for the **Back** (metaphor + exercise).

**Dojo Mission Unlock** — Complete a dojo mission → earn the matching card. Track mastered cards in your save file using stable IDs.

**Practice Chain** — How many days in a row can you answer every card in a suit? Track your continuity, not your streak.

**Tier Progression** — Play only 🟢 Beginner cards first. Unlock 🟡 Intermediate after completing a Beginner run. Unlock 🔴 Advanced last.

***

## PYTHON 🐍

**Suit of Roots.** Python is the soil — every other technology grows from here.

| Tier | Cards | Learning Outcome |
|------|-------|------------------|
| 🟢 Beginner | A–6 | Variables, print, strings, numbers, booleans, if/else |
| 🟡 Intermediate | 7–J | Loops, functions, lists, dictionaries |
| 🔴 Advanced | Q–K | Imports, OOP / Class |

***

### 🟢 A — Variable  `[Beginner]`

**🎴 FRONT**

```
📦 [ seed = 42 ]
```

```python
seed = 42
name = 'David'
```

**🔄 BACK**

*A named vessel. Like a seed — holds potential until called.*

🎯 Try it: Open your terminal. Type `seed = 42` then `print(seed)`. What appears?

***

### 🟢 2 — Print  `[Beginner]`

**🎴 FRONT**

```
🖥️  → 'Hello, Dojo!'
```

```python
print("Hello, Dojo!")
print("Honor:", 42)
```

**🔄 BACK**

*Your first voice in code. Terminal listens when you speak.*

🎯 Try it: Print your own name and your city in two separate print() calls.

***

### 🟢 3 — String  `[Beginner]`

**🎴 FRONT**

```
"hello" ← quotes = text
```

```python
greeting = "Dojo"
full = "Hello " + greeting
```

**🔄 BACK**

*Text wrapped in quotes. Words are data too.*

🎯 Try it: Create a variable `dojo_name` with your dojo's name. Concatenate it with 'Welcome to '.

***

### 🟢 4 — Integer & Float  `[Beginner]`

**🎴 FRONT**

```
42 = int  ·  3.14 = float
```

```python
honor = 240
confidence = 0.75
```

**🔄 BACK**

*Whole vs. fractional. Honor points are integers; mastery is a float.*

🎯 Try it: Create `honor = 50`. Multiply it by 1.5. Print the result. What type is it now?

***

### 🟢 5 — Boolean  `[Beginner]`

**🎴 FRONT**

```
True ● ○ False
```

```python
is_ready = True
is_done = False
print(type(is_ready))
```

**🔄 BACK**

*Binary heartbeat. Every decision reduces to True or False.*

🎯 Try it: Type `print(5 > 3)` and `print(5 < 3)`. What do you get? Why?

***

### 🟢 6 — If / Else  `[Beginner]`

**🎴 FRONT**

```
honor > 100?
  ✅ yes → level_up()
  ❌ no  → keep_going()
```

```python
if honor > 100:
    level_up()
else:
    keep_going()
```

**🔄 BACK**

*The dojo chooses its own path. Decision branches are forks in the road.*

🎯 Try it: Write an if/else that prints 'Apprentice' if honor >= 50, else prints 'Initiate'.

***

### 🟡 7 — For Loop  `[Intermediate]`

**🎴 FRONT**

```
skills = ['git','py','json']
  → git
  → py
  → json
```

```python
skills = ['git', 'py', 'json']
for s in skills:
    print('Practicing:', s)
```

**🔄 BACK**

*The dojo drill. Repetition with purpose — each rep builds a layer.*

🎯 Try it: Create a list of 3 things you want to learn. Loop through and print each one.

***

### 🟡 8 — While Loop  `[Intermediate]`

**🎴 FRONT**

```
while honor < 100:
  ↻ train()
```

```python
honor = 0
while honor < 50:
    honor += 10
    print('Honor:', honor)
```

**🔄 BACK**

*Loops until the condition breaks. Persistence in code form.*

🎯 Try it: Write a while loop that doubles a number starting at 1 until it exceeds 100. Count the steps.

***

### 🟡 9 — Function (def)  `[Intermediate]`

**🎴 FRONT**

```
def greet(name)
  input → logic → output
```

```python
def greet(name):
    return 'Hello, ' + name

print(greet('David'))
```

**🔄 BACK**

*Jeet Kune Do: write once, strike infinitely. Maximum efficiency.*

🎯 Try it: Write a function `add_honor(current, points)` that returns the new total. Call it 3 times.

***

### 🟡 10 — List  `[Intermediate]`

**🎴 FRONT**

```
[ 'git', 'py', 'json' ]
  0      1     2
```

```python
tools = ['git', 'python', 'json']
tools.append('html')
print(tools[0])
```

**🔄 BACK**

*A dojo roster. Ordered, indexable, growable.*

🎯 Try it: Make a list of your top 3 skills. Append a 4th. Print the length with len().

***

### 🟡 J — Dictionary  `[Intermediate]`

**🎴 FRONT**

```
{ 'skill': 'git'
  'level': 3 }
```

```python
player = {'name': 'David', 'rank': 'Adept'}
print(player['rank'])
player['honor'] = 90
```

**🔄 BACK**

*The character sheet. Keys unlock values — like a map of your skills.*

🎯 Try it: Build a dict with your name, city, and one skill. Add a 'level' key set to 1.

***

### 🔴 Q — Import  `[Advanced]`

**🎴 FRONT**

```
import json
  └─ borrowed mastery
```

```python
import json
import os
from pathlib import Path
```

**🔄 BACK**

*Calling in a specialist. The open-source community is your extended dojo.*

🎯 Try it: `import math` then print `math.pi` and `math.sqrt(144)`. What are the results?

***

### 🔴 K — Class  `[Advanced]`

**🎴 FRONT**

```
class Player:
  blueprint
    ↓
  p = Player()
  instance
```

```python
class Player:
    def __init__(self, name):
        self.name = name
        self.honor = 0

p = Player('David')
print(p.name)
```

**🔄 BACK**

*The franchise model. Class = blueprint. Object = your neighborhood bakery.*

🎯 Try it: Add an `add_honor(pts)` method to the Player class. Create a player and call it twice.

***

## JSON 📦

**Suit of Memory.** JSON is how programs remember, communicate, and persist.

| Tier | Cards | Learning Outcome |
|------|-------|------------------|
| 🟢 Beginner | A–6 | JSON syntax rules, objects, arrays, types |
| 🟡 Intermediate | 7–J | Nested data, loads/dumps, file read/write |
| 🔴 Advanced | Q–K | Stable IDs, data-driven mission architecture |

***

### 🟢 A — What is JSON?  `[Beginner]`

**🎴 FRONT**

```
{ "key": "value" }
Universal trade language
```

```python
{
  "name": "David",
  "rank": "Apprentice"
}
```

**🔄 BACK**

*The fiat currency of data exchange. Every system speaks JSON.*

🎯 Try it: Spot the error: `{'name': 'David'}` — why won't this work as JSON? (hint: quote style)

***

### 🟢 2 — Object (curly braces)  `[Beginner]`

**🎴 FRONT**

```
{ } = object
"key": value inside
```

```python
{
  "player": "David",
  "honor": 240
}
```

**🔄 BACK**

*Your save file. Curly braces hold your character's entire state.*

🎯 Try it: Write a JSON object for yourself: name, city, one skill, and honor points set to 0.

***

### 🟢 3 — Array (square brackets)  `[Beginner]`

**🎴 FRONT**

```
[ "git", "python", "html" ]
  0       1         2
```

```python
{
  "skills": ["git", "python", "json"]
}
```

**🔄 BACK**

*A skill inventory. Ordered, indexed, ready to iterate.*

🎯 Try it: Add a JSON array called 'completed_missions' with 3 mission IDs (use stable string IDs, not numbers).

***

### 🟢 4 — String Values  `[Beginner]`

**🎴 FRONT**

```
"always" double quotes
not 'single'
```

```python
{ "name": "David", "city": "SLC" }
```

**🔄 BACK**

*JSON is strict. Double quotes only — no exceptions. Discipline is a feature.*

🎯 Try it: Find 2 errors: `{name: 'David', 'city': "SLC"}` and fix them.

***

### 🟢 5 — Number Values  `[Beginner]`

**🎴 FRONT**

```
{ "honor": 240 }
no quotes on numbers
```

```python
{
  "honor": 240,
  "confidence": 0.75
}
```

**🔄 BACK**

*Raw numbers speak plainly — no quotation needed. Truth doesn't need decoration.*

🎯 Try it: Which is wrong? `{"score": 100}` or `{"score": "100"}` — when does it matter?

***

### 🟢 6 — Boolean & Null  `[Beginner]`

**🎴 FRONT**

```
true / false (lowercase!)
null = empty vessel
```

```python
{
  "active": true,
  "retired": false,
  "mentor": null
}
```

**🔄 BACK**

*Lowercase in JSON — not Python's True/False. A small difference that breaks everything.*

🎯 Try it: Convert this Python dict to valid JSON by hand: `{'active': True, 'data': None}`

***

### 🟡 7 — Nested Object  `[Intermediate]`

**🎴 FRONT**

```
{ "player":
    { "name": "David"
      "rank": "Adept" } }
```

```python
{
  "player": {
    "name": "David",
    "skills": {"git": 3, "python": 4}
  }
}
```

**🔄 BACK**

*Objects inside objects. Genealogy of data — tracing lineage through nested layers.*

🎯 Try it: Access the git skill level from the snippet above using Python. Write the full path: `data['player']['skills']['git']`

***

### 🟡 8 — json.loads()  `[Intermediate]`

**🎴 FRONT**

```
string → 🔓 → dict
json.loads(text)
```

```python
import json
text = '{"honor": 90}'
data = json.loads(text)
print(data["honor"])
```

**🔄 BACK**

*Decoding a message. Raw text becomes a living Python structure.*

🎯 Try it: Take a JSON string `'{"level": 3}'`, parse it, and print the value plus 1.

***

### 🟡 9 — json.dumps()  `[Intermediate]`

**🎴 FRONT**

```
dict → 🔒 → string
json.dumps(data)
```

```python
import json
data = {'rank': 'Adept'}
text = json.dumps(data, indent=2)
print(text)
```

**🔄 BACK**

*Encoding for travel. Python dict becomes portable JSON text.*

🎯 Try it: Create a Python dict of your skills, convert to JSON string with indent=2, and print it.

***

### 🟡 10 — Read JSON File  `[Intermediate]`

**🎴 FRONT**

```
📂 save.json
  → json.load(f)
  → dict in memory
```

```python
import json
with open("save.json", "r") as f:
    data = json.load(f)
print(data)
```

**🔄 BACK**

*Reading institutional memory. The dojo remembers who trained and when.*

🎯 Try it: Create a file `test.json` with `{"name": "you"}`. Write Python to read and print the name.

***

### 🟡 J — Write JSON File  `[Intermediate]`

**🎴 FRONT**

```
dict in memory
  → json.dump(f)
  → 💾 save.json
```

```python
import json
data = {"honor": 50, "rank": "Initiate"}
with open("save.json", "w") as f:
    json.dump(data, f, indent=2)
```

**🔄 BACK**

*Writing your legacy to disk. Progress that survives closing the terminal.*

🎯 Try it: Save your own player dict to a file. Close Python. Reopen and read it back. Did it persist?

***

### 🔴 Q — Stable ID Pattern  `[Advanced]`

**🎴 FRONT**

```
"id": "git-branching"
not "id": 3
IDs never change. Numbers do.
```

```python
{
  "id": "git-branching",
  "number": 6,
  "title": "Git Branching"
}
```

**🔄 BACK**

*Names outlive positions. A dojo belt has a name, not just a number in line.*

🎯 Try it: Refactor a save file that uses `'completed': [1,3,5]` to use stable string IDs. Why is this safer?

***

### 🔴 K — JSON as Mission Pack  `[Advanced]`

**🎴 FRONT**

```
missions.json
  engine.py loads ↗
  educators edit ↗
  no Python needed
```

```python
[
  {
    "id": "py-variables",
    "skill": "python",
    "challenge": "Assign 42 to seed",
    "answer": "seed = 42"
  }
]
```

**🔄 BACK**

*Content separated from engine. Anyone can add missions — coders, teachers, community members.*

🎯 Try it: Write a new mission card in JSON for a concept YOU learned this week. Share it as a PR.

***

## JAVASCRIPT & HTML 🌐

**Suit of Expression.** HTML gives structure; JavaScript gives behavior.

| Tier | Cards | Learning Outcome |
|------|-------|------------------|
| 🟢 Beginner | A–6 | HTML boilerplate, headings, text, links, images, divs |
| 🟡 Intermediate | 7–J | JS variables, functions, if/else, DOM, events |
| 🔴 Advanced | Q–K | Fetch API, debugging with console |

***

### 🟢 A — HTML Boilerplate  `[Beginner]`

**🎴 FRONT**

```
<!DOCTYPE html>
<html>
  <head>🧠</head>
  <body>👁️</body>
</html>
```

```js
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>Dojo</title>
</head>
<body>
  <h1>Hello, Dojo!</h1>
</body>
</html>
```

**🔄 BACK**

*The skeleton every page is built on. Structure before style.*

🎯 Try it: Create `index.html` with this boilerplate. Add your name in an <h1>. Open it in a browser.

***

### 🟢 2 — Heading Tags  `[Beginner]`

**🎴 FRONT**

```
<h1> BIG
<h2> Medium
<h3> smaller
<h6> tiny
```

```js
<h1>The Dojo</h1>
<h2>Python Suit</h2>
<h3>Variables</h3>
```

**🔄 BACK**

*Six levels of hierarchy. Structure is meaning — headings tell the browser what matters most.*

🎯 Try it: Build an outline of this card deck using h1 for the deck name and h2 for each suit.

***

### 🟢 3 — Paragraph & Text Tags  `[Beginner]`

**🎴 FRONT**

```
<p>block of text</p>
<strong>bold</strong>
<em>italic</em>
```

```js
<p>Welcome to the <strong>Dojo</strong>.</p>
<p><em>Practice daily.</em></p>
```

**🔄 BACK**

*Words need homes. Paragraphs give text breathing room and meaning.*

🎯 Try it: Write a 2-sentence paragraph about why you're learning to code. Bold one key word.

***

### 🟢 4 — Link Tag  `[Beginner]`

**🎴 FRONT**

```
<a href="url">
  Click ← anchor text
</a>
```

```js
<a href="https://github.com">GitHub</a>
<a href="index.html">Home</a>
```

**🔄 BACK**

*The hyperlink — the web's most powerful primitive. One tag connects the whole internet.*

🎯 Try it: Add a link in your HTML to the Dojo Ascension GitHub repo. Open it. Does it work?

***

### 🟢 5 — Image Tag  `[Beginner]`

**🎴 FRONT**

```
<img src="🖼️" alt="desc">
self-closing · alt = required
```

```js
<img src="dojo.png" alt="Dojo crest">
<img src="logo.svg" alt="Logo" width="200">
```

**🔄 BACK**

*Alt text is respect for all learners — screen readers depend on it.*

🎯 Try it: Add an image to your page. What happens if you misspell the src? What does the alt text show?

***

### 🟢 6 — div & span  `[Beginner]`

**🎴 FRONT**

```
<div> = 📦 block (full row)
<span> = 🔤 inline (within text)
```

```js
<div class='card'>
  <span class='rank'>A</span>
  <span class='suit'>🐍</span>
</div>
```

**🔄 BACK**

*Rooms and words inside rooms. divs structure layout; spans style specific words.*

🎯 Try it: Wrap three card titles in divs with class='card'. Style them with a border using inline CSS.

***

### 🟡 7 — JS Variables  `[Intermediate]`

**🎴 FRONT**

```
let = changeable 🔄
const = fixed 🔒
var = avoid (old)
```

```js
let rank = 'Apprentice';
const MAX_HONOR = 500;
rank = 'Practitioner'; // ✅
MAX_HONOR = 600;      // ❌ Error
```

**🔄 BACK**

*let changes, const never does. Name your constraints — it prevents bugs.*

🎯 Try it: Open browser console (F12). Declare a `let` and change it. Try changing a `const`. What error appears?

***

### 🟡 8 — JS Function  `[Intermediate]`

**🎴 FRONT**

```
function name(input) {
  // logic
  return output;
}
```

```js
function addHonor(current, pts) {
  return current + pts;
}
console.log(addHonor(50, 10));
```

**🔄 BACK**

*Same Jeet Kune Do principle — write once, use anywhere. JS uses {} instead of indentation.*

🎯 Try it: Write a JS function `greetPlayer(name, rank)` that returns 'Hello [name], rank [rank]'.

***

### 🟡 9 — JS If/Else  `[Intermediate]`

**🎴 FRONT**

```
if (honor > 100) {
  ✅ unlock()
} else {
  ❌ train()
}
```

```js
let honor = 120;
if (honor > 100) {
  console.log('Rank up!');
} else {
  console.log('Keep training.');
}
```

**🔄 BACK**

*Same decision logic as Python — curly braces replace indentation. The thought is identical.*

🎯 Try it: Write an if/else/else-if in JS that prints a rank name based on honor: <50 Initiate, <100 Apprentice, else Practitioner.

***

### 🟡 10 — DOM Select  `[Intermediate]`

**🎴 FRONT**

```
HTML element
   ↑
document.querySelector('#id')
   ↑
JS control
```

```js
const card = document.querySelector('#card-1');
const allCards = document.querySelectorAll('.card');
console.log(card.textContent);
```

**🔄 BACK**

*The bridge between HTML and JS. Select an element, then control it.*

🎯 Try it: In your browser console, run `document.querySelector('h1').textContent`. What do you see? Change it.

***

### 🟡 J — Event Listener  `[Intermediate]`

**🎴 FRONT**

```
btn 🖱️ click
  → function fires
  → page responds
```

```js
const btn = document.querySelector('#flip-btn');
btn.addEventListener('click', () => {
  card.classList.toggle('flipped');
});
```

**🔄 BACK**

*Code that waits, then responds. Reactive thinking — don't act until the moment calls.*

🎯 Try it: Add a button to your HTML. Write JS so clicking it toggles 'visible' class on a hidden div.

***

### 🔴 Q — Fetch API  `[Advanced]`

**🎴 FRONT**

```
fetch(url)
  .then(→ parse)
  .then(→ use data)
```

```js
fetch('data/deck.json')
  .then(r => r.json())
  .then(cards => {
    console.log(cards.length);
  });
```

**🔄 BACK**

*The JS version of Python's `requests`. Pull data from anywhere without reloading the page.*

🎯 Try it: Fetch `dojo_52_card_deck.json` locally. Log the first card's `concept` field to the console.

***

### 🔴 K — console.log() & Debugging  `[Advanced]`

**🎴 FRONT**

```
console.log() → F12 console
console.error() → red alert
console.table() → formatted
```

```js
const player = {name:'David', honor:90};
console.log('Player:', player);
console.table(player);
```

**🔄 BACK**

*The print() of JavaScript. Your debug voice in the browser. Master this before anything else.*

🎯 Try it: Open any webpage. In the console, type `console.table(document.querySelectorAll('a'))`. What do you see?

***

## GITHUB WORKFLOWS 🔀

**Suit of Chronicle.** Git tracks every change. History is accountability.

| Tier | Cards | Learning Outcome |
|------|-------|------------------|
| 🟢 Beginner | A–7 | clone, init, status, add, commit, push, pull |
| 🟡 Intermediate | 8–J | Branching, merging, pull requests, README |
| 🔴 Advanced | Q–K | GitHub Actions, stable IDs in save files |

***

### 🟢 A — git clone  `[Beginner]`

**🎴 FRONT**

```
☁️ GitHub repo
     ↓ git clone
💻 local copy
```

```python
git clone https://github.com/user/repo.git
cd repo
ls
```

**🔄 BACK**

*Your first step onto the mat. Downloads the dojo to your machine.*

🎯 Try it: Clone the Dojo Ascension repo. Navigate into it. Run `ls` and name 3 files you see.

***

### 🟢 2 — git init  `[Beginner]`

**🎴 FRONT**

```
📁 my-project/
  git init
    ↓
  📁 .git/ created
```

```python
mkdir my-dojo
cd my-dojo
git init
ls -a
```

**🔄 BACK**

*Founding a new dojo. The .git folder is your chronicle's spine.*

🎯 Try it: Create a new folder, run `git init`, then `ls -a`. Can you see the hidden `.git` directory?

***

### 🟢 3 — git status  `[Beginner]`

**🎴 FRONT**

```
🔴 untracked
🟡 staged
🟢 committed
```

```python
git status
# On branch main
# Untracked files:
#   new_file.py
```

**🔄 BACK**

*Know your terrain before you move. A scout always checks the field first.*

🎯 Try it: Create a new file in your repo. Run `git status`. What color/label does it show?

***

### 🟢 4 — git add  `[Beginner]`

**🎴 FRONT**

```
untracked file
  git add .
    ↓
  staged (ready)
```

```python
git add .          # stage everything
git add README.md  # stage one file
git status         # confirm
```

**🔄 BACK**

*Prepare your offering before committing. Stage is your review moment.*

🎯 Try it: Stage only ONE specific file (not `.`). Run `git status`. Notice the difference.

***

### 🟢 5 — git commit  `[Beginner]`

**🎴 FRONT**

```
📸 snapshot
git commit -m "message"
     ↓
  logged to history
```

```python
git commit -m "feat: add card deck module"
# present tense, imperative mood
# "add" not "added"
```

**🔄 BACK**

*The journalist's dateline. A commit is a timestamped, immutable statement of fact.*

🎯 Try it: Commit your staged file. Then run `git log --oneline`. Read your own history.

***

### 🟢 6 — git push  `[Beginner]`

**🎴 FRONT**

```
💻 local commits
  git push
    ↓
  ☁️ GitHub updated
```

```python
git push origin main
git push           # if upstream set
```

**🔄 BACK**

*Publishing your chronicle. Your work becomes visible to the community.*

🎯 Try it: Push a commit to GitHub. Refresh the repo page. Can you see your commit message online?

***

### 🟢 7 — git pull  `[Beginner]`

**🎴 FRONT**

```
☁️ new commits exist
  git pull
    ↓
  💻 local updated
```

```python
git pull            # fetch + merge
git pull origin main
```

**🔄 BACK**

*Staying current with the community. A practitioner keeps their knowledge fresh.*

🎯 Try it: Make a change on GitHub.com directly. Then pull it to your local machine. Confirm the change appeared.

***

### 🟡 8 — Branch  `[Intermediate]`

**🎴 FRONT**

```
main ───●───●───●
         \
          ●───● feature
```

```python
git checkout -b feature/card-deck
git branch        # list branches
git switch main   # return to main
```

**🔄 BACK**

*R&D in isolation. Wing Chun: deflect risk to a side branch so experiments can't crash production.*

🎯 Try it: Create a branch named `feature/your-name`. Add a file. Commit it. Switch back to main. Is the file still there?

***

### 🟡 9 — Merge  `[Intermediate]`

**🎴 FRONT**

```
main ───●───●───●──●
         \       /
          ●───●
```

```python
git switch main
git merge feature/card-deck
git log --oneline --graph
```

**🔄 BACK**

*Returning force to the trunk. Wing Chun redirect — the experiment rejoins the main flow.*

🎯 Try it: Merge your feature branch into main. Run `git log --oneline --graph`. Draw what you see.

***

### 🟡 10 — Pull Request  `[Intermediate]`

**🎴 FRONT**

```
feature branch
  → 🔍 PR opened
  → 👥 reviewed
  → ✅ merged to main
```

```python
# On GitHub:
# 1. Push branch
# 2. Open Pull Request
# 3. Add description
# 4. Request review
# 5. Merge
```

**🔄 BACK**

*The digital tatami mat. Code review is mutual growth — the gentle art of making each other better.*

🎯 Try it: Push a feature branch to GitHub. Open a PR. Write a 2-sentence description of what it changes and why.

***

### 🟡 J — README.md  `[Intermediate]`

**🎴 FRONT**

```
# Project Title
## What it does
## How to run
## How to contribute
```

```python
# Dojo Ascension
A terminal learning game.

## Run
```bash
python dojo.py
```

## Contributing
See CONTRIBUTING.md
```

**🔄 BACK**

*A project's front door. The README is the first impression — make it welcoming.*

🎯 Try it: Write a one-paragraph README for a project you're working on. Include 'What it does' and 'How to run'.

***

### 🔴 Q — GitHub Actions  `[Advanced]`

**🎴 FRONT**

```
on: push
  jobs:
    test:
      → auto-runs
      → ✅ or ❌
```

```python
# .github/workflows/test.yml
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: python -m pytest
```

**🔄 BACK**

*Your automated sensei. Tests run on every push without you asking — the dojo that never sleeps.*

🎯 Try it: Add a GitHub Actions workflow that runs `echo 'Dojo tests passing'` on every push. Watch it succeed.

***

### 🔴 K — Stable ID in Save  `[Advanced]`

**🎴 FRONT**

```
✅ completed: ['git-clone', 'py-vars']
❌ completed: [1, 3, 5]
IDs survive refactoring. Numbers don't.
```

```python
# save.json
{
  "player": "David",
  "rank": "Adept",
  "completed": [
    "git-clone",
    "py-variables",
    "json-objects"
  ]
}
```

**🔄 BACK**

*Names outlive positions. The dojo chronicle references practitioners by name, not row number.*

🎯 Try it: Open your save file. If it uses numbers, refactor to string IDs. Commit the change with a clear message explaining why.

***

## Rank Unlock Requirements

| Rank | Gate |
|------|------|
| Initiate | Identify 5 cards by concept in any suit |
| Apprentice | Master all 🟢 Beginner cards (Ace–6 or 7) in Python |
| Practitioner | Master all 🟢 Beginner cards across all 4 suits |
| Adept | Master all 🟡 Intermediate cards in at least 2 suits |
| Expert | Master all 52 cards |
| Co-Architect | Teach any 10 cards to another learner. Explain the exercise, not just the answer. |

***

## Integration with `missions.json` & Save File

Each card has a stable `id` field. Reference it in your save file:

```json
{
  "player": "David",
  "rank": "Practitioner",
  "mastered_cards": [
    "card-python-a",
    "card-python-2",
    "card-json-a",
    "card-git-4"
  ]
}
```

> ⚡ Build `card_deck.py` as a separate module that loads `dojo_52_card_deck_v2.json` — keep content out of the engine, so educators can add cards without touching Python.
