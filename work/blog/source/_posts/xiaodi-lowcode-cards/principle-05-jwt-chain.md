---
title: JWT 鉴权链路：从签发到全局守卫
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 原理, JWT, 鉴权]
---

## JWT 鉴权链路：从签发到全局守卫

链路五环节：
1. **签发**：登录/注册成功后 `@nestjs/jwt` 签发 token，payload 只放 id 不放密码，有效期 7 天——注册即自动登录，免二次登录。
2. **携带**：前端 axios 请求拦截器注入请求头 `Authorization: Bearer <token>`（注意 Bearer 后有空格）。
3. **解析**：passport-jwt 的 `JwtStrategy`，`jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken()` + `secretOrKey`。
4. **校验**：`validate` 依次验证 token 有效→未过期→用户存在（二次查库），并把用户挂上 request；手写 verify 需 try/catch 兜非法 token，解密结果含 iat/exp 判过期。
5. **拦截**：`JwtAuthGuard` 以 `APP_GUARD` 全局注册——**默认拦截一切接口，@Public() 显式豁免**，从架构上杜绝"新接口忘加守卫"。

**本项目实例**：accountId 不由前端传参，一律从 token 解出（用 Omit 类型在编译期排除）；返回用户数据经 `Omit<IUser,'password'>` 脱敏。手写 verify 版与 Guard 版是同一原理的两个实现阶段。

出处「课程25 · 8-4、11-7、14-3；scan3」
