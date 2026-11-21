# 画面线理解：20.配置api.manage.haoke.com进行访问

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\20.配置api.manage.haoke.com进行访问【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:21, 00:23, 00:24, 00:34, 00:44, 00:47, 01:01, 01:03, 01:07, 01:10, 01:16, 01:20, 01:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:00:13

1) 这一组画面整体在讲什么（一句话）：
演示如何通过修改 Nginx 配置文件来配置两个虚拟主机（manage.haoke.com 和 api.manage.haoke.com），并验证配置效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在终端中列出 /etc/nginx/conf.d/ 目录下的配置文件，准备编辑 nginx.conf。
画面 2: 进入 /etc/nginx/conf.d/ 目录，准备编辑 nginx.conf。
画面 3: 显示 nginx.conf 文件的开头部分，包含 user、worker_processes、events 和 http 块。
画面 4: 显示 server 块，配置了 listen 80、server_name manage.haoke.com，并设置了 proxy_pass 和 root。
画面 5: 在 server 块中添加了新的 server_name api.manage.haoke.com。
画面 6: 与画面 1 相同，列出 /etc/nginx/conf.d/ 目录下的配置文件。
画面 7: 启动 SwitchHosts! 工具，切换到生产环境，显示 manage.haoke.com 的 IP 地址。
画面 8: 与画面 6 相同，列出 /etc/nginx/conf.d/ 目录下的配置文件。
画面 9: 在 SwitchHosts! 工具中，将当前主机切换为 manage.haoke.com。
画面 10: 在终端中执行命令，提示“已切换为‘生产环境’”。
画面 11: 在浏览器中访问 http://192.168.1.7:18000/house/resources，页面为空白。
画面 12: 浏览器加载成功，显示 JSON 数据，内容为 API 返回的资源列表。
画面 13: 浏览器中高亮显示了 JSON 数据中的某个字段。
画面 14: 浏览器中高亮显示了 JSON 数据中的另一个字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
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
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for";'

    #access_log  logs/access.log  main;
```

画面 4:
```
server {
    listen     80;
    server_name manage.haoke.com;

    #charset koi8-r;

    #access_log  logs/host.access.log  main;

    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    location ~ ^/haoke/ {
        proxy_pass http://192.168.1.7:18000/;
        proxy_connect_timeout 600;
        proxy_read_timeout 600;
    }

    location / {
        root /haoke/publish/manage-web;
    }
}
```

画面 5:
```
server {
    listen     80;
    server_name api.manage.haoke.com;

    #charset koi8-r;

    #access_log  logs/host.access.log  main;

    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    location / {
        proxy_pass http://192.168.1.7:18000/;
        proxy_connect_timeout 600;
        proxy_read_timeout 600;
    }
}
```

画面 6:
```
drwxr-xr-x  2 root root 4096 Mar  1 00:10 ./
drwxr-xr-x 11 root root  4096 Feb 25 22:40 fastcgi.conf
drwxr-xr-x  1 root root  1077 Feb 28 22:42 fastcgi.conf.default
drwxr-xr-x  1 root root  1007 Feb 28 22:42 fastcgi_params
drwxr-xr-x  1 root root  1007 Feb 28 22:42 fastcgi_params.default
drwxr-xr-x  1 root root  2837 Feb 28 22:42 koi-utf
drwxr-xr-x  1 root root  2225 Feb 28 22:42 koi-win
drwxr-xr-x  1 root root  3957 Feb 28 22:44 mime.types
drwxr-xr-x  1 root root  3956 Feb 28 22:46 mime.types.default
drwxr-xr-x  1 root root  2556 Feb 28 22:42 nginx.conf
drwxr-xr-x  1 root root  2556 Feb 28 22:42 nginx.conf.default
drwxr-xr-x  1 root root  636  Feb 28 22:40 scgi_params
drwxr-xr-x  1 root root  636  Feb 28 22:40 scgi_params.default
drwxr-xr-x  1 root root  664  Feb 28 22:40 uwsgi_params
drwxr-xr-x  1 root root  664  Feb 28 22:40 uwsgi_params.default
drwxr-xr-x  1 root root  3610 Feb 28 22:42 win-utf
```

画面 7:
```
SwitchHosts! 0.2.2.1801
生产环境
192.168.1.18 manage.haoke.com
```

画面 8:
```
drwxr-xr-x  2 root root 4096 Mar  1 00:10 ./
drwxr-xr-x 11 root root  4096 Feb 25 22:40 fastcgi.conf
drwxr-xr-x  1 root root  1077 Feb 28 22:42 fastcgi.conf.default
drwxr-xr-x  1 root root  1007 Feb 28 22:42 fastcgi_params
drwxr-xr-x  1 root root  1007 Feb 28 22:42 fastcgi_params.default
drwxr-xr-x  1 root root  2837 Feb 28 22:42 koi-utf
drwxr-xr-x  1 root root  2225 Feb 28 22:42 koi-win
drwxr-xr-x  1 root root  3957 Feb 28 22:44 mime.types
drwxr-xr-x  1 root root  3956 Feb 28 22:46 mime.types.default
drwxr-xr-x  1 root root  2556 Feb 28 22:42 nginx.conf
drwxr-xr-x  1 root root  2556 Feb 28 22:42 nginx.conf.default
drwxr-xr-x  1 root root  636  Feb 28 22:40 scgi_params
drwxr-xr-x  1 root root  636  Feb 28 22:40 scgi_params.default
drwxr-xr-x  1 root root  664  Feb 28 22:40 uwsgi_params
drwxr-xr-x  1 root root  664  Feb 28 22:40 uwsgi_params.default
drwxr-xr-x  1 root root  3610 Feb 28 22:42 win-utf
```

画面 9:
```
SwitchHosts! 0.2.2.1801
生产环境
192.168.1.18 manage.haoke.com
```

画面 10:
```
已切换为“生产环境”。
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
