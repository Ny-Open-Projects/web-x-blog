
REVIEW_RUBRIC = {
    "功能正确": "接口语义, 状态码, 幂等, 边界输入",
    "可观测": "request id, 结构化日志, 指标, SLO 告警",
    "容量": "压测基线, 连接池对账, 超时预算",
    "安全": "认证授权, 输入校验, 限流熔断, 密钥管理",
    "演进": "版本化, 兼容发布, 回滚方案",
}

def review(design: dict) -> list:
    return [f"{k}: {'已覆盖' if v else '缺失'}" for k, v in design.items()]

design = {k: True for k in REVIEW_RUBRIC}
design["容量"] = False
print(review(design))
