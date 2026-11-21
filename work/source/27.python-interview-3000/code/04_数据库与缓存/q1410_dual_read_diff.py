"""双读比对: 新旧读路径的结果 diff 采样"""
import random

random.seed(9)

def old_path(uid):
    return {"uid": uid, "points": uid * 2, "level": uid // 10}

def new_path(uid):
    r = old_path(uid)
    if random.random() < 0.01:              # 新路径偶现漂移
        r = dict(r, points=r["points"] + 1)
    return r

mismatch = []
for uid in range(1, 301):
    a, b = old_path(uid), new_path(uid)
    if a != b:
        mismatch.append((uid, a["points"], b["points"]))
print(f"采样 300 次, 不一致 {len(mismatch)} 处, 样例 {mismatch[:5]}")
print("双读要落证据(参数与两侧值), 归因后再决定修数据还是修逻辑")
