"""模拟 SCAN 游标遍历 + 客户端去重"""
def scan(store, cursor, count=2):
    keys = sorted(store.keys())                  # redis 真实为桶序, 此处简化
    if cursor >= len(keys):
        return [], 0
    chunk = keys[cursor:cursor + count]
    nxt = (cursor + count) if cursor + count < len(keys) else 0
    return chunk, nxt

def scan_all(store):
    seen, cursor = set(), 0
    while True:
        chunk, cursor = scan(store, cursor)
        seen.update(chunk)
        if cursor == 0:
            return seen

if __name__ == "__main__":
    store = {f"user:{i}": i for i in range(10)}
    all_keys = scan_all(store)
    print("遍历到:", sorted(all_keys))
    print("完整:", all_keys == set(store.keys()))
    print("语义: 可能重复(需去重), 遍历期间新增键不保证返回")
    print("删除大集合: HSCAN 分批取 field -> HDEL 批删, 拒绝一次性 DEL")
