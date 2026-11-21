---
title: [Q1126] 安全左移:secret 扫描与依赖审计
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1126 · 安全左移:secret 扫描与依赖审计

> 难度:★★★★ | 标签:安全, DevSecOps

**问**:开发把 AWS key 提交进了 git 历史,怎么让这种事在提交前就被拦住?

**答**:安全左移三层:提交前 pre-commit 钩子扫 secret(正则 + 熵检测,gitleaks/trufflehog),扫到即阻断;CI 层依赖漏洞审计(pip-audit/safety 对照漏洞库),高危阻断合并;运行时最小权限兜底。已泄露的处理流程比拦截更重要:立即轮换凭证、清理 git 历史(filter-repo)并通知协同方重新克隆、评估暴露窗口期影响。纪律:secret 只走环境变量或密钥管理服务,样例文件用占位符,扫描白名单要最小化。

```python
# file: code/05_数据分析与工程化/q1126_secret_scan.py
import re

PATTERNS = [
    ("aws-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("generic-secret", re.compile(r"(?i)(password|secret)\s*=\s*['\"][^'\"]{8,}")),
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]
FILES = {
    "app.py": "token = 'abcd1234efgh'\n",
    "conf.yml": "password = \"hunter2secret\"\n",
    "readme.md": "hello\n",
}

def scan(files):
    hits = []
    for path, text in files.items():
        for i, line in enumerate(text.splitlines(), 1):
            for name, pat in PATTERNS:
                if pat.search(line):
                    hits.append((path, i, name))
    return hits

for path, line, kind in scan(FILES):
    print(f"{path}:{line} 疑似 {kind}")
print("接入 pre-commit 与 CI:发现即阻断;已泄露先轮换凭证再清历史")
```

**追问**:
- 追问 1:误报高怎么办?—— 优先精确规则(已知前缀)、熵阈值过滤、白名单标注责任人,而不是关掉扫描。
- 追问 2:依赖审计怎么避免"每天红着也没人管"?—— 只阻断新增高危(基线存量登记豁免),升级窗口自动提 PR 修复,让红有出口。
