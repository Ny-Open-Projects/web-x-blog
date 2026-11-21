"""CSV 导入的流式校验: 逐行验证 唯一性检查 错误配额提前终止(纯标准库)。"""
import csv
import io

REQUIRED = ["uid", "age", "email"]
MAX_ERRORS = 3


def validate_stream(row_iter, now_rows=None):
    """row_iter 是按行产出的文本迭代器, 模拟逐行读取大文件。"""
    errors, seen, ok_count = [], set(), 0
    reader = csv.DictReader(row_iter)
    if reader.fieldnames is None:
        return 0, [{"line": 1, "field": None, "message": "空文件"}]
    missing_cols = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
    if missing_cols:
        return 0, [{"line": 1, "field": None,
                    "message": "表头缺少必填列: " + ",".join(missing_cols)}]
    for row_no, row in enumerate(reader, start=2):
        if len(errors) >= MAX_ERRORS:
            errors.append({"line": None, "field": None,
                           "message": "错误数达到配额 {}, 提前终止".format(MAX_ERRORS)})
            break
        problem = None
        for col in REQUIRED:
            if not (row.get(col) or "").strip():
                problem = {"line": row_no, "field": col, "message": "必填列缺失"}
                break
        if problem is None and not row["age"].isdigit():
            problem = {"line": row_no, "field": "age", "message": "年龄必须是整数"}
        elif problem is None and not 0 <= int(row["age"]) <= 120:
            problem = {"line": row_no, "field": "age", "message": "年龄必须在 0..120"}
        elif problem is None and "@" not in row["email"]:
            problem = {"line": row_no, "field": "email", "message": "邮箱格式不合法"}
        elif problem is None and row["uid"] in seen:
            problem = {"line": row_no, "field": "uid", "message": "uid 重复"}
        if problem:
            errors.append(problem)
        else:
            seen.add(row["uid"])
            ok_count += 1
    return ok_count, errors


good_csv = "uid,age,email\nu1,30,a@x.com\nu2,41,b@x.com\n"
bad_csv = ("uid,age,email\n"
           "u1,30,a@x.com\n"
           ",25,c@x.com\n"          # 缺 uid
           "u2,abc,d@x.com\n"       # 年龄非数字
           "u1,30,e@x.com\n"        # uid 重复
           "u3,999,f@x.com\n"       # 年龄越界
           "u9,20,g@x.com\n")       # 配额已满, 不再校验

n_ok, errs = validate_stream(io.StringIO(good_csv))
print("合法文件: 通过 {} 行, 错误 {}".format(n_ok, errs))
assert n_ok == 2 and errs == []

n_ok2, errs2 = validate_stream(io.StringIO(bad_csv))
print("非法文件: 通过 {} 行".format(n_ok2))
for e in errs2:
    print("  行 {} 字段 {}: {}".format(e["line"], e["field"], e["message"]))
assert n_ok2 == 1
assert len(errs2) == MAX_ERRORS + 1 and errs2[-1]["field"] is None
assert [e["field"] for e in errs2[:3]] == ["uid", "age", "uid"]

n_ok3, errs3 = validate_stream(io.StringIO("id,note\n1,hi\n"))
assert n_ok3 == 0 and "表头缺少必填列" in errs3[0]["message"]
print("要点: 流式校验只保留 累积错误列表 与 已见键集合, 内存不随文件涨; "
      "错误配额让脏文件快速失败, 行号让用户能直接定位")
