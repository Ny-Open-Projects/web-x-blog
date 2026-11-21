import { Injectable, ExecutionContext } from '@nestjs/common';
import { Reflector } from '@nestjs/core';
import { AuthGuard } from '@nestjs/passport';
import { IS_PUBLIC_KEY } from '../decorators/public.decorator';

/**
 * 全局 JWT 守卫:默认拦截一切请求,被 @Public() 标记的接口放行。
 * 相比在每个接口上手挂 @UseGuards,全局守卫杜绝"新接口忘加守卫"的安全隐患。
 */
@Injectable()
export class JwtAuthGuard extends AuthGuard('jwt') {
  constructor(private readonly reflector: Reflector) {
    super();
  }

  canActivate(context: ExecutionContext) {
    // 方法级与控制器级元数据合并判断(@Public 加在 Controller 上则全类豁免)
    const isPublic = this.reflector.getAllAndOverride<boolean>(IS_PUBLIC_KEY, [
      context.getHandler(),
      context.getClass(),
    ]);
    if (isPublic) return true;
    return super.canActivate(context);
  }
}
