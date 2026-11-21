# 07.圈子推荐之发送消息（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\07.圈子推荐之发送消息（上）_【海量资源尽在 666java.com】.mp4
- 时长 12分30秒（音频 750s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下发送消息那么前面呢我们讲过啊在流程中呢我们可以来看一下啊就是呃那么用户对于圈子的一些这种动态操作啊都会去发送一个消息给RockDMQ那么我们现在呢要做这一块的一些功能好那么首先呢我们来看一下那么我们需要先去引入我们的一些RockDMQ相关的一些这个依赖那么在我们这个server这个工程中
[00:28] 好 那么我们把它拿来拷贝一下然后找到我们这个server这个工程那么因为我们的用户超度都是在这个工程中然后我们就把它丢到最下面来吧丢到这好 那我们把这个RoftMQ相关的一些这个依赖就导入进来那么导入进来之后接下来我们就需要去编写一个这个叫ChangerMQ的一个Service去做一个消息的一个发送的一个处理那么我们就来回到我们的
[00:58] 在我们这个Service中那我们需要去写一个这样的一个类写这样的一个类好那么我们把它标记为这是一个什么呢标记为这是一个Service好那么相关的一些逻辑在这里面是不是就可以去做一个完成了那么首先呢我们在这个位置去注入什么呢是rocket这个template mqtemplate把它注进来当然了
[01:26] 我们是不是还是需要去做一下配置对吧那么在我们的applicationappopolis文件中它并没有去配我们来配置一下好那么在配置中我们需要配置两项那么第一个就是我们 rocketMQ的一个name server是它第二个就是配置我们的一个produce的一个grip那么是一个探花好那么这个我们把它加到我们的
[01:54] 我们来看一下下面应该还没有那么我们加到上面这个位置来就加到我们的这个讲义中然后呢我们来看一下这一块我们得这样操作一下了因为没有空行那么我们这样来操作一下那么下面这个呢是我们的一个配置配置文件好那我们来退出到我们这个视图中配置文件呢我们去写一下这个就是properties
[02:22] 那我们就写到obligationproperties中好那么这个是相关的配置啊下面这个呢是我们相关的一些这个代码啊ok好那么到这里呢我们是不是就呃把配置呢就已经啊导入进来了呃然后呢我们来看一下那么我们就可以在我们的这个刚刚所写的这个Service中啊去编写一些相关的一些逻辑了好那么下面我们来看一下这个逻辑的一个编写那么首先呢我们编写一个方法那么我们
[02:51] 先编写的是一个私有方法那么就是一个叫send messagesend message这样的一个方法那么这个方法会有两个参数那么第一个参数就是我们要去发送的一个类型对吧就是你是什么样的一个消息类型那么一个就是我们的一个public idpublic id那么
[03:19] 然后呢这个类型其实应该是我们的int类型啊就是我们前面所看到的这个计分这个规则啊这么几个这个操作对吧这么几个操作那么我们可以来写一下比如说我们有这么几个操作比如说我们这个type啊它其实指的就是我们先写这个叫什么呢叫发送啊这个消息然后type呢就会有这么几个啊那我们就直接来拷贝一下吧拷贝下面的这个这个内容那么我们把它来拷贝一下啊
[03:48] 好那么type就是他就说第一这么几个操作第一就是发动态第二是浏览动态第三就是我们点赞第四是喜欢
[03:59] 第五是评论第六是取消点赞第七是取消喜欢那么大概有七个这样的一个操作我们在这个位置就需要去发送我们的消息那么发送我们消息我们需要去构造我们的一个消息体对吧那么我们可以通过list.template做一个什么convert understand是不是做一个发送那么第一个就是我们的一个目标那么目标其实就是我们需要去写一下我们这样的一个topic
[04:29] 那我们就写谁呢叫比如说探探花杠然后呢我们就写一个圈子对吧然后呢后面这个呢就是我们的消息体了那么消息体呢我们其实可以写一个这个mapmap比如我们写一个stream然后呢再写一个object吧然后呢写一个messagemessage等于new一个hcmap这个呢就是我们所发送的一个消息体内容哎呀OK
[04:58] 好 那么我们来看一下这个消息内容需要设置哪些东西那么首先第一个我们是需要把这个type肯定要传递出去对吧那么在我们接收到这个消息之后我们好去做一个处理那么是针对于不同的一些这个操作我们要做出不同的一些处理的然后第二个就是我们需要把我们publicsid是不是也需要发出去然后我们还是需要去发送谁呢比如说我们put一个
[05:26] 时间这个肯定是不是也是需要的把我们当前的这个时间戳呢发出去那么那么还有谁呢比如说我们还有这个叫做UraID用户ID那么肯定也得发出去对吧那么所以在这个位置那么我们又需要拿到这个Ura了那么我们去把这个Ura呢导入进来那Ura等于等于什么呢叫UraSuiteUraSuiteLocal.get那么拿到它之后那么我们就通过这个Ura
[05:55] 然后点get id这样去拿到它然后这个是us id比如说我们还需要谁在我们publish中是我们新增了一个pid的我们必须把这个pid是不是也拿到但是我们现在并没有这个pid怎么办但是我们有这个publish id对吧我们就需要去查询一下所以我们需要通过这个publish id来查询到我们的pid我们去做一个发送
[06:23] 好那么我们就把我们这个圈子API这个注入进来那么把它呢做一个reface那么去引入进来在这儿那么这个Watson版本呢就是1.0.0然后呢我们通过这个圈子这个来做一个获取那我们就在这儿吧叫做我们this.这个圈子API.queryPublishById把这个PublishId传递过去
[06:50] 那我们就会得到一个publish对象那我们就拥有了谁呢是不是拥有了我们这个pid点get什么pid打到他好那么有了这个数据之后基本上是不是也就ok了那我们是不是就可以把它发出去了那么我们把这个呢做一个try catch的处理那么因为发送消息呢不要去影响我们正常逻辑的一个执行那我们就直接去做一个try catch的一个处理那么在这个位置就定一个
[07:20] 什么呢exception吧好那么我们在这个位置呢把这个异常打印一下那么我们就还是得定义一个我们的一个这个log4jlogger对象然后呢定义这个logger等于我们loggerlogger factory.getlogger这个圈子这个mqservice.class好那我们去记录一下这个就叫什么呢就是我们这个
[07:49] 就是我们的叫圈子圈子的这个消息发送失败发送失败然后呢我们记录一下比如说就记录两个参数一个呢就是这个type等于等于加一个这个type那么另外一个呢就是加一个什么呢就是publishpublish然后呢id它等于去加一个
[08:19] Public ID然后呢我们再传递一个这个E就对象就是Exception这样的一个对象好那么这样的话是不是我们这个是不是就搞定了对吧这个是我们编写了一个通用的一个方法那么接下来呢我们就在上面去编写我们直接可以调用的方法比方说呢第一个啊第一个呢就叫这个发送动态那我们就写一个叫做什么呢比方说叫SendSend这个Sale
[08:47] C5 Publish然后message这样去写叫C5 PublishMessage然后我们来看一下在这个位置我们需要把这个Publish ID是不是也传递过来然后我们直接就去调用类似点Send Message把这个Type就设置为1第二个就是Publish IDOK这样的话是不是就可以了这是我们第一个操作这个是发送什么动态这个消息
[09:18] 就是我们去新增我们别发送了就是这个新增吧叫做新增动态的这样的一个消息然后呢我们类似于这个方法那我们就做一个拷贝那么第二个呢叫做什么呢浏览那我们就叫这个把C5改成什么queryquery publish message传递它那么这个type呢就改成2那么这个我们来写一下这个叫什么呢就是浏览动态的这个消息这第二个这个操作那我们来看一下这个
[09:48] 第三个啊这个操作那么第三个呢把它改成这个三是点赞对吧点赞我们就这个叫like啊like好那么这个改成啊点赞点赞这个消息那么第四个啊第四个叫什么呢喜欢那第四我们这个改成几个四然后呢这一块改成把点赞改成什么呢喜欢然后呢还有评论啊评论
[10:18] 评论呢是comment那么我们把这个like跟着comment啊comment然后呢这个改成几呢是五对吧五然后呢这个是评论啊评论呃这个是五还有六和七那我们一起来写一下对吧这个是再来个六啊再来个七啊这个是七那七呢是叫什么呢取消喜欢那就写一个低思什么呢这个烙低思
[10:51] 那么把这个comment去掉这个呢就是叫取消取消喜欢啊动态消息上面的这个呢第六是什么我们来看一下啊第六呢是取消点赞那么这个改成六那么这个改成取消取消点赞这个就comment我们改成dislikedislikepublish好这样的话我们是不是就
[11:22] 已经就完成了这样的一个编写这块是不是我们还多了一个这个叫这个改成什么呢好检查一下有没有问题啊1234567啊总共呢有7个这个方法那我们只需要在我们的Controller中是不是去调用这个Service啊是不是就可以了对吧ok好那我们来看一下我们的讲义啊
[11:50] 那么在我们讲义中是不是也是去编写了这样一些逻辑对吧重点是编写下面的Service那么可以看到有发布动态的消息这个也是123当然了它的参数的位置跟我们的刚刚所编写代码的位置颠倒这个其实没有关系大家能够理解这个意思就可以了好那么最终就是发送这个消息下面去构造我们这个消息没有问题然后去做一个发送OK
[12:20] 好嘞好那么到这里呢我们是不是就已经完成了这个消息的一个发送那么下面通过control了调用就OK了啊好那么我们先把这个视频呢先来保存一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在推荐系统中使用 RocketMQ 实现动态消息的发布功能，包括添加依赖、配置、编写服务类和控制器。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程大纲，当前在讲解“1.5.1. QuanzhiMQService”，并显示了添加 RocketMQ 依赖的 Maven 配置片段。
画面2: 展示了 QuanzhiMQService 类的开头部分，导入了相关包并声明了 RocketMQTemplate 和 User 等类。
画面3: 展示了 application.properties 配置文件，其中包含 Redis 集群配置、SSO 配置、FDFS 分布式文件系统配置等。
画面4: 展示了 RocketMQ 相关的配置文件内容，设置了 RocketMQ.nameServer 和 spring.RocketMQ.producer.group。
画面5: 展示了 QuanzhiMQService 类中定义的 RocketMQTemplate 字段和注解。
画面6: 展示了 sendMsg 方法的开始部分，准备构建消息体。
画面7: 展示了 sendMsg 方法中构建消息体的代码，包括 type、publishId、date 和 userId。
画面8: 展示了 sendMsg 方法中添加了查询评论数和用户信息的字段。
画面9: 展示了 QuanzhiMQService 类中定义的 Logger 字段。
画面10: 展示了 QuanzhiMQService 类中定义的 QuanZiApi 字段和 RocketMQTemplate 字段。
画面11: 展示了 sendSavePublishMsg 方法，用于发送新增动态消息。
画面12: 展示了 sendQueryPublishMsg 方法，用于发送浏览动态消息。
画面13: 展示了 sendCommentPublishMsg 方法，用于发送评论动态消息。
画面14: 展示了 MovementsController 类的开头部分，导入了 MovementsService 和 QuanzhiMQService。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

