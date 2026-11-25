---
title: [OPS-108] nginx + keepalived 高可用的原理是什么？怎么配置主备切换？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-108：nginx + keepalived 高可用的原理是什么？怎么配置主备切换？
**答**：
- 原理：两台 nginx 通过 VRRP 协议共享一个虚拟 IP（VIP），MASTER 持有 VIP 并承载流量，心跳丢失时 BACKUP 抢占 VIP，域名只需解析到 VIP。
- health check 脚本检测 nginx 进程与本地端口，失败时给节点降权（weight 负值）或直接杀掉本机 keepalived 让出 VIP，避免"进程在但服务死"的脑裂式假活。
- virtual_router_id 同一广播域内唯一；priority 主高备低；advert_int 1s 决定故障发现速度。
- 两台都配真实服务，备机平时可承载低优先级流量；切换是秒级但连接会断，客户端需重试能力。
- 云上环境通常用 SLB/云负载均衡替代自建 keepalived，自建方案多见于 IDC 与混合云。

```bash
# 主节点 /etc/keepalived/keepalived.conf：VRRP 抢占 VIP
vrrp_script check_nginx {
    script "/usr/local/bin/check_nginx.sh"   # 检测 nginx 进程与 80/443 端口
    interval 2                               # 每 2s 探测一次
    weight -30                               # 失败优先级 -30，触发 VIP 迁移到备机
    fall 2                                   # 连续 2 次失败判定为故障
    rise 2
}

vrrp_instance VI_WEB {
    state MASTER                             # 备机为 BACKUP
    interface eth0
    virtual_router_id 51                     # 主备必须一致，广播域内唯一
    priority 100                             # 备机设 90，主高备低
    advert_int 1                             # 心跳间隔 1s
    authentication {
        auth_type PASS
        auth_pass S3cretVRRP
    }
    virtual_ipaddress {
        10.0.0.100/24                        # 业务域名 A 记录指向该 VIP
    }
    track_script {
        check_nginx
    }
}

# /usr/local/bin/check_nginx.sh：服务假活时主动让出 VIP
# systemctl is-active nginx >/dev/null || { killall -TERM keepalived; exit 1; }
# ss -lnt | grep -q ':443 '            || exit 1
```
