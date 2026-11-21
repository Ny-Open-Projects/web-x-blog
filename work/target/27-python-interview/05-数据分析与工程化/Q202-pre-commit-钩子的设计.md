---
title: [Q202] pre-commit 钩子的设计
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q202 · pre-commit 钩子的设计

> 难度:★★☆ | 标签:pre-commit, git hooks

**问**:pre-commit 是什么?哪些检查适合放 pre-commit,哪些必须放 CI?

**答**:pre-commit 框架用 `.pre-commit-config.yaml` 声明钩子,`pre-commit install` 后每次 `git commit` 自动执行,失败即中断提交。**分层原则**:本地钩子跑"快且本地可修复"的检查(格式化、lint、大文件检查、密钥扫描),几十秒内完成;慢的、需要完整环境依赖的(全量测试、类型检查大项目、构建)放 CI。这样开发者能在秒级修复风格问题,CI 只兜底"没装 pre-commit 或 --no-verify 绕过"的情况。注意 hooks 只在变更是不可靠的,`pre-commit run --all-files` 用于初始化全量修复。

```yaml
# .pre-commit-config.yaml:非 python 文件示例
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: local
    hooks:
      - id: no-secrets
        name: 检查疑似密钥
        entry: grep -rIE "AKIA[0-9A-Z]{16}" --exclude-dir=.git
        language: system
```

```python
# file: code/05_数据分析与工程化/q202_precommit_demo.py
def format_target(line_length=88):
    # 演示:格式化工具会把超长行折行,这里验证行宽约定
    assert line_length == 88

def test_convention():
    format_target()
```

**追问**:
- 钩子失败但开发者用 --no-verify 提交了怎么办?——CI 是最终防线,同套检查在流水线必跑;--no-verify 只能骗过本地骗不过 main 分支保护。
- pre-commit 首次安装怎么强制?——CI 检查 `.pre-commit-config.yaml` 与本地版本一致(`pre-commit validate`);新人 onboarding 文档里放 install 步骤。
- 密钥扫描放哪层?——本地 pre-commit(gitleaks)即时拦截 + CI 再扫一遍 + 平台侧 secret scanning 三层;任何一层都可能被绕过。
