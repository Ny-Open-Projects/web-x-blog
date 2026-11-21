import csv
import io


def import_rows(text: str) -> dict:
    ok_rows, errors = [], []
    reader = csv.DictReader(io.StringIO(text))
    for lineno, row in enumerate(reader, start=2):  # 表头是第 1 行
        try:
            name = row["name"].strip()
            if not name:
                raise ValueError("empty name")
            amount = int(row["amount"])  # 显式类型转换
            ok_rows.append((name, amount))
        except (KeyError, ValueError) as exc:
            errors.append({"line": lineno, "reason": str(exc)})
    return {"imported": len(ok_rows), "failed": len(errors), "errors": errors}


if __name__ == "__main__":
    sample = "name,amount\nalice,10\n,bad\nbob,xx\n"
    print(import_rows(sample))
