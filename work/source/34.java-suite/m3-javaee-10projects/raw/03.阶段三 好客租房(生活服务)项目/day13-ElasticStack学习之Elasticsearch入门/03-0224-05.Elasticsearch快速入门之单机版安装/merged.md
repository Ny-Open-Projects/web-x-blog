# 05.Elasticsearch快速入门之单机版安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\05.Elasticsearch快速入门之单机版安装【海量资源尽在 ubkz.com】.mp4
- 时长 10分40秒（音频 641s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来安装Elite Search那么首先呢我们先去做一个下载那么下载呢我们点击这个Download这个按钮那我们来看一下好那么打开这个Download这个页面的话我们可以看到在这个位置呢它的版本最新的是不是就6.5.4然后呢我们去选择下载呢我们一般选择这个就可以了因为我们一般都是在Linux平台去做一个安装
[00:27] 那么如果你使用的是windows平台的话那么点击它下载就可以了当然了其实我们现在也不需要下载了那么我已经下载好了在资料中呢有那么接下来呢我们就来看一下这个安装那么首先我们要讲的是一个单机版的一个安装OK那么首先我们第一步啊安装之前要记住啊要先做第一步这个操作就是我们添加一个这个ELsearch啊这样的一个用户给我们这个系统添加这样的一个用户
[00:56] 那么为什么要去做一个添加呢原因是elixir它不允许或者不支持我们使用这个root用户去运行去启动elixir它是不支持的原因是认为使用这个root用户不安全OK权限太大了权限太大了OK好那么下面我们来看一下那么我这个机器已经就创建好这个用户了那么没有去创建这个用户的同学那么输入一下这个命令就创建就可以了
[01:26] 然后呢我们就可以去做一个减压了那么怎么减压呢来看一下那么这样我先去切换到我这个Electro Search这个用户然后呢我进入根目录下面的一个号客然后呢这个下面呢它有一个这个压缩包压缩包然后呢我们创建一个目录啊就叫ES创建一个ES这个是没有权限啊我还得去退出啊
[01:55] 然后我现在这个里面先创建好吧叫做ES然后我把这个压缩包我解压这个压缩包到这个ES下面跟目录下面的ES当前目录ES下面做一个这样的一个解压那么解压完成之后那么我们就可以去更改一下它的一个这个目录的一些这个所属可以解压完了那么我们可以看到那么
[02:24] 他所有的所有的这个用户是不是都所属是root对不对那我们要去更改一下他的一个所属chchwin然后呢做一个elsearch然后呢来个冒号冒号刚刚可能有点卡然后呢来一个elsearch然后呢来个es对吧然后呢大写的r做一个做一个这个d归
[03:00] 然后我们进入ES下面可以看到是不是所有已经就变成什么了说变成ELSEARCH然后我们再去切换到目录然后进入根目录下面的浩克下面的ES下面然后我们再去进入ELSEARCH6.5.4目录到这我们就已经成功的就解压好了对吧好嘞那么接下来我们继续往下面看
[03:28] 那么下面呢我们需要去修改它这个配置文件那么我们需要去进入这个config然后呢打开一个叫做elag searchYaml文件然后在这个里面我们要找到一个http做一个搜索啊找到这个http在下面啊在这个位置在这就是network的一个这个host那么要注意它默认的会读取你的本机那么由于呢我现在装的是虚拟机对吧
[03:56] 那我就需要设置我这个虚拟机的一个IP地址那么把它copy过来那么我这个呢就是要需要1655.185其实就是我上面这个地址啊就它好嘞好那么大家这个地址要注意啊这个地址要跟着你的这个地址来啊哎OK好嘞那么这是第一个我们需要所做的一个配置那么接下来呢我们就需要啊我们就需要去设置两个啊还需要设置两个这个配置那么第一个配置呢是
[04:26] 在我们的这个在config下面有一个配置呢叫做jvmjvm的一个配置那么可以看到在这个位置呢它默认的是这个初始的内存和最大内存都是一气对吧那么对于我们做测试而言呢其实用不了这么大因为我们的测试机器的这个资源没有那么大所以我们设置128兆就可以了OK好保存退出
[04:55] 这是我们的这样的这个配置啊第三个配置呢就需要去修改一下我们单个进程中的一个最大限程数那么我们为什么要去修改这个配置呢我们来简单的说一下原因是呢在我们之前的这个配置文件中啊那么我们是不是把这个network的host改成了我们这个地址那么要注意的是在electsus中呢如果我们这个network的这个host它不是localhost
[05:24] 或者也不是这个127 0.0.1的话那么就会认为我们这个当前所运行的这个electros的环境它是一个生产环境生产环境打了所对应的它就是一个这个我们的开发环境那么对于环境的要求是比较高的因为他认为我们这个生产环境那么自然对我们的生产环境的要求是比较高的我们的测试环境的不一定能够满足所以一般情况下我们需要去修改两个配置
[05:53] 那么前面我们是不是已经修改过这个配置对吧哎呦给把它改小了那么接下来我们来修改这个配置这个配置呢是我们在服务器就是在Linux这个系统中它的一个单个进程中的一个最大线程数的一个设置那么我们去给它做一个这样的一个设置那么我们打开来看一下那么我在这个位置已经就修改好了那么在最下面把它添加进来保存退出就可以了这个修改也比较简单OK
[06:23] 当我们把这个修改完成之后呢下面的我们就可以去启动啊这个服务了那么怎么样启动呢我们来看一下那么我们cd点点回去然后进入到B目录在B目录下面的我们去执行这个脚本去做一个启动就叫什么呢Elect search回车那么这样这个启动的是一个前台的一个启动那么如果我们想要后台启动的话那么后面加一个杠D就可以了
[06:49] OK那么大家呢我建议大家在第一次启动的时候呢先通过我们这个前台的启动那么可以观察一下它的一个日志OK好那么我们等待它的一个启动好那么现在这个服务呢就跑起来了我们来看一下那么当我们看到这么几个关键字呢就服务就OK了啊那么首先第一个呢它在starting之间启动然后呢它要去做一些我们这种这个地址和端口的一个绑定那么首先第一个端口呢是9300
[07:18] 然后下面在这个位置还有一个是9200那么当然我们可以看到这个IP地址和这个IP地址是不是刚刚我们所配置的那个IP地址OK那么看到这个基本上就差不多了然后下面当我们看到这个study的那么就代表着我们这个服务它就已经跑起来了那么接下来我们就需要来验证一下我们这个服务它究竟有没有成功的跑起来我们来看一下怎么样去做一个验证那么我们就需要去
[07:46] 访问一个地址就是这个地址1721655185这个9200这个地址那我们尝试访问一下172然后呢不185下面的9200走当我们看到有这样的一个信息的时候呢那就说明我们的elite设置服务呢就已经跑起来了那我们可以看到他的一些这个版本信息啊包括他的一些这个当前这个名字啊然后呢一些cluster的一个名字啊等等
[08:16] 然后呢还有他的一些这个就是lucent的这个信息使用的是7.5.0这样的一个信息那么OK那么这个呢就是我们其实看到他的第一个这个接口服务啊就是展现他的一个这个信息啊展现他的一个信息那么我们也可以通过我们那些这个rest client的工具是不是去做一些这个使用啊那么把这个拷贝过来然后呢我们把它丢到这然后呢我们去做一个
[08:45] 做一个我们这个盖的请求啊就盖的请求然后呢走好嘞那么同样是不是可以看到相同的这个效果啊那么后面呢我们也会基于这样的工具呢去做一些这个演示啊OK好嘞那么看到这个信息那就说明我们已经是启动起来了那么接下来有个问题呢就是我们又该如何啊去做停止呢停止我们这个服务那么停止服务呢应该这样来做啊
[09:12] 那么比如说我们再我们再来开一个再来开一个那么在这个里面那么我们再去做一个什么我们再去做一个查询我先把这个清掉然后做一个查询就是什么JPS去查询我们的一个进程那么可以看到这个是不是就是Electro Search的一个进程那么我们就要通过一个Q然后去给它指定一个进程就可以了不要加那个-9-9太暴力了
[09:43] 然后呢走那么可以看到这个进程其实就已经你可以看到他正在stop去停止然后呢就close的就做一个关闭了啊那么这个是一个比较平滑的一个关闭那么通过通过这样的一种形式呢就可以去把我们这个服务就停掉了当然了我现在需要把这个服务跑起来原因是我后面是不是需要做一些测试啊做一些这个学习那么OK那么先不跑了吧这个这个是我们的这样的一个
[10:11] 安装那么下面我们还需要通过这个DAO卡去做个安装那我们就先不做一个运行了那么大家我给大家演示一下那么如果是我们通过一个后面加一个参数杠D的话那么就代表了它是在后台运行那么可以看到我们现在看不到它的整个输出对不对那么但是它的进程已经是有了这个elastic的一个进程了那么OK这就是一个后台的一个启动大了这个就是我们整个讲解的一个单机版的一个安装好那么这个单机版的一个安装我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中手动解压、配置并启动 Elasticsearch 6.5.4 单节点服务，包括修改配置文件、调整 JVM 参数和系统内核参数，并通过 REST API 验证服务状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Elasticsearch 官网的 RESTful API 示例代码，其中包含 `Resilient->search($params);`。
画面 2: 在终端中执行 `rm -rf *` 清理目录，然后列出目录内容，显示 `Elasticsearch-6.5.4.tar.gz` 文件，接着执行 `rm -rf es` 删除旧目录。
画面 3: 列出 `Elasticsearch-6.5.4` 解压后的目录结构，包含 `bin`、`modules`、`plugins` 等子目录。
画面 4: 在终端中执行 `cd es` 进入目录，然后执行 `chown -R Elasticsearch:Elasticsearch es` 修改目录权限。
画面 5: 在 PDF 文档中显示单机版安装步骤，包含命令：`useradd Elasticsearch` 和 `tar -xvf Elasticsearch-6.5.4.tar.gz -C /haoke/es/`。
画面 6: 在终端中编辑 `Elasticsearch.yml` 配置文件，设置 `network.host: 172.16.55.185` 和 `http.port: 9200`，并提示 `E138: Can't write viminfo file /viminfo`。
画面 7: 在终端中编辑 `/etc/sysctl.conf` 文件，显示内核参数配置，如 `net.ipv4.conf.all.rp_filter=1`。
画面 8: 在终端中进入 `bin` 目录，列出可执行脚本，然后执行 `./Elasticsearch` 启动服务。
画面 9: 在浏览器中访问 `172.16.55.185:9200`，显示 Elasticsearch 的响应信息。
画面 10: 在 Advanced REST Client 中构造 POST 请求，发送 JSON 数据：`{"email": "xxx", "password": "xxx"}`。
画面 11: 在终端中查看 Elasticsearch 启动日志，显示 `high disk watermark [90%] exceeded` 警告和 `shards will be relocated away from this node` 信息。
画面 12: 在 PDF 文档中显示 Docker 安装部分，包含命令 `kill 68072`。
画面 13: 在终端中执行 `kill 68072` 结束进程，然后执行 `su - Elasticsearch` 切换用户，执行 `cd /haoke/es/` 进入目录，执行 `./Elasticsearch` 启动服务。
画面 14: 在 PDF 文档中显示修改配置文件的步骤，包括 `vim conf/Elasticsearch.yml`、`vim conf/jvm.options`、`vim /etc/sysctl.conf`，并提示 `启动ES服务`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```php
$response = Resilient->search($params);
```
画面 2:
```bash
rm -rf *
ll
rm -rf es
```
画面 3:
```
Elasticsearch-6.5.4/bin/Elasticsearch-plugin.bat
Elasticsearch-6.5.4/bin/Elasticsearch-env.bat
Elasticsearch-6.5.4/bin/Elasticsearch-keystore.bat
Elasticsearch-6.5.4/README.txt
Elasticsearch-6.5.4/LICENSE.txt
Elasticsearch-6.5.4/modules/x-pack-monitoring/
Elasticsearch-6.5.4/modules/x-pack-monitoring/plugin-descriptor.properties
Elasticsearch-6.5.4/modules/x-pack-monitoring/Elasticsearch-rest-client-sniffer-6.5.4.jar
Elasticsearch-6.5.4/modules/x-pack-monitoring/LICENSE.txt
Elasticsearch-6.5.4/modules/x-pack-monitoring/plugin-security.policy
Elasticsearch-6.5.4/modules/Mapper-extras/
Elasticsearch-6.5.4/modules/Mapper-extras/plugin-descriptor-6.5.4.jar
Elasticsearch-6.5.4/modules/Mapper-extras/plugin-security.policy
Elasticsearch-6.5.4/modules/percolator/
Elasticsearch-6.5.4/modules/percolator/plugin-descriptor-6.5.4.jar
Elasticsearch-6.5.4/modules/percolator/plugin-security.policy
Elasticsearch-6.5.4/modules/ingest-common/
Elasticsearch-6.5.4/modules/ingest-common/plugin-descriptor-6.5.4.jar
Elasticsearch-6.5.4/modules/ingest-common/joni-2.1.6.jar
Elasticsearch-6.5.4/modules/ingest-common/jcodings-1.0.12.jar
```
画面 4:
```bash
chown -R Elasticsearch:Elasticsearch es
```
画面 5:
```bash
#创建Elasticsearch用户，Elasticsearch不支持root用户运行
useradd Elasticsearch
#解压安装包
tar -xvf Elasticsearch-6.5.4.tar.gz -C /haoke/es/
```
画面 6:
```yaml
# Set the bind address to a specific IP (IPv4 or IPv6):
network.host: 172.16.55.185

# Set a custom port for HTTP:
http.port: 9200

# For more information, consult the network module documentation.

# Discovery
# Pass an initial list of hosts to perform discovery when new node is started:
# The default list of hosts is ["127.0.0.1", "[::1]"]
# discovery.zen.ping.unicast.hosts: ["host1", "host2"]

# Prevent the "split brain" by configuring the majority of nodes (total number of master-eligible nodes / 2 + 1):
discovery.zen.minimum_master_nodes: "1"
```
画面 7:
```
#kernel.domainname = example.com
#kernel.printk = 3 4 1 3
# Functions previously found in netbase
# Uncomment the next two lines to enable Spoof protection (reverse-path filter)
# Turn on Source Address Verification in all interfaces to
# prevent some spoofing attacks
net.ipv4.conf.default.rp_filter=1
net.ipv4.conf.all.rp_filter=1

# Uncomment the next line to enable TCP/IP SYN cookies
# See http://lwn.net/Articles/277146/
# Note: This may impact IPv4 TCP sessions too
net.ipv4.tcp_syncookies=1

# Uncomment the next line to enable packet forwarding for IPv4
"etc/sysctl.conf" [readonly] 63L, 210C
```
画面 8:
```bash
cd ..
cd bin
ls
./Elasticsearch
```
画面 9:
```
172.16.55.185:9200
```
画面 10:
```json
{
  "email": "xxx",
  "password": "xxx"
}
```
画面 11:
```
[2018-12-31T20:26:20,275][WARN ][o.e.c.r.a.DiskThresholdMonitor] [x30rcg] high disk watermark [90%] exceeded on [x30rcg][fS6qY3lC8LC0][1][haoke/es/Elasticsearch-6.5.4/data/nodes][0] free: 2.5gb[8.9%], shards will be relocated away from this node
[2018-12-31T20:26:20,280][WARN ][o.e.c.r.a.DiskThresholdMonitor] [x30rcg] high disk watermark [90%] exceeded on [x30rcg][fS6qY3lC8LC0][1][haoke/es/Elasticsearch-6.5.4/data/nodes][0] free: 2.5gb[8.9%], shards will be relocated away from this node
[2018-12-31T20:26:20,280][WARN ][o.e.c.r.a.DiskThresholdMonitor] [x30rcg] high disk watermark [90%] exceeded on [x30rcg][fS6qY3lC8LC0][1][haoke/es/Elasticsearch-6.5.4/data/nodes][0] free: 2.5gb[8.9%], shards will be relocated away from this node
[2018-12-31T20:26:20,280][WARN ][o.e.c.r.a.DiskThresholdMonitor] [x30rcg] high disk watermark [90%] exceeded on [x30rcg][fS6qY3lC8LC0][1

