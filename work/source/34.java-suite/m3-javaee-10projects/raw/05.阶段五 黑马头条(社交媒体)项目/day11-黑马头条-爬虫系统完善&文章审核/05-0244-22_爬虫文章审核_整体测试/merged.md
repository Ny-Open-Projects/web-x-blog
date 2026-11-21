# 22_爬虫文章审核_整体测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day11-黑马头条-爬虫系统完善&文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day11-黑马头条-爬虫系统完善&文章审核\22_爬虫文章审核_整体测试【海量资源尽在 666java.com】.mp4
- 时长 8分57秒（音频 537s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去测试一下啊那测试之前呢首先呢呃你得去把这个环境给准备一下首先你要是把当前那个mycat给启动然后同时呢咱们要创建索引所以说你要把这个ES啊也给启动一下啊好那这两个启动完之后呢咱们现在啊先去用单元测试去测一下呃在这啊在咱们之前呢应该是测过自媒体的咱们还是用当前这个测试这个单元测试就可以了啊
[00:30] 然后呢你在这啊再去创建一个方法然后是wide然后是test reviewcrawler crawler然后我们加一个test这时候呢你需要去注入谁啊注入当前爬虫那个自动审核private然后是reviewcrawler article Service就它
[01:05] 收进来之后呢咱们再去调用一下里边的方法这个方法呢有很多我们就用第一个就是根据当前低去审核就可以了这个呢咱们需要先去抛个一长抛出去吧下面呢咱们就在这个库中去找一条数据一批article CL News很显然是找到哪啊CL News好 没问题吧好 找到CL News
[01:36] 怎么就找第一条吧好吧拷贝一下然后呢是到到这啊到这我们可以直接debug一下走动啊咱现在这啊先在这打个点看看能不能到这啊好来去执行debug稍等一下正在加载环境稍等这个环境应该还行啊还行这速度还行稍等一会吧好过来了是吧
[02:19] 过来之后咱们可以往下去执行一步步走看一看走走先去查一次是吧他因为他的一个状态咱们统一都查为这个状态为一的好往下走看看这个数据有没有这个数据是不是有啊有问题吧好接着往下走他到这了到这之后咱们再进入到这个方法里边在这再打个断点这是要真正审核的爱来了后来往下看把这稍微拉一下好
[02:48] 咱们接着往下走现在开始执行开始这个流程开始然后它不为空首先是拿到它的内容拿到它的什么标题好第一步呢它两个不同时都不能为空是吧它两个本身就不为空是吧然后这时候呢你要去拿到什么呢拿到它的一个这种匹配度是吧好匹配度它这个是有纸的是吧所以说咱们它这个文章和标题也算是匹配的啊好再往下走
[03:16] 然后是开始文本内容的审核往下走走走这时候呢从当前的content中去取出来images和当前的内容好往下走你可以看一下当前images是0这个sb呢这也是0是吧没有值这个显然是有值的对吧有值的那有可能咱们这个写错了来看一下啊复活循环json array然后他然后是
[03:49] 这写错了是吧这不是EP这是DE那这个我们就把这个停了之后呢咱们再重新去走一遍那这样你可以干嘛呢你可以从当前的这直接在这打断点就可以了稍等直接在这断点稍等一下把这个断点也给去掉这样的话就比较快一些好到这之后呢咱们再往下走来往下看
[04:28] 你看当前的隐秘之思里边是不是有六张图片没问题吧然后这个然后这个sb呢这里边是不是也有数据啊是566个好没问题啊然后拿到这个文本和内容之后啊咱们下面第一步要干嘛呢第一步要去调用阿里的接口去审核文本往下走稍等他正在调用啊那你看当前这个返回值是不是pass那就审核通过了呗往下走
[04:56] 好这时候开始审核图片内容再往下走这时候是六张图片他都会去审核啊这时候也是pass看到了吗没问题啊好再往下再往下啊然后下面就该去保存数据了啊保存先去保存的当前的是一个这种作者是吧没问题文章也没问题然后标签往下走也没有事是吧文章的配置呢好也过了然后看一下这个文章内容呢
[05:26] 内容好像出问题了是吧哎内容好像出问题了那这个内容啊咱们好像是写的有问题啊咱们先停了啊您去看一看啊感觉写的没事是吧那这样咱们可以看一下当前的文章的内容这个啊其实咱们最终最终去保存的时候呢要去做一个压缩做一个压缩那这时候咱们并没有压缩是吧咱们可以看咱们可以这样啊可以参考一下之前写的代码之前在哪写过呀
[05:59] 还拉不过来了是吧之前是不是咱们在这个当前的这种media中去设置过呀你看这块是不是加了个压缩呀所以说呢咱们在这啊应该去压缩一下这样的话才能正常保存好好呗背完之后呢这个内容呢就是当前的哪个content好那这个啊这个的话就是咱们那个也改了啊改完之后啊咱们再来重新debug一下咱们也可以直接打算点到哪啊
[06:29] 直接打断点到这个保存content这一块啊好把这个断点给去掉然后再去debug走一遍debug走嗯稍等那这样这样的话我这块你看我这块数据没有保存啊这个数据好像是保存了是吧保存链啊我先把这个数据给删了啊看看能不能重新保存一下啊好稍等啊到这了啊到这之后呢你可以直接去往下走一步你看是不是这时候就走过来了
[07:07] 好那这个内容保存完之后呢下面是该去创建索引再往下走这个索引创建也是没问题的啊前提你必须得干嘛必须得是开启当前这个ES这个环境啊好那这个创建完之后啊下面咱们的流程基本上就走完了最终呢它会把这个状态改为9改为9啊往下走好咱们直接放行就可以了啊好那这个中间是没有出错的啊咱们可以看一下
[07:35] 当前这个AP article中是不是保存了一条数据你看这个当然你也可以看一下时间啊看时间是10月28号啊没问题就是当前这个cstn没问题啊当然你也可以看这啊你看这个是什么公告第27啥的是吧这个标题是能够对应上的啊当然这里边还有一个东西就是你看一下当前那个cellnews里边的状态到底改没改啊这状态应该是改了几啊改成9这还没改是吧刷新一下啊
[08:05] 应该是这个咱们可以看一下当前这个IT值叫3518135181这状态怎么老变呢我看看它状态应该是给改了的是哪一个我看看35181咱们试试35181看看是不是35181没问题当前这个35181这条数据它这个状态已经改成了9
[08:41] 好那这样的话咱们整个流程啊就算是走完了啊那这个呢我只是去测了一下他成功的啊比如说这个所有的都已经成功了如果说要是审核失败的话他应该会把状态改为二啊这个呢你可以去测一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个文章自动审核服务的测试与实现过程，包括从测试用例触发、内容相似度比对、图片审核到最终数据持久化入库的完整流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示测试类 ReviewArticleTest 中的 testReviewCrawler 方法调用，以及服务类 ReviewCrawlerArticleServiceImpl 中的 autoReviewArticleByCrawler 方法。日志显示数据库连接池初始化和连接创建。
画面2：在 ReviewArticleTest.java 中，光标位于 testReviewCrawler 方法的定义处，准备执行测试。
画面3：执行 testReviewCrawler 方法，日志显示测试成功完成。
画面4：在调试模式下，查看 CNews 对象的属性，包括 id=35181，title="CSDN 公司公告"，content 为文章内容，status 为 0。
画面5：在 ReviewCrawlerArticleServiceImpl.java 中，查看 autoReviewArticleByCrawler 方法，其中包含内容相似度计算逻辑。
画面6：查看 handlerTextAndImages 方法，用于处理 JSON 数组中的文本和图片数据。
画面7：查看内容相似度计算逻辑，若相似度小于 0 则返回，否则继续执行文本审核。
画面8：查看图片审核逻辑，使用阿里云图片审核服务，若审核失败则更新状态并返回。
画面9：查看 saveArticleContent 方法，将文章内容保存到数据库。
画面10：查看 saveIndexEntity 方法，将文章索引信息保存到数据库。
画面11：在 Navicat for MySQL 中，查看 ap_article 表的数据，显示文章内容和元数据。
画面12：在 Navicat for MySQL 中，执行 DELETE 语句，删除 id 为 25103 的记录。
画面13：在 Navicat for MySQL 中，执行 SELECT 语句，查询 ap_article 表中的文章数据。
画面14：在 Navicat for MySQL 中，查看 ap_article 表中包含文章标题、内容、标签等字段的数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public void testReviewCrawler() throws Exception {
    reviewCrawlerArticleService.autoReviewArticleByCrawler(cNewsId: 35181);
}
```
画面2：
```java
public void testReviewCrawler() throws Exception {
```
画面3：
```java
public void testReviewCrawler() throws Exception {
    reviewCrawlerArticleService.autoReviewArticleByCrawler(cNewsId: 35181);
}
```
画面4：
```java
cNews = new CNews();
cNews.setId(35181);
cNews.setTitle("CSDN 公司公告");
cNews.setStatus((byte) 0);
cNews.setChannelId(2101);
cNews.setAuthorId(4100);
cNews.setOriginalTime(new Date());
cNews.setPublishTime(new Date());
cNews.setUpdateTime(new Date());
cNews.setLabels(new ArrayList<>());
cNews.setImages(new ArrayList<>());
cNews.setContent("H41AAAAAAAAAA..."); // 内容省略
```
画面5：
```java
long currentTimeMillis = System.currentTimeMillis();
if (null == cNews) {
    log.info("文章内容为空");
    return;
}
double degree = Compute.SimilarDegree(content, title);
if (degree < 0) {
    updateNews(cNews, messages: "文章和标题不匹配");
    return;
}
log.info("开始文本内容的审核");
```
画面6：
```java
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    for (Object obj : jsonArray) {
        JSONObject jsonObject = (JSONObject) obj;
        String type = (String) jsonObject.get("type");
        if ("image".equals(type)) {
            String value = (String) jsonObject.get("value");
            images.add(value);
        }
        if ("text".equals(type)) {
            String value = (String) jsonObject.get("value");
            sb.append(value);
        }
    }
}
```
画面7：
```java
double degree = Compute.SimilarDegree(content, title);
if (degree < 0) {
    updateNews(cNews, messages: "文章和标题不匹配");
    return;
}
log.info("开始文本内容的审核");
```
画面8：
```java
String imageResponse = aliYunImageScanRequest.imageScanRequest(images);
if (null == imageResponse || !imageResponse.equals("pass")) {
    updateNews(cNews, messages: "图片内容审核失败");
    return;
}
```
画面9：
```java
try {
    saveArticleContent(content, apArticle);
    createIndex(apArticle);
} catch (Exception e) {
    e.printStackTrace();
}
```
画面10：
```java
private IndexEntity savedIndexEntity(ApArticle apArticle, CNews cNews) {
    IndexEntity indexEntity = new IndexEntity();
    indexEntity.setId(new Long(apArticle.getId()));
    indexEntity.setContent(cNews.getContent());
    indexEntity.setStatus(new Long(value: 1));
    indexEntity.setTitle(cNews.getTitle());
    indexEntity.setPublishTime(new Date());
    if (apArticle.getChannelId() != null) {
        indexEntity.setChannelId(new Long(apArticle.getChannelId()));
    }
    return indexEntity;
}
```
画面11：
```sql
SELECT * FROM ap_article LIMIT 0, 1000;
```
画面12：
```sql
DELETE FROM ap_article WHERE id = 25103;
```
画面13：
```sql
SELECT * FROM ap_article LIMIT 0, 1000;
```
画面14：
```sql
SELECT * FROM ap_article LIMIT 0, 1000;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