画面2:
```java
package com.tanhua.server.Service;

import com.alibaba.dubbo.config.annotation.Reference;
import com.tanhua.dubbo.server.api.QuanziApi;
import com.tanhua.dubbo.server.pojo.Publish;
import com.tanhua.server.utils.UserThreadLocal;
import org.apache.RocketMQ.spring.core.RocketMQTemplate;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class QuanziMQService {
```

画面3:
```properties
spring.redis.cluster.nodes=192.168.31.81:6379,192.168.31.81:6380
tanhuu.sso.url=http://127.0.0.1:18080
#默认今日达人推荐用户
tanhuu.sso.default.user=2
#是否开启数据缓存
tanhuu.cache.enable=false

# 分布式文件系统FDFS配置
#fdfs.so-timeout = 1501
#fdfs.connect-timeout = 601
#缩略图生成参数
fdfs.thumb-image.width=150
fdfs.thumb-image.height=150
#TrackerList参数，支持多个
fdfs.tracker-list=192.168.31.81:22122
fdfs.web-server-url=http://192.168.31.81:8080/
```

画面4:
```properties
#RocketMQ相关配置
spring.RocketMQ.nameServer=192.168.31.81:9876
spring.RocketMQ.producer.group=tanhua
```

画面5:
```java
@Service
public class QuanziMQService {

    @Autowired
    private RocketMQTemplate rocketMQTemplate;

    @Reference
    private QuanZiApi quanZiApi;
```

