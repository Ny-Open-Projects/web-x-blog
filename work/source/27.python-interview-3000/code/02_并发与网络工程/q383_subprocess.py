"""subprocess 安全调用示例(跨平台均可运行)。"""
import subprocess
import sys


def safe_run(cmd: list, timeout=10):
    result = subprocess.run(
        cmd,
        capture_output=True,  # 等价 stdout+stderr=PIPE
        text=True,
        timeout=timeout,
        check=True,           # 非零退出码抛 CalledProcessError
    )
    return result.stdout


def unsafe_example(user_input: str):
    """错误示范(仅注释说明,不执行):
    subprocess.run(f"echo {user_input}", shell=True)
    user_input='hello; rm -rf ~' 时会发生灾难。
    """
    pass


if __name__ == "__main__":
    # 参数列表传递,用户输入不会被 shell 二次解释
    out = safe_run([sys.executable, "-c", "print(1+1)"])
    print("计算结果:", out.strip())

    try:
        safe_run([sys.executable, "-c", "import sys; sys.exit(3)"])
    except subprocess.CalledProcessError as e:
        print("非零退出被感知, returncode =", e.returncode)

    try:
        safe_run([sys.executable, "-c", "import time; time.sleep(30)"], timeout=1)
    except subprocess.TimeoutExpired as e:
        print("超时被杀死, timeout =", e.timeout)
