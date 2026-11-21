---
title: [Q7083] CI artifact 泄漏 .env 事故复盘
date: 2026-11-20
categories: [Python数据分析与工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7083 · CI artifact 泄漏 .env 事故复盘

难度：P6 ｜ 标签：CI/CD / 安全 / 事故复盘

**问**：一次 CI 失败排查时，同事下载了构建 artifact 调试，发现里面有 `.env`（含生产密钥）。密钥怎么进到 artifact 的？如何复盘与防复发？

**答**：
- **结论**：根因是 CI 配置里 `upload-artifact` 上传了整个工作目录（`path: .`）或通配过宽（`path: dist/**` 之外还有 `.env` 被 `**` 命中），而 pipeline 的密钥注入（`secrets` → 写入 `.env` 文件 → 应用读取）让密钥落了盘。artifact 的可见性往往比代码仓库宽（Fork PR 可触发的工作流、长期保留策略），于是"排障用的产物"成了泄漏面。
- **取舍**：修复取舍在"上传粒度 vs 排障效率"：只上传明确的制品目录（`dist/`、`coverage.xml`）最安全，但失败时缺上下文——折中是失败分支才上传受限的诊断包（白名单文件列表 + 排除 `.*`），并把保留期从 90 天压到 7 天。更深一层的取舍：生产密钥根本不应进 CI 工作目录，改为运行时从 secret manager 拉取（vault/OIDC 短令牌），CI 里只持有 5 分钟有效期的临时凭证。
- **实战**：复盘四步：① 立即吊销泄漏密钥并轮换（先止血）；② 审计 artifact 访问日志确认读取面；③ 改 workflow 白名单上传 + 加 secret 扫描门禁（gitleaks/trufflehog 扫 artifact 内容再上传）；④ 密钥注入方式改为 OIDC 短令牌 + 运行时拉取，工作目录里不再出现 `.env`。

```python
# artifact 上传前的白名单过滤器 + 密钥扫描门禁（纯标准库）
# 基线：Python 3.9+

import fnmatch
import re

ALLOW = ["dist/**", "reports/**", "coverage.xml", "pytest-results.xml"]
SECRET_PAT = re.compile(
    r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"
)


def pick_files(paths: list[str]) -> list[str]:
    picked = []
    for p in paths:
        if any(fnmatch.fnmatch(p, pat) for pat in ALLOW):
            picked.append(p)
    return picked


def secret_scan(contents: dict[str, str]) -> list[str]:
    return [n for n, text in contents.items() if SECRET_PAT.search(text)]


def main() -> None:
    files = ["dist/app.whl", ".env", "src/.env.local", "coverage.xml", "reports/junit.xml"]
    print("上传:", pick_files(files))
    assert pick_files(files) == ["dist/app.whl", "coverage.xml", "reports/junit.xml"]

    contents = {"reports/junit.xml": "<testsuite/>",
                "dist/config.py": "API_KEY='sk-live-abcdef1234567890ab'"}
    leaks = secret_scan(contents)
    print("密钥命中:", leaks)
    assert leaks == ["dist/config.py"]  # 命中则拒绝上传


if __name__ == "__main__":
    main()
```

**追问 1**：为什么说"secrets 写入 .env 文件"这个模式本身就有问题？
→ 一句话提示：秘密一旦落盘就脱离了 CI 的 secret 审计与日志脱敏体系（CI 会自动掩码日志中的 secret 值，但不会扫文件内容），任何后续步骤都能读到它。

**追问 2**：Fork PR 能触发的工作流为什么风险更高？
→ 一句话提示：fork PR 的 workflow 运行环境可能拿到仓库 secret（若配置不当）且 PR 作者不受仓库权限约束，artifact 或日志可能被陌生人下载，所以 fork 场景必须关 secret 注入。

## 背诵要点
- 根因链：secrets → 写 .env → 宽通配上传 artifact → 下载者拿到密钥。
- 修复优先级：吊销轮换 > 访问审计 > 白名单上传（排除点文件）> secret 扫描门禁 > OIDC 短凭证根治。
- artifact 保留期也是攻击面：90 天默认值应压到 7 天以内。

## 复盘追问
- 为什么"日志掩码"防不住这类泄漏？提示：掩码只作用于标准输出，文件内容与 artifact 不在掩码范围。
- 如何在流程上保证以后新增上传路径不引入泄漏？提示：workflow 改动强制 code review + CI 配置 lint（actionlint）+ 定期对存量 artifact 抽样扫描。
