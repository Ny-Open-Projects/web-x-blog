# 06-环境搭建-CDH环境搭建

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\06-环境搭建-CDH环境搭建_【海量资源尽在 666java.com】.mp4
- 时长 14分29秒（音频 869s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来呢学习环境安装这里环境安装呢有两种方式一个是存零开始手动搭建存零开始手动搭建呢就是存安装到可开始以及配置咱们的大数据的各个组件配置完成之后呢进行打包然后进行编排最终呢组成咱们的大数据开发环境第二种呢是使用VMware的虚拟机这种方式呢
[00:30] 咱们在虚拟机里边已经配置好了所有的组件开箱即用直接把虚拟机起起来然后就可以是正常的一个使用了这里呢也是推荐使用这种方式因为呢简单嘛开箱即用通过本节的学习呢需要掌握的是把咱们CDH的基础环境给搭建起来也就是咱们大数据的开发环境给搭建起来不管你是采用第一种还是第二种当然咱们是推荐你是第二种的接下来呢咱们就首先来介绍
[01:02] 存零开始搭建这个呢是存安装Dock开始然后一步一步的配置这里呢采用的是独立的文档咱们来切换到文档文档的位置呢在咱们的资料中Dock目录下的Dock使用文档咱们来切到这里资料中DockDock使用文档这个文档呢详细的介绍了存安装Dock到安装Dock Compose的一些基础的一些安装及配置
[01:38] 安装配置完之后呢,咱们就是大数据组件的安装了,大数据组件的一个配置了,这里大数据的组件在咱们的资料目录中,CDH5.14.0在这个目录下,这个目录就是咱们所有组件的一个配置目录,你手动配置的时候需要将这个上传到你的虚拟机或者是你的服务器上,这里呢咱们安装Docker还有安装Docker Compose,
[02:07] 默认你是已经有了一个虚拟机环境是无版图环境是无版图这里文档中也说明了把之前Dock和Dock Compose配置完成之后配置完成之后只需要把这个CDH5.14.0上传到OPT目录下就即可上传到OPT目录下上传到OPT目录下给这个文件添加可执行权限
[02:36] 就是auto.build.sh咱们来看一下这个文件这个文件呢对咱们的基础配置进行了就是自动化的一个操作你只用执行这个脚本它就会自动的将你配置自动的对文件进行一个打包这个打包指的就是咱们的Docker容器的打包打包完成之后呢咱们就可以进行一个启动编排就是你直接使用Docker Composeup-d的一个操作
[03:07] 将所有的容器给启动起来但是这个地方还有一个还有一个问题是什么呢就是打包过程中它依赖了一些其他的库这个库呢是需要去网上下载的咱们可以看一下这个脚本其实在这个文档里边也有这个脚本build.sh auto build.sh它在打包这些镜像的时候它会有一些第三方的依赖
[03:40] 这个是那个你使用的库下的依赖比如说as hheader还有这些hue这些这些程序它有一些第三方依赖但是打包的时候它必须下载好才行这就造成了咱们在打包的过程中它在打包过程中需要有一个等待的一个时间这个等待时间根据网络来确定的然后第二个需要注意的一个地方呢就是咱们虽然说打包完成之后了
[04:09] 但是咱们在第一次使用的时候还是要做很多的初始化操作比如说Hive需要初始化HDFS需要对目录进行格式化还有HUE也需要初始化这些初始化操作呢根据你电脑的配置也是需要一定的时间的这个经测试呢最快的话是五分钟然后最慢的话这里也没有测到然后是大概的话也就是需要三十分钟左右吧之后的启动就非常快了就是一分钟就行
[04:40] 以上就是咱们从存零开始,然后打包的一步步安装咱们CDH环境的一个操作。
[04:48] 这里需要注意的一个就是咱们的附录1,端口说明。
[04:53] 咱们整个配置是占用了这么多的一个端口,假如说你不知道哪一个组件使用了哪个端口,可以来这里进行一个查看。
[05:05] 接下来咱们切到咱们这个文档,切到咱们的环境那个文档,环境单件文档。
[05:12] 咱们推荐的方式是VMware的虚拟机的这种方式这个步骤咱们会一一的演示虚拟机的目录是在咱们Dock授课资料中Dock目录下的虚拟机目录中咱们来切到咱们的虚拟机目录中你们得到的文件的话应该是没有学成XC这个目录了是没有这个目录了但是有以下这几个文件通过执行
[05:44] xc.exe会解压得到咱们学程那个虚拟机这个目录给大家演示一下为了防止覆盖我先给它改下名这个呢执行它执行xc.exe双击即可它就会告诉你你这个虚拟机要解压到哪个目录默认呢就是你当前的目录我这里边点击这个就是点击这个解压的意思这个时候呢就新建了这个xc目录它呢会
[06:14] 把咱们的虚拟机解压到这个目录里边但是这个时间还是比较久的由于我已经解压好这里就先把它给取消掉点击是就是取消掉这个就把它给删了因为它是不完整的这个还把名字给改下来改回来这个就是咱们解压好的虚拟机解压好的虚拟机咱们直接把它给导入到VMware里边就行这里文档中也有详细的操作
[06:42] 就是你右键这个文件然后使用VMware进行打开咱们这里就直接操作右键XC.VMX这个文件然后右键它进行使用VMware Workstation进行打开打开之后这个界面就是咱们的虚拟机界面可以直接点击开启此虚拟机进行一个启动操作
[07:14] 启动完成之后呢由于咱们Dog Commons已经配置了它是随什么呀它里边的容器是随咱们虚拟机的开机启动的也就是说你只要虚拟机开机了它里边的容器就已经启动这个时候呢刚才点了开机操作它已经启动了但是你们在执行的时候这个地方会有一个注意事情就是会弹出一个窗口会询问你
[07:42] 你是可此虚拟机可能被移动或复制咱们这个地方点击我已移动了此虚拟机它就会进行一个启动操作好我这里边呢已经启动完了咱们呢虚拟机的用户是XC密码是123456使用这个单号密码进行登录这个地方呢XC然后密码是123456登录完成之后呢咱们它需要一个想要的时间
[08:14] 咱们来查看一下使用Docker PS刚才已经说了咱们编排完成之后呢这个虚拟机会随着咱们这个不是啊咱们这个容器会随着咱们的虚拟机启动而启动但是呢有两个不常用的没有启动咱们来看一下这个时候呢切到咱们的这个Docker Compose这个文件里在咱们的CDH 5.14.0的这个目录里边有一个Docker Compose的YML
[08:45] 咱们的配置都是在这个目录里边进行配置的咱们来看一下这个配置的话都起都配置了restart always它这个属性的意思就是说随着Docker引擎启动而启动也就是说只要你虚拟机开机了它就会启动但是下面有两个没有随着虚拟机启动而启动这是其中一个就是yapi的还有一个是esheader这两个
[09:15] 如果你在需要使用这两个文件的时候需要使用这两个容器的时候咱们再进行单独启动就行了这里其实为了方便就是为了来小事咱还可以使用一键启动的方式就是dock,compose,up,d的方式如果你已经启动了虚拟机它告诉你已经启动了如果没有启动了它会帮你启动咱们来看一下真相效果这个需要一个稍微的等待时间
[09:48] 因为咱们大部分虚拟机都随着系统的启动而启动但是有两个可以看到ES的UI还有VIP这两个容器没有配置开机启动所以说你在使用Dark Composeup-d的时候它会自动帮你自动帮你把未启动的给启动起来已经启动的它还是继续使用好这就是咱们使用VMware搭建咱们开发环境的一个方式
[10:16] 也是咱们推荐的方式就是这个推荐的方式到此咱们环境搭建就介绍完了这个地方还有一个注意事项需要大家了解的第一个就是咱们宿主机上也就是说你这个系统你在哪个系统上运行该虚拟机你要保证这个系统上有足够的空间咱们这个虚拟机的话最大是应该是占用200G
[10:46] 也就是说随着你后面的统计分析空间会越来越大如果空间不足的话它可能会报各种莫名其妙的错误第二个呢就是你有足够的内存因为咱们这个地方是把所有的给放到一个虚拟机里边所有的容器放在一个虚拟机里边你可以看一下我这个地方是配置了多少咱们来点设置看一下稍微等一下这个地方的话我内存是给了16G也就是说你在使用的时候
[11:20] 如果你的内存不足可以将这个虚拟机的内存调小一点但是可能遇到的一个问题啥呀你的大数据环境就不正常了所以说也要保证它有足够的内存第二个呢就是咱们刚才已经提到的一点你在执行的时候它会弹出一个窗口我已移动或我已移动该虚拟机或者是呢询问你我复制了该虚拟机就是有这两个选项咱们呢点击我已移动该虚拟机这个时候
[11:49] 点它的一个好处是说它会帮你自动配置虚拟机的IP咱们可以查一下IP-A这个的话它是有很多这是咱们配置了Docker之后它的一个虚拟网卡这个时候它会帮你自动配置虚拟IP如果你点了我已复制的话它并不会帮你自动配置虚拟IP会导致一个问题是你在使用的过程中
[12:17] 你可能你使用终端连咱们虚拟机的时候你并不能连上好以上就是咱们搭建cdh开发环境的所有内容就是通过本节的学习一定要将咱们的cdh环境给搭建起来这个地方有一个这个地方再多说一嘴吧这个地方的话你在这里边执行了执行了IP命令之后你说这么多我想查我本机真实的IP并不能查到
[12:50] 这个地方其实有一个迂回的方式咱们cd到咱们的opt目录下我可以使用ip-a的命令然后把它给查出来这个地方会有一个文件生成到一个1的文件就是把我刚才输入命令的结果写入这个文件里边写入这个文件里边之后呢我就可以使用编辑命令进行一个查看这个时候呢你就可以换行了当前的这个虚拟网卡不是虚拟网卡当前我这个
[13:20] 虚拟机的网卡就是192.1ns32这个IP呢就是192.168.40.129就可以通过使用这个IP来进行连接虚拟机我这里边给大家连一下试试这里呢我就新建一个是SSH地址呢就是192.168.40.这个是多少看一下129
[13:56] 40.129这个地方咱们的用户名就是学成然后密码等会再输他会歧视你这个时候已经开始歧视输入密码了密码就是123456好已经连接进来咱们就可以使用Docker PS来查看一下咱们已经启动的所有容器好以上就是咱们所有内容就是环境搭建CDE是环境搭建的所有内容
[14:26] 好视频就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何从零开始搭建一个基于 Docker 和 VMware 的大数据开发环境，包括安装 Docker、配置虚拟机、编写 Dockerfile 和 Docker-compose.yml 文件等。

