---
title: [Q7137] cron 非交互 shell 环境缺失的事故复盘
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7137 · cron 非交互 shell 环境缺失的事故复盘

难度：P6 ｜ 标签：事故复盘 / 定时任务 / 环境工程

**问**：一个手工跑了两年的数据脚本挂上 cron 后立刻出事：`ModuleNotFoundError`、`command not found`、写文件权限报错、时区算错。为什么"手工能跑、cron 必挂"是定时任务最经典的事故模式？怎么系统性防住？

**答**：
- **结论**：cron 用**非交互、非登录 shell** 执行：不读 `.bashrc`/`.bash_profile`，环境变量只有极简的 PATH（经典 Unix 是 `/usr/bin:/bin`），HOME/TZ/语言环境都是默认值。四类经典炸点：① `python` 解析到系统老版本或干脆不存在（pyenv/uv 的 PATH 注入只在交互 shell 生效）；② venv 未激活——`ModuleNotFoundError`；③ 相对路径/写权限：cron 的 cwd 是用户家目录、umask 与登录 shell 不同；④ TZ 默认 UTC，任务里用 `datetime.now()` 与本地时间假设错位（Q7093 DST 事故的环境放大版）。系统性防线：① **用绝对路径**：解释器用 venv 内绝对路径（`/srv/app/.venv/bin/python`），脚本与数据同理；② **显式环境**：cron 条目里显式设置 PATH/TZ，或干脆套一层包装脚本 `set -euo pipefail` + `source` 环境文件；③ 更优方案：用 systemd timer（环境由 unit 文件完整声明、有日志与依赖管理）替代裸 cron，APScheduler 类应用内调度（Q7026）则彻底复用应用环境；④ 上 cron 前用 `crontab` 同环境冒烟：`env -i` 模拟最小环境跑一遍。
- **取舍**：systemd timer 比 cron 重（要写 unit 文件、root 权限），换来日志（journalctl）、失败重试、依赖顺序、资源限制；容器化调度（K8s CronJob）环境最可控但运维成本最高。裸 cron 适合简单任务，但必须配"绝对路径 + 显式环境 + 日志重定向"三件套——缺一样就是待发事故。
- **实战**：① 所有 cron 条目带日志重定向 `>> /var/log/task.log 2>&1`，否则 stderr 丢失只能靠邮件（通常没人看）；② 脚本入口 assert 环境：`sys.executable` 是否 venv 内、关键环境变量存在与否，启动即 fail-fast（Q7141 的解释器自检同源）；③ 把"最小环境冒烟"做成上线清单项：`env -i /bin/sh -c 'your command'`。

```python
# cron 环境自检: 启动即断言解释器/关键环境/时区, fail-fast 代替静默跑错
# 基线: Python 3.9+ 标准库
import os
import sys
from pathlib import Path


def check_env(expected_venv: Path, required_vars: set[str]) -> list[str]:
    problems = []
    # 1. 解释器必须在预期 venv 内 (防 PATH 劫持到系统 python)
    if expected_venv.resolve() not in Path(sys.executable).resolve().parents:
        problems.append(f"interpreter={sys.executable} 不在 {expected_venv}")
    # 2. 关键环境变量 (cron 里不会自动继承)
    missing = required_vars - os.environ.keys()
    if missing:
        problems.append(f"missing env: {sorted(missing)}")
    # 3. 时区显式声明 (cron 默认 UTC)
    if "TZ" not in os.environ:
        problems.append("TZ 未显式设置: now() 可能与业务时区错位")
    # 4. 工作目录与写权限
    if not os.access(Path.cwd(), os.W_OK):
        problems.append(f"cwd={Path.cwd()} 不可写 (cron cwd 是家目录)")
    return problems


def main() -> None:
    # 演示: 在当前环境构造一个"缺 env"场景
    venv = Path(sys.executable).parent.parent          # 当前解释器当 venv
    problems = check_env(venv, {"DB_URL"})             # DB_URL 故意缺失
    assert any("missing env" in p for p in problems)
    # 全部满足时返回空
    os.environ["TZ"] = "Asia/Shanghai"
    os.environ["DB_URL"] = "postgres://..."
    ok = check_env(venv, {"DB_URL", "TZ"})
    assert ok == [] or all("TZ" not in p and "missing" not in p for p in ok), ok
    print(f"自检捕获 {len(problems)} 类问题: {problems[0][:50]}...")
    print("OK: 定时任务入口先自检环境 fail-fast; 绝对路径+显式env+日志三件套")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么推荐 systemd timer 而不是给 cron 堆包装脚本？
→ 一句话提示：包装脚本是在补 cron 的环境缺陷（PATH/日志/依赖/重试全手工造），systemd unit 天然声明式提供这些；用声明式平台比在错误层上打补丁可持续。

**追问 2**：`env -i` 冒烟测的是什么？
→ 一句话提示：剥离全部继承环境模拟 cron 的最小环境，暴露脚本对 PATH/变量/时区的隐式依赖；它测的是"环境契约"而非功能。

## 背诵要点
- cron = 非交互非登录 shell：PATH 极简、无 .bashrc、cwd 是家目录、TZ 默认 UTC——手工能跑 cron 必挂是必然不是偶然。
- 三件套：绝对路径解释器（venv 内）、显式 PATH/TZ/env、日志重定向；进阶替代 = systemd timer / K8s CronJob。
- 入口 fail-fast 自检：sys.executable 在 venv 内、关键变量存在、TZ 声明；上线前 `env -i` 冒烟。

## 复盘追问
- 日志重定向缺失为什么算事故隐患而不只是不便？提示：cron 默认把输出寄邮件，无人订阅即静默失败数月；无日志也让事后复盘失去唯一证据链。
- 应用内调度（APScheduler）与 cron 的环境差异？提示：复用应用进程环境（PATH/venv/配置全一致），代价是与应用共存亡（重启丢调度状态，Q7026 的错过触发问题）。
