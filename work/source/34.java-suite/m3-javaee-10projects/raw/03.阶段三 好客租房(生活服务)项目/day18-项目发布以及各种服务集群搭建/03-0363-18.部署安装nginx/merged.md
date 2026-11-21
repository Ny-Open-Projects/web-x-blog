# 18.部署安装nginx

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\18.部署安装nginx【海量资源尽在 ubkz.com】.mp4
- 时长 3分32秒（音频 213s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来安装一下NGX那么我们呢,选择呢,是在我们的18这个机器上面去做一个安装好,那么我们安装呢,我们先进入这个Hawk这个目录啊然后呢,我们下面呢,创建一个这个NGX这个目录那么NGX呢,之前我们这个其实已经装过了就这样,我把这个就删除掉吧,我们重新来安装一下NGX 1.16,11.6啊,这个目录
[00:29] 那么把它去删除一下那么删除之后呢我们来安装一下那么大家首先肯定需要去做一个解压对吧那么把它解压出来那么解压出来之后呢其实我们这个得到的是一个NJAX的圆满包那么我们需要对圆满做一个编译那么进入这个NJAX这个目录
[00:49] 然后这个下面呢要注意的是那么我们需要安装的时候啊我们首先需要装它的一些依赖但这个依赖呢其实我已经都装过了要不然的话那么你是安装不成功的啊这个要注意一下那么我们稍微可以等待去查看一下它其实这个依赖已经装过了啊那么等到我们这个依赖装好之后啊那我们就需要去对我们的Nginx做一个configuration然后呢再去做一个install啊就可以了OK那么我们稍微等待一下
[01:18] 好那么下面呢我们就来执行一下那么首先我们先去做一个这个config这个处理然后呢我们再去做一个install那么这个呢需要去对我们当前的系统的环境做一些这个检测看一下我们是否能够满足ngx的一个安装的一个这个要求那我们稍微等待一下好那么到这里呢会发现那么是基本上是符合要求的那么所以我们可以去做一个安装了
[01:46] 那我们就去做一个make install去做一个安装它呢会去做一些这个编译之后去做一些安装把我们的一些这个Nginx去安装到一些我们的默认的一些目录中啊那我们稍微等待一下好那么现在呢我们其实可以看到它已经就安装成功了啊那么安装的路径呢会放到把Nginx放到U的local这个下面哎呀OK好那么接下来呢我们可以看一下那么进入到这个
[02:15] 有的local下面ngxsbin这个下面它会有一个ngx这样的一个脚本那么我们就去执行一下好那么现在呢我们可以看到ngx呢就已经跑起来了那我们尝试的来访问一下那么你比如说访问的是19168然后呢1818就OK了好那么这样的话呢我们就可以去做一个访问了那么大家呢这个访问到的是我之前所去
[02:43] 配置的啊部署的这样的一个html那么呃大家那个也可以看到其实我们现在呢ngx就已经跑起来了哎ok好那么我们回去回到上一层目录来看一下这个下面其实是有这个html这样的一个呃这样的一个目录的对吧哎ok好那么我们就呃ngx的安装呢我们就先讲到这里那么我们目前呢就已经把ngx呢就跑起来了那跑起来之后呢后面我们就需要去部署
[03:12] 我们的这个系统以及设置我们一些代理包括我们去可以把我们刚刚的一些这个系统的一些虚拟的一些这个域名呢我们去做一些这样的配置那通过域名就可以实现对我们这个这种接口的一些这种访问OK好那么关于这个Nginx的一个安装那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 服务器上从源码编译安装 Nginx，并配置其运行环境。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档，内容为 Nginx 安装命令和目录结构，提示静态资源和数据库代理需通过 Nginx。
画面 2: SSH 连接终端，显示进入 /haoke 目录，列出其中的文件，包括 Nginx、haproxy、mycat 等。
画面 3: 在 Nginx-1.11.6 目录下，列出源码中的模块文件。
画面 4: 进入 Nginx-1.11.6 目录，列出其内容。
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
#安装Nginx
apt install libpcre3 libpcre3-dev zlib1g-dev openssl libssl-dev
./configure
make install
#启动
cd /usr/local/Nginx/sbin/
./Nginx
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
drwxr-xr-x 2 root root 4096 Feb 28 22:55 Nginx/
drwxr-xr-x 2 root root 4096 Feb 28 22:55 rmq/
```

画面 3:
```bash
Nginx-1.11.6/src/http/modules/ngx_http_autoindex_module.c
Nginx-1.11.6/src/http/modules/ngx_http_browser_module.c
Nginx-1.11.6/src/http/modules/ngx_http_not_modified_filter_module.c
Nginx-1.11.6/src/http/modules/ngx_http_chunked_filter_module.c
Nginx-1.11.6/src/http/modules/ngx_http_dav_module.c
Nginx-1.11.6/src/http/modules/ngx_http_degradation_module.c
Nginx-1.11.6/src/http/modules/ngx_http_empty_gif_module.c
Nginx-1.11.6/src/http/modules/ngx_http_fastcgi_module.c
Nginx-1.11.6/src/http/modules/ngx_http_geo_module.c
Nginx-1.11.6/src/http/modules/ngx_http_gzip_filter_module.c
Nginx-1.11.6/src/http/modules/ngx_http_gzip_static_module.c
Nginx-1.11.6/src/http/modules/ngx_http_headers_filter_module.c
Nginx-1.11.6/src/http/modules/ngx_http_image_filter_module.c
Nginx-1.11.6/src/http/modules/ngx_http_limit_conn_module.c
Nginx-1.11.6/src/http/modules/ngx_http_log_module.c
Nginx-1.11.6/src/http/modules/ngx_http_map_module.c
Nginx-1.11.6/src/http/modules/ngx_http_memcached_module.c
Nginx-1.11.6/src/http/modules/ngx_http_mp4_module.c
Nginx-1.11.6/src/http/modules/ngx_http_random_index_module.c
Nginx-1.11.6/src/http/modules/ngx_http_proxy_module.c
```

画面 4:
```bash
root@itcast02:Nginx# ll
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
root@itcast02:Nginx-1.11.6# ll
total 716
drwxr-xr-x 3 root root 4096 Feb 28 23:36 ./
drwxr-xr-x 7 root root 4096 Feb 28 20:51 ../
drwxr-xr-x 2 root root 4096 Feb 28 23:36 auto/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 conf/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 contrib/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 html/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 man/
drwxr-xr-x 2 root root 4096 Feb 28 23:36 src/
root@itcast02:Nginx-1.11.6# ./configure
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

