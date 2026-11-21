import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';

/**
 * 租户隔离守卫（商业化 rbac 第一层）。
 *
 * 解析租户身份并在请求上挂载 `tenantId`，供 Service 做数据隔离与计量。
 * 身份来源优先级：网关 / 反向代理注入的 `x-tenant-id` 头（推荐，由平台统一鉴权后注入）。
 * 生产环境应在此校验 API Key / JWT 并映射为可信 tenantId；本实现以注入值为准，
 * 便于本地联调，已在 README 注明硬隔离升级路线（见 06 §商业化）。
 */
@Injectable()
export class TenantGuard implements CanActivate {
  canActivate(ctx: ExecutionContext): boolean {
    const req = ctx.switchToHttp().getRequest();
    const h = (req.headers['x-tenant-id'] as string | undefined)?.toString().trim();
    if (h) req.tenantId = h;
    return true;
  }
}
