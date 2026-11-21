"""多语言字段的返回结构与回退链: 按请求链路取, 永不空手(纯标准库)。"""

FIELD = {"zh": "你好", "en": "Hello", "ja": "こんにちは"}
MISSING_FIELD = {"zh": "只有中文"}


def parse_accept_language(header):
    """q 值排序: 语言标签与权重成对解析, q 缺省为 1, 同 q 按出现顺序。"""
    entries = []
    for i, part in enumerate((header or "").split(",")):
        seg = part.strip()
        if not seg:
            continue
        tag, _, q = seg.partition(";q=")
        try:
            weight = float(q) if q else 1.0
        except ValueError:
            weight = 1.0
        entries.append((-weight, i, tag.strip().lower()))
    return [tag for _, _, tag in sorted(entries)]


def chain_for(header):
    """请求语言 -> 语言主部 -> 兜底 en -> 兜底 zh, 链由服务端拼接, 客户端只给偏好。"""
    tags = parse_accept_language(header)
    chain = []
    for tag in tags:
        chain.append(tag)
        if "-" in tag:
            chain.append(tag.split("-")[0])
    chain.extend(["en", "zh"])
    return list(dict.fromkeys(chain))  # 去重保序


def resolve(field, header):
    for lang in chain_for(header):
        if lang in field and field[lang] != "":
            return {"text": field[lang], "matched": lang}
    return {"text": "", "matched": None}


assert parse_accept_language("zh-CN,zh;q=0.8,en;q=0.6") == ["zh-cn", "zh", "en"]
assert parse_accept_language("en;q=0.4,fr") == ["fr", "en"], "fr 权重 1 优先于 en 的 0.4"
r1 = resolve(FIELD, "zh-CN,zh;q=0.8,en;q=0.6")
assert r1 == {"text": "你好", "matched": "zh"}
r2 = resolve(FIELD, "de-DE,fr")
assert r2 == {"text": "Hello", "matched": "en"}, "链尾兜底 en 命中"
r3 = resolve(MISSING_FIELD, "ja-JP")
assert r3 == {"text": "只有中文", "matched": "zh"}, "ja->ja->en 都缺, 落到 zh"
r4 = resolve({}, "en")
assert r4["matched"] is None, "全链落空返回 null 并让客户端出默认文案"
print("回退链: zh-CN -> zh -> en -> zh; 空串视为缺失, 永不返回半截结构")
