# 21.nginx反向代理websocket

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\21.nginx反向代理websocket【海量资源尽在 ubkz.com】.mp4
- 时长 2分28秒（音频 149s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接下来呢让我们的NJX来反向代理我们的WebSocket也就是我们那个IM那个项目那么目前呢我们这个IM项目呢是部署在19这个服务器上面那么我们希望呢通过这个im.hawk.com这个域名呢去做一个这样的一个访问那么OK我们来看一下这个配置啊那么其实NJX去反向代理我们的WebSocket呢也是比较简单的
[00:27] 那么他只需要在我们之前的http代理的基础之上呢添加两个配置就可以了这两个配置呢其实就告诉Nginx呢需要去升级我们原有的http的这样的一个请求那么这样的话就可以去反向代理到我们的WebSocket那好那么接下来我们来实际操作一下那我们把这个配置拷贝一下然后呢我们去打开我们的这个Nginx的一个配置那么找到Nginx
[00:55] 然后呢在下面这个位置那么我们再添加一个这个server那就在这吧我们去添加一个这个server把它拷贝进来那么它所反向代理到的就是我们这个地址好保存退出一下那么我们使我们这个ngx呢做一个reload的操作哎呦ok好那么下面呢我们就可以来测试一下那么我们找到我们的
[01:18] 找到我们这个连接就是这个是我们之前的一个WebSocket的一个连接那么我们先把它关闭打开一下发现没有问题那么接下来我们就需要去通过域名去访问对不对那么这个域名呢我们就需要把这个位置改成什么呢改成im然后点poker.com那么要注意的是呢我们这个域名其实需要在我们本地先做一个映射那么我们找到我们这个host这个软件那么我们去做这样的一个映射
[01:46] 那么把我们imhawk.com所映射到我们的18要注意的是18所在的机器其实就是我们刚刚的NJAX所在的机器那么先指向他他就会去你看我们请求他那么先找到他对吧找到他就会找到我们18上面的NJAXNJAX就会去反向代理到19上面的我们im服务OK就是这样的一个过程点击应用OK好那么我们尝试连接一下
[02:15] 会发现这样的话是不是也是可以去正常连接ok没有问题没有问题好那么我们现在是不是就已经完成了通过 NGX去反向代理WebSocket好那么关于我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置 Nginx 反向代理 WebSocket 服务。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Typora 编辑器中关于“3.5. Nginx反向代理WebSocket”的配置代码，包含 server 块和 location 块，用于反向代理 WebSocket。
画面2: 展示了终端界面，提示符为 root@itcast02: sbin#，准备进行后续操作。
画面3: 展示了 Nginx 配置文件的开头部分，包含 worker_processes、events 和 http 块的配置。
画面4: 展示了 Nginx 配置文件中 http 块的继续部分，包含 include、default_type 和 access_log 配置。
画面5: 展示了 Nginx 配置文件中包含的 server 块，用于配置虚拟主机，监听 80 端口，server_name 为 api.manage.haoke.com。
画面6: 展示了 Nginx 配置文件中 server 块的继续部分，包含 #charset 和 proxy_set_header 配置。
画面7: 展示了 Nginx 配置文件中 location 块的继续部分，包含 proxy_pass、proxy_connect_timeout、proxy_read_timeout 和 proxy_set_header Connection "upgrade" 配置。
画面8: 展示了终端界面，提示符为 root@itcast02: sbin#，准备编辑 Nginx 配置文件。
画面9: 展示了 Elasticsearch Head 界面，显示了索引数据，包括 house、orientation、rentMethod、time 等字段。
画面10: 展示了 Simple WebSocket Client 界面，显示了 WebSocket 连接状态为 OPENED，请求和消息日志内容。
画面11: 展示了 SwitchHosts! 工具界面，显示了生产环境的多个 hosts 配置，包括 192.168.1.19 和 im.haoke.com。
画面12: 展示了 Simple WebSocket Client 界面，显示了 WebSocket 连接状态为 CLOSED。
画面13: 展示了 Typora 编辑器中关于“3.5. Nginx反向代理WebSocket”的配置代码，与画面1相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```
3.5. Nginx反向代理WebSocket

server {
    listen 80;
    server_name in.haoke.com;

    #charset koi8-r;

    #access_log logs/host.access.log main;

    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    location / {
        proxy_pass http://192.168.1.19:18081;
        proxy_connect_timeout 600;
        proxy_read_timeout 600;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

画面3:
```
#user nobody;
worker_processes 1;

#error_log logs/error.log;
#error_log logs/error.log notice;
#error_log logs/error.log info;

#pid logs/Nginx.pid;

events {
    worker_connections 1024;
}

http {
    include mime.types;
    default_type application/octet-stream;

    #log_format main '$remote_addr - $remote_user [$time_local] "$request" '
    #               '$status $body_bytes_sent "$http_referer" '
    #               '"$http_user_agent" "$http_x_forwarded_for";'

    #access_log logs/access.log main;
    sendfile on;
```

画面5:
```
server {
    listen 80;
    server_name api.manage.haoke.com;

    #charset koi8-r;

    #access_log logs/host.access.log main;

    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    location / {
        proxy_pass http://192.168.1.19:18080;
        proxy_connect_timeout 600;
        proxy_read_timeout 600;
    }
}
```

画面6:
```
# another virtual host using mix of IP-, name-, and port-based configuration
```

画面7:
```
server {
    listen 80;
    server_name im.haoke.com;

    #charset koi8-r;

    #access_log logs/host.access.log main;

    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    location / {
        proxy_pass http://192.168.1.19:18081;
        proxy_connect_timeout 600;
        proxy_read_timeout 600;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面9: 展示了 Elasticsearch Head 界面，表格数据包括索引、类型、ID、image、orientation、houseType、rentMethod、time 等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。

