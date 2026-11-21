# 17.Kibana入门学习之Metricbeat仪表盘

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\17.Kibana入门学习之Metricbeat仪表盘【海量资源尽在 ubkz.com】.mp4
- 时长 5分41秒（音频 341s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来实战一下把我们的magicbit的一些数据呢在我们的kbund中呢去展现出来那么怎么去做展现呢我们来看一下那么最终我们其实所想要去看到的一种效果呢就是我们希望呢再通过这种方式啊就是一秒盘这种方式
[00:19] 去把我们这个数据呢去展现出来那么我们就需要如果啊如果我们要去做这样的仪表盘的话我们就需要一个一个的这个图表去做一个这个设计然后呢把它拼装到一起形成这整个啊这个页面这个还是需要花一点时间的啊比较庆幸的是呢在这个methodbit中呢他提供了啊默认提供了这个decibel的
[00:45] 我们只需要去一个名令它就可以把我们的这个DESKBORD发送到我们这个K8的中那么我们就可以看到下面的这个效果了好那我们实际的来操作一下那么我们就来找到我们的配置文件那么我们看一下进入我们这个CD进入到MATRIX的bit下面的我们找到这个我们就打开这个它的一个yaml文件
[01:13] 然后呢下面呢我们去搜索一下然后呢在这然后呢我们去把它这个host打开然后呢我们去给它指定就是我们这个地址然后呢localhost我们改成192.168.1.75601然后呢我们这个搞定之后啊那么下面我们就通过这个命令一个setup来把我们的despot安装到kibana中走等待它的一个执行
[01:44] 那么可以看到呢它现在呢是正在去loading这个decibel的它提示我们说这个k8呢一定要保持一个运行的状态那么才可以去使用那么我们稍微去等一下它现在已经就加载成功了那么加载成功的我们其实可以来看一下在我们这个decibel的里面那么就会有一些这样的一些decibel的可用当然了你比如说我们来找一下比如说我们找一下我们这个system
[02:13] 系统我们来搜一下搜索system那么system我们看它的一个概览那么你会发现现在好像也没什么太多的一些数据对吧我们点一下没有太多的一些你看最近30分钟没有什么数据那么我们现在就可以把我们的这个bit跑起来然后让它去把一些数据继续做一些发送不断的去更新数据那么我们去查看这个仪表盘的时候它的数据是不是就比较多了
[02:44] 看起来就比较好看一点对吧metric的bit然后呢-e去执行那么我们等待一下它马上就有数据会写入进去那么比如说我们来查看最近15分钟的数据那么OK现在是不是看到数据了包括你可以看到这个是它的内存的数据然后呢一些CPU的一些这个数据那么如果我每次点击这个刷新太麻烦了它还有一个自动刷新比如说我们定义它五秒钟去刷新一次
[03:11] 那么他就会在每五秒钟去刷新一下这个数据那我们点击这个看一下他这些这个容器一些运行的一些情况然后呢我们系统的一些盖蓝的一些信息包括我们这个CPU啊内存的一些信息啊都有OK那么这个是我们的一些这个这个是CPU的一些使用的一些这个情况那么前面的没有数据后面的才有数据出来啊然后呢我们再看一下
[03:38] 他应该10秒钟会采集一次刚刚我们其实记得CPU这个位置刚刚是没有数据的是吧现在是不是已经有数据了OK好嘞好那么下面还有一些其他的一些表格的一些数据投表的数据CPU内存一些使用的一些情况OK可以去看一下这个是我们的网络的一些情况蓝色的代表的是我们的输入对吧这个叫紫色
[04:06] 紫色的这个是代表的是它的一个输出好然后这个是我们的一些进程的一些情况进程的情况包括现在在我们的内存资源比较多的一个就是加了一个进程是吧还有node的进程等等可以看到这样的一个情况好那么这个图表内容还是比较丰富的当然我们还可以去看一下其他的一些信息包括redis那么我们来看一下那么这个里面是不是有一个redis的一些信息
[04:36] 那么目前是不是也有一些这个数据啊数据显示出来那么这个呢有两个客户端去连接到我们当前的Redis这个是一些这个我们的一些这个cont啊连接的一个cont哎呦OK然后呢下面呢是我们的一些服务的一些这个版本啊版本信息啊等等好那么通过这种方式呢是不是也可以去查看啊去查看我们这个Redis的一些这个
[05:01] 内容就它一些指标的数据然后这个就是它的一些我们三个节点对吧6379,6380和6381OK那么当然了这个里面还会有一些其他的大家都可以去点一下那么比如说我们要去找一下像System我刚刚看过了Redis也有Windows因为其他的如果我们现在没有去做一个抓取指标的话那么其实我们也是看不到的那么大概可能我们就现在只有两个一个就是System一个就是Redis的OK
[05:31] 好 那么这个就是给大家去讲一下我们如何在k8当中去查看我们的仪表盘的数据ok好嘞好那么关于这个我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何配置并使用 Metricbeat 将系统指标数据导入 Kibana 并展示仪表盘。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 讲义第 4.5 节“Metricbeat 仪表盘”，说明 Metricbeat 数据可在 Kibana 中展示，并显示配置文件 `setup.kibana` 的内容：`#修改metricbeat配置 setup.kibana: host: "192.168.1.7:5601"`。
画面 2: 展示 Kibana 中 Metricbeat 系统概览仪表盘，包含 CPU、内存、负载、网络流量等指标图表。
画面 3: 展示 PDF 讲义第 4.6 节“Filebeat 仪表盘”，并显示 Kibana 中仪表盘列表，包含 Metricbeat 各模块的仪表盘。
画面 4: 展示终端中 Metricbeat 配置文件 `setup.kibana` 的内容，其中 `host` 设置为 `"localhost:5601"`。
画面 5: 展示终端中进入 Metricbeat 安装目录并执行 `./metricbeat setup --dashboards` 命令，加载仪表盘。
画面 6: 展示 Kibana 中仪表盘正在加载的状态。
画面 7: 展示终端中执行 `./metricbeat setup --dashboards` 命令后，提示“Loaded dashboards”。
画面 8: 展示 Kibana 中 Metricbeat 系统主机概览仪表盘，显示 CPU、内存、磁盘等指标，提示“无数据可显示”。
画面 9: 展示 Kibana 中“按 CPU 使用率的主机直方图”，鼠标悬停显示 CPU 使用率 22.4%。
画面 10: 展示 Kibana 中“网络流量（数据包）”和“网络流量（字节）”图表，以及“按内存排序的进程”和“按 CPU 排序的进程”图表。
画面 11: 展示 Kibana 中“Redis 客户端”仪表盘，显示连接客户端数量、主机信息、服务器版本等。
画面 12: 展示 Kibana 中“Redis 服务器模式”仪表盘，显示集群和 epoll 模式。
画面 13: 展示 Kibana 中 Metricbeat 各模块仪表盘列表，包括 Docker、Apache、Golang、HAProxy、MySQL 等。
画面 14: 重复画面 2 的内容，展示 Kibana 中 Metricbeat 系统概览仪表盘。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
#修改metricbeat配置
setup.kibana:
  host: "192.168.1.7:5601"
