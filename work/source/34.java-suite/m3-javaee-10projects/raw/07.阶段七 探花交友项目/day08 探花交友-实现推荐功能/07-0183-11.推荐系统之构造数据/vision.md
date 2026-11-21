# 画面线理解：11.推荐系统之构造数据

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\11.推荐系统之构造数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:48, 01:10, 01:23, 01:39, 02:00, 02:11, 03:28, 03:39, 03:51, 04:03, 04:45, 05:04, 05:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:58:06

1) 这一组画面整体在讲什么（一句话）：
演示如何在推荐系统中通过测试代码生成并保存动态（Publish）和推荐（RecommendQuanZi）数据，并通过 MongoDB 查看数据存储结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Markdown 文件 day08.md 的内容，其中包含“2. 推荐系统”标题。
- 代码部分：一个测试方法 testSavePublish()，用于创建并保存 Publish 对象。
- 代码中设置了 userId、locationName、seeType、text、medias 等属性，并调用 quanZiApi.savePublish() 保存。

画面 2：
- 展示了 QuanZiMsgConsumer.java 文件中的 onMessage 方法。
- 代码逻辑：从消息中解析 type、publishId、date、userId、pid，创建 RecommendQuanZi 对象并设置属性，然后根据 type 做不同处理。
- 注释说明了不同 type 对应的操作：1-发动态，2-浏览动态，3-点赞，4-喜欢，5-取消点赞，7-取消喜欢。

画面 3：
- 展示了 TestQuanzi.java 文件中的 testSavePublish() 方法。
- 代码逻辑：创建 Publish 对象，设置 userId、locationName、seeType、text、medias，然后调用 quanZiApi.savePublish() 保存。
- 代码中设置了 locationName 为“上海市”，text 为“今天天气不错~”。

画面 4：
- 展示了 TestQuanzi.java 文件中的 testSaveRecommend() 方法。
- 代码逻辑：循环 1000 次，创建 RecommendQuanZi 对象，设置 id、date、userId、publishId、score、type，然后调用 mongoTemplate.save() 保存到指定集合。

画面 5：
- 展示了 TestQuanzi.java 文件中的 testSavePublish2() 方法。
- 代码逻辑：循环 100 次，创建 Publish 对象，设置 userId、pid、locationName、seeType、text、medias，然后调用 quanZiApi.savePublish() 保存。

画面 6：
- 展示了 TestQuanzi.java 文件中的 testSaveRecommend() 方法。
- 代码逻辑：循环 1000 次，创建 RecommendQuanZi 对象，设置 id、date、userId、publishId、score、type，然后调用 mongoTemplate.save() 保存到指定集合。

画面 7：
- 展示了 TestQuanzi.java 文件中的 testSavePublish2() 和 testSaveRecommend() 方法。
- 代码逻辑：testSavePublish2() 设置 userId、pid、locationName、seeType、text、medias；testSaveRecommend() 设置 id、date、userId、publishId、score、type。

画面 8：
- 展示了 TestQuanzi.java 文件中的 testSavePublish2() 方法。
- 代码中设置了 locationName 为“上海市”，text 为“今天天气不错~”。

画面 9：
- 展示了 TestQuanzi.java 文件中的 testSavePublish2() 方法。
- 代码中设置了 locationName 为“上海市”，text 为“今天天气不错~”。

画面 10：
- 展示了 Robo 3T 数据库客户端界面。
- 当前选中集合：quant_publish。
- 执行的查询语句：db.getCollection('quant_publish').find()。

画面 11：
- 展示了 TestQuanzi.java 文件中的 testSaveRecommend() 方法。
- 代码逻辑：循环 1000 次，创建 RecommendQuanZi 对象，设置 id、date、userId、publishId、score、type，然后调用 mongoTemplate.save() 保存到指定集合。

画面 12：
- 展示了 Robo 3T 数据库客户端界面。
- 当前选中集合：quant_publish。
- 查询结果：显示了多个文档，其中一条文档的 score 为 100，userId 为 5，publishId 为 30。

