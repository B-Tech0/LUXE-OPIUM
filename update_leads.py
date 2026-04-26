import pandas as pd
import json
import os
import subprocess
from datetime import datetime

LEADS_FILE = 'leads.json'
EXCEL_FILE = 'leads.xlsx'

def update_excel():
    if not os.path.exists(LEADS_FILE):
        print(f"{LEADS_FILE} not found. Creating empty Excel.")
        df = pd.DataFrame(columns=['email', 'phone', 'timestamp'])
    else:
        with open(LEADS_FILE, 'r') as f:
            try:
                data = json.load(f)
                df = pd.DataFrame(data)
            except json.JSONDecodeError:
                print("Error decoding JSON. Creating empty Excel.")
                df = pd.DataFrame(columns=['email', 'phone', 'timestamp'])

    df.to_excel(EXCEL_FILE, index=False)
    print(f"Updated {EXCEL_FILE}")

def commit_to_github():
    try:
        # Add files
        subprocess.run(['git', 'add', LEADS_FILE, EXCEL_FILE], check=True)
        
        # Check if there are changes to commit
        status = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if not status.stdout.strip():
            print("No changes to commit.")
            return

        # Commit
        commit_msg = f"Update leads Excel - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
        
        # Push
        subprocess.run(['git', 'push'], check=True)
        print("Successfully pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operations: {e}")

if __name__ == "__main__":
    update_excel()
    commit_to_github()
