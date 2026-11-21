"""哨兵故障转移状态机模拟: SDOWN -> ODOWN -> 切换"""
import time

class Sentinel:
    def __init__(self, name, quorum=2):
        self.name, self.quorum = name, quorum
        self.sdown = {}                          # 各哨兵的主观下线记录

    def ping_timeout(self, sentinels, master):
        votes = 0
        for s in sentinels:
            if s.sdown.get(master):
                votes += 1
        return votes >= self.quorum

def failover(masters, replicas, dead_master):
    replicas.sort(key=lambda r: -r["prio"])
    new_master = replicas[0]["name"]
    return {"down": dead_master, "promoted": new_master,
            "others": [r["name"] for r in replicas[1:]]}

if __name__ == "__main__":
    s1, s2, s3 = Sentinel("s1"), Sentinel("s2"), Sentinel("s3")
    sentinels = [s1, s2, s3]
    s1.sdown["master1"] = True                   # 一个哨兵主观下线
    print("仅 1 票, 客观下线:", s1.ping_timeout(sentinels, "master1"))
    s2.sdown["master1"] = True                   # 达到 quorum=2
    print("2 票, 客观下线:", s1.ping_timeout(sentinels, "master1"))

    replicas = [{"name": "r1", "prio": 100}, {"name": "r2", "prio": 90}]
    print("切换结果:", failover({}, replicas, "master1"))
    print("脑裂防护: min-replicas-to-write 让孤主拒绝写入")
