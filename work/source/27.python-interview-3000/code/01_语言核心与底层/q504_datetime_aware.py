from datetime import datetime, timedelta, timezone

if __name__ == "__main__":
    naive = datetime(2026, 11, 1, 12, 0)
    aware = datetime(2026, 11, 1, 12, 0, tzinfo=timezone(timedelta(hours=8)))
    print("naive tzinfo:", naive.tzinfo)
    print("aware offset:", aware.utcoffset())

    try:
        naive < aware
    except TypeError as e:
        print("cannot compare:", e)

    print("to UTC:", aware.astimezone(timezone.utc).isoformat())
    print("epoch:", aware.timestamp())
    print("now UTC:", datetime.now(timezone.utc).isoformat())
    print("naive now has no tzinfo:", datetime.now().tzinfo is None)
