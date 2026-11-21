"""CRC16 取模映射槽位(教学实现) + hash tag 同槽演示"""

CRC16_TABLE = None

def crc16(data: bytes) -> int:
    """CRC-16/XMODEM, Redis cluster 使用的多项式 0x1021"""
    crc = 0
    for b in data:
        crc ^= b << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) if crc & 0x8000 else (crc << 1)
            crc &= 0xFFFF
    return crc

def key_slot(key: str) -> int:
    # hash tag: 取第一个 {..} 内的内容参与计算
    if "{" in key and "}" in key:
        tag = key[key.index("{") + 1:key.index("}")]
        if tag:
            key = tag
    return crc16(key.encode()) % 16384

if __name__ == "__main__":
    nodes = {"nodeA": range(0, 8192), "nodeB": range(8192, 16384)}
    def node_of(key):
        slot = key_slot(key)
        return ("nodeA" if slot in nodes["nodeA"] else "nodeB", slot)

    for k in ("user:1", "user:2", "{user1}:profile", "{user1}:orders"):
        n, s = node_of(k)
        print(f"{k:<18} -> 槽 {s:<5} 节点 {n}")
    print("hash tag 保证 {user1} 系列同槽, 多键操作可用")
