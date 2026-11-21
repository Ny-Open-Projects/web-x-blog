# 画面线理解：18.部署安装nginx

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\18.部署安装nginx【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:16, 00:41, 00:55, 01:20, 01:30, 01:36, 01:47, 02:11, 02:23, 02:43, 02:56, 03:04, 03:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:58:33

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 服务器上从源码编译安装 Nginx，并配置其运行环境。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档，内容为 Nginx 安装命令和目录结构，提示静态资源和数据库代理需通过 Nginx。
画面 2: SSH 连接终端，显示进入 /haoke 目录，列出其中的文件，包括 nginx、haproxy、mycat 等。
画面 3: 在 nginx-1.11.6 目录下，列出源码中的模块文件。
画面 4: 进入 nginx-1.11.6 目录，列出其内容。
画面 5: 执行 ./configure 命令前，显示已解压的依赖包。
画面 6: 执行 ./configure 命令，显示系统检查信息，确认 GCC 版本。
画面 7: ./configure 命令继续执行，检查系统库和功能。
画面 8: ./configure 命令完成，显示配置摘要，包括路径和日志文件。
画面 9: 执行 make 命令，同时在 Typora 中查看文档。
画面 10: 执行 make 命令后，显示编译完成，列出 bin 目录下的可执行文件。
画面 11: 执行 make 命令后，显示编译完成，列出 bin 目录下的可执行文件。
画面 12: 进入 html 目录，准备测试。
画面 13: 浏览器访问 http://192.168.1.18/，显示 404 页面。
画面 14: 显示 Typora 文档，内容为项目打包的域名规划和 Spring Boot 打包配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```bash
#安装nginx
apt install libpcre3 libpcre3-dev zlib1g-dev openssl libssl-dev
./configure
make install
#启动
cd /usr/local/nginx/sbin/
./nginx
```

画面 2:
```bash
root@itcast02:conf# cd /haoke/
root@itcast02:haoke# ll
total 28
drwxr-xr-x 7 root root 4096 Feb 28 20:51 ./
drwxrwxr-x 5 root root 4096 Feb 28 17:28 ../
drwxr-xr-x 2 root root 4096 Feb 28 11:52 haproxy/
drwxr-xr-x 2 root root 4096 Feb 28 22:55 mycat/
drwxr-xr-x 2 root root 4096 Feb 28 22:55 nginx/
drwxr-xr-x 2 root root 4096 Feb 28 22:55 rmq/
```

画面 3:
```bash
nginx-1.11.6/src/http/modules/ngx_http_autoindex_module.c
nginx-1.11.6/src/http/modules/ngx_http_browser_module.c
nginx-1.11.6/src/http/modules/ngx_http_not_modified_filter_module.c
nginx-1.11.6/src/http/modules/ngx_http_chunked_filter_module.c
nginx-1.11.6/src/http/modules/ngx_http_dav_module.c
nginx-1.11.6/src/http/modules/ngx_http_degradation_module.c
nginx-1.11.6/src/http/modules/ngx_http_empty_gif_module.c
nginx-1.11.6/src/http/modules/ngx_http_fastcgi_module.c
nginx-1.11.6/src/http/modules/ngx_http_geo_module.c
nginx-1.11.6/src/http/modules/ngx_http_gzip_filter_module.c
nginx-1.11.6/src/http/modules/ngx_http_gzip_static_module.c
nginx-1.11.6/src/http/modules/ngx_http_headers_filter_module.c
nginx-1.11.6/src/http/modules/ngx_http_image_filter_module.c
nginx-1.11.6/src/http/modules/ngx_http_limit_conn_module.c
nginx-1.11.6/src/http/modules/ngx_http_log_module.c
nginx-1.11.6/src/http/modules/ngx_http_map_module.c
nginx-1.11.6/src/http/modules/ngx_http_memcached_module.c
nginx-1.11.6/src/http/modules/ngx_http_mp4_module.c
nginx-1.11.6/src/http/modules/ngx_http_random_index_module.c
nginx-1.11.6/src/http/modules/ngx_http_proxy_module.c
```

画面 4:
```bash
root@itcast02:nginx# ll
total 716
drwxr-xr-x 3 root root 4096 Feb 28 23:36 ./
drwxr-xr-x 7 root root 4096 Feb 28 20:51 ../
drwxr-xr-x 2 root root 4096 Feb 28 23:36 auto/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 conf/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 contrib/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 html/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 man/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 src/
```

画面 5:
```bash
Preparing to unpack .../openssl_1.0.2g-ubuntu4.15_amd64.deb
Unpacking openssl (1.0.2g-ubuntu4.15) over (1.0.2g-ubuntu4.14) ...
Processing triggers for libc-bin (2.3.2-ubuntu10) ...
Setting up libssl1.0.0:amd64 (1.0.2g-ubuntu4.15) ...
Setting up openssl (1.0.2g-ubuntu4.15) ...
Processing triggers for libc-bin (2.3.2-ubuntu10) ...
```

画面 6:
```bash
Setting up openssl (1.0.2g-ubuntu4.15) ...
Processing triggers for libc-bin (2.3.2-ubuntu10) ...
root@itcast02:nginx-1.11.6# ll
total 716
drwxr-xr-x 3 root root 4096 Feb 28 23:36 ./
drwxr-xr-x 7 root root 4096 Feb 28 20:51 ../
drwxr-xr-x 2 root root 4096 Feb 28 23:36 auto/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 conf/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 contrib/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 html/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 man/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 src/
root@itcast02:nginx-1.11.6# ./configure
checking for OS ...
checking for C compiler ... found
+ using GNU C compiler
+ gcc version: 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1-16.04.1)
```

画面 7:
```bash
checking for sys/vfs.h ... found
checking for nobody group ... not found
checking for nogroup group ... found
checking for poll() ... found
checking for queue ... not found
checking for crypt() ... not found
checking for F_READAHEAD ... found
checking for O_DIRECT ... found
checking for O_NOCACHE ... not found
checking for directio() ... found
checking for statfs() ... found
checking for dlopen() in Libdl ... found
checking for sched_yield() ... found
checking for SO_REUSEPORT ... found
checking for SO_ACCEPTFILTER ... not found
checking for SO_BINDANY ... not found
checking for IP_BIND_ADDRESS_NO_PORT ... found
checking for IP_TRANSPARENT ... found
checking for IP_BINDANY ... not found
checking for IP_RECVDSTADDR ... not found
```

画面 8:
```bash
Configuration summary
