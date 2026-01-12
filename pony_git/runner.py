import subprocess
from pony_git.exceptions import GitManagerError

def run_cmd(cmd, check=True) -> None:
    try:
        subprocess.run(cmd, check=check)
    except subprocess.CalledProcessError as e:
        raise GitManagerError(f"Git command failed: {' '.join(cmd)}") from e

#! FOR 0.2.0
# def check(cmd) -> bool:
#     try:
#         subprocess.run(
#             cmd,
#             check=True,
#             stdout=subprocess.DEVNULL,
#             stderr=subprocess.DEVNULL,
#         )
#         return True
#     except subprocess.CalledProcessError:
#         return False