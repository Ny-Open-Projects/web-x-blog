# 12.tomcat部署

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\12.tomcat部署_【海量资源尽在 ubkz.com】.mp4
- 时长 5分20秒（音频 321s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好,接下来呢我们来学习使用Docker来部署一个Tomcat的环境首先第一步我们要去拉取Tomcat镜像我们在这里使用的是Tomcat然后标签是7-jre7这个7-jre7也就是说是这个7代表Tomcat本身的版本jre7代表的是这里安装的jre的版本是7的这个版本
[00:31] 好我们这一步呢是可以省略的因为我给大家提供的这个镜像中其实已经包括这个镜像了大家也无需要啊另行下载了那我们现在可以直接去根据这个镜像来创建容器就可以了干DI啊然后呢,干干内幕等于等于什么呢这个买他们看比如说起名叫买他们看那接下来呢我们再加杠批
[01:01] -p 是什么端口映射我们可以用9000来映射它本身的8080端口-v 代表的是目录挂载对吧我们说为了更方便的部署他们开的应用这里我们可以挂载一个目录比如说叫webapps这个webapps我给它放到local目录下本地的local目录下如果这个目录不存在它会自动创建的
[01:32] 接下来冒号后面的部分就是你的这个呃就容器内的他们开的路径啊那么容器内的他们的路径呢是在这啊usr local他们开的下的web apps啊是这个目录usr local他们开的下的a webapps啊这是我们说的一个目录挂载然后紧接着我们再写这个呃这个镜像的名称
[02:04] 他们看他码号7-7-JRE7JRE7现在我们已经把容器就创建成功了我们来看一下现在的容器已经是运行状态那么运行状态之后咱们现在可以打开9000我们来看一下到底能不能访问192.168.2
[02:44] 184.141大家会发现我们并没有看到他们开的欢迎页面是吧这是为什么是因为我们在这里用了一个目录挂载那么目录挂载之后这时候你本地的文件夹是新创建的是没有任何的内容的而原来是有一个root对吧那么这个root已经被清空了所以说这个时候你就看不到任何页面了那么现在可以
[03:14] 为他们看的部署一个web应用就可以了就部署一个web应用那么部署哪一个呢我们在这里可以把CAS给它布上去这个时候我们来找一下我给大家提供一个CS.Y这是耶鲁大学开源的一个单点登录的这么一个程序我们现在可以把它布上去上传上去地盘的setup下的CS.Y
[03:47] 上传上去之后接下来咱们看一下看一下现在这个var已经传上去了接下来我们要怎么办把它转移转移一下转移到哪里USR local下的webapps那么转移到之后接下来咱们再次测试这里写cas这时候仍然是没有显示出来是吧
[04:24] 那么看一下问题出在哪现在我们进到这个幕下usr local下的webapps咱们这时候会发现这个CS是已经解压的对吧已经解压的那么咱们现在再次的来看一下再刷这回好了刚才是没有没有完全的解压完成所以说这个是没有显出来现在已经能看到这个CS的这么一个
[04:57] 主界面了这么一个登录界面了好这就是关于Tomcat的一个部署那么在这个环节我们主要学习的就是就是什么呢就是端口映射第二个就是我们的目录挂载这两个实际的这种容器创建过程中是应用比较广泛的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 Tomcat 和 Nginx 容器，并通过浏览器访问部署后的服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Docker 教程文档，内容包括 Docker 概念、安装、镜像管理等，重点是 4.2 Tomcat 部署和 4.3 Nginx 部署章节，其中包含 Docker 拉取和创建容器的命令。
画面2：在 Linux 终端中执行 `Docker images` 命令，列出本地镜像，包括 JDK 8、mysql-57-centos7、centos、Nginx 等。
画面3：空白画面，无有效信息。
画面4：浏览器访问 `http://localhost:9100`，显示一个包含多个功能模块（如交易系统、新闻、电影等）的网站主页。
画面5：浏览器地址栏显示 `localhost:9000`，页面为空白。
画面6：浏览器访问 `http://192.168.184.141:9000`，返回 HTTP 404 错误，提示“找不到该网页”。
画面7：在 Linux 终端中执行 `Docker ps` 命令，列出正在运行的容器，包括名为 `mytomcat` 的容器，映射端口 8000:8080。
画面8：在 Linux 终端中执行 `ftp put` 命令，上传 `jdk-8u111-linux-x64.tar.gz` 文件到远程服务器。
画面9：Windows 文件资源管理器，显示 `C:\` 盘符，无其他内容。
画面10：在 Linux 终端中执行 `Docker ps` 命令，列出正在运行的容器，包括名为 `mytomcat` 的容器。
画面11：浏览器访问 `http://192.168.184.141:9000`，返回 HTTP 404 错误，提示“找不到该网页”。
画面12：浏览器访问 `http://192.168.184.141:9000/cas`，返回 HTTP 404 错误，提示“找不到该网页”。
画面13：在 Linux 终端中执行 `cd /usr/local/webapps` 命令，进入目录。
画面14：在 Linux 终端中执行 `cd /usr/local/webapps` 命令，进入目录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
-p 代表端口映射，格式为：宿主机映射端口:容器运行端口
（3）远程登录mysql
连接宿主机的IP，指定端口为3306
4.2 Tomcat部署
（1）拉取镜像
Docker pull Tomcat:7-jre7
（2）创建容器
创建容器 -d 表示后台运行
Docker run -d --name=mytomcat -p 8000:8080
-v /usr/local/webapps:/usr/local/Tomcat/webapps Tomcat:7-jre7
4.3 Nginx部署
（1）拉取镜像
Docker pull Nginx
（2）创建Nginx容器
```
画面7：
```
# Docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
JDK 8              latest             48c19b0b3445        About an hour ago   387MB
mysql               57-centos7          78b60b2ef6e0        2 hours ago         129MB
centos              latest             2e10df7a8a6f        9 days ago          200MB
redis               latest             4e8b0118f18c        3 weeks ago         83.4MB
Nginx               latest             c8221b76580            3 weeks ago         10MB
registry            latest             c8221b76580            3 weeks ago         10MB
# Docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
c8221b76580         Nginx:latest        "Nginx -g 'daemon off'"   3 weeks ago         Up 9 hours          0.0.0.0:3306->3306/tcp              mycentos
```
画面13：
```
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr/local/webapps
# cd /usr

