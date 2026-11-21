# 20.Logstash入门学习之部署安装（HelloWorld）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\20.Logstash入门学习之部署安装（HelloWorld）【海量资源尽在 ubkz.com】.mp4
- 时长 4分35秒（音频 275s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下部署安装当然了在我们安装之前呢我们首先来看一下我们的LockState它的一个处理的一个流程那么这个呢是我们的数据源那么去输入输入之后呢最后的输出进入到Electros那么所以关键的就中间的这个部分啊那这个中间这个部分呢我们把它称之为叫做LockState的一个PayPayLine然后就是一行一行去做一些这个处理然后呢我们可以看到
[00:29] 在这个Pipeline里面呢是有三个啊三个组件或者三个内容首先是一个input然后呢就是还有一个filt还有一个output所以说它的这个架构呢整体来讲还是非常简单的一个是输入那么一个是过滤一个就是输出那么所以其实我们可以知道输入是不是就去接收数据然后那filt呢显然就是在做一些什么数据的一些处理然后呢再去做一些这个输出就可以了所以它整个的一个架构是非常简单的啊
[00:59] 那么下面我们就来看一下它的一个安装那么由于Logstix它是使用什么的加尔语言开发的所以它要依赖于我们的JDK那么先检查一下我们的环境要求是JDK 1.8以上那么当然了这个我就不做检查了那么我这个版本肯定是1.8以上对吧那么我们也可以去执行一下看一下那么我所采用的版本是1.8.0.141这个版本
[01:27] 好然后我们去找到我们压缩包然后我们去做一个安装那么我们还是把它放到beast下面然后我们去找到一个安装包下面是不是有一个logstate对吧把它往上一拖然后我们去等待它的一个上传好那么现在就上传成功了那么我们就来去进回去的回到beast下面那么是不是有一个logstate的压缩包那么我们去做一个
[01:57] 解压xvf logstate然后呢去做一个解压那么解压之后呢我们就会得到一个logstate的一个项目然后呢我们就可以去做一些这个启动了做一些启动然后呢做一个运行就可以了那么我们来看一下进入这个logstate然后呢可以看到这个呢相对而言是一个标准的一个加码项目那么所运行的一些
[02:28] 这个运行命令呢是在这个bin这个下面啊所以呢我们需要通过这个bin下面的logstate去做一个运行然后呢我们指定一个-e就是一个这样的一个page然后呢去做一个去做一个测试吧那我们先来测试啊然后呢我们再去说一下它里面的这个这个到底是什么意思啊那我们先来做一个执行那么先看效果大家就明白了那么我们现在呢启动logstate那么由于启动logstate呢是比较慢的一个
[02:57] 过程因为他使用的是Java去开发的启动的是比较慢的这个也是一直有人比较诟病的这样的一个点就是就是说logstates的速度太慢了启动运行速度比较慢那么所以说他的一些采集的功能很大的一部分会被beats所代替掉
[03:19] OK那么现在你可以看到他慢慢的就跑起来了那么跑起来之后呢我们就可以在这个位置呢去做一个输入比如说输入一个hello然后呢你会发现他是不是会有一个输出那么当我们输入的是一个hello然后他会得到这样的一个输出那么我们输入的内容是在这然后他会放到这个message的这个里面来其他的是不是都会额外的给我们增加一些这个属性那么我们来回头来看一下他的一个这个命令
[03:47] 那么在这个命令我们是不是指定了input注意你看这个位置是不是有input然后是一个标准的一个输入然后后面是不是有一个输出
[03:56] 那么后面要有一个标准的一个输出那么有同学可能会比较奇怪了就说为什么在这个里面没有fail那么注意这个fail他并不是必须的就是说如果我们不希望对我们的数据做任何的一些这个处理的时候那我们是可以没有他的可以没有他的那么我们现在是不是就是你输入了一个hello然后呢我们返回的时是不是也是一个hello并没有做任何的一个处理ok好嘞那么
[04:22] 这个呢其实就是我们给大家所演示的这样的一个效果那么我们基本上第一个属于Hallowood级别的一个LuxTest的一个示例那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中安装、配置并启动 Logstash，并展示其基本命令行用法和数据处理流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示终端中 filebeat 的日志输出，包含系统监控指标（如 CPU、内存、磁盘 I/O）和事件统计。
- 日志文件路径：log/log.go.144。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 2：
- 终端显示 filebeat 服务已停止，日志中包含“filebeat stopped”。
- 执行了 `java -version` 命令，输出 Java 版本信息：Java HotSpot(TM) 64-Bit Server VM (build 1.8.0_141-b15, mixed mode)。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 3：
- 终端内容与画面 2 相同。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 4：
- 终端内容与画面 2 相同。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 5：
- 终端中执行了 `cd` 命令，进入当前目录。
- 执行了 `ll` 命令，列出当前目录下的文件和目录。
- 显示了 filebeat 相关的配置文件（如 `filebeat.reference.yml`、`haoke-es.yml`、`haoke-redis.yml`）和目录结构。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 6：
- 终端中执行了 `ls` 命令，列出 logstash-6.5.4 目录下的文件。
- 显示了 logstash 的 Ruby 库文件路径，如 `lib/elasticserach/api/actions/`、`lib/dotenv/`、`lib/edn/` 等。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 7：
- 终端中执行了 `ls` 命令，列出 logstash-6.5.4 目录下的文件。
- 显示了 logstash 的 SNMP MIB 文件路径，如 `RADIUS-ACC-SERVER-MIB.yaml`、`RFC1155-SHIT.yaml`、`RFC1213-MIB.yaml` 等。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 8：
- 终端中执行了 `ls` 命令，列出 logstash-6.5.4 目录下的文件。
- 显示了 logstash 的测试文件和模块配置文件，如 `spec/modules/arcsght/`、`spec/modules/azure/` 等。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 9：
- 终端中执行了 `cd` 命令，进入 logstash-6.5.4 目录。
- 执行了 `ll` 命令，列出当前目录下的文件和目录。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 10：
- 终端中执行了 `cd logstash-6.5.4` 命令，进入 logstash-6.5.4 目录。
- 执行了 `ll` 命令，列出当前目录下的文件和目录。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 11：
- 终端中执行了 `bin/logstash -e 'input { stdin {} } output { stdout {} }'` 命令，启动 Logstash。
- 显示了 Logstash 启动日志，包括创建目录、忽略配置文件、启动管道等。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 12：
- 终端中显示 Logstash 启动成功，管道已启动。
- 显示了 Logstash 的 API 端点信息，包括端口 9600。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 13：
- 终端中显示 Logstash 启动成功，管道已启动。
- 显示了 Logstash 的 API 端点信息，包括端口 9600。
- 画面左下角显示“Remote monitoring”和“Follow terminal folder”选项。

画面 14：
- 显示了 PDF 文档《讲义.pdf》的第 25 页。
- PDF 中包含 Logstash 数据处理流程图，从“Data Source”到“Logstash Pipeline”再到“Elasticsearch”。
- PDF 中包含 Logstash 命令示例：
  ```
  #检查jdk环境，要求JDK 8+
  java version
  #解压安装包
  tar -xvf logstash-6.5.4.tar.gz
  #第一个logstash示例
  bin/logstash -e 'input { stdin {} } output { stdout {} }'
  ```
- PDF 中包含“执行效果如下”字样。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5：
```
root@itcast01:beats# cd
root@itcast01:beats# ll
total 35839
drwxr-xr-x 6 root root 4096 Jan 15 23:13 ./
drwxr-xr-x 4 root root 4096 Jan 12 12:24 ../
drwxr-xr-x 14 root root 4096 Dec 18 19:45 module/
drwxr-xr-x 11 root root 4096 Dec 18 05:36 module/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096 Jan 15 22:03 logs/
drwxr-xr-x 2 root root 4096

