# FastDFS 环境搭建：Docker 三条命令拉起 tracker 与 storage

技术方案把存储押在 FastDFS 上，这一讲动手把环境立起来。搭建方式沿用项目的惯例：Docker。一条镜像里打包了 tracker 与 storage 两个角色，两条 run 命令各起一个容器，剩下的工作全在「看懂配置」上：配置文件在哪、端口是谁的、文件落在哪。环境本身十分钟就能就绪，真正要带走的是每个参数背后的角色分工。

## 先给结论

- 用 Docker 镜像 `delron/fastdfs` 搭建，tracker 与 storage 各起一个容器，`--network=host` 让容器直接用宿主机网络栈。
- storage 容器必须通过环境变量 `TRACKER_SERVER` 指定 tracker 的地址与端口，IP 要换成自己的，`22122` 是 FastDFS 的服务端口。
- 容器内配置文件集中在 `/etc/fdfs` 目录，`storage.conf` 里的 `http.server_port=8888` 与镜像自带的 nginx 监听端口对应。
- 文件访问走 nginx：`/usr/local/nginx` 下的 `nginx.conf` 监听 8888，`location ~ /group[0-9]+/` 交给 `ngx_fastdfs_module` 模块去读文件。
- 数据默认落在 `/var/fdfs/data`，两个容器都通过 `-v` 把宿主机目录挂进容器，文件在容器之外持久保存。

## 一、一条镜像，两个角色

FastDFS 有两类节点：tracker 是调度者，接收客户端请求后挑一台可用的 storage 分配任务；storage 是存储者，文件真正落在这里，还自带 web 服务对外供下载。镜像 `delron/fastdfs` 把两个角色都装好了，启动哪个角色由容器启动参数的最后一段决定。动手前先拉镜像：

```bash
# 拉取 FastDFS 镜像
docker pull delron/fastdfs

# 创建 tracker 容器：host 网络模式，数据目录挂载到宿主机
docker run -d --network=host --name tracker \
  -v /var/fdfs/tracker:/var/fdfs \
  delron/fastdfs tracker

# 创建 storage 容器：TRACKER_SERVER 指向 tracker 的 IP:22122，声明卷组 group1
docker run -d --network=host --name storage \
  -e TRACKER_SERVER=192.168.31.81:22122 \
  -v /var/fdfs/storage:/var/fdfs \
  -e GROUP_NAME=group1 \
  delron/fastdfs storage
```

三处参数值得停下来看。**TRACKER_SERVER 是 storage 的注册地址。** storage 启动后要主动向 tracker 汇报自己的状态，汇报去哪就是去这个地址，`192.168.31.81` 要替换成自己宿主机的 IP，`22122` 是 tracker 的默认服务端口。这个值写错，storage 注册不上，后面上传一律失败。**GROUP_NAME 是卷组名。** FastDFS 按卷组组织 storage，一台或多台同组机器互为备份，这里声明为 `group1`，日后上传返回的路径都以它开头。**`-v` 挂载是数据生命线。** 容器随时可能重建，文件目录挂在宿主机的 `/var/fdfs` 下，容器没了数据还在。

host 网络模式是多留的一个心眼。tracker 与 storage 之间互相通信时上报的是真实 IP 与端口，如果用 Docker 默认的端口映射，节点间拿到的可能是映射前的容器内部地址，通信就对不上了；`--network=host` 让容器直接共享宿主机网络，规避掉这层地址翻译。

## 二、容器里的配置文件都在哪

容器跑起来后进 storage 里看一眼配置，默认值已经可用，看懂它们是为了心里有数：

```bash
# 进入 storage 容器
docker exec -it storage /bin/bash

# FastDFS 的配置文件集中在 /etc/fdfs
cd /etc/fdfs
```

`/etc/fdfs` 目录下摆着 storage 与 tracker 各自的配置文件。打开 `storage.conf`，与文件访问直接相关的是这一行：

```properties
# the port of the web server on this storage server
http.server_port=8888
```

这个 8888 就是 storage 对外的 web 端口，可以改也可以保持默认。镜像里自带了一个 nginx，装在 `/usr/local/nginx` 下，`nginx.conf` 里恰好有一个 server 块把端口对上：

```nginx
server {
    listen       8888;
    server_name  localhost;

    location ~ /group[0-9]+/ {
        ngx_fastdfs_module;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
}
```

这段配置是整个下载链路的钥匙：请求进来时只要路径以 `group` 加数字开头，nginx 就不再找静态文件，而是交给 `ngx_fastdfs_module` 模块反向代理执行，模块拿着路径去 FastDFS 里定位并读出文件。nginx 负责高性能的 HTTP 收发，FastDFS 模块负责文件定位，两端各干专业的事。

