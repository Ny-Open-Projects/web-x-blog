---
title: [Q7152] subprocess 命令注入事故复盘
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7152 · subprocess shell=True 命令注入事故复盘

难度：P6-P7 | 标签：subprocess、安全、事故复盘

**问**：一个内部运维工具用 `subprocess.run(f"git log {user_input}", shell=True)` 拉提交记录，用户传 `main; rm -rf /tmp/evidence` 后命令被拼接执行。注入的机理是什么？安全封装的标准姿势与防线怎么搭？

**答**：结论：`shell=True` 把整串文本交给 `/bin/sh` 解释，`;`、`&&`、`` ` ``、`$()` 等元字符都会被展开执行——拼接即注入。标准姿势是**列表参数 + shell=False**：`["git", "log", user_input]`，此时 `user_input` 是 execve 的一个 argv，永远只是参数，不可能变成命令。防线三层：① 一律列表调用，② 必须走 shell 时对输入做白名单校验（`shlex.quote` 只是缓解不是根治），③ subprocess 降权 + 文件系统权限收敛，限制爆炸半径。

实战要点：
1. 代码评审守门：CI grep `shell=True`，出现即要求豁免说明；包装函数 `run_checked(cmd_list)` 统一入口，禁止散写。
2. `shlex.quote` 能处理空格与元字符，但它保护的是"参数位置"；如果输入能控制**命令名**（第一个元素）或有管道重定向需求，quote 救不了。
3. 高危模式清单：`os.system`（等价 shell=True）、`os.popen`、`bash -c` 传变量——一并纳入守门。

```python
"""安全封装 run_checked 与注入对照演示（标准库，可运行）"""
import subprocess
import sys

def run_checked(cmd: list[str], timeout: float = 10.0) -> str:
    """唯一允许的 subprocess 入口：列表 + 超时 + 非零退出即抛"""
    r = subprocess.run(cmd, capture_output=True, text=True,
                       timeout=timeout, check=False)
    if r.returncode != 0:
        raise RuntimeError(f"cmd failed {r.returncode}: {r.stderr[:200]}")
    return r.stdout

evil = "main; rm -rf /tmp/x"

# 危险示意（仅展示，不执行）：
#   subprocess.run(f"git log {evil}", shell=True)   # 注入成立
# 安全路径：evil 只是 git log 的一个参数，git 会当分支名报错
print(run_checked(["python3", "-c",
                   'import sys; print("argv:", sys.argv[1])', evil]))

# 白名单校验：必须走 shell 的场景（如管道）先校验每个 token
import re
TOKEN = re.compile(r"^[A-Za-z0-9._/-]+$")

def safe_tokens(user: str) -> bool:
    return all(TOKEN.match(t) for t in user.split())

print("token check:", safe_tokens("scripts/run.sh --dry"),
      "|", safe_tokens(evil))

if "--shell-demo" in sys.argv:  # 默认不进入，演示意识
    pass
```

**追问 1**：为什么 `shlex.quote` 不被推荐为最终防线？
**提示**：它只保证"参数整体性"，无法防御"命令名被控制""shell 特性被业务需要（管道/变量）时输入进入解释层"；根治仍是列表+无 shell。

**追问 2**：注入工具还需要跑 OS 命令时，降权怎么设计？
**提示**：专用低权用户/容器（无 shell 或最小镜像）、只读挂载、`close_fds`、按命令白名单执行；把"能删什么"限制在工位的视野内。

## 背诵要点
- shell=True 拼接即注入；列表参数 + shell=False 让输入永远停在 argv 层。
- 守门三层：CI 禁 shell=True、必须 shell 时白名单+shlex.quote 仅作缓解、执行层降权限爆炸半径。
- os.system/os.popen/bash -c 与 shell=True 同罪，一并守门。

## 复盘追问
- 事故工具还有哪些入口接受用户串进命令？如何一次性清查（grep shell=True/入参审计）？
- 如果业务真的需要管道组合，比 shell 更安全的工程方案是什么（Python 内组合输出流）？
