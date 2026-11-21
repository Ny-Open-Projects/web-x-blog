"""Session ID 的生成强度与恒定时间比较(纯标准库)。"""
import hmac
import secrets

# 弱示例:顺序号完全可预测,仅作对照
weak_sids = [f"SID-{i:08d}" for i in range(3)]
print("弱 SID 可预测:", weak_sids)

strong = secrets.token_urlsafe(32)          # 32 字节 = 256 位熵
print("强 SID 示例:", strong[:16], "... 熵 bits:", 32 * 8)

# 恒定时间比较:避免逐字节短路带来的计时侧信道
a, b = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
print("compare_digest 自身:", hmac.compare_digest(strong, strong))
print("compare_digest 他人:", hmac.compare_digest(strong, b))
