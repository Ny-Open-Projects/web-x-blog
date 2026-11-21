"""主从异步复制的丢失窗口与 min-replicas-to-write 保护"""
import random

random.seed(5)
writes = [f"w{i:03d}" for i in range(100)]
fail_at = 70

lost_a = []
for i, w in enumerate(writes[:fail_at]):
    if random.random() < 0.9:
        pass                          # 已同步到从
    else:
        lost_a.append(w)              # 主宕机时还没到从库
print(f"场景A 纯异步: 宕机点 {fail_at}, 静默丢失 {len(lost_a)} 条")

in_flight, refused = [], []
for w in writes[:fail_at]:
    if len(in_flight) >= 2:           # min-replicas 语义: 未确认写超限则拒写
        refused.append(w)
    else:
        in_flight.append(w)
        if random.random() < 0.9:
            in_flight.remove(w)       # 到达从库
print(f"场景B 保护模式: 丢失被钳制到 {len(in_flight)} 条以内, 拒写 {len(refused)} 条交客户端重试")
print("结论: 异步复制有固有丢失窗口, min-replicas 把静默丢失换成可见失败")
