# 画面线理解：10.目录挂载查看IP与删除容器

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\10.目录挂载查看IP与删除容器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:30, 02:49, 04:15, 04:29, 04:31, 04:37, 04:40, 05:48, 06:08, 06:22, 07:03, 07:23, 08:30, 08:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:05:06

1) 这一组画面整体在讲如何使用 Docker 命令查看和管理容器，特别是通过 docker inspect 命令获取容器的网络配置和 IP 地址，并演示了如何停止和删除容器。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示终端界面，提示符为 [root@localhost myhtml]，但未显示任何命令或输出。
画面 2: 显示一个名为 "test" 的新文件，但未显示任何命令或输出。
画面 3: 显示 PPT 页面，标题为“3.2.6 查看容器IP地址”，并列出命令：docker inspect 容器名称（容器ID） 和 docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名称（容器ID）。
画面 4: 显示 docker inspect 命令的输出，包含容器的配置信息，如 Cpusetcpus、Memory、NetworkSettings 等。
画面 5: 显示 docker inspect 命令的输出，包含容器的详细信息，如 Status、Image、Name、NetworkMode 等。
画面 6: 显示 docker inspect 命令的输出，包含容器的详细信息，如 Status、Image、Name、NetworkMode 等。
画面 7: 显示 docker inspect 命令的输出，包含容器的详细信息，如 Config、NetworkSettings 等。
画面 8: 显示 docker inspect 命令的输出，包含容器的详细信息，如 NetworkSettings、IP Address 等。
画面 9: 显示 docker inspect 命令的输出，包含容器的详细信息，如 NetworkSettings、IP Address 等。
画面 10: 显示 docker ps 命令的输出，列出正在运行的容器，包括 CONTAINER ID、COMMAND、CREATED、STATUS、PORTS、NAMES。
画面 11: 显示尝试删除容器 mycentos 时，因容器正在运行而失败，提示信息为 "Error response from daemon: You cannot remove a running container ... Stop the container before attempting to remove it"。
画面 12: 显示使用 docker stop 命令停止容器 mycentos，然后再次尝试删除，但提示 "Error response from daemon: You cannot remove a running container ... Stop the container before attempting to remove it"。
画面 13: 显示使用 docker rm -f 命令强制删除容器 mycentos，然后尝试删除镜像 centos，提示 "Error response from daemon: conflict: unable to remove repository reference 'centos': (must force) - container b5eccd1114b is using its referenced image 51be286772b1"。
画面 14: 显示 PPT 页面，标题为“3.2.5 目录挂载”，并列出命令：docker run -v /宿主机目录:/容器内目录 容器名:镜像名，以及 docker run -d -v /宿主机目录:/容器内目录 --name=容器名 镜像名。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 3:
docker inspect 容器名称（容器ID）
docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名称（容器ID）

画面 4:
{
  "Cpusetcpus": "",
  "Cpusetmems": "",
  "Devices": [],
  "DiskUsage": "",
  "Memory": 0,
  "MemoryReservation": 0,
  "MemorySwap": 0,
  "MemorySwappiness": null,
  "NanoCpus": 0,
  "OomKillDisable": false,
  "PidsLimit": 0,
  "Ulimits": [],
  "CpuPeriod": 0,
  "CpuQuota": 0,
  "CpuSet": "",
  "CpuShares": 0,
  "CpuSetMems": "",
  "CpuSetMemsMask": "",
  "CpuSetMemsList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMemsMaskList": "",
  "CpuSetMems
