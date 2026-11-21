# 画面线理解：07_RabbitMQ安装

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/1.RabbitMQ第一天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\1.RabbitMQ第一天\07_RabbitMQ安装_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:39, 02:13, 03:07, 03:34, 04:38, 05:54, 06:24, 07:07, 07:31, 09:09, 10:24, 10:46, 12:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:34:21

1) 这一组画面整体在讲什么（一句话）：
本组画面讲解了 RabbitMQ 的安装与配置过程，包括环境依赖安装、Erlang 安装、RabbitMQ 服务启动及管理界面访问。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 标题页，内容为“2. RabbitMQ 的安装和配置”，并列出官方地址和安装文档路径。
画面 2: 浏览器打开 RabbitMQ 官网首页，展示其作为开源消息代理的介绍。
画面 3: 浏览器显示 RabbitMQ 官网的“Getting started”页面，展示不同语言的示例和开发工具。
画面 4: 浏览器显示 RabbitMQ 官网的“Downloading and Installing”页面，列出不同平台的安装指南。
画面 5: 浏览器显示 RabbitMQ 官网的“Erlang Version Requirements”页面，说明 Erlang 版本支持政策。
画面 6: Markdown 文档显示“1. 安装依赖环境”和“2. 安装Erlang”部分，列出在线安装依赖的命令和上传的 RPM 包。
画面 7: 终端显示 `ll` 命令输出，列出当前目录下的文件和目录。
画面 8: Markdown 文档显示“1. 安装依赖环境”和“2. 安装Erlang”部分，列出在线安装依赖的命令和上传的 RPM 包。
画面 9: Markdown 文档显示“当前最新版本2.12，需要2.15，所以需要升级glibc”，并列出使用 yum 更新安装依赖的命令和下载 RPM 包的链接。
画面 10: 终端显示 `rpm -ivh erlang-18.3.1.e17.centos.x86_64.rpm` 命令正在执行。
画面 11: 多窗口界面，显示 Markdown 文档、终端、PPT 和浏览器，PPT 标题为“2. RabbitMQ 的安装和配置”，并列出服务管理命令。
画面 12: 终端显示 RabbitMQ 服务配置文件内容，包括内存、磁盘、队列等参数设置。
画面 13: 浏览器地址栏显示 RabbitMQ 管理界面地址，但页面未完全加载。
画面 14: 浏览器显示 RabbitMQ 管理界面的“Overview”页面，包含连接、通道、交换机、队列等统计信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6:
```
yum install build-essential openssl openssl-devel unixODBC unixODBC-devel make gcc gcc-c++ kernel-devel m4 ncurses-devel tk tc xz
```
画面 6:
```
# 安装
rpm -ivh erlang-18.3-1.e17.centos.x86_64.rpm
```
画面 9:
```
sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make -y
```
画面 9:
```
wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-6.x86_64.rpm &
wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-6.x86_64.rpm &
wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-6.x86_64.rpm &
wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-6.x86_64.rpm &
wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-6.x86_64.rpm &
wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-6.x86_64.rpm &
wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-6.x86_64.rpm &
wget http://copr-be.cloud.fedoraproject.org/results/mosquito/myrepo-6.x86_64.rpm &
```
画面 12:
```
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit, [1]]}.
{mod, rabbit, [1]}.
{env, [rabbit
