"""缓存容量估算: 对象头放大与预算反推"""
import sys

def entry_overhead(key_chars, value_bytes):
    """简化模型: 键串对象头 值对象头 字典槽位摊销"""
    return sys.getsizeof("k" * key_chars) + sys.getsizeof(b"v" * value_bytes) + 64

n = 100_000_000
naive_gb = n * (32 + 256) / 1024 ** 3
real_gb = n * entry_overhead(32, 256) / 1024 ** 3
print(f"一亿条 键 32 字符 值 256 字节")
print(f"  字节累加口径 {naive_gb:6.1f} GB  含对象头与槽位估算 {real_gb:6.1f} GB  放大系数 {real_gb / naive_gb:.2f}")

# 实测: 真实容器装 10 万条样本 外推
sample = {}
for i in range(100_000):
    sample["user:profile:%012d" % i] = b"x" * 256
per_key = sys.getsizeof("user:profile:000000000000")
per_val = sys.getsizeof(b"x" * 256)
table = sys.getsizeof(sample)
per_entry = (table + 100_000 * (per_key + per_val)) / 100_000
print(f"实测样本 每条摊 {per_entry:.0f} 字节  外推一亿条 {per_entry * n / 1024 ** 3:.1f} GB")

# 预算反推: 给定内存预算能容纳多少条
budget_gb = 16
short_key = "up:123456"
short_entry = sys.getsizeof(short_key) + per_val + 64
fit_million = budget_gb * 1024 ** 3 / short_entry / 1e6
print(f"预算 {budget_gb} GB 短键模型可容纳约 {fit_million:.0f} 百万条")

# 安全水位: 淘汰开始前的缓冲
print(f"留 30% 水位后建议容量约 {fit_million * 0.7:.0f} 百万条")
print("结论: 容量规划不能按字节累加 对象头 对齐 槽位与碎片带来 1.5 到 2 倍放大 还要留水位防淘汰")
