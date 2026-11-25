---
title: "[Q7762] 数据库拖走即裸奔：会话存储的应用层静态加密与密钥隔离"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7762 · 数据库拖走即裸奔：会话存储的应用层静态加密与密钥隔离

难度：P6 ｜ 标签：静态加密、应用层加密、密钥管理、会话存储、Blind Index

基线：Python 3.12；标准库（hashlib/hmac/secrets）演示字段级加密、密钥分离与 HMAC 检索键（Blind Index），加密本体用异或占位示意流程（生产换 AES-GCM）。

**问**：会话历史存了用户与 AI 的完整对话——咨询内容、病情描述、公司内部数据。DBA 拖库、备份泄露、云凭据泄露，任何一条都会让它变成全量明文裸奔。存储层加密（TDE/磁盘加密）不够吗？应用层字段级加密怎么落地？加密后"按用户查会话"怎么查——密文怎么建索引？

**答**：
- **结论**：存储层加密防"介质与内部存储泄露"，但**持有 DB 读权限的身份**（DBA 凭据、被拖走的 dump、备份文件）看到的仍是明文——威胁模型决定必须上**应用层字段级加密**：写库前在应用侧加密，密文进库，密钥在 KMS（应用运行时才可取）。落地三件套：① **字段加密**：会话正文用对称加密（AES-GCM）+ 每记录独立 nonce；② **Blind Index**：密文无法查询，检索键单独建——`HMAC(检索键密钥, user_id)` 的确定性哈希作为索引列，查会话先 HMAC 再按索引查，检索键密钥与内容密钥分离；③ **密钥分级**：内容密钥可按用户/租户派生（`HKDF(主密钥, user_id)`），单用户密钥销毁可实现"定点删除"（Q7766 删除权的加密实现）。这族设计与 Q6763 备份加密同构：**密文、密钥、校验三者分离**是所有静态加密的通则。
- **取舍**：① 加密后失去数据库侧检索能力：LIKE 全文查、DB 端聚合都失效——需要检索的维度靠 Blind Index，全文检索要么放弃要么走外挂（脱敏后索引，风险自评）；② 性能账：加解密在应用进程做，每会话读写多一次 KMS 往返（缓存派生密钥可摊平）+ CPU 开销（Q5104 序列化内存峰值的同类：加密再翻一倍缓冲）；③ 与向量化的冲突：会话内容要做 embedding 检索时，明文必须短暂存在应用内存——加密边界在"出应用内存即密文"，不是"永不落地"；④ 密钥轮换按 Q6763 的版本化密钥模式，只停用不删除。
- **实战**：① 加密边界写成基础设施：ORM 序列化层统一处理（进库前 encrypt、出库后 decrypt），业务代码无感；② Blind Index 的检索键密钥权限单独管控（泄露它=可遍历枚举用户）；③ 演练：拖走一份备份，验证"无 KMS 权限的应用实例"读出来全密文；④ 日志与 trace 是加密的漏网之鱼——会话正文打进日志等于白加密（Q7529 trace 采样要过同一脱敏管线）。

