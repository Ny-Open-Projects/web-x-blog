import functools
import operator

def send_email(to, subject, body, *, dry_run=False):
    return f"[{subject}] to {to}: {body}{' (dry)' if dry_run else ''}"

if __name__ == "__main__":
    notify_admin = functools.partial(send_email, "admin@corp.local")
    crash_alert = functools.partial(notify_admin, subject="CRASH", dry_run=True)
    print(crash_alert(body="worker died"))

    int2 = functools.partial(int, base=2)     # 固化关键字参数
    print(int2("1010"))

    double = functools.partial(operator.mul, 2)
    print(list(map(double, [1, 2, 3])))
    print("overridable:", crash_alert.keywords["dry_run"])   # partial 元数据可见
