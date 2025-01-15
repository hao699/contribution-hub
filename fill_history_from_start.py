import os
import random
import subprocess
from datetime import datetime, timedelta

# Configuration
REPO_PATH = "/home/ubuntu/contribution-hub"
LOG_FILE = "activity.log"
# Account created on 2025-01-13
START_DATE = datetime(2025, 1, 13)

# English commit messages
MESSAGES = [
    "Refactor module for better scalability",
    "Update project dependencies",
    "Fix minor UI issues",
    "Add new feature to the core engine",
    "Improve code documentation",
    "Optimize performance for data processing",
    "Add unit tests for utility functions",
    "Clean up legacy code",
    "Implement security patches",
    "Sync progress with remote repository"
]

def make_commit(date):
    """Creates a commit with a specific date."""
    date_str = date.strftime("%Y-%m-%d %H:%M:%S")
    message = random.choice(MESSAGES)
    
    # Update a log file to have something to commit
    with open(os.path.join(REPO_PATH, LOG_FILE), "a") as f:
        f.write(f"[{date_str}] {message}\n")
    
    # Set environment variables for git commit date
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    subprocess.run(["git", "add", "."], cwd=REPO_PATH, check=True)
    subprocess.run(["git", "commit", "-m", message], cwd=REPO_PATH, env=env, check=True)

def main():
    current_date = START_DATE
    end_date = datetime.now()
    
    print(f"Starting to fill history from {START_DATE.date()} to {end_date.date()}...")
    
    while current_date <= end_date:
        # Randomly decide if we should commit on this day (85% chance for higher density)
        if random.random() < 0.85:
            # Random number of commits per day (2 to 6)
            num_commits = random.randint(2, 6)
            for _ in range(num_commits):
                # Random time during the day
                hour = random.randint(0, 23)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                commit_time = current_date.replace(hour=hour, minute=minute, second=second)
                
                if commit_time <= end_date:
                    make_commit(commit_time)
        
        current_date += timedelta(days=1)
    
    print("Full history generation completed successfully.")

if __name__ == "__main__":
    main()
