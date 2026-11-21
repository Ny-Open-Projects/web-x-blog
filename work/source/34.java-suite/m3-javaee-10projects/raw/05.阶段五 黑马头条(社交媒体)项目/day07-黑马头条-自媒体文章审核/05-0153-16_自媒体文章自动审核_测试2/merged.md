# 16_自媒体文章自动审核_测试2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\16_自媒体文章自动审核_测试2【海量资源尽在 666java.com】.mp4
- 时长 7分18秒（音频 438s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就继续往下测啊刚才呢咱们是测了一条数据啊没问题我又把这数据给修复了一下啊这数据呢目前呢是一啊还是一这状这个时间呢我在这发布时间呢给他加了一个那这时候呢咱们再分别去测一下其他的这种情况好吧这里边当然刚才有个问题啊这个问题咱们还要再去修复一下就是当前去审核图片的时候啊有可能会出问题哎有可能会出问题你的图片有可能他没找着是吧所以说咱们在这啊
[00:30] 咱们在这去判断一下判断什么东西首先是imageR equals不等于none然后这时候咱们再去干嘛再去放进去再去判断其他的那种那就可以了你说它要是等于none的话那就是很往下走了是吧这时候咱们可以再往下去写else等于none的话咱们也
[01:03] 直接垒蹭直接垒蹭就可以了这个垒蹭的方式呢就是还是这种方式问你干嘛呢这个审核失败图片内容有问题图片审核出现问题其实一句话其实就可以了行那这个咱们就先写到这儿一会儿咱们可以再去测一测然后的话咱们再往下看再往下看然后下面咱们就来去测首先咱们测一个4如果说状态为4的话呢咱们会直接保存
[01:37] 状态位四的时候呢其实亮啊状态位四的时候是它是人工审核已经通过了那通过之后呢那这时候咱们就不需要再去审核一遍了直接去保存数据就完事了好吧那这个八呢刚才也说了啊这个八的话就是当前是待发布的状态如果说这个时间这个时间好像写了些问题是吧说是发布时间大于当前时间应该是写反了如果当前时间是大于发布时间
[02:05] 50发布时间的话咱们就直接放在审核了直接在干嘛呢直接去保存数据就可以了然后下面有一个啊下面这个这个数据这个发布时间如果说大于当前时间的话咱们可以把暂时把它状态改为8先不保存数据明白了意思吧行那咱们下面就来去把这几个把这几种情况给测一下啊首先呢咱们在这儿啊把它改成状态改成4好吧改成4啊保存保存完之后呢咱们在这儿直接打赞点就可以了
[02:35] 打个断点然后是debug走着好到这之后呢来看一下啊到这之后呢他应该是能够走到这一步啊走这一步应该是没有问题的啊好稍等啊正在加载环境好他到这了是吧到这之后呢可以往下走你看他这个提议院士会去保存咱们直接放行就可以了好吧这东西咱们就不测了因为这东西咱们刚才已经测完了好那放行完之后啊你可以看一下这个数据
[03:13] 这数据目前是不是改成9了因为他保存数据之后他就审核成功了是吧所以说咱们在这啊再来改一下改成8好吧4已经错过了改成8改成8的情况是这样啊改成8的情况目前我这个数据呢是9月30号9月30号啊这个我这还没有到9月30号啊还没有到9月30号那这时候呢他应该是啥都不做那这时候咱们可以把这个时间改一改改成啥呢改成上个月好吧改成我说3号改成3号啊
[03:41] 改成9月3号那这个9月3号已经过去了已经过去了毕竟它是8它该走哪该走哪你看啊往上去找咱们的逻辑这是不是这你看它等于8吗等于8它不等于那刚才这个时间咱们说了如果说当前时间是大于这个发布时间的它也会去直接保存咱们在这打断点啊直接再去运行一下稍等啊看一看看一看这个效果
[04:25] 刚才咱们在这写错了这是之前是大宇号现在是小宇号啊好往下走你看是不是能进来啊没问题啊那这时候呢它也能保存咱们也可以直接运行完然后呢咱们可以刷一下当前的数据你看它现在是不是又成9了没问题吧没问题啊行那咱们现在再去做一个测试啊它是1显示这个时间呢是大于当前时间的比如说是今天今天是29号是吧咱们各设置成30号好吧
[04:54] 那30号之后呢去保存一下那这时候他就不应该去保存数据他应该是把这状态改成几改成待发布的状态是吧审核审核完之后再发布啊应该是改成8是吧改成8啊好咱们来去走一遍运行运行完之后啊他就会去走到哪呢他就会往下走先去审核审核完之后啊这个未必能审核过去啊因为我这会儿刚才是加了个代码是吧
[05:26] 嗯对有可能他就审核不通过了啊咱们来看一下啊好咱们来看一下啊刷新一下这成2了是吧为什么成2呢因为刚才啊刚才我在这去加代码的时候啊在这如果说他等于难的话因为咱们这图片本身有问题大家也知道啊本身的是你要去等于难的时候咱们让他去修改成2说审核图片出现问题你看是不是整个图片出现问题了是吧
[05:55] 那这样咱们可以向他注钓目前的话咱们其实就不需要再去干嘛了呢再去审核图片了咱们这个已经测完了包括什么呢包括咱们这个这方面的内容这方面的内容咱们也不审了好吧目前那个文本内容咱们也不审了那这个咱们就只审当前的这个标题的匹配度好吧行其他暂时不审
[06:19] 那咱们下面呢就可以去再去测试一下他应该是能正常走到这把数据改成8改成8啊目前把状态改成几啊改成1是吧改成1啊好那咱们就直接运行看一下效果走看看能不能到这儿啊稍等应该是可以到这儿看到了吧然后往下走他这个时间当年这个发布时间大于当前时间吗肯定是大于的这时候他就把状态改成8了啊直接放行就可以了啊好改成8之后呢可以看一下啊
[07:06] 刷下这个状态是不是吧是不是再发布的状态啊好没问题啊那这个咱们所有的情况基本上都测试完了行那这个咱们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个新闻文章审核服务的 Java 代码实现，包括文本和图片内容的审核逻辑、状态更新以及数据库操作，并通过单元测试验证功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 ReviewMediaArticleServiceImpl.java 中审核文章状态为 -4 时直接保存的逻辑。
画面 2: 展示审核文章时，根据阿里云文本审核 API 返回的 response 值判断是否需要人工审核或审核失败。
画面 3: 展示审核文章时，根据阿里云图片审核 API 返回的 response 值判断是否需要人工审核或审核失败。
画面 4: 展示审核文章时，根据文章标题和内容的相似度判断是否“文章标题与内容不匹配”。
画面 5: 展示审核文章时，将文本内容和图片信息拼接成 JSON 字符串，调用阿里云文本审核 API。
画面 6: 展示 ReviewMediaArticleTestReview 类中，调用 autoReviewArticleByMedia 方法并打印日志。
画面 7: 展示 ReviewMediaArticleServiceImpl.java 中，将文章内容和图片内容插入数据库。
画面 8: 展示审核文章时，根据阿里云文本审核 API 返回的 response 值判断是否“需要人工审核”或“文本内容审核失败”。
画面 9: 展示 Navicat for MySQL 中，查询 wm_news 表，显示文章状态为 8（审核中）。
画面 10: 展示 ReviewMediaArticleServiceImpl.java 中，根据文章的发布时间判断是否“符合发布”或“立即发布”。
画面 11: 展示 ReviewMediaArticleServiceImpl.java 中，审核失败后更新文章状态为 2。
画面 12: 展示 ReviewMediaArticleServiceImpl.java 中，审核通过后更新文章状态为 6。
画面 13: 展示 ReviewMediaArticleServiceImpl.java 中，根据文章的发布时间判断是否“符合发布”或“立即发布”。
画面 14: 展示 Navicat for MySQL 中，查询 wm_news 表，显示文章状态为 1（已发布）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
//状态为-4的时候，直接保存数据
if(wlves.getStatus()==-4){
    reviewSuccessSaveAll(wlves);
    return;
}
//审核通过后待发布文章，判断发布时间
if(wlves.getStatus()==8 && wlves.getPublishTime()!=null && wlves.getPublishTime().getTime() - new Date().getTime() > 0){
    return;
}
//审核文章
if(wlves.getStatus()==1){
    //审核文章的标题与内容的匹配度
    String content = wlves.getContent();
    String title = wlves.getTitle();
    double degree = Compute.SimilarDegree(content, title);
    if(degree<0){
        //文章标题与内容匹配
        updateNews(wlves, (short)2, message: "文章标题与内容不匹配");
        return;
    }
}
```

画面 2:
```java
try {
    String response = aliyunTextScanRequest.testScanRequest(sb.toString());
    if("review".equals(response)) {//人工审核
        updateNews(wlves, (short)3, message: "需要人工审核");
        return;
    }
    if("block".equals(response)) {//审核失败
        updateNews(wlves, (short)2, message: "文本内容审核失败");
        return;
    }
}
```

画面 3:
```java
//审核文章中的图片信息。阿里云接口
if(imagesResponse == null) {
    if("review".equals(imagesResponse)) {//人工审核
        updateNews(wlves, (short)3, message: "需要人工审核");
        return;
    }
    if("block".equals(imagesResponse)) {//审核失败
        updateNews(wlves, (short)2, message: "图片内容审核失败");
        return;
    }
}
```

画面 4:
```java
//审核文章
if(wlves.getStatus()==1){
    //审核文章的标题与内容的匹配度
    String content = wlves.getContent();
    String title = wlves.getTitle();
    double degree = Compute.SimilarDegree(content, title);
    if(degree<0){
        //文章标题与内容匹配
        updateNews(wlves, (short)2, message: "文章标题与内容不匹配");
        return;
    }
}
```

画面 5:
```java
//审核文本内容。阿里云接口
List<String> images = new ArrayList<>();
StringBuilder sb = new StringBuilder();
JSONArray jsonarray = JSON.parseArray(content);
handlerTextAndImages(images, sb, jsonarray);
```

画面 6:
```java
@Override
public void autoReviewArticleByMedia(Integer newsId) {
    //文章状态为1时，进行文章审核
    if(wlves == null) {
        //状态为-4的时候，直接保存数据
        if(wlves.getStatus() == -4) {
            reviewSuccessSaveAll(wlves);
            return;
        }
    }
}
```

画面 7:
```java
apArticleMapper.insert(aparticle);
//ap_article_content
apArticleContent aparticleContent = new ApArticleContent();
aparticleContent.setArticleId(aparticle.getId());
aparticleContent.setContant(sb.toString());
aparticleContentMapper.insert(aparticleContent);
```

画面 8:
```java
try {
    String response = aliyunTextScanRequest.testScanRequest(sb.toString());
    if("review".equals(response)) {//人工审核
        updateNews(wlves, (short)3, message: "需要人工审核");
        return;
    }
    if("block".equals(response)) {//审核失败
        updateNews(wlves, (short)2, message: "文本内容审核失败");
        return;
    }
}
```

画面 9:
```sql
UPDATE `wm_news` SET `publish_time` = '2019-09-03 10:10:15' WHERE (`id` = '6110') AND (`enable` = '1')
```

画面 10:
```java
if(wlves.getPublishTime() != null) {
    if(wlves.getPublishTime().getTime() - new Date().getTime() > 0) {
        //修改文章的状态为8
        updateNews(wlves, (short)6, message: "符合发布");
    } else {
        //立即发布
        reviewSuccessSaveAll(wlves);
    }
} else {
    //立即发布
    reviewSuccessSaveAll(wlves);
}
```

画面 11:
```java
updateNews(wlves, (short)2, message: "图片内容审核失败");
return;
```

画面 12:
```java
updateNews(wlves, (short)6, message: "符合发布");
```

画面 13:
```java
if(wlves.getPublishTime() != null) {
    if(wlves.getPublishTime().getTime() - new Date().getTime() > 0) {
        //修改文章的状态为8
        updateNews(wlves, (short)6, message: "符合发布");
    } else {
        //立即发布
        reviewSuccessSaveAll(wlves);
    }
} else {
    //立即发布
    reviewSuccessSaveAll(wlves);
}
```

画面 14:
```sql
UPDATE `wm_news` SET `status` = '1' WHERE (`id` = '6110') AND (`enable` = '1')
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

