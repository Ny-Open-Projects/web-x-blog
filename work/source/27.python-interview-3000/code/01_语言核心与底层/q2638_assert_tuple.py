"""assert 元组陷阱与 -O 模式实测。"""
import subprocess
import sys


def check(x):
    assert (x > 0, "x 必须为正")      # 陷阱:非空元组恒真,永不触发
    # 正确写法:assert x > 0, "x 必须为正"(逗号在 assert 语法层,不在括号里)
    return x * 2


if __name__ == "__main__":
    print("check(-5) 竟然通过:", check(-5))

    code = "assert False, 'gone'\nprint('survived')"
    r_off = subprocess.run([sys.executable, "-O", "-c", code],
                           capture_output=True, text=True)
    r_on = subprocess.run([sys.executable, "-c", code],
                          capture_output=True, text=True)
    print("-O 模式退出码:", r_off.returncode, "输出:", r_off.stdout.strip())
    print("默认模式退出码:", r_on.returncode, "消息:", r_on.stderr.strip().splitlines()[-1])
