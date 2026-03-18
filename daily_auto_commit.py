import os
import random
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = "/home/ubuntu/contribution-hub"
LOG_FILE = "activity.log"

# English commit messages
MESSAGES = [
    "Daily update: refine project logs",
    "Maintenance: update documentation",
    "Feature: add new entry to activity log",
    "Optimization: clean up log structure",
    "Routine: sync daily progress"
]

def make_commit():
    """Creates a commit with the current date and time."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")
    message = random.choice(MESSAGES)
    
    # Update the log file
    with open(os.path.join(REPO_PATH, LOG_FILE), "a") as f:
        f.write(f"[{date_str}] {message}\n")
    
    try:
        # Git operations
        subprocess.run(["git", "add", "."], cwd=REPO_PATH, check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=REPO_PATH, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=REPO_PATH, check=True)
        print(f"[{date_str}] Successfully pushed: {message}")
    except subprocess.CalledProcessError as e:
        print(f"[{date_str}] Error during git operation: {e}")

def main():
    # Random number of commits for today (2 to 6)
    num_commits = random.randint(2, 6)
    print(f"Starting daily task: generating {num_commits} commits...")
    
    for i in range(num_commits):
        make_commit()

if __name__ == "__main__":
    main()
