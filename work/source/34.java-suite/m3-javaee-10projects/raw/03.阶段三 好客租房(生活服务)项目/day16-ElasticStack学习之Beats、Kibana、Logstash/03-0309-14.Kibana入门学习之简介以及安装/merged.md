# 14.Kibana入门学习之简介以及安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\14.Kibana入门学习之简介以及安装【海量资源尽在 ubkz.com】.mp4
- 时长 6分1秒（音频 362s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来我们来看一下KBanner那么在前面无论我们使用的是Fairbit还是Metricbit那么都是我们把数据最终要不然就是在我们的控制台去输出要不然就是我们把这个数据去发送到Elixir中去做一个展现那么这样肯定是不是很友好的对吧那么我们希望我们的数据是以一种图形化的方式去做展现比如说像柱形图,饼图这样的一些图形化的方式去把它展现出来
[00:29] 那么KBUNNER就是在做这个事情它是我们ELAC stack的一个窗口就是一个可视化好那么下面我们来看官方对它的一个描述来看一下那么KBUNNER是一个开源的一个数据分析和可视化的在那个平台它是ELAC stack的成员之一用于设计于ELAC search的一个协助那么也就是说它可以在ELAC设置中进行什么的数据的搜索查看以及交互
[00:55] 那么可以方便的利用这种图表的表格的地图的一些展现方式对我们的数据进行多元化的一个展现ok好那么下面我们来看他的一个官方官方的网站那么在这个官方的这个网站中他做了一个这个动画还是非常形象的你看这个住行图然后去转换成这样的一个图形对吧然后会转换成在那个饼图ok好那么这个就变成一个地图了对吧地图的一个展现
[01:23] 好那么下面呢这句话说的也不是比较有意思的对吧叫做怎么的一张图片胜过千万行这个日志比如说你就拿它为例对吧那么我们去看这个内容的话是不是就非常的清楚知道哎这个红色的是这样的绿色的是这样的它代表什么对吧那么如果说我们要去看这个日志的话一行一行看日志那么是是非常不容易去发现里面一些问题的那么我们看日志的目的是什么我们的目的肯定要是从中去发现问题对吧发现问题然后我们才能够去解决问题
[01:53] 好嘞那么还有呢是可以把数据呢导入到一些我们的地图里面去OK所以可以看到它的功能呢是非常强大的对吧非常强大的OK那么这个我们就不详细去说了大家可以自行去做一些这个阅读OK好一会呢我们也会去把它的一些功能呢给大家做一些这个基本的一些展示好那么接下来呢我们就动手去做一个配置安装这个还是比较简单的啊我们来看一下那么首先呢我们需要去上传一个我们这个包啊
[02:22] 那么我们就把它还是放到这个beast下面吧然后呢找到我们的一个安装包这个下面呢有一个叫做kbanner这个安装包然后呢我们把它拖到这个里面来做一个这个上传然后呢我们等待它的一个上传完成完成之后呢它就会有这样的一个我们退出去啊cd点点回去然后呢它就会有这样的一个这个现在还没有上传完我们稍等一下好那么我们看到现在已经上传结束了那我们去做一个解压
[02:51] Kibana把它解压出来那么解压出来我们就会得到一个Kibana的一个这样的一个项目然后我们去对它的配置文件做一些修改那么就可以做一个使用了我们来看一下那么我们去修改config下面一个Kibana这样的一个yaml文件然后去做一些修改那么主要是修改两个内容一个是它的host一个就是elect search的一个url好我们来看一下那么我们进入Kibana
[03:16] 然后我们去找到它的configure下面有一个kbunner的configure然后下面我们要找到的是这个serverhost那么要注意如果他如果采用他默认的localhost的话那么我们是没有办法通过IP地址去做一个访问的所以我们需要在这个位置来指定我们的IP地址19168.1.7好嘞然后下面还有一个elagsrch的配置我们来找一下往下面找
[03:47] 还在下面吗在我们来搜索一下吧搜索没看到那我们就搜索一下在这然后在下面走没有在这找到了那么这个是不是就是elite search url那么我们要给它来指定一下就叫什么的192.168.1.7好嘞那么我们保存退出那么有这两个配置就可以了
[04:27] 那么一个是他一个是他好嘞那么现在我们就来启动一下进入到下面有一个bin目录然后我们去执行 kbana然后去把它跑起来就可以了那么要注意的是它是一个要依赖云洞的js的一个这样的项目那么可以看到有一个叫node-modules这个里面有一些依赖我们其实直接去运行就可以了好我们等待它执行因为它的启动稍微需要一点点时间
[04:57] 我们稍微等待一下好那么我们可以看到现在他已经就跑起来了跑起来之后呢我们就尝试着去访问一下那么可以看到在这个位置呢他告诉我们说端口是不是5601那我们尝试访问一下然后1.75601走那么我们可以看到这个就是我们的KBANA那么可以看到他就是一个前端的啊这样的一个项目这样的界面啊哎OK然后呢我们来看一下呃现在呢我们是呃他他在咨询我们啊是否要导入一些
[05:27] 这个就是测试的一些这个数据那我们现在不需要就让他去守一个空的吧如果我们需要的话再去做一些这个导入啊就可以了那么我们现在可以看到那么当我们看到这个界面的时候呢我们就会呃就知道啊我们的kbana就安装成功了那么由于我们现在呢仅仅是讲一个安装具体他的一些功能呢我们一会我们再讲ok那么这个就是我们通过这个安装包的方式去做一个安装那么下面呢我们就呃来呃我们就通过这个Docker去做一个安装
[05:57] 好那么关于这个通过这个安装包的安装我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中解压、配置并启动 Kibana，使其能与 Elasticsearch 协同工作并提供数据可视化功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 PDF 文档中关于 Kibana 的介绍页，内容为“您使用 Elastic Stack 的窗口”，并附有世界地图点状图。
画面 2：展示 Kibana 官网页面，标题为“您使用 Elastic Stack 的窗口”，并包含“Kibana 101：入门必知的所有内容，观看视频”按钮。
画面 3：展示 Kibana 官网页面，内容包括“用 Machine Learning 探索异常情况”和“通过 Canvas，发挥无限创意”两个功能模块。
画面 4：展示 Kibana 官网页面，内容为“通过 Canvas，发挥无限创意”，并展示销售漏斗图等可视化图表。
画面 5：展示终端界面，显示 Metricbeat 的日志输出，包含系统监控信息和动态配置重载停止的记录。
画面 6：展示终端界面，执行 `cd` 命令进入 `beats` 目录，然后列出目录内容，显示 `metricbeat.yml`、`modules.d/` 等文件。
画面 7：展示终端界面，进入 `kibana-6.5.4-linux-x86_64` 目录，列出 `node_modules/` 下的文件。
画面 8：展示终端界面，进入 `kibana-6.5.4-linux-x86_64` 目录下的 `config/` 子目录，列出 `kibana.yml` 等文件。
画面 9：展示终端界面，打开并显示 `kibana.yml` 配置文件内容，包含 `#Elasticsearch.ssl.verificationMode`、`#Elasticsearch.pingTimeout` 等注释。
画面 10：展示 PDF 文档中“4.1、配置安装”章节，内容包括解压命令、修改配置文件命令和启动命令。
画面 11：展示终端界面，进入 `kibana-6.5.4-linux-x86_64/bin/` 目录，列出 `kibana` 可执行文件。
画面 12：展示浏览器地址栏，输入 `192.168.1.7:9200` 后跳转至 Google 搜索页面，显示搜索建议。
画面 13：展示 Kibana 登录页面，提示“Help us improve the Elastic Stack...”，并显示“Add Data to Kibana”功能模块。
画面 14：展示 PDF 文档中“4.1、配置安装”章节，内容与画面 10 相同，包含解压命令、修改配置文件命令和启动命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5：无直接代码或配置。
画面 6：
```
root@itcast01:beats# cd
root@itcast01:beats# ll
total 39164
drwxr-xr-x 2 root root 4096 Jan 15 22:04 .
drwxr-xr-x 4 root root 4096 Dec 18 04:29 metricbeat
drwxr-xr-x 2 root root 4096 Dec 18 04:29 metricbeat.yml
drwxr-xr-x 2 root root 4096 Dec 18 04:29 modules.d/
drwxr-xr-x 2 root root 4096 Dec 18 04:29 README.md
```
画面 7：
```
kibana-6.5.4-linux-x86_64/node_modules/@elastic/eui/lib/components/header/header_alert/index.js
```
画面 8：
```
root@itcast01:config# ll
total 16
drwxr-xr-x 2 itcast itcast 4096 Dec 18 05:33 .
drwxr-xr-x 11 itcast itcast 5054 Dec 18 05:23 kibana.yml
```
画面 9：
```
# To disregard the validity of SSL certificates, change this setting's value to 'none'.
#Elasticsearch.ssl.verificationMode: full

# Time in milliseconds to wait for Elasticsearch to respond to pings. Defaults to the value of
#Elasticsearch.pingTimeout: 1500

# Time in milliseconds to wait for responses from the back end or Elasticsearch. This value
# must be a positive integer.
#Elasticsearch.requestTimeout: 30000

# List of Elastic client-side headers to send to Elasticsearch. To send "no" client-side
# headers, set this value to [] (an empty list).
#Elasticsearch.requestHeadersWhitelist: []

# Header names and values that are sent to Elasticsearch. Any custom headers cannot be overwritten
# by client-side headers, regardless of the Elasticsearch.requestHeadersWhitelist configuration.
#Elasticsearch.customHeaders: {}

# Time in milliseconds for Elasticsearch to wait for responses from shards. Set to 0 to disable.
#Elasticsearch.shardTimeout: 30000

# Time in milliseconds to wait for Elasticsearch at Kibana startup before retrying.
#Elasticsearch.startupTimeout: 5000
```
画面 10：
```
#解压安装包
tar -xvf kibana-6.5.4-linux-x86_64.tar.gz
#修改配置文件
vim config/kibana.yml
#启动
./bin/kibana
#通过浏览器进行访问
http://192.168.1.7:5601/app/kibana
```
画面 11：
```
root@itcast01:config# cd bin/
root@itcast01:bin# ll
total 20
drwxr-xr-x 2 itcast itcast 4096 Dec 18 05:38 .
```
画面 14：
```
#解压安装包
tar -xvf kibana-6.5.4-linux-x86_64.tar.gz
#修改配置文件
vim config/kibana.yml
#启动
./bin/kibana
#通过浏览器进行访问
http://192.168.1.7:5601/app/kibana
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：PPT 标题为“4. Kibana”，内容为“您使用 Elastic Stack 的窗口”，并附有世界地图点状图。
画面 2：官网标题为“您使用 Elastic Stack 的窗口”，并包含“Kibana 101：入门必知的所有内容，观看视频”按钮。
画面 3：官网标题为“用 Machine Learning 探索异常情况”，并包含“通过 Canvas，发挥无限创意”功能模块。
画面 4：官网标题为“通过 Canvas，发挥无限创意”，并展示销售漏斗图等可视化图表。
画面 10：PPT 标题为“4.1、配置安装”，内容包括解压命令、修改配置文件命令和启动命令。
画面 14：PPT 标题为“4.1、配置安装”，内容与画面 10 相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

