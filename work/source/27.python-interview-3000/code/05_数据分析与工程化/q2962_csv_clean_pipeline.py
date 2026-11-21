"""CSV 清洗完整管线: 编码探测 -> 解析 -> 去重 -> 类型修正 -> 归一化, 全程留台账"""
import csv
import io
import json

# 模拟上游: 一个 utf-8 带 BOM 的文件, 一个 gbk 的文件, 以及一段彻底乱码的字节
UTF8_BYTES = "uid,name,age,phone\n1,Alice ,29,13800000001\n2,bob,35,13800000002\n".encode("utf-8-sig")
GBK_BYTES = "uid,name,age,phone\n3,张三,,13900000003\n3,张三,41,13900000003\n4,李四,abc,137-0000-0004\n".encode("gbk")
BROKEN_BYTES = b"\xff\xfe\xfa\x01garbled"


def decode_smart(raw):
    """编码探测: 依次尝试常见编码, 全部失败抛 ValueError, 绝不静默替换字符"""
    for enc in ("utf-8-sig", "utf-8", "gbk"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    raise ValueError("无法识别编码, 字节头=%r" % raw[:4])


def parse(text):
    rows = list(csv.DictReader(io.StringIO(text)))
    return rows


def clean(rows):
    """去重 -> 类型修正 -> 归一化, 返回 干净行/拒绝行/告警"""
    good, rejects, warns, seen = [], [], [], set()
    for i, r in enumerate(rows):
        uid = r["uid"].strip()
        if uid in seen:
            rejects.append({"row": i, "uid": uid, "reason": "duplicate"})
            continue
        seen.add(uid)
        rec = {"uid": uid, "name": r["name"].strip().title()}
        try:
            rec["age"] = int(r["age"])
            if rec["age"] < 0 or rec["age"] > 150:
                raise ValueError("age 越界")
        except ValueError:
            if r["age"] == "":                      # 缺失允许, 置 None 并告警
                rec["age"] = None
                warns.append({"row": i, "uid": uid, "field": "age", "msg": "缺失置空"})
            else:                                   # 类型错或越界, 拒收
                rejects.append({"row": i, "uid": uid, "reason": "bad_age", "raw": r["age"]})
                continue
        digits = "".join(ch for ch in r["phone"] if ch.isdigit())
        if len(digits) == 11 and digits.startswith("1"):
            rec["phone"] = digits                   # 统一为 11 位裸号
        else:
            rejects.append({"row": i, "uid": uid, "reason": "bad_phone", "raw": r["phone"]})
            continue
        good.append(rec)
    return good, rejects, warns


if __name__ == "__main__":
    all_rows, sources = [], []
    for name, raw in [("orders_utf8.csv", UTF8_BYTES), ("orders_gbk.csv", GBK_BYTES)]:
        try:
            text, enc = decode_smart(raw)
            rows = parse(text)
            sources.append({"file": name, "encoding": enc, "rows": len(rows)})
            all_rows.extend(rows)
        except ValueError as e:
            sources.append({"file": name, "error": str(e)})
    try:
        decode_smart(BROKEN_BYTES)
    except ValueError as e:
        print("故意乱码被拦截:", e)

    print("读取台账:", json.dumps(sources, ensure_ascii=False))
    good, rejects, warns = clean(all_rows)
    print("清洗: 原始 %d 行 -> 合格 %d 行, 拒收 %d 条, 告警 %d 条"
          % (len(all_rows), len(good), len(rejects), len(warns)))
    print("拒收:", json.dumps(rejects, ensure_ascii=False))
    print("告警:", json.dumps(warns, ensure_ascii=False))
    for g in good:
        print("  合格:", json.dumps(g, ensure_ascii=False))
    print("要点: 编码探测失败要硬失败, 缺失与类型错分开处置, 归一化统一在最后一步, 每行去留都有台账")
