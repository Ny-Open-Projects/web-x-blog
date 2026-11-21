---
title: "安装Mysql数据库和可视化工具安装使用"
date: 2026-11-17 04:12
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# 安装Mysql数据库和可视化工具安装使用

> **导语**：NestJS 最契合的 ORM 是 TypeORM，而它操作的数据库通常是 MySQL。本文教你用 Docker 容器化一键安装 MySQL 8.0，并搭配 Navicat 可视化工具建库建表，为后面用 TypeORM 连接数据库打好环境基础。

## 前置知识

阅读前建议先看《Nestjs框架课程介绍+适合人员+学后水平》，了解本项目后端用 TypeORM 操作 MySQL 的整体定位。本文偏向环境搭建。

## 正文

### 为什么用 Docker 安装 MySQL

原生直接安装 MySQL 会涉及各种环境变量、服务注册等问题，比较繁琐。本课程采用 **Docker 容器化**安装，一段命令即可拉起一个干净的 MySQL 实例，方便随时重建。

### 第一步：安装 Docker

到 Docker 官网（docker.com）按自己的系统（macOS / Windows / Linux）下载对应版本。安装完成后验证：

```bash
docker -v
```

若正常输出版本号，说明安装成功。

除了命令行，也可以安装 **Docker Desktop**（桌面端）。打开后能看到本机已有的容器（Containers）与镜像（Images），例如课程演示环境里就有 `mysql`、`redis`、`rabbitmq` 等镜像。

常用命令：

```bash
docker images      # 查看本机镜像
docker ps          # 查看正在运行的容器
docker ps -a       # 查看所有容器（含未运行）
```

### 第二步：用 docker run 安装 MySQL 8.0

```bash
docker run -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=xdclass.net168 \
  --name xdclass_nest \
  --restart always \
  -d mysql:8.0
```

参数说明：

- `-p 3306:3306`：把容器内的 3306 端口映射到宿主机的 3306；
- `-e MYSQL_ROOT_PASSWORD=xxx`：设置 root 密码（可自定义）；
- `--name xdclass_nest`：给容器起名；
- `--restart always`：Docker 重启时容器自动重启；
- `-d`：后台运行；
- `mysql:8.0`：镜像及版本。

执行后，用 `docker ps` 或 Docker Desktop 的 Containers 面板即可看到运行中的 MySQL。

### 第三步：用 Navicat 连接并管理

命令行不方便看表结构，推荐可视化工具 **Navicat**。新建一个 MySQL 连接：

- 连接名：自定义；
- 主机：`localhost`；
- 端口：`3306`；
- 密码：上面 `-e` 设置的 root 密码。

连接成功后即可管理数据库。新建数据库右键「新建数据库」，名称如 `xdclass_nest`，字符集一般选 `utf8mb4`，排序规则选对应第一项即可。在数据库里右键「新建表」，用「设计表」添加字段、拖拽排序，保存即可。

Navicat 基础操作：

- 设计表：增删字段、设置类型与排序；
- 新增数据：表中点「+」加一行；
- 删除数据/表：右键操作。

### 后续：用 TypeORM 连接

环境就绪后，下一阶段会通过 **TypeORM** 连接这个 MySQL，并在代码里用 Entity（实体）定义表结构，启动时自动同步到数据库。配套的建库建表 SQL 也会以文件形式提供，可直接导入。

## 小结

- 用 Docker 安装 MySQL 比原生安装省心，一条 `docker run` 即可拉起 8.0 实例。
- 关键参数：`-p` 端口映射、`-e MYSQL_ROOT_PASSWORD` 设密码、`--restart always` 保活、`-d` 后台运行。
- `docker images` / `docker ps` / `docker ps -a` 是日常排查三件套。
- Navicat 负责可视化建库建表，连接 `localhost:3306` 用设置的 root 密码。
- 数据库与表准备好后，下一步由 TypeORM 在代码中以 Entity 形式接管同步。

## 下一步

MySQL 与 Navicat 就绪后，下一步建议接着看《Nest通过TypeORM链接Mysql数据库》，学习如何在 NestJS 工程里配置 TypeORM 并连上刚才装好的数据库。
