"""只读降级开关: 数据库故障时保读弃写, 写请求显式失败或暂存"""

STATE = {"read_only": False}
outbox = []

class DegradedError(Exception):
    pass

def write_profile(user_id, name):
    if STATE["read_only"]:
        outbox.append((user_id, name))
        raise DegradedError("库处于只读降级, 写入已暂存待补放")
    return ("db-write", user_id, name)

def read_profile(user_id):
    return {"id": user_id, "name": "cached-name"}

STATE["read_only"] = True
try:
    write_profile(42, "new-name")
except DegradedError as e:
    print("写被显式拒绝:", e)
print("读不受影响:", read_profile(42), " 暂存量:", len(outbox))

STATE["read_only"] = False
replayed = [write_profile(u, n) for u, n in outbox]
outbox.clear()
print("恢复后补放:", replayed)
print("要点: 写显式失败 队列有界带 TTL 补放走幂等 开关全程可观测")
