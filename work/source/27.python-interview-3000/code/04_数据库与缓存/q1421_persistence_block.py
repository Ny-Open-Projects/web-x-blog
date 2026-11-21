"""持久化阻塞: fork 时延随实例内存增长与 COW 写惩罚"""
def fork_cost_ms(mem_gb):
    return mem_gb * 50                  # 页表建立与遍历的粗略模型

def cow_penalty_ms(mem_gb, dirty_ratio):
    return dirty_ratio * mem_gb * 300   # rewrite 期间业务写触发写时复制的粗略模型

print("实例内存 -> fork 预估毫秒(bgsave / AOF rewrite 前置):")
for g in (1, 4, 10, 30):
    print(f"  {g:>2} GB: {fork_cost_ms(g):5.0f} ms")
for ratio in (0.05, 0.2):
    print(f"rewrite 期脏页比例 {ratio:.0%}: COW 惩罚约 {cow_penalty_ms(10, ratio):.0f} ms")
print("对策: 限制单实例内存, 持久化错峰, 关 THP, 盯 latest_fork_usec")
