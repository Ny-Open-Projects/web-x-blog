---
title: [Q2128] 被信号杀死的 returncode:负数的含义
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2128 · 被信号杀死的 returncode:负数的含义

> 难度:★★★ | 标签:SIGTERM, SIGKILL, returncode

**问**:子进程的 returncode 是 -15,这是什么意思?和退出码 15 怎么区分?

**答**:负数 returncode 表示进程被信号终止,-N 就是被信号 N 杀死,这是 waitpid 的原始语义透传。

- terminate() 发 SIGTERM,进程可捕获后体面退出,实测返回 0;

- kill() 发 SIGKILL,不可捕获不可忽略,直接 -9;

- 编排规则:rc==0 成功,rc>0 业务失败,rc<0 按 -rc 分诊信号;

- SIGTERM 后超时未退,升级 SIGKILL 是标准的两级止损。

```python
# file: code/02_并发与网络工程/q2128_signal_returncode.py
# -*- coding: utf-8 -*-
"""被信号杀死的 returncode: 负数的含义。

- 进程被信号 N 杀死时, Python 侧 returncode 是 -N, 这是 waitpid 的原始语义;
- terminate() 发 SIGTERM, kill() 发 SIGKILL, SIGKILL 不可捕获不可忽略;
- 退出码判定的完整规则: 正数是 exit(n), 负数是被信号 N 终止。
"""
import subprocess
import sys
import time


def main():
    p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    time.sleep(0.3)
    p.terminate()             # SIGTERM: 可捕获, 进程可先收尾
    rc = p.wait()
    print("terminate 后 returncode:", rc, "-> 被信号 %d 终止" % -rc)

    p2 = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    time.sleep(0.3)
    p2.kill()                 # SIGKILL: 无 opportunity 收尾
    rc2 = p2.wait()
    print("kill 后 returncode:", rc2, "-> 被信号 %d 终止" % -rc2)

    # 自捕获 SIGTERM 的子进程: 干净退出, returncode 为正
    p3 = subprocess.Popen([sys.executable, "-c",
                           "import signal,sys;"
                           "signal.signal(signal.SIGTERM,"
                           "lambda s,f:(print('graceful'),sys.exit(0)));"
                           "import time; time.sleep(30)"],
                          text=True)
    time.sleep(0.5)
    p3.terminate()
    rc3 = p3.wait()
    print("自捕获 SIGTERM 后 returncode:", rc3, "-> 0 是干净退出")
    print("编排规则: rc==0 成功; rc>0 业务失败; rc<0 信号终止需按 -rc 分诊")


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么 -15 和 15 完全不同?——15 是业务退出码(语义自定义),-15 是系统层的死因,混用会让告警分诊错乱。2) Python 程序默认收到 SIGTERM 会怎样?——默认 handler 直接终止进程,returncode -15;要体面就注册 handler 走排干流程。3) SIGTERM 的体面退出 handler 怎么写?——注册 handler 置停止标志/抛 SystemExit→主循环排干→sys.exit(0);handler 里不做复杂收尾(信号安全,Q1603);两级止损:terminate() 后 wait(timeout) 超时升级 kill()——「先礼后兵」是编排标准动作。4) -N 与 128+N 两种表达怎么统一?——Python subprocess 的 returncode 是 -N(waitpid 原始语义);shell 的 $? 是 128+N;同一事实两种投影,跨层编排放统一分诊函数(rc<0→信号 -rc;rc>127→信号 rc-128)。5) 生产陷阱?——SIGTERM handler 里无限等待(编排器最终 SIGKILL,收尾白做);把 -15 当业务失败告警(死因错分);kill 后不 wait(僵尸,Q2129);SIGKILL 前不给 SIGTERM(数据丢失);容器里 PID 1 不转发信号(Q1612 同坑)。

---
