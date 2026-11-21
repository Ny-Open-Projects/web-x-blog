"""流式取消:生成器在 close 时于 finally 中做清理,保留部分结果并标记取消。"""


def token_stream(tokens, billing, partials):
    produced = []
    try:
        for t in tokens:
            produced.append(t)
            billing["tokens"] += 1      # 每片都计费,取消后必须停止
            yield t
        billing["finished"] = True
    except GeneratorExit:
        billing["cancelled"] = True
        partials.append("".join(produced))  # 部分结果持久化
        raise                                # GeneratorExit 必须继续抛出
    finally:
        billing["connections"] -= 1          # 连接/上游资源必释放


if __name__ == "__main__":
    billing = {"tokens": 0, "finished": False, "cancelled": False, "connections": 1}
    partials = []
    gen = token_stream(iter(["你", "好", "世", "界"]), billing, partials)
    out = []
    for i, tok in enumerate(gen):
        out.append(tok)
        if i == 1:
            gen.close()                       # 用户点击停止
    assert billing["cancelled"] and not billing["finished"]
    assert billing["tokens"] == 2, "取消后不再计费"
    assert billing["connections"] == 0, "连接已清理"
    assert partials == ["你好"], "部分结果已保存"
    print("取消成功:计费", billing["tokens"], "片,部分结果:", partials[0])
