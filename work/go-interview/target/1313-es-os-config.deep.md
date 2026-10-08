# 1313 ES 部署 OS 配置全景（深挖）

> 分类：搜索 / Elasticsearch | 难度：L4 | 题型：体系题 | 频率：中 | 关键词：**九项OS配置**/**虚拟内存**/**交换**/**THP**/**JVM堆**/**网络**
> 原文锚点：第 1~57 段「部署 ES 的 OS 配置」全景

## 思路与架构
本卡把 ES 部署 OS 配置按「**内存类 → 交换类 → 网络/安全类 → JVM 类**」串起 `1313-os-virtual-fd`（max_map_count/limits.noile）、`1313-swap-thp`（swapoff/swappiness/THP）、`1313-network-jvm-security`（tcp_keepalive/somaxconn/安全/JVM 堆）三张主卡，并显式划边界。

- **内存类**：vm.max_map_count（mmapfs 映射数）、limits.conf nofile（es 用户 65536）。
- **交换类**：swapoff -a / 注释 fstab；vm.swappiness=1（现代内核最少交换）；THP 写 never。
- **网络/安全类**：tcp_keepalive_time 调小、somaxconn 调大、防火墙+认证+TLS。
- **JVM 类**：Xms=Xmx、50% 总内存、≤31G 压缩指针、留 OS 缓存。

## 方案取舍
| 配置 | 临时 | 永久 | 作用 |
| --- | --- | --- | --- |
| max_map_count | sysctl -w | /etc/sysctl.conf | ES 能起 |
| nofile | ulimit -n | /etc/security/limits.conf | 不报 fd 耗尽 |
| swap | swapoff -a | 注释 /etc/fstab | 避免换出延迟 |
| swappiness | sysctl -w | sysctl.conf | 减换出 |
| THP | 写 never | rc.local | 去分配毛刺 |
| 堆 | jvm.options | jvm.options | GC/压缩指针 |

- 选型主线：内存两项是「起得来」前提；交换/THP 是「稳且快」；网络/安全是「抗并发+防入侵」；JVM 堆是「性能天花板」。
- 与「压缩指针」的呼应：堆 ≤31G 才开启，越过 32G 指针膨胀、堆实际更慢——这是 ES 最易踩的反直觉坑。

## 答题技巧
- **九项清单必背**：虚拟内存/文件描述符/交换/交换偏好/THP/keepalive/somaxconn/安全/JVM 堆。
- **第一坑**：max_map_count 不够 ES 直接起不来；limits 必须按 es 运行用户。
- **反直觉点**：堆不是越大越好，≤31G 保压缩指针；留 OS 内存做文件系统缓存。
- **显式边界**：「本地 docker 起 ES + max_map_count 必调」见 `131-docker-setup`（本卡只把该项并入九项清单、不重画 docker 起法）；Linux 内存/swap 机制底层见 `811-memory-foundations`/`811-tlb-pagefault-swap`；本卡只讲部署配置清单。
