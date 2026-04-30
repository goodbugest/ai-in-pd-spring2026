# Local Setup Guide: VS Code + Python on Your Laptop

**ME 493B — AI in Product Development, Spring 2026**

The backup path when Codespaces isn't an option — storage limit hit, billing reset, outage, weak WiFi, or just preference. Set up once, then everything works the same as Codespaces. Budget about 30 minutes the first time. After that, opening the project takes a few seconds.

---

## When to use this guide

- You hit your monthly Codespaces quota (15 GB-month or 120 core-hours on free accounts)
- Codespaces is down or laggy
- You want to work offline
- You prefer your local environment
- You're doing MP3 Part B — running an MCP server is **easier locally** because the AI host (Copilot agent mode, Claude Desktop, Cursor) and your server are on the same machine

You can switch between local and Codespaces freely. The repo and submission process are identical.

---

## What you'll set up

- Python 3.11 or newer
- Git (probably already installed)
- VS Code with the Python, Jupyter, and GitHub Copilot extensions
- A local clone of your course repo
- A Python virtual environment with course dependencies
- A `.env` file with your GitHub Models token

Total disk footprint: ~1.5 GB.

---

## Step 1: Install Python 3.11+

Check first — you may already have it:

```bash
python3 --version    # Mac/Linux
python --version     # Windows
```

If you see `Python 3.11.x` or higher, skip to Step 2.

**Windows:** Download from [python.org/downloads](https://python.org/downloads). On the first installer screen, **check "Add python.exe to PATH"** before clicking Install. This is the most common setup mistake.

**Mac:** Download from [python.org/downloads](https://python.org/downloads), or if you have Homebrew: `brew install python@3.11`.

**Linux (Ubuntu/Debian):** `sudo apt install python3.11 python3.11-venv python3-pip`.

---

## Step 2: Install Git

Check first:

```bash
git --version
```

If you see a version, skip to Step 3.

**Windows:** Download from [git-scm.com](https://git-scm.com). Accept all defaults.

**Mac:** Run `git --version` in Terminal — macOS will offer to install the Xcode Command Line Tools, which includes Git. Accept.

**Linux:** `sudo apt install git`.

If this is your first time using Git on this machine, set your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@uw.edu"
```

---

## Step 3: Install VS Code + extensions

Download from [code.visualstudio.com](https://code.visualstudio.com).

Open VS Code and install these extensions (Extensions sidebar icon, or `Ctrl+Shift+X` / `Cmd+Shift+X`):

- **Python** (Microsoft)
- **Jupyter** (Microsoft)
- **GitHub Copilot** (GitHub)
- **GitHub Copilot Chat** (GitHub)

---

## Step 4: Clone your repo

```bash
cd ~                                                    # or wherever you keep code
git clone https://github.com/YOUR-USERNAME/ai-in-pd-spring2026.git
cd ai-in-pd-spring2026
```

Replace `YOUR-USERNAME` with your GitHub username.

Add the upstream remote so you can pull new course content as the quarter progresses:

```bash
git remote add upstream https://github.com/dr-thielman/ai-in-pd-spring2026.git
git remote -v
```

You should see both `origin` (your repo) and `upstream` (the instructor's repo). You only do this once.

---

## Step 5: Create a virtual environment and install dependencies

From inside the repo folder:

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

Install takes 2–5 minutes. The `.venv/` folder is in `.gitignore` and won't be pushed.

You'll need to activate the venv each time you open a new terminal in this folder — but VS Code does it automatically once you select the interpreter (Step 6).

---

## Step 6: Open in VS Code and pick the interpreter

```bash
code .
```

In VS Code:

1. Open any `.ipynb` file (try `hello_world.ipynb`)
2. Top-right of the notebook → "Select Kernel" → "Python Environments" → choose the one in `.venv`
3. Sign in to GitHub via the account icon in the bottom-left. This also activates GitHub Copilot Pro using your Student Developer Pack.

---

## Step 7: Create your `.env` file

In the repo root, create a file named exactly `.env` with one line:

```
GITHUB_TOKEN=ghp_YOUR_TOKEN_HERE
```

Easiest way: in VS Code → File → New File → save as `.env` in the repo root.

Use the same Personal Access Token you created for MP2 (with `models:read` scope). If you've lost it, generate a new one at [github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens).

**`.env` is already in `.gitignore`** — it will not be pushed to GitHub. Do not commit your token.

---

## Step 8: Verify

Open `hello_world.ipynb`, click "Run All" at the top of the notebook (or `Ctrl+Shift+P` → "Run All Cells"). All cells should execute without errors.

For any MP that hits the GitHub Models API, the first cell that reads `GITHUB_TOKEN` should succeed and print confirmation.

---

## Submitting work

Identical to Codespaces. From the repo folder:

```bash
git add -A
git commit -m "MP2 Part A complete"
git push origin main
```

Or use VS Code's Source Control panel (branch icon in the sidebar) → stage all → enter message → Commit → Sync Changes.

Then submit your repo URL on Canvas — same URL every time.

---

## Pulling new content

```bash
git pull upstream main
```

---

## Quick reference

| Task | How |
|------|-----|
| Activate venv (Mac/Linux) | `source .venv/bin/activate` |
| Activate venv (Windows PS) | `.venv\Scripts\Activate.ps1` |
| Open VS Code in repo | `code .` |
| Run a notebook | Open `.ipynb` → click "Run All" |
| Commit + push | Source Control → ✓ → Sync, or `git push origin main` |
| Pull new content | `git pull upstream main` |

---

## Troubleshooting

**Python command not found (Windows).** You missed the "Add python.exe to PATH" checkbox during install. Reinstall or add it manually via Settings → System → Environment Variables.

**`pip install` fails on `torch` or `chromadb`.** Both packages are large. Confirm you have at least 5 GB free disk space. If it still fails: `pip install --upgrade pip setuptools wheel` and retry.

**VS Code doesn't see the venv.** `Ctrl+Shift+P` (Cmd+Shift+P on Mac) → "Python: Select Interpreter" → choose the one in `.venv`.

**Copilot doesn't work.** Check your Student Developer Pack is approved at [github.com/settings/copilot](https://github.com/settings/copilot) and that you're signed in to GitHub in VS Code (bottom-left).

**`.env` not loading.** Verify the file is named exactly `.env` — some editors and Windows File Explorer silently append `.txt`. In Windows File Explorer, enable View → File name extensions to confirm.

**Permission denied on `.venv\Scripts\Activate.ps1` (Windows).** Open PowerShell as administrator once and run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.

**Anything else.** The course Slack channel is the fastest help — most classmates will run into the same things, and answers compound.
