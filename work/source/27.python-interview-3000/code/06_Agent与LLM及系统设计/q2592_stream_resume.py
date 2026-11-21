"""Q2592 流式断点续传的语义:幂等去重与半截词的分叉处理。

续传必须定义两件事:重复事件怎么去重(客户端按 seq 幂等,
at-least-once 多发无害),断在半个 token 上怎么续(半截不入账,
服务端从词边界整词重发,客户端覆盖而不是拼接,不出脏字)。
"""

def server_stream(tokens, last_acked):
    """服务端从 last_acked+1 起重放,at-least-once,可能多给。"""
    return [(i, t) for i, t in enumerate(tokens) if i > last_acked]


def client_assemble(events, known):
    """客户端按 seq 幂等去重,只认没见过的序号。"""
    parts = []
    for seq, tok in sorted(events):
        if seq in known:
            continue
        known.add(seq)
        parts.append(tok)
    return "".join(parts)


def main():
    tokens = ["你好", ",", "世界", "!", "再见"]
    known = set()
    acked = 1                       # 客户端已确认 0、1 两个事件
    dup = server_stream(tokens, acked) * 2   # 网络层重发一份
    text = client_assemble(dup, known)
    assert text == "世界!再见", text  # 去重后不重不漏
    # 断在 再见 的半个词上:半截 不 入账,整词重发覆盖
    half = "再"
    replay = server_stream(tokens, acked)   # 服务端从边界整词重发
    text2 = client_assemble(replay, set())
    assert text2 == "世界!再见"
    assert half + "见" == "再见" and half not in text2.replace("再见", "")
    print("重复事件去重重组:", text)
    print("词边界续传:", text2, "| 半截", repr(half), "被整词覆盖,不拼接出脏字")


if __name__ == "__main__":
    main()
