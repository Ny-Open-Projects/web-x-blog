---
title: [A264] 双令牌体系：refresh 轮换与重放检测、注销黑名单与多端挤下线
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A264 · 单点登录的令牌体系设计

> 难度:★★★★ | 标签:双令牌, JWT, refresh 轮换, 重放检测, 注销黑名单, 多端挤下线

**问**（笔试·场景题）：A181 已回答「OIDC 怎么接入、SSO 会话与应用会话怎么分离」，A126 已回答「签名密钥怎么轮换」——本题只咬住**令牌本体的生命周期：发、续、转、废、踢**。自研一套 access + refresh 双令牌体系，要求：① access 短命、无状态可验（JWT 形态，HMAC 签名），refresh 长命、**有状态可吊销**——先说清为什么注定了这个不对称；② refresh **轮换**：每次续期旧 refresh 作废、发新的，客户端**重放已轮换的 refresh** 必须被识别并**整族吊销**（宁可全端重新登录，不可放过盗号）；③ 注销要真注销：access 无状态是它的优点也是它的死穴，注销必须落到 **jti 黑名单**，且黑名单条目要自动过期（TTL = 剩余有效期），不能无限膨胀；④ 多端挤下线：同一账号手机/平板多设备在线，支持「踢指定设备」与「踢全部设备」，且**已签发的 access 不等过期就立刻失效**（token 不能改，怎么让它作废？）；⑤ 篡改签名、过期、注销、被踢四类请求全部拒绝且错误可区分。请说清与 A181（OIDC 流程与会话关系）、A126（kid 密钥轮换）、A252（时间轮过期）的分工。

**答**：① 不对称的根源是**信任模型**：access 发出去之后谁都不查（无状态，每个网关本地验签，省一次 RTT），所以它的「有效期」必须短到——被偷了也只能偷到十几分钟的窗口；refresh 恰恰相反，它只在续期端点出现、必须每次查库（有状态），换来的是**随时可吊销**。反过来配（access 长命 + refresh 短命）是最常见的设计错误：等于把「随时踢人」的能力丢了，注销全靠等过期。② 轮换协议：`refresh(rt)` 只接受**当前值**；成功后旧值进 `_used` 历史、新值下发。重放检测的判定是「这个 rt 在某个族的已轮换历史里出现过」——正常用户手里只有最新值，再次出示旧值只可能是两种人：网络重试（罕见）或**偷到旧值的攻击者**（他在和真用户赛跑）。处理不能只拒绝这一次：**整族吊销**（该登录族所有端全部失效），用一次强制的重新登录换掉「攻击者持有效 refresh 长期续命」。这是把「检测到异常」升级成「消灭攻击者的资产」，也是 OAuth BCP（best current practice）明确要求的动作。宽限窗口（旧值放行几秒再作废）可以缓解弱网重试误杀，但窗口内攻击者同样受益，代价要向业务明说。③ 注销黑名单：access 的 payload 里必须带 **jti**（唯一 ID，没有 jti 就没有可注销的粒度）。注销 = `blacklist[jti] = exp`；验证端查一次即可。两个工程要点：**TTL = 剩余有效期**——条目活过 exp 之后永远不会再匹配到任何合法请求，不删就是纯泄漏（长时间运行的注销服务，黑名单只增不减是最典型的慢性内存事故）；**查询发生在验签之后**——先做免费的本地验签，黑名单才有资格引入一次外部查询，顺序反了等于把最贵的检查放在最前面。本题实现里黑名单在验证时顺手清扫过期条目。④ 多端挤下线：token 签发后改不了，唯一办法是让它**引用一个可变的服务端事实**。本题在 payload 里放 `dv`（设备版本号），服务端按 `(uid, device)` 维护当前版本；踢设备 = 版本 +1，所有持旧 `dv` 的 access 验证时立刻失配。这一招的通用形态是「**短命引用 + 服务端版本**」，会话、API key、Webhook secret 全适用。踢设备的级联动作不能漏：该设备的 refresh 族同步吊销——只踢 access 不踢 refresh，被踢的端 15 分钟后自己续期复活，这是挤下线最常翻车的点。⑤ 错误可区分是可运维性的底线：签名无效（密钥问题/伪造）、过期（正常轮转）、已注销（用户主动）、版本失配（被踢）是四种**完全不同的处置**（前者要报警，中间两个是正常流，最后一个前端要弹「已在别处登录」）——共用一个「token 无效」会把排查变成玄学。本题用 `AuthError` 细分消息，实测逐类断言。

