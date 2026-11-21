# 1.17 应用服务介绍

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day1 背景介绍与系统介绍
- 源文件：06.阶段六 冷链监控平台项目\day1 背景介绍与系统介绍\1.17 应用服务介绍_【海量资源尽在 666java.com】.mp4
- 时长 4分53秒（音频 293s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来从系统的角度看一下我们整个冷链监控平台拥有的这种应用服务主要包括两部分一部分是我们的后台服务一部分是我们的前台应用那么前台应用我们使用是Node.js VUE来开发的这种前台的一些HTML JS它会调用我们后台的一个请求那么我们重点会说一下我们的这个后台服务后台服务包括我们的CodeUric
[00:30] 然后也包括我们的code gatewaycode uric是我们的服务注册中心那么它的端口是8001我们在启动的时候直接用java-j来启动起来就可以了因为本身我们所有的服务都是属于用spawn boot来创建的这种java应用我们所以可以直接用java-j来启动
[00:53] 这个命令的后边这一部分呢是我们是一个&的符号&的符号的意思是说在Linux操作系统里边如果启动用加上&的符号那么这个应用或者这个进程会在Linux的后台来执行那我们看一看我们的code辅助的中心那么它的一个作用相当于是说一个公司或者说一个部门一个公司它在有一个前台而这个前台呢有一个
[01:22] 叫做有一个目录或者说有一个小本本这个目录里边它会给告诉我们我们后边就是说整个公司的每一个部门每一个办公室每个部门在哪个办公室比如说我们的有一个前台应用前台的一个API调用调用到了我们的code gateway那么code gateway 8080它先查一下我们的Ureca有哪些服务注册上来了那么有
[01:51] 比如说有code user或者code admin他们注册上来之后呢我们直接就是由code gateway对他做一次这种路由路由到说你如果是访问了code user就是访问用户服务那么我会告诉你你需要访问到8185这个端口那么code user是在这个端口里面提供了一些服务这是我们的code uric和code gateway的一个不太恰当的一个举的一个例子大家可以体会一下这个
[02:21] 服务注册中心和网关它的一个作用那么code user的话是我们在系统里面提供的用户的一些服务目前我们在冷链设备监控平台当前这个版本里面提供的服务比较简单就是用户的一个登录用户的一个退出这样的一个功能那么code admin的话是我们的管理服务这个管理服务包括我们的一些公司仓库主机设备的一些设置和管理那么code
[02:50] Droid的话它的端口是8182它是用来查询Droid里边的一个查询服务是查询Droid里边的数据库那么CodeMonitor的话是实时查询我们的MySQL数据库它是查询MySQL数据库里边的一个数据的结果的一个服务那么CodeJobs是我们的一个定时任务这个定时任务会模拟我们的硬件设备用定时任务的方式来启动
[03:20] 发送我们的设备的报文CodeNative是我们的Native服务器就是用来接收前端请求过来的就是设备提交过来的一些用报文数据也就是说我们在CodeJob模拟的设备然后它提交的一些文字提交的一些报文会发送到Native服务器的一个端口里边那么CodeUI就是我们的前端应用了这个前端应用会
[03:48] 也是部署在我们的Tomcat里面去我们使用后边这个命令可以启动起来那我们的前台应用的话就是实际上是一个刚才也提到了是我们的TomcatTomcat我们在Linux里面是放到我们的etc Tomcat这个目录下然后我们使用的是它的应用目录是在Tomcat的应用目录里面如果我们在本地编译的时候我们可以使用npm install这个命令来编译Vue
[04:18] 那么也可以也会会使用 npm run server 这个方式来这个命令来在本地启动我们的web应用那么如果我们要部署到我们的Tomcat里边去就是 linux的Tomcat里边那么我们需要先用 npm run build 这种命令来生成生成我们的 data 的目录就是生成这个 html js 的这个目录然后把这个目录呢上传到我们的linux web 服务器里面去
[04:46] 然后这个时候其实就OK了这是我们的前台和后台的这个应用和服务

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个微服务架构的后台服务与前台应用的配置与部署方法。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了“3.3.1 后台服务”章节，包含一个表格，列出了多个服务的“应用”、“端口”、“说明”和“启动命令”。
- 表格内容包括：cold-Eureka (8001, 服务注册中心), cold-gateway (8080, API网关), cold-user (8185, 用户服务), cold-admin (8181, 管理服务), cold-druid (8182, Druid查询服务), cold-monitor (8183, 实时查询服务), cold-jobs (8184, 定时任务服务), cold-netty-server (10010, netty服务), cold-ui (8000, web服务, Tomcat)。
- 表格下方开始显示“3.3.2 前台应用”章节。

