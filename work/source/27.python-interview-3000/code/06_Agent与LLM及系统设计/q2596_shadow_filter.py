"""Q2596 红黑名单的灰度过滤:先影子观察,误伤达标再转正。

新过滤规则直接 enforce 误伤没法撤;先跑 observe 模式只记录
would-block 不真拦,用标注样本算误伤率,达标才转正,不达标
回炉修规则——灰度让过滤器的上线和下线都有台阶。
"""
import random

RULE_BAD = ["赌", "枪"]
SAMPLES = [("正常咨询", "ok"), ("赌博推广", "bad"), ("买枪支", "bad"),
           ("正常复诊", "ok"), ("枪械历史课", "ok")]  # 最后一例规则误伤


def rule_hit(text):
    return any(w in text for w in RULE_BAD)


def run(mode):
    stats = {"blocked": 0, "passed": 0, "would_block": 0, "fp_if_enforced": 0}
    for text, label in SAMPLES:
        hit = rule_hit(text)
        if hit:
            if mode == "enforce":
                stats["blocked"] += 1
            else:
                stats["would_block"] += 1
            if label == "ok":
                stats["fp_if_enforced"] += 1
        else:
            stats["passed"] += 1
    return stats


def promote(shadow, allow_fp):
    fp_rate = shadow["fp_if_enforced"] / max(shadow["would_block"], 1)
    return fp_rate <= allow_fp


def main():
    shadow = run("observe")
    enforce = run("enforce")
    assert shadow["would_block"] == 3 and shadow["blocked"] == 0, shadow
    assert enforce["blocked"] == 3 and shadow["fp_if_enforced"] == 1
    assert promote(shadow, allow_fp=0.2) is False   # 误伤 1/3 超标
    assert promote(shadow, allow_fp=0.5) is True
    print("影子模式:", shadow, "← 一条都没真拦")
    print("误伤率:", shadow["fp_if_enforced"], "/", shadow["would_block"],
          "超 20% 红线 → 不转正,先修规则")


if __name__ == "__main__":
    main()
