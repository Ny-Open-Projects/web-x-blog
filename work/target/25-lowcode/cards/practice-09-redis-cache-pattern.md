---
title: Redis 工程化封装：动态模块与 getCachedData 模式
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, Redis, NestJS]
---

## Redis 工程化封装：动态模块与 getCachedData 模式

**模块封装**（NestJS 动态模块标准写法）：

```ts
@Module({})
export class RedisModule {
  static forRoot(options): DynamicModule {
    return { global: true, module: RedisModule, providers: [...], exports: [...] };
  }
}
```

`@Global` + 静态 `forRoot` 返回 DynamicModule，一处注册处处可注入；封装 `set`（支持 EX 过期）/`del`/`get`/`exists` 四方法。坑：全局模块要走 `imports`，塞进子模块 `providers` 注入不到。

**getCachedData 通用缓存模式**：`getCachedData(cacheKey, callback, {ttl, force})`——命中直接返回，未命中执行 callback 查库并 set 回填，force 置空回写（并非显式 del）；课程示例 TTL 600 秒；缓存版本在最终仓库处于注释状态、未合入主线。业务查询作为回调传入，缓存逻辑与业务解耦。

**Redis 在本项目的五类用途**：①验证码短时存储（60 秒 EX）；②图形验证码防刷比对；③微信扫码状态 isScan；④问卷提交防重（MD5(ip+ua) 匿名标识）；⑤接口缓存 QPS 优化（getCachedData 调用在最终仓库以注释形式保留、未合入主线）。

**key 设计规范**：冒号分层（`register:code:phone`、`wechat:ticket:${ticket}`）、场景字段隔离（register/login）、对象值必须 JSON.stringify。

出处「课程25 · 11-2、30-6；scan3」
