---
title: [OPS-111] CDN 的缓存键由什么决定？query 参数和 Vary 头怎样影响命中率？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-111：CDN 的缓存键由什么决定？query 参数和 Vary 头怎样影响命中率？
**答**：
- 默认缓存键通常 = 域名 + 完整 URI（含 query）：utm 参数、分享随机串都会生成新缓存条目，命中率被稀释、回源翻倍。
- 治理方式：CDN 侧配置"忽略指定 query"或"白名单参数参与 key"（如分页 page、排序 sort 参与，追踪参数剔除）。
- Vary 响应头让缓存按对应请求头分桶：Vary: Accept-Encoding 合理；后端返回无意义的 Vary: User-Agent 会把缓存按 UA 碎片化，应让后端去掉或在边缘忽略。
- 接口缓存（短 TTL）要格外小心 query：既不能全参与（击穿）也不能全忽略（串数据），参数白名单是标准解法。
- 用 x-cache 状态头验证命中行为，配置改动后抽样比对命中率曲线。

```nginx
# 代理/源站层演示缓存键设计（CDN 控制台的"缓存键配置"与此同构）
proxy_cache_path /data/cache levels=1:2 keys_zone=cdn:100m max_size=50g inactive=7d;

server {
    location /static/ {
        proxy_cache cdn;
        # 静态资源：忽略全部 query（时间戳防刷新场景按需保留 $is_args$args）
        proxy_cache_key "$host$uri";
        proxy_cache_valid 200 301 7d;
        proxy_set_header Accept-Encoding "";   # 压缩策略在边缘统一，避免按编码分桶
        add_header X-Cache-Status $upstream_cache_status;
    }

    location /api/list {
        proxy_cache cdn;
        # 接口缓存：query 白名单参与 key，剔除 utm/随机串（CDN 侧同理配置"参数保留名单"）
        proxy_cache_key "$host$uri$is_args$args";
        proxy_cache_valid 200 60s;
        # 后端返回的无意义 Vary: User-Agent 会按 UA 碎片化缓存 → 边缘忽略
        proxy_ignore_headers Vary;
        add_header X-Cache-Status $upstream_cache_status;
    }
}
```
