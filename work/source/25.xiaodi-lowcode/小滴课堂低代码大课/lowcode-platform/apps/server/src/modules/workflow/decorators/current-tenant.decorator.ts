import { createParamDecorator, ExecutionContext } from '@nestjs/common';

/** 读取 TenantGuard 挂载的当前租户 ID（无则 null）。 */
export const CurrentTenant = createParamDecorator(
  (_data: unknown, ctx: ExecutionContext) => ctx.switchToHttp().getRequest().tenantId ?? null,
);
