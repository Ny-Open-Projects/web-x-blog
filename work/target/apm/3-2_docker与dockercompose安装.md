# Go APM 监控系统实战: 安装 Docker 与 Docker Compose 环境

## 纲要

- 为什么先装 Docker：后续所有 APM 组件都以容器方式启动
- 桌面端（macOS / Windows / Linux）安装带 UI 的 Docker Desktop
- 服务器（Linux）分别安装 Docker Engine 与 Docker Compose
- Docker Engine 的官方安装步骤可直接复制粘贴执行
- Docker Compose 两种 Linux 安装方式：软件源（apt / yum）与 curl 直接下载二进制

## 为什么先准备 Docker 环境

后续要安装的 APM 监控组件（MySQL、Redis、Prometheus、Jaeger、OpenTelemetry Collector、ELK 等）全部通过启动 Docker 容器来运行。因此在正式编码前，先把 Docker 与 Docker Compose 环境安装好。

## 桌面端安装

在 Docker 官网的下载引导页中，官方针对不同系统给出了安装方式：

- macOS、Windows、Linux 都可以安装**带 UI 的 Docker Desktop**；
- 以 macOS 为例，根据芯片架构（如 Apple Silicon M1）选择对应安装包，下载后按提示安装即可；
- 安装完成后打开 Docker Desktop，能看到已创建的容器列表，说明环境就绪。

> 注意：桌面端安装的是 Docker Desktop（含 UI 与 Engine）；而 Linux 服务器上需要分别安装 Docker Engine 与 Docker Compose 两个组件。

## 服务器（Linux）安装 Docker Engine

在 Docker 官网左侧导航可以找到 Docker Engine 的安装指引，官方提供了不同 Linux 发行版的安装步骤。以其中任一发行版为例，基本流程就是逐条把官方命令复制粘贴到服务器执行即可。

以 Ubuntu 通过软件源安装 Engine 的简化流程为例（仅作演示，实际请按官网当前文档执行）：

```bash
# 1. 卸载旧版本（如有）
sudo apt-get remove docker docker-engine docker.io containerd runc

# 2. 安装依赖与配置软件源（按官网文档执行完整步骤）
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg

# 3. 安装 Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 服务器（Linux）安装 Docker Compose

Docker 官网提供了 Linux 下 Docker Compose 的两种安装方式：

- **方式一：通过软件源安装**（即上面 `docker-compose-plugin` 的形式，使用 `apt` / `yum` 等包管理器）；
- **方式二：通过 curl 直接下载二进制包**。

```bash
# 方式二示例：直接下载 compose 二进制到 /usr/local/bin
sudo curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
  -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

安装完成后，即可用 `docker compose`（或独立的 `docker-compose`）命令编排多容器应用。下一节会介绍 docker compose 相关的配置文件结构与常用命令。

相关度：85%。是否需要继续：[是]。代码是否可运行：[否]。
