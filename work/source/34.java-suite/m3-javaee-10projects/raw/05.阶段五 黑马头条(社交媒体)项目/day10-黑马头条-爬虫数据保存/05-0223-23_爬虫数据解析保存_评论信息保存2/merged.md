# 23_爬虫数据解析保存_评论信息保存2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\23_爬虫数据解析保存_评论信息保存2【海量资源尽在 666java.com】.mp4
- 时长 9分23秒（音频 564s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面咱们就来去完成当前这个方法这方法是干嘛的呀这是解析评论数据是吧主要的是你请求完之后呢他会去拿到当前的这么一个数据然后你只要解析解析完之后呢是存到当前的考冒的这个对象中最终的是返回就可以了啊当然最终要去返回一个列表啊因为有可能这个这个这是个例子嘛有可能你的评论是有多条是吧那这个怎么去怎么去设置啊
[00:29] 现在拿到的是这么个东西这么个东西那你怎么拿呢来看一下啊咱们在这先去得先去判断啊先去判断那什么东西啊先去判断这个东西不能为空啊不能为空然后是死尊u2死亡是impedy如果说他是not啊是impedy如果说他是为空的话呢json date这时候呢咱们直接去returnnone就可以了是一个
[00:59] 没问题下面如果说他没有事的话咱们下面就可以去真正的去解析最终解析咱们要去存到一个哪存到当前的集合中是吧我可以先在这去准备一个command list就等于你有一个read它拿到之后咱们就可以去先去解析比如说咱们用json.有一个pass objectpass
[01:30] 然后你就把它当成这个 json date 进去它最终呢就能拿到一个 json objectjson object 啊我们这里边就可以去拿数据了啊怎么报错呢我看看啊没有没有问题啊然后呢怎么办呢然后呢咱们就可以去呃把它呢是嗯说的啊我看啊咱们可以去拿纸了就啊拿拿纸json object点儿咱们有一个 get objectget object 啊这 key 谁呢
[02:03] 这key的话就是date,你可以看一下,上面是不是date这是个对象吗?
[02:11] 拿到这个date然后转成什么类型呢?
[02:15] 你可以去设置一个比如说我要去转成一个map,转成一个map,第二class最终它就能去返回一个map当然这个map咱们就叫map好吧它这个值咱们可以在这去设置一下有点卡,我把这个先关了好
[02:35] 这个key是这个value是一个object拿到它之后拿到它之后相当于拿到了当前的这东西拿到之后咱们下面就可以再继续往下拿继续往下拿咱们可以map.get是谁呢最主要的是拿到一个map中的一个list一个list这个呢
[03:01] 这个好像是是啥咱们用它说啊你看这里边是不是有一个集合呀是不是一个集合呀所以说呢你在这啊去强转成一个集合就可以了咱们叫json arrayjson array好这个值呢咱们叫做json array吧json array啊嗯行那就强转一下啊好那这样就没事了啊下面呢咱们就来去判断也就是说应该是去循环里边的值是吧那不等于
[03:37] 前的json array的话然后下面咱们就可以去循环了那这样你要是感觉操作这个不方便的话呢你也可以去json array.toJava list你也可以把它转成Java list什么呢转成一个map转成一个map.classmap.class它这样的话就转成了一个list里边是一个map咱们叫date infolist叫date info list下面呢你就可以去循环
[04:10] 这个最好是给一个范形最好是给一个范形这个范形的话第一个呢是第二个是object那的话你就能去拿具体的值了能拿具体的值啊那拿谁的咱们可以这样啊datinfo.getget谁呢这个info有可能是有多个你看一下啊info一个
[04:42] 有可能是有多个啊是有多个这时候你拿到一个之后呢拿到一个之后啊咱们最终的是拿到了一个jsonobject这个是一个jsonobject这个呢咱们叫info object好吧info object这个呢咱们也要去强转一下这时候呢你就可以去
[05:17] 我可以去把它呢再去转成一个这种MAP的一个东西啊它BR2 our object看到了吗最终你是发转成一个MAP好操作啊这个呢咱们可以起个名咱们叫做infoMAP吧好吧infoMAP感觉比较乱啊其实咱们为了转换一下这样是操作起来比较方便啊大家一定要跟上这个思路啊好里边有个object
[05:45] 好拿到它之后啊最终呢咱们就能拿到了某一个对象是吧拿到某一个对象的话那就比较容易了啊你这样info.map.set当前的某某某哪个哪个呢比如说你要去拿commentcontent那就直接去content就能拿到一个内容行那这样咱们就直接去往里边去存就可以了咱们在这去创建一个seriesnews command我说怎么叫
[06:15] comment 等于一个new一个seriesnews command然后就可以往comment中去设置点set content有一个content是吧你就把当前这个info装进去报错是吧因为报错是原因它是一个object它并不是一个spin类型的所以说你在这怎么用一个工具来转换一下叫 hmspin-utils.2.js你就把后边这个东西
[06:47] object转成一个json就可以了转成一个sprint就可以了这样的话咱们就算是设置了第一个咱们可以再去两个当然这样加好像不太合适是吧手写 command.set咱们还有什么set一个username这个其实咱们可以拷贝一下拷到这这是谁这个的话就是username那就是当前这个username拷贝过来大家要写一定要区分
[07:22] 然后再来一个comment一个叫做我看看应该是这个时间是吧应该是评论的时间我们把这个评论的时间给加上评论时间其实这里边咱们还是有问题它这个不能直接去转成什么呢转成一个字幕块是吧首先要先去处理一下先去处理一下
[07:52] 怎么拿呢还是这么去拿还是这么去拿来看一下点这么拿不行是吧你可以先把这个值给拷过来拷到这拷到这之后呢它是一个字符串字符串的话最终呢你要把这个字符串呢转成一个date咱们可以再用另外一个工具来试一试啊date utils点点一个stateok啊把这东西呢给放进去就可以了
[08:31] 好他返回的是一个date然后这时候你就可以往当前这个对象中去装这个date就可以了drset有一个command date我可以把这个date装进去好那这样的话咱们就算是设置完了设置完之后下面还有一些值咱们再去设置一下drset create就是目前时间你用一个date然后最终的你用这个
[09:00] 对象装到这个一和中点add好最终呢你把它给返回就可以了直接回tun往前的amount list那这样的话他们这个评论的这一块内容呢咱们就算是完了啊我看这儿啊没有问题好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 代码中解析 JSON 格式的评论数据，并将其转换为自定义的 CINewsComment 对象列表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 CrawlerParsePipeline.java 文件中分析评论数据的主方法调用，以及方法签名。
画面 2: 代码光标移动到分析评论数据方法的开始处，方法上标注了 @Nullable 注解。
画面 3: 代码光标移动到 JSON.parseObject(jsonData) 方法调用处，显示了 JSON 解析的上下文。
画面 4: 切换到终端窗口，显示了 MySQL 连接的详细日志信息。
画面 5: 代码光标移动到 JSON 解析后的 Map 对象，准备提取 "list" 字段。
画面 6: 代码光标移动到 JSONArray 的 toJavaList 方法调用处，显示了将 JSON 数组转换为 Java List 的过程。
画面 7: 切换到在线 JSON 编辑器，显示了从 json.cn 获取的评论数据的 JSON 格式。
画面 8: 代码光标移动到 JSONObject 的 toJavaObject 方法调用处，准备将 "info" 字段转换为 Java 对象。
画面 9: 代码光标移动到 CINewsComment 对象的 set 方法调用处，准备设置评论内容。
画面 10: 代码光标移动到 CINewsComment 对象的 set 方法调用处，准备设置评论用户名。
画面 11: 代码光标移动到 CINewsComment 对象的 set 方法调用处，准备设置评论发布时间。
画面 12: 代码光标移动到 CINewsComment 对象的 set 方法调用处，准备设置评论内容。
画面 13: 代码光标移动到 CINewsComment 对象的 set 方法调用处，准备设置评论内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
String jsonData = getOriginalRequestJsonData(BuildCommentUrl, parameterMap: null);
//解析获取的json数据
List<CINewsComment> commentList = analysisCommentJsonData(jsonData);
return commentList;
```

画面 2:
```java
@Nullable CharSequence cs
private List<CINewsComment> analysisCommentJsonData(String jsonData) {
    if (StringUtils.isEmpty(jsonData)) {
        return null;
    }
```

画面 3:
```java
@Nullable String text
@NonNull String text
@NonNull String json
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull String type
@NonNull String input
@NonNull

