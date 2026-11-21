"""Q2836 Agent 输出的溯源信封:指纹 工具清单与内容哈希。

答案离开 Agent 边界后就可能被转发 截图 改写。给每个回答附一个溯源
信封:run_id 串起全链路日志,输入指纹锁定用户到底问了什么,工具
调用清单回答「结论靠什么得出」,内容哈希让下游能验证答案没被篡改。
"""

import hashlib


def norm_text(s):
    return " ".join(s.split()).strip()


def make_envelope(run_id, user_input, answer, tool_calls, model_version):
    return {
        "run_id": run_id,
        "model_version": model_version,
        "input_fp": hashlib.sha256(
            norm_text(user_input).encode("utf-8")).hexdigest()[:16],
        "tool_calls": list(tool_calls),
        "content_hash": hashlib.sha256(
            answer.encode("utf-8")).hexdigest(),
    }


def verify(envelope, answer):
    """下游验真:重算内容哈希比对,任何改动都会暴露。"""
    expect = hashlib.sha256(answer.encode("utf-8")).hexdigest()
    return expect == envelope["content_hash"]


def main():
    answer = "本季度退款平均 3 个工作日到账。"
    env = make_envelope(
        run_id="run_20261105_001",
        user_input="  退款   多久到账? ",
        answer=answer,
        tool_calls=["search(policy_v3)", "read_doc(d1)"],
        model_version="glm-x-2026Q4",
    )
    assert env["input_fp"] == hashlib.sha256(
        u"退款 多久到账?".encode("utf-8")).hexdigest()[:16], env   # 归一化后指纹稳定
    assert verify(env, answer) is True
    # 篡改检测:有人改了一个数字
    forged = "本季度退款平均 30 个工作日到账。"
    assert verify(env, forged) is False
    # 溯源:这结论动用了哪些工具,一眼可见
    assert env["tool_calls"] == ["search(policy_v3)", "read_doc(d1)"], env
    print("信封:", {k: env[k] for k in ("run_id", "input_fp", "model_version")})
    print("原文验真:", verify(env, answer), "篡改检出:", verify(env, forged) is False)
    print("工具清单:", env["tool_calls"])


if __name__ == "__main__":
    main()
