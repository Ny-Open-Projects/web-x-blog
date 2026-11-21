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
