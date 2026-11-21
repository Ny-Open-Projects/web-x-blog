---
title: [Q383] subprocess 安全调用:shell=False 与参数注入
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q383 · subprocess 安全调用:shell=False 与参数注入

> 难度:★★★ | 标签:subprocess, 安全, 进程管理

**问**:`subprocess.run(cmd, shell=True)` 有什么风险?安全的调用方式是什么?

**答**:`shell=True` 把整条命令交给 shell 解释,若命令里拼了用户输入就会被注入(`; rm -rf /`)。安全姿势:①`shell=False`,命令写成列表 `["ls", "-la", path]`,参数原样传递;②`capture_output=True, text=True` 捕获输出;③显式 `timeout` 防挂死;④`check=True` 让失败抛 `CalledProcessError`;⑤尽量不用 `input=` 传敏感数据,环境变量按需最小化传给 `env=`。确实需要管道/通配符时,可用 shlex 拆分或交给专门的库。

```python
# file: code/02_并发与网络工程/q383_subprocess.py
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
```

**追问**:
- 需要执行带管道的命令怎么办?`shell=True` 且参数完全可信时才可用;否则用两个 Popen 用 `stdout=PIPE` 串联,或直接用 Python 实现。
- 如何流式读子进程输出?`Popen(..., stdout=subprocess.PIPE)` 后逐行 `for line in proc.stdout`。
