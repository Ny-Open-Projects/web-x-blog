---
title: [Q1093] mypy 渐进治理策略
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1093 · mypy 渐进治理策略

> 难度:★★★★ | 标签:mypy, 类型标注

**问**:几十万行的存量项目想上 mypy,一跑几千个错,怎么推进?

**答**:渐进四步:先 `--ignore-missing-imports` 全库跑通拿到基线错误数,写入 CI 报告(不阻断);开启新代码严格(`disallow_untyped_defs`),用文件级豁免(`# mypy: ignore-file` 或 per-module overrides)保护存量;按目录逐个收紧,错误数单调下降;最后全局 strict 并把豁免清零。配套手段:`reveal_type` 与 `mypy --strict` 本地快速反馈、CI 里比较错误数禁止回升、公共 API 优先标注。原则:类型是渐进承诺,先把"新增欠债"堵住,再还旧账。

```python
# file: code/05_数据分析与工程化/q1093_mypy_gradual.py
from typing import Optional

def normalize_email(raw: Optional[str]) -> str:
    if raw is None:
        return "unknown@example.com"
    return raw.strip().lower()

def parse_amount(text: str) -> float:
    try:
        return float(text.replace(",", ""))
    except ValueError:
        return 0.0

if __name__ == "__main__":
    print(normalize_email("  Bob@X.com "))
    print(parse_amount("1,234.5"))
    # 治理配置示例:
    # [tool.mypy] python_version = "3.12"
    # files = ["src"] ; disallow_untyped_defs = true ; ignore_missing_imports = true
    # 存量目录用 per-module overrides 逐个收紧
```

**追问**:
- 追问 1:mypy 和运行时校验(pydantic)冲突吗?—— 不冲突,mypy 管静态结构,pydantic 管运行时边界(外部输入),边界处用 `cast`/构造器桥接。
- 追问 2:`type: ignore` 怎么治理?—— 必须带错误码与原因(`type: ignore[attr-defined]`),CI 统计新增 ignore 数,只许减不许增。
