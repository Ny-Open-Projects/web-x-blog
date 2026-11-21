# 画面线理解：06-环境搭建-CDH环境搭建

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\06-环境搭建-CDH环境搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:19, 02:19, 02:47, 03:57, 05:31, 06:47, 07:32, 08:12, 09:11, 10:22, 11:12, 12:35, 13:40, 14:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:30:26

1) 这一组画面整体在讲如何从零开始搭建一个基于 Docker 和 VMware 的大数据开发环境，包括安装 Docker、配置虚拟机、编写 Dockerfile 和 docker-compose.yml 文件等。

2) 按时间顺序列出每张画面的要点：
画面1：显示了课程资料目录，包含多个视频文件，如“01-项目介绍”、“02-项目目标-业务架构和版本”等。
画面2：显示了“docker使用教程.md”文档的第2.1节“大数据库组件的安装”，其中包含安装Docker依赖的命令：
sudo apt remove docker docker-engine docker.io containerd runc
sudo apt install \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common
以及添加Docker官方GPG密钥的命令：
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
并提示“验证密钥指纹成功”。
画面3：显示了Sublime Text编辑器中的Dockerfile内容，包含多个cp命令用于复制配置文件，以及构建镜像的命令：
docker build -f ./config/ads/Dockerfile -t xc-base
docker build -f ./config/es-head/Dockerfile -t xc-es-head
docker build -f ./config/yapi/Dockerfile -t xc-yapi
画面4：显示了“docker使用教程.md”文档的第2.3节“启动编排”，其中提到执行命令：
docker-compose up -d
并附有“附录1 端口说明”，列出了各服务的端口映射：
# 端口说明
2019 业务报表系统API
3000 es head 端口
9200 es http 端口
9300 es 协议 端口
50070 hadoop fs web
50075 hadoop web file down
50010 hadoop data web
8080 hadoop app web
画面5：显示了“docker使用教程.md”文档的第1.2.1节“从0开始手动搭建”，并展示了“xc”文件夹下的多个虚拟机配置文件，如xc.7z.001、xc.7z.002等。
画面6：显示了“xc”文件夹下的VMware虚拟机配置文件，包括xc.vmware、xc.vmxf、xc.vmx等。
画面7：显示了VMware Workstation的“导入到VMware”界面，提示“导入后会弹出如下窗口”，并显示了虚拟机的硬件配置信息。
画面8：显示了虚拟机登录后的终端界面，提示“xc-online”已登录。
画面9：显示了Sublime Text编辑器中的docker-compose.yml文件内容，包含：
image: elasticsearch:6.4.0 # 指定镜像
Restart: always # 重启策略
container_name: xc-online-es
hostname: xc-online-es
environment:
- discovery.type=single-node
- http.cors.enabled=true
- http.cors.allow-origins*
ulimits:
nproc: 65536
nofile:
soft: 65536
hard: 65536
port:
- "9200:9200"
- "9300:9300"
xc_online_es-ui:
image: xc-es-ui
container_name: xc-online-es-ui
hostname: xc-online-es-ui
ports:
- "9100:9100"
xc_online_vue:
container_name: xc-online-vue
hostname: xc-online-vue
image: node:10.17
working_dir: /opt/xuancheng/vue
restart: always
command: bash -c "npm install && npm run serve"
画面10：显示了“docker使用教程.md”文档的第1.2.2节“VMware虚拟机 - 推荐”，并提示“VMware虚拟机提供了现成可用的环境，解压后导入VMware中，直接启动即可，需要硬盘预留200G左右的空间”。
画面11：显示了“docker使用教程.md”文档的第1.2.3节“注意事项”，并提示“首次启动会弹出如下窗口”，并显示了“xc - VMware Workstation”窗口中的弹窗，提示“我已移动该虚拟机”。
画面12：显示了VMware Workstation的终端界面，显示了网络配置信息，包括：
valid_lft forever preferred_lft forever
eth0: ether 00:0c:29:39:10:80 brd ff:ff:ff:ff:ff:ff Link encap:Ethernet HWaddr 00:0c:29:39:10:80
inet addr:192.168.10.100 Bcast:192.168.10.255 Mask:255.255.255.0
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets 1080877 errors 0 dropped 0 overruns 0 frame 0
TX packets 1080877 errors 0 dropped 0 overruns 0 carrier 0 collisions 0
RX bytes 1080877 (1080877) TX bytes 1080877 (1080877)
画面13：显示了MobaXterm的界面，提示“Start local terminal”，并显示了“xc_docker”会话。
画面14：显示了“docker使用教程.md”文档的第1.2.2节“VMware虚拟机 - 推荐”，并提示“VMware虚拟机提供了现成可用的环境，解压后导入VMware中，直接启动即可，需要硬盘预留200G左右的空间”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
# 输出结果
No LSB modules are available.
Distributor ID: Ubuntu
Description: Ubuntu 18.04.2 LTS
Release: 18.04
Codename: bionic
docker新版本不需要，安装新版本的卸载命令：
sudo apt remove docker docker-engine docker.io containerd runc
安装依赖：
sudo apt install \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common
添加Docker的官方GPG密钥：
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
验证密钥指纹成功。
画面3：
cp config/hbase/conf/hbase-env.sh hbase 1.2.0 cdh5.14.8/conf/hbase-env.sh
cp config/hbase/conf/hbase-site.xml hbase 1.2.0 cdh5.14.8/conf/hbase-site.xml
cp config/hbase/conf/regionservers hbase 1.2.0 cdh5.14.8/conf/regionservers
cp config/kafka/ zookeeper kafka_2.11-2.2.0/conf/server.properties
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
cp config/nifi/To-Hive-nar nifi 1.9.2/lib/To-Hive-nar
