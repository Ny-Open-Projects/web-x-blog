"""管道错误分类器:可重试、致命、未知三类,给不同处置动作"""

CLASSIFIER = [
    (("timeout", "timed out"), "RETRYABLE", "指数退避重试"),
    (("connection", "eof", "reset"), "RETRYABLE", "指数退避重试"),
    (("503", "throttl", "rate limit"), "RETRYABLE", "限流退避, 降低并发"),
    (("permission", "access denied", "403"), "FATAL", "检查凭证与授权, 不重试"),
    (("syntax", "column not found", "schema"), "FATAL", "修代码或对齐 schema, 不重试"),
    (("oom", "out of memory", "killed"), "FATAL", "扩内存或优化逻辑, 不重试"),
]


def classify(message):
    low = message.lower()
    for tokens, category, action in CLASSIFIER:
        if any(t in low for t in tokens):
            return category, action
    return "UNKNOWN", "人工介入, 先查上下文再定策略"


ERRORS = [
    "ReadTimeout: socket timed out after 30s",
    "HTTP 503 Service Unavailable",
    "AnalysisException: column not found: user_city",
    "AccessDenied: 403 on s3://bucket/path",
    "Cannot allocate memory (OOM killed)",
    "weird stack trace nobody has seen",
]

if __name__ == "__main__":
    for msg in ERRORS:
        cat, action = classify(msg)
        print(f"[{cat}] {action} <- {msg[:60]}")
    print("要点:未知类错误必须显式暴露给人工,不能默认当可重试处理")
