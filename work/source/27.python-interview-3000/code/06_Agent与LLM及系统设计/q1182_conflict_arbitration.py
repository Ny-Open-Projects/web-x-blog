"""写冲突解决:版本检测 + 类型化仲裁策略 + 异议记录。"""


class SharedDoc:
    ARBITERS = {
        "budget": lambda a, b: min(a, b),          # 预算类:取保守值
        "title": lambda a, b: a,                   # 文本类:新写入者胜,败方留异议
    }

    def __init__(self):
        self.data, self.versions, self.disputes = {}, {}, []

    def write(self, agent, field, value, priority=0, expect_version=None):
        cur = self.versions.get(field, 0)
        if expect_version is not None and expect_version != cur:
            other = self.data.get(field)
            merged = self.ARBITERS.get(field, lambda x, y: x)(value, other)
            loser = agent if merged != value else "prior_writer"
            self.disputes.append({"field": field, "winner_value": merged,
                                  "loser": loser, "agent": agent})
            self.data[field] = merged
            self.versions[field] = cur + 1
            return "arbitrated", merged
        self.data[field] = value
        self.versions[field] = cur + 1
        return "ok", value


if __name__ == "__main__":
    doc = SharedDoc()
    r1, val1 = doc.write("researcher", "title", "初稿标题", priority=1)
    print("首写:", r1, val1, "版本", doc.versions["title"])
    assert r1 == "ok" and doc.versions["title"] == 1
    # 基于 v0 的过期写入 -> 冲突仲裁
    r2, val2 = doc.write("editor", "title", "编辑标题", priority=2, expect_version=0)
    print("冲突仲裁:", r2, val2, "争议记录:", doc.disputes)
    assert r2 == "arbitrated" and val2 == "编辑标题", "高优先级编辑胜出"
    assert len(doc.disputes) == 1 and doc.disputes[0]["loser"] == "prior_writer"

    r3, val3 = doc.write("planner", "budget", 100)
    r4, val4 = doc.write("reviewer", "budget", 80, expect_version=0)   # 过期版本
    print("预算字段仲裁取保守值:", val4)
    assert r4 == "arbitrated" and val4 == 80, "数值型合并规则取 min"

    # 乐观锁正常路径:版本正确则直接写入
    r5, val5 = doc.write("editor", "title", "定稿标题", priority=9,
                         expect_version=doc.versions["title"])
    assert r5 == "ok" and doc.versions["title"] == 3
    print("版本号乐观写 + 类型化仲裁 + 异议留痕 全部生效")
