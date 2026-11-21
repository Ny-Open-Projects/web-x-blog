"""SCAN 游标遍历找大 key + hash 分片拆分 + 分批删除"""
import json

def scan_all(store, cursor=0, batch=3):
    """模拟 SCAN: 返回 批内keys, 新cursor; cursor=0 表示结束"""
    keys = sorted(store.keys())
    if cursor >= len(keys):
        return [], 0
    chunk = keys[cursor:cursor + batch]
    nxt = cursor + batch
    return chunk, nxt if nxt < len(keys) else 0

def big_keys(store, limit=20):
    found = []
    c = 0
    while True:
        chunk, c = scan_all(store, c)
        for k in chunk:
            size = len(json.dumps(store[k]).encode())
            if size > limit:
                found.append((k, size))
        if c == 0:
            break
    return found

def split_hash(big_value, shards=4):
    out = {f"hash:{i}": {} for i in range(shards)}
    for field, v in big_value.items():
        out[f"hash:{hash(field) % shards}"][field] = v
    return out

if __name__ == "__main__":
    store = {"user:1": {"name": "a"}, "feed:2": {f"p{i}": "x" * 30 for i in range(50)}}
    print("大 key 扫描:", big_keys(store))
    big = store["feed:2"]
    parts = split_hash(big)
    print("拆分后:", {k: len(v) for k, v in parts.items()})
    print("删除用 UNLINK 分批: 每次 SCAN 取一批 UNLINK, 避免单次 DEL 阻塞")
