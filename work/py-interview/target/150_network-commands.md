# 150. 网络命令：查端口 / 远程 / 抓包（ss / netstat / ssh / scp / tcpdump）

> 分类：操作系统/Linux | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**ss** / **netstat** / **端口排查** / **scp** / **tcpdump**
> 原文锚点：第 60~67 段「ifconfig 看网卡/IP；lsof/netstat 查端口；ssh 远程登录、scp 远程拷贝；tcpdump 抓 TCP 包」

## 一句话总述
查端口占用用 **`ss -tlnp`**（新）或 **`netstat -tlnp`**（旧）；远程登录 **`ssh`**、远程拷贝 **`scp`**；抓包 **`tcpdump`**（或 Wireshark 图形化）——"Web 应用占用了哪个端口"是高频实战题。

## 面试官视角
- **考察意图**：考你能否**定位端口冲突/连接问题**，这是线上排障硬技能。
- **P5** 能写出 `ss -tlnp` 或 `netstat -tlnp` 查监听端口 / **P6** 能讲清 `ss` 比 `netstat` **更快**（直接读内核）、`ss -tlnp` 各字母含义（t=TCP/l=监听/n=数字/p=进程）/ **P7** 能指出查"某进程占用的端口"与"某端口被谁占用"的正反两种用法，以及 `tcpdump` 抓特定端口过滤表达式 `[经验]`。
- **红旗**：① 端口冲突只会重启不知道谁占着；② 分不清 `ss -tlnp`（监听）与 `ss -tnp`（已建立）；③ `scp` 用法写反（源/目标顺序）。
- **惊艳点**：`ss -tlnp | grep :8080` 直接看 8080 被哪个进程监听；`tcpdump -i any port 8080` 抓该端口流量。验证：两个表达式分别定位端口与流量 `[实测]`。

## 主问答
**Q：Web 应用起了但访问不通，怎么查它占用的端口？**
**A：**
1. **结论**：用 **`ss -tlnp`**（或 `netstat -tlnp`）列出所有监听端口，按端口号定位进程。
2. **机制**：`ss -tlnp` 的 `t`=TCP、`l`=监听、`n`=数字显示、`p`=显示进程；`grep :8080` 即可看 8080 被谁占用。
3. **边界**：`ss` 直接读内核、比 `netstat` 快；远程拷贝用 `scp 源 目标`（本地→远程 `scp f user@host:/path`）；抓包用 `tcpdump -i any port 8080`。
**加分层**：`ssh user@host` 登录、`scp` 传文件、`tcpdump`/`Wireshark` 抓包，构成"连通性→端口→流量"的排查链。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 查端口命令 | 基础 | ss/netstat | 换题 → 不及格 |
| L2 | ss vs netstat | 辨析 | 速度/内核 | 判 P5 |
| L3 | tlnp 含义 | 细节 | 四字母 | 判 P6 |
| L4 | 双向查法 | 深入 | 端口↔进程 | 判 P6+ |
| L5 | tcpdump 过滤 | 实战 | port 表达式 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 各 Linux | ss 取代 netstat | 优先 ss |
| macOS | netstat 参数不同 | 用 lsof -i |
| 容器 | ss 需装 | iproute2 包 |

## 关键代码
```bash
ss -tlnp | grep :8080     # 查 8080 被谁监听
netstat -tlnp | grep :80  # 旧式等价
ssh user@host             # 远程登录
scp f user@host:/tmp/     # 本地→远程拷贝
tcpdump -i any port 8080  # 抓 8080 流量
```

```python
import socket
print(socket.gethostbyname("localhost"))  # DNS 解析（网络基础能力）
```

## ⚠️ 原文纠错
原文"ifconfig 看网卡/IP；lsof/netstat 查端口；ssh 远程登录、scp 远程拷贝；tcpdump 抓 TCP 包；查 Web 应用占用端口可用 lsof 或 netstat"——准确（机翻"RSF/nextstead"=**lsof / netstat**，"IOSapp"=**lsof**，"SCP"=**scp**，"TCPdump"=**tcpdump**，"yshock"=**Wireshark**，"ifconfig" 同形）。原文未强调"ss 比 netstat 更快、tlnp 各字母含义"，已在机制与 P6 补充 `[经验]`。无事实错误，仅术语音译需还原。

## 总结与追问预判
- 查端口 ss -tlnp；scp 传文件；tcpdump 抓包。
- 下一题：**free/用户组/crontab**（151）、**进程命令**（149）。
