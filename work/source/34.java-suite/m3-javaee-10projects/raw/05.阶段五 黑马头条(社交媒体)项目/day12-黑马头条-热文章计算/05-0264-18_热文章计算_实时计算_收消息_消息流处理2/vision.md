# 画面线理解：18_热文章计算_实时计算_收消息_消息流处理2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\18_热文章计算_实时计算_收消息_消息流处理2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:21, 02:38, 04:58, 06:53, 08:55, 09:42, 10:44, 11:23, 12:07, 13:34, 14:34, 15:25, 16:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:43:42

1) 这一组画面整体在讲什么（一句话）：
实现文章点赞行为的实时流处理，包括定义聚合器、解析消息、提取字段并生成 Key-Value 对。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 HotArticleStreamHandler.java 中，定义了 KStream 的 getStream 方法，用于处理文章点赞流，其中包含对消息的格式化和打印日志。
画面2：在 getStream 方法中，使用 .new 来创建一个新对象，IDE 提示了可能的构造函数。
画面3：在 PPT 中，展示了 3.2.6 综合测试部分，包含启动服务和添加单元测试的步骤，其中单元测试代码片段显示了如何模拟用户和点赞行为。
画面4：在 HotArticleStreamHandler.java 中，定义了聚合器的 apply 方法，用于处理聚合后的数据。
画面5：在 apply 方法中，使用 .replace 方法对字符串进行替换操作。
画面6：在 apply 方法中，使用 .split 方法对字符串进行分割。
画面7：在 apply 方法中，使用 for 循环遍历分割后的字符串数组。
画面8：在 apply 方法中，使用 switch 语句根据不同的字段类型进行处理。
画面9：在 apply 方法中，为每个 case 分配了对应的变量值。
画面10：在 apply 方法中，使用 switch 语句根据不同的字段类型进行处理。
画面11：在 apply 方法中，使用 String.format 方法格式化输出。
画面12：在 apply 方法中，使用 .map 方法对流进行转换。
画面13：在 apply 方法中，使用 .new KeyValue 方法创建新的 Key-Value 对。
画面14：在 apply 方法中，使用 .map 方法对流进行转换。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
public KStream<String, String> getStream(String key, String stream) {
    return stream.map((key, val) -> {
        UpdateArticleMessage value = format(val);
        System.out.println(value);
        //likes:1
        return new KeyValue<>(value.getData().toString(), value.getData().gettype().name()+"-"+value.getData().getadd());
    });
}
```

画面2：
```java
.new
```

画面3：
```java
@AutoWired
private AppliesBehaviorsService appliesBehaviorsService;

@Btest
public void testLikesSave() {
    Apuser user = new Apuser();
    user.setId(1L);
    AppBehaviorUtils.setUser(user);
    LikesBehaviorDto dto = new LikesBehaviorDto();
    dto.setArticleId(1001L);
}
```

画面4：
```java
public String apply() {
    return "COLLECTION:0,COMMENT:0,LIKES:0,VIEWS:0";
}
```

画面5：
```java
public String apply(Object aggKey, String value, String aggValue) {
    return null;
}
```

画面6：
```java
String[] aggArr = aggValue.split(regexp);
int tol = 0, com = 0, lik = 0, vie = 0;
for(int i = 0; i<aggArr.length; i++){
    String[] temp = aggArr[i].split(regexp);
    switch (UpdatedArticle.UpdateArticleType.valueOf(temp[0])){
```

画面7：
```java
case LIKES:
    lik = Integer.valueOf(temp[1]);
case VIEWS:
    vie = Integer.valueOf(temp[1]);
case COLLECTION:
    col = Integer.valueOf(temp[1]);
case COMMENT:
    com = Integer.valueOf(temp[1]);
```

画面8：
```java
switch (UpdatedArticle.UpdateArticleType.valueOf(temp[0])){
```

画面9：
```java
case LIKES:
    lik = Integer.valueOf(temp[1]);
case VIEWS:
    vie = Integer.valueOf(temp[1]);
case COLLECTION:
    col = Integer.valueOf(temp[1]);
case COMMENT:
    com = Integer.valueOf(temp[1]);
```

画面10：
```java
switch (UpdatedArticle.UpdateArticleType.valueOf(temp[0])){
```

画面11：
```java
return String.format("COLLECTION:%d,COMMENT:%d,LIKES:%d,VIEWS:%d", col, com, lik, vie);
```

画面12：
```java
return String.format("COLLECTION:%d,COMMENT:%d,LIKES:%d,VIEWS:%d", col, com, lik, vie);
```

画面13：
```java
return new KeyValue<>(key, toString(), formatObj(key, toString()));
```

画面14：
```java
return String.format("COLLECTION:%d,COMMENT:%d,LIKES:%d,VIEWS:%d", col, com, lik, vie);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：PPT 标题为“3.2.6 综合测试”，其中包含两个要点：
1. 启动文章点赞服务。
2. 在 behavior 服务中添加一个单元测试，为一条已有的数据添加点赞阅读数。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
