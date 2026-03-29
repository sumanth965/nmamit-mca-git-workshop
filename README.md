# NMAMIT MCA - Git & GitHub Workshop

Welcome to the **Git & GitHub Workshop**! This repository is your hands-on playground for learning version control like a professional software engineer.

## Workshop Details

- **Duration**: 2 Hours
- **Instructor**: Tushar Prabhu (Software Engineer)
- **Prerequisites**: GitHub account + Git CLI installed

## What You'll Learn

| Topic | Duration |
|-------|----------|
| Why Version Control? | 10 min |
| What is Git & GitHub? | 10 min |
| Fork, Clone & Setup | 10 min |
| Git Basics (add, commit, status) | 15 min |
| Branching & Merging | 15 min |
| Push, Pull & Pull Requests | 15 min |
| Merge Conflicts | 10 min |
| GitHub Actions (CI/CD) | 15 min |
| Best Practices & Interview Tips | 10 min |
| Q&A | 10 min |

## Quick Setup

```bash
# 1. Fork this repository (click the "Fork" button on GitHub)

# 2. Clone YOUR fork (replace <your-username>)
git clone https://github.com/<your-username>/nmamit-mca-git-workshop.git

# 3. Navigate into the project
cd nmamit-mca-git-workshop

# 4. Verify everything works
git status
```

## Project Structure

```
nmamit-mca-git-workshop/
├── README.md              # You are here!
├── src/
│   └── app.py             # A simple Python app
├── students/
│   └── example.md         # Example student profile
├── .github/
│   └── workflows/
│       └── welcome.yml    # GitHub Actions workflow
└── .gitignore
```

## Workshop Exercises

### Exercise 1: Your First Commit
Add your profile to the `students/` folder.

### Exercise 2: Create a Branch
Create a feature branch and make changes.

### Exercise 3: Push & Create a Pull Request
Push your branch and open a PR to your fork's `main`.

### Exercise 4: Merge Your PR
Review and merge your own pull request.

### Exercise 5: Resolve a Merge Conflict
Practice resolving a conflict scenario.

### Exercise 6: GitHub Actions
See CI/CD in action when you push code.

## Useful Git Commands Cheat Sheet

```bash
# Configuration
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Basics
git init                    # Initialize a new repo
git status                  # Check current status
git add <file>              # Stage a file
git add .                   # Stage all changes
git commit -m "message"     # Commit staged changes
git log --oneline           # View commit history

# Branching
git branch                  # List branches
git branch <name>           # Create a branch
git checkout <name>         # Switch to a branch
git checkout -b <name>      # Create + switch in one step
git merge <branch>          # Merge a branch into current

# Remote
git remote -v               # View remote URLs
git push origin <branch>    # Push to remote
git pull origin <branch>    # Pull from remote
git fetch                   # Fetch remote changes

# Undoing
git restore <file>          # Discard changes
git reset HEAD <file>       # Unstage a file
```

## Need Help?

Raise your hand or ask the instructor! No question is too basic.

---

Made with enthusiasm for **NMAMIT MCA** students.
