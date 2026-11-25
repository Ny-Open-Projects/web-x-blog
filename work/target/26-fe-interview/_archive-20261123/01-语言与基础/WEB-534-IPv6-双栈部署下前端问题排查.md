---
title: [WEB-534] IPv6 双栈部署下前端问题排查
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-534：IPv6 双栈部署下前端问题排查

**答**：
- 双栈：域名同时返回 A（IPv4）与 AAAA（IPv6）记录；终端优先 v6，v6 链路有问题时出现「部分用户超时」
- 典型症状：AAAA 记录已发布但 v6 链路（运营商/CDN 节点）不通，用户等待 v6 超时才回退 v4（Happy Eyeballs 能缓解但不是万能）
- 排查：`dig AAAA` 确认记录 → 用 v6 网络实测（test-ipv6.com 或拨测平台 v6 节点）→ 检查 CDN/SLB 的 v6 配置与证书是否同步部署
- 前端可感知的坑：某些上报/第三方域名只有 A 记录，页面在纯 v6 网络（部分新小区/移动网络）下这些请求失败——排查「特定网络环境接口全挂」要想到这层
- 治理：上线前对全部第三方域名做 v6 连通性核查，关键域名补 AAAA 或换 v6 友好的供应商

```bash
dig +short AAAA example.com          # 有返回 = 已发布 v6
curl -6 -sI https://example.com -m 5 # v6 链路实测
```
