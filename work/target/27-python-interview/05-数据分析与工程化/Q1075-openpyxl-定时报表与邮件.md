---
title: [Q1075] openpyxl 定时报表与邮件
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1075 · openpyxl 定时报表与邮件

> 难度:★★★☆ | 标签:报表, 自动化

**问**:运营每天早上要一份带样式的 Excel 日报并邮件发群,这个自动化怎么写才不变成"每周修一次的脚本"?

**答**:骨架四段:取数(SQL/DuckDB)、加工与校验(缺失率、行数阈值,数据不对就不发,宁可迟到不发错)、openpyxl 生成带样式的多 sheet(表头加粗填色、冻结首行、列宽、条件格式)、邮件发送(EmailMessage + 附件)。工程化要点:定时交给 cron/调度系统,脚本自己只做"一次运行";凭证走环境变量;失败要有重试与告警,别让静默失败吞掉一天的数据;输出文件带日期命名并归档,方便回溯。

```python
# file: code/05_数据分析与工程化/q1075_openpyxl_report.py
import csv
import os
import tempfile

rows = [["date", "city", "gmv"], ["2026-10-31", "bj", 1200], ["2026-10-31", "sh", 1800]]
out_dir = tempfile.gettempdir()

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill
    wb = Workbook()
    ws = wb.active
    ws.title = "日报"
    ws.append(["日期", "城市", "GMV"])
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="4472C4")
    for r in rows[1:]:
        ws.append(r)
    ws.freeze_panes = "A2"
    ws.column_dimensions["A"].width = 14
    path = os.path.join(out_dir, "daily_report_20261031.xlsx")
    wb.save(path)
    print("已生成 Excel:", path)
except ImportError:
    path = os.path.join(out_dir, "daily_report_20261031.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)
    print("未安装 openpyxl,降级生成 CSV:", path)

from email.message import EmailMessage
msg = EmailMessage()
msg["Subject"] = "每日经营报表 2026-10-31"
msg["From"] = os.environ.get("REPORT_FROM", "bot@example.com")
msg["To"] = os.environ.get("REPORT_TO", "me@example.com")
msg.set_content("详见附件,数据截至 2026-10-31")
with open(path, "rb") as f:
    msg.add_attachment(
        f.read(), maintype="application", subtype="octet-stream", filename=os.path.basename(path)
    )
print("邮件已构建,主题:", msg["Subject"], "附件:", os.path.basename(path))
print("定时交给 cron 或调度系统;失败重试并告警;凭证走环境变量")
```

**追问**:
- 追问 1:为什么"数据不对就不发"很重要?—— 一封错误报表的信任成本远高于一次迟到,校验失败应转告警而不是静默发出。
- 追问 2:openpyxl 和 xlsxwriter 怎么选?—— xlsxwriter 写入更快、图表更强;openpyxl 支持读写已有文件,做"改模板"类报表更合适。

```mermaid
flowchart LR
    A[定时触发 cron] --> B[取数 SQL 或 DuckDB]
    B --> C[pandas 加工与口径校验]
    C --> D[openpyxl 生成多 sheet 报表]
    D --> E[附件邮件或归档]
    E --> F[运行日志与失败告警]
```
