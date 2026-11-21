# 18.Kibana入门学习之Filebeat仪表盘

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\18.Kibana入门学习之Filebeat仪表盘【海量资源尽在 ubkz.com】.mp4
- 时长 2分49秒（音频 169s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下failbit的仪表牌它的使用呢其实跟我们前面所讲的magicbit的这个使用是几乎是一样的啊差不多那么我们就以这个redis为例来做一个查看那么前面的这个内容呢这个内容其实就是我们刚刚所写的redis那个配置那么我们只需要给它添加kbana的配置就可以了好那我们来看一下那么我们就把这个就停掉吧然后呢我们去cd
[00:28] 点点回去然后呢找到failbit然后呢这个里面呢我们要去修改的是hawk下面有一个redis这个配置然后呢我们他已经把数据是不是写入到我们的elite search了那我们只需要再给他配置一个kibana就可以了好把它配置过来要注意格式好然后呢保存退出这样的话那么就搞定了那么接下来呢我们要去把我们的这个预表盘的安装到kibana中
[00:57] 然后我们依然是这样去做一个setup去做一个安装但是我们要指定一个-c去指定我们的一个配置文件走那么去做一个安装那么我们等待它的一个执行好那么现在我们看到它已经就加载完成了已经就把我们的DESPOD已经就发送到K8.0那么现在我们为了一会测试方便我们先把刚刚我们所测试的failbit也跑起来
[01:26] -1-C然后指定这个浩克浩克然后release把它也跑起来那么跑起来之后我们去查看一下那么还是进入这个despot我们来刷新一下然后我们去去做一个搜索搜索一个release那么你会发现那么刚刚的我们所看的是这个对吧那么现在又多了一个failbit的一个release注意这有个failbit好那我们点击它来看一下这个里面
[01:53] 我们目前可能在上面没有一些信息信息还没来但是我们会发现在下面已经有信息了已经有信息了那么它是最近15分钟是吧我们把这个调大一点看一下会怎么样那么这个就是它下面的数据当然上面的信息还没有那么可能得运行一段时间才会有OK但是我们现在目前已经看到什么它是不是已经就把数据是不是已经就把这个一把盘就已经发送过来了
[02:22] 并且我们在仪表盘里面也可以看到相关Redis的一些数据那就说明什么我们这Failbit的仪表盘也就OK了那么当然了其实它会有很多仪表盘我们只是以 Redis为例去做一个讲解OK那么如果需要去查看的话大家可以去做一些搜索去做一些查看好那么这个就是关于Failbit的一个仪表盘的一个使用那么我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Filebeat 配置监控 Redis 日志并将其数据可视化到 Kibana 仪表盘。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中 Filebeat 配置文件内容，包含 inputs、output.Elasticsearch、setup.kibana 等配置项，以及安装仪表盘的命令。
画面2：终端显示 metricbeat 服务停止的日志信息。
画面3：终端显示空的命令行界面，准备执行后续操作。
画面4：终端显示进入 Filebeat 目录并列出文件，包含 haoke-redis.yml 配置文件。
画面5：终端执行 ./filebeat -c haoke-redis.yml setup 命令，成功加载索引模板和仪表盘配置。
画面6：终端显示命令执行完成，提示加载仪表盘。
画面7：Kibana Dashboard 页面显示多个 Metricbeat 相关仪表盘。
画面8：在 Kibana Dashboard 页面搜索框中输入 "redis"，筛选出 Filebeat Redis 仪表盘。
画面9：进入 Filebeat Redis 日志页面，显示日志数据。
画面10：在 Filebeat Redis 仪表盘中，显示“无结果”。
画面11：在 Filebeat Redis 仪表盘中，显示“无结果”。
画面12：在 Kibana 日志页面，同时打开 PDF 文档，显示配置文件内容。
画面13：PDF 文档中显示 Filebeat 配置文件内容，聚焦于 output.Elasticsearch 和 setup.kibana 配置。
画面14：PDF 文档中显示 Filebeat 配置文件内容，聚焦于 setup.kibana 配置。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
#修改配置文件
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/log/*.log
setup.template.settings:
  index.number_of_shards: 3
filebeat.config.modules:
  path: ${path.config}/modules.d/*.yml
  reload.enabled: false
output.Elasticsearch:
  hosts: ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
setup.kibana:
  host: "192.168.1.7:5601"
#安装仪表盘到kibana
./filebeat -c haoke-redis.yml setup

画面4：
root@itcast01:filebeat-6.5.4-linux-x86_64# ll
drwxr-xr-x 7 root root 4096 Jan 15 18:05 logs/
drwxr-xr-x 6 root root 4096 Jan 15 22:13 .build.hash.txt
drwxr-xr-x 2 root root 41 Dec 18 04:24 .data/
-rw-r--r-- 1 root root 100372 Dec 18 04:22 fields.yml
-rw-r--r-- 1 root root 35930715 Dec 18 04:22 filebeat*
-rw-r--r-- 1 root root 68183 Dec 18 04:21 filebeat.reference.yml
-rw-r--r-- 1 root root 324 Jan 15 17:51 haoke-es.yml
-rw-r--r-- 1 root root 308 Jan 15 19:49 haoke.yml
-rw-r--r-- 1 root root 227 Jan 15 17:37 haoke.yml
-rw-r--r-- 1 root root 13675 Dec 18 04:17 LICENSE.txt
-rw-r--r-- 1 root root 802 Jan 15 19:34 log/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 NOTICE.txt
-rw-r--r-- 1 root root 802 Jan 15 19:34 README.md
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw-r--r-- 1 root root 163067 Dec 18 04:18 module.d/
-rw

