import os

def check_settings(s: dict) -> list:
    problems = []
    if s.get("DEBUG", True):
        problems.append("DEBUG 必须为 False")
    if s.get("ALLOWED_HOSTS") in (None, [], ["*"]):
        problems.append("ALLOWED_HOSTS 必须白名单具体域名")
    if not s.get("SECRET_KEY"):
        problems.append("SECRET_KEY 必须来自环境变量或密钥服务")
    if s.get("SECURE_SSL_REDIRECT") is not True:
        problems.append("建议开启 HTTPS 强制跳转")
    return problems

prod = {
    "DEBUG": False,
    "ALLOWED_HOSTS": ["api.example.com"],
    "SECRET_KEY": os.environ.get("DJANGO_SECRET_KEY", ""),
    "SECURE_SSL_REDIRECT": True,
}
print("检查结果:", check_settings(prod))
