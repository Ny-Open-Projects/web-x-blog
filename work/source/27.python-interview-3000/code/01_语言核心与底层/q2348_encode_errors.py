"""encode 的 errors 策略对比:strict、ignore、replace 与转写家族。"""
import codecs

if __name__ == "__main__":
    text = "价格 ¥100,café"
    for policy in ["strict", "ignore", "replace",
                   "xmlcharrefreplace", "backslashreplace", "namereplace"]:
        try:
            out = text.encode("ascii", errors=policy)
        except UnicodeEncodeError as exc:
            out = f"报错: {exc.reason}"
        print(f"{policy:>18}: {out}")

    def star_replace(exc):
        """自定义策略:编码不了的字符换成星号。"""
        return ("*", exc.end)

    codecs.register_error("star", star_replace)
    print("自定义 star:", text.encode("ascii", errors="star"))

    dirty = b"caf\xe9"
    print("decode replace:", dirty.decode("ascii", errors="replace"))
    print("decode backslashreplace:", dirty.decode("ascii", errors="backslashreplace"))
