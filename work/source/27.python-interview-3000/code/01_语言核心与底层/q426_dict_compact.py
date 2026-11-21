import sys

d = {}
for k in ["z", "a", "m"]:
    d[k] = ord(k)
print("iteration order == insertion order:", list(d) == ["z", "a", "m"])

# 哈希与槽位:int 的 hash 是它自身,观察 index 数组稀疏性
i = hash("z")
print("hash('z') =", i, "mod 8 =", i % 8)

# 缩容不自动发生:大表删空后 sizeof 不降
big = {k: k for k in range(100_000)}
size_full = sys.getsizeof(big)
for k in list(big): del big[k]
print("full:", size_full, "after del all:", sys.getsizeof(big),
      "rebuilt:", sys.getsizeof(dict(big)))

# 碰撞演示:自定义对象 hash 恒定,强制全部撞进同一槽
class Collide:
    def __hash__(self): return 42
    def __eq__(self, other): return self is other

cd = {Collide(): i for i in range(5)}
print("collisions survived, len:", len(cd))
