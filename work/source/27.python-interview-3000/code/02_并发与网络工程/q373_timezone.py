"""时区处理:naive vs aware、UTC 存储、本地展示。"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

if __name__ == "__main__":
    # 1. 正确方式:创建带时区的 aware 时间
    now_utc = datetime.now(timezone.utc)
    print("UTC   :", now_utc.isoformat())

    # 2. 转上海时区展示,自动处理 +8
    sh = now_utc.astimezone(ZoneInfo("Asia/Shanghai"))
    print("上海  :", sh.isoformat())

    # 3. 夏令时验证:纽约 7 月与 12 月偏移不同
    ny_summer = datetime(2026, 7, 1, 12, tzinfo=ZoneInfo("America/New_York"))
    ny_winter = datetime(2026, 12, 1, 12, tzinfo=ZoneInfo("America/New_York"))
    print("NY 夏令时偏移:", ny_summer.utcoffset(), "冬季:", ny_winter.utcoffset())

    # 4. 危险方式:naive + replace 只改字段不换算,是错误示范
    naive = datetime(2026, 11, 1, 10, 0, 0)
    wrong = naive.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
    correct = naive.replace(tzinfo=ZoneInfo("Asia/Shanghai")).astimezone(timezone.utc)
    print("错误理解:", wrong, "正确换算:", correct)

    # 5. aware 之间才能安全比较与做差
    print("时间差:", now_utc - ny_winter.astimezone(timezone.utc))
