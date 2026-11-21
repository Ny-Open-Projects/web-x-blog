import random

def gen_scores(seed, n=5):
    rng = random.Random(seed)   # 独立实例,不污染全局 random
    return [{"id": i, "score": round(rng.gauss(80, 10), 2)} for i in range(n)]

if __name__ == "__main__":
    a = gen_scores(42)
    b = gen_scores(42)
    assert a == b, "同种子必须可复现"
    print(a)
    print("失败时可打印 seed=42 与生成器参数,精确重现数据")
    # 全局 random 的反面教材:random.shuffle 会影响其他模块的随机序列
