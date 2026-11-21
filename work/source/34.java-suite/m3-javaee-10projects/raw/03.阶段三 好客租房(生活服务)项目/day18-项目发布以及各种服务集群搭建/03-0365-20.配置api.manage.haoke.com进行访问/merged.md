# 20.配置api.manage.haoke.com进行访问

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\20.配置api.manage.haoke.com进行访问【海量资源尽在 ubkz.com】.mp4
- 时长 1分30秒（音频 90s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们把这个API这个Manager的配置呢也给它配置一下那么这个呢就非常类似了那么我们只需要在Nginx中呢去配置这样的一个配置然后它指向到是我们的1.7,18080就可以了好嘞,那么我们把这个呢来配置一下那么把它拷贝一下然后呢我们进入到我们这个Config下面去找到Nginx配置然后呢下面我们在这个位置就是我们重新再去添加一个这个Server
[00:29] 那么也就相当于我们添加两个这个serve啊同样监听的都是80这个端口那么它是api这个这个域名啊api.managerhawk.com然后它所指向的是这个1.718080好那么保存退出一下就OK了然后呢我们做一个reload然后呢在我们这个本机呢去做一个虚拟域名的一个映射然后呢这个改成这个是api啊api
[00:56] 那么api.manager.com同样也是指向到18由这个18这个机器呢再去指向到这个171去啊那么我们可以去测试一下那么我们点击这个OK去生效一下然后呢我们这个例子注意这个例子是直接去访问的17那么现在呢我可以通过这个域名去做一个访问了那么它得到的效果呢是一样的这个大家能够理解吗就是我们通过域名去访问我们这个接口服务哎OK好嘞好那么这个呢就是
[01:24] 我们刚刚所写的通过API域名去访问我们的后台的一个接口服务

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过修改 Nginx 配置文件来配置两个虚拟主机（manage.haoke.com 和 api.manage.haoke.com），并验证配置效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在终端中列出 /etc/Nginx/conf.d/ 目录下的配置文件，准备编辑 Nginx.conf。
画面 2: 进入 /etc/Nginx/conf.d/ 目录，准备编辑 Nginx.conf。
画面 3: 显示 Nginx.conf 文件的开头部分，包含 user、worker_processes、events 和 http 块。
画面 4: 显示 server 块，配置了 listen 80、server_name manage.haoke.com，并设置了 proxy_pass 和 root。
画面 5: 在 server 块中添加了新的 server_name api.manage.haoke.com。
画面 6: 与画面 1 相同，列出 /etc/Nginx/conf.d/ 目录下的配置文件。
画面 7: 启动 SwitchHosts! 工具，切换到生产环境，显示 manage.haoke.com 的 IP 地址。
画面 8: 与画面 6 相同，列出 /etc/Nginx/conf.d/ 目录下的配置文件。
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
#pid logs/Nginx.pid;

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
drwxr-xr-x  1 root root  2556 Feb 28 22:42 Nginx.conf
drwxr-xr-x  1 root root  2556 Feb 28 22:42 Nginx.conf.default
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
drwxr-xr-x  1 root root  2556 Feb 28 22:42 Nginx.conf
drwxr-xr-x  1 root root  2556 Feb 28 22:42 Nginx.conf.default
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

