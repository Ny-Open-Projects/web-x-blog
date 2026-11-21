"""IDN 域名: punycode 与同形异义字。

- 国际化域名在 DNS 里只能存 ASCII: 非 ASCII 标签被编码成 xn-- 前缀的
  punycode(ASCII 兼容编码 ACE), "中文.jp" 在线上其实是 xn--fiq228c.jp;
- 风险: 西里尔字母 а 与拉丁字母 a 长得一模一样, punycode 却完全不同 ——
  同形异义字(homograph)钓鱼; 多脚本混排检测是最实用的防线。
"""
import unicodedata


def to_ascii(domain):
    return domain.encode("idna").decode("ascii")


def to_unicode(domain):
    return domain.encode("ascii").decode("idna")


def label_scripts(label):
    """一个标签里出现的文字系统集合, 用于同形异义字检测。"""
    scripts = set()
    for ch in label:
        name = unicodedata.name(ch, "")
        if name:
            scripts.add(name.split()[0])
    return scripts


def looks_suspicious(domain):
    for label in domain.split("."):
        if len(label_scripts(label)) > 1:
            return True
    return False


def main():
    # 1) 编解码往返
    ace = to_ascii("中文.jp")
    back = to_unicode(ace)
    print("中文.jp -> ACE:", ace, "-> 还原:", back)
    assert back == "中文.jp", "IDN 编解码应无损往返"

    # 2) 纯 punycode 编码(不带 xn-- 外壳)
    print("münchen 的 punycode:", "münchen".encode("punycode").decode())
    assert "münchen".encode("punycode").decode().startswith("mnchen")

    # 3) 同形异义字: 视觉相同, 字节不同
    real = "apple.com"
    fake = "\u0430pple.com"          # 首字母是西里尔 а U+0430
    print("真实域名:", real, "ACE:", to_ascii(real))
    print("仿冒域名:", fake, "ACE:", to_ascii(fake))
    assert to_ascii(real) != to_ascii(fake), "视觉相同但编码必然不同"

    # 4) 混排检测
    verdicts = [(d, looks_suspicious(d)) for d in (real, fake)]
    for d, bad in verdicts:
        print("检测 %-12s -> %s" % (d, "可疑(多脚本混排)" if bad else "正常"))
    assert not looks_suspicious(real) and looks_suspicious(fake)

    print("结论: IDN 是编码层的事, 显示层的事是同形字——证书校验挡不住视觉欺骗")


if __name__ == "__main__":
    main()
