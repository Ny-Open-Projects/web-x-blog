# 13.nginx部署

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\13.nginx部署_【海量资源尽在 ubkz.com】.mp4
- 时长 7分3秒（音频 423s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好接下来我们来讲解如何用Docker来搭建和部署NJX首先我们第一步应该拉取NJX的镜像NJX镜像这一步就是Docker pull NJX这一步我们是可以省略的因为我给大家提供的镜像已经提供了NJX的镜像了大家可以直接的去使用NJX就可以了
[00:31] 那么 NGIX 镜像拿过来之后下载完成之后接下来我们就来开始创建一个 NGIX 容器Docker run di 杠杠 name 等于 mynginx然后硬设端口80 冒号80后面写 NGIX这是我们的镜像名称好回车
[01:05] 我们在这一句创建的时候我们并没有像上面他们看的部署他们看一样我们去做这种目录的映射对吧那么这种墙我要想部署是不是得用CP命令将我们的进程一面拷贝到我们的ngs里对吧就是说这时候我们部署就需要拷贝了我们现在把容器创建好之后接下来我们可以测试一下
[01:34] 这时候我们会发现我们能看到 Nginx 的一个欢迎页面是吧这就表示我们 Nginx 的容器已经安装成功了那么接下来我们要考虑这个问题就是我怎么样才能把我们的静态页面部署到 Nginx里静态页面部署到 Nginx里我们现在给大家提供一套测试用的静态页面在这有一个 dist这里有一个
[02:03] 十字方的这么一个整个网站的这么一个这么一个页面我现在就想把这个页面给他传上去那么怎么做呢首先我们应该把第四的这个整个这个目录上传到我们的这个速度机上因为是传一个目录所以说我要写杠二地板setup下的dist好现在已经上传成功了我们来看一下
[02:40] 看一下现在已经有这个文件夹了那么有这个文件夹之后那么问题来了我怎么样才能把这个文件夹拷贝到哪一个目录下呢这时候我们就得需要去进到容器里去看一下是吧进到容器里看一下那这时候就是ESEC-IT然后接下来就是myngx-bin-bash好进到容器之后呢我们来看一下现在这个这个结构
[03:11] 我现在可以告诉大家在哪在这个这个NJX安装的ETC目录下了我们可以看到ETC那么ETC目录呢这里头有一个NJX看了吗这个是他安装的这个位置了NJX那么NJX下面大家看是不是就是一个NJX比较典型的一个结构啊那我们现在看这里有一个NJX的config那很显然它是什么
[03:41] 它是我们njigs的它的一个配置文件我们用开的命令然后把它打开来查看一下内容这时候就会发现这个内容实际上是什么呢是只是配置基本的一些配置然后这里有一句叫include啥意思导入也就是说它这里头需要导入另外的一些配置文件配置文件的这是etc下的njigs下的config.d
[04:11] 下的新点config也就是说我们可以把配置分别写的不同很多配置文件中通过这个include导入这样可以实现我们配置文件也可以实现配置文件的一个模块化方便之后的维护那么所以说咱们现在要做的事就是要怎么进到config.d这个文件夹看一下这里头有一个default.config我们看一下这里其实就是配置了一个
[04:41] server对吧配这个server那么我们从这个配置中很容易就能找到什么找到我们这里的一个目录rootroot是usrshare下的index下的HTML我们现在就可以看一下这个是不是我们的我们会找到那个辉映页面的目录这里有两个文件一个是index.hml一个是50x.
[05:12] HTML就是我们所看到的这个画用页好了那么把这个我们也知道了说这个具体的位置是在这个位置那怎么办呢我现在退出退出之后我们需要把这个dist文件夹下的所有内容都拷贝到我们的HTML这个目录那这一时候我应该怎么办呢我告诉大家最好的方式是这样写就是我们可以先把这个dist改个名改成HTML
[05:44] 这时候我们可以把html目录拷贝到这一级目录就是拷贝到usr share ngix目录下这样一来不就把这个html目录整个覆盖了吗那这时候我们就写命令cp什么cp html然后呢就是我们的myngix 号usr share ngix好
[06:16] 那么经过这样一个拷贝这时候我们就把 hml 整个跑考的 index 目录下了就会把它原来的覆盖,覆盖之后咱们现在再次来进行测试来看一下到底能不能显示出来来看一下我们现在已经把整个的静态原型就给 boost 到我们的 index 里了这是我们说的 index 环节
[06:51] 这个环节主要是练习端口映射以及我们的CP命令的使用这是关于index部署我们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 Nginx 服务，并通过配置文件实现对静态资源和 PHP 脚本的代理转发。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 Docker 容器运行命令：`Docker run -d --name=mytomcat -p 8080:8080 Tomcat:7-jre7`
- 展示了 Docker 镜像列表，包含 Tomcat、mysql、Nginx 等镜像。
- 展示了容器运行状态，包括 Tomcat、mysql、Nginx 等容器。

