
STRATEGIES = {
    "冷备": "另一地域仅存数据备份, 恢复小时级",
    "热备读多活": "两地部署, 写走主地域, 读就近",
    "单元化": "用户按分片绑定单元, 读写单元内闭环, 故障整体切流",
}

def failover_note() -> str:
    return "主地域故障: GSLB 切流 + 数据层提升, 依赖 RPO 与 RTO 评估"

for k, v in STRATEGIES.items():
    print(f"{k}: {v}")
print(failover_note())
