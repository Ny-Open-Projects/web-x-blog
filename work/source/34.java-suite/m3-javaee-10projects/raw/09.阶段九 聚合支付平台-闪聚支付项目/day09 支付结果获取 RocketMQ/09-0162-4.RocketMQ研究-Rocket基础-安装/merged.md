# 4.RocketMQ研究-Rocket基础-安装

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day09 支付结果获取 RocketMQ
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day09 支付结果获取 RocketMQ\4.RocketMQ研究-Rocket基础-安装【海量资源尽在 666java.com】.mp4
- 时长 14分0秒（音频 841s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来安装RocketMQ那首先我们看环境要求那么RocketMQ是Java开发的这里边呢我们要先装JDK要求1.8以上然后另外呢我们为了方便我们进行编译啊打包然后呢我们也要有这个Maven3.2以上版本然后呢那就是操作系统了对吧操作系统Windows Linux都支持啊那么当前课程我们是在Windows上进行操作好
[00:28] 首先呢我们需要下载这个Rocket Amicro这里边我们本课程用的是4.5.0版本然后呢你下载然后在资料文件夹下边其实我给大家已经提供好了在这儿大家看到是吧然后呢那如果我们下载到了或者是你直接从我资料文件夹拷贝走之后呢你接下来就要去解压对你把它解压解压到一个没有空格没有中文的目录这就是它的一个解压目录好了那下面呢我们就把它解压开来
[00:58] 我就解压开了就是这个目录了大家看到了吗那么在这个目录当中在这个目录当中其实你主要关注的是什么呢BIM目录里面是不是有很多的执行脚本对那其他的目录还有一个配置文件目录其实关注这两个就行了那这个jar 包这个你一般就不用管它里面是它执行的依赖的一些jar 包好那么这几个目录这几个目录你主要关注的是BIM里面有很多我们的这个执行脚本以及configure那各位我们现在要启动怎么做
[01:27] 其实你先不要着急因为我们在启动之前先要配置一些东西首先第一点那默认的这个RocketMQ它启动的时候它启动参数的这个内存呢它就设的比较高所以呢大家呢这个电脑呢它这个内存呢可能就不是很大所以呢我建议你开发环境把内存调小一些它的这个方法呢那我们打开在这个各位看啊在闭幕录像
[01:55] 在并目录下边呢这里边呢我们主要看啊你就看我讲义就行了首先找到这个有一个叫runserver.cmd因为现在我是在windows环境下对吧我是找扩展名是cmd那你如果是在linux呢那你扩展名叫sh的是吧sh好那现在呢我们就找到这两个啊这个runserverrunserver又说老师runserver这个是干啥的呀你刚才我们学过这个RocketMQ的结构吗一个它有一个name server
[02:24] 对不对还有一个broker所以其实你现在猜也能猜得到对吧这个呢是内部server的配置下面是broker的配置好那我们来看吧那这里边呢你看它是不是有好多的这个设置环境面量呀那这里边呢按照老师讲义上边的要求注意看这儿有一个叫set对java opt看然后呢后边这一堆你把它复制下来对复制下来有说gon servergon server一直到这儿然后呢我们把它贴到咱们的这里头
[02:53] 从这开始贴一直贴到这看见了吗保存然后呢还有找到RAM broker这个呢就是我们真正干活的人RAM broker就是他呢里面有消息堆裂对吧好我们找到找到仍然重复相同的动作找到我们要粘贴的地方这第一个在这你找到了吗在哪呀
[03:23] 那其实它有好多你没发现吗有好多那你我们得找一个哎这个杠server看见了吗杠server然后呢它这有一个叫哎你看1g你看是不是都是设的是1g的内存啊那哎你其实是可以对找到它的这个这一点来我们把它拿拿过去就是run broker然后呢这有人说老师这个
[03:50] 后边呢这是我们说这个设置的加码的内存这个我们都知道但是前边这一串是啥意思看不懂我给大家讲一下前边这个呢在我上面有说明说什么呀这个broker呀他呢这个你把它解压到你的这个磁盘上他会自动检测你这个磁盘的利用率对吧如果你这个磁盘的利用率达到85%了也就是用了85%了那这个时候那你往里边发消息就发他就不再接收了就会报错
[04:20] 那你也知道我们作为开发环境我们电脑呢可能就空间利用率肯定当前可能就用的很多了剩余的空间很小这时候呢我们还想让Broker去工作这个时候呢我们就要把它设的对稍微大一些假如说我们的设到这个0.98那就相当于你的利用率到达98%他才进行报警不再接受消息大家理解我这个用意吗那你不要你默认是85%很有可能你这个磁盘呢
[04:50] 你把这个RocketMQ考到你的这个磁盘上边可能都已经超过85%了这时候呢它是不能工作的啊咱们把这个参数给它设置一下好那么这个设置好了之后呢下面我们就可以启动咱们的这个消息队列了启动的方式非常简单看好刚才你设置的这俩文件呀咱们把它关掉然后呢再回到闭幕录那启动的话首先我们要启动谁呀你告诉我是broker还是内部server启动哪个
[05:20] 启动哪个都行但是通常呢我们先启动什么呀Name serverName server呢在这儿看见吗在这儿那么我们呢就双击这个mcrv name你看mcrv name srv对吧它缩写了是吧就双击它来启动好启动起来就不要管它了然后呢我们还要启动一个broker对吧broker那这个broker我们因为你要知道我们去启动broker就没那么
[05:51] 简单需要带一个什么需要带一个参数这个参数是啥呢就是你想Broker是不是要把自己的状态报给Name Server因为Name Server我们说它是一个注册中心所以你要带一个参数叫-n然后后边127.0.0.1是我们本地的IP对吧然后默认Name Server它的端口是9876回车这样的话Broker就可以起来了对
[06:20] 我们回到讲义就是按照讲义上说的方法就把它起来了起来了之后各位我们说那到底能不能用呢我们是不是就可以测试一下那怎么测试呢那测试方法很简单就思路很简单就是你向broker发消息就你弄个生产者然后再造个消费者一个发一个接收如果说我能发消息还能接收消息那不就OK了吗就说明这个消息对了可以用了吗是吧那怎么做呢
[06:49] 看好它里边正好有一个工具CMD看见了吗这个工具CMD它的这个好处呢就是我们可以利用它来执行一些什么执行一些测试的这个类这个测试的类在哪呢你注意看啊在它的jar 包里边有一个这个jar 包各位它的目录结果大家还有知道是不是有一个类吧它这里边有一个叫做example看见吗里边呢有一个类
[07:19] 这个类呢就是一个专门让你用用来测试一个生产者的类啥意思啊对我们呢准备要发消息了准备发消息了那发消息你回车试一下看好哎看见了吗报错了这就说明现在它是有问题的就是这个消息它是不能正常发送的没错了吧哎哎那你说这是啥你看no name server address你看见吗
[07:50] 但是他没有这个地址你看见吗对我们还是按照讲义上来你首先你要调用这个兔子CMD的时候啊你前边呢得设一个环境变量是吧也就是说这个生产者也需要去访问Nameserver我们前边其实介绍他的组成结构应该我给大家说过生产者是不是要从Nameserver去拿到Broker的地址啊对你先要set一下然后再来执行各位
[08:19] 消息发出去了你咋知道呢你看他的日志就打出来了嘛send ok是吧然后呢这是消息的ID那这个消息到底发送成功没有那我觉得你用怎么样你用消费者去接受一下我觉得比较好对吧你这样能接收到了就说明咱们这个消息真的发出去了对不对所以我们再来打开窗口然后呢还运行刚才的命令只不过现在呢这个类名换成consumer了看见了吗
[08:47] 当然我们你运行的话先不着急还是我刚才说的消费者他要监听堆裂他也需要知道内幕server的地址所以你也需要set一下懂了吧这个时候各位我们再来启动这个时候呢消费者你看消息都消费了但是这个消费者你没发现吗他还在这停着呢因为他是要监听的你看
[09:14] 这个光标还在闪对吧但是生产者我告诉你他呢都已经看都已经执行结束了两个窗口左边消费者右边生产者看好啊我现在准备让他发了这个消息一旦发出去消费者就立即能接受看好两个窗口同时滚动看见了吗也就是右边在发左边在搜那么我测试到这儿就说明我们的Rocket MQ都已经安装成功了
[09:45] 那么光安装这个呢哎你说这个黑窗口看起来很不舒服对吧我们还有一个管理端很好的一个管理端就是图形界面啊那你下载管理端的源代码哎然后呢进行编译打包然后运行因为这个管理端呢它只有源码所以我们因为它是Maven做的嘛所以我们用Maven把它打包打成一个jar 包然后呢运行jar 包就行了那这个呢我给大家已经提供了一个什么哎压缩包对吧咱们把这个压缩包呢咱们把它解压就行了
[10:14] 好那么我们把这个压造包呢解压开来到老师的这个这个目录当中我把它解压到这儿啊这是我解压的解压到这之后呢我们就需要按照讲义上要求的来运行一个命令首先呢我们要改一些配置啊因为大家看啊这个我觉得大家都非常熟悉因为它是圆码嘛并且是Spring Boot的你看打开
[10:37] 这个管理端他也需要去连接name server是吧所以这里边呢你是需要去配置一下他的这个什么这个name server的来看一下我们的这个讲义他在哪里啊在哪里在这对吧在这那我们搜一下哎你看我这没有配置没有配置可以他默认是127.0.19876懂吧对如果你说我想练远程的一个name server那你这就必须配了啊还有一个他是一个什么你看
[11:09] 它是一个web服务8080端口web服务还有就是它的日志呢我们可以让它设置一个专门存放它这个数据的一个目录啊这个是它的一个数据的一般来说我们不要管它啊因为它是一个管理端我们只要随便配一个目录这个目录的空间够就可以了好这个弄完了之后呢我们现在就开始打包了打包的方法非常简单这个命令我相信大家也都见过吧
[11:38] 其实就是Maven的packagingpackage之前先清理一下对吧然后后边你也知道它还有可能有很多的这种单元测试的类我们呢让它跳过不要执行直接打包打包的方法你需要复制这个命令然后呢进入到刚才我们说的这个源码当中POM文件所在目录啊这是我们Maven学的知识然后执行这个命令它就开始去干嘛打包懂了吧就打包那这个呢它要联网
[12:06] 对它要下载jar 包那这个过程呢我就不再演示了然后呢我们打包成功之后在Target的下边就有一个jar 包看见了吗这个时候因为它是个Spring Boot的工程我们只要运行这个jar 包就可以了怎么做进入CMD然后呢把它放进去运行各位刚才我们修改配置文件的时候它的web的目录叫9877是吗不是吧这个你可以看一下看一下啊
[12:36] 看一下啊我的讲义上写的是9877但是这儿我好像没有改还是8080看见了吗所以当它启动起来之后我们就可以看好9877啊9877我们还得看这个配置文件配置文件在哪呢看在这儿吧这儿讲义上写的9877对吧但是呢我们的配置文件是8080怎么回事呢
[13:09] 千万记着因为刚才我的一系列操作都是直接复制讲义上面的命令对吧这个命令是啥意思呀我们运行一个jar 包然后呢后边给他传参看见了吗我们传的这个参数指定的是9877对吧包括后边传的参数你看你看这是啥name server的地址对吧好我们把它刚才已经复制到这个我们的这个CMD命令行是不是运行它然后呢起来起来了之后各位这个9877的端口是不是就有了
[13:37] 大家理解吗是因为我在运行的时候呢给他传了一个9877好那现在呢我们就可以来访问他这就是我们的这个管理端对吧管理端好那么整个的界面呢他是支持简体中文的回头我们需要去看里面的内容呢我再带着大家来学习到这整个ROCK的MQ的安装的内容我们就安装完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Windows系统上安装、启动RocketMQ服务并使用其管理控制台。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT中“2.2 安装RocketMQ”章节，列出环境要求（64位JDK 1.8+、Maven 3.2.x、64位Windows系统）和下载地址（http://archive.apache.org/dist/RocketMQ/4.5.0/RocketMQ-all-4.5.0-bin-release.zip），并显示解压后的目录结构（benchmark, bin, conf, lib, LICENSE）。
画面2：显示解压后的文件夹内容，包含多个JAR文件，如RocketMQ-broker-4.5.0.jar、RocketMQ-client-4.5.0.jar等。
画面3：显示解压后的bin目录内容，包含多个脚本文件，如mqnamesrv.cmd、mqbroker.cmd等。
画面4：显示RocketMQ-all-4.5.0-bin-release\bin\runbroker.cmd文件内容，包含设置JAVA_HOME、环境变量和启动参数的配置。
画面5：展示PPT中“2.2.3 启动”章节，说明启动NameServer和Broker的命令（cd到bin目录，执行mqnamesrv.cmd和mqbroker.cmd）。
画面6：展示PPT中“2.2.4 测试”章节，说明发送和接收消息的命令。
画面7：显示发送消息的命令行界面，执行tools.cmd -cp ... Producer。
画面8：显示接收消息的命令行界面，执行tools.cmd -cp ... Consumer。
画面9：显示接收消息的命令行界面，输出多条“Receive New Message”信息。
画面10：显示解压后的RocketMQ-console-1.0.1.jar文件。
画面11：显示RocketMQ-console-1.0.1.jar的源码文件夹结构，包含application.properties、logback.xml等配置文件。
画面12：显示RocketMQ-console-1.0.1.jar的target目录内容，包含编译后的JAR文件。
画面13：显示RocketMQ-console-1.0.1.jar的src/main/resources目录内容，包含application.properties、logback.xml等配置文件。
画面14：展示PPT中“2.2.5 安装管理端”章节，说明启动管理控制台的命令（java -jar RocketMQ-console-ng-1.0.1.jar --server.port=8877 --RocketMQ.config.namesrvAddr=127.0.0.1:9876）和访问地址（http://127.0.0.1:8877），并显示管理控制台的界面（Broker TOP 10和Broker Smith trend图表）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```
set JAVA_HOME=D:\Program Files\Java\JDK 8.0_201
set BASE_DIR=%~dps0
set BASE_DIR=%BASE_DIR%\RocketMQ
set CLASSPATH=%BASE_DIR%\conf\%CLASSPATH%
set JAVA_OPT=%JAVA_OPT% -server -Xms4g -Xmx4g -Xmn2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=512m -XX:SurvivorRatio=8 -XX:MaxDirectMemorySize=2g -XX:MaxHeapSize=4g -XX:NewRatio=3 -XX:NewSize=1g -XX:OldSize=3g -XX:ReservedCodeCacheSize=256m -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:+UseG1GC -XX:+UseTLAB -XX:+UseBiasedLocking -XX:+UseAdaptiveSizePolicy -XX:+UseCodeCacheFlushing -XX:+UseCompressedOops -XX:+UseConcMarkSweep