画面6:
```java
private void sendMsg(Integer type, String publishId) {
    User user = UserThreadLocal.get();
    Map<String, Object> msg = new HashMap<>();
    msg.put("type", type);
    msg.put("publishId", publishId);
    msg.put("date", System.currentTimeMillis());
    msg.put("userId", user.getId());
    this.rocketMQTemplate.convertAndSend("tanhua-quanzi", msg);
}
```

画面7:
```java
private void sendMsg(Integer type, String publishId) {
    User user = UserThreadLocal.get();
    Map<String, Object> msg = new HashMap<>();
    msg.put("type", type);
    msg.put("publishId", publishId);
    msg.put("date", System.currentTimeMillis());
    msg.put("userId", user.getId());
    this.rocketMQTemplate.convertAndSend("tanhua-quanzi", msg);
}
```

画面8:
```java
private void sendMsg(Integer type, String publishId) {
    User user = UserThreadLocal.get();
    Map<String, Object> msg = new HashMap<>();
    msg.put("type", type);
    msg.put("publishId", publishId);
    msg.put("date", System.currentTimeMillis());
    msg.put("userId", user.getId());
    msg.put("queryCommentCount", queryCommentCount(publishId, type));
    this.rocketMQTemplate.convertAndSend("tanhua-quanzi", msg);
}
```

画面9:
```java
private static final Logger LOGGER = LoggerFactory.getLogger(QuanziMQService.class);
```

画面10:
```java
@Reference(version = "1.0.0")
private QuanZiApi quanZiApi;
```

画面11:
```java
public void sendSavePublishMsg(String[] publishId) {
    this.sendMsg(type: 1, publishId);
}
```

画面12:
```java
public void sendQueryPublishMsg(String publishId) {
    this.sendMsg(type: 2, publishId);
}
```

画面13:
```java
public void sendCommentPublishMsg(String publishId) {
    this.sendMsg(type: 5, publishId);
}
```

画面14:
```java
package com.tanhua.server.Controller;

import com.tanhua.server.Service.MovementsService;
import com.tanhua.server.Service.QuanzhiMQService;
import com.tanhua.server.vo.Movements;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/movements")
public class MovementsController {
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。

