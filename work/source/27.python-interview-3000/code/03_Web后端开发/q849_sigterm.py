import signal

def shutdown_plan(sig: int) -> str:
    if sig == signal.SIGTERM:
        return "停止 accept, 排空在途请求, 关闭 lifespan 资源"
    if sig == signal.SIGINT:
        return "快速退出, 中断在途请求"
    if sig == signal.SIGHUP:
        return "gunicorn 平滑重载 worker"
    return "未知信号"

print("SIGTERM:", shutdown_plan(signal.SIGTERM))
print("SIGINT:", shutdown_plan(signal.SIGINT))
