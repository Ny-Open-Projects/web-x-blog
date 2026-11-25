---
title: "[Q5141] shell=True 命令注入事故与 shlex 演进"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5141 · shell=True 命令注入事故与 shlex 演进

难度：P6 ｜ 标签：subprocess、命令注入、shlex、安全

**问**：一次需求里需要调用外部 `ffmpeg` 处理用户上传的文件名，同事写了 `subprocess.run(f"ffmpeg -i {filename} ...", shell=True)`，结果被 `a.mp4; rm -rf /` 注入。事故怎么复盘？`shell=True` 的正确替代是什么？为什么列表参数 + `shlex.quote` 是安全线？

**答**：
结论：`shell=True` 把整个字符串交给 `/bin/sh` 再解释一遍，`;`、`` ` ``、`$()`、`&&`、`|` 都会成为 shell 语法，任何用户可控片段都可能改变命令语义。安全做法是**去掉 shell**：`subprocess.run(["ffmpeg", "-i", filename, ...])`——参数被 `execvp` 直接传给目标程序，shell 元字符退化为普通字符。当确实必须走 shell（如需要管道、通配符展开）时，对每个插值用 `shlex.quote()` 包一层。

取舍：列表参数失去了 shell 的管道/通配符能力，复杂管线要么用 Python 自己串（`subprocess.PIPE` 连接两个进程），要么只对"白名单命令 + quote 后的参数"拼 shell 串。`shlex.quote` 是"转义"而非"消除"，属于纵深防御的第二层，不能替代列表参数。

实战：复盘清单三步——① 全库 grep `shell=True`，逐一判断是否有用户可控输入；② 有可控输入的改为列表参数，无法改的用 `shlex.quote` 并记录为什么必须用 shell；③ 加 lint/CI 规则（如 bandit 的 B602/B607）拦新增。另外注意 `os.system`/`os.popen` 等价于 `shell=True`，同样要清理。

```python
import subprocess
import shlex

user_input = "a.mp4; touch /tmp/pwned"

# 危险写法（不要在生产使用）：shell 会把分号当命令分隔符
# subprocess.run(f"echo {user_input}", shell=True)

# 正确写法一：列表参数，元字符退化为普通字符
r = subprocess.run(["echo", user_input], capture_output=True, text=True)
print("list-args echo:", r.stdout.strip())  # 整段作为一个参数输出，无注入

# 正确写法二：确实需要 shell 时，对插值做 shlex.quote
quoted = shlex.quote(user_input)
print("quoted:", quoted)  # 'a.mp4; touch /tmp/pwned' 被整体加引号
r2 = subprocess.run(f"echo {quoted}", shell=True, capture_output=True, text=True)
print("shell + quote echo:", r2.stdout.strip())

# shlex.split 用于反向场景：把用户给的命令行字符串安全拆成列表
cmd_list = shlex.split("ffmpeg -i 'my video.mp4' -c:v libx264 out.mp4")
print("shlex.split:", cmd_list)
```

**追问一**：`shlex.quote` 为什么不等于"过滤危险字符"？——它不删除任何字符，而是让整个字符串变成 shell 的一个单引号字面量（对单引号做 `'` → `'\''` 处理）；攻击面被"关闭"而不是"清洗"，所以它安全的前提是使用位置正确。

**追问二**：Windows 下为什么列表参数也未必安全？——Windows 没有 execvp 语义，Python 会用 `list2cmdline` 重新拼串交给 `CreateProcess`，某些程序（如 `cmd /c`、批处理文件）会再次解释参数；跨平台高危拼接仍要谨慎，必要时显式 `shell=False` 并避免调用解释器类命令。

**追问三**：`shlex.split` 有什么坑？——它按 POSIX 规则解析，Windows 路径反斜杠会被当转义符（`C:\path` 需 `shlex.split(s, posix=False)` 或正斜杠）；空串返回 `[]` 而非报错，直接 `run([])` 会抛 IndexError 类错误。

## 背诵要点
- `shell=True` 让 `/bin/sh` 再解释一次字符串，`; | && $( )` 均可注入；列表参数走 `execvp` 才是根治。
- 必须用 shell 时对每个插值 `shlex.quote`；它是"转义成单引号字面量"，不是过滤。
- `os.system`/`os.popen` 等价于 `shell=True`；用 bandit B602/B607 在 CI 拦截新增。

## 复盘追问
- 如果命令必须用到管道，如何在不用 shell 的前提下实现？（`Popen` + `stdout=PIPE` 串联两个子进程，讨论与 shell 管道的语义差异）
- 改造后发现参数里确实需要通配符展开，有哪些安全替代？（Python 侧 `glob` 模块预展开，或 `shlex.quote` 包住已展开结果）
