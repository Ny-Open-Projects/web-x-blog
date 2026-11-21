"""异常指纹:类型加最内层帧聚合(纯标准库)。"""
import hashlib
import traceback


def fingerprint(exc_type, tb_text):
    frames = []
    for line in tb_text.strip().splitlines():
        s = line.strip()
        if s.startswith("File ") and ", in " in s:
            frames.append(s.rsplit(" in ", 1)[1].strip())
    raw = exc_type + "@" + "|".join(frames[-3:])
    return hashlib.sha1(raw.encode()).hexdigest()[:12]


def capture(fn):
    try:
        fn()
        return None
    except Exception as exc:
        return fingerprint(type(exc).__name__, traceback.format_exc())


def boom_key():
    return {}["missing"]


def boom_value():
    return int("not-a-number")


fp1 = capture(boom_key)
fp2 = capture(boom_key)
fp3 = capture(boom_value)
print("同异常指纹一致:", fp1 == fp2, fp1)
print("不同异常指纹不同:", fp1 != fp3, fp3)
print("指纹稳定可做聚合键,窗口内只通知一次")
