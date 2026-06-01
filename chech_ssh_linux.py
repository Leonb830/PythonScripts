import subprocess
from typing import Optional
ACTIVE = "active"

def run_subprocess(*args):
    return subprocess.run(
        ["sudo", "systemctl", *args, "ssh"],
        capture_output=True,
        text=True,
    )

def main():
    result = run_subprocess("status")
    status = result.stdout.strip() 
    
    if status == ACTIVE:
        print("SSH service is running")
        return
    else:
        run_subprocess("start")

   