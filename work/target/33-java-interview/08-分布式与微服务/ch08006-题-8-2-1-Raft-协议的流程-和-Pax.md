---
title: "题 8.2.1：Raft 协议的流程？和 Paxos、ZAB 什么关系？"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 8.2.1：Raft 协议的流程？和 Paxos、ZAB 什么关系？

**【参考回答（可背）】**
Raft 三角色：Leader / Follower / Candidate。三个子问题：
1. **选主**：心跳超时的 Follower 变 Candidate，term+1 拉票；多数派投票（每 term 一票，先到先得）成为 Leader；日志不全的候选人拿不到票（投票条件：候选日志不旧于自己）。
2. **日志复制**：客户端请求 → Leader 追加日志 → 并行发给 Follower → **多数派确认后提交** → 应用状态机 → 响应；Follower 事后异步 apply。
3. **安全性**：Leader 崩溃后新 Leader 必须包含所有已提交日志（选举限制保证）；term 小的日志被覆盖丢弃。
**Paxos**：正确但难懂难实现（Multi-Paxos 无标准实现）；**Raft 的贡献是可理解性**——把问题分解成选主/复制/安全三块，成了工业界事实标准（etcd、TiKV、Nacos CP 模式）。
**ZAB**：ZooKeeper 的协议，与 Raft 同族（Fast Leader Election + 崩溃恢复 + 消息广播），epoch 对应 term。

**【追问链】**
1. 为什么日志型系统都要"多数派"？→ 2N+1 容忍 N 故障；少数派数据可能过期，多数派一定包含最新已提交数据（法定人数 Quorum：W+R>N）。
2. 脑裂怎么防？→ 任一时刻只有一个多数派能选出 Leader，旧 Leader 的写无法凑齐多数派确认。

**【P10 加分项】**
指出"工程上的 Raft"还要处理：成员变更（joint consensus/单步变更）、日志压缩快照、读线性化（ReadIndex/Lease Read，etcd 的实现）——读过 etcd/raft 源码或实现过状态机复制的候选人极少，这是硬通货。

---