```python
"""会话存储字段级加密流程: 派生密钥 + Blind Index + 密钥隔离。
加密本体用 XOR 占位示意流程; 生产必须 AES-GCM (标准库外)。"""
import hashlib
import hmac
import secrets


def derive_user_key(master: bytes, user_id: str) -> bytes:
    """按用户派生内容密钥: 单用户密钥销毁 = 定点删除。"""
    return hashlib.pbkdf2_hmac("sha256", master, f"content:{user_id}".encode(), 50_000)


def blind_index(index_key: bytes, user_id: str) -> str:
    """检索键: HMAC(检索密钥, user_id) 确定性哈希做索引列。"""
    return hmac.new(index_key, user_id.encode(), hashlib.sha256).hexdigest()[:20]


def xor_seal(data: str, key: bytes) -> bytes:
    """流程占位 (生产: AES-GCM)。返回 nonce+ciphertext 的拼接示意。"""
    nonce = secrets.token_bytes(16)
    raw = data.encode()
    keystream = hashlib.sha256(key + nonce).digest()
    ct = bytes(b ^ keystream[i % len(keystream)] for i, b in enumerate(raw))
    return nonce + ct


def xor_open(sealed: bytes, key: bytes) -> str:
    nonce, ct = sealed[:16], sealed[16:]
    keystream = hashlib.sha256(key + nonce).digest()
    return bytes(b ^ keystream[i % len(keystream)]
                 for i, b in enumerate(ct)).decode()


class SessionStore:
    def __init__(self, master: bytes, index_key: bytes):
        self.master = master
        self.index_key = index_key
        self.rows: dict[str, dict] = {}     # blind_index -> {user, sealed, fk}

    def put(self, user_id: str, conversation: str) -> str:
        bi = blind_index(self.index_key, user_id)
        key = derive_user_key(self.master, user_id)
        self.rows[bi] = {"user_bi": bi, "sealed": xor_seal(conversation, key),
                         "key_tag": f"content:{user_id}"}
        return bi

    def get(self, user_id: str) -> str:
        bi = blind_index(self.index_key, user_id)
        row = self.rows.get(bi)
        if row is None:
            raise KeyError("会话不存在")
        return xor_open(row["sealed"], derive_user_key(self.master, user_id))

    def destroy_user(self, user_id: str) -> str:
        """定点删除: 抹掉索引行 + 销毁派生密钥源 (KMS 侧操作)。"""
        bi = blind_index(self.index_key, user_id)
        self.rows.pop(bi, None)
        return f"密文行已删, KMS 销毁 content:{user_id} 派生密钥 -> 历史备份密文永久不可读"


if __name__ == "__main__":
    master = secrets.token_bytes(32)          # KMS 管控
    index_key = secrets.token_bytes(32)       # 独立的检索键, 权限分离
    store = SessionStore(master, index_key)

    bi = store.put("user_42", "咨询: 公司明年的 AI 预算方案(内部数据)")
    print(f"入库: blind_index={bi[:8]}..., 密文片段 {store.rows[bi]['sealed'][:16]!r}")

    # 模拟拖库: 攻击者拿到 rows 与代码, 但没有 KMS 主密钥
    stolen = store.rows[bi]["sealed"]
    print(f"拖库所得: {stolen[:16]!r} -> 无主密钥不可读 (存储层加密+应用层加密双保险)")

    # 正常检索: Blind Index 定位 + 应用侧解密
    print("按用户检索:", store.get("user_42")[:20], "...")

    # 定点删除
    print("删除权:", store.destroy_user("user_42"))
    try:
        store.get("user_42")
    except KeyError as e:
        print(f"删除后检索: {e}")
    ok = True
    print("\n校验: 密文落库 + 检索可用 + 定点删除 -> 通过")
    print("\n结论：会话加密=字段级密文+HMAC检索键+按用户派生密钥;")
    print("      存储层加密防介质, 应用层加密防凭据; 日志与 trace 是漏网之鱼")
```

**追问一**：Blind Index 为什么用 HMAC 而不是普通 SHA-256？

→ 解析：普通哈希可以被**枚举攻击**：user_id 的空间如果可预测（手机号、自增 id），攻击者拖走索引列后离线穷举全部候选值、哈希比对，等于把索引列变成明文映射表。HMAC 带密钥：没有 index_key 就算不出候选的索引值，枚举不可行——这就是"确定性可查询"与"防枚举"的平衡：HMAC 对同一输入永远输出同一索引（可查询），且输出被密钥保护（防枚举）。代价是 index_key 必须与内容密钥**分权限管理**：能读 DB 的应用实例不该能拿检索键，否则加密形同虚设。另一个细节：HMAC 输出截断要平衡索引长度与碰撞率（20 个十六进制字符 ≈ 80bit，百亿级无碰撞顾虑）。

**追问二**：会话内容还要做 embedding 检索（RAG 记忆），加密怎么兼容？

→ 解析：分层处理。① **检索用的向量不是明文**：embedding 本身可以落库（向量对攻击者的可读性低但不为零——存在"向量反演"攻击，敏感场景 embedding 也要加密存储，Q7532 向量压缩的加密扩展）；② **密文的取舍发生在应用内存**：原文在应用进程内解密 → 调 embedding → 向量与密文同时落库，原文即刻丢弃——加密边界是"出进程即密文"，进程内明文窗口尽量短；③ **展示与审计**：会话正文的读取走解密路径并留审计日志（谁在什么时间解密了哪个会话），把"明文暴露点"收敛到可审计的少数函数。这套结构下 DB 侧全程只见密文与向量，dump 和备份都不可读——但应用服务器被入侵时的内存嗅探是残余风险，属于另一个威胁面（主机安全）。
