# 1847 TIME_WAIT 生产治理与端口耗尽攻防 深挖

> 覆盖源 18-47 全文：TIME_WAIT 堆积的生产画像（谁在堆、堆在哪、危害是什么）、治理手段的优先级与陷阱（tcp_tw_reuse 的出方向限制、tw_recycle 之死）、连接权归属设计、MSL=30s 的推演逻辑。主卡已给 2MSL 原理与实测，本附录做生产工程四层深挖。

## 思路与架构

```text
TIME_WAIT 治理决策树
├─ 先分清: 谁主动关? TIME_WAIT 归主动方
│   ├─ 客户端堆 -> 本地端口耗尽 (无法新建出向连接)
│   └─ 服务端堆 -> 文件描述符/内存表项压力
├─ 治本: 长连接 + 连接池 (握手省了, TIME_WAIT 也不产生)
├─ 次优: tcp_tw_reuse=1 + 时间戳
│   └─ 仅对「出方向主动连接」生效, 服务端 listen 侧无效
├─ 归属调整: 让对端先关 (服务端 Close 先行 -> TIME_WAIT 转移)
└─ 反面教材: tcp_tw_recycle 已因 NAT 冲突被内核移除, 别再用
```

## 方案取舍
- **危害的精确刻画：不是内存，是端口空间**。客户端侧每个 TIME_WAIT 占一个**四元组**（本地 IP:port + 远端 IP:port），对同一远端的出向连接理论上限只有约 64K 个端口；短连接打满后 `connect` 报 `EADDRNOTAVAIL`——这才是「TIME_WAIT 危害」的主体。服务端侧TIME_WAIT 占的是 fd 与表项，量大但一般先撞 fd 上限（可调）而非端口。**先量清楚堆在哪一侧，再选治理手段** [经验]。
- **tcp_tw_reuse 的边界要背准**：`net.ipv4.tcp_tw_reuse=1` 依赖 TCP 时间戳选项，允许**作为客户端发起出向连接时**复用超过 1 秒的 TIME_WAIT 端口——**只对主动 connect 方生效**，对服务端 accept 侧无意义。所以「服务端 TIME_WAIT 多」调这个参数无效，正确动作是把**关闭权交给客户端**（服务端不主动 Close）或上连接池。而 `tcp_tw_recycle` 因与 NAT 环境的时间戳乱序冲突导致大面积掉线，**内核 4.12 已移除**——生产配置里还看到它就是事故隐患 [经验]。
- **MSL=30s 是怎么推出来的**：Linux 认为 IP 报文 TTL 初始 64 跳，穿越 64 个路由器不会超过 30 秒——即 30 秒内报文要么送达、要么已被 TTL 机制丢弃。2MSL=60 秒因此是「旧报文必然死透 + FIN 重传最坏路径走完」的双重保守估计。**理解这个推算才能回答「能不能调小」**：能（重编译改 MSL），但违背 RFC 保守语义、在乱序/重传路径上冒险，生产没人这么干——正确方向是少产生 TIME_WAIT 而非缩短它 [经验]。
- **连接权归属是架构层解法**：HTTP 场景服务端主动关（如 Keep-Alive 超时）会让 **服务端**堆 TIME_WAIT；反向设计成 **客户端先关**（读到 EOF 后客户端 Close）则 TIME_WAIT 分散在成千上万个客户端——服务端只占少量。这就是「服务端堆 TIME_WAIT 时把关闭权下移」的原理。配合长连接池（复用连接不新建），TIME_WAIT 从源头消失——**每条连接的整个生命周期只关一次** [经验]。
- **实测方法论可复用**：用 300 个短连接压出恰好 300 条 TIME_WAIT（`netstat -an | awk '{print $6}' | sort | uniq -c`）——这种「精确计数验证协议语义」的实验模式可推广到其他 TCP 状态（SYN_SENT/CLOSE_WAIT 等）。顺带一提：**CLOSE_WAIT 堆积是另一码事**——它是「被动关闭方收到 FIN 后应用层没调 Close」，属于应用 bug（忘关连接/泄漏），与 TIME_WAIT 的协议行为要分开诊断 [实测]。

## 答题技巧
- 先答两重保险（ACK 丢失兜底 + 旧报文消亡），再报最坏情况账（1+1=2MSL），最后补 MSL/TTL 区别——三层递进 [源码]。
- 报实测数字立可信：300 短连接 → 300 TIME_WAIT，主动关闭方实锤 [实测]。
- 被问「生产 TIME_WAIT 爆了怎么办」→ 按决策树顺序答：分侧 → 长连接治本 → tw_reuse（出方向限制说清）→ 归属调整，并主动点名 tw_recycle 已移除 [经验]。
- 被问「CLOSE_WAIT 多呢」→ 立刻纠正这是应用层忘 Close 的泄漏 bug，与 TIME_WAIT 协议行为不同——一题双查显深度 [经验]。
- 主动边界到 `1844-rst-use-cases.deep`（RST 不产生 TIME_WAIT 的对照）、`1843-tcp-handshake-recap`（握手侧状态机）、`1849-http-vs-tcp-keepalive`（长连接原理），构成 TCP 连接生命周期专题 [边界]。

## 细节与核心 API

```bash
# TIME_WAIT：主动关闭方最后发 ACK 后进入，持续 2*MSL（Linux 默认 60s）
# 目的：① 确保最后 ACK 可达（丢则对端重传 FIN）② 让旧连接的迷途报文在网络中消亡
# 端口耗尽：高并发短连接（如调用下游）时，本地端口被大量 TIME_WAIT 占满 -> 无法建新连
ss -tan | grep TIME-WAIT | wc -l
# 治理（主动关闭方才产生，故客户端侧最有效）：
sysctl -w net.ipv4.tcp_tw_reuse=1      # 复用 TIME_WAIT 连接（客户端安全，RFC 允许）
sysctl -w net.ipv4.tcp_timestamps=1    # tw_reuse 依赖
# 不推荐 tcp_tw_recycle（已移除，且 NAT 下乱序）；更治本：用长连接（连接池）/SO_REUSEADDR
# 服务端侧：通常被动关闭，TIME_WAIT 在客户端；若服务端主动关（如反向代理上游）则同理治理
```
