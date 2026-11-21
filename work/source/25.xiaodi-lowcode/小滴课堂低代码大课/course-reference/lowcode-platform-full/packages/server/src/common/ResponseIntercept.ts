// ResponseIntercept.ts
import type {
  ExecutionContext,
  NestInterceptor,
  CallHandler,
} from '@nestjs/common';
import type { Observable } from 'rxjs';
import { map } from 'rxjs';
import { Injectable } from '@nestjs/common';

/**
 * 拦截器 成功返回的统一响应格式
 */
@Injectable()
export class ResponseIntercept implements NestInterceptor {
  // 调用 next 处理器，执行里面 handel()，使用 pipe 操作符进行管道处理，map 操作符映射数据
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    return next.handle().pipe(
      map((data) => {
        if (data?.msg === '微信验证回调') return data.data;
        if (data?.msg !== undefined) {
          return {
            code: 0,
            msg: data.msg,
            data: data.data,
          };
        }
        return {
          code: 0,
          data,
        };
      }),
    );
  }
}
