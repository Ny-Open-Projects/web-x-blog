"""枚举值扩展兼容: 新值对老代码的冲击与双兼容窗口"""

OLD_STATUSES = {"created", "paid", "void"}
NEW_STATUSES = OLD_STATUSES | {"refunding", "refunded"}

def legacy_reader(status):
    """老版本代码: 只认识旧枚举 未知值全部掉进 else 分支"""
    if status == "paid":
        return "已支付"
    if status == "void":
        return "已作废"
    if status == "created":
        return "待支付"
    return "未知状态"

def compat_reader(status, mapping=None):
    """兼容读: 新值映射回最接近的旧语义 建立在发布顺序约定上"""
    mapping = mapping or {"refunding": "paid", "refunded": "paid"}
    return legacy_reader(mapping.get(status, status))

for s in ["created", "paid", "refunding", "refunded"]:
    print(f"{s:10s} 老代码读 -> {legacy_reader(s):6s}  兼容读 -> {compat_reader(s)}")

# 写方向约束: 兼容期内老写入方写新值必须显式失败 比静默落库安全
def legacy_writer(status):
    if status not in OLD_STATUSES:
        raise ValueError("未知状态 %s 老写入方直接失败" % status)
    return True

for s in ["paid", "refunded"]:
    try:
        legacy_writer(s)
        print(f"写入 {s} -> 成功")
    except ValueError as e:
        print(f"写入 {s} -> 拒绝: {e}")
print("结论: 枚举扩展先发读兼容 再放开写权限 兼容映射要有退役时间 新旧两侧的兼容窗口要错开")
