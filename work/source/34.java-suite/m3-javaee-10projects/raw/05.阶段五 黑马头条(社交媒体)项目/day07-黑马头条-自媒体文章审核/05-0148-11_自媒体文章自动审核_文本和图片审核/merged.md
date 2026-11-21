# 11_自媒体文章自动审核_文本和图片审核

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\11_自媒体文章自动审核_文本和图片审核【海量资源尽在 666java.com】.mp4
- 时长 10分10秒（音频 610s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续往下讲刚才咱们是把这个标题给说了一下然后下面咱们就来去干嘛呢就来去说审核当前的文本和审核文章中的图片信息这个都需要调用阿里的接口那这时候咱们首先你要知道都是审核文本那这个文本是谁呢其实就是当前那个content
[00:26] 那content实际上咱们可以去打开当前表中看这个content是个什么样的结构那这个其实咱们在之前保存的时候已经说过一次可以打开咱们去找一条数据找一条数据比较少的比如说最后一条这是咱们自己添加的这个内容可能就比较少拷贝一下然后你在这去加一个json.json把它给拷过来拷过来之后其实最终咱们要去获取两部分内容
[00:54] 第一个就是它是text这个咱们是要审核的文本这是要审核的文本然后第二个咱们要去审核图片所以说咱们还要从当前的这个里边去获取到什么去获取到图片是吧并且是装到一个list集合中因为阿里接口里边咱们要传达参数就是一个list集合所以说咱们现在要去把当前这个内容给解析一下取出了两部分内容第一个是文本第二个是图片
[01:24] 好吧行啊那咱们来一块来看一下啊那这该怎么做呢这怎么做呢我先要获取内容啊我们在这先去创建一个比如说先去创建一个集合吧集合呢是一个shrimp然后呢要以密质思维等于什么呢写错了是吧没写错是吧好等于new一个relist这是图片用的然后咱们再去创建一个stream builder
[01:58] 是
[02:30] 我们可以去转成一个集合是吧把这个content放进去因为它就是一个集合是不是一个通号啊好没问题啊然后就往下写啊最终呢它就会返回这个东西但是呢咱们往这里边去装值啊那怎么装啊所以说咱们在这就不在这写了好吧
[02:56] 这个数据咱们只是准备一下这时候呢咱们可以用当前的一个什么呢当前的一个抽取一个类好吧叫handler.txt.and.images然后呢咱们就可以把当前的什么images装进去第二个呢是sb装进去第三个呢是当前的json.arif装进去好吧有类有方法没有怎么就换件出来好那这个方法呢就是干嘛用呢
[03:28] 找出文本是吧文本内容和图片列表是吧行那咱们就写一下首先这个东西你可以直接去写完了是吧点点好这是叫OBG好吧然后下面咱们就可以去拿值了首先你可以把它OBG转成什么转成一个jsonobject比如说怎么叫jsonobject什么叫
[04:01] JSON的OBGOW放于它这时候强转一下强转强转完之后咱们现在就可以去拿值了首先是JSON OBGOW-GET代表一个说TYPE然后这个就是一个TYPE它其实是一个Street是一个Street可以直接强转成StreetStreet 错了是吧 不好意思 没事
[04:34] 好下面咱们就可以判断了如果说当前的imageim咱们可以拷贝一下image.ecos type这时候咱们就可以去通数据了这时候咱们就可以拿到当前的什么jsonobgo.getvalue最终的这个其实就是你要拿到的value这也是一个stripe
[05:10] 这个其实就可以去装谁呀放到以密子思爱的然后就可以把当年那个y6装进去就完事了好吧这样的话其实它就是一个图片信息好那这是一个下面咱们还要再去拿第二个if什么呢是tax吗你可以看一下是吧好如果说是tax
[05:45] 那这时候咱们是不是可以拿文本了然后咱们可以去当前的jsonjson-gobigrow.get当前的value然后就是谁呀还是value这个就是文本内容那这时候呢s都是当前的内容dmitris呢就是当前的什么
[06:15] 当前的图片列表信息好了这时候咱们该拿到的都拿到了这时候咱们可以去调接口调接口的话咱们就比较简单了往上往上在哪呢在这是吧在这是吧这时候咱们就可以去调接口了好首先你要调接口之前还得去把当前的这两个工具类两个类注入进来private然后是阿里云是吧一个是text好
[06:47] 然后呢下面还有一个是吧把这个注进来啊private阿里云叫什么image scan request好这加进来之后呢咱们再注入啊这时候咱们就可以去审核了啊首先去审核的第一个是哪个先的文本是吧好往下走这个在这儿去审核文本啊好打什么呢打当前的text scan request是吧我们可以把当前的sb.toast
[07:20] 那的话呢咱们就拿到了一个response.response这是response这个需要去抛一场咱们就抛出去吧好吧抛出去啊嗯看抛出去了没这个不行是吧那这样咱们就try一下吧好吧好那这个加上之后啊那咱们下面就可以去判断了啊看看它是什么值我们可以判断咱们之前应该讲过吧
[07:59] 如果说当前的什么字母牌reviewreviewrequels response如果说它是review的话就是人工是吧这是人工需要人工审核人工审核好然后下面咱们就可以去修改当前的什么update什么是吧一个值是wm第二个是咱们的人工是哪个人工是3是short
[08:29] 然后呢咱们可以提示一句话人工审核需要人工审核好下面还有一个比如说if这样啊咱们这个人工审核之后啊咱们这点就结束了就不需要再往下走了直接准就可以好吧然后再往下咱们再去判断一个如果他block呢i o c k好吧这时候呢是审核失败审核
[09:00] 失败就是整合失败是几啊这时候就是是文本内容审核是OK那这个咱们直接旅行可以好那这个啊那这个文本的审核咱们就做完了啊下面还有一个是吧我们要去审核内容审核图片啊图片的话其实更容易一些像阿里密室什么点
[09:28] 当前的要传一个以秘之思这个里面是不是已经放完了咱们的什么东西啊完了咱们的图片是吧叫以秘之request response吧好吧行下面咱们也可以判断其实跟他是一样吗一样的好好背这个又不是response了这是啊是当前的以秘之response好吧行这个啊你们在这可以稍微改一改啊这是图片内容适合之外好吧
[10:00] 好那到目前的话呢咱们这个目前的理的接口啊就是说内容的审核和图片的审核咱们就做完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 服务中集成阿里云的文本和图片审核功能，实现对文章内容的自动审核并根据审核结果更新文章状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 ReviewMediaArticleServiceImpl 类中审核文章逻辑的代码，当相似度为0时，更新文章状态为“待发布”。
画面2：在代码中使用了 String 类型的变量，IDE 提示需要导入 java.lang.String。
画面3：在代码中使用了 StringBuilder 类型的变量，IDE 提示需要导入 java.lang.StringBuilder。
画面4：在代码中使用了 JSON.parse 方法，IDE 提示需要导入 com.alibaba.fastjson.JSONObject。
画面5：在代码中使用了 Integer 类型的变量，IDE 提示需要导入 java.lang.Integer。
画面6：展示 handlerTextAndImages 方法的定义，用于处理文章中的文本和图片。
画面7：在 handlerTextAndImages 方法中，使用 JSON 对象遍历 JSON 数组。
画面8：在 handlerTextAndImages 方法中，判断 JSON 对象的 type 是否为 "image"。
画面9：在 handlerTextAndImages 方法中，判断 JSON 对象的 type 是否为 "text"。
画面10：展示 ReviewMediaArticleServiceImpl 类中定义了两个 @Autowired 注入的阿里云审核请求对象。
画面11：展示 ReviewMediaArticleServiceImpl 类中定义了审核文章的方法，根据文章状态和发布时间判断是否需要审核。
画面12：在审核文章方法中，调用阿里云文本审核接口，传入文章内容。
画面13：在审核文章方法中，根据阿里云文本审核的返回结果，更新文章状态为“需要人工审核”。
画面14：在审核文章方法中，根据阿里云图片审核的返回结果，更新文章状态为“图片内容审核失败”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
if (degree == 0) {
    updateNews(wNews, (short) 2, message: "文章标题与内容不匹配");
    return;
}
```

画面2：
```java
String title = wNews.getTitle();
```

画面3：
```java
StringBuilder sb = new StringBuilder();
```

画面4：
```java
JSONArray jsonArray = JSON.parseArray(content);
```

画面5：
```java
int degree = wNews.getSimilarDegree(content, title);
```

画面6：
```java
private void handlerTextAndImages(List<String> images, StringBuilder sb, JSONArray jsonArray) {
    for (Object obj : jsonArray) {
        JSONObject jsonObj = (JSONObject) obj;
    }
}
```

画面7：
```java
String type = (String) jsonObj.get("type");
```

画面8：
```java
if ("image".equals(type)) {
    String value = (String) jsonObj.get("value");
}
```

画面9：
```java
if ("text".equals(type)) {
    String value = (String) jsonObj.get("value");
}
```

画面10：
```java
@Autowired
private AliyunTextScanRequest aliyunTextScanRequest;

@Autowired
private AliyunImageScanRequest aliyunImageScanRequest
```

画面11：
```java
public void auditReviewArticleByIdMedia(int newsId) {
    News wNews = wNewsMapper.selectNewsById(newsId);
    if (wNews == null) {
        return;
    }
    if (wNews.getStatus() == -8 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() > new Date().getTime()) {
        reviewSuccessSaveAll(wNews);
        return;
    }
}
```

画面12：
```java
String response = aliyunTextScanRequest.textScanRequest(sb.toString());
```

画面13：
```java
if ("review".equals(response)) { //人工审核
    updateNews(wNews, (short) 5, message: "需要人工审核");
    return;
}
```

画面14：
```java
if ("block".equals(imagesResponse)) { //图片审核失败
    updateNews(wNews, (short) 2, message: "图片内容审核失败");
    return;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

