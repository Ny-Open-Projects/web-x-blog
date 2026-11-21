# 14-26-Docker Build 优化镜像大小

在进入下一部分 GitHub Actions 之前，先聊聊怎样优化 Docker image 的大小和构建速度，这是 Docker 最佳实践之一。本篇先解决大小问题。

`docker images` 看一下：区区一个 opsflow-backend，大小居然达到 1.23GB。它的基础是 `FROM node:16`，而 node:16 这个基础镜像本身就有 905MB。一个 Node 运行环境要九百多兆，有点恐怖：原因就出在基础 node 镜像上，我们在它之上并没有添加多少东西。

## Alpine：小而精的 Linux 发行版

有什么办法减小镜像？去 Docker Hub 看 node 官方镜像的 tag 列表，会发现每个版本都有一个 a 开头的变体，这个单词是 Alpine。看别的镜像（比如 Redis）也能找到它。

Alpine 是什么呢？除了是一家汽车改装公司，还能查到一个叫 alpinelinux.org 的网站，它是一个 Linux 发行版。常用发行版有 Ubuntu、Fedora、Arch Linux 等，Alpine 的口号有三个：Small、Simple、Secure，特点也围绕这三点展开：

- Small（小）：和 CentOS 这类大发行版相比，Alpine 最大特点就是小。它删掉了很多不用的东西，包括默认软件包；选择使用更小的 BusyBox，C 运行库也不用常见的 glibc，而是选择 MUSL。本着选择最精简工具的原则，容量非常小。
- Simple（最简依赖）：把很多内置软件和插件都去掉，还删除了国际化的内容（国际化在 Linux 里也是很大一块）。
- Secure（安全）：有人可能觉得 CentOS 命令多、软件库多，理应更好。事实恰恰相反：Alpine 包含的基础命令足够在 container 中使用，而包含的库越多，隐藏的系统漏洞也越多。从安全层面来说，还真不如 Alpine。

综上，构建 image 更倾向于使用轻量级的发行版。Docker 的场景是应用隔离、分发、部署和资源分配，如果还用大而全的镜像、搞一系列大杂烩的服务，那就和一般虚拟机的用法差不多了，失去了 Docker 设计出来的优势。

## 换用 alpine 版本对比

对比一下大小：自行去 pull alpine 版本，这里选 node:16-alpine。同屏对比，node:16 是 905MB，而 node:16-alpine 只有 110MB，容量缩小得惊人。

修改 Dockerfile，把 `node:16` 换成 `node:16-alpine`。记住原来镜像是 1.23GB，先 `docker rmi` 把它删掉，再重新构建：

```bash
docker build -t opsflow-backend .
```

构建结束后 `docker images` 查看：新镜像只剩 434MB，是一个非常大的进步。

这节课学习了优化大小的第一个秘诀：选用 Alpine 这个 Linux 版本。其他镜像也可以选 alpine 版本试一下。下节课看另一个优化的秘诀。
