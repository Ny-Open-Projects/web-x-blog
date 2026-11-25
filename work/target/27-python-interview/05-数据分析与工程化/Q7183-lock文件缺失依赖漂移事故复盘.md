---
title: [Q7183] lock 文件缺失与依赖漂移事故复盘
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7183 · lock 文件缺失导致依赖漂移事故复盘

难度：P6 ｜ 标签：事故复盘、依赖管理、锁文件、可复现构建

基线：Python 3.9+；pip / uv（0.4+）/ Poetry；CI 与生产同链路。

**问**：同一个 commit，CI 里测试是绿的，部署机上跑起来却报 `TypeError`——排查发现两个环境装的 `requests` 一个 2.31 一个 2.32。为什么会出现这种"同代码不同世界"？根治方案是什么？

**答**：
- **结论**：根因是"依赖解析发生在安装时刻而不是提交时刻"。`requirements.in` 或 `pyproject.toml` 里写的是范围约束（`requests>=2.31`），每次不带锁文件安装都会重新解析，拿到的版本随时间漂移。间接依赖（依赖的依赖）没有锁定时，任何上游发版都可能改变你的运行时。**同一 commit 必须解析出同一棵依赖树**是可复现构建的底线。
- **取舍**：方案梯度——(1) `pip freeze > requirements.txt` 全量钉死：简单但把直接/间接依赖混在一起，升级痛苦；(2) uv/Poetry 的 lock 文件（`uv.lock`/`poetry.lock`）：分层记录解析结果 + 哈希，`--frozen`/`--locked` 安装时不重新解析，校验不一致直接失败；(3) 容器镜像锁死：lock 文件 + 固定基础镜像 digest。锁文件必须进版本库，且 CI 要校验"lock 与 manifest 同步"。
- **实战**：防线清单——CI 用 `--frozen` 安装禁止解析；本地和 CI 用同一安装命令（Makefile/taskfile 单一入口）；升级依赖是显式 PR（改 lock + 跑全量测试），而不是环境里随手 `pip install -U`。

```python
# 依赖一致性自检：校验 lock 与 manifest 是否同步、
# 关键包版本是否钉死（标准库可运行的模拟检查器）。
import re
from pathlib import Path

def check_lockfile(lock_text: str, manifest_text: str,
                   critical: tuple[str, ...]) -> list[str]:
    issues = []
    # 模拟 uv.lock：[[package]] name/version 段
    locked = dict(re.findall(r'\[\[package\]\]\s*name = "([^"]+)"\s*\n'
                             r'version = "([^"]+)"', lock_text))
    # manifest 中的直接依赖范围
    declared = re.findall(r'^([a-zA-Z0-9_-]+)\s*>=\s*([0-9.]+)', manifest_text, re.M)
    for name, _ in declared:
        if name.lower() not in locked:
            issues.append(f"{name} 在 manifest 有但 lock 没有 -> lock 过期，禁止安装")
    for pkg in critical:
        if pkg.lower() not in locked:
            issues.append(f"关键包 {pkg} 未锁定，上游发版即漂移")
    if "hash" not in lock_text:
        issues.append("lock 无哈希字段 -> 供应链完整性缺失")
    return issues or ["lock 与 manifest 同步，关键包全部锁定"]

if __name__ == "__main__":
    lock = '[[package]]\nname = "requests"\nversion = "2.31.0"\n' \
           'hash = "sha256:abc..."\n'
    manifest = "requests>=2.31\nhttpx>=0.27\n"
    for line in check_lockfile(lock, manifest, critical=("requests", "httpx")):
        print("-", line)
    # - httpx 在 manifest 有但 lock 没有 -> lock 过期，禁止安装
    # - lock 无哈希字段 -> 供应链完整性缺失
```

**追问**：
- 一层：`pip install -r requirements.txt` 生成了 lock 还有漂移风险吗？→ 提示：有——若文件里含范围约束或依赖带有环境标记被跳过；真正钉死需要全量 `==` + 哈希，或 uv/poetry 这类带解析器的工具。
- 二层：为什么"upgrade 是显式 PR"这条纪律重要？→ 提示：让依赖变更进入评审与回归视野，漂移从"随机事故"变成"受控变更"；配合 dependabot 类工具定时批量处理。

**背诵要点**：
1. 漂移根因：依赖解析发生在安装时刻；同一 commit 必须解析出同一棵依赖树（lock 文件进库 + `--frozen` 安装）。
2. 方案梯度：freeze 全量钉死 < uv/Poetry lock（分层+哈希+同步校验）< 镜像 digest 锁死。
3. 纪律：本地/CI/生产同一安装命令；升级依赖走显式 PR + 全量回归。

**复盘追问**：
1. 为什么 CI 绿了还出事？提示：CI 安装时解析了一次，部署时又解析了一次，两次环境时间不同。
2. 如果必须紧急修一个间接依赖的 CVE 怎么办？提示：lock 文件里最小范围升级该包 + 回归，禁止全局 -U。
