"""异常树粒度:三层结构、演化安全性与 handler 匹配。"""


class AppError(Exception):
    """根:所有业务异常的祖先,携带机器可读 code。"""
    code = "APP_ERROR"


class NotFound(AppError):
    code = "NOT_FOUND"


class UserNotFound(NotFound):
    code = "USER_NOT_FOUND"


class Transient(AppError):
    """中层的另一种维度:可重试。"""
    code = "TRANSIENT"


class RateLimited(Transient):
    code = "RATE_LIMITED"


def handle_user_missing(err):
    return f"按 NotFound 处理: {err.code}"


if __name__ == "__main__":
    err = UserNotFound("user 42")
    print(isinstance(err, NotFound), isinstance(err, AppError))
    print(handle_user_missing(err))

    # 演化:后来插入的中间类不破坏老 handler
    try:
        raise UserNotFound("still fine")
    except AppError as exc:                       # 老代码只认识 AppError
        print("老 handler 仍然接住:", exc.code)

    # 重试维度独立于存在维度,同一个异常可双重归类吗
    print("RateLimited 是 Transient:", issubclass(RateLimited, Transient))
    print("RateLimited 不是 NotFound:", not issubclass(RateLimited, NotFound))
