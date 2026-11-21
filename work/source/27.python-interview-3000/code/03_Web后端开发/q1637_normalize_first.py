"""规范化必须先于校验: before 与 after 的顺序实战(纯标准库模拟)。"""


def wrong_order(raw):
    """坏味道: 先格式校验后规范化 -> 带空格或大写的合法输入被误拒。"""
    if "@" not in raw or " " in raw:
        return "拒绝"
    return "通过: " + raw.strip().lower()


def right_order(raw):
    """正确: mode=before 里先规范化, 格式校验看到的是干净数据。"""
    cleaned = raw.strip().lower()
    if "@" not in cleaned:
        return "拒绝"
    return "通过: " + cleaned


cases = [" A@B.COM ", "a@b.com", "not-email"]
for c in cases:
    print(repr(c), "坏顺序:", wrong_order(c), "| 好顺序:", right_order(c))

phone_raw = " 138 0000 0000 "
clean = phone_raw.strip().replace(" ", "")
print("电话规范化:", clean, "位数合法:", len(clean) == 11)
print("要点: 清洗放 before, 断言放 after; 两类逻辑混进同一个校验器最容易出隐性 bug")
