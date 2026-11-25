---
title: "[Q7197] uv export 与哈希锁定的生产部署校验"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7197 · uv export 与哈希锁定的生产部署校验

难度：P6 ｜ 标签：版本迁移、uv、供应链安全、可复现构建

基线：Python 3.12；uv 0.4+；hashlib 标准库演示哈希校验。

**问**：开发环境用 `uv sync` 很顺，生产镜像里想用 requirements.txt 装配。有人直接 `uv pip freeze > requirements.txt`，结果生产装的版本和 lock 文件不一致，还担心供应链投毒。正确姿势是什么？

**答**：
- **结论**：`uv pip freeze` 导出的是**当前环境已安装**的版本，可能受临时安装、缓存影响，不保证对应 lock 文件的可复现性。正确做法是从 lock 文件派生：`uv export --format requirements-txt --hashes -o requirements.txt`，生产用 `pip install --require-hashes -r requirements.txt` 安装。带哈希后 pip 会逐个校验 wheel 的 sha256，防止依赖被替换/投毒，同时保证与开发环境完全同版本。
- **取舍**：哈希锁定要求所有依赖（含传递依赖）都有哈希，某些私有包/sdist 可能没有，需要 `--no-hashes` 退路或自建带哈希的 index；`--require-hashes` 模式下所有包都必须带哈希，不允许混用。导出产物应纳入 CI 校验"与 lock 一致"，防止有人手改。
- **实战**：把 `uv export` 作为 CI 生成步骤，产物提交或在部署时现生成；镜像构建用 `--require-hashes`；定期通过 `uv lock --upgrade` 更新并审查 diff，而不是在开发环境随手升级后 freeze。

```python
import hashlib


def verify_hash(data: bytes, expected: str) -> bool:
    return hashlib.sha256(data).hexdigest() == expected


if __name__ == "__main__":
    data = b"pkg-wheel-bytes"
    digest = hashlib.sha256(data).hexdigest()
    print("correct hash:", verify_hash(data, digest))
    print("tampered:", verify_hash(data, "0" * 64))
    # --require-hashes 模式：每个 wheel 都要有 expected 且校验通过。
```

**追问一**：`uv export --hashes` 和 `pip freeze` 导出的本质区别是什么？
→ 解析：前者从 lock 文件派生、包含每个包的哈希、与解析结果严格一致；后者只反映当前环境状态、不含哈希、可能已被临时操作污染，不能作为可复现/可验证的生产清单。

**追问二**：`--require-hashes` 模式下混入一个没有哈希的私有包会怎样？
→ 解析：pip 会直接报错拒绝安装，因为该模式要求所有依赖都有哈希。解决是为私有包生成并写入哈希（自建 index 提供）、或对该包单独走另一条安装路径，不能在同一次 `--require-hashes` 安装里混用。
