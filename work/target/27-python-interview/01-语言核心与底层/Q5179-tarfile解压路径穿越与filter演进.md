---
title: "[Q5179] tarfile 解压路径穿越与 3.12 filter 演进"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5179 · tarfile 解压路径穿越与 3.12 filter 演进

难度：P6-P7 ｜ 标签：tarfile、extractall、路径穿越、filter、3.12

**问**：用户上传 tar 包，服务端直接 `tarfile.open(...).extractall(dest)` 解压。一个成员名是 `../evil.txt`，为什么文件被写到了 `dest` 的上级目录？3.12 里 `extractall` 明明会打 `DeprecationWarning: Python 3.14 will, by default, filter extracted tar archives`，为什么"警告了但还是解压了"？`filter="data"` 能挡哪些、挡不了哪些？这和 Q1826（zipfile 路径穿越）有什么区别？

**答**：
结论：`tar` 成员名是**任意字符串**，`extractall` 默认按"完全信任归档"的语义把 `name` 拼到目标目录后写入——`../`、绝对路径、符号链接都能把文件写到目标目录之外；恶意包可以覆盖 `/etc/cron.d/*`、`~/.ssh/authorized_keys`，或先解一个指向外部的 symlink 再往里写。3.12 引入了解压过滤器（PEP 706）：`filter="data"` 会拒绝绝对路径、`..`、设备文件、以及指向目标目录之外的硬/软链接；但 3.12 的默认仍是 `fully_trusted`（只是发 DeprecationWarning），到 3.14 才默认 `data`。所以"看到警告但没拦住"是预期行为，必须显式传 `filter="data"`（或 `"tar"`，按需）。

取舍：`data` 最安全但会拒绝一些合法归档（如绝对路径、特殊文件、指向外部的链接），适合"用户上传"；`tar` 保留大多数元数据但仍拒绝绝对路径/`..`/设备文件，适合"内部可信但想防手滑"；`fully_trusted` 只适合"归档由本进程刚生成、内容完全可控"。别自己写 `name.replace("..","")` 之类的字符串过滤——`..%2f`、`a/../../b`、symlink 链、硬链接都能绕过；过滤器是按解析后的路径/链接目标判断的。Q1826 讲 zipfile 的 `extract/extractall` 与 `ZipFile` 校验，本题专攻 tar 的 filter 演进与链接类攻击。

实战：事故形态是"支持导入 tar 备份的功能被做成任意文件写入，攻击者覆盖 cron/authorized_keys 拿 shell"。下面构造一个成员名为 `../evil.txt` 的 tar：默认 `extractall` 会把它写到解压目录的上级（并只给一条 3.14 的弃用警告）；显式 `filter="data"` 抛 `OutsideDestinationError`，目标目录保持为空。

```python
import io
import pathlib
import tarfile
import tempfile
import warnings

buf = io.BytesIO()
with tarfile.open(fileobj=buf, mode="w") as tf:
    data = b"pwned"
    info = tarfile.TarInfo("../evil.txt")     # 想写到解压目录之外
    info.size = len(data)
    tf.addfile(info, io.BytesIO(data))

with tempfile.TemporaryDirectory() as td:
    root = pathlib.Path(td)
    out_default = root / "default"
    out_default.mkdir()
    buf.seek(0)
    with tarfile.open(fileobj=buf, mode="r") as tf:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            tf.extractall(out_default)
        print("默认 filter 的警告:", [str(w.message)[:48] for w in caught])
    print("默认解压逃逸到上级:", (root / "evil.txt").exists())

    out_data = root / "data"
    out_data.mkdir()
    buf.seek(0)
    with tarfile.open(fileobj=buf, mode="r") as tf:
        try:
            tf.extractall(out_data, filter="data")
        except tarfile.FilterError as e:
            print("filter='data' 拒绝:", type(e).__name__)
    print("data 目录仍为空:", list(out_data.iterdir()) == [])
```

**追问一**：为什么 symlink 比 `../` 更危险？——攻击者可以先放一个成员 `link -> /etc`（symlink），再放一个成员 `link/cron.d/x`；解压器如果先创建链接、再按路径写文件，实际写入会跟随链接落到 `/etc/cron.d/x`。`filter="data"` 会检查链接目标是否在目标目录内，并拒绝指向外部的链接；`fully_trusted` 不检查。硬链接同理（指向归档外 inode）。所以"只过滤成员名里的 `..`"完全不够，必须按解析后的真实路径/链接目标判断。

**追问二**：`filter="data"` 和 `filter="tar"` 怎么选？——`data` 面向"不可信数据"：拒绝绝对路径、`..`、设备/FIFO、外部链接，甚至会把权限位收敛到安全集合，适合用户上传；`tar` 面向"可信 tar 但防误伤"：保留权限/属主/时间等元数据，但仍拒绝绝对路径、`..`、设备文件，适合内部制品。`fully_trusted` 只在"归档是本进程刚用 `tarfile` 生成、内容字节级可控"时使用。3.12 显式传 filter 还能消掉 DeprecationWarning；3.14 起默认就是 `data`，但显式写出来更利于跨版本行为一致。

## 背诵要点
- tar 成员名可为 `../`、绝对路径、symlink；默认 `extractall` 完全信任，可写到目标目录之外。
- 3.12 有过滤器但默认 `fully_trusted`（仅警告），3.14 才默认 `data`；必须显式 `filter="data"` 处理不可信包。
- `data` 拒绝绝对路径/`..`/设备/外部链接；别用字符串替换过滤，链接链能绕过。与 zipfile 穿越（Q1826）同类但机制不同。

## 复盘追问
- 用户上传 tar 后 `../evil.txt` 写到上级、甚至覆盖 cron，如何解释并修复？（成员名任意、fully_trusted、显式 data filter）
- 为什么"把成员名里的 `..` 删掉"挡不住 symlink 攻击？`data` 与 `tar` 过滤器如何选？（先链接后写入、链接目标校验；不可信 vs 内部制品）
