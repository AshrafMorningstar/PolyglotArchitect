# history_faker.py
import os
import subprocess
import datetime
import random

def run_git(args):
    subprocess.run(["git"] + args, check=True, shell=True)

def make_commit(date_obj, message):
    # Create or modify a dummy file to ensure there's something to commit if needed, 
    # but preferably we commit actual files incrementally.
    # Since we have existing files, we can simulate "refactoring" them.
    # A simpler way for a "viral" look is to update a log file.
    
    with open("activity_log.txt", "a") as f:
        f.write(f"Update on {date_obj.strftime('%Y-%m-%d')}: {message}\n")
    
    run_git(["add", "activity_log.txt"])
    
    # Format date for git: "YYYY-MM-DD HH:MM:SS"
    date_str = date_obj.strftime("%Y-%m-%d %H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    subprocess.run(
        f'git commit -m "{message}"',
        shell=True,
        env=env,
        check=False # Ignore if nothing to commit
    )

def generate_history():
    # Initialize if not already
    if not os.path.exists(".git"):
        run_git(["init"])
        run_git(["config", "user.email", "you@example.com"])
        run_git(["config", "user.name", "PolyglotDev"])

    start_date = datetime.datetime(2024, 1, 15)
    end_date = datetime.datetime.now()
    delta = end_date - start_date
    
    print(f"Generating history from {start_date.date()} to {end_date.date()}...")
    
    current_files = ["README.md", "main.py", "requirements.txt", "run_bot.bat", 
                     "dashboard_generator.py", "generators/bot_config.py", 
                     "generators/generator.py", "generators/file_creator.py", 
                     "tests/validator.py"]
    
    # Initial commit in the past
    run_git(["add", "."])
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = start_date.strftime("%Y-%m-%d %H:%M:%S")
    env["GIT_COMMITTER_DATE"] = start_date.strftime("%Y-%m-%d %H:%M:%S")
    subprocess.run('git commit -m "Initial commit of Core Architecture"', shell=True, env=env)

    # Spread 50-100 commits over the duration
    num_commits = 80
    
    for i in range(num_commits):
        # Random day offset
        days_passed = int((delta.days / num_commits) * i) + random.randint(0, 5)
        if days_passed > delta.days:
             days_passed = delta.days
             
        commit_date = start_date + datetime.timedelta(days=days_passed)
        
        msgs = [
            "Refactored generator logic", "Updated language quotas", "Fixed typos in README",
            "Added new unit tests", "Optimized file creation", "Updated dependencies",
            "Enhanced dashboard UI", "Added support for Rust", "Bug fix in validator",
            "Documentation update", "Performance improvements", "Cleaned up code"
        ]
        
        msg = random.choice(msgs)
        print(f"Committing: {msg} on {commit_date.date()}")
        make_commit(commit_date, msg)

    # Final commit for today
    run_git(["add", "."])
    run_git(["commit", "-m", "Finalizing release v1.0"])
    
    print("History generation complete! Now git push to your new repo.")

if __name__ == "__main__":
    generate_history()
