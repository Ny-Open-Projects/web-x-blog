"""集群 slot 概念: CRC16 到 16384 槽 与 hash tag 的同槽聚合"""

CRC_TABLE = []
for b in range(256):
    c = b << 8
    for _ in range(8):
        c = ((c << 1) ^ 0x1021) & 0xFFFF if c & 0x8000 else (c << 1) & 0xFFFF
    CRC_TABLE.append(c)

def crc16(data):
    crc = 0
    for byte in data:
        crc = ((crc << 8) & 0xFFFF) ^ CRC_TABLE[((crc >> 8) ^ byte) & 0xFF]
    return crc

def key_slot(key):
    # hash tag: 取第一个 { 与下一个 } 之间的内容参与哈希
    i = key.find("{")
    if i >= 0:
        j = key.find("}", i + 1)
        if j > i + 1:
            key = key[i + 1:j]
    return crc16(key.encode()) % 16384

# 校验: redis 官方 spec 的已知向量 "123456789" -> 12739
print("crc16('123456789') =", crc16(b"123456789"), "slot =", key_slot("123456789"))
print("user:1000 -> slot", key_slot("user:1000"))
print("{u1000}:profile 与 {u1000}:orders 同槽:",
      key_slot("{u1000}:profile") == key_slot("{u1000}:orders"))

def mget_sim(keys):
    slots = {key_slot(k) for k in keys}
    if len(slots) > 1:
        return "CROSSSLOT: 多键命令要求同一槽, 请用 hash tag 或客户端分组"
    return "OK"

print("MGET user:1 user:2 ->", mget_sim(["user:1", "user:2"]))
print("MGET {u9}:a {u9}:b ->", mget_sim(["{u9}:a", "{u9}:b"]))
print("要点: 16384 槽按 CRC16 mod 分配, 节点持有槽区间; 槽迁移期间客户端按 MOVED 与 ASK 重定向")
print("hash tag 让相关键同槽支持多键操作, 但也制造热点, tag 粒度要按业务实体设计")
