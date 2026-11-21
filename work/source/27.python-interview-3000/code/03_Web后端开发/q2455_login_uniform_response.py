"""登录的统一失败语义与恒定时间比较(纯标准库)。"""
import hashlib
import hmac
import time

ITER = 20000
SALT = b"static-demo-salt"
DUMMY = hashlib.pbkdf2_hmac("sha256", b"dummy-password-for-timing", SALT, ITER)
USERS = {"alice": hashlib.pbkdf2_hmac("sha256", b"right-pass", SALT, ITER)}


def attempt(user, pwd):
    """无此用户也跑一遍 KDF 与比较, 让两种失败的耗时形态一致。"""
    stored = USERS.get(user, DUMMY)
    got = hashlib.pbkdf2_hmac("sha256", pwd.encode(), SALT, ITER)
    ok = user in USERS and hmac.compare_digest(got, stored)
    message = "登录成功" if ok else "用户名或密码错误"
    return ok, message


def timing_of(user, pwd, n=5):
    best = None
    for _ in range(n):
        t0 = time.perf_counter()
        attempt(user, pwd)
        dt = time.perf_counter() - t0
        best = dt if best is None else min(best, dt)
    return best


ok1, msg1 = attempt("alice", "right-pass")
ok2, msg2 = attempt("ghost", "whatever")
ok3, msg3 = attempt("alice", "wrong-pass")
print("真实用户+正确密码 -> {} {}".format(ok1, msg1))
print("不存在用户        -> {} {}".format(ok2, msg2))
print("真实用户+错误密码 -> {} {}".format(ok3, msg3))
assert (ok1, ok2, ok3) == (True, False, False)
assert msg2 == msg3, "两种失败必须返回完全相同的文案"

t_ghost = timing_of("ghost", "whatever")
t_wrong = timing_of("alice", "wrong-pass")
print("不存在用户耗时 {:.1f}ms, 密码错误耗时 {:.1f}ms".format(
    t_ghost * 1000, t_wrong * 1000))
assert 0.5 * t_wrong <= t_ghost <= 2.0 * t_wrong, "两种失败的耗时形态应接近"

# 常数时间比较的意义: 逐字节短路比较会在前缀匹配时更快, 泄露匹配进度
assert hmac.compare_digest(b"aaaa", b"aaab") is False
print("要点: 统一文案消除信息差, 不存在用户也烧一次 KDF 拉平耗时, "
      "compare_digest 避免短路比较泄露匹配程度, 三件事共同压缩枚举与侧信道空间")
