"""停写切换 cutover: 锁写 -> 追平增量 -> 校验 -> 切读"""
import queue

src, dst = {}, {}                     # 模拟旧表/新表
pending = queue.Queue()               # 迁移期增量队列
state = {"writes": True, "read_from": "src"}

def business_write(uid, name):
    if not state["writes"]:
        raise RuntimeError("cutover 停写窗口: 请稍后重试")
    src[uid] = name
    pending.put(uid)

for i in range(1, 6):
    business_write(i, "u%d" % i)

state["writes"] = False               # 步骤 1: 停写
for uid in list(src):                 # 步骤 2: 存量已对齐
    dst[uid] = src[uid]
while not pending.empty():            # 追平停写前的增量队列
    uid = pending.get()
    dst[uid] = src[uid]
ok = dst == src                       # 步骤 3: 终验
if ok:
    state["read_from"] = "dst"        # 步骤 4: 切读
    state["writes"] = True            # 步骤 5: 恢复写
print("终验一致:", ok, "新表行数:", len(dst), "读路由:", state["read_from"], "可写:", state["writes"])
print("窗口分钟级; 超时回滚: 读路由拨回 src, 保持双写, 另约窗口")