## 三、文件落在哪，怎么被访问

storage 的默认存储路径在根目录下的 `/var/fdfs/data`，进目录能看到文件系统初始化出的一整套目录结构，上传的文件就散落其中。把两个角色与端口的关系画成图：

```mermaid
flowchart LR
    C["Java client 与 App"] -->|服务端口 22122 上传调度| T["tracker 容器"]
    T -->|分配节点| S["storage 容器 group1"]
    S -->|落盘| D[("宿主机 /var/fdfs/data")]
    C -->|下载请求 8888| N["storage 内置 nginx"]
    N -->|group 开头路径 交给模块| M["ngx_fastdfs_module"]
    M --> D
```

图里两条链路要分清：上传走 22122，那是 FastDFS 自己的协议端口，tracker 负责调度；下载走 8888，那是 nginx 的 HTTP 端口，模块负责读盘。两个端口属于两个角色，混为一谈是排查环境问题时的头号坑。到这里环境已经立起来了，可用性验证要等 Java client 写完上传代码才算闭环，那是下一讲的内容。

## 常见误区

- **TRACKER_SERVER 原样照抄别人的 IP。** 错例：命令从文档里复制出来直接执行，storage 一直连不上 tracker，上传报连接超时。正解：把环境变量里的 IP 换成自己宿主机的地址，tracker 端口 22122 保持默认。
- **把 8888 当成 tracker 端口。** 错例：Java client 里把 8888 配进 tracker 地址，上传请求发到 nginx 上石沉大海。正解：22122 是 tracker 与 storage 的服务端口，8888 是 storage 上 nginx 的文件访问端口，各走各的链路。
- **启动参数写成 `--network-host`。** 错例：横线与等号混用，Docker 把参数当成未知值，容器仍走默认网桥模式，节点间注册异常。正解：`--network=host` 用等号连接，并在 `docker inspect` 里确认网络模式生效。
- **只建容器不挂目录。** 错例：省掉 `-v` 挂载，文件写进容器可写层，容器一重建所有已上传文件消失。正解：`/var/fdfs` 挂到宿主机，持久化与容量规划都在宿主机盘上做。

## 面试可能被问到的问题

1. 面试官追问：「FastDFS 里 tracker 和 storage 各承担什么职责？」
   答：tracker 是调度中心，只管元信息不存文件，客户端上传或下载先问它，由它按负载挑一台 storage；storage 是存储节点，文件按卷组组织，同组互为备份，并把状态定期上报给 tracker。调度与存储分离，扩容时加 storage 即可，tracker 无状态。
2. 面试官追问：「为什么 FastDFS 部署常用 host 网络模式而不是端口映射？」
   答：storage 向 tracker 注册时上报自己的 IP 与端口，后续客户端与同组节点会拿这个地址直连它。端口映射模式下上报的是容器内部地址，外部根本连不上。host 模式让容器共享宿主机网络栈，上报的就是真实地址，绕开了 NAT 带来的地址失真。
3. 面试官追问：「文件下载为什么要经 nginx 的 ngx_fastdfs_module，而不是直接访问 storage？」
   答：storage 自带的内置 HTTP 服务性能有限，nginx 擅长高并发连接与 sendfile 零拷贝发送静态内容，模块再负责把 group 开头的路径翻译成文件定位。HTTP 层交给 nginx，文件寻址交给 FastDFS 模块，还能顺路挂上防盗链、限速、缓存这些 nginx 生态能力。
4. 面试官追问：「上传返回的 group1/M00/00/00/xxx.jpg 各段是什么含义？」
   答：group1 是卷组名，对应启动时声明的 GROUP_NAME；M00 是 storage 上的虚拟磁盘编号，一块盘一个编号；后面两级目录是按文件名算出的哈希散列，用来把文件均匀摊到目录树下，避免单目录文件数过大拖慢查找；末段是系统生成的文件名，天然防重名。

## 配套资料

- 目标：`materials/code/07/day04 探花交友-实现评论、小视频/day04/学习目标.md`，「独立完成 FastDFS 环境的搭建」对应本讲实操。
- 原型：`materials/code/07/day01 探花交友-项目搭建以及登录完善个人信息/day01/资料/探花交友移动端原型V1.2/小视频.html`，环境服务的最终消费方小视频页面。
- 说明：day04 资料包未解出工程源码，Docker 命令、`storage.conf` 片段与 nginx server 均按课程画面逐字整理（IP 替换为示例值），host 网络模式的补充解释为按主流部署实践加注。
