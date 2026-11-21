"""按访问频率 TopN 预热 + 限速分批"""
import time
from collections import Counter

def top_keys(access_log, n=5):
    return [k for k, _ in Counter(access_log).most_common(n)]

def warmup(cache, db, keys, batch=2, delay=0.01):
    loaded = 0
    for i in range(0, len(keys), batch):          # 限速分批, 保护 DB
        for k in keys[i:i + batch]:
            cache[k] = db[k]
            loaded += 1
        time.sleep(delay)
    return loaded

if __name__ == "__main__":
    access_log = ["p:1"] * 100 + ["p:2"] * 60 + ["p:3"] * 30 + \
                 ["p:4"] * 10 + ["p:5"] * 5 + ["p:6"] * 1
    db = {f"p:{i}": f"data{i}" for i in range(1, 7)}
    cache = {}
    hot = top_keys(access_log)
    print("热点 key:", hot)
    n = warmup(cache, db, hot)
    print(f"预热 {n} 个 key, 缓存:", cache)
    print("上线后热点请求直接命中, 长尾请求限速回源")