```
画面 4:
```
#setup.dashboards.enabled: false

# The URL from where to download the dashboards archive. By default this URL
# has a value which is computed based on the Beat name and version. For released
# versions, this URL points to the dashboard archive on the artifacts.elastic.co
# website.
#setup.dashboards.url:

# Starting with Beats version 6.0.0, the dashboards are loaded via the Kibana API.
# This requires a Kibana endpoint configuration.
setup.kibana:
  # Kibana Host
  # Scheme and port can be left out and will be set to the default (http and 5601)
  # In case you specify and additional path, the scheme is required: http://localhost:5601/path
  # IPv6 addresses should always be defined as: https://[2001:db8:1]:5601
  host: "localhost:5601"
```
画面 5:
```
root@itcast01:metricbeat-6.5.4-linux-x86_64# ./metricbeat setup --dashboards
Loading dashboards (Kibana must be running and reachable)
Loaded dashboards
```
画面 7:
```
root@itcast01:metricbeat-6.5.4-linux-x86_64# ./metricbeat setup --dashboards
Loading dashboards (Kibana must be running and reachable)
Loaded dashboards
```
画面 11:
```
Hosts [Metricbeat Redis]
metricset.host: Descending
Uptime (s)  PID  Memory  CPU used(user)  CPU used (system)
192.168.1.76579  10.142  1  1.506MB  16.16  26.324
192.168.1.76380  10.142  1  1.506MB  16.408  26.516
192.168.1.76381  10.142  1  1.506MB  16.456  26.696
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“4.6. Filebeat 仪表盘”，展示 Kibana 仪表盘，包含多个指标图表。
画面 3: PPT 标题为“4.6. Filebeat 仪表盘”，展示 Kibana 仪表盘列表，包含 Metricbeat 各模块的仪表盘。
画面 13: PPT 标题为“Metricbeat 各模块仪表盘”，展示仪表盘列表，包括 Docker、Apache、Golang、HAProxy、MySQL 等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

