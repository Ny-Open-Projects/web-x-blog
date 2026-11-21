# 15.Kibana入门学习之通过Docker部署安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\15.Kibana入门学习之通过Docker部署安装【海量资源尽在 ubkz.com】.mp4
- 时长 2分59秒（音频 179s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们通过这个Docker呢去做一个部署那么首先呢我们需要去拉取这个镜像镜像呢在前面呢我已经拉取过了那么就不做一个拉取了那么我就直接来去创建这个容器吧那么当然了创建容器之前呢我们首先呢需要是去创建一个配置文件那么我这样我把这个配置文件呢我丢到外面去然后呢丢掉
[00:25] 这个位置吧那么在这个里面我们去创建一个这个kibanda的一个配置文件然后呢我们把下面的配置项我们拷贝过来然后呢是在下面这个位置设置Ctrl C然后拷贝然后呢是不是就这两个配置项啊刚刚我们所修改的是也是这两个配置项好嘞然后呢我们去做一个做一个创建这个容器啊那么之前呢我这个里面已经有一个容器了所以呢我把这个容器呢先给它删除掉
[00:53] 然后呢来一个Docker然后呢RemoteKeybanner好那么这个容器呢是不是就已经删除掉了然后呢我们再来创建一个容器把它拷贝一下然后呢就放到这吧然后呢把这个格式呢我们整理一下然后呢我们来看一下这个挂载它是挂载到Docker这个可能是路径稍微有点问题那么我们这个路径呢是Hawk下面的BeesHawk下面的Bees然后呢Keybanner有没有
[01:24] 然后把这个就拿掉了这样的话路径就对了但是后面这个路径要保持一个这样的路径好那么然后我们就去创建这个容器走然后我们就可以把这个容器去启动起来了Kibana然后我们去按的tail然后我们通过这个dockerlogslogslogs-f然后我们通过
[01:54] 就是这个kbana然后呢我们去启动这个容器并且去查看它的一个日志那么我们就可以看到它是否已经有启动成功啊那么当然了在我们刚刚这个脚本中啊就是启动了创建这个命令中啊我们所使用的网络模式呢使用的是host是直接跟我们主机做一个共享那么我们等待它一下OK那么现在呢已经就跑起来了那么我们来看一下我们的这个Docker的
[02:25] 容器的运行的情况那么会发现K8是不是就跑起来了那么我们尝试去刷新一下那么看它会出现一个什么情况那么依然是OK的那就说明我们这个Docker的一个通过一个Docker的一个部署那么已经是OK了那么其实我们学了两种方式一种是通过安装包的方式去做一个部署另外一种是通过Docker的方式去做一个部署其实我更建议使用这个Docker的一个部署因为相对比较简单我们只需要去使用一个命令把它启动起来就可以了
[02:54] OK好那么这个就是通过一个Docker去安装kebana

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 部署 Elasticsearch、Kibana 和 Redis，并配置 Filebeat 将数据导入 Kibana。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 讲义，标题为“4.2、通过Docker部署”，下方列出“#拉取镜像”和“#创建配置文件”步骤，包含代码：Docker pull kibana:6.5.4；vim kibana.yml；server.host: "192.168.1.7"；Elasticsearch.url: "http://192.168.1.7:9200"。
画面2：终端显示 Kibana 监控插件状态从黄色变为绿色，Elasticsearch 集群模式为 basic，状态 active，服务器在 http://192.168.1.7:5601 监听，但出现“Unhandled rejection Error: No Living connections”错误。
画面3：终端显示进入 kibana-6.5.4-linux-x86_64 目录并执行 ll 命令，列出目录结构。
画面4：终端显示进入 kibana-6.5.4-linux-x86_64 目录，执行 ll 命令，列出目录结构，然后执行 cd .. 命令。
画面5：终端显示进入 kibana-6.5.4-linux-x86_64 目录，执行 ll 命令，列出目录结构，然后执行 cd .. 命令。
画面6：终端显示进入 kibana-6.5.4-linux-x86_64 目录，执行 ll 命令，列出目录结构，然后执行 cd .. 命令。
画面7：EditPlus 编辑器中显示 Docker 创建 Redis 集群节点的命令，包括 redis-node01、redis-node02、redis-node03，以及配置文件和日志文件路径。
画面8：EditPlus 编辑器中显示 Docker 创建 Kibana 容器的命令，包含 --net host 参数和配置文件路径。
画面9：终端显示执行 Docker rm kibana 命令删除容器，然后执行 pwd 命令查看当前目录。
画面10：终端显示 Elasticsearch 和 Kibana 插件状态从 uninitialized 变为 yellow，再变为 green，但出现安全警告。
画面11：终端执行 Docker ps 命令，列出正在运行的容器，包括 kibana、redis-node01、redis-node02、redis-node03、es-node01、es-node02、es-node03。
画面12：浏览器打开 Kibana 网页，显示空白页面，左侧导航栏包含 Discover、Visualize、Dashboard、Timeline、Canvas、Machine Learning、Infrastructure、Logs、APM、Monitoring、Management、Default、Collapse 等选项。
画面13：PDF 讲义页面，标题为“4.2、通过Docker部署”，下方文字说明“可以看到kibana页面，并且可以看到提示，导入数据到Kibana”。
画面14：PDF 讲义页面，标题为“4.2、通过Docker部署”，下方列出“#拉取镜像”和“#创建配置文件”步骤，包含代码：Docker pull kibana:6.5.4；vim kibana.yml；server.host: "192.168.1.7"；Elasticsearch.url: "http://192.168.1.7:9200"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
#拉取镜像
Docker pull kibana:6.5.4
#创建配置文件
vim kibana.yml
server.host: "192.168.1.7"
Elasticsearch.url: "http://192.168.1.7:9200"

画面7：
Docker create --name redis-node01 -v /data/redis-data/node01/data --cluster-enabled yes --cluster-config-file nodes-node-01.conf --loglevel debug --logfile nodes-node-01.log redis:5.0.2
Docker create --name redis-node02 -v /data/redis-data/node02/data --cluster-enabled yes --cluster-config-file nodes-node-02.conf --loglevel debug --logfile nodes-node-02.log redis:5.0.2
Docker create --name redis-node03 -v /data/redis-data/node03/data --cluster-enabled yes --cluster-config-file nodes-node-03.conf --loglevel debug --logfile nodes-node-03.log redis:5.0.2

画面8：
Docker create --name kibana --net host -v /haoke/beats/kibana:/usr/share/kibana/config/kibana.yml kibana:6.5.4

画面14：
#拉取镜像
Docker pull kibana:6.5.4
#创建配置文件
vim kibana.yml
server.host: "192.168.1.7"
Elasticsearch.url: "http://192.168.1.7:9200"

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.2、通过Docker部署”，下方文字说明“可以看到kibana页面，并且可以看到提示，导入数据到Kibana”。
画面13：PPT标题为“4.2、通过Docker部署”，下方文字说明“可以看到kibana页面，并且可以看到提示，导入数据到Kibana”。
画面14：PPT标题为“4.2、通过Docker部署”，下方文字说明“可以看到kibana页面，并且可以看到提示，导入数据到Kibana”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

