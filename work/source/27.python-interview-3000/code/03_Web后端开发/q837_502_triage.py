
def triage(upstream_alive: bool, app_log_error: bool, recently_deployed: bool) -> str:
    if not upstream_alive:
        return "进程死了: 查退出原因 OOM panic 配置错误"
    if app_log_error and recently_deployed:
        return "疑似新版本缺陷: 先回滚止血再定位"
    if app_log_error:
        return "应用报错: 按异常日志定位"
    return "检查网关到应用的网络与超时配置"

print(triage(False, False, False))
print(triage(True, True, True))
print(triage(True, False, False))
