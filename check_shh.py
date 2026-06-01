import subprocess

def main():
    result = subprocess.run(
        ["systemctl", "is-active", "ssh"],
        capture_output= True,
        text=True
        )
    
    while result.stdout.strip() != "active":
        try:
            subprocess.run(
                ["systemctl", "start", "ssh"]
            )
        except Exception as e:
            raise Exception(f"Error: Cant continue because of: {e}")
    
    print("SSH service is running")




if __name__ == "__main__":
    main()