# 画面线理解：07.圈子推荐之发送消息（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\07.圈子推荐之发送消息（上）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:47, 01:33, 02:27, 03:41, 04:50, 05:55, 06:46, 07:35, 08:38, 09:47, 10:40, 11:45, 12:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:54:58

1) 这一组画面整体在讲如何在推荐系统中使用 RocketMQ 实现动态消息的发布功能，包括添加依赖、配置、编写服务类和控制器。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了课程大纲，当前在讲解“1.5.1. QuanzhiMQService”，并显示了添加 RocketMQ 依赖的 Maven 配置片段。
画面2: 展示了 QuanzhiMQService 类的开头部分，导入了相关包并声明了 RocketMQTemplate 和 User 等类。
画面3: 展示了 application.properties 配置文件，其中包含 Redis 集群配置、SSO 配置、FDFS 分布式文件系统配置等。
画面4: 展示了 RocketMQ 相关的配置文件内容，设置了 rocketmq.nameServer 和 spring.rocketmq.producer.group。
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
package com.tanhua.server.service;

import com.alibaba.dubbo.config.annotation.Reference;
import com.tanhua.dubbo.server.api.QuanziApi;
import com.tanhua.dubbo.server.pojo.Publish;
import com.tanhua.server.utils.UserThreadLocal;
import org.apache.rocketmq.spring.core.RocketMQTemplate;
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
#rocketmq相关配置
spring.rocketmq.nameServer=192.168.31.81:9876
spring.rocketmq.producer.group=tanhua
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
package com.tanhua.server.controller;

import com.tanhua.server.service.MovementsService;
import com.tanhua.server.service.QuanzhiMQService;
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
