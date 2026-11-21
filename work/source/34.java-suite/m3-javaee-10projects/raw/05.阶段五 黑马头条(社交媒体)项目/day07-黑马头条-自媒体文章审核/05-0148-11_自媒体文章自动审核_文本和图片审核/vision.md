# 画面线理解：11_自媒体文章自动审核_文本和图片审核

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\11_自媒体文章自动审核_文本和图片审核【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:37, 02:01, 02:30, 03:15, 04:06, 04:48, 05:17, 05:47, 06:37, 07:03, 07:57, 08:50, 10:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:22:54

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
