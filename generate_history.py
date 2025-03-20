import os
import random
import subprocess
from datetime import datetime, timedelta

# Configuration
REPO_PATH = "/home/ubuntu/contribution-hub"
LOG_FILE = "activity.log"
START_DATE = datetime.now() - timedelta(days=365)

# English commit messages
MESSAGES = [
    "Update project documentation",
    "Refactor core logic for better performance",
    "Fix minor bugs in the utility module",
    "Add new features to the dashboard",
    "Improve code readability and structure",
    "Update dependencies to latest versions",
    "Optimize database queries",
    "Add unit tests for the authentication flow",
    "Clean up unused assets and files",
    "Implement responsive design for mobile devices"
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
    
    print(f"Starting to generate history from {START_DATE.date()} to {end_date.date()}...")
    
    while current_date <= end_date:
        # Randomly decide if we should commit on this day (80% chance)
        if random.random() < 0.8:
            # Random number of commits per day (1 to 5)
            num_commits = random.randint(1, 5)
            for _ in range(num_commits):
                # Random time during the day
                hour = random.randint(0, 23)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                commit_time = current_date.replace(hour=hour, minute=minute, second=second)
                
                if commit_time <= end_date:
                    make_commit(commit_time)
        
        current_date += timedelta(days=1)
    
    print("History generation completed successfully.")

if __name__ == "__main__":
    main()
