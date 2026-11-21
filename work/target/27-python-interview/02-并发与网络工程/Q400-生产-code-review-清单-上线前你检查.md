---
title: [Q400] 生产 code review 清单:上线前你检查什么
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q400 · 生产 code review 清单:上线前你检查什么

> 难度:★★★ | 标签:code review, 工程规范, 上线

**问**:作为 reviewer,一份要上生产运行的 Python 改动,你会按什么清单检查?

**答**:结合业界 checklist,按优先级过六层:①正确性——逻辑边界、异常是否捕获具体类型(禁止裸 `except:`)、失败路径是否处理;②资源与并发——超时、连接池、锁、幂等、优雅停机;③安全——不硬编码密钥、输入校验、SQL/命令注入、日志脱敏;④可观测性——关键路径有结构化日志与指标、错误带上下文;⑤测试——单测覆盖成功与失败分支、边界值,lint/type check 通过;⑥依赖与兼容——新依赖的必要性、Python 版本兼容、迁移脚本可回滚。AI 辅助生成的代码同样按此清单,尤其要审"看起来对但没有错误处理"的片段。

```python
# file: code/02_并发与网络工程/q400_review_checklist.py
"""code review 清单的自检脚本骨架:静态检查 + 风险模式扫描。"""
import ast
import sys

RISKY_PATTERNS = {
    "eval": "禁止 eval 动态执行",
    "exec": "禁止 exec 动态执行",
    "shell=True": "禁止 shell=True 拼接命令",
    "except:": "禁止裸 except",
    "password = \"": "疑似硬编码密码",
    "verify=False": "禁止关闭 TLS 校验",
    "utcnow": "utcnow 已废弃, 用 now(timezone.utc)",
}


def scan_source(code: str) -> list:
    findings = []
    for lineno, line in enumerate(code.splitlines(), 1):
        for pattern, msg in RISKY_PATTERNS.items():
            if pattern in line:
                findings.append(f"L{lineno}: {msg} -> {line.strip()}")
    # 语法层面: 能解析才继续
    try:
        ast.parse(code)
    except SyntaxError as e:
        findings.append(f"语法错误: {e}")
    return findings


SAMPLE = '''
import subprocess
def run(user):
    try:
        subprocess.run("ping " + user, shell=True)
    except:
        pass
secret = "hunter2"
'''

if __name__ == "__main__":
    findings = scan_source(SAMPLE)
    for f in findings:
        print("[风险]", f)
    print("共发现", len(findings), "处, 均需在上线前修复")
    # 演示脚本固定 exit 0; 接入 CI 时改为 sys.exit(1 if findings else 0) 阻断合并
    sys.exit(0)
```

**追问**:
- 裸 `except: pass` 为什么是最恶劣的反模式?吞掉一切异常包括 KeyboardInterrupt/SystemExit,错误无迹可查;至少 `except Exception as e: logger.exception(e)`。
- 如何把清单自动化?pre-commit 钩子跑 ruff/mypy/bandit/secret 扫描,CI 阻断高危项,人只审逻辑与设计——清单里能自动化的都不该靠人眼。
