"""Gossip 成员同步:节点随机互拉成员表 按版本号取新,轮次内全网收敛。"""
import random


def build(n):
    return {i: {"ver": 0, "members": {i: 0}} for i in range(n)}


def gossip_round(nodes, rng):
    changed = 0
    for i in list(nodes):
        j = rng.choice([x for x in nodes if x != i])
        mine, theirs = nodes[i], nodes[j]
        updated = False
        for m, v in theirs["members"].items():
            if v > mine["members"].get(m, -1):
                mine["members"][m] = v
                updated = True
        if updated:
            mine["ver"] += 1
            changed += 1
    return changed


def join(nodes, nid, new_node):
    nodes[nid]["members"][new_node] = nodes[nid]["ver"] + 1


def converged(nodes):
    members = [frozenset(n["members"]) for n in nodes.values()]
    return len(set(members)) == 1


if __name__ == "__main__":
    nodes = build(5)
    rng = random.Random(42)
    join(nodes, 0, 9)
    rounds = 0
    while not converged(nodes) and rounds < 20:
        gossip_round(nodes, rng)
        rounds += 1
    assert converged(nodes), "gossip 轮次内全网收敛"
    assert rounds <= 10, "5 节点应在个位数轮收敛 实测 %d" % rounds
    for i in range(5):
        assert 9 in nodes[i]["members"], "新成员视图同步到每个节点"
    info = [nodes[i]["members"][9] for i in range(5)]
    assert len(set(info)) == 1, "成员条目版本全网一致"
    print("gossip 收敛通过:轮次 %d 全员视图一致" % rounds)
