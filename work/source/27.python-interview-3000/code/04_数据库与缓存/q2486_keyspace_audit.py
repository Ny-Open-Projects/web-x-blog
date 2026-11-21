"""缓存命名空间的审计盘点: 按前缀统计键量与体积, 找出野键"""
import itertools

STORE = {}
for i in range(300):
    STORE["shop:product:%d" % i] = "x" * 120
for i in range(150):
    STORE["shop:cart:%d" % i] = "y" * 40
for i in range(80):
    STORE["session:%d" % i] = "z" * 200
for i in range(25):                                   # 没登记过的野命名空间
    STORE["tmp:debug:%d" % i] = "w" * 500

REGISTERED = {"shop:product", "shop:cart", "session"}

def scan(store):                                      # SCAN 语义: 全量但分批 不阻塞
    for k in sorted(store):
        yield k

def audit(store, registered):
    stat = {}
    for k in scan(store):                             # 取前两段作为命名空间
        ns = ":".join(k.split(":")[:2])
        n, size = stat.get(ns, (0, 0))
        stat[ns] = (n + 1, size + len(store[k]))
    wild = sorted(set(stat) - registered)
    return stat, wild

stat, wild = audit(STORE, REGISTERED)
print("%-16s %8s %10s" % ("命名空间", "键数", "字节量"))
for ns in sorted(stat, key=lambda x: -stat[x][1]):
    n, size = stat[ns]
    flag = " [未注册]" if ns in wild else ""
    print("%-16s %8d %10d%s" % (ns, n, size, flag))
print("键总量 %d, 未注册命名空间: %s" % (len(STORE), wild or "无"))
print("结论: 命名空间规范要配上审计工具才不烂尾——按前缀聚合键数与体积,")
print("      未注册前缀就是清理候选, 每月盘点一次比出了事再扫全库便宜得多")
