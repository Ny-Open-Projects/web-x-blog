import hashlib
import json
import os

DST = "dim_user.json"
STATE = "load_state.json"

def row_key(row):
    """以业务键 + 内容指纹为唯一键,与运行时间无关。"""
    digest = hashlib.md5(json.dumps(row, sort_keys=True).encode()).hexdigest()
    return f"{row['uid']}-{digest}"

def upsert(rows, state):
    """标准库模拟 upsert:同 key 覆盖,重跑结果不变。"""
    store = {}
    if os.path.exists(state):
        store = json.load(open(state))
    before = len(store)
    for r in rows:
        store[row_key(r)] = r          # 幂等:重复导入只覆盖
    json.dump(store, open(state, "w"))
    return before, len(store)

if __name__ == "__main__":
    rows = [{"uid": 1, "name": "a"}, {"uid": 2, "name": "b"}]
    upsert(rows, STATE)
    r1 = json.load(open(STATE)) if os.path.exists(STATE) else {}
    upsert(rows, STATE)                # 再跑一遍
    r2 = json.load(open(STATE))
    assert r1 == r2, "必须幂等"
    print("idempotent ok, rows =", len(r2))
    os.remove(STATE)
