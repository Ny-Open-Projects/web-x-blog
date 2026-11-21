"""写偏斜: 两个事务都守规则 合起来却违反规则"""
import copy

# 场景: 值班规则要求'至少一名医生在线'; 两人都基于快照判断后同时下线
db = {"alice": {"on_call": True}, "bob": {"on_call": True}}
RULE_MIN_ON_CALL = 1

class SnapshotTxn:
    """快照隔离的最小模拟: 读自己启动时的快照, 写缓存在本地, 提交只覆盖自己写的键"""

    def __init__(self, db):
        self.db = db
        self.snapshot = copy.deepcopy(db)
        self.writes = {}

    def read(self, key):
        return self.snapshot.get(key)

    def write(self, key, row):
        self.writes[key] = row

    def commit(self):
        for k, v in self.writes.items():      # 快照隔离只检测写写冲突
            self.db[k] = copy.deepcopy(v)
        return True

t1 = SnapshotTxn(db)
t2 = SnapshotTxn(db)

# 两个事务并发: 各自读到快照里'还有 2 人在值' -> 自己下线是安全的
for t, who in ((t1, "alice"), (t2, "bob")):
    on_call = sum(1 for d in t.snapshot.values() if d["on_call"])
    print("%s 提交前快照判断: 在值 %d 人 >= %d, 判定自己下线合法" % (who, on_call, RULE_MIN_ON_CALL))
    assert on_call >= RULE_MIN_ON_CALL
    row = dict(t.read(who))
    row["on_call"] = False
    t.write(who, row)

t1.commit()
t2.commit()

final = sum(1 for d in db.values() if d["on_call"])
print("两个事务都成功提交, 最终在值 %d 人  <- 规则被合谋击穿, 这就是写偏斜" % final)
assert final == 0
print("成因: 两个事务写的是不同的行, 写写冲突检测放过它们; 但它们读的是同一个谓词集合")
print("对策: 可串行化隔离 / 对谓词范围显式加锁 (SELECT ... FOR UPDATE 锁住全部在值行) /")
print("      把守卫状态收拢成一行热点计数 (代价是串行化该规则)")
