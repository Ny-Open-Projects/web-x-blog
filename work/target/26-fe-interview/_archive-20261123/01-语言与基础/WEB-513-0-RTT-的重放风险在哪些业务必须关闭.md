---
title: [WEB-513] 0-RTT 的重放风险在哪些业务必须关闭
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTPS]
type: 面试题
---

## WEB-513：0-RTT 的重放风险在哪些业务必须关闭

**答**：
- 0-RTT 数据没有防重放保护：攻击者录下首包可原样重发，服务端无法区分「真用户」与「重放包」
- 必须关闭的业务：下单/支付入口、验证码获取、短信发送、秒杀接口——重放一次就是一笔业务损失
- 可以保留的业务：静态资源、配置拉取、广告请求等纯幂等读操作
- 实施方式：网关按路径开关 early data（如 Nginx 的 `ssl_early_data off` / CDN 控制台按路径规则），或在服务端用 425 Too Early 拒绝
- 面试话术：能说出「early data 只对幂等请求开放」这句原则+一个反例业务即可，不需要背协议细节

```nginx
server {
    location /api/order/ {
        ssl_early_data off;   # 写操作路径禁 0-RTT
    }
    location /static/ {
        ssl_early_data on;    # 幂等资源可开
    }
}
```
