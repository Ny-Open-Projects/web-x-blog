---
title: [Q340] Excel / CSV 导入导出健壮性
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q340 · Excel / CSV 导入导出健壮性

> 难度:★★☆ | 标签:csv, 编码, 脏行

**问**:导入外部 CSV 时常见哪些坑?如何写出健壮的导入代码?

**答**:高频坑:编码(GBK vs UTF-8,先用 chardet/file 命令探测或逐个尝试)、脏行(字段数不对、引号未闭合、混入小计行)、类型污染(同一列混有 "1,000" 千分位、"N/A" 文本)、大文件内存、以及 Excel 的日期自动转换篡改数据。健壮做法:csv 模块显式指定 encoding 和 quoting、逐行校验字段数并把坏行写入 reject 文件而不是中断、数值解析统一走 `to_numeric(errors="coerce")` 后检查 coerce 数量、导出时用 `utf-8-sig` 兼容 Excel 打开。

```python
# file: code/05_数据分析与工程化/q340_csv_robust.py
import csv
import os
import tempfile

def robust_import(path, expect_cols=2):
    good, bad = [], []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for lineno, row in enumerate(reader, start=2):
            if len(row) != expect_cols:          # 脏行进 reject,不中断
                bad.append((lineno, row))
                continue
            try:
                amt = float(row[1].replace(",", ""))   # 处理千分位
            except ValueError:
                bad.append((lineno, row))
                continue
            good.append((row[0], amt))
    return good, bad

def export_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:  # Excel 兼容
        w = csv.writer(f)
        w.writerow(["city", "amt"])
        w.writerows(rows)

if __name__ == "__main__":
    # 演示文件放临时目录,避免污染当前工作目录
    tmpdir = tempfile.mkdtemp()
    dirty_path = os.path.join(tmpdir, "dirty.csv")
    clean_path = os.path.join(tmpdir, "clean.csv")
    with open(dirty_path, "w", newline="", encoding="utf-8") as f:
        f.write("city,amt\nBJ,1,000\nSH,20\nSZ\nBJ,30\n")
    good, bad = robust_import(dirty_path)
    print("good:", good)
    print("bad lines:", bad)
    export_csv(clean_path, good)
    os.remove(dirty_path); os.remove(clean_path)
    os.rmdir(tmpdir)
```

**追问**:
- pandas 里如何拿到坏行?没有直接参数,思路是先用 `on_bad_lines="skip"` 粗导,再与逐行校验的结果做差集定位坏行,或干脆用 csv 模块预清洗。
- utf-8-sig 解决什么?——Excel 打开 UTF-8 CSV 中文乱码,BOM 头让 Excel 识别编码;导出给 Excel 用户必带。
- 千分位与货币符号怎么清洗?——`str.replace(',','')` 后 to_numeric(errors='coerce'),并统计 coerce 出的 NaT/NaN 数量验证清洗率。
- Excel 日期篡改怎么防?——「1-2」被转日期、长数字转科学计数;模板列设文本格式,或改用 CSV 交付关键数据。
