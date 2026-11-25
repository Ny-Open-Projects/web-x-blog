---
title: [A181] 内部工具 SSO 统一认证：一次登录到处通行
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A181 · 内部工具 SSO

> 难度:★★☆ | 标签:SSO, OIDC, 治理

**问**（笔试·编程+场景题）：内部 20 个工具各有登录（20 套账号密码）——SSO（OIDC）统一认证怎么接入（授权码流程），「一次登录到处通行」的会话关系（SSO 会话 vs 各应用会话），SSO 挂了全站都登录不了怎么降级，僵尸工具（离职员工的账号还能登）怎么治理？

**答**：① OIDC 授权码流程：用户访问工具 A → A 重定向到 SSO（IdP）→ 用户在 IdP 登录（一次）→ IdP 带授权码回 A → A 用授权码换 token（后端对 IdP）→ A 建立自己的会话——「SSO 会话」（IdP 的 cookie）与「应用会话」（各工具自己的）分离：登录一次后访问工具 B 无需再输密码（IdP 会话还在），但 B 的应用会话是独立的（B 注销不影响 A）。② SSO 单点故障降级：IdP 挂了全站登录不了——降级方案：各工具保留「本地紧急账号」（break-glass，双人审批激活+全量审计）、已登录会话不受影响（应用会话独立——这就是 ①分离的意义）、IdP 自身高可用（IdP 是 Tier-0 服务）。③ 僵尸账号治理：SSO 接 HR 系统（离职自动禁用）——这是 SSO 的隐藏最大收益：20 个工具各自管账号永远漏（离职员工僵尸账号是渗透测试必中项）；工具接入 SSO 时强制迁移 = 账号治理一次到位。

```python
# 全部标准库；demo 实现「授权码流程 + break-glass + 会话分离」
import hmac, hashlib, json, time, secrets

class IdP:
    """最小 OIDC IdP：授权码 + token 换发。"""
    def __init__(self):
        self.sso_session: dict[str, str] = {}       # sso_cookie -> user
        self.codes: dict[str, tuple[str, str]] = {} # code -> (user, client, exp)
        self.clients = {"tool-a": "secret-a", "tool-b": "secret-b"}
    def login(self, user: str, password: str) -> str:
        assert password == "correct"                # demo 固定密码
        sid = secrets.token_urlsafe(16)
        self.sso_session[sid] = user
        return sid
    def authorize(self, sso_cookie: str, client: str) -> str | None:
        if sso_cookie not in self.sso_session:
            return None                             # IdP 会话不在 → 要重新登录
        code = secrets.token_urlsafe(16)
        self.codes[code] = (self.sso_session[sso_cookie], client, time.time() + 60)
        return code
    def exchange(self, code: str, client: str, secret: str) -> dict | None:
        c = self.codes.pop(code, None)              # 授权码一次性（pop）
        if not c or c[1] != client or time.time() > c[2]:
            return None
        assert hmac.compare_digest(secret, self.clients[client])
        return {"user": c[0], "app_session": secrets.token_urlsafe(16)}  # 应用会话独立

class BreakGlass:
    """紧急本地账号：双人审批激活 + 全量审计 + 24h 自动失效。"""
    def __init__(self):
        self.active: dict[str, float] = {}
        self.audit: list[str] = []
    def activate(self, user: str, approver1: str, approver2: str) -> bool:
        if approver1 == approver2:
            self.audit.append(f"拒绝：{user} 双人审批不能同一人")
            return False
        self.active[user] = time.time() + 24 * 3600
        self.audit.append(f"{time.strftime('%m-%d %H:%M')} BREAK-GLASS: {user} 激活（{approver1}+{approver2}）")
        return True
    def usable(self, user: str) -> bool:
        return self.active.get(user, 0) > time.time()

if __name__ == "__main__":
    idp = IdP()
    sid = idp.login("zhang", "correct")
    code = idp.authorize(sid, "tool-a")
    sess = idp.exchange(code, "tool-a", "secret-a")
    assert sess and sess["user"] == "zhang"
    # 一次登录：访问 tool-b 无需再登录（IdP 会话仍有效）
    code_b = idp.authorize(sid, "tool-b")
    sess_b = idp.exchange(code_b, "tool-b", "secret-b")
    assert sess_b and sess_b["user"] == "zhang"
    print("SSO 一次登录：tool-a/tool-b 免密通行，应用会话独立 ✅")
    bg = BreakGlass()
    assert bg.activate("ops", "a", "a") is False        # 双人不能同一人
    assert bg.activate("ops", "a", "b") is True
    print("break-glass：双人审批激活 + 24h 自动失效 ✅（audit:", len(bg.audit), "条）")
    # 口径：授权码一次性 pop + 时效 60s；会话两层分离（IdP/应用）；
    # IdP=Tier-0 + break-glass 降级；接 HR 系统消灭僵尸账号。
```

**追问**：1) 为什么授权码要「一次性 pop + 60 秒时效」？——授权码出现在 URL（浏览器历史/日志/referrer），被截获的码必须不可重用：pop 保证一次性、60s 限制截获窗口；token 交换走后端（client_secret）不经过浏览器——这是授权码流程比隐式流程安全的根本。2) 「应用会话独立」为什么是 SSO 可用性的关键？（提示：IdP 挂了已登录的应用会话仍有效（不影响在用用户），只有新登录受影响——会话分离把 IdP 故障的影响面从「全站全员」缩到「新登录」；全站会话绑 IdP 的设计是 SSO 单点事故的根源）3) 工具接入 SSO 的迁移顺序怎么定？（提示：按「账号风险 × 使用频率」——有敏感数据的高频工具先接（僵尸账号风险最大）、边缘工具后接；每接入一个消灭一批僵尸账号，治理收益递增）

## 背诵要点
1. OIDC 授权码流程：授权码一次性 pop + 60s 时效 + 后端 token 交换——码泄露不可重用。
2. 会话两层分离：IdP 会话（一次登录）+ 应用会话（各自独立）——IdP 故障影响面缩到「新登录」。
3. SSO = 认证统一 + 账号治理（接 HR 离职自动禁用）；break-glass 双人审批 + 24h 自动失效 + 全量审计。

## 复盘追问
1. 离职 3 个月的员工账号还能登某个工具——SSO 之后还会有吗？（提示：SSO 账号源接 HR 会消灭「目录内」僵尸；但漏网的是「未接入 SSO 的工具」和「本地建的历史账号」——治理要盘点全量工具清单（Q172 内部工具平台），接入率是 SSO 项目的核心 KPI）
2. break-glass 账号被滥用（每周都用），审计发现后怎么收紧？（提示：滥用说明「正常通道有障碍」（SSO 太慢/权限太少）——先修正常通道体验，再收紧 break-glass；每次使用必须关联工单（无工单的 break-glass 自动告警））