```python
# 全部标准库；双令牌体系：HMAC 签名 access + refresh 轮换重放检测 + jti 黑名单 + 设备版本挤下线
import base64
import hashlib
import hmac
import json
import secrets


def b64u(raw):
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def b64u_dec(text):
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


class AuthError(ValueError):
    """拒绝原因可区分：签名无效 / 过期 / 已注销 / 被挤下线 / refresh 异常。"""


class TokenService:
    """access 短命无状态（本地验签），refresh 长命有状态（可吊销、可轮换）。"""

    def __init__(self, secret, access_ttl=600, refresh_ttl=1209600):
        self.secret = secret
        self.access_ttl = access_ttl
        self.refresh_ttl = refresh_ttl
        self.now = 1_700_000_000               # 固定时钟，测试可复现
        self._refresh = {}                     # rt -> {"uid","device","family"}
        self._family = {}                      # family -> {"current","uid","device"}
        self._used = {}                        # family -> set(已轮换历史)，重放检测依据
        self._blacklist = {}                   # jti -> exp（TTL=剩余有效期）
        self._dv = {}                          # (uid, device) -> 设备版本号

    def tick(self, seconds):
        self.now += seconds

    # ---------- 签发 ----------
    def _jwt(self, payload):
        head = b64u(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
        body = b64u(json.dumps(payload).encode())
        sig = b64u(hmac.new(self.secret, ("%s.%s" % (head, body)).encode(),
                            hashlib.sha256).digest())
        return "%s.%s.%s" % (head, body, sig)

    def issue(self, uid, device):
        key = (uid, device)
        self._dv[key] = self._dv.get(key, 0) + 1
        family = secrets.token_urlsafe(8)      # 一次登录 = 一个令牌族
        rt = secrets.token_urlsafe(32)
        self._family[family] = {"current": rt, "uid": uid, "device": device}
        self._used[family] = set()
        self._refresh[rt] = {"uid": uid, "device": device, "family": family}
        return self._access(uid, device), rt

    def _access(self, uid, device):
        payload = {"sub": uid, "dev": device, "dv": self._dv[(uid, device)],
                   "jti": secrets.token_urlsafe(9),
                   "iat": self.now, "exp": self.now + self.access_ttl}
        return self._jwt(payload)

    # ---------- 验证：验签（免费）→ 过期 → 黑名单 → 设备版本 ----------
    def verify(self, token):
        try:
            head, body, sig = token.split(".")
        except ValueError:
            raise AuthError("token 结构非法")
        signing_input = ("%s.%s" % (head, body)).encode()
        expect = b64u(hmac.new(self.secret, signing_input, hashlib.sha256).digest())
        if not hmac.compare_digest(sig, expect):
            raise AuthError("签名无效")
        payload = json.loads(b64u_dec(body))
        if payload["exp"] < self.now:
            raise AuthError("access 已过期")
        for jti in [j for j, exp in self._blacklist.items() if exp <= self.now]:
            del self._blacklist[jti]           # 条目活过 exp 即垃圾，顺手清扫
        if payload["jti"] in self._blacklist:
            raise AuthError("access 已注销")
        if payload["dv"] != self._dv.get((payload["sub"], payload["dev"])):
            raise AuthError("设备版本不匹配（被挤下线）")
        return payload

    # ---------- 续期：轮换 + 重放检测 ----------
    def refresh(self, old_rt):
        rec = self._refresh.get(old_rt)
        if rec is not None:
            family = rec["family"]
            if old_rt != self._family[family]["current"]:
                self.revoke_family(family)
                raise AuthError("refresh 状态异常，令牌族已吊销")
            del self._refresh[old_rt]
            self._used[family].add(old_rt)
            new_rt = secrets.token_urlsafe(32)
            self._family[family]["current"] = new_rt
            self._refresh[new_rt] = rec
            return self._access(rec["uid"], rec["device"]), new_rt
        for family, used in self._used.items():
            if old_rt in used:                 # 已轮换历史里出现 → 重放，整族吊销
                self.revoke_family(family)
                raise AuthError("refresh 重放，令牌族已吊销")
        raise AuthError("refresh 不存在")

    # ---------- 注销 / 挤下线 ----------
    def logout(self, payload, rt=None):
        self._blacklist[payload["jti"]] = payload["exp"]   # TTL = 剩余有效期
        if rt is not None:
            rec = self._refresh.pop(rt, None)
            if rec:
                self.revoke_family(rec["family"])

    def revoke_family(self, family):
        for rt in [r for r, v in self._refresh.items() if v["family"] == family]:
            del self._refresh[rt]
        self._family.pop(family, None)
        self._used.pop(family, None)

    def kick(self, uid, device=None):
        """挤下线：设备版本 +1（旧 access 立刻失配），该端 refresh 族级联吊销。"""
        targets = [(uid, device)] if device else [k for k in self._dv if k[0] == uid]
        for key in targets:
            self._dv[key] = self._dv.get(key, 0) + 1
            for rt in [r for r, v in self._refresh.items()
                       if (v["uid"], v["device"]) == key]:
                rec = self._refresh.pop(rt)
                self.revoke_family(rec["family"])


def expect_error(fn, frag):
    try:
        fn()
    except AuthError as e:
        assert frag in str(e), (frag, str(e))
        return
    raise AssertionError("应当拒绝: %s" % frag)


if __name__ == "__main__":
    svc = TokenService(b"dev-secret")

    # 1) 正常签发与验证
    at, rt = svc.issue("alice", "phone")
    assert svc.verify(at)["sub"] == "alice"
    print("签发验签: access 本地验签通过 ✅")

    # 2) 过期 → refresh 轮换续命，新 rt 不同于旧 rt
    svc.tick(601)
    expect_error(lambda: svc.verify(at), "过期")
    at2, rt2 = svc.refresh(rt)
    assert rt2 != rt and svc.verify(at2)["sub"] == "alice"
    print("过期续期: refresh 轮换拿到新 access/新 rt ✅")

    # 3) 重放旧 rt → 整族吊销：新 rt 一起陪葬（续命能力归零）
    expect_error(lambda: svc.refresh(rt), "重放")
    expect_error(lambda: svc.refresh(rt2), "不存在")          # 族已吊销，新 rt 也无主
    assert svc.verify(at2)["sub"] == "alice"                  # access 不受族吊销影响
    print("重放检测: 旧 rt 重放触发整族吊销，续命已断、攻击者无法长期续命 ✅")

    # 4) 注销：access 不等过期立刻失效，refresh 同步回收
    at3, rt3 = svc.issue("bob", "pad")
    svc.logout(svc.verify(at3), rt3)
    expect_error(lambda: svc.verify(at3), "注销")
    expect_error(lambda: svc.refresh(rt3), "不存在")
    assert all(exp > svc.now for exp in svc._blacklist.values())   # 黑名单无过期残留
    print("真注销: jti 进黑名单立即生效，refresh 族回收 ✅")

    # 5) 多端挤下线：踢手机不影响平板；踢全部则全灭
    ph, _ = svc.issue("carol", "phone")
    pd, _ = svc.issue("carol", "pad")
    svc.kick("carol", "phone")
    expect_error(lambda: svc.verify(ph), "挤下线")
    assert svc.verify(pd)["dev"] == "pad"
    svc.kick("carol")
    expect_error(lambda: svc.verify(pd), "挤下线")
    print("多端挤下线: 踢指定设备精准生效，全踢级联吊销 refresh ✅")

    # 6) 篡改签名被拒（错误类型与过期/注销可区分）
    bad = at[:-3] + ("aaa" if not at.endswith("aaa") else "bbb")
    expect_error(lambda: svc.verify(bad), "签名无效")
    print("防篡改: 比较签名用 hmac.compare_digest，拒绝原因可区分 ✅")
```

