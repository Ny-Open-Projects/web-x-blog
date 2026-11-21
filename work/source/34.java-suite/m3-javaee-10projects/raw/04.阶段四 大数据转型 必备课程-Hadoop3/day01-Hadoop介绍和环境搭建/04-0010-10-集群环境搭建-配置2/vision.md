# 画面线理解：10-集群环境搭建-配置2

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\10-集群环境搭建-配置2【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 02:28, 02:39, 02:53, 02:58, 03:08, 03:13, 03:38, 04:30, 05:10, 05:27, 05:44, 06:19, 06:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:22:30

1) 这一组画面整体在讲什么（一句话）：
在三台 Linux 服务器上安装并配置 NTP 服务以实现时间同步。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“5.4 三台机器时钟同步”，内容解释了分布式系统需要时间同步的原因，并列出操作步骤：安装、启动定时任务。下方提示“随后在输入界面输入”并显示命令：*/1 * * * /usr/sbin/ntpdate ntp4.aliyun.com;。
画面 2: 展示 PPT 页面，对比两种时钟同步方案：第一种是所有主机和网络时间保持一致（通过阿里云时钟同步服务器）；第二种是所有主机和某一台主机保持时钟同步。
画面 3: 展示 SecureCRT 连接终端，提示符为 [root@node01 ~]#，准备执行操作。
画面 4: 展示 SecureCRT 终端，显示 yum 安装 ntp 和 ntpdate 包的进度，已解决依赖关系。
画面 5: 展示 SecureCRT 终端，用户在 node02 上尝试执行 crontab -l 命令，但提示“crontab: usage error: unrecognized option --'-'”，并尝试 crontab -e，但提示“no crontab for root”。
画面 6: 展示 SecureCRT 终端，用户在 node02 上执行 crontab -r 删除现有定时任务，然后执行 yum install -y ntp 安装 NTP 包。
画面 7: 展示课程 PPT 页面，内容与画面 1 相同，但命令行中“crontab -e”被高亮。
画面 8: 展示课程 PPT 页面，内容与画面 1 相同，但命令行中“crontab -e”被高亮。
画面 9: 展示课程 PPT 页面，内容与画面 1 相同，但命令行中“*/1 * * * /usr/sbin/ntpdate ntp4.aliyun.com;”被高亮。
画面 10: 展示 SecureCRT 终端，用户在 node02 上输入命令：*/1 * * * /usr/sbin/ntpdate ntp4.aliyun.com;。
画面 11: 展示 SecureCRT 终端，用户在 node02 上执行命令后，终端返回提示符 [root@node02 ~]#。
画面 12: 展示 SecureCRT 终端，用户在 node02 上执行命令后，终端返回提示符 [root@node02 ~]#。
画面 13: 展示 SecureCRT 终端，用户在 node03 上执行命令：crontab -l，然后输入：*/1 * * * /usr/sbin/ntpdate ntp4.aliyun.com;。
画面 14: 展示课程 PPT 页面，内容与画面 1 相同，但命令行中“*/1 * * * /usr/sbin/ntpdate ntp4.aliyun.com;”被高亮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
## 安装
yum install -y ntp
## 启动定时任务
crontab -e
```
画面 10:
```
*/1 * * * /usr/sbin/ntpdate ntp4.aliyun.com;
```
画面 13:
```
crontab -l
*/1 * * * /usr/sbin/ntpdate ntp4.aliyun.com;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
- 标题：第一种：所有主机和网络时间保持一致；第二种：所有主机和某一台主机保持时钟同步。
- 架构图：
  - 第一种：时钟同步服务器（阿里云）指向 A、B、C 三个节点。
  - 第二种：A、B、C 三个节点分别指向一个中心节点（未明确标出，但由连线表示）。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
