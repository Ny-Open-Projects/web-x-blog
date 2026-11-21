"""带错误码的异常体系:分层、查表与退出码映射。"""
import enum
import sys


class Err(enum.IntEnum):
    OK = 0
    BAD_INPUT = 10
    NOT_FOUND = 20
    UNAUTHORIZED = 30


class AppError(Exception):
    code = Err.OK
    default = "未分类错误"

    def __init__(self, message=None, *, detail=None):
        super().__init__(message or self.default)
        self.detail = detail


class BadInput(AppError):
    code = Err.BAD_INPUT
    default = "入参不合法"


class NotFound(AppError):
    code = Err.NOT_FOUND
    default = "资源不存在"


EXIT_TABLE = {
    Err.BAD_INPUT: 2,        # 用法错误
    Err.NOT_FOUND: 3,
    Err.UNAUTHORIZED: 4,
}


def exit_code(exc):
    return EXIT_TABLE.get(exc.code, 1)


def run_main(fn):
    """入口统一捕获:打印 [错误码] 消息,返回建议退出码。"""
    try:
        return fn() or int(Err.OK)
    except AppError as e:
        print("[" + str(int(e.code)) + "] " + str(e), file=sys.stderr)
        return exit_code(e)


def fake_main():
    raise NotFound("订单不存在", detail="order_id=404")


if __name__ == "__main__":
    rc = run_main(fake_main)
    print("建议退出码:", rc)
    print("按码捕获仍是同一体系:", isinstance(NotFound("x"), AppError))