2) 按时间顺序列出每张画面的要点：
画面1：显示了课程资料目录，包含多个视频文件，如“01-项目介绍”、“02-项目目标-业务架构和版本”等。
画面2：显示了“Docker使用教程.md”文档的第2.1节“大数据库组件的安装”，其中包含安装Docker依赖的命令：
sudo apt remove Docker Docker-engine Docker.io containerd runc
sudo apt install \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common
以及添加Docker官方GPG密钥的命令：
curl -fsSL https://download.Docker.com/linux/ubuntu/gpg | sudo apt-key add -
并提示“验证密钥指纹成功”。
画面3：显示了Sublime Text编辑器中的Dockerfile内容，包含多个cp命令用于复制配置文件，以及构建镜像的命令：
Docker build -f ./config/ads/Dockerfile -t xc-base
Docker build -f ./config/es-head/Dockerfile -t xc-es-head
Docker build -f ./config/yapi/Dockerfile -t xc-yapi
画面4：显示了“Docker使用教程.md”文档的第2.3节“启动编排”，其中提到执行命令：
Docker-compose up -d
并附有“附录1 端口说明”，列出了各服务的端口映射：
# 端口说明
2019 业务报表系统API
3000 es head 端口
9200 es http 端口
9300 es 协议 端口
50070 Hadoop fs web
50075 Hadoop web file down
50010 Hadoop data web
8080 Hadoop app web
画面5：显示了“Docker使用教程.md”文档的第1.2.1节“从0开始手动搭建”，并展示了“xc”文件夹下的多个虚拟机配置文件，如xc.7z.001、xc.7z.002等。
画面6：显示了“xc”文件夹下的VMware虚拟机配置文件，包括xc.vmware、xc.vmxf、xc.vmx等。
画面7：显示了VMware Workstation的“导入到VMware”界面，提示“导入后会弹出如下窗口”，并显示了虚拟机的硬件配置信息。
画面8：显示了虚拟机登录后的终端界面，提示“xc-online”已登录。
画面9：显示了Sublime Text编辑器中的Docker-compose.yml文件内容，包含：
image: Elasticsearch:6.4.0 # 指定镜像
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
container_name: xc-online-Vue
hostname: xc-online-Vue
image: node:10.17
working_dir: /opt/xuancheng/Vue
restart: always
command: bash -c "npm install && npm run serve"
画面10：显示了“Docker使用教程.md”文档的第1.2.2节“VMware虚拟机 - 推荐”，并提示“VMware虚拟机提供了现成可用的环境，解压后导入VMware中，直接启动即可，需要硬盘预留200G左右的空间”。
画面11：显示了“Docker使用教程.md”文档的第1.2.3节“注意事项”，并提示“首次启动会弹出如下窗口”，并显示了“xc - VMware Workstation”窗口中的弹窗，提示“我已移动该虚拟机”。
画面12：显示了VMware Workstation的终端界面，显示了网络配置信息，包括：
valid_lft forever preferred_lft forever
eth0: ether 00:0c:29:39:10:80 brd ff:ff:ff:ff:ff:ff Link encap:Ethernet HWaddr 00:0c:29:39:10:80
inet addr:192.168.10.100 Bcast:192.168.10.255 Mask:255.255.255.0
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets 1080877 errors 0 dropped 0 overruns 0 frame 0
TX packets 1080877 errors 0 dropped 0 overruns 0 carrier 0 collisions 0
RX bytes 1080877 (1080877) TX bytes 1080877 (1080877)
画面13：显示了MobaXterm的界面，提示“Start local terminal”，并显示了“xc_docker”会话。
画面14：显示了“Docker使用教程.md”文档的第1.2.2节“VMware虚拟机 - 推荐”，并提示“VMware虚拟机提供了现成可用的环境，解压后导入VMware中，直接启动即可，需要硬盘预留200G左右的空间”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
# 输出结果
No LSB modules are available.
Distributor ID: Ubuntu
Description: Ubuntu 18.04.2 LTS
Release: 18.04
Codename: bionic
Docker新版本不需要，安装新版本的卸载命令：
sudo apt remove Docker Docker-engine Docker.io containerd runc
安装依赖：
sudo apt install \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common
添加Docker的官方GPG密钥：
curl -fsSL https://download.Docker.com/linux/ubuntu/gpg | sudo apt-key add -
验证密钥指纹成功。
画面3：
cp config/hbase/conf/hbase-env.sh hbase 1.2.0 cdh5.14.8/conf/hbase-env.sh
cp config/hbase/conf/hbase-site.xml hbase 1.2.0 cdh5.14.8/conf/hbase-site.xml
cp config/hbase/conf/regionservers hbase 1.2.0 cdh5.14.8/conf/regionservers
cp config/Kafka/ ZooKeeper kafka_2.11-2.2.0/conf/server.properties
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