画面2：
- 继续展示“3.3.2 前台应用”章节。
- 显示“前端Tomcat”的配置信息：配置文件：/etc/Tomcat/，应用目录：/var/lib/Tomcat/webapps。
- 开始显示“编译web应用”部分，包含“# 搭建Vue”、“npm install”、“# 本地运行web应用”、“npm run serve”等命令。

画面3：
- 继续展示“编译web应用”部分，命令为“npm run serve”。
- 同时显示“部署web应用”部分，包含“# 生成dist目录”、“npm run build”、“# 将dist目录上传至web服务器”、“# 修改文件夹名为cold”、“[root@godz-web]# cd /var/lib/Tomcat/webapps/”、“[root@godz-web]# unzip dist.zip”、“[root@godz-web]# mv dist cold”等命令。

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
cold-Eureka	8001	服务注册中心	java -jar cold-Eureka-0.0.1-SNAPSHOT.jar &
cold-gateway	8080	API网关，前端统一入口	java -jar cold-gateway-0.0.1-SNAPSHOT.jar &
cold-user	8185	用户服务	java -jar cold-user-1.0.0.jar &
cold-admin	8181	管理服务	java -jar cold-admin-0.0.1-SNAPSHOT.jar &
cold-druid	8182	Druid查询服务	java -jar cold-druid-1.0.0.jar &
cold-monitor	8183	实时查询服务	java -jar cold-monitor-0.0.1-SNAPSHOT.jar &
cold-jobs	8184	定时任务服务	java -jar cold-jobs-0.0.1-SNAPSHOT.jar &
cold-netty-server	10010	netty服务	java -jar cold-netty-server-1.0-SNAPSHOT.jar &
cold-ui	8000	web服务，Tomcat	Service Tomcat start | stop | restart
```

画面2：
```
前端Tomcat：
• 配置文件： /etc/Tomcat/
• 应用目录： /var/lib/Tomcat/webapps

编译web应用
# 搭建Vue
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
[root@godz-web]# cd /var/lib/Tomcat/webapps/
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
[root@godz-web]# cd /var/lib/Tomcat/webapps/
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
[root@godz-web]# cd /var/lib/Tomcat/webapps/
[root@godz-web]# unzip dist.zip
[root@godz-web]# mv dist cold
```

画面6：
```
应用	端口	说明	启动命令
cold-Eureka	8001	服务注册中心	java -jar cold-Eureka-0.0.1-SNAPSHOT.jar &
cold-gateway	8080	API网关，前端统一入口	java -jar cold-gateway-0.0.1-SNAPSHOT.jar &
cold-user	8185	用户服务	java -jar cold-user-1.0.0.jar &
cold-admin	8181	管理服务	java -jar cold-admin-0.0.1-SNAPSHOT.jar &
cold-druid	8182	Druid查询服务	java -jar cold-druid-1.0.0.jar &
cold-monitor	8183	实时查询服务	java -jar cold-monitor-0.0.1-SNAPSHOT.jar &
cold-jobs	8184	定时任务服务	java -jar cold-jobs-0.0.1-SNAPSHOT.jar &
cold-netty-server	10010	netty服务	java -jar cold-netty-server-1.0-SNAPSHOT.jar &
cold-ui	8000	web服务，Tomcat	Service Tomcat start | stop | restart
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 画面1、2、6：标题为“3.3.1 后台服务”和“3.3.2 前台应用”。
- 画面1、2、6：表格数据包括“应用”、“端口”、“说明”、“启动命令”。
- 画面2、3、4、5：表格数据包括“前端Tomcat”、“编译web应用”、“部署web应用”。
- 画面5：标题为“4. 数据结构”。

5) 不要评价画面美观，不要输出与课程无关的内容。