画面2：
- 展示了 Docker 镜像列表，包含 Tomcat、mysql、Nginx 等镜像。
- 展示了容器运行状态，包括 Tomcat、mysql、Nginx 等容器。
- 展示了执行 `Docker run -d --name=mynginx -p 8080:8080 Nginx` 命令。

画面3：
- 展示了 Nginx 默认欢迎页面，确认 Nginx 服务已成功安装并运行。

画面4：
- 展示了本地文件夹结构，包含 HTML 文件、CSS 文件、图片等静态资源。

画面5：
- 展示了“十次方”网站的首页，包含“JAVA从零构建到大型电商项目实战”等宣传内容。

画面6：
- 展示了 Docker 镜像列表，包含 Tomcat、mysql、Nginx 等镜像。
- 展示了容器运行状态，包括 Tomcat、mysql、Nginx 等容器。
- 展示了执行 `Docker run -d --name=mynginx -p 8080:8080 Nginx` 命令。

画面7：
- 展示了通过 `scp` 命令将文件从本地传输到远程服务器的过程，传输的文件包括 `plugins/` 目录下的多个 JS 文件。

画面8：
- 展示了执行 `Docker run -d --name=mynginx -p 8080:8080 Nginx` 命令。
- 展示了执行 `Docker cp html /usr/share/Nginx/html` 命令，将本地 HTML 文件复制到 Nginx 服务的根目录。

画面9：
- 展示了 Nginx 配置文件 `/etc/Nginx/Nginx.conf` 的部分内容，包括 worker_processes、events、http、server、location 等配置项。

画面10：
- 展示了一个空白的浏览器页面。

画面11：
- 展示了 Nginx 配置文件 `/etc/Nginx/conf.d/default.conf` 的部分内容，包括 error_page、location、proxy_pass、fastcgi_pass 等配置项。
- 展示了执行 `Docker cp html /usr/share/Nginx/html` 命令，将本地 HTML 文件复制到 Nginx 服务的根目录。

画面12：
- 展示了浏览器中的搜索结果页面，包含多个网站链接。

画面13：
- 展示了“十次方”网站的首页，包含“JAVA从零构建到大型电商项目实战”等宣传内容。

画面14：
- 展示了 Docker 部署文档，包含“4.3 Nginx部署”、“4.4 Redis部署”、“5 迁移与备份”等章节标题。
- 展示了 Nginx 部署的步骤，包括“拉取镜像”、“创建Nginx容器”等。
- 展示了 Redis 部署的步骤，包括“拉取镜像”、“创建容器”等。
- 展示了“5.1 容器保存为镜像”等章节标题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
Docker run -d --name=mytomcat -p 8080:8080 Tomcat:7-jre7
```

画面2：
```bash
Docker run -d --name=mynginx -p 8080:8080 Nginx
```

画面6：
```bash
Docker run -d --name=mynginx -p 8080:8080 Nginx
```

画面8：
```bash
Docker run -d --name=mynginx -p 8080:8080 Nginx
Docker cp html /usr/share/Nginx/html
```

画面9：
```Nginx
user Nginx;
worker_processes 1;

error_log /var/log/Nginx/error.log warn;
pid /var/run/Nginx.pid;

events {
    worker_connections 1024;
}

http {
    include /etc/Nginx/mime.types;
    default_type application/octet-stream;

    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for";'

    access_log /var/log/Nginx/access.log main;

    sendfile on;
    tcp_nopush on;
    keepalive_timeout 65;

    include /etc/Nginx/conf.d/*.conf;
}
```

画面11：
```Nginx
# redirect error pages to the static page /50x.html
error_page 500 502 503 504 /50x.html;
location = /50x.html {
    root /usr/share/Nginx/html;
}

# proxy the PHP scripts to Apache listening on 127.0.0.1:80
location ~ \.php$ {
    proxy_pass http://127.0.0.1:80;
}

# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
location ~ \.php$ {
    fastcgi_pass 127.0.0.1:9000;
    fastcgi_index index.php;
    fastcgi_param SCRIPT_FILENAME /scripts$fastcgi_script_name;
    include fastcgi_params;
}

# deny access to .htaccess files, if Apache's document root
# concurs with Nginx's one
location ~ /\.ht {
    deny all;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
- PPT 标题：“4.3 Nginx部署”、“4.4 Redis部署”、“5 迁移与备份”。
- PPT 内容：
  - “4.3 Nginx部署”：
    - (1) 拉取镜像：`Docker pull Nginx`
    - (2) 创建Nginx容器：`Docker run -d --name=mynginx -p 8080:8080 Nginx`
  - “4.4 Redis部署”：
    - (1) 拉取镜像：`Docker pull redis`
    - (2) 创建容器：`Docker run -d --name=myredis -p 8080:8080 redis`
  - “5 迁移与备份”：
    - “5.1 容器保存为镜像”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

