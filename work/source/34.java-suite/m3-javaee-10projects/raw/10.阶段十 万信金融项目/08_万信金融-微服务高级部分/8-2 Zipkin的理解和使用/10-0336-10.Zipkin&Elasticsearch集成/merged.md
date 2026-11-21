# 10.Zipkin&Elasticsearch集成

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-2 Zipkin的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-2 Zipkin的理解和使用\10.Zipkin&Elasticsearch集成_【海量资源尽在 666java.com】.mp4
- 时长 10分13秒（音频 613s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 前面呢咱们已经完成了Sluice跟Zking的一个集成测试整个效果呢也出来了但是呢这里边还存在着不完善的地方哪个地方不完善呢大家看这儿就是说Zking它是负责这个采集这个监控数据的对不对那它采集到了这个监控数据它目前是临时存储在什么呀内存里边存在内存里边那你想存在内存里边那就意味着它会出现什么问题让我们的服务器挂掉
[00:32] 或者说ZKing这个服务就这个服务我重启了你会发现你以前采集到的那些监控数据全都没了这个大家下去可以自己试你看我们刚才是不是又采集到了一些数据嘛对不对那你可以把这个服务给它干什么关掉然后再重启然后你这边再刷新其实你会发现那些数据就已经干什么对就已经没有了那我觉得这样肯定不行吧是不是那我将来某一天我要
[01:00] 我要通过Z King对吧做一些数据的分析哎我发现呢以前的一些数据已经没了我只能看到最新采取的一些数据那我觉得肯定不行是不是所以我们现在要干什么呀我们现在要实现把监控数据给它干什么呀持久化存储下来那比如说我可以存到MySQL数据库里边比如说我可以给它存到这个什么呀Elasticsearch索引库里边对不对那将来任何时候呢我都可以通过Z King去干什么呀去查询这个历史
[01:29] 对吧或者说所有的这个什么呀产生的这个监控数据我们要进行这个持久化的存储那我们接下来呢要给大家演示的就是如何把ZKIN采集到的这个监控数据呢给它存到什么地方存到Elasticsearch为什么要选择Elasticsearch呢这个大家都知道Elasticsearch呢作为这个全文检索这个工具的话它的这个查询效率或者说性能是非常好
[01:57] 而且呢这个Z King啊跟这个Elasticsearch他们之间的这个集成啊非常非常的简单啊大概呢其实只需要两个步骤就可以了咱一起看看呃首先你的手头上是得有一个Elasticsearch手头上还得有一个什么呀Z King的服务端啊当然Elasticsearch呢你最好要下载一个他的什么呀他的查证啊便于观察这个项目这些咱之前都讲过吧
[02:25] 那这里边有个细节就是需要大家注意Elasticsearch这个版本不能太新不能太新啊我们这说了不要超过6.0啊因为zking的目前对于较新版本的Elasticsearch这个适配啊或者说这个支持的还不是很好所以说你这个Elasticsearch的版本呢不要超过6.0超过6.0的话这个机身可能这个会会失败啊会失败那你呢手头上有了Elasticsearch啊
[02:55] 有了Z King之后呢其实就可以了啊接下来呢你就可以正常的像以前一样去准备干净启动Z King的服务段但是启动的时候呢我们要设置一些参数啊大家注意了你看我们前面在启动这个Z King服务的时候是不是就是加吧然后呢加上哪个参数啊-GAR是不是就把这个加包啊或者说这个Z King这个服务就给它启动了对不对但是呢这次呢我们是不是要
[03:24] 让他跟谁搞集成啊跟Elasticsearch那你想一下你要是要想让这个什么呀Zking把采集到的数据给他存到Elasticsearch里边那你想一下你在启动这个谁呀Zking的时候是不是得告诉他Elasticsearch这个服务的地址是不是这个最基本的信息你得告诉他这个信息他要是不知道的话那他采集到数据他就不知道该传给谁是不是所以说呢我们在启动这个谁呀
[03:52] Z King这服务的时候呢我们需要再加两个参数大家注意看就是我选中的这两个参数啊第一个参数就是Storage Type就是存储类型吧就是来设置啊你这个谁啊Z King要把采集到的数据持久化存储到哪个服务里边是存储到MySQL里边还是存储到什么呀ELASTIC SEARCH里边明白什么意思吧这是设置这个存储类型然后呢
[04:22] 第二个参数叫ES下完线HOST对不对这个大家一看就知道是设置ES TIG SEARCH这个服务的这个什么呀地址包括它的端口号那我们这个肯定都是本机对不对端口号默认9200所以说呢我们只需要在启动ZKING这个服务的时候呢设置一下这两个参数就搞定了就这么简单那么将来呢ZKING就会把采集到的数据自动往哪传对
[04:51] 往这个地址上来传那么也就是说它会自动呢就存到了什么呀存到了Elasticsearch当中那咱接下来呢测试一下那这个时候呢你就不能用传统的方式去启动这个什么呀ZKING对不对看看啊这边你看这个Elasticsearch我给大家提供了一个5.6.16的这么一个版本是不是我们把它解压出来
[05:29] 那我是不是首先要先把Elasticsearch给它启动一下对不对在这儿你要观察一下控制台看它有没有正常的给启动一下没问题吧然后呢我们的Elasticsearch是不是还有一个head插件对吧这个head插件呢我放到这个什么桌面上来head插件是不是相当于是一个前端工程啊我们怎么启动啊大家还有印象吗是不是叫npm转什么呀大对不对
[06:07] 这是这个黑的插件我们也启动成功了断口号9100然后呢接下来我们就可以启动谁对接下来最后我们要启动的就是这个谁啊对ZKing Server怎么启动呢这个命令就跟之前不一样我们刚才说了是不是又加参数我就直接沾过来了啊加了是不是这两个参数对不对那咱接下来的话就敲回车启动一下不能访问
[06:41] 好稍等一下啊我看看是不是后边这个jar 包的这个文件的这个名字是不是写的有问题我再重新拷过来一会在这对吧我们粘到这个后边哎没有粘过来呢好我们再重新复制一下啊然后呢再拿到这里敲回这好我们这个时候是不是就正常启动了啊我们看这个过程当中应该是没有报错对吧应该是启动成功好大家注意一下啊
[07:36] 目前的话我们已经把Elasticsearch还有header插件以及这个谁啊对Zking的服务器端呢全部都启动起来这个过程当中是没有报错的那咱接下来呢怎么测试你还是要发请求吧让它产生几次这个什么呀调用然后呢我们就通过header插件对不对看看它这里面是不是就已经把这个追踪到的这个什么呀日信息给保存起来我们还是访问这儿对吧这个呢我们说在这儿
[08:05] 这呢你还不行啊因为我们前面是不是这是不是报异常对不对我得把这行代码给它注视掉然后Service b呢重新启动一下这一定要注意啊我们要保证这个代码是没问题的在这种情况下呢我们进行测试Service b呢这边呢就马上就要启动完毕了启动完了Service a这边呢我们把控制台清一下就行了那接下来我是不是还是往这发请求就回事正常了是不是
[08:38] 然后呢咱怎么观察这个什么呀这个日志有没有被存到这个什么地方Elasticsearch里面那我们是不是通过header查证对不对啊访问这个9100就行好我们刷新一下哎大家看一下已经有了吧你看这名字很明显吗zkey对不对这是刚刚采集到的数据采集到了这是多少五条吗对不对那没关系我们进去浏览一下呗这是采集到的数据吗
[09:09] 你看这里边有没有我们能看懂的一些信息你看这有什么呀trace id嘛对不对trace id还有啥你看这里边是不是涉及到我们调用的那些什么呀微服的名字对不对Service-a呀Service-b呀还有这个什么呀时间戳time step还有这个什么呀请求的类型都是get请求还有什么呀还有这个什么呀parent id是不是还有这个时间戳等等等等
[09:40] 其实说白了还是相当于还是把他在这个什么呀这个地方用图形化展示的那些数据啊他全部都存到什么地方存到Elasticsearch这就是一个什么呀持久化的一个存储嘛你存到Elasticsearch里边你就不用担心这个数据会干什么呀会丢失啊所以说这儿呢就是我们给大家介绍了一下怎么着啊如何把zking采集到的这个日志信息给它持久化的保存到什么呀
[10:10] Elastique Search

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何将 Zipkin 与 Elasticsearch 集成，以实现监控数据的持久化存储。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档“3.3 Zipkin&Elasticsearch集成”章节，其中包含集成步骤：自行下载并启动 Elasticsearch 及 head 插件（注意：Elasticsearch 版本不要超过 6.0），并通过命令启动 Zipkin 服务端。命令为：java -DSTORAGE_TYPE=Elasticsearch -D ES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar。
画面 2: 同画面 1，内容无变化。
画面 3: PDF 文档中新增“3.3.2 集成测试”小节，内容包括：1. 再次通过浏览器访问 http://localhost:9021/Service-a/service1；2. 在 Ees-head (http://localhost:9100/) 中观察到产生了如下索引。
画面 4: 展示 Windows 文件资源管理器，路径为“.../warenhp2p/资料/”，显示 Elasticsearch 5.6.16 的安装目录，其中包含多个 .bat 文件和 .zip 文件。
画面 5: 展示 Windows 桌面，桌面上有多个快捷方式图标，包括“project.p...”、“wandp2p”、“Spring Cloud”、“elastic...”等，以及“黑马程序员”和“博学谷”的标志。
画面 6: 展示 Windows 文件资源管理器，路径为“.../warenhp2p/资料/”，显示多个文件，包括“zipkin-server-2.12.9-exec.jar”，并提示“在此处打开 PowerShell 窗口(S)”。
画面 7: 展示 Windows 文件资源管理器，路径为“.../Elasticsearch-head”，显示“Elasticsearch-head”文件夹的内容，包括 .gitignore、Dockerfile-alpine、package.json 等文件。
画面 8: 展示桌面，显示“zipkin-server-2.12.9-exec.jar”文件，同时在任务栏中有一个“Elasticsearch 5.6.16”的命令行窗口。
画面 9: 展示 PowerShell 窗口，显示启动 Zipkin 服务的命令行输出，包括版本信息、启动日志和配置参数。
画面 10: 展示 PDF 文档“3.3.2 集成测试”小节，内容包括：1. 再次通过浏览器访问 http://localhost:9021/Service-a/service1；2. 在 Ees-head (http://localhost:9100/) 中观察到产生了如下索引。同时，浏览器窗口显示“Elasticsearch http://localhost:9200/”页面。
画面 11: 展示 IntelliJ IDEA 开发环境，打开项目“SleuthWithZipkinDemo”，显示“ServiceController.java”文件中的代码。
画面 12: 展示浏览器窗口，地址栏显示“localhost:9100”，页面为空白。
画面 13: 展示浏览器窗口，显示“Elasticsearch http://localhost:9200/”页面，其中包含一个表格，显示了多个 span 的数据，包括“id”、“name”、“parentid”、“timestamp”等字段。
画面 14: 展示 PDF 文档“3.3.1 集成步骤”和“3.3.2 集成测试”小节，内容与画面 1 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1: java -DSTORAGE_TYPE=Elasticsearch -D ES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar
画面 3: http://localhost:9021/Service-a/service1
画面 9: java -DSTORAGE_TYPE=Elasticsearch -D ES_HOSTS=http://localhost:9200 -jar zipkin-server-2.12.9-exec.jar
画面 11: public String Service() {
String Service=serviceAgent.Service();
//System.out.println(1/0);
return "Service-b-Service" + "===" + Service;
}
画面 13: 表格数据：
| id | name | parentid | timestamp |
|----|------|----------|-----------|
| 35aec22138/beb51 | sleuth-with-zipkin-Service-b | 5990290058a0b51 | 1573138206281 |
| 5680330b5a014 | sleuth-with-zipkin-Service-a | 71ab753245aa1194 | 1573138205541 |
| 5090290058a0b51 | sleuth-with-zipkin-Service-b | 71ab753245aa1194 | 1573138205706 |

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“3.3 Zipkin&Elasticsearch集成”，内容包括“Zipkin默认是将监控数据存储在内存的，如果Zipkin服务挂掉或重启的话，那么监控数据就会丢失。如果想要搭建生产环境下可用的Zipkin，就需要实现监控数据的持久化。前面提到过，Zipkin提供了可插拔数据存储方式，如In-Memory、MySQL、Cassandra以及Elasticsearch。接下来演示如何使用Elasticsearch作为Zipkin的持久化方案。”
画面 3: PPT 标题为“3.3.2 集成测试”，内容包括“1. 再次通过浏览器访问 http://localhost:9021/Service-a/service1；2. 在 Ees-head (http://localhost:9100/) 中观察到产生了如下索引。”
画面 13: 表格数据如上所述。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

