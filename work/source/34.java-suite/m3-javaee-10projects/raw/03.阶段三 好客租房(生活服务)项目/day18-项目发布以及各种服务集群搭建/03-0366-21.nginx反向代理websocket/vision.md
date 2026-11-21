# 画面线理解：21.nginx反向代理websocket

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\21.nginx反向代理websocket【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:46, 00:48, 00:55, 00:57, 00:58, 00:59, 01:02, 01:07, 01:16, 01:19, 01:43, 02:13, 02:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:00:45

1) 这一组画面整体在讲如何配置 Nginx 反向代理 WebSocket 服务。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Typora 编辑器中关于“3.5. nginx反向代理websocket”的配置代码，包含 server 块和 location 块，用于反向代理 WebSocket。
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
画面13: 展示了 Typora 编辑器中关于“3.5. nginx反向代理websocket”的配置代码，与画面1相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```
3.5. nginx反向代理websocket

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

#pid logs/nginx.pid;

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