画面 13：
- 展示了 Robo 3T 数据库客户端界面。
- 当前选中集合：recommend_quanzi_20191001。
- 查询结果：显示了多个文档，其中一条文档的 score 为 100，userId 为 8，publishId 为 30。

画面 14：
- 展示了 day08.md 文件的内容。
- 代码部分：testSaveRecommend() 方法，循环 1000 次，创建 RecommendQuanZi 对象，设置 id、date、userId、publishId、score、type，然后调用 mongoTemplate.save() 保存到指定集合。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
@Test
public void testSavePublish() {
    Publish publish = new Publish();
    publish.setUserId(11);
    publish.setLocationName("上海市");
    publish.setSeeType(1);
    publish.setText("今天天气不错~" + i);
    publish.setMedias(Arrays.asList("http://itcast-tanhua.oss-cn-shanghai.aliyuncs.com/images/2019/10/01/156992621084717.png",
            "http://itcast-tanhua.oss-cn-shanghai.aliyuncs.com/images/2019/10/01/156992621083644.png",
            "http://itcast-tanhua.oss-cn-shanghai.aliyuncs.com/images/2019/10/01/156992621092211.png"));
    String publishId = this.quanZiApi.savePublish(publish);
    System.out.println(publishId);
}
```

画面 2：
```java
@Override
public void onMessage(String msg) {
    JsonNode jsonNode = MAPPER.readTree(msg);
    int type = jsonNode.get("type").asInt();
    String publishId = jsonNode.get("publishId").asText();
    Long date = jsonNode.get("date").asLong();
    Long userId = jsonNode.get("userId").asLong();
    RecommendQuanZi recommendQuanZi = new RecommendQuanZi();
    recommendQuanZi.setPublishId(publishId);
    recommendQuanZi.setDate(date);
    recommendQuanZi.setUserId(userId);
    switch (type) {
        case 1: {
            // 动态
            break;
        }
        case 2: {
            // 浏览动态
            break;
        }
        case 3: {
            // 点赞
            break;
        }
        case 4: {
            // 喜欢
            break;
        }
        case 5: {
            // 取消点赞
            break;
        }
        case 7: {
            // 取消喜欢
            break;
        }
    }
}
```

画面 3：
```java
@Test
public void testSavePublish() {
    Publish publish = new Publish();
    publish.setUserId(11);
    publish.setLocationName("上海市");
    publish.setSeeType(1);
    publish.setText("今天天气不错~" + i);
    publish.setMedias(Arrays.asList("http://itcast-tanhua.oss-cn-shanghai.aliyuncs.com/images/2019/10/01/156992621084717.png",
            "http://itcast-tanhua.oss-cn-shanghai.aliyuncs.com/images/2019/10/01/156992621083644.png",
            "http://itcast-tanhua.oss-cn-shanghai.aliyuncs.com/images/2019/10/01/156992621092211.png"));
    String publishId = this.quanZiApi.savePublish(publish);
    System.out.println(publishId);
}
```

画面 4：
```java
@Test
public void testSaveRecommend() {
    for (int i = 0; i < 1000; i++) {
        RecommendQuanZi recommendQuanZi = new RecommendQuanZi();
        recommendQuanZi.setId(ObjectId.get());
        recommendQuanZi.setDate(System.currentTimeMillis());
        recommendQuanZi.setScore(Double.valueOf(RandomUtils.nextInt(0, 15)));
        recommendQuanZi.setUserId(RandomUtils.nextLong(1, 10));
        recommendQuanZi.setPublishId(RandomUtils.nextLong(1000, 1099));
        this.mongoTemplate.save(recommendQuanZi, collectionName: "recommend_quanzi_20191001");
    }
}
```

画面 5：
```java
@Test
public void testSavePublish2() {
    for (int i = 0; i < 100; i++) {
        Publish publish = new Publish();
        publish.setUserId(RandomUtils.nextLong(1, 10));
        publish
