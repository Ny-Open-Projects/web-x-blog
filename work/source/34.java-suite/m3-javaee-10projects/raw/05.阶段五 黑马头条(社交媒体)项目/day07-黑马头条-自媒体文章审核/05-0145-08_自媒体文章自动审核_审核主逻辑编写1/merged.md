# 08_自媒体文章自动审核_审核主逻辑编写1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\08_自媒体文章自动审核_审核主逻辑编写1【海量资源尽在 666java.com】.mp4
- 时长 9分57秒（音频 597s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来完成他这个Service的编写右层刚才咱们已经把这个mypool所有的mypool都已经准备完了那这时候咱们要去写代码了啊那个代码在哪写呢刚才咱们说了啊就是你审核文章的时候应该是在admin端去干嘛呢admin端去进行去审核是吧所以说咱们在这在admin端呢去创建咱们的mypool或者专门的Service啊打开当前的哪
[00:29] 当前的admin然后在这去创建一个Service在这就创建然后在这去创建一个什么样的类叫review然后是media article Service好吧名字有点长是一个接口ok然后这是下面去写一个方法publico是咱们是void但是void没有任何返回值然后是叫什么o2叫o2什么review
[01:12] review article在谁呢在media其实咱们后期还有啥呢还有当前的这种比如说咱们后期要去做一个这种发虫是吧发虫里边咱们也要去审核这接收的什么接收的就是一个news当前一个文章的it然后呢这里边怎么写是什么是自媒体自媒体发布文章
[01:46] 自动审核自动审核下面咱们就来去写一个Service的实现类在这去写在这去创建一个Service是mpl是吧前面不用加了是吧这是一个类好ok然后下面咱们就来去让他去实现的结果implement然后当前这个Service导演pull
[02:19] 那这样就好了啊然后下面咱们在这去加一个吗一个Service让他去让死不认去管理然后再去加一个super one啊防止爆错是吧那好那这个咱们就准备好了准备好之后呢咱们下面来去写的这又到底该怎么写那这样咱们还是要去看当前的这个这个逻辑或者这个流程是吧首先呢咱们要去干嘛呢获取自媒体文章信息
[02:49] 好咱们就看个图一步步去实现好吧来获取自媒体文章信息那怎么做呢这时候呢咱们应该先去注入一个MAP这个MAP呢WM News MAP这件事有的好吧注入进来之后啊咱们就可以干嘛呢就可以在这里填什么slack没有吗slack的
[03:24] news detail by primary key就它它就要传一个news id其中它就能去返回什么呢返回一个wnews就是咱们要审核的一个文章这条文章下面呢是在这写一下注释就是什么呢根据文章id查询文章信息好下面要干嘛呢
[03:53] 下面咱们首先第一步呢就是当前文章是否状态为己是吧这时候咱们可以在这去加东西啊在这去写首先可能在判断的是吧WM News他不等于浪啊等于浪的时候再往下去走啊然后是这时候咱们要去做第一步呢就是要去查看要判断吧判断状态是否为是吧状态
[04:24] 放开为4的时候怎么办直接保存数据对吧所以说咱们在这直接判断就可以了然后是WM News然后是叫什么Argetas Datas然后是等于等于几等于4如果它等于等于4的话就说明什么意思看下来回顾一下这是不是人工审核已经通过了人工审核通过之后呢那这时候咱们就干嘛呢
[04:53] 就可以让他直接去保存数据了直接保存数据啊这时候咱们可以去抽出来一个方法叫什么叫reviewreview success然后是叫什么来着啊c5好这里边才能参数呢其实就是有两个啊有两个一个呢是wm第二个呢咱们要去把这之前的news里边的什么content转进去content啊
[05:31] 因为这样后期为了方便去抽取所以说你可以直接去传这一个也可以传这一个也可以我把这个B2B news传过去就可以了具体该怎么去创建这些东西到底有什么业务逻辑一会再说好吧先放置先放置这个其实就是保存数据保存数据这个数据其实要很多张表今天咱们也说了应该是有几张表弄去保存的时候是不是有四张表
[06:01] 咱们也可以拷贝一下啊咱们要去保存这四张表的信息这信息呢咱们一会儿再保存好吧先把这个主业务逻辑呢咱们先捋通OK好那这是第一个状态啊第一个然后再往下啊再往下该去判断啥呢往上看啊这块是不是状态为8是吧并且呢是发布时间大于当前时间那这个怎么做呢来看啊如果说当前的状态
[06:38] 等于等于8并且干嘛并且 wm news.getpublishname但是这个东西啊咱们还是要去做一个判断吧好吧首先呢你要去判断他的这个时间的必须不等不能等于那不能等于那啊不等于那然后呢然后再去并且什么呢publishname然后是gettime然后对谁呀
[07:10] 大于当前的new一个date吧好吧new一个date而getTimeOK那这样的话我们就能去判断当前的时间是发布时间是大于了当前的时间这能看明白吧好了啊行那这个设完之后啊设完之后咱们就接着往下写逻辑那这个逻辑呢其实跟这个逻辑是不是一样的没问题吧跟这个逻辑是一样的啊好我们直接写上
[07:40] 在这里边还有一个东西还有东西怎么还要再去要再去设置一下哪一个呢这个你保存完之后你应该去最终你保存完之后这个东西咱们就结束了比如说就不有必要再去往下走了直接轮它就可以了最终咱们这是就往下走了那这一块这个第二个怎么在这去写一下这是什么意思是审核审核通过
[08:13] 后的再发布文章再发布判断什么呢发布时间好吧那这个啊这个咱们就说是完了再往下看啊还有啥呢状态唯一状态唯一的啊这时候咱们要真正去保存了啊真正去审核了啊状态唯一的来看一看嗯在这是吧来计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计算计
[08:49] 我们要真正的去审核文章审核文章审核文章审核文章里边内容其实有可能我们来去写下一个要干嘛呢要去审核文章的什么文章的标题与内容的匹配度匹配度吧然后第二个呢第二个要去审核什么整合整合文本内容是阿里吧把你接口啊
[09:26] OK然后下面呢这个什么呢整合文当中的头片信息也是阿里接口好吧行然后下面还有吗下面的话这样的话咱们中的就可以去算是这样这样是吧这三项过了之后呢他就能干嘛呢就能去算是发布了就能真正发布了行那这个流程咱们先说到这好吧咱们一会儿再往下写

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中为一个媒体文章审核服务编写 Java 代码，包括定义接口、实现类、使用 MyBatis Mapper 和条件判断逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示一个流程图，包含“标题与内容是否匹配”、“审核文本”、“审核图片”、“发布时间是否大于当前时间”等判断节点，以及“人工审核拒绝”和“通过”等分支。
画面 2: 展示 IntelliJ IDEA 项目结构，选中了 `heima-leadnews-media` 模块。
画面 3: 展示 `ReviewMediaArticleService` 接口定义，包含 `autoReviewArticleByMedia(Integer newsId)` 方法。
画面 4: 展示 `ReviewMediaArticleServiceImpl` 类的开始部分，包含 `@Service` 注解和 `@Autowired` 注解。
画面 5: 展示 `ReviewMediaArticleServiceImpl` 类中定义 `private WalleMapper walleMapper;` 字段。
画面 6: 展示 `ReviewMediaArticleServiceImpl` 类中 `public void autoReviewArticleByMedia(Integer newsId)` 方法的开始部分。
画面 7: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle != null) { ... }` 条件判断语句。
画面 8: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle != null) { ... }` 条件判断语句，其中包含 `if (walle.getStatus() == 1) { reviewSuccessSaveAll(walle); }`。
画面 9: 展示 `ReviewMediaArticleServiceImpl` 类中 `private void reviewSuccessSaveAll(Walle walle) { ... }` 方法的开始部分。
画面 10: 展示 `ReviewMediaArticleServiceImpl` 类中 `private void reviewSuccessSaveAll(Walle walle) { ... }` 方法的注释部分。
画面 11: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle.getStatus() == 8 && walle.getPublishtime() != null && walle.getPublishtime().getTime() > new Date().getTime()) { ... }` 条件判断语句。
画面 12: 展示 `ReviewMediaArticleServiceImpl` 类中 `reviewSuccessSaveAll(Walle walle)` 方法的调用。
画面 13: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle.getStatus() == 8) { ... }` 条件判断语句。
画面 14: 展示 `ReviewMediaArticleServiceImpl` 类中 `if (walle.getStatus() == 8) { ... }` 条件判断语句，其中包含 `//审核文章的标题与内容的匹配度` 和 `//审核文章内容的图片信息，然后接口` 注释。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
package com.heima.admin.Service;
public interface ReviewMediaArticleService {
    public void autoReviewArticleByMedia(Integer newsId);
}
```

画面 4:
```java
@Service
public class ReviewMediaArticleServiceImpl implements ReviewMediaArticleService {
```

画面 5:
```java
private WalleMapper walleMapper;
```

画面 6:
```java
public void autoReviewArticleByMedia(Integer newsId) {
```

画面 7:
```java
if (walle != null) {
```

画面 8:
```java
if (walle.getStatus() == 1) {
    reviewSuccessSaveAll(walle);
}
```

画面 9:
```java
private void reviewSuccessSaveAll(Walle walle) {
```

画面 11:
```java
if (walle.getStatus() == 8 && walle.getPublishtime() != null && walle.getPublishtime().getTime() > new Date().getTime()) {
```

画面 12:
```java
reviewSuccessSaveAll(Walle walle);
```

画面 13:
```java
if (walle.getStatus() == 8) {
```

画面 14:
```java
if (walle.getStatus() == 8) {
    //审核文章的标题与内容的匹配度
    //审核文章内容的图片信息，然后接口
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 流程图结构：
- 起始节点 → “标题与内容是否匹配” → “是” → “审核文本” → “通过” → “审核图片” → “通过” → “发布时间是否大于当前时间” → “是” → 结束节点。
- “标题与内容是否匹配” → “否” → “人工审核拒绝” → 结束节点。
- “审核文本” → “不通过” → 结束节点。
- “审核图片” → “不通过” → 结束节点。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

