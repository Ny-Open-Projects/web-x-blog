# 13.Metricbeat入门学习之Redis Module

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\13.Metricbeat入门学习之Redis Module【海量资源尽在 ubkz.com】.mp4
- 时长 5分58秒（音频 358s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下Magicbit的module那么前面呢我们其实已经用过它的一个module了对吧就是一个system系统那么下面呢我们就来看一下它有哪些module可供我们选择去使用那我们去查通过list去做一个查看走那么可以发现呢有这么多的一些这个module可用啊那么当然都是disable的那么只有一个呢是启用就是system
[00:27] 那么这个是默认启用的这样的一个module当然了我们可以把它disable掉禁用掉那么接下来我们就以一个redis为例还是拿这个redis为例然后去去获取一些redis的一些指标的一些数据然后把它去保存到我们的elite设置中我们来看一下那么首先我们需要把我们 redis这个module给它去做一个enable做一个启用好那么我们来看一下在这个位置然后之前走
[00:56] 那么我们已经启用成功了然后我们再去查看list你会发现那么在 enable这个位置它有两个module已经被启用一个是redis一个是systemok好那么我们接着继续往下面看那么下面我们就需要去修改一下我们redis module的一些配置文件那么前面我们讲failbit的时候其实我们讲过这个module它的配置文件都是在这个modules然后点d这个里面
[01:25] 那么来看一下这个里面呢可以看到是不是有两个已经被启用了OK好那么下面我们去修改一下redis的这个配置文件那么我们可以看到在这个位置是需要去指定我们的redis的一些配置信息的对吧那么我们来指定一下那么我们去给它设置成什么呢设置成192.168.1.7然后呢6379然后呢还有一个呢是
[01:53] 192.168.1.7冒号6380然后我们再来一个192.168.1.7冒号6381OK那么我们总共是不是有三个OK那么来看一下讲义在讲义中是不是也是有三个没有问题好那么接下来我们来看一下下面这些保证默认就可以了好那么现在我们基本上就已经把release
[02:21] 的这个module就已经配置完成了那么接下来我们做启动就可以了好那我们来看一下怎么样启动呢我们是回到前面这个目录然后执行这个然后呢是不是通过一个刚一这个参数对吧走然后呢我们去跑起来之后他就应该去把数据是把redis里面的数据呢就已经去发送到我们的elect search了我们来查看一下刷新一下走
[02:50] 数据现在是不是还没有我们来看一下刷新一下然后我们到这个里面来然后我们才浏览一下数据那么我们点击它点击它好那么现在我们可以看到他拿到的这个数据是host这个应该是我们看一下这个是不是redis的数据现在还没有看到redis的数据那么来看一下
[03:16] OK那么我们按照这个时间去做一个排序那么就会发现已经有Redis的数据写入进来了我们来看一下现在又看不到了那我们去看一下那么可以看到现在好像又看不到它应该是有我刚才已经是可以看到我们来看一下那我们刷新等待它一会就会有新的数据进来那么这个我们在后面就需要通过界面就比较好看一点了
[03:49] 那么OK你可以看到在这个位置是不是已经就有Redis的相关的数据了那就说明我们Redis数据它是不是已经就写入到我们的Electro Search中了来看一下那么它的一个module就是Redis然后所执行的一个指标就是info那么它所拿到的信息就下面的这么一堆信息我们来看一下那么就是下面这么一堆它的信息replace的一些相关的信息然后包括还有一些它的内存的一些使用的情况
[04:19] 等等OK好那么这个呢我们是不是就已经完成了对于我们的一个这个REDIS module的一个使用OK那么最终可以看到数据呢就是有这样的一个数据OK那么当然它会有一些其他的一些这个用法那么大家也可以去参考这官方的一些文档那么其他用法呢都非常的相似了那我们就不一一去展开了非常的相似啊那么我们可以等待一下它打开我们可以大概的来看一下
[04:47] 大家有这么一些包括有什么Apache的对吧然后还有Docker大家也可以去这个我还建议大家可以去做一下就是我们现在本身所使用的环境是不是就使用这个Docker那么我们是可以去监测一下我们的一些这个Docker的一些它的一些运行的一些指标然后我们可以看一下还有一些什么的还有一些这个叫Docker然后还有还有这个Golang
[05:14] 然后还有Kafka这个也是会用的比较多的一个然后还有Kubernetes然后是芒果DB这个大家是不是也可以去用一下因为我在我们项目中是不是也使用了芒果DBOKMySQL这个就不用说了我们项目中要用到那么Nginx这个肯定不用说了那么在我们的后面部署的时候我们会使用到Nginx
[05:35] 好嘞那么RobinMQRobinMQ呢我们并没有使用到那么这个呢大家在前面的也学习过也可以去尝试去做一下OK好那么你只需要需要哪些你点进去看参考官方的文档就可以了OK好嘞那么这个呢就是它的moduleReadyModule的一个使用OK好那么关于这个ReadyModule的使用那么就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Metricbeat 启用和配置 Redis 模块，并查看其采集到的指标数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 讲义中 Metricbeat 的 Module 配置部分，重点是 system 模块的配置示例。
画面2：在终端中执行命令 `./metricbeat modules list`，查看当前已启用的模块，显示 system 模块已启用。
画面3：终端中继续执行 `./metricbeat modules list`，确认 system 模块启用状态。
画面4：在终端中执行 `ls -l` 命令，列出 modules 目录下的所有文件，显示多个 .yaml.disabled 文件。
画面5：展示 PDF 讲义中 Redis Module 部分，介绍如何启用 Redis 模块并编辑配置文件。
画面6：在终端中执行 Metricbeat 启动命令，日志显示成功连接到 Elasticsearch。
画面7：在 Kibana 的 Discover 页面查看 metricbeat 采集到的指标数据，显示 system 模块采集的指标。
画面8：在 Kibana 的 Discover 页面，指标数据中显示了 system 模块采集的 filesystem 指标。
画面9：在 Kibana 的 Discover 页面，指标数据中显示了 system 模块采集的 process 指标。
画面10：在 Kibana 的 Discover 页面，指标数据中显示了 system 模块采集的 network 指标。
画面11：在 Kibana 的 Discover 页面，指标数据中显示了 system 模块采集的 load 指标。
画面12：展示 PDF 讲义中 Redis Module 配置的 hosts 字段，包含三个 Redis 服务地址。
画面13：浏览器打开 Metricbeat 官方文档页面，页面为空白。
画面14：展示 PDF 讲义中 Kibana 部分，介绍如何使用 Elastic Stack 的窗口。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
- drop_event.when.regex:
  system.filesystem.mount_point: '/sys/fs/cgroup/proc/devicet/host/lib/{1}/'
- module: system
  period: 15m
  metricssets:
    - uptime
- module: system
  period: 5m
  metricssets:
    - raid
    - raid.mount_point: '/'

画面5：
#启用redis module
./metricbeat modules enable redis
#修改redis module配置
vim modules.d/redis.yml
module: redis
metricssets:
  - info
  # - keyspace
period: 10s

画面12：
# Redis hosts
hosts: ["192.168.1.7:6379","192.168.1.7:6380","192.168.1.7:6381"]
# Network type to be used for redis connection. Default: tcp
#network: tcp
# Max number of concurrent connections. Default: 10
#maxconn: 10
# Redis AUTH password. Empty by default.
#password: foobared

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：标题为“3.4、Redis Module”，内容包括启用模块的命令和配置文件路径。
画面12：标题为“3.4、Redis Module”，内容包括 Redis hosts 配置和网络类型等参数。
画面14：标题为“4、Kibana”，内容包括 Elastic Stack 的窗口介绍。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

