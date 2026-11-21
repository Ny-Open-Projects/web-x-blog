"""密码强度策略与 KDF 成本参数(纯标准库)。"""
import hashlib
import hmac
import time

COMMON = {"123456", "password", "qwerty", "admin123", "password1"}


def policy_check(pwd):
    """静态策略: 返回问题列表, 空列表即合格。"""
    problems = []
    if len(pwd) < 10:
        problems.append("长度至少 10 位")
    classes = sum([any(c.islower() for c in pwd),
                   any(c.isupper() for c in pwd),
                   any(c.isdigit() for c in pwd),
                   any(not c.isalnum() for c in pwd)])
    if classes < 3:
        problems.append("至少覆盖小写 大写 数字 符号中的三类")
    if pwd.lower() in COMMON:
        problems.append("命中常见弱口令表")
    for i in range(len(pwd) - 2):
        if pwd[i] == pwd[i + 1] == pwd[i + 2]:
            problems.append("存在三连重复字符")
            break
    return problems


def kdf_hash(pwd, salt, cost=60000):
    """PBKDF2-HMAC-SHA256, cost 是迭代次数, 随硬件升级而调高。"""
    return hashlib.pbkdf2_hmac("sha256", pwd.encode(), salt, cost)


def kdf_verify(pwd, salt, expected, cost=60000):
    """校验必须用常数时间比较, 防逐字节侧信道。"""
    return hmac.compare_digest(kdf_hash(pwd, salt, cost), expected)


for pwd in ["abc", "password1", "aaaaaaaaaa1", "S3:Summer!2026"]:
    problems = policy_check(pwd)
    print("{:16s} -> {}".format(pwd, problems if problems else "通过"))

assert policy_check("abc") == ["长度至少 10 位", "至少覆盖小写 大写 数字 符号中的三类"]
assert any("弱口令" in p for p in policy_check("password1"))
assert any("三连" in p for p in policy_check("aaaaaaaaaa1"))
assert policy_check("S3:Summer!2026") == []

salt = b"\x9f" * 16                                 # 每个用户独立随机盐
t0 = time.perf_counter()
digest = kdf_hash("S3:Summer!2026", salt, cost=60000)
elapsed = time.perf_counter() - t0
print("PBKDF2 cost=60000 单次耗时 {:.0f} ms".format(elapsed * 1000))
assert kdf_verify("S3:Summer!2026", salt, digest)
assert not kdf_verify("s3:summer!2026", salt, digest)
print("要点: 策略挡弱口令, KDF 挡拖库爆破; "
      "独立盐防彩虹表, cost 控制单次验证成本, 校验用 compare_digest 常数时间比较")
