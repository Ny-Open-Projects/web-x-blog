# 画面线理解：05.docker安装

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\05.docker安装_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:14, 01:32, 01:41, 02:32, 02:35, 02:44, 03:10, 03:31, 04:00, 04:20, 04:28, 06:08, 06:43, 07:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:01:13

1) 这一组画面整体在讲什么（一句话）：
在 CentOS 7 系统上安装和配置 Docker，并设置镜像加速器。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Docker 安装与启动章节的文档，内容为安装前的说明，包括更新 yum 包、安装必要软件包、设置 yum 源等步骤。
画面 2: VMware Workstation 界面，显示 CentOS7 虚拟机的设置页面，准备启动。
画面 3: VMware 启动过程，显示 VMware 标志和启动信息。
画面 4: Windows 文件资源管理器，显示 CentOS7 的安装文件（.vmdk, .vmx, .mdk 等）。
画面 5: Windows 桌面，显示 Docker 安装文档的预览窗口。
画面 6: Windows 桌面，显示“传智播客”和“黑马程序员”的联合出品标志。
画面 7: SecureCRT 登录提示，提示主机的 DNS 解析问题。
画面 8: SecureCRT 登录成功，显示 root 用户的命令行界面。
画面 9: SecureCRT 会话选项，设置记录文件路径。
画面 10: Docker 安装文档，显示安装步骤，包括更新 yum、安装软件包、设置阿里云源。
画面 11: Docker 安装文档，显示安装步骤，包括安装 docker-ce 和验证安装。
画面 12: Docker 安装文档，显示设置 uSTC 镜像的步骤，包括编辑 /etc/docker/daemon.json 文件。
画面 13: SecureCRT 命令行界面，显示空白屏幕，准备执行命令。
画面 14: Docker 安装文档，显示设置 uSTC 镜像和启动 Docker 的步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
(1) yum 包更新到最新
sudo yum update
(2) 安装需要的软件包。yum-util 提供 yum-config-manager 功能，另外两个是 devicemapper 驱动依赖的
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
(3) 设置 yum 源为阿里云
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
(4) 安装 docker
sudo yum install docker-ce
(5) 安装后查看 docker 版本
docker -v

画面 10:
(1) yum 包更新到最新
sudo yum update
(2) 安装需要的软件包。yum-util 提供 yum-config-manager 功能，另外两个是 devicemapper 驱动依赖的
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
(3) 设置 yum 源为阿里云
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
(4) 安装 docker
sudo yum install docker-ce
(5) 安装后查看 docker 版本
docker -v

画面 12:
编辑配置文件：
vi /etc/docker/daemon.json
在该文件中加入如下内容：
{
  "registry-mirrors": ["https://docker-mirrors.ustc.edu.cn"]
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2 Docker安装与启动”，子标题为“2.1 安装Docker”。
画面 10: PPT 标题为“2.1 安装Docker”。
画面 12: PPT 标题为“2.2 设置ustc的镜像”，内容为 uSTC 镜像的介绍和配置文件编辑说明。
画面 14: PPT 标题为“2.2 设置ustc的镜像”和“2.3 Docker的启动与停止”，内容为设置镜像和启动 Docker 的命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
