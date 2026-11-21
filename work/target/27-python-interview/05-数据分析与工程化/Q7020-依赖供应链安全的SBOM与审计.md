---
title: [Q7020] 依赖供应链安全：SBOM 与审计闸门
date: 2026-11-19
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7020 · 依赖供应链安全

> 难度:★★☆ | 标签:供应链, SBOM, 安全

**问**：某热门包被投毒（typosquatting）或维护者被攻击（如 xz 事件模式），你的服务多久能知道、多久能止血——SBOM 是什么、为什么锁文件（Q7014）是它的基础？私有源/内部镜像怎么搭，CI 里依赖审计闸门该挡什么？

**答**：① **SBOM**（软件物料清单）：每个构建产物列出「用了哪些依赖的哪些版本、来自哪个源」——事故响应的第一步是「查我们有没有」，没有 SBOM 就要人工全仓排查（小时级），有则一条查询（分钟级）。Python 侧 SBOM 从 `uv.lock`/`pip freeze` 生成（CycloneDX 格式），构建时自动产出并归档。② **审计闸门三层**：构建时校验哈希（锁文件含每个包的 sha256，镜像源内容不一致即拒绝——防传输篡改）、CVE 扫描（pip-audit/osv-scanner 挡已知漏洞版本）、异常检测（新包名相似度检查防 typosquatting：`requests` vs `reqeusts`、维护者变更告警）。③ **私有源**：全部依赖经内部 PyPI 镜像（devpi/Nexus/uv index），外网包先经镜像审核进内网——单点出口让「允许哪个包进」变成可管理决策；紧急止血 = 镜像层下架包 + 锁文件 pin 前一版本。

```python
# 全部标准库；demo 实现「SBOM 生成 + typosquat 检查 + 哈希审计」
import difflib, hashlib, json, re

KNOWN_TOP = {"requests", "flask", "fastapi", "pydantic", "numpy", "sqlalchemy",
             "click", "uvicorn", "redis", "httpx"}      # 简化：生产用 PyPI 全量榜单

def build_sbom(lock_resolved: dict[str, str], index_url: str) -> dict:
    """从锁文件生成 CycloneDX 风格 SBOM。"""
    return {"bomFormat": "CycloneDX", "components": [
        {"name": p, "version": v, "purl": f"pkg:pypi/{p}@{v}",
         "source": index_url, "hash": hashlib.sha256(f"{p}{v}".encode()).hexdigest()[:12]}
        for p, v in sorted(lock_resolved.items())]}

def typosquat_check(pkg: str, known: set[str], cutoff: float = 0.88) -> str | None:
    """typosquatting：与知名包名过近但不在白名单 → 拦截人工确认。"""
    if pkg in known:
        return None
    m = difflib.get_close_matches(pkg, known, n=1, cutoff=cutoff)
    return f"疑似仿冒 {m[0]}（相似度过高）" if m else None

def audit_gate(sbom: dict, blocklist: set[str]) -> list[str]:
    """CI 闸门：黑名单版本 + 哈希校验。"""
    issues = []
    for c in sbom["components"]:
        if c["name"] in blocklist:
            issues.append(f"CVE 黑名单: {c['name']}=={c['version']}")
        expect = hashlib.sha256(f"{c['name']}{c['version']}".encode()).hexdigest()[:12]
        if c["hash"] != expect:
            issues.append(f"哈希不一致（传输篡改？）: {c['name']}")
    return issues

if __name__ == "__main__":
    lock = {"requests": "2.32.3", "reqeusts": "0.1.0", "flask": "3.0.0"}  # 混入仿冒包
    sbom = build_sbom(lock, "https://pypi.internal.corp/simple")
    print("SBOM 组件数:", len(sbom["components"]))
    hits = [c["name"] for c in sbom["components"]
            if (t := typosquat_check(c["name"], KNOWN_TOP))]
    print("typosquat 拦截:", hits or "无")
    assert "reqeusts" in hits                     # 仿冒包被识别 ✅
    print("审计闸门:", audit_gate(sbom, blocklist={"requests==2.32.2"}) or "通过")
    # 事故响应口径：CVE 公告 → SBOM 查询受影响服务（分钟级）→ 镜像下架/锁 pin →
    # 全仓升级 → 演练验证。没有 SBOM 的组织此流程从小时起步。
```

**追问**：1) 为什么镜像源比「CI 里直接 pip install 公网」安全？——单点出口 + 审核前置：外网包先进镜像隔离区（新包延迟 N 天可用——投毒包存活窗口通常极短，延迟即免疫）+ 哈希审计后才进可用区；直接公网安装则每次构建都是信任赌注。2) `hash-checking mode`（pip --require-hashes）的价值？——锁文件含哈希时安装强制校验：传输篡改/镜像不一致/锁外包全部拒绝——供应链的最小技术防线。3) xz 类「维护者社工攻击」怎么防？——技术手段有限（长线潜伏伪装正常贡献），防线是：关键依赖多方冗余（同一功能双实现备选）、行为异常审计（新维护者突然接手核心包）、只升级经评估的版本（不追 latest）。

## 背诵要点
1. SBOM = 构建产物自动产出（锁文件→CycloneDX），事故响应「查有没有」从小时级变分钟级。
2. 审计三层：锁哈希校验（--require-hashes）+ CVE 扫描（pip-audit）+ typosquat 相似度拦截。
3. 私有镜像单点出口：新包延迟可用（投毒窗口免疫）、下架止血、审核记录可审计。

## 复盘追问
1. 紧急 CVE 来了但升级包有 breaking change，48 小时内怎么决策？（提示：SBOM 查影响面 → 临时缓解（WAF 规则/禁用功能路径）优先于盲目升级 → 评估分支升级 → 回归验证）
2. 内部包自己发到私有源，审计链怎么补全？（提示：内部包同样签名+SBOM+版本审批流程——「内部包无风险」是错觉，内部投毒（离职员工权限）真实存在）
