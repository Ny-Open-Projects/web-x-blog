---
title: [OPS-107] 怎么用 nginx 实现蓝绿切换与按权重金丝雀分流？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-107：怎么用 nginx 实现蓝绿切换与按权重金丝雀分流？
**答**：
- 蓝绿：新旧两套目录各起一个 upstream（blue/green），切换入口指向一个"可变 upstream"，sed 改一行配置 + nginx -s reload（秒级、可反向）。
- 金丝雀：split_clients 按 uid/UA 哈希稳定分桶，固定小比例流量进新版本；同一用户始终命中同一桶，灰度期间体验一致。
- 更细粒度灰度用 cookie/header map（内白名单定向放量），与权重灰度叠加。
- 切换必须配合日志标记（X-Gray-Bucket）与看板归因，否则分不清错误来自哪个版本（OPS-187）。
- reload 前必跑 nginx -t；灰度目录切换脚本纳入发布平台，不裸敲命令。

```nginx
# 双 upstream 切换：蓝绿用配置切换，金丝雀用 split_clients 按权重分流
upstream web_blue  { server 127.0.0.1:8001; }   # 稳定版本
upstream web_green { server 127.0.0.1:8002; }   # 新版本

# 按客户端特征哈希稳定分流 5% 到 green（同一用户始终命中同一版本）
split_clients "${remote_addr}${http_user_agent}" $gray_bucket {
    5%      web_green;
    *       web_blue;
}

server {
    listen 443 ssl http2;

    location / {
        # 灰度期按权重分流；验证通过后执行蓝绿整体切换：
        #   sed -i 's/^upstream web_active.*/upstream web_active { server 127.0.0.1:8002; }/' conf.d/active.conf
        #   nginx -t && nginx -s reload
        proxy_pass http://$gray_bucket;
        proxy_set_header X-Gray-Bucket $gray_bucket;   # 日志归因用，看板按桶分组
    }
}
```
