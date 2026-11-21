# 10.圈子功能实现之发布动态（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\10.圈子功能实现之发布动态（下）_【海量资源尽在 666java.com】.mp4
- 时长 6分12秒（音频 372s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们就来编写一下测试用力,然后呢去测试一下那么这个呢就是测试用力了,我们就直接拿过来使用了然后呢我们来拷贝一下找到我们的这个代码,那么我们在这个位置呢我们就写一个测试用力叫做什么呢,test水呢,比方说叫圈子圈子好,那么我们呢就去写两个注点,对吧一个呢叫做什么呢
[00:27] 叫做run with谁呢sprint然后呢jolitor for这个runner然后呢再写一个sprint boot test那么这样的话就可以去完成一个测试了那我们把之前所是写的这个什么叫做圈子圈子API的这个它的一个对象的注入进来那么做一个注入下面呢我们就可以把刚刚这个代码呢就copy过来了
[00:54] 那么这样的话呢就可以去实现实现这样的一个这样的一个操作了好那么我们去在这个位置呢构建了我们的一个public对象然后呢要注意的是他的这个UID呢是1UID呢是1那么因为这个1这个用户呢我们设置了有几个这个好友所以可以看到这样的一个效果OK好那么接下来呢我们就来执行一下那我们来看一下最终的一个结果会怎么样
[01:23] 然后呢我们当然我们可以去打一个断点是吧比如说呢我们在这个位置吧我们去打一个断点我们看他会怎么样去做一个执行好那么我们在这个位置吧去执行执行一个debug的一个启动了好那我们来等待一下他的一个启动那么启动之后呢就会进入这个断点了好那我们来看一下他的一个执行过程那么首先呢去
[01:50] 判断一下ID肯定不为空对吧然后呢我们去设置一个ID然后呢设置这个权限然后呢做一个SAVE的一个保存OK那么到这呢就保存完成了那么我们可以到这个位置来刷新一下看一下那么是不是有一个publish这样的一张表那么是不是已经有一条数据了对吧好那么接下来我们继续往下面走走走走这个呢就是我们的相册表
[02:14] 然后我们去再去做一个保存那么我们就会拥有了什么自己的一个这样的一张表了对吧是不是有一个这个唯一的这样的这个表那么可以看到这个就是这个ID所指向的就是我们刚刚所看到的这个ID它的ID是不是就是这个03ac这个是不是就是03ac对吧03ac好的我们接着继续再往下面去走
[02:43] 去查询这个Uris那么会发现的这个Uris是5对吧是不是有5个这个好友对吧5个好友然后呢我们继续往下面去写走走走这是去往第一个好友中去给他写出数据那我们来看一下这个数据对不对呢我们来刷新一下啊然后在这个位置是不是一个Terminal2那么就是ID为2的这个用户呢是不是就有了这个ID为1的用户的这样的一个动态了对吧
[03:11] 好那我们接着继续往下面走走走这是第二条对吧走哎第二条那么我们再来刷新一下是不是就有了这个三对吧然后呢去看查看一下是不是还是这条数据啊然后呢继续往下面去写这是第三条了那我们就直接通过吧然后呢直接通过走好那我们再来刷新一下再来刷新一下那么是不是二三四五六这个都是一些好友啊
[03:40] 那么如果现在的用户YD为5的这个用户去查询这个就是圈子动态的时候是不是直接去查询这张表是不是就跟能够拿到动态了对吧所以这个呢就是我们前面所说的这个什么呢写入的时候可能我们会花费一些我们的这个工作量然后呢但是呢我们在读取的时候就变得更简单了那么就是成本的也就更低了OK好那么其实到这里呢我们是不是
[04:07] 就能够看出目前我们已经就实现了我们的这样的一个保存我们的一个动态但这个里面会有一个问题就是那么大家其实也能够看出这样的一个问题就是什么呢事物问题那么我们其实保存了有多张表那么如果其中有一个出问题的话那么是不是必然会导致什么呢必然会导致这个一些这个就是比如说我就是动态信息保存了
[04:36] 但是呢我这个相册表没有保存或者说我的一些好友表呢没有保存啊会出现这样的一种情况那么这个应该怎么去做呢其实呢我们可以来看一下我们的讲义啊那么在讲义中呢我们其实应该是把我们的三个这个保存这个逻辑啊那我们去放到一个try cut里面来那么如果一旦出错的话那我们就应该去做一个事物的这样的一个回滚了那么这样的话就可以做一个保障啊当然我们这个呢就不做具体实现了
[05:06] 那么我们就大家如果要是有这个需求的话也可以去做一个实践那么我们就直接去做一个最简单的一个这个try cut一个操作吧那我们就去写一个try cut那么如果一旦有异常的话那么这个位置就应该做一个什么呢做一个事物的一个回滚OK好然后呢走到这呢那就是returnreturn什么呢true
[05:34] 然后呢在最后面呢就return什么呢false哎呦ok好嘞好那么这样的话呢这个逻辑是不是就ok了当然这个我们就不做具体的实现了因为
[05:44] 这个呢不是在我们这个课程中呢去涉及到的一个这个处理的一个范围啊OK好那么呃接下来呢我们来看一下啊那么到目前为止我们是不是就已经完成了我们的一个这个double接口的一个编写啊那后面我们是不是就可以基于这个double的一个这个接口呢来做我们具体服务编写了对吧OK好那么关于我们这个保存我们的一个这个发布那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中编写一个用于保存动态（Publish）并同步写入用户相册和好友时间线的接口服务，包含单元测试和 MongoDB 操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了课程笔记文档（day03 四子.md），目录结构显示当前在“2.2.3. 编写接口服务”下的“2.2.3.1. Controller”部分。
- 代码片段：测试用例 `@Test public void testSavePublish(){ ... }`，其中创建了 `Publish` 对象并调用 `quanziApi.savePublish(publish)`。

