
GATEWAY_DUTIES = {
    "路由与转发": "按 path 与 host 路由到服务, 剥离外部前缀",
    "认证卸载": "统一校验 JWT, 内网转发时注入可信身份头",
    "限流与配额": "按 key 与租户限制, 保护后端容量",
    "观测": "访问日志, trace 注入, 指标导出",
    "安全": "TLS 终止, WAF, IP 黑名单",
}
for duty, note in GATEWAY_DUTIES.items():
    print(f"{duty}: {note}")
