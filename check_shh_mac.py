import subprocess


REMOTE_LOGIN_ON = "Remote Login: On"
REMOTE_LOGIN_OFF = "Remote Login: Off"
FULL_DISK_ACCESS_ERROR = (
    "setremotelogin: Turning Remote Login on or off requires Full Disk Access privileges."
)


def run_systemsetup(*args):
    return subprocess.run(
        ["sudo", "systemsetup", *args],
        capture_output=True,
        text=True,
    )


def main():
    result = run_systemsetup("-getremotelogin")
    status = result.stdout.strip()

    if result.returncode != 0:
        raise SystemExit(f"Could not check Remote Login status:\n{result.stderr.strip()}")

    if status == REMOTE_LOGIN_ON:
        print("SSH service is running")
        return

    if status != REMOTE_LOGIN_OFF:
        raise SystemExit(f"Unexpected Remote Login status: {status}")

    result = run_systemsetup("-setremotelogin", "on")

    if result.returncode == 0:
        print("SSH service started")
        return

    error = result.stderr.strip()

    if FULL_DISK_ACCESS_ERROR in error:
        raise SystemExit(
            "Could not enable Remote Login because Terminal or your Python runner needs "
            "Full Disk Access.\n\n"
            "Open System Settings > Privacy & Security > Full Disk Access, enable the app "
            "you are running this script from, then run the script again."
        )

    raise SystemExit(f"Could not enable Remote Login:\n{error}")


if __name__ == "__main__":
    main()
