"""异常对象的属性携带:args、自定义属性与结构化取数。"""


class ApiError(Exception):
    def __init__(self, message, status=0, *, request_id=""):
        super().__init__(message)       # args 只放消息,str(e) 干净
        self.status = status
        self.request_id = request_id


def call_api(status, request_id):
    if status >= 500:
        raise ApiError("服务端错误", status=status, request_id=request_id)
    if status >= 400:
        raise ApiError("请求被拒绝", status=status, request_id=request_id)
    return "ok"


if __name__ == "__main__":
    try:
        call_api(503, "req-42")
    except ApiError as e:
        print("args 元组:", e.args)
        print("str(e):", str(e))
        print("结构化字段:", e.status, e.request_id)

    try:
        call_api(403, "req-7")
    except ApiError as e:
        print("按状态码路由:", "稍后重试" if e.status >= 500 else "检查权限")

    e = ApiError("仅构造")
    e.hint = "查看网关日志"             # 异常实例也是普通对象,可事后附加
    print("事后附加属性:", e.hint)
