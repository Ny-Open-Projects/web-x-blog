---
title: "题 5.8.3：Buffer Pool 的调优与命中率监控？"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 5.8.3：Buffer Pool 的调优与命中率监控？

**【参考回答（可背）】** 原理一句话：InnoDB 用 Buffer Pool 缓存页（默认 LRU 变种：young/old 子链 5:3，老区停留 1s 才晋升——**防全表扫污染**）。调优：① 大小：专机给物理内存 60%~70%（innodb_buffer_pool_size），容器按 Min(堆外预算, 60%)；② 命中率：`show global status like 'innodb_buffer_pool_read%'`，(1 - read_requests/物理读) 应 >99%，突然下跌=大扫描/冷启动/池太小；③ change buffer：对写多读少的二级索引页有效，随机写场景可观察。预警信号：命中率下降 + 物理读 IOPS 上升 = 内存被"烫穿"，先查新增大扫描 SQL。
**【追问链】** ① 为什么双 LRU 要 1 秒滞留？（一次性全表扫的页只进 old 区不污染 young 热点——预热与防污染的关键设计）② 预读机制怎么配合？（线性读预读连续页进 old 区，随机读预读关闭）。
**【P10 加分项】** 类比升华："Buffer Pool 命中率下降的排查与 Redis 缓存命中率下降同构——都是'回源流量异常'，第一反应应该是'谁新增了全表扫描/谁把热点 key 冲掉了'，而不是先调参。存储层缓存思想是通的。"
