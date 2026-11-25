---
title: [OPS-102] open_file_cache 为什么能加速静态资源？参数怎么定？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-102：open_file_cache 为什么能加速静态资源？参数怎么定？
**答**：
- 每次静态请求默认都要 open/stat/close 文件，热点文件元数据缓存在内存后可省掉这组系统调用，高 QPS 下收益显著。
- max 控制缓存 fd 总量（按热点文件数估，1 万足够大多数站点）；inactive 控制无访问多久移出。
- open_file_cache_valid 是元数据有效期：CDN 回源与版本化文件名场景可放心调大；文件会被原地覆盖的场景要调小。
- min_uses 防缓存被长尾冷文件挤占；open_file_cache_errors 连"文件不存在"也缓存，可缓解恶意路径扫描。
- 注意与发布方式配合：若用 symlink 切版本（OPS-140），软链目标变化后 stat 缓存可能短暂陈旧，切换后 reload 或控制 valid 时长。

```nginx
# 静态资源元数据缓存：fd/stat 结果直接命中内存
http {
    open_file_cache max=10000 inactive=60s;   # 最多缓存 1 万个 fd，60s 无访问移出
    open_file_cache_valid 120s;               # 缓存元数据的有效检查间隔
    open_file_cache_min_uses 2;               # 60s 内命中 2 次以上才保留在缓存
    open_file_cache_errors on;                # 缓存"不存在"结果，扛恶意路径扫描

    server {
        location /static/ {
            alias /data/releases/current/static/;
            expires 30d;
            add_header Cache-Control "public, immutable";
            # 版本化 hash 文件名不可变，stat 缓存失效风险极低，可放心开启
        }
    }
}
```