**追问**：1) access TTL 多短才合适？—— 三个约束一起压：**被盗窗口**（越短越好，常见 5-15 分钟）、**refresh 端点压力**（TTL 60 秒意味着每分钟全量用户打一次续期，要么做静默续期——前端拦截器发现快过期就后台换，要么单飞合并——同用户并发请求只放一个 refresh 过去，其余等结果）；**分布式时钟漂移**（多签发方时要把 exp 预留 30-60 秒验证缓冲，否则节点间钟差会造成「刚签出来就过期」）。给出原则：TTL 由「你能接受的最大失窃损失」定，而不是由「用户体验」定——体验问题用静默续期解决，安全问题没有银弹。2) 并发 refresh 竞态：同一 rt 被两个请求同时用怎么办？—— 本题实现是查改非原子，生产必须把「读 current → 比较 → 写 current」做成**单次原子操作**（Redis Lua 或 DB 行锁 compare-and-swap）：恰好一个请求赢，另一个拿到「rt 已轮换」。难点在**误杀**：赢的请求还没把新 access 送回，输的请求是同用户的正常并发——所以 BCP 建议给「已轮换 rt」一个几秒宽限，窗口内重放放行旧值最后已知响应而不是触发吊销；窗口外才是真重放。宽限值 = 新 access 送达客户端的最大时延，5 秒起步。3) 黑名单为什么不直接「user 级版本号」替代 jti？—— user 级版本一加就全体下线（粒度太粗），jti 才能只废一张票。但黑名单也有它的反面：**验证路径引入了一次外部查询**，规模化时要么网关本地缓存黑名单（布隆过滤器粗筛 + 命中才查 Redis，假阳性无害——多查一次，注意这里布隆的误差方向恰好是安全的），要么接受「注销延迟 = 缓存 TTL」。另一个方向是极短 access（30 秒）+ 不做黑名单，注销等它自然过期——大量团队最后真的选了这条，因为运维成本最低；这是「体验/安全/运维」三角的取舍，没有唯一正解。

## 背诵要点
1. 不对称根源：access 无状态可验但不可废 → 短命；refresh 有状态可吊销 → 长命；access payload 必须带 jti 和 dv（设备版本）。
2. refresh 轮换：只认 current，旧值进已轮换历史；重放 = 旧值再出现 → 整族吊销（宁可全端重登，不可放过盗号）。
3. 注销 = jti 黑名单（TTL=剩余有效期，验签后才查）；挤下线 = 设备版本 +1 + 该端 refresh 族级联吊销；四类拒绝原因必须可区分。
