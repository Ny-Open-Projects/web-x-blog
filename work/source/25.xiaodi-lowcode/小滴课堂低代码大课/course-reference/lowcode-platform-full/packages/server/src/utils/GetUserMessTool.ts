/**
 * 自定义参数装饰器
 */
import type { ExecutionContext } from '@nestjs/common'; // 执行上下文的类型
import { createParamDecorator } from '@nestjs/common'; // 用于创建自定义参数装饰器
import type { IUser } from '@lowcode/share';
// 用户数据类型剔除 password
export type TCurrentUser = Omit<IUser, 'password'>;

// 获取用户 ip 的参数装饰器
const GetUserIp = createParamDecorator((data, ctx: ExecutionContext) => {
  // 获取当前 HTTP 的请求对象
  const request = ctx.switchToHttp().getRequest();

  // 拿到用户的 ip 地址，使用正则表达式匹配 IPv4 地址，转成字符串形式
  return request.ip.match(/\d+\.\d+\.\d+\.\d+/)?.join('.');
});

// 获取用户设备的参数装饰器
const GetUserAgent = createParamDecorator((data, ctx: ExecutionContext) => {
  // 获取当前 HTTP 的请求对象
  const request = ctx.switchToHttp().getRequest();

  // 获取用户的设备信息
  return request.headers['user-agent'];
});

// 获取用户所有信息参数装饰器
const getUserMess = createParamDecorator((data, ctx: ExecutionContext) => {
  // 获取当前 HTTP 的请求对象
  const request = ctx.switchToHttp().getRequest();

  // 获取用户的所以信息
  return request.user;
});

export { GetUserIp, GetUserAgent, getUserMess };
