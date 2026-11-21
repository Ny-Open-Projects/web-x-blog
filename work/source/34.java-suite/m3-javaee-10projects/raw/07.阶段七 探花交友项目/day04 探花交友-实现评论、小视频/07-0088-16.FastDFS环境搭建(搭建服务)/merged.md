# 16.FastDFS环境搭建（搭建服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\16.FastDFS环境搭建（搭建服务）_【海量资源尽在 666java.com】.mp4
- 时长 4分31秒（音频 271s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来搭建一下我们的fastDFS环境那么我们依然呢是采用着我们这个Docker啊去做一个搭建那么下面我们就动手呢实际的来操作一下那么首先第一个呢就是我们去拉取我们这个fastDFS这个镜像那么我们采用的是它的最新的这个镜像啊去做一个PullLatch那么其实呢我已经就拉取完了只是我们来执行一下这个命令
[00:29] 那么我们等待它执行完成之后啊那么我们就来去创建我们这个容器啊那么首先第一个呢我们创建这个tronker这个容器那我们把它创建出来然后呢下面我们再创建这个storage这个容器那么要注意的是呢在storage这个容器中啊需要指定我们这个tronker的这个server的一个地址那么这个IP地址要改成你自己的那个IP地址
[00:59] 然后呢这个后面是22122是它的默认的端口那么我们就直接来做一个这个创建好那么来创建一下那么并且呢我们来看参数啊那我们指定它的一个group name呢是group1啊这样的一个参数那么这样的话呢我们这个storage这个这个容器呢就创建好了那并且呢其实这两个容器呢就已经跑起来了那么接下来呢我们可以进入到我们这个storage这个容器啊
[01:28] 我们可以去做一些配置那么其实我们保持默认也可以我们可以进去来看一下通过 Docker exe-it然后进入storage然后我们来看一下操作那么进入之后要知道的是我们的fastdfs的配置文件都是在etc下面有一个fastdfs然后这个下面就会有一些相关的一些文件了比如说storage它的一些配置文件
[01:58] 然后还有什么的tranq它的一些配置文件那么OK好那么然后我们还有装完之后它其实容器内部就自带了一个什么呢ngx那么ngx在usern local下面会有一个ngx那么在这个里面就会有一些相关的配置那么在这可以去修改配置我们其实可以来看一下你比如说我们storage它的一些
[02:25] 这个配置默认端口呢是四个8那么我们可以来看一下就进入到刚才我们所说的etc下面的fdfs然后呢这个下面我们来打开一个什么呢打开一个我们这个storage这个配置然后呢我们可以去搜索一下什么呢我们这个portport然后呢搜搜把它走走走嗯好ok再加啊那么可以看到
[02:55] 那么这个端口呢是不是就是我们这个http server这个端口就是四个八对吧它所对应的就是我们NGX的端口那么就是刚才我们所看到的这个目录UserLocal NGX Config下面有一个什么的NGX Config文件那么在NGX Config文件中呢它呢是有一个这个指定的这个server这个配置那么可以看到是在这个位置啊那么可以看到它的这个server所监听的端口呢
[03:24] 就是四个八这个端口然后呢去指定了一些location然后呢我们如果是这个匹配到这个group0到9那么我们往往都是group1然后呢这个呢就去调用什么呢njax fastdvice这样的一个module这样的一个模块去做一个这个反向代理执行就可以了好那么这样的话呢我们其实就可以看到它的一个配置啊那么我们其实把它保持默认呢就可以了
[03:52] 那么我们默认存储路径是在下面就是在根目录下面有个var fdfs然后还有个date下面我们可以来看一下我们就退出了进入到什么var fdfs下面会有一个叫做date目录然后可以看一下这个就是我们的分布式的文件系统所存储的一些目录大概有这么多ok好那么其实到这里我们环境就已经搭建起来了
[04:21] 那么接下来我们就需要对这个环境的做个测试看它环境是否可用OK好那么关于我们这个环境的一个搭建我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 搭建 FastDFS 分布式文件系统，包括拉取镜像、启动 tracker 和 storage 容器、配置 storage 的 http 端口以及配置 Nginx 代理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示终端界面，提示符为 root@itcast:~#，准备执行命令。
画面 2: 显示 Typora 编辑器中的文档内容，标题为“4.1、搭建服务”，内容是使用 Docker 搭建 FastDFS 的步骤，包含拉取镜像、创建 tracker 容器、创建 storage 容器、进入 storage 容器配置 http 端口、配置 Nginx 的代码片段。
画面 3: 显示 Typora 编辑器中的文档内容，与画面 2 内容相同，但光标位于第 15 行，显示 http.server_port=8888。
画面 4: 显示终端界面，执行了 Docker pull delron/fastdfs 命令，成功拉取镜像，接着执行了 Docker run 命令启动 storage 容器。
画面 5: 显示终端界面，执行了 Docker exec -it storage /bin/bash 命令进入 storage 容器，然后执行了 cd /etc/fdfs 命令，显示了目录内容。
画面 6: 显示 Typora 编辑器中的文档内容，与画面 2 内容相同，但光标位于第 17 行，显示了 Nginx 配置文件的代码片段。
画面 7: 显示终端界面，执行了 cd /etc/fdfs 命令，然后执行了 ls 命令，显示了目录内容。
画面 8: 显示终端界面，执行了 cd /etc/fdfs 命令，然后执行了 ls 命令，显示了目录内容。
画面 9: 显示终端界面，执行了 vi storage.conf 命令，然后执行了 ls 命令，显示了目录内容。
画面 10: 显示 Typora 编辑器中的文档内容，与画面 2 内容相同，但光标位于第 17 行，显示了 Nginx 配置文件的代码片段。
画面 11: 显示 Typora 编辑器中的文档内容，与画面 2 内容相同，但光标位于第 17 行，显示了 Nginx 配置文件的代码片段。
画面 12: 显示终端界面，执行了 cd /var/fdfs/data 命令，然后执行了 ls 命令，显示了目录内容。
画面 13: 显示 Typora 编辑器中的文档内容，与画面 2 内容相同，但光标位于第 17 行，显示了 Nginx 配置文件的代码片段。
画面 14: 显示 Typora 编辑器中的文档内容，与画面 2 内容相同，但光标位于第 4 行，显示了创建 tracker 容器的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```markdown
#拉取镜像
Docker pull delron/fastdfs

#创建tracker容器
Docker run -d --network-host --name tracker -v /var/fdfs/tracker:/var/fdfs delron/fastdfs tracker

#创建storage容器
Docker run -d --network-host --name storage -e TRACKER_SERVER=192.168.31.81:22122 -v /var/fdfs/storage:/var/fdfs -e GROUP_NAME=group1 delron/fastdfs storage

#进入storage容器，到storage的配置文件中配置http访问的端口，配置文件在/etc/fdfs目录下的storage.conf。
Docker exec -it storage /bin/bash

#默认的http端口为8888，可以修改也可以配置
# the port of the web server on this storage server
http.server_port=8888

#配置Nginx，在/usr/local/Nginx目录下，修改Nginx.conf文件
#默认配置如下：
server {
    listen 8888;
    server_name localhost;
    location ~ /group[0-9]+/ {
        ngx_fastdfs_module;
    }
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root html;
    }
}
```

