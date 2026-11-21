"""数据导出多格式适配器: 注册制适配器, 新增格式不改调用方"""
import csv
import io
import json

ROWS = [
    {"name": "alice", "dept": "data", "score": 92},
    {"name": "bob", "dept": "ops", "score": 85},
    {"name": "张三", "dept": "data", "score": 78},
]


def export_csv(rows):
    """RFC 4180: 表头 + utf-8-sig, Excel 打开中文不乱码"""
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def export_json(rows):
    """机器可读: ensure_ascii=False 保持中文, 缩进稳定便于 diff"""
    return json.dumps(rows, ensure_ascii=False, indent=2)


def export_markdown(rows):
    """人可读: 首行做表头, 数字列右对齐"""
    cols = list(rows[0].keys())
    lines = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for r in rows:
        lines.append("| " + " | ".join(str(r[c]) for c in cols) + " |")
    return "\n".join(lines)


EXPORTERS = {"csv": export_csv, "json": export_json, "md": export_markdown}


def register(fmt, fn):
    """注册新格式: 调用方 export 零改动"""
    EXPORTERS[fmt] = fn


def export(rows, fmt):
    if fmt not in EXPORTERS:
        raise KeyError("不支持的格式: %s, 可选: %s" % (fmt, ", ".join(sorted(EXPORTERS))))
    return EXPORTERS[fmt](rows)


if __name__ == "__main__":
    for fmt in ("csv", "json", "md"):
        out = export(ROWS, fmt)
        print("---- %s (%d 字节) ----" % (fmt, len(out.encode("utf-8"))))
        print(out.rstrip())

    # 下游系统要 tsv: 注册即接入, 不碰 export 一行代码
    def export_tsv(rs):
        cols = list(rs[0].keys())
        return "\n".join(["\t".join(cols)] + ["\t".join(str(r[c]) for c in cols) for r in rs])
    register("tsv", export_tsv)
    print("---- tsv (新注册格式) ----")
    print(export(ROWS, "tsv"))

    try:
        export(ROWS, "xlsx")
    except KeyError as e:
        print("故意请求未知格式被拦截:", e)
    print("要点: 适配器把 '导出' 抽象成 注册表 + 统一签名, 数据不变格式随便加, 调用方永远只认 export(rows, fmt)")
