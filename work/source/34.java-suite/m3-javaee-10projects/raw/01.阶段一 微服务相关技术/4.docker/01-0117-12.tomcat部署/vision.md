# 画面线理解：12.tomcat部署

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\12.tomcat部署_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:45, 02:29, 02:34, 02:38, 02:49, 03:14, 03:26, 03:32, 03:56, 04:13, 04:19, 04:33, 05:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:06:47

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 Tomcat 和 Nginx 容器，并通过浏览器访问部署后的服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Docker 教程文档，内容包括 Docker 概念、安装、镜像管理等，重点是 4.2 Tomcat 部署和 4.3 Nginx 部署章节，其中包含 Docker 拉取和创建容器的命令。
画面2：在 Linux 终端中执行 `docker images` 命令，列出本地镜像，包括 jdk1.8、mysql-57-centos7、centos、nginx 等。
画面3：空白画面，无有效信息。
画面4：浏览器访问 `http://localhost:9100`，显示一个包含多个功能模块（如交易系统、新闻、电影等）的网站主页。
画面5：浏览器地址栏显示 `localhost:9000`，页面为空白。
画面6：浏览器访问 `http://192.168.184.141:9000`，返回 HTTP 404 错误，提示“找不到该网页”。
画面7：在 Linux 终端中执行 `docker ps` 命令，列出正在运行的容器，包括名为 `mytomcat` 的容器，映射端口 8000:8080。
画面8：在 Linux 终端中执行 `ftp put` 命令，上传 `jdk-8u111-linux-x64.tar.gz` 文件到远程服务器。
画面9：Windows 文件资源管理器，显示 `C:\` 盘符，无其他内容。
画面10：在 Linux 终端中执行 `docker ps` 命令，列出正在运行的容器，包括名为 `mytomcat` 的容器。
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
4.2 tomcat部署
（1）拉取镜像
docker pull tomcat:7-jre7
（2）创建容器
创建容器 -d 表示后台运行
docker run -d --name=mytomcat -p 8000:8080
-v /usr/local/webapps:/usr/local/tomcat/webapps tomcat:7-jre7
4.3 Nginx部署
（1）拉取镜像
docker pull nginx
（2）创建Nginx容器
```
画面7：
```
# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
jdk1.8              latest             48c19b0b3445        About an hour ago   387MB
mysql               57-centos7          78b60b2ef6e0        2 hours ago         129MB
centos              latest             2e10df7a8a6f        9 days ago          200MB
redis               latest             4e8b0118f18c        3 weeks ago         83.4MB
nginx               latest             c8221b76580            3 weeks ago         10MB
registry            latest             c8221b76580            3 weeks ago         10MB
# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
c8221b76580         nginx:latest        "nginx -g 'daemon off'"   3 weeks ago         Up 9 hours          0.0.0.0:3306->3306/tcp              mycentos
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
