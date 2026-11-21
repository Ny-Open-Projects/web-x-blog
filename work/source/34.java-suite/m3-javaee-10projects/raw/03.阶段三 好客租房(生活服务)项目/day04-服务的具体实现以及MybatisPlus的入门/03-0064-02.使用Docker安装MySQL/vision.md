# 画面线理解：02.使用Docker安装MySQL

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\02.使用Docker安装MySQL【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 03:32, 04:02, 04:21, 05:05, 06:55, 07:06, 07:18, 07:48, 08:10, 08:22, 08:40, 09:41, 09:59, 10:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:39:43

1) 这一组画面整体在讲什么（一句话）：
使用 Docker 容器化方式部署 Percona 版本的 MySQL 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档内容，介绍 Percona 是 MySQL 的增强版本，采用 Docker 部署。列出 Docker 拉取和创建容器的命令：docker pull percona:5.7.23 和 docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23。
画面 2: 在终端中执行 docker stop percona 和 docker rm percona 停止并删除容器。接着执行 docker ps -a 查看容器状态，显示 percona 容器已停止。执行 docker images 查看镜像列表，包含 zookeeper:3.5 和 percona:5.7.23。
画面 3: 展示 PDF 文档内容，详细解释 Docker 创建容器命令的参数：-name、-v、-p、-e。
画面 4: 终端中执行 docker stop percona 和 docker rm percona 停止并删除容器。执行 docker ps -a 查看容器状态，显示 percona 容器已停止。执行 docker images 查看镜像列表，包含 zookeeper:3.5 和 percona:5.7.23。
画面 5: 终端中执行 docker stop percona 和 docker rm percona 停止并删除容器。执行 docker ps -a 查看容器状态，显示 percona 容器已停止。执行 docker images 查看镜像列表，包含 zookeeper:3.5 和 percona:5.7.23。
画面 6: 在终端中执行 ls -l /data/mysql-data 命令，查看目录内容，显示目录为空。
画面 7: 在 EdiPlus 编辑器中，显示创建容器的命令：docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23。
画面 8: 在终端中执行 rm -rf /data/mysql-data 删除目录，提示目录不存在。接着执行 docker create 命令创建容器，然后执行 docker start percona 启动容器。
画面 9: 在终端中执行 ls -l /data/mysql-data 命令，查看目录内容，显示 MySQL 相关文件和目录，如 mysql、performance_schema、sys 等。
画面 10: 在终端中执行 ls -l /data/mysql-data 命令，查看目录内容，显示 MySQL 相关文件和目录，如 mysql、performance_schema、sys 等。
画面 11: 展示文件资源管理器，显示 Navicat Premium 的安装文件夹，包含 Navicat Premium 的可执行文件。
画面 12: 展示 PDF 文档内容，详细解释 Docker 创建容器命令的参数：-name、-v、-p、-e。
画面 13: 展示 PDF 文档内容，显示连接属性窗口，主机地址为 172.16.55.185，端口为 3306。
画面 14: 展示 PDF 文档内容，介绍 Percona 是 MySQL 的增强版本，采用 Docker 部署。列出 Docker 拉取和创建容器的命令：docker pull percona:5.7.23。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
#镜像地址：https://hub.docker.com/_/percona/
#拉取镜像
docker pull percona:5.7.23
#创建容器
docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#参数解释
--name percona 指定容器的名称
-v /data/mysql-data:/var/lib/mysql 将主机目录/data/mysql-data挂载到容器的/var/lib/mysql上
-p 3306:3306 设置端口映射，主机端口是3306，容器内部端口3306
-e MYSQL_ROOT_PASSWORD=root 设置容器参数，设置root用户的密码为root
percona:5.7.23 镜像名:版本
#启动容器
docker start percona

画面 3:
#镜像地址：https://hub.docker.com/_/percona/
#拉取镜像
docker pull percona:5.7.23
#创建容器
docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
#参数解释
--name percona 指定容器的名称
-v /data/mysql-data:/var/lib/mysql 将主机目录/data/mysql-data挂载到容器的/var/lib/mysql上
-p 3306:3306 设置端口映射，主机端口是3306，容器内部端口3306
-e MYSQL_ROOT_PASSWORD=root 设置容器参数，设置root用户的密码为root
percona:5.7.23 镜像名:版本
#启动容器
docker start percona

画面 7:
docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

画面 8:
root@bitcast:~# rm -rf /data/mysql-data
ls: cannot access '/data/mysql-data': No such file or directory
root@bitcast:~# docker create --name percona -v /data/mysql-data:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
a801fcb82204ff995391a5u16f3b5d1cc7f4bchce1c2325b7b7612d2416
root@bitcast:~# docker start percona

画面 9:
root@bitcast:~# ls -l /data/mysql-data
total 192324
drwxr-x--- 2 999 999 4096 Nov 15 11:46 ./
drwxr-x--- 2 999 999 4096 Nov 15 11:46 ../
-rw-r----- 1 999 999 56 Nov 7 17:52 auto.cnf
-rw-r----- 1 999 999 1680 Nov 7 17:52 ca-key.pem
-rw-r----- 1 999 999 1120 Nov 7 17:52 ca.pem
-rw-r----- 1 999 999 1120 Nov 7 17:52 client-cert.pem
-rw-r----- 1 999 999 1339 Nov 7 17:52 client-key.pem
-rw-r----- 1 999 999 79631776 Nov 15 11:46 ibdata1
-rw-r----- 1 999 999 50331648 Nov 15 11:46 ib_logfile0
-rw-r----- 1 999 999 50331648 Nov 15 11:46 ib_logfile1
-rw-r----- 1 999 999 1676 Nov 7 17:52 mysql/
-rw-r----- 1 999 999 1676 Nov 7 17:52 performance_schema/
-rw-r----- 1 999 999 452 Nov 7 17:52 private_key.pem
-rw-r----- 1 999 999 1120 Nov 7 17:52 public_key.pem
-rw-r----- 1 999 999 1676 Nov 7 17:52 server-cert.pem
-rw-r----- 1 999 999 1676 Nov 7 17:52 server-key.pem
-rw-r----- 1 999 999 12288 Nov 7 17:52 sys/
-rw-r----- 1 999 999 12288 Nov 15 11:4
