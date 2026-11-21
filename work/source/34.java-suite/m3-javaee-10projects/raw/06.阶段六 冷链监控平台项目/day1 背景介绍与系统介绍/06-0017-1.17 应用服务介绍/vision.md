# 画面线理解：1.17 应用服务介绍

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day1 背景介绍与系统介绍
- 源文件：06.阶段六 冷链监控平台项目\day1 背景介绍与系统介绍\1.17 应用服务介绍_【海量资源尽在 666java.com】.mp4
- 抽帧：6 帧 @ 03:51, 03:53, 04:10, 04:27, 04:48, 04:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:47:38

1) 这一组画面整体在讲一个微服务架构的后台服务与前台应用的配置与部署方法。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了“3.3.1 后台服务”章节，包含一个表格，列出了多个服务的“应用”、“端口”、“说明”和“启动命令”。
- 表格内容包括：cold-eureka (8001, 服务注册中心), cold-gateway (8080, API网关), cold-user (8185, 用户服务), cold-admin (8181, 管理服务), cold-druid (8182, Druid查询服务), cold-monitor (8183, 实时查询服务), cold-jobs (8184, 定时任务服务), cold-netty-server (10010, netty服务), cold-ui (8000, web服务, Tomcat)。
- 表格下方开始显示“3.3.2 前台应用”章节。

画面2：
- 继续展示“3.3.2 前台应用”章节。
- 显示“前端tomcat”的配置信息：配置文件：/etc/tomcat/，应用目录：/var/lib/tomcat/webapps。
- 开始显示“编译web应用”部分，包含“# 搭建vue”、“npm install”、“# 本地运行web应用”、“npm run serve”等命令。

画面3：
- 继续展示“编译web应用”部分，命令为“npm run serve”。
- 同时显示“部署web应用”部分，包含“# 生成dist目录”、“npm run build”、“# 将dist目录上传至web服务器”、“# 修改文件夹名为cold”、“[root@godz-web]# cd /var/lib/tomcat/webapps/”、“[root@godz-web]# unzip dist.zip”、“[root@godz-web]# mv dist cold”等命令。

画面4：
- 画面内容与画面3基本一致，只是“npm run serve”命令被选中或高亮显示。
- 同时显示“部署web应用”部分的命令。

画面5：
- 画面内容与画面3、4基本一致，只是“部署web应用”部分的命令被选中或高亮显示。
- 同时显示“4. 数据结构”章节标题。

画面6：
- 画面内容与画面1基本一致，展示了“3.3.1 后台服务”表格和“3.3.2 前台应用”章节的开头部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
应用	端口	说明	启动命令
cold-eureka	8001	服务注册中心	java -jar cold-eureka-0.0.1-SNAPSHOT.jar &
cold-gateway	8080	API网关，前端统一入口	java -jar cold-gateway-0.0.1-SNAPSHOT.jar &
cold-user	8185	用户服务	java -jar cold-user-1.0.0.jar &
cold-admin	8181	管理服务	java -jar cold-admin-0.0.1-SNAPSHOT.jar &
cold-druid	8182	Druid查询服务	java -jar cold-druid-1.0.0.jar &
cold-monitor	8183	实时查询服务	java -jar cold-monitor-0.0.1-SNAPSHOT.jar &
cold-jobs	8184	定时任务服务	java -jar cold-jobs-0.0.1-SNAPSHOT.jar &
cold-netty-server	10010	netty服务	java -jar cold-netty-server-1.0-SNAPSHOT.jar &
cold-ui	8000	web服务，Tomcat	service tomcat start | stop | restart
```

画面2：
```
前端tomcat：
• 配置文件： /etc/tomcat/
• 应用目录： /var/lib/tomcat/webapps

编译web应用
# 搭建vue
npm install
# 本地运行web应用
npm run serve
```

画面3：
```
部署web应用：
# 生成dist目录
npm run build
# 将dist目录上传至web服务器
# 修改文件夹名为cold
[root@godz-web]# cd /var/lib/tomcat/webapps/
[root@godz-web]# unzip dist.zip
[root@godz-web]# mv dist cold
```

画面4：
```
部署web应用：
# 生成dist目录
npm run build
# 将dist目录上传至web服务器
# 修改文件夹名为cold
[root@godz-web]# cd /var/lib/tomcat/webapps/
[root@godz-web]# unzip dist.zip
[root@godz-web]# mv dist cold
```

画面5：
```
部署web应用：
# 生成dist目录
npm run build
# 将dist目录上传至web服务器
# 修改文件夹名为cold
[root@godz-web]# cd /var/lib/tomcat/webapps/
[root@godz-web]# unzip dist.zip
[root@godz-web]# mv dist cold
```

画面6：
```
应用	端口	说明	启动命令
cold-eureka	8001	服务注册中心	java -jar cold-eureka-0.0.1-SNAPSHOT.jar &
cold-gateway	8080	API网关，前端统一入口	java -jar cold-gateway-0.0.1-SNAPSHOT.jar &
cold-user	8185	用户服务	java -jar cold-user-1.0.0.jar &
cold-admin	8181	管理服务	java -jar cold-admin-0.0.1-SNAPSHOT.jar &
cold-druid	8182	Druid查询服务	java -jar cold-druid-1.0.0.jar &
cold-monitor	8183	实时查询服务	java -jar cold-monitor-0.0.1-SNAPSHOT.jar &
cold-jobs	8184	定时任务服务	java -jar cold-jobs-0.0.1-SNAPSHOT.jar &
cold-netty-server	10010	netty服务	java -jar cold-netty-server-1.0-SNAPSHOT.jar &
cold-ui	8000	web服务，Tomcat	service tomcat start | stop | restart
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 画面1、2、6：标题为“3.3.1 后台服务”和“3.3.2 前台应用”。
- 画面1、2、6：表格数据包括“应用”、“端口”、“说明”、“启动命令”。
- 画面2、3、4、5：表格数据包括“前端tomcat”、“编译web应用”、“部署web应用”。
- 画面5：标题为“4. 数据结构”。

5) 不要评价画面美观，不要输出与课程无关的内容。
