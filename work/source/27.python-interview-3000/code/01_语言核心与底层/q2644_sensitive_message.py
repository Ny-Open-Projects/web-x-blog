"""异常消息的脱敏:自定义异常在 __str__ 统一裁剪。"""
import re

SECRET_RE = re.compile(r"(token|password|secret)=(\S+)", re.IGNORECASE)


def scrub(text):
    """把键值对形态的凭证替换为占位。"""
    return SECRET_RE.sub(r"\1=***", text)


class ApiError(Exception):
    """对外异常:__str__ 强制脱敏,原始消息不出境。"""

    def __init__(self, message, status):
        super().__init__(scrub(message))
        self.status = status


def call_api(url, token):
    raise ApiError(
        f"POST {url} 失败 token={token} status=401", status=401)


if __name__ == "__main__":
    try:
        call_api("https://api.example.com/v1/user", "s3cr3t-token")
    except ApiError as exc:
        print("对外消息:", exc)
        print("状态码:", exc.status)
