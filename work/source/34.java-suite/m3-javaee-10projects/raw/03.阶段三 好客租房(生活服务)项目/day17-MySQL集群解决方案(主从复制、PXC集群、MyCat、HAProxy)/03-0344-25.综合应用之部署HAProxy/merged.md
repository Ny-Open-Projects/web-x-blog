# 25.综合应用之部署HAProxy

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\25.综合应用之部署HAProxy【海量资源尽在 ubkz.com】.mp4
- 时长 2分25秒（音频 146s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来部署我们的HAPropesy那么我们来看一下其实我们只需要去修改配置文件是不是就可以了那么配置文件的修改内容呢关键是在下面的这个位置就是指定我们的两个Macad启动的一个端口呢是这个18067一个是18068这个呢也要改一下这个改成18068好那么我们来修改一下那么它是在我们的Hawk下面有一个叫做HAPropesy
[00:28] 下面有一个文件把它打开看一下那么在最下面我们把它设置为一个叫做18067然后还有一个叫做18068对吗检查一下18067好18068然后这个是变成18067然后18068好搞定那么配置文件修改完成其实我们的这个
[00:58] 负载均衡也就已经搞定了那么把这个容器呢我们去启动一下那么我们容器现在有启动吗检查一下PS那么没有那么我们来启动一下走那么等待它的一个启动好现在它就启动成功了那我们来去连接一下那么前面我们已经创建过连接了是不是有一个叫做HAProxy是它
[01:23] 打开连接没有问题可以看到是不是这两张表通过它是不是也可以去查询到我们的数据没有任何问题的对吧没有任何问题哎OK好嘞那么这样的话呢到这呢其实我们的就已经搭建完成了对不对那么我们也可以看一下吧这个呢我们刚刚也看到过啊来刷新一下哎OK他又还是有两个这个节点啊没有任何问题好那么呃我们呢也测试成功了这边拿到数据了至此呢我们这个集群是不是就已经搭建完成了我们来看一下
[01:51] 架构中的我们他是不是只要做他呢是不是只要做一个配置那么这不就可以了那么只要把这个请求能够转发到这两个节点就OK那我们的应用程序去连接他就可以了那么也就是说我们现在呢是不是只需要将我们的应用程序的数据库的一个连接改为什么呢改为他的一个连接是不是就可以了OK好那么到这里呢我们整个综合应用的一个这个实现的就已经搞定了
[02:19] 好那么关于我们最后一个部署HAPopsy的一个讲解那我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置和启动 HAProxy 作为 MyCat 集群的负载均衡器，并通过 Docker 部署。

2) 按时间顺序列出每张画面的要点：
画面1：展示 HAProxy 配置文件内容，包含 global 和 defaults 部分，以及 listen admin_stats 和 listen proxy-mysql 的配置。
画面2：在终端中列出 MyCat 节点的依赖库文件路径，准备启动 MyCat。
画面3：显示 HAProxy 配置文件中的 global 和 defaults 部分，以及 listen admin_stats 配置。
画面4：显示 HAProxy 配置文件中的 listen proxy-mysql 配置，包含 server mycat_1 和 server mycat_2 的定义。
画面5：在终端中查看 haproxy 目录下的文件，准备编辑配置文件。
画面6：在终端中执行 Docker ps 查看容器状态，并执行 Docker start haproxy 启动 HAProxy。
画面7：在 Navicat 中连接到 MyCat 集群，查看 tb_ad 表。
画面8：在 Navicat 中连接到 HAProxy 代理，查看 tb_ad 表。
画面9：展示 HAProxy 配置文件内容，包含启动命令和访问地址。
画面10：显示 HAProxy 统计报告，展示前端和后端的连接状态。
画面11：展示 HAProxy 的连接属性，配置了 HTTP 访问。
画面12：在 Navicat 中连接到 HAProxy 代理，查看 tb_ad 表。
画面13：展示 HAProxy 作为负载均衡器的架构图，说明其与 MyCat 集群的关系。
画面14：展示 Docker 容器创建命令，用于部署 MyCat 集群。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
# 频繁文件
2 vin /haoke/haproxy/haproxy.cfg
4 # 请加入如下内容
5 global
6 log    127.0.0.1 local2
7 maxconn 4000
8 daemon

9 defaults
10 mode http
11 log global
12 option httplog
13 option dontlognull
14 option http-server-close
15 option forwardfor except 127.0.0.0/8
16 option redispatch
17 retries 3
18 timeout http-request 10s
19 timeout queue 1m
20 timeout connect 10s
21 timeout client 1m
22 timeout server 1m
23 timeout http-keep-alive 10s
24 timeout check 10s
25 maxconn 3000

26 listen admin_stats
27 bind 0.0.0.0:4001
28 mode http
29 stats uri /dbs
30 stats realm Global\ statistics
31 stats auth admin:admin123

32 listen proxy-mysql
33 bind 0.0.0.0:4002
34 mode tcp
35 balance roundrobin
36 option tcplog
37 server mycat_1 192.168.1.18:18067 check port 18067 maxconn 2000
38 server mycat_2 192.168.1.18:18068 check port 18068 maxconn 2000
```

画面4：
```
listen proxy-mysql
bind 0.0.0.0:4002
mode tcp
balance roundrobin
option tcplog
server mycat_1 192.168.1.18:18067 check port 18067 maxconn 2000
server mycat_2 192.168.1.18:18068 check port 18068 maxconn 2000
```

画面9：
```
# 启动容器
1 Docker start haproxy && Docker logs -f haproxy
http://192.168.1.18:4001/dbs
```

画面14：
```
node4 13309
pcc_node4
haoke-v4

# 创建数据卷（存储路径：/var/lib/Docker/volumes）
2 Docker volume create haoke-v1
3 Docker volume create haoke-v2
4 Docker volume create haoke-v3
5 Docker volume create haoke-v4

# 拉取镜像
8 Docker pull persona/persona-xtradb-cluster:5.7

# 创建网络
13 Docker network create --subnet=172.30.0.2/24 pxc-network

# 创建容器
15 Docker create -p 13306:3306 -v haoke-v1:/var/lib/mysql --name=pxc_node1 -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --net=pxc-network --ip=172.30.0.2 pxc
17 Docker create -p 13306:3306 -v haoke-v2:/var/lib/mysql --name=pxc_node2 -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --net=pxc-network --ip=172.30.0.3 pxc
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13：
架构图：
- 应用系统 → HAProxy → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- My

