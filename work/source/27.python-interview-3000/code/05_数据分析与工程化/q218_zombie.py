import subprocess
import sys


def run_and_reap(cmd: list[str]) -> int:
    # 正确收尸:communicate 会 wait,避免僵尸
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL)
    proc.wait()
    return proc.returncode


def test_no_zombie():
    code = run_and_reap([sys.executable, "-c", "print(1)"])
    assert code == 0
