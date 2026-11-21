import { SetMetadata } from '@nestjs/common';

// 标记公开接口的元数据键
export const IS_PUBLIC_KEY = 'isPublic';

/**
 * @Public() 装饰器:标记无需登录的接口。
 * 全局 JwtAuthGuard 默认拦截一切请求,仅被 @Public 标记的方法/控制器放行。
 * 用法:
 *   @Public()                  // 方法级豁免
 *   @Get('release')
 *   getRelease(...) {}
 *
 *   @Public() @Controller()    // 控制器级豁免(整个模块公开)
 */
export const Public = () => SetMetadata(IS_PUBLIC_KEY, true);
