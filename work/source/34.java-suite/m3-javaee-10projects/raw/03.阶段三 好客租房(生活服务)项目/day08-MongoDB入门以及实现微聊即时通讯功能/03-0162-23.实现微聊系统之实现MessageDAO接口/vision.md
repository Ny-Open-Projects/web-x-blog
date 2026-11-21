# 画面线理解：23.实现微聊系统之实现MessageDAO接口

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\23.实现微聊系统之实现MessageDAO接口【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:30, 03:27, 05:01, 08:11, 09:49, 10:54, 12:44, 13:48, 15:05, 16:38, 18:33, 20:22, 21:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:48:30

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 和 MongoDB 实现一个简单的点对点消息系统，包括 DAO 层接口与实现、实体类定义、测试类编写及配置文件设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 MessageDAO 接口定义，包含 findByFromAndTo 方法，用于查询指定发送者和接收者之间的消息列表。
画面 2: 展示 MessageDAOImpl 类中 findByFromAndTo 方法的实现，使用 Criteria 构建查询条件。
画面 3: 展示 MessageDAOImpl 中 findByFromAndTo 方法的实现，使用 Criteria 和 Query 对象构建查询，并调用 mongoTemplate.find。
画面 4: 展示 Message 实体类的定义，包含 id、msg、status、sendDate、readDate、from、to 等字段，并使用 @Builder、@Indexed 等注解。
画面 5: 展示 MessageDAOImpl 中 findByFromAndTo 方法的实现，构建 Criteria 条件并设置分页参数 PageRequest。
画面 6: 展示在 MessageDAOImpl 中使用 Criteria 构建查询条件，其中包含 fromId 和 toId 的条件。
画面 7: 展示 MessageDAOImpl 中 saveMessage 和 deleteMessage 方法的实现，调用 mongoTemplate 的 save 和 delete 方法。
画面 8: 展示 PDF 文档中 Message 实体类的构建示例，包含设置 id、msg、from、to、status 等属性并调用 saveMessage 方法。
画面 9: 展示 ImApplication 主类，使用 @SpringBootApplication 注解，定义 main 方法。
画面 10: 展示 application.properties 配置文件，设置 spring.application.name 和 spring.data.mongodb.uri。
画面 11: 展示 TestMessageDAO 测试类中 testSave 方法，调用 messageDAO.saveMessage 保存消息。
画面 12: 展示 TestMessageDAO 测试类中 testQueryList 方法，调用 messageDAO.findByFromAndTo 查询消息并打印。
画面 13: 展示 PDF 文档中 TestMessageDAO 测试类的 testSave 方法，用于测试消息保存功能。
画面 14: 展示 MessageDAOImpl 类的完整定义，包含导入的包和 @Component 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import com.mongodb.client.result.DeleteResult;
import com.mongodb.client.result.UpdateResult;
import org.bson.types.ObjectId;

public interface MessageDAO {
    /**
     * 查询点对点聊天记录
     * @param fromId
     * @param toId
     * @param page
     * @param rows
     * @return
     */
    List<Message> findByFromAndTo(Long fromId, Long toId, Integer page, rows);
}
```

画面 2:
```java
@Override
public List<Message> findByFromAndTo(Long fromId, Long toId, Integer page, Integer rows) {
    return this;
}
```

画面 3:
```java
@Override
public List<Message> findByFromAndTo(Long fromId, Long toId, Integer page, Integer rows) {
    Criteria criteria = new Criteria().orOperator();
    Query query = Query.query(criteria);
    return this.mongoTemplate.find(query, null, Message.class);
}
```

画面 4:
```java
@Builder
public class Message {
    @Id
    private ObjectId id;
    private String msg;
    /**
     * 消息状态，1-未读，2-已读
     */
    @Indexed
    private Integer status;
    @Field("send_date")
    @Indexed
    private Date sendDate;
    @Field("read_date")
    @Indexed
    private Date readDate;
    @Indexed
    private User from;
    @Indexed
    private User to;
}
```

画面 5:
```java
// 用户A发送给用户B的条件
Criteria criteriaTo = new Criteria().andOperator(
    Criteria.where("from_id").is(fromId),
    Criteria.where("to_id").is(toId)
);

Criteria criteria = new Criteria().orOperator(criteriaFrom, criteriaTo);

PageRequest pageRequest = PageRequest.of(page, rows, Sort.by(Sort.Direction.ASC, "sendDate"));

Query query = Query.query(criteria).with(pageRequest);
return this.mongoTemplate.find(query, Message.class);
```

画面 6:
```java
where("from_id").is(fromId),
where("to_id").is(toId)
```

画面 7:
```java
@Override
public Message findMessageById(String id) {
    return null;
}

@Override
public UpdateResult updateMessageState(ObjectId id, Integer status) {
    return null;
}

@Override
public Message saveMessage(Message message) {
    return this.mongoTemplate.save(message);
}

@Override
public DeleteResult deleteMessage(String id) {
    return null;
}
```

画面 8:
```java
message = Message.builder()
    .id(ObjectId.get())
    .msg("你好啊")
    .sendDate(new Date())
    .from(new User(1001, "zhangsan"))
    .to(new User(1002, "lisi"))
    .build();
this.messageDAO.saveMessage(message);

message = Message.builder()
    .id(ObjectId.get())
    .msg("你也好")
    .sendDate(new Date())
    .from(new User(1001, "zhangsan"))
    .to(new User(1002, "lisi"))
    .build();
this.messageDAO.saveMessage(message);
```

画面 9:
```java
package cn.itcast.haoke.im;

import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ImApplication {
    public static void main(String[] args) {
        SpringApplication.run(ImApplication.class, args);
    }
}
```

画面 10:
```properties
spring.application.name=itcast-haoke-im
spring.data.mongodb.uri=mongodb://172.16.55.185:27017/testdb
```

画面 11:
```java
this.messageDAO.saveMessage(message);
System.out.println("ok");
```

画面 12:
```java
public void testQueryList() {
    List<Message> list = this.messageDAO.findByFromAndTo(fromId: 1001L, rows: 10);
    for (Message message : list) {
        System.out.println(message);
    }
}
```

画面 13:
```java
@RunWith(SpringRunner.class)
@SpringBootTest
public class TestMessageDAO {
    @Autowired
    private MessageDAO messageDAO;

    @Test
    public void testSave() {
        Message message = Message.builder()
            .id(ObjectId.get())
            .msg("你好啊")
            .sendDate(new Date())
            .from(new User(1001, "zhangsan"))
            .to(new User(1002, "lisi"))
            .build();
        this.messageDAO.saveMessage(message);

        message = Message.builder()
            .id(ObjectId.get())
            .msg("你也好")
            .sendDate(new Date())
            .from(new User(1001, "zhangsan"))
            .to(new User(1002, "lisi"))
            .build();
        this.messageDAO.saveMessage(message);
    }
}
```

画面 14:
```java
package cn.itcast.haoke.im.dao.impl;

import cn.itcast.haoke.im.dao.MessageDAO;
import cn.itcast.haoke.im.pojo.Message;
import cn.itcast.haoke.im.pojo.User;
import com.mongodb.client.result.DeleteResult;
import com.mongodb.client.result.UpdateResult;
import org.bson.types.ObjectId;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.Update;
import org.springframework.stereotype.Component;

@Component
public class MessageDAOImpl implements MessageDAO {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8: PDF 文档中显示了“4.1. 在创建 itcast-haoke-im 工程”、“4.2. 编写 MessageDAO”、“4.3. 实现”、“4.4. 测试”等章节标题。
画面 13: PDF 文档中显示了“编写实现类”章节标题。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
