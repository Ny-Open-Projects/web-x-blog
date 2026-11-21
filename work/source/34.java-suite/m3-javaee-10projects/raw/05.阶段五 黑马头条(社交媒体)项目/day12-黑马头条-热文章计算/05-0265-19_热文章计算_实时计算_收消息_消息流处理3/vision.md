# 画面线理解：19_热文章计算_实时计算_收消息_消息流处理3

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\19_热文章计算_实时计算_收消息_消息流处理3【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:34, 01:07, 02:03, 02:34, 02:52, 03:12, 03:43, 04:28, 04:57, 05:21, 05:37, 05:48, 06:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:44:14

1) 这一组画面整体在讲如何在 Java 中使用正则表达式和 Pattern 类解析 Kafka 消息中的文章访问数据，并将其转换为结构化的 ArticleVisitStreamDto 对象，最终通过 ObjectMapper 序列化为 JSON。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 ArticleIncHandleListener.java 文件中 format001 方法的定义，该方法用于处理文章访问数据。
画面2: 展示了 ArticleIncHandleListener.java 文件中 @Component 注解和 onMessage 方法的定义，用于监听 Kafka 消息。
画面3: 展示了 format001 方法中创建 ArticleVisitStreamMessage 和 ArticleVisitStreamDto 对象，并定义正则表达式。
画面4: 展示了正则表达式 String regex = "COLLECTION:((\\d+),COMMENT:((\\d+),LIKES:((\\d+),VIEWS:((\\d+)"; 的完整定义。
画面5: 展示了 Pattern 类的 matcher 方法用于匹配字符串。
画面6: 展示了 if (mat.find()) {} 语句块，用于处理匹配成功的情况。
画面7: 展示了 else 语句块，用于处理匹配失败的情况。
画面8: 展示了 Long 类型的 valueOf 方法，用于将字符串转换为 Long 类型。
画面9: 展示了 ArticleVisitStreamDto 类的 setArticleId 方法，用于设置文章 ID。
画面10: 展示了 ObjectWriter 类的 writeValueAsString 方法，用于将对象序列化为 JSON 字符串。
画面11: 展示了 try-catch 块，用于处理序列化过程中的异常。
画面12: 展示了 KStream 的 map 和 aggregate 方法，用于处理流数据。
画面13: 展示了 format 方法的返回值，用于返回格式化的字符串。
画面14: 展示了 ArticleIncHandleListener.java 文件中 onMessage 方法的定义，用于处理 Kafka 消息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3:
```java
private String format001(String articleId, String value) {
    String ret = "";
    ArticleVisitStreamMessage temp = new ArticleVisitStreamMessage();
    ArticleVisitStreamDto dto = new ArticleVisitStreamDto();
    String regex = "COLLECTION:((\\d+),COMMENT:((\\d+),LIKES:((\\d+),VIEWS:((\\d+)";
    Pattern pat = Pattern.compile(regex);
    Matcher mat = pat.matcher(value);
    if (mat.find()) {
        dto.setCollect(Long.valueOf(mat.group(1)));
        dto.setComment(Long.valueOf(mat.group(2)));
        dto.setLike(Long.valueOf(mat.group(3)));
        dto.setView(Long.valueOf(mat.group(4)));
    } else {
        dto.setCollect(0);
        dto.setComment(0);
        dto.setLike(0);
        dto.setView(0);
    }
    dto.setArticleId(Integer.valueOf(articleId));
    temp.setData(dto);
    try {
        ret = mapper.writeValueAsString(temp);
    } catch (JsonProcessingException e) {
        e.printStackTrace();
    }
    return ret;
}
```

画面4:
```java
String regex = "COLLECTION:((\\d+),COMMENT:((\\d+),LIKES:((\\d+),VIEWS:((\\d+)";
```

画面5:
```java
Pattern pat = Pattern.compile(regex);
Matcher mat = pat.matcher(value);
```

画面6:
```java
if (mat.find()) {
```

画面7:
```java
} else {
    dto.setCollect(0);
    dto.setComment(0);
    dto.setLike(0);
    dto.setView(0);
}
```

画面8:
```java
dto.setCollect(Long.valueOf(mat.group(1)));
dto.setComment(Long.valueOf(mat.group(2)));
dto.setLike(Long.valueOf(mat.group(3)));
dto.setView(Long.valueOf(mat.group(4)));
```

画面9:
```java
dto.setArticleId(Integer.valueOf(articleId));
```

画面10:
```java
ret = mapper.writeValueAsString(temp);
```

画面11:
```java
try {
    ret = mapper.writeValueAsString(temp);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

画面12:
```java
return stream.map((key, val) -> {
    UpdateArticleMessage value = format(val);
    System.out.println(value);
    return new KeyValue<>(key, value);
}).groupByKey().windowedBy(TimeWindows.of(10000)).aggregate(new Initializer<String>() {
    @Override
    public String apply() {
        return "COLLECTION:0,COMMENT:0,LIKES:0,VIEWS:0";
    }
});
```

画面13:
```java
private UpdateArticleMessage format(String val) {
    UpdateArticleMessage msg = null;
    try {
        msg = mapper.readValue(val, UpdateArticleMessage.class);
    } catch (IOException e) {
        e.printStackTrace();
    }
    return msg;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
