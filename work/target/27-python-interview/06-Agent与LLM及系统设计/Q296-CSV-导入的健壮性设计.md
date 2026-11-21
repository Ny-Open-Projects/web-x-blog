---
title: [Q296] CSV 导入的健壮性设计
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q296 · CSV 导入的健壮性设计
> 难度:★★★ | 标签:数据处理, 健壮性

**问**:用户上传 CSV 批量导入,格式五花八门,如何设计一个健壮的导入流程?

**答**:要点:用 `csv.DictReader` 按表头映射而非下标;逐行校验并收集错误(行号+原因),坏行跳过不中断全量;类型转换显式处理(金额用 Decimal、日期 strptime);限制文件大小与编码(`utf-8-sig` 兼容 Excel 导出的 BOM);结果返回成功/失败统计。关键决策:部分成功(跳过坏行)还是全量回滚,要和业务确认。

```python
# file: code/06_Agent与LLM及系统设计/q296_csv_import.py
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
```

**追问**:
- 部分成功和全量回滚怎么选?——数据完整性要求高(账务)全量回滚;批量导入类部分成功+错误清单更实用;必须和业务方确认。
- 金额为什么用 Decimal?——float 二进制误差会让 0.1+0.2≠0.3,账务对不上分;入库也用精确类型。
- utf-8-sig 是什么?——带 BOM 的 UTF-8,兼容 Excel 导出;按 utf-8 读会多出 \ufeff 污染第一列表头。

---
