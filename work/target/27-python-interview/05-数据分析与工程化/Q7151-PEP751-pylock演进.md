---
title: [Q7151] PEP 751 pylock.toml 锁文件标准演进
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7151 · PEP 751 pylock.toml：锁文件的标准化演进

难度：P6 | 标签：PEP 751、锁文件、版本演进

**问**：requirements.txt 锁定、poetry.lock、uv.lock、Pipfile.lock 并存多年，PEP 751 的 `pylock.toml` 要统一什么？与 requirements.txt 冻结相比强在哪？

**答**：结论：PEP 751 定义**工具无关的通用锁文件**（`pylock.toml`）：锁定全闭包（含哈希、依赖元数据、环境标记），任何支持它的工具都能按同一结果安装。相比 `requirements.txt` 冻结：① 有 schema 与校验（版本字段、依赖关系而非平铺列表），② 区分直接/传递依赖，③ 原生支持 extras/groups（与 PEP 735 联动）、多环境标记。统一的意义是"锁文件不再被工具绑定"——换包管理器不换锁格式，CI/审计工具可直接读。

实战要点：
1. 生成与消费：uv/pip（较新版）/pdm 等均可生成 `pylock.toml`；CI 消费时用 `--locked` 类参数校验一致性，漂移即失败（Q7102 的标准化解法）。
2. 命名扩展：`pylock.dev.toml`、`pylock.audit.toml` 等按 group 命名，替代"多个 requirements-*.txt"。
3. 过渡策略：仓库里保留 `uv export` 出的 requirements.txt 作为旧工具兜底，CI 断言两者等价，待工具链齐备后删除。

```python
"""pylock.toml 结构解析与闭包校验（标准库模拟，可运行）"""
import tomllib

LOCK = """
lock-version = "1.0"
requires-python = ">=3.11"

[[packages]]
name = "requests"
version = "2.32.3"

[[packages]]
name = "charset-normalizer"
version = "3.4.1"
dependencies = ["requests"]   # 示意：真实 schema 为组与标记
"""


def check_closure(packages: list[dict]) -> list[str]:
    """闭包完整性：依赖必须都在锁内，且锁内无重复包"""
    names = [p["name"] for p in packages]
    issues = []
    if len(names) != len(set(names)):
        issues.append("duplicate package in lock")
    known = set(names)
    for p in packages:
        for dep in p.get("dependencies", []):
            if dep not in known:
                issues.append(f"{p['name']} depends on locked-out {dep}")
    return issues or ["closure OK"]


data = tomllib.loads(LOCK)
print("requires-python:", data["requires-python"])
print(check_closure(data["packages"]))
print("工具无关: 任何支持 PEP 751 的安装器读到同一闭包")
```

**追问 1**：为什么"平铺的 requirements.txt"在审计场景不够用？
**提示**：没有依赖关系图，SBOM/漏洞影响分析要靠解析器重建；pylock 自带包级元数据与关系，审计工具可直接消费。

**追问 2**：锁文件里 `requires-python` 与项目 `pyproject.toml` 冲突时听谁的？
**提示**：锁是对特定解释器范围的有效快照，冲突说明锁过期或编辑了边界；CI 应在生成时即校验并拒绝不一致。

## 背诵要点
- PEP 751 = 工具无关锁文件 `pylock.toml`：全闭包+哈希+环境标记，替代各工具私有锁格式。
- 比 requirements.txt 强在：有 schema、分直接/传递依赖、联动 PEP 735 的 groups/extras。
- 过渡期双文件 + CI 等价断言，防 Q7102 式版本漂移。

## 复盘追问
- 你们的 uv.lock/poetry.lock 迁到 pylock 的一次性成本与兼容期怎么安排？
- 审计工具（SBOM）接入通用锁格式后，哪类安全问题能更早发现？
