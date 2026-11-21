"""查询日志分析:零结果与低点击查询统计,主题聚类找语料缺口,输出补语料优先级。"""
from collections import Counter, defaultdict


def topic_key(query):
    """主题抽取桩:取前两个字符作主题键,演示用。"""
    return query[:2]


class QueryLogAnalyzer:
    def __init__(self, logs):
        # log: {"query", "hits", "clicked"}  hits 为检索命中数
        self.logs = logs

    def zero_result(self):
        c = Counter(l["query"] for l in self.logs if l["hits"] == 0)
        return c.most_common()

    def low_click(self, min_hits=3, max_clicks=0):
        """有结果但没人点:检索到的都不是用户想要的。"""
        c = Counter(l["query"] for l in self.logs
                    if l["hits"] >= min_hits and l["clicked"] <= max_clicks)
        return c.most_common()

    def gaps(self):
        """缺口主题:零结果与低点击按主题合并计数,给出建议补语料优先级。"""
        merged = Counter()
        for q, n in self.zero_result():
            merged[topic_key(q)] += n * 2          # 零结果权重更高
        for q, n in self.low_click():
            merged[topic_key(q)] += n
        return merged.most_common()

    def funnel(self):
        """漏斗:请求→有结果→有点击 三级转化。"""
        req = len(self.logs)
        with_hits = sum(1 for l in self.logs if l["hits"] > 0)
        clicked = sum(1 for l in self.logs if l["clicked"] > 0)
        return {"requests": req,
                "hit_rate": round(with_hits / max(1, req), 2),
                "click_rate": round(clicked / max(1, req), 2)}


if __name__ == "__main__":
    logs = [
        {"query": "年假怎么请", "hits": 5, "clicked": 2},
        {"query": "年假可以折现吗", "hits": 0, "clicked": 0},
        {"query": "年假折现政策", "hits": 0, "clicked": 0},
        {"query": "报销流程是什么", "hits": 4, "clicked": 0},
        {"query": "报销发票丢了怎么办", "hits": 3, "clicked": 0},
        {"query": "考勤打卡机坏了", "hits": 2, "clicked": 1},
        {"query": "社保基数调整", "hits": 6, "clicked": 3},
    ]
    az = QueryLogAnalyzer(logs)
    zr = az.zero_result()
    assert dict(zr) == {"年假可以折现吗": 1, "年假折现政策": 1}
    lc = az.low_click()
    assert set(q for q, _ in lc) == {"报销流程是什么", "报销发票丢了怎么办"}
    gaps = az.gaps()
    assert gaps[0] == ("年假", 4), "零结果 2 条 x2 权重居首"
    assert ("报销", 2) in gaps, "低点击 2 条各计 1 合并到报销主题"

    f = az.funnel()
    assert f == {"requests": 7, "hit_rate": 0.71, "click_rate": 0.43}
    print("日志分析通过:零结果 2 条 低点击 2 条 缺口首位 年假可 权重 4 漏斗", f)
