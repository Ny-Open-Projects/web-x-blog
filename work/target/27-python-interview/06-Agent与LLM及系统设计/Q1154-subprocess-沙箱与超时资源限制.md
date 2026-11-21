---
title: [Q1154] subprocess 沙箱与超时资源限制
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1154 · subprocess 沙箱与超时资源限制

> 难度:★★★★ | 标签:沙箱, 进程隔离

**问**:要执行模型生成的 Python 代码,进程级沙箱至少要做哪些防护?

**答**:至少五层:`subprocess.run(timeout=...)` 防死循环;RLIMIT_CPU/RLIMIT_AS 限制 CPU 与内存,防资源耗尽;独立工作目录 + 环境变量清洗,防读敏感文件与凭据泄漏;`-I` 隔离模式启动解释器,忽略用户 site 与环境;网络按需关闭(容器层做,进程内做不了)。还要收集 stdout/stderr 截断存储,退出码非零时把 stderr 摘要回传给模型修复。这些是最低配,生产环境应上容器/微 VM 隔离。

```python
# file: code/06_Agent与LLM及系统设计/q1154_subprocess_sandbox.py
"""subprocess 沙箱:超时 + 资源限制 + 隔离模式执行用户代码,stderr 摘要回传。"""
import resource, subprocess, sys, textwrap


def run_user_code(code: str, timeout=2):
    preexec = None
    if sys.platform != "win32":
        def preexec():
            for res_id, limit in ((resource.RLIMIT_CPU, (2, 2)),
                                  (resource.RLIMIT_AS, (256 * 1024 * 1024,) * 2),
                                  (resource.RLIMIT_FSIZE, (1024 * 1024,) * 2)):
                try:
                    resource.setrlimit(res_id, limit)
                except (ValueError, OSError):
                    pass                    # 个别 rlimit 平台不支持时跳过
    try:
        p = subprocess.run(
            [sys.executable, "-I", "-c", code],  # -I 隔离:忽略环境与用户 site
            capture_output=True, text=True, timeout=timeout,
            preexec_fn=preexec, cwd="/tmp" if sys.platform != "win32" else None,
        )
    except subprocess.TimeoutExpired:
        return {"code": -9, "stdout": "",
                "stderr_summary": "killed by timeout"}   # 超时被杀,stderr 不可靠
    return {
        "code": p.returncode,
        "stdout": p.stdout[:2000],
        "stderr_summary": p.stderr.strip().splitlines()[-1][:200] if p.stderr else "",
    }


if __name__ == "__main__":
    r1 = run_user_code(textwrap.dedent("""
        total = sum(i * i for i in range(100))
        print("sum =", total)
    """))
    print("正常执行:", r1)
    assert r1["code"] == 0 and "sum = 328350" in r1["stdout"]

    r2 = run_user_code("while True: pass", timeout=1)
    print("死循环:", r2)
    assert r2["code"] != 0, "超时任务必须被杀死"
    print("超时防护生效,退出码", r2["code"])

    r3 = run_user_code("1/0")
    print("异常回传:", r3["stderr_summary"])
    assert "ZeroDivisionError" in r3["stderr_summary"], "stderr 摘要可供模型修复"
    print("subprocess 沙箱通过")
```

**追问**:
- preexec_fn 有什么坑?答:多线程程序里 fork + preexec_fn 可能死锁,生产建议改用容器 runsc/gVisor 或独立沙箱服务,子进程方案只适合低风险场景。
- 怎么限制它访问网络?答:进程内做不到可靠限制,必须在网络层(无网 netns、容器 network none、出口白名单代理)实现。