画面 6:
```markdown
#创建storage容器
Docker run -d --network-host --name storage -e TRACKER_SERVER=192.168.31.81:22122 -v /var/fdfs/storage:/var/fdfs -e GROUP_NAME=group1 delron/fastdfs storage

#进入storage容器，到storage的配置文件中配置http访问的端口，配置文件在/etc/fdfs目录下的storage.conf。
Docker exec -it storage /bin/bash

#默认的http端口为8888，可以修改也可以配置
# the port of the web server on this storage server
http.server_port=8888

#配置Nginx，在/usr/local/Nginx目录下，修改Nginx.conf文件
#默认配置如下：
server {
    listen 8888;
    server_name localhost;
    location ~ /group[0-9]+/ {
        ngx_fastdfs_module;
    }
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root html;
    }
}
```

画面 10:
```markdown
#创建storage容器
Docker run -d --network-host --name storage -e TRACKER_SERVER=192.168.31.81:22122 -v /var/fdfs/storage:/var/fdfs -e GROUP_NAME=group1 delron/fastdfs storage

#进入storage容器，到storage的配置文件中配置http访问的端口，配置文件在/etc/fdfs目录下的storage.conf。
Docker exec -it storage /bin/bash

#默认的http端口为8888，可以修改也可以配置
# the port of the web server on this storage server
http.server_port=8888

#配置Nginx，在/usr/local/Nginx目录下，修改Nginx.conf文件
#默认配置如下：
server {
    listen 8888;
    server_name localhost;
    location ~ /group[0-9]+/ {
        ngx_fastdfs_module;
    }
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root html;
    }
}
```

画面 13:
```markdown
#创建storage容器
Docker run -d --network-host --name storage -e TRACKER_SERVER=192.168.31.81:22122 -v /var/fdfs/storage:/var/fdfs -e GROUP_NAME=group1 delron/fastdfs storage

#进入storage容器，到storage的配置文件中配置http访问的端口，配置文件在/etc/fdfs目录下的storage.conf。
Docker exec -it storage /bin/bash

#默认的http端口为8888，可以修改也可以配置
# the port of the web server on this storage server
http.server_port=8888

#配置Nginx，在/usr/local/Nginx目录下，修改Nginx.conf文件
#默认配置如下：
server {
    listen 8888;
    server_name localhost;
    location ~ /group[0-9]+/ {
        ngx_fastdfs_module;
    }
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root html;
    }
}
```

画面 14:
```markdown
#拉取镜像
Docker pull delron/fastdfs

#创建tracker容器
Docker run -d --network-host --name tracker -v /var/fdfs/tracker:/var/fdfs delron/fastdfs tracker

#创建storage容器
Docker run -d --network-host --name storage -e TRACKER_SERVER=192.168.31.81:22122 -v /var/fdfs/storage:/var/fdfs -e GROUP_NAME=group1 delron/fastdfs storage
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 标题为“4.1、搭建服务”，内容是使用 Docker 搭建 FastDFS 的步骤。
画面 6: 标题为“4.1、搭建服务”，内容是使用 Docker 搭建 FastDFS 的步骤。
画面 10: 标题为“4.1、搭建服务”，内容是使用 Docker 搭建 FastDFS 的步骤。
画面 13: 标题为“4.1、搭建服务”，内容是使用 Docker 搭建 FastDFS 的步骤。
画面 14: 标题为“4.1、搭建服务”，内容是

