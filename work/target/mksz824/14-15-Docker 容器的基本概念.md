# 14-15-Docker 容器的基本概念

上节课介绍了 images 镜像，这节课来看另一个核心概念：container 容器。images 和 container 的关系，就好比类和实例：images 是 class，container 是实例化出来的对象。

启动任何容器都需要一条特殊命令：docker run。它的常用参数先简单过一遍：

```bash
docker run -d -p 81:80 --name <容器名> <image name>
```

- `-d`：后台运行，不会阻塞整个终端。
- `-p`：端口映射，前面是主机的端口，后面是镜像中服务对应的端口。
- `--name`：给容器起一个自定义名称。
- 最后是镜像名称。如果本地没有这个镜像，docker 会先自动 pull 下来再启动。

这里用 nginx 镜像举例，因为它启动后会自动运行 nginx，并带一个默认 HTML 页面，方便演示。比如把主机 81 端口映射到容器的 80 端口（nginx 在镜像里监听的就是 80，后半段不要改）：

```bash
docker run -d -p 81:80 nginx
```

回车后稍等片刻，终端会输出一长串字符串，说明容器启动成功了。这时访问 localhost:81，能看到熟悉的 nginx 默认页面，第一个容器就算启动完毕。

## 容器的基本操作

```bash
# 查看正在运行的容器
docker ps

# 停止容器（传入对应的容器 ID）
docker stop <id>

# 查看 包括已停止的 所有容器
docker ps -a

# 删除容器
docker rm <id>

# 重新启动一个已停止的容器
docker container start <id>
```

`docker ps` 会显示容器的启动时间、ID 和端口映射关系。停止后再查就看不到它了，但容器本身还在，用 `docker ps -a` 能看到状态为 exited 的记录，此时才能 `docker rm` 删除。`docker container start` 则可以把已停止的容器重新拉起来，不必再用 docker run 重建一遍。

除了命令行，Docker Desktop 的 Dashboard 也提供可视化管理：能看到所有 container 和本地 images，并在界面上直接停止、删除容器。

## 进入容器内部：docker exec

对容器常有定制化需求，比如修改 nginx 的配置。Docker 提供了 `docker exec`，可以像登录远程机器一样进入容器内部操作：

```bash
docker exec -it <id> bash
```

两个选项记住就好：`-i` 保持 STDIN 打开，`-t` 分配一个伪终端（这个很关键），后面的 command 是在容器内部执行的命令。进入后会看到 `root@<容器id>` 这样的提示符，里面有完整的文件系统，就像远程登录了一台机器。比如 `/etc/nginx` 下是 nginx 的配置，`/usr/share/nginx/html` 下是那个默认首页的 index.html，可以 cat 查看，也可以自定义修改后重启容器验证效果。

注意这个镜像装的是最精简版，没有预装 vim。可以先 `apt-get update` 更新，再 `apt-get install vim` 装上，就能在容器内部直接编辑文件了。

到这里，Docker 容器的一系列基本操作就学完了。现在我们可以从 images 启动各种 container 来完成不同的任务，下一步就是定制化启动自己的后端程序，下节课继续探索。
