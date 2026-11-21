# 画面线理解：15.HAProxy负载均衡之介绍以及架构说明

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\15.HAProxy负载均衡之介绍以及架构说明【海量资源尽在 ubkz.com】.mp4
- 抽帧：9 帧 @ 00:09, 00:10, 00:11, 00:25, 00:26, 00:45, 02:28, 02:29, 02:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:38:41

1) 这一组画面整体在讲如何搭建多节点的 MyCat 数据库中间件集群，并引出使用 HAProxy 进行负载均衡的架构。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 MyCat 配置界面，填写主机地址 192.168.1.18、端口 8067、用户名 root，下方显示已部署的 mycat2 节点。
画面2: 展示 MyCat 配置文件 server.xml 的部分代码，包含设置管理端口的配置项。
画面3: 展示 MyCat 多节点集群的架构图，应用系统通过中间件连接 MySQL（主）和 MySQL（从），并标注“同步”。
画面4: 展示 MyCat 多节点集群的架构图，与画面3相同，但下方显示了 MyCat 配置文件的代码片段。
画面5: 展示 MyCat 配置界面，填写主机地址 192.168.1.18、端口 8067、用户名 root。
画面6: 展示 HAProxy 简介页面，介绍 HAProxy 是一个高性能的 TCP/HTTP 负载均衡器。
画面7: 展示 HAProxy 架构图，应用系统通过 proxy 连接两个中间件，再连接 MySQL（主）和 MySQL（从）。
画面8: 展示 HAProxy 架构图，与画面7相同，但下方显示了 HAProxy 的架构图。
画面9: 展示 HAProxy 架构图，与画面7相同，但鼠标悬停在“读写操作”上。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面2:
```xml
<property name="serverPort">8067</property>
<property name="managerPort">9067</property>
```

画面4:
```bash
cp mycat mycat2 -R
```

画面6:
```text
haproxy 是一个使用 C 语言编写的自由软件负载均衡器，其支持 HTTP、TCP、UDP 协议，以及基于 TCP/HTTP 的应用程序代理。
```

4) PPT 标题、架构图/流程图的结构：
画面3:
架构图结构：
- 应用系统 → 读写操作 → 中间件
- 应用系统 → 读写操作 → 中间件
- 中间件 → 写操作 → MySQL（主）
- 中间件 → 读操作 → MySQL（从）
- MySQL（主） ↔ 同步 ↔ MySQL（从）

画面7:
架构图结构：
- 应用系统 → 读写操作 → proxy
- proxy → 读写操作 → 中间件
- proxy → 读写操作 → 中间件
- 中间件 → 写操作 → MySQL（主）
- 中间件 → 读操作 → MySQL（从）
- MySQL（主） ↔ 同步 ↔ MySQL（从）

5) 无
