"""租户头注入: 入站清洗与可信来源注入(纯标准库, 附 fastapi 降级)。"""
try:
    from fastapi import FastAPI
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    print("[降级] 未安装 fastapi, 以下用纯函数演示同一头处理语义")


def resolve_tenant(inbound_headers, token_claims):
    """从已验证的 token claims 解析租户; 客户端自带的 X-Tenant-ID 一律剥掉。

    返回 (tenant_id, clean_headers); token 无租户声明的多租户部署必须拒绝。
    """
    headers = dict(inbound_headers)
    stripped = headers.pop("x-tenant-id", None)     # 不可信来源, 直接丢弃
    tenant = token_claims.get("tenant_id")
    if tenant is None:
        return None, headers                        # 无租户上下文 -> 拒绝
    headers["x-tenant-id"] = tenant                 # 注入服务端可信任值
    return tenant, headers


def forward_downstream(headers):
    """向下游服务转发时带上注入后的租户头, 下游不再自行解析鉴权材料。"""
    return {k: v for k, v in headers.items() if k.startswith("x-")}


# 场景一: 客户端伪造租户头 + token 属于 tenant-a -> 以 token 为准
inbound = {"authorization": "Bearer xx", "x-tenant-id": "tenant-evil"}
tenant, clean = resolve_tenant(inbound, {"tenant_id": "tenant-a"})
print("伪造入站头 -> 剥掉的是:", "tenant-evil", "实际租户:", tenant)
assert tenant == "tenant-a" and "x-tenant-id" in clean
print("下游收到的头:", forward_downstream(clean))

# 场景二: token 无租户声明 -> 多租户部署必须拒绝, 不能猜默认
tenant, _ = resolve_tenant({"authorization": "Bearer y"}, {"uid": "u1"})
print("无租户声明 ->", tenant, "(返回 401 缺租户上下文)")
assert tenant is None

if HAS_FASTAPI:
    print("fastapi 可用: 等价于在中间件里改 request.headers 并向下游转发")
print("要点: 租户上下文只能来自已验证凭证, 入站租户头是攻击面, 剥掉再注入是唯一安全顺序")
