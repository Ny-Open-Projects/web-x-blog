---
title: [WEB-460] 请求重放与 diff 排查怎么做
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-460：请求重放与 diff 排查怎么做

**答**：
- 适用场景：「我这边正常他那边报错」类问题——环境差异藏在请求里，把两边请求并排 diff 一次就水落石出
- 采集方式：Charles/DevTools 导出 HAR（包含 header、cookie、时序），失败用户让 TA 导出或前端 SDK 自动采关键请求
- diff 关注点排序：URL 与参数 → header（UA/Referer/token/Cookie 覆盖范围）→ 时序（先后依赖请求的顺序）→ 灰度路由头
- 重放验证：在本地 curl/Postman 按用户原始请求重放，逐步增删 header 做二分，定位是哪个字段导致失败
- 工程沉淀：把「自动采集失败请求 + 与对照组 diff」做成平台能力，排查时间从小时级降到分钟级

```bash
# 从 HAR 提取请求做重放二分
curl -s 'https://api.example.com/x' \
  -H 'Cookie: sid=用户的' -H 'X-Gray: b' --data @body.json | jq '.code'
# 依次去掉 X-Gray / 换 UA / 清 Cookie，定位差异字段
```
