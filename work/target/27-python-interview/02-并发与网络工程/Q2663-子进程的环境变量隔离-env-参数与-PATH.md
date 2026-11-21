---
title: [Q2663] 子进程的环境变量隔离:env 参数与 PATH 的陷阱
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2663 · 子进程的环境变量隔离:env 参数与 PATH 的陷阱

> 难度:★★ | 标签:subprocess, 环境变量, 最小暴露面

**问**:调用 subprocess 时传 env 参数意味着什么?不传又意味着什么?

**答**:不传 env 表示完整继承父进程环境——包括 API_TOKEN 这类敏感变量,实测子进程 environment 里 can 看到凭证;显式传 env 则子进程只看到白名单变量,是最小暴露面。陷阱是 PATH 也属于环境:白名单里忘了带 PATH,裸名可执行文件立刻找不到,实测 PATH 指向空目录时启动裸名 python3 直接 FileNotFoundError。

- 凭证隔离的正确姿势:白名单 env,一个变量一个变量的给;

- 可执行文件用绝对路径(sys.executable)就不依赖子进程 PATH;

- 排查"子进程行为诡异"时先 diff 父子环境,LD_PRELOAD、LANG 这类变量影响深远;

- env 的继承是全有或全无:给了 env 就没有了"默认项",要自己拼齐。

```python
# file: code/02_并发与网络工程/q2663_env_isolation.py
# -*- coding: utf-8 -*-
"""子进程的环境变量隔离: env 参数与 PATH 的陷阱。

- 默认 env=None: 完整继承父进程环境, 凭证等敏感变量也一起带过去;
- 显式传 env: 子进程只看到白名单变量, 这是最小暴露面;
- PATH 也属于环境: 子进程的 PATH 决定裸名可执行文件的查找范围。
"""
import os
import subprocess
import sys

PROBE = (
    "import os, shutil; "
    "print('env_keys=%d' % len(os.environ)); "
    "print('has_secret=%s' % ('API_TOKEN' in os.environ)); "
    "print('which_python3=%s' % (shutil.which('python3') or 'NOT-FOUND'))"
)


def run(env):
    r = subprocess.run([sys.executable, "-c", PROBE],
                       capture_output=True, text=True, env=env, timeout=10)
    return r.stdout.strip().splitlines()


if __name__ == "__main__":
    os.environ["API_TOKEN"] = "should-not-leak"

    print("== 默认继承父进程环境 ==")
    for line in run(None):
        print("  ", line)

    print("== 白名单环境(仅 MINIMAL 与受控 PATH) ==")
    clean = {"MINIMAL": "1", "PATH": "/usr/bin:/bin"}
    for line in run(clean):
        print("  ", line)

    print("== 子进程 PATH 指向空目录时, 裸名查找会怎样 ==")
    try:
        subprocess.run(["python3", "-c", "print(1)"],
                       capture_output=True, env={"PATH": "/nonexistent"},
                       timeout=10)
        print("  竟然成功了")
    except FileNotFoundError as e:
        print("  FileNotFoundError:", e)

    print("== 结论: 凭证要靠白名单 env 挡住, 别依赖子进程自觉 ==")
```

**追问**:1) 只想加一个变量、其余继承怎么做?——先 copy os.environ 再覆盖目标键,注意别把敏感变量一并带过去。2) 为什么裸名查找失败报 FileNotFoundError 而不是更明确的错误?——execvp 语义如此,PATH 上找不到就是文件不存在,排障时先查 PATH。3) 底层机制:PATH 查找发生在哪一层?——POSIX execvp 按子进程 env 里的 PATH 逐目录探测,subprocess 只把 argv 与 env 交给 fork/exec;父进程 shutil.which 用的是父进程自己的 PATH,两边不一致时就是"父进程找得到、子进程跑不起来"。4) 生产陷阱?——白名单忘带 PATH/HOME,子进程工具链行为异常;LD_PRELOAD、LANG 这类深远变量未经审查就继承;用字符串拼接构造 env,把凭证带进日志或临时文件。

---
