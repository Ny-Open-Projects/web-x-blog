
DIRTY_LOG = (b"[2026-11-05] user=\xe4\xb8\xad\xe6\x96\x87 action=login\n"
             b"[2026-11-05] note=\xff\xfe broken bytes here\n")


def try_strategies(payload):
    strategies = ("strict", "replace", "ignore", "backslashreplace",
                  "surrogateescape")
    out = {}
    for name in strategies:
        try:
            out[name] = payload.decode("utf-8", errors=name)
        except UnicodeDecodeError as err:
            out[name] = "!error: UnicodeDecodeError at byte %d" % err.start
    return out


def safe_display(text):
    """含代理区码点的字符串不能直接 print,转义后展示。"""
    return text.encode("ascii", errors="backslashreplace").decode("ascii")


if __name__ == "__main__":
    for name, text in try_strategies(DIRTY_LOG).items():
        if text.startswith("!error:"):
            print(f"{name:>16}: {text}")
        else:
            one_line = text.splitlines()[1]
            print(f"{name:>16}: {safe_display(one_line)}")

    # surrogateescape 往返:坏字节无损还原
    decoded = DIRTY_LOG.decode("utf-8", errors="surrogateescape")
    restored = decoded.encode("utf-8", errors="surrogateescape")
    print("roundtrip lossless:", restored == DIRTY_LOG)

    # replace 的占位符是什么
    print("U+FFFD is:", repr("\ufffd"),
          "len:", len(b"\xff".decode("utf-8", errors="replace")))

    # latin-1 永不失败,但多字节会碎成乱码——降级链的最后一步
    print("latin-1 fallback:", DIRTY_LOG.decode("latin-1").splitlines()[1][:30])