画面 2:
- 展示了 IDE 中的项目结构，选中了测试类 `TestQuanzi.java`。
- 代码片段：`@RunWith(SpringBootTest)` 注解，以及导入的 Spring Boot 测试相关类。

画面 3:
- 展示了测试类 `TestQuanzi` 的代码，其中定义了 `private QuanziApi quanziApi;` 字段。

画面 4:
- 展示了服务实现类 `QuanziApiImpl` 的代码，包含 `@Service(version = "1.0.0")` 注解和 `@Autowired private MongoTemplate mongoTemplate;` 字段。
- 代码片段：`@Override public boolean savePublish(Publish publish) { ... }` 方法，包含校验、填充数据、保存动态等逻辑。

画面 5:
- 展示了调试过程，`publish` 对象的变量值已设置，`this.mongoTemplate.save(publish);` 语句被选中。
- 调试器显示 `this` 对象和 `publish` 对象的详细信息。

画面 6:
- 展示了代码中创建 `Album` 对象并保存到 MongoDB 的部分。
- 代码片段：`Album album = new Album(); album.setId(ObjectId.get()); ... this.mongoTemplate.save(album, collectionName: "quanzi_album_" + publish.getUserId());`

画面 7:
- 展示了查询用户好友数据并创建 `Timeline` 对象的代码。
- 代码片段：`Query query = Query.query(Criteria.where("userId").is(publish.getUserId())); List<Users> users = this.mongoTemplate.find(query, Users.class);`

画面 8:
- 展示了创建 `Timeline` 对象并设置属性的代码。
- 代码片段：`Timeline timeline = new Timeline(); timeline.setUserId(publish.getUserId()); timeline.setPublishId(publish.getId()); timeline.setDate(System.currentTimeMillis());`

画面 9:
- 展示了将 `Timeline` 对象保存到 MongoDB 的代码。
- 代码片段：`this.mongoTemplate.save(timeline, collectionName: "quanzi_time_line_" + user.getFriendId());`

画面 10:
- 展示了 `savePublish` 方法的结尾部分，`return true;` 语句。
- 调试器显示“Application is running”。

画面 11:
- 展示了课程笔记文档（day03 四子.md），其中包含对代码逻辑的注释，如“//写入到自己的相册表中”、“//查询当前用户的友好的数据”等。

画面 12:
- 展示了 `savePublish` 方法中校验和填充数据的部分。
- 代码片段：`if (publish.getUserId() == null) { return false; } ... publish.setCreated(System.currentTimeMillis());`

画面 13:
- 展示了代码中 `return false;` 语句的上下文，以及 IDE 提示的异常类列表。
- 代码片段：`return false;` 语句。

画面 14:
- 展示了课程笔记文档（day03 四子.md），其中包含对 `savePublish` 方法的注释，如“//校验”、“//填充数据”、“//保存动态信息”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Test
public void testSavePublish(){
    Publish publish = new Publish();
    publish.setUserId(1L);
    publish.setLocaionName("上海市");
    publish.setSeeType(1);
    publish.setText("今天天气不错");
    publish.setMedias(Arrays.asList("https://itcast-tanhua.oss-cn-shanghai.aliyuncs.com/images/quanzi/1.jpg"));
    boolean result = this.quanziApi.savePublish(publish);
    System.out.println(result);
}
```

画面 2:
```java
package com.tanhua.dubbo.server.api;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot

