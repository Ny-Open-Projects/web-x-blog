"""Q2601 Gossip 推与拉的收敛实测:固定种子下比较轮数与消息量。

推模式传播快但尾部慢:最后几个未感染节点要靠运气撞上;
拉模式让未感染者主动出击,尾部收敛更快;推拉结合双向开火,
轮数逼近理论下限 log2 n。固定种子可复现。
"""
import math
import random


def simulate(n, mode, seed, rounds_cap=60):
    rng = random.Random(seed)
    informed = [False] * n
    informed[0] = True
    msgs = 0
    for r in range(rounds_cap):
        new = list(informed)
        for i in range(n):
            peer = rng.randrange(n)
            if peer == i:
                continue
            if mode == "push" and informed[i] and not informed[peer]:
                msgs += 1
                new[peer] = True
            elif mode == "pull" and informed[peer] and not informed[i]:
                msgs += 1
                new[i] = True
            elif mode == "push-pull" and informed[i] != informed[peer]:
                msgs += 1
                new[i] = new[peer] = True
        informed = new
        if all(informed):
            return r + 1, msgs
    return None, msgs


def main():
    n = 32
    results = {}
    for mode in ("push", "pull", "push-pull"):
        rounds, msgs = simulate(n, mode, seed=42)
        assert rounds is not None, mode + " 未收敛"
        results[mode] = (rounds, msgs)
    assert results["push-pull"][0] <= results["push"][0], results
    assert results["push-pull"][0] <= results["pull"][0], results
    print("n =", n, "理论下限 log2 n =", math.ceil(math.log2(n)))
    for mode, (r, m) in sorted(results.items(), key=lambda kv: kv[1][0]):
        print(mode, "收敛轮数:", r, "成功传播消息数:", m)


if __name__ == "__main__":
    main()
