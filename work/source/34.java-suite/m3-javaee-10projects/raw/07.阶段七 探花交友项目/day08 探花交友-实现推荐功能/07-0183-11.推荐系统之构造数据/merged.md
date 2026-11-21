# 11.推荐系统之构造数据

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\11.推荐系统之构造数据_【海量资源尽在 666java.com】.mp4
- 时长 5分33秒（音频 333s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们的推荐系统啊那么前面呢我们已经完成了数据的啊这样的一个写入那么接下来呢我们就需要基于前面我们所写的一些数据呢我们去做具体的推荐了那么当然了我们要想去做推荐呢肯定得有一些数据才能推荐啊那么如果我们只是个别的几条数据这个其实没有办法去做推荐的
[00:26] 所以说呢我们有必要呢先来构造一些数据那么我们需要构造两个数据一个就是我们的这个动态信息数据那么另外一个呢就是我们的这个就是Rickmonde就是我们刚刚所写的这个Rickmonde圈子啊这样的一个数据了好那么我们把这两个呢来拷贝一下那我们就把它写到我们的这个double的这个server这个工程里面啊写一个测试用力啊我们来测一下
[00:54] 然后呢我们这个里面呢就我们来看一下啊这个里面我们就应该是在这个里面啊然后在这儿啊刚刚找错这个位置了然后呢我们找到这个test这个里面来然后呢圈子啊写到这个里面来吧然后呢我们把这两个这个测试的方法我们来拷贝一下啊那么这个方法名呢会和前面这个有冲突啊有冲突的话呢我们就写成2吧
[01:23] 然后呢下面这个呢是缺少我们这个对象那我们把这个呃Recommend这个对象就是这个对象我们也拷贝到我们的这个这个里面来啊做一个测试好那么接下来呢我们先来执行一下我们的这个呃就是Save Publish啊呃呃当然了我们先找到之前那个数据啊之前的数据呢我们有三条数据那我把这个数据呢就全部给他就先
[01:49] 删除掉了然后呢下面呢还有是这张表那么这张表的话呢我们就使用这张表的表名使用它写到这然后呢我们把它呢也删除掉也做不掉好嘞好那么接下来呢我们来看一下这个测试用力的一个编写的内容那么首先呢我们来看一下这个是
[02:12] TestSalePublish然后呢我们呢可以看到在这个位置是不是写了一个复循环那么循环100次那么也就意味着我们要写入100条这个动态的信息数据然后呢这个用户ID啊我们是随机产生了1到10之间那么也就是说相当于有10个用户然后呢发送了有100个这个动态啊然后呢我们去设置它的一个PID那么就是
[02:39] 这个1000啊1000加i那么也就是说我们从1000起啊就是1000啊1001 1002这样去编写
[02:48] 然后它的一个地址呢是上海市然后呢C type 1然后呢内容啊图片啊等等然后呢我们做一个税务保存当然了在这个位置需要大家注意一下就是那么我们做一个这个税务的时候前面呢我们其实在这个里面我们这个税务的时候啊那么我们在这是不是要去做一个自增长的一个生成啊但是我们现在其实不需要了因为我们做测试呢我们先把这个注射掉然后执行完之后呢我们再把它打开就可以了
[03:15] 正常情况下我们是需要去生成一个自增长ID的但是呢在我们刚刚的所测试的这个环境中啊那我们是不是直接把这个PID给他写进来了那就不需要做一个测试了啊好那么接下来我们就可以来执行大家注意一下执行的时候啊那我们需要把之前的这个double这个服务呢我们要停掉要不然他会有端口的一个冲突啊这给大家注意一下好那我们就执行他走好那我们来等待他的一个执行
[03:43] 好那么现在呢我们就已经啊执行结束了那我们来看一下这个数据然后呢我们来刷新一下啊publish中肯定会有100条数据我们可以点开来看一下啊他这些这种数据哎ok好那么接下来呢我们就来再次生成什么呢啊生成我们的这个recommend啊这个数据然后呢我们来看一下
[04:07] 这个数据啊这个数据那么循环呢我们循环的是1000次也就是说我们要生成1000条我们的这个推荐的这样的一个数据然后呢它的一个得分的我们是从0到15分的做一个随机的一个生成那么用Y定的也是从1到10呢去随机的去生成这1到10然后呢Public setting是我们从1000到1099
[04:36] 随机啊来做一个生成哎ok好那我们来执行一下走好那么等待他的一个执行那么已经执行结束了啊接下来呢我们来看一下这个数据那么找到这张啊表我们来看一下那么这个就是他所生成的一些数据啊可以看到publics id啊也是随机啊去生成然后用户id也随机然后呢这个score呢也是随机啊随机去做一些这个生成这样的话呢基本是有一定的这个
[05:06] 就是真实性相对真实的一些这个数据然后呢供我们后续的一些这个使用啊OK那么当然了大家也可以把这个数据生成更多一些啊因为数据越多他的这个推荐的这个准确度也就越高啊OK好嘞好那么关于我们这个数据的一个这个生成呢那我们就啊先讲到这里这个是我为我们后面的一个推荐的做一个数据的一个准备OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

