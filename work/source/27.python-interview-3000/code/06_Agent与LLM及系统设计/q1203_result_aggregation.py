"""结果聚合:规范化 + 多数投票/中位数 + 置信度加权 + 平票升级。"""
import statistics


def normalize(ans):
    alias = {"北京市": "北京", "beijing": "北京"}
    return alias.get(ans.strip().lower(), ans.strip())


def majority_vote(answers, weights=None):
    norm = [normalize(a) for a in answers]
    tally = {}
    for a in norm:
        tally[a] = tally.get(a, 0) + 1
    top = max(tally.values())
    winners = [a for a, n in tally.items() if n == top]
    if len(winners) > 1:
        return None, "tie", tally
    return winners[0], "majority", tally


def weighted_vote(answers, confidences):
    tally = {}
    for a, c in zip(answers, confidences):
        tally[normalize(a)] = tally.get(normalize(a), 0) + c
    return max(tally.items(), key=lambda x: x[1])


def aggregate_numeric(values):
    return statistics.median(values)


if __name__ == "__main__":
    # 分类任务:多数投票
    ans = ["北京", "北京市", "上海"]
    result, mode, tally = majority_vote(ans)
    print("投票:", result, mode, tally)
    assert result == "北京", "归一化后北京 2 票胜出"

    # 平票升级
    r2, mode2, _ = majority_vote(["北京", "上海", "北京", "上海"][:3] + ["上海"])
    r2, mode2, _ = majority_vote(["北京", "上海", "广州"])
    assert r2 is None and mode2 == "tie"
    print("平票 -> 升级人工或追加讨论,不随机选")

    # 置信度加权:低置信高票被高置信拉回
    w = weighted_vote(["A", "B", "A"], [0.4, 0.95, 0.4])
    print("加权:", w)
    assert w[0] == "B", "置信度加权纠正低置信多数"

    # 数值聚合:中位数抗离群
    assert aggregate_numeric([10, 12, 11, 100]) == 11.5
    print("离群值 100 被中位数抑制")
