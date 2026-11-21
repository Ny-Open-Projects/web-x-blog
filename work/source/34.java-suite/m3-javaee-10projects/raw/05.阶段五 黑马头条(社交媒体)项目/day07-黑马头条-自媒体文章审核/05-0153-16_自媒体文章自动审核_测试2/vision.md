# 画面线理解：16_自媒体文章自动审核_测试2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\16_自媒体文章自动审核_测试2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:42, 01:00, 01:49, 02:32, 02:51, 03:10, 03:55, 04:37, 05:23, 05:41, 06:05, 06:31, 07:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:27:12

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
