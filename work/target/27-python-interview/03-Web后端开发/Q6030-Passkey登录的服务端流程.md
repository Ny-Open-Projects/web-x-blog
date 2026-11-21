---
title: [Q6030] Passkey/WebAuthn 登录：挑战-应答的服务端流程
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6030 · Passkey/WebAuthn 登录：挑战-应答的服务端流程

> 难度:★★★★☆ | 标签:WebAuthn, Passkey, 认证

**问**：Passkey 登录替代"密码+OTP"的核心机制是什么——服务端必须校验哪几样东西，哪几样绝对不能信客户端？challenge 为什么必须服务端生成、一次性、短 TTL？signCount 防什么？Python 侧落地怎么分"自己校验"与"用 fido2/py_webauthn 库"两条路？

**答**：Passkey = WebAuthn 的公钥凭据：私钥留在用户设备（认证器），服务端只存公钥。登录流程（assertion）：1) 服务端生成 **challenge**（≥16 字节随机数），与用户会话绑定存服务端，标记**未使用 + 短 TTL（~60s）**——它是防重放的核心：服务端只信"自己刚发、只用一次、没过期"的挑战；2) 认证器用私钥对 `authenticatorData || SHA256(clientDataJSON)` 签名返回；3) 服务端逐项校验（**全部服务端判定**）：`clientDataJSON.challenge` 与发出的逐字节相等；`clientData.origin` 等于自己的 origin（防中间人换站）；`type` 等于 `webauthn.get`；`authenticatorData` 的 **rpIdHash**（SHA256(rpId)）正确（凭据只在注册域有效）；签名用**服务端存的公钥**验签通过；`signCount` **大于上次值**——认证器用它探测克隆凭据（克隆体的计数器可能倒退或不增，可疑即触发风控/吊销）。注册（attestation）阶段同理，额外校验凭据公钥格式（COSE）与 RP ID。落地路线：生产直接用 `py_webauthn`/`fido2`（python-fido2 基线 1.x）——COSE/attestation 解析非常容易写错；理解流程是面试重点，下面用标准库演示校验骨架（签名用 HMAC 代替真实 ES256，标注降级）。

```python
# file: code/03_Web后端开发/q6030_passkey_flow.py
import base64, hashlib, hmac, json, os

def b64u(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()

class RelyingParty:                     # RP: 你们的 Web 服务端
    def __init__(self, rp_id, origin):
        self.rp_id, self.origin = rp_id, origin
        self.pending = {}               # challenge 会话台账: 未使用+短TTL
        self.creds = {}                 # credentialId -> {"key":..., "count": int}

    def begin(self, user) -> str:
        ch = os.urandom(32)             # >=16 字节 CSPRNG
        self.pending[user] = {"challenge": ch, "used": False}
        return b64u(ch)                 # 下发给浏览器(应答里必须逐字节一致)

    def _check_challenge(self, user, client):
        s = self.pending.get(user)
        assert s and not s["used"], "challenge 已用/不存在(重放)"
        s["used"] = True                # 单次消费
        assert client["challenge"] == b64u(s["challenge"]), "challenge 不匹配"
        assert client["origin"] == self.origin, "origin 不匹配(钓鱼站)"
        assert client["type"] in ("webauthn.get", "webauthn.create"), "type 错误"

    def _check_rp_id(self, auth_data):
        assert auth_data[:32] == hashlib.sha256(self.rp_id.encode()).digest(), "rpIdHash 不符"

    def verify_login(self, user, cred_id, client, auth_data, sig):
        self._check_challenge(user, client)
        self._check_rp_id(auth_data)
        cred = self.creds[cred_id]
        count = int.from_bytes(auth_data[33:37], "big")     # flags 1B + signCount 4B
        assert count > cred["count"], "signCount 未递增 -> 克隆凭据嫌疑,触发风控"
        cred["count"] = count
        expect = hmac.new(cred["key"],
                          auth_data + hashlib.sha256(json.dumps(client).encode()).digest(),
                          hashlib.sha256).digest()          # 真实为 ES256,需 fido2/py_webauthn
        assert hmac.compare_digest(sig, expect), "签名不符"
        return True

rp = RelyingParty("example.com", "https://example.com")
sk = os.urandom(32)                     # 演示: 私钥的替身(真实私钥永不离开设备)
client_data = {"type": "webauthn.get", "challenge": None, "origin": "https://example.com"}
challenge = rp.begin("ann")
client_data["challenge"] = challenge
auth_data = hashlib.sha256(b"example.com").digest() + b"\x05" + (1).to_bytes(4, "big")
sig = hmac.new(sk, auth_data + hashlib.sha256(json.dumps(client_data).encode()).digest(),
               hashlib.sha256).digest()
rp.creds["cred-1"] = {"key": sk, "count": 0}
print("登录校验:", rp.verify_login("ann", "cred-1", client_data, auth_data, sig))
try:
    rp.verify_login("ann", "cred-1", client_data, auth_data, sig)   # 同一 challenge 重放
except AssertionError as e:
    print("重放被拒:", e)
```

**追问**：1) challenge 能让客户端生成吗？——绝对不能：客户端生成则服务端无法防重放（同一应答可无限复用），challenge 必须服务端随机、会话绑定、单次消费。2) 为什么 origin 与 rpIdHash 都要查？——origin 防"认证器被诱到钓鱼站签名"（域不匹配即拒），rpIdHash 防凭据跨站复用（凭据按 RP ID 作用域绑定），两层独立。3) signCount 恒为 0 的认证器（如某些平台 authenticator）怎么办？——部分认证器不实现计数器（count 恒 0），注册时记录该特性，验证时跳过递增断言、改用设备指纹/风控补偿，不要一刀切拒绝。

## 背诵要点
1. Passkey = 公钥凭据：私钥在设备，服务端只存公钥；防重放核心是服务端生成的一次性 challenge。
2. 校验五件套（全服务端判定）：challenge/origin/type/rpIdHash/签名，外加 signCount 递增防克隆。
3. 生产用 py_webauthn/fido2（基线 1.x）处理 COSE 与 attestation；自研校验极易在编码层出错。

## 复盘追问
1. 用户丢了登录设备，Passkey 的账户恢复流程怎么设计才不变成后门？（提示：多凭据注册（多设备）+ 恢复走强验证通道（人工/已有会话+二次因子），恢复不是"邮箱重置密码"的同构物）
2. 内网灰度 Passkey 时怎么统计"哪些认证器不支持 signCount"？（提示：注册时记录 authenticator 的 AAGUID/传输与返回的计数器行为，分桶观察 assertion 的 count 分布再定断言策略）
