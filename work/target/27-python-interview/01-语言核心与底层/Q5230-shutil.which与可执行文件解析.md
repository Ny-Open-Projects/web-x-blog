---
title: "[Q5230] shutil.which 与可执行文件解析：PATH 语义与诊断"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5230 · shutil.which 与可执行文件解析：PATH 语义与诊断

难度：P5 ｜ 标签：shutil.which、PATH、可执行权限、X_OK、sys.executable、环境诊断

**问**：`shutil.which("python3")` 找的是什么？"能找到"和"能执行"差在哪？为什么当前目录不在 PATH 里？`path=`/`mode=` 参数怎么用？诊断"跑错解释器"为什么必须对比 `sys.executable`？

**答**：
结论：`shutil.which(cmd)` 复刻 shell 的解析规则：按 **PATH 环境变量**逐目录查找名为 `cmd` 的文件，找到**第一个**同时满足"存在 + 通过 mode 权限检查（默认 X_OK，可执行）"的就返回绝对路径——是"第一个匹配"而不是"最优版本"。三个高频坑：①**当前目录不在 PATH 里**（POSIX 从不隐式包含 `.`），脚本目录下的 `tool.sh` 必须 `./tool.sh` 或把目录显式加进 PATH，`which("tool.sh")` 直接 None；②**权限即语义**：没有 x 位（644）的文件不算可执行文件，which 返回 None——"文件明明在"与"which 找不到"的矛盾十有八九是权限；③**绝对路径输入直接校验后返回**，不经 PATH。`path=` 参数可以脱离环境变量传自定义搜索路径（测试/沙箱），`mode=os.R_OK` 能放宽为"只要可读"。诊断价值：`which("python3")` 拿到的解释器**不等于**正在跑的解释器——venv、symlink、cron 的精简 PATH 都会让两者分叉（Q7141 错误解释器事故），排障第一步永远是对比 `which` 结果与 `sys.executable`。

取舍：a) 探测外部工具是否存在：`shutil.which("ffmpeg")` 是标准做法，比 `os.system` 试跑干净；b) 测试/沙箱里隔离候选目录：`which(name, path=自定义)`，不污染全局 PATH；c) 需要"只读即可"的场景（找数据文件）：`mode=os.R_OK`；d) Windows 差异：会自动尝试 PATHEXT（.exe/.bat），移植代码时别假设后缀存在；e) 找到 ≠ 版本对：PATH 前序目录里的旧版本会赢，部署脚本用绝对路径而不是 which 结果——which 适合"探测存在性"，不适合"锁定版本"。

实战：事故形态是"CI 里 `which python3` 指向系统 3.9，脚本实际由 venv 的 3.12 执行，安装依赖装进了系统 site-packages 导致 'ModuleNotFoundError'；修复为所有脚本统一用 `sys.executable` 调起子进程，which 仅用于启动前自检并告警分叉"。下面演示 which 的查找规则、权限语义与 path/mode 参数。

```python
# shutil.which 与可执行文件解析
import os
import shutil
import tempfile

print("[1] which 沿 PATH 找可执行文件, 找到的是'第一个'而非'最好的'")
print("    which('python3') =", shutil.which("python3"))
print("    绝对路径输入: which('/bin/ls') =", shutil.which("/bin/ls"))

print("[2] 无执行权限的文件不算可执行文件")
with tempfile.TemporaryDirectory() as d:
    exe = os.path.join(d, "tool.sh")
    with open(exe, "w", encoding="utf-8") as f:
        f.write("#!/bin/sh\necho ok\n")
    os.chmod(exe, 0o644)                              # 缺 x 位
    print("    chmod 644 -> which(path=) =", shutil.which("tool.sh", path=d))
    os.chmod(exe, 0o755)
    print("    chmod 755 -> which(path=) =", shutil.which("tool.sh", path=d))

print("[3] 当前目录不在 PATH 里: ./tool.sh 与 tool.sh 是两回事")
print("    which(相对路径, path='') =", shutil.which("tool.sh", path=""))

print("[4] mode 参数可放宽/收紧判定 (X_OK|R_OK)")
with tempfile.TemporaryDirectory() as d:
    f = os.path.join(d, "data.txt")
    with open(f, "w", encoding="utf-8") as fh:
        fh.write("x")
    os.chmod(f, 0o644)
    print("    可读文件 which(mode=R_OK) =", shutil.which("data.txt", mode=os.R_OK, path=d))

print("[5] 排障价值: which 拿到的解释器路径 != 正在跑的解释器 (venv/symlink), 诊断要对比 sys.executable")
print("    sys.executable vs which('python3') 可能不同, 部署前先对齐")
```

**追问一**：为什么 POSIX 的 PATH 默认不包含当前目录？—— 安全设计：若 PATH 含 `.`，攻击者把恶意脚本命名为 `ls` 放进可写目录，用户在该目录执行 `ls` 就会命中恶意版本（劫持常见命令）。Linux 发行版默认 PATH 无 `.`，历史上一些 Unix 把 `.` 放在 PATH 末尾也被逐步移除。Python 侧同理：`sys.path` 脚本目录优先但**不含任意 CWD**（交互环境才补 `''`），import 遮蔽（Q2378）本质是同一类"名字就近解析"的风险。工程纪律：可执行与可导入都走显式路径/显式包名，不做隐式就近。

**追问二**：cron 里 `which python3` 与交互 shell 结果不同，为什么？怎么根治？—— cron 的环境是**精简 PATH**（通常 `/usr/bin:/bin`），venv 里装的解释器、用户级工具全不在列；交互 shell 还有 shell hash（`hash` 缓存查找结果）干扰。根治三板斧：①cron 条目写绝对解释器路径（venv 的 bin/python）；②脚本开头自检 `sys.executable` 与预期前缀一致，不一致直接退出码非 0 报警；③依赖安装也用同一解释器（`sys.executable -m pip`），杜绝"装进 A 跑在 B"。Q7137 的 cron 环境事故、Q7184 的环境污染事故同族。

## 背诵要点
- which 按 PATH 取第一个"存在+X_OK"的匹配；644 无 x 位返回 None；绝对路径输入直查。
- 当前目录不在 PATH（POSIX 安全设计）；path=/mode= 参数支持沙箱与只读探测。
- which 结果 ≠ sys.executable（venv/cron 分叉），脚本自检解释器一致性是部署门禁。

## 复盘追问
- CI 里依赖装到系统 site-packages，怎么定位？（which 与 sys.executable 分叉；统一 sys.executable 安装与执行）
- 为什么 PATH 不含当前目录是安全特性？（防可写目录命令劫持；与 import 遮蔽同源）
