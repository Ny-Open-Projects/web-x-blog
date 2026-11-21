// AbnormalFilter.ts
import type { ArgumentsHost, ExceptionFilter } from '@nestjs/common';
import { Catch, HttpException } from '@nestjs/common';

@Catch(HttpException)
export class AbnormalFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    // 获取请求的上下文
    const ctx = host.switchToHttp();
    // 获取上下文的 response 对象
    const response = ctx.getResponse();
    // 获取异常的状态码
    const status = exception.getStatus();
    // 异常的消息,兼容 DTO 验证提示
    const message = (exception.getResponse() as any).message;
    response.status(status).json({
      code: -1,
      data: null,
      msg: message,
    });
  }
}
