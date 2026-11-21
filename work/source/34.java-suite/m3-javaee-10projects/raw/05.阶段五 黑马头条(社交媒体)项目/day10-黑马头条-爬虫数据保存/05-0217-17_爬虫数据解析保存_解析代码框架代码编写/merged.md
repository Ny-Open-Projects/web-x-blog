# 17_爬虫数据解析保存_解析代码框架代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\17_爬虫数据解析保存_解析代码框架代码编写【海量资源尽在 666java.com】.mp4
- 时长 11分28秒（音频 688s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好嘞那咱们下面呢就来去解析或者叫编写咱们当前的一个类啊这是一个词类是当前这个Obsrack的html pass people line然后是他的一个词类在这呢去创建一个包创建一个包啊impl然后呢你就可以在这去创建一个类这个类就叫做caller html pass people line
[00:25] 他并不是抽象的咱们下面这个是抽象的好直接点ok让他干嘛让他去继承谁呀继承当前的HubbleStack的ST.A.C.E.然后是HTMLPathPlan他需要一个范型这个范型就是ColorWLAR PathItem好我们要去重写他的方法
[00:57] 这三个三个啊首先呢你得让他让死不润去管理然后呢是log4j2加上好吧那这里边啊里边刚才说了啊这个是一个前置的处理参数啊其实最核心的方法是这个啊最核心的方法这个啊这个是啥呢这个是个优先级怎么可以是这个1000或者10000都可以啊无所谓用啥呢是最后处理的你只要是大于120 130大于130啊
[01:22] 到130的话他就是放到最后一个所以说你到130的值都可以现在是这里1000完全OK了行那这个这个参数咱们咱们一个个去写咱们先写这个好吧先写这个那为什么会有这个东西咱们再去说一说其实咱们再去处理的时候就是前置参数处理这里边主要主要是有一个叫做read count
[01:56] 看呢很显然是读的一个什么就是到底是读了多少次是吧阅读量啊有这个阅读量的统计阅读量统计呢它最终的是在文章中去爬取的时候是阅读数它有可能是这么保存的啊这么爬的阅读数然后空格比如说200这么着但是呢咱们呢不需要那么多咱们要干嘛呢咱们只需要200就可以不需要这个阅读数
[02:25] 所以说呢咱们去拿的时候呢咱们要去单独去把这个给处理一下处理完之后呢再去保存到当前那个passitem中是这么一个东西啊好那咱们在这怎么做呢你可以去通过当前item.getget谁呢就是当前的readtank这个不能写错啊你要是不知道怎么写的话你可以查看一下之前的代码最终呢你把它转成一个死准转成一个死准啊
[02:55] 转成str的话,咱们可以直接通过一个工具列就可以工具列是叫什么?
[03:02] hmstr utils.toString把它装进去装进去之后,它就是返回了一个readCount然后咱们就可以判断说readCount不等于num不太合适,咱们可以直接用工具列str utils.isNotEmptyReadCount
[03:27] 如果它不会空的话呢这时候呢我们就可以去切割一下切割之后呢要几啊要200不要阅读数阅读数是不是就去掉了所以说咱们在这啊怎么着read count加suprate然后呢咱们以什么风格呢控制啊我们取一个取一个也就是取第二个它返回的就是一个不是read count你可以直接负加值啊比如咱们还是要它啊
[03:59] 好还是叫他不用再去重新试这个变量了好吧按的话就重新复制之后呢就只拿了200拿了200之后啊这时候呢咱们可以干嘛呢就可以再重新收拾进去啊再去判断一下striptutils.isNotEmpty然后是readCount如果他不会空的话啊解写完之后还是不会空这时候呢咱们就可以item.setputkey呢就是他
[04:31] 然后呢然后下面是V的那这样的话咱们这个前置的参数啊就算是设置完了那这个设置完了之后啊咱们下面还有一个方法是吧把这个方法也写一下啊先去把这个大概的思路写一写然后呢一会具体的时候咱们可以再具体去写啊那这个呢就是干嘛是要数据处理的入口入口啊
[04:57] 这个不可能把所有的数据处理写到这是吧那肯定是不合适的这个咱们可以设置改成fabric这个也是设置完之后咱们在这就可以去解析那你该怎么去解析呢因为现在你已经拿到数据了咱们可以再看一下这个东西拿到数据之后你看这获取的数据了你是不是得判断正向或者是反向然后解析出去
[05:28] 然后保送文章保存附加信息然后最终是保存评论和发送消息对吧OK啊那咱们呢就按照这个思路去写首先呢你还是得去打印点这一会就不再多说了啊咱们之前经常写啊你可以直接在这点info当然咱们可以开启现场啊开启现场去做啊开启现场这时候呢咱们就可以去设置啊说将数据
[06:00] 将数据加入现成池现成池进行执行好URL是啥试着一个然后下面是有一个handle typehandle type少了一个er是吧handle type是谁?
[06:24] 冒号他然后是怎么着power bus itemget URL然后下面还有个什么
[06:37] sitem.gethandle试试完了试试完之后咱们就可以去用callerpoolcaller p-r-a-w-e-r然后是有一个threadpool点什么呢有一个叫submit里边咱们就可以去设置一些东西少了一个括号一个公号这个咱们就可以这里边去写代码
[07:10] 首先去判断是正向正向那这个正向或者反向那怎么去判断呢是不是咱们有一个叫做$enumer.handletype.forward.name然后它等于谁啊.ecos
[07:45] 就是当前passitem中的gethandletype如果说是forward的话那就是正向否则的话呢就是反向最好咱们是这样去多做一步判断还是这个东西好呗这个就不是forward了叫什么reverse好吧这个是reverse那这个是反向那我就不再去写了这是正向那这个就是反向了
[08:20] 那正向干嘛呢正向咱们之前是不是说过正向是叫添加数据是吧正向是要添加数据吧添加一系列的数据啊我们不可以去封装成一个方法叫passitemmessage好那这里边其实还了很多包含什么呢包含了咱们的怎么去保存文章保存附加信息保存什么还有一个就是评论还有发送消息咱们统一都封装到这个里边就可以了
[08:51] 行那这是一步啊我们把这个方法给创建出来OK这是一个方法那这个呢这个的话其实咱们要去更新updateaddi然后是tionl是吧我们要更新additional更新的这个数据这个呢其实参数也是一样参数也是当前的passitem那咱们在这儿也可以去记录一些日志啊比如说log.info
[09:21] 这是开始处理消息URL是啥每次标记记录是handletype然后是他这个还是要去写的passitem.getURL然后是passitem.gethandletype那这个设置完之后还要再继续写拷贝一拷方法没有咱们先去创建出来
[09:56] 出来之后呢咱们在这啊他都都去设置结束了结束之后呢你可以在这去设置一个参数参数呢就是参数啊只要去打印日志啊咱们要去处理什么处理文章数据结束这个URL和HandleTime都需要下面还有什么呢还有一个号时号时
[10:29] 有个少一个是吧在这去搭上前的system.r.r.那这个咱们就算是设置完了啊很好那这个咱们就写到这儿这个是整体的架子起码出来了下面咱们分别的去设置当前的这两个啊怎么可以在这写住是吧保存那这样是吧放下这是逆向啊逆向更新
[11:07] 文章附加信息这个呢是正向保存数据发送消息那这个咱们就先说到这一会儿咱们再去编写具体的内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 CrawlerHtmlParsePipeline 类的实现细节，包括如何处理爬虫解析后的数据、设置优先级、前置参数处理以及根据 handleType 分发消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“3.8 CrawlerHtmlParsePipeline类”的标题和内容，说明该类用于解析后的数据存储，因数据量大，需控制并发线程数。
画面2：在IDE中展示 CrawlerHtmlParsePipeline 类的继承结构，它继承自 AbstractHtmlParsePipeline。
画面3：展示 CrawlerHtmlParsePipeline 类中的 getPriority() 方法，返回值为 1000。
画面4：在 preParameterHandle 方法中，使用 StringUtils.toString 获取 readCount 字段值。
画面5：在 preParameterHandle 方法中，对 readCount 字段值进行 split 处理。
画面6：在 preParameterHandle 方法中，将处理后的 readCount 值存入 itemAll。
画面7：展示一个流程图，内容为：是否匹配 -> 获取对象 -> 解析数据 -> 保存文章 -> 保存数据消息 -> 结束。
画面8：在 preParameterHandle 方法中，使用 log.info() 输出日志。
画面9：在 handleData 方法中，记录当前时间戳，并使用 CrawlerThreadPool.submit() 提交任务。
画面10：在 handleData 方法中，使用 CrawlerEnum.HandleType 判断 handleType。
画面11：在 handleData 方法中，根据 handleType 判断是否为 REVERSE 类型。
画面12：在 handleData 方法中，调用 addParseItemMessage 方法。
画面13：在 handleData 方法中，调用 additional 方法。
画面14：展示 updatedAdditional 方法和 addParseItemMessage 方法的定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.heima.crawler.process.parse.imp;
import com.heima.crawler.process.parse.AbstractHtmlParsePipeline;
public class CrawlerHtmlParsePipeline extends AbstractHtmlParsePipeline(CrawlerParseItem {
```

画面3：
```java
@Override
public int getPriority() {
    return 1000;
}
```

画面4：
```java
String readCount = StringUtils.toString(itemAll.get("readCount"));
```

画面5：
```java
readCount = readCount.split(regexp)[1];
```

画面6：
```java
itemAll.put("readCount", readCount);
```

画面8：
```java
log.info("开始处理消息，url: {}, handleType: {}", parseItem.getUri(), parseItem.getHandleType());
```

画面9：
```java
long currentMillis = System.currentTimeMillis();
log.info("数据加入线程池进行执行。url: {}, handleType: {}, parseItem.getUri(), parseItem.getHandleType());
CrawlerThreadPool.submit(() -> {
```

画面10：
```java
if (CrawlerEnum.HandleType.REVERSE.name().equals(parseItem.getHandleType())) {
```

画面11：
```java
} else if (CrawlerEnum.HandleType.REVERSE.name().equals(parseItem.getHandleType())) {
```

画面12：
```java
private void addParseItemMessage(CrawlerParseItem parseItem) {
```

画面13：
```java
additional(CrawlerParseItem parseItem) {
    addParseItemMessage(parseItem);
```

画面14：
```java
private void updatedAdditional(CrawlerParseItem parseItem) {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面7：流程图结构如下：
- 是否匹配 → 获取对象
- 获取对象 → 解析数据
- 解析数据 → 保存文章
- 保存文章 → 保存数据消息
- 保存数据消息 → 结束

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

