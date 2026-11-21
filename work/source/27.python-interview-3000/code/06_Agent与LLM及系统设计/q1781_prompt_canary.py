"""Prompt 灰度:按用户标识稳定分桶到候选提示词,评估集对比达标才放量。"""

PROMPTS = {
    "baseline": "你是客服助手,回答保持简短",
    "candidate": "你是客服助手,回答保持简短并附一个跟进建议",
}

EVAL_SET = [
    {"q": "怎么改地址", "expect_key": "地址"},
    {"q": "怎么退款", "expect_key": "退款"},
]


def bucket(user_id, rollout_pct):
    """稳定分桶:同一用户永远同桶,可复现可回放。"""
    return int(user_id) % 100 < rollout_pct


def fake_generate(prompt, q):
    """生成桩:candidate 版本多附一句跟进建议,命中期望词。"""
    key = next(e["expect_key"] for e in EVAL_SET if e["expect_key"] in q)
    base = "已处理%s诉求" % key
    if "跟进建议" in prompt:
        base += " 需要跟进建议可再次咨询"
    return base


def eval_prompt(name):
    prompt = PROMPTS[name]
    hits = sum(1.0 for e in EVAL_SET
               if e["expect_key"] in fake_generate(prompt, e["q"]))
    aux = sum(1.0 for e in EVAL_SET
              if "跟进建议" in fake_generate(prompt, e["q"]))
    return {"hit_rate": hits / len(EVAL_SET), "aux_rate": aux / len(EVAL_SET)}


if __name__ == "__main__":
    users = [105, 115, 125, 135, 145, 155, 165, 175, 185, 195]
    canary_ids = [u for u in users if bucket(u, 20)]
    assert canary_ids == [105, 115], "放量 20% 精确命中 2 个用户"
    assert all(bucket(u, 20) == bucket(u, 20) for u in users), "分桶稳定可复现"

    base, cand = eval_prompt("baseline"), eval_prompt("candidate")
    assert base["hit_rate"] == 1.0 and cand["hit_rate"] == 1.0, "主指标不回退"
    assert cand["aux_rate"] == 1.0 > base["aux_rate"] == 0.0, "候选版带来增量收益"
    gate = cand["hit_rate"] >= base["hit_rate"] and cand["aux_rate"] > base["aux_rate"]
    assert gate, "达标才继续放量"
    print("Prompt 灰度通过:稳定分桶 20 命中 2 人,评估达标获准放量")
