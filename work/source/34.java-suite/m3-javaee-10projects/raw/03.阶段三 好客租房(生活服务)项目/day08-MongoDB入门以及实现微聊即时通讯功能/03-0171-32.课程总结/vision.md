# 画面线理解：32.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\32.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:36, 00:39, 01:03, 01:05, 01:18, 01:23, 01:30, 01:37, 02:50, 02:52, 02:56, 03:04, 03:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:54:50

1) 这一组画面整体在讲如何使用 MongoDB 和 Spring Boot 实现一个基于 WebSocket 的分布式消息系统。

2) 按时间顺序列出每张画面的要点：
画面1：课程介绍，展示目录结构，内容包括 MongoDB 入门、Java API 操作、Spring Boot 整合、搭建消息系统、分布式 WebSocket 解决方案分析。
画面2：创建 itcast-mongodb 工程，展示 pom.xml 中添加的 MongoDB 驱动依赖。
画面3：编写 Demo，展示 Java 代码连接 MongoDB、选择数据库和集合、执行查询。
画面4：Spring Boot 项目中导入依赖，展示 pom.xml 中添加 spring-boot-starter-data-mongodb 和 spring-boot-starter-test。
画面5：展示 MessageDAO 接口定义，包含 findByFromAndTo 方法。
画面6：创建 itcast-haoke-im 工程，展示 pom.xml 中的项目配置。
画面7：展示 MessageDAO 接口定义，包含 findByFromAndTo 方法。
画面8：展示 IM 系统架构图，用户A 发送消息到 IM 服务器，IM 服务器将消息存入 MongoDB。
画面9：展示 MessageController 类，包含 @RestController 和 @Autowired 注解。
画面10：展示 chat.js 代码，用于查询好友列表。
画面11：展示 chat.js 代码，用于处理用户信息和列表渲染。
画面12：展示 chat-window.js 代码，用于接收消息并更新列表。
画面13：展示 socket 服务端架构图，socket 客户端连接到 socket 服务端，服务端使用 Map 存储 session，支持订阅和发送消息。
画面14：展示分布式 Socket 解决方案分析，指出 Session 存储在全局 Map 中会导致系统瓶颈，解决方案是采用消息系统。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.mongodb</groupId>
    <artifactId>itcast-mongodb</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>org.mongodb</groupId>
            <artifactId>mongodb-driver-sync</artifactId>
            <version>3.9.1</version>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面4：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

画面6：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
    </parent>
    <groupId>cn.itcast.haoke.im</groupId>
    <artifactId>itcast-haoke-im</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

画面7：
```java
package cn.itcast.haoke.im.dao;
import cn.itcast.haoke.im.pojo.Message;
import com.mongodb.client.result.DeleteResult;
import com.mongodb.client.result.UpdateResult;
import org.bson.types.ObjectId;
import java.util.List;
public interface MessageDAO {
    /**
     * 查询点对点聊天记录
     * @param fromId
     * @param toId
     * @param page
     * @param rows
     * @return
     */
    List<Message> findByFromAndTo(Long fromId, Long toId, Integer page, Integer rows);
}
```

画面9：
```java
@RestController
@CrossOrigin
public class MessageController {
    @Autowired
    private MessageService messageService;
}
```

画面10：
```javascript
componentDidMount () => {
    axios.get('http://127.0.0.1:18081/user?fromId=1001').then((data) => {
        this.setState({
            list: data,
            isLoading: true
        })
    })
}
```

画面11：
```javascript
if(this.state.isLoading) {
    // let currentUser = parseInt(localStorage.getItem('uid'),10);
    let currentUser = parseInt(this.state.fromId,10);
    infoList = this.state.infos.map(item => {
        return (
```

画面12：
```javascript
componentDidMount () => {
    let {to_user, from_user} = this.props.chatInfo;
    axios.get('http://127.0.0.1:18081/message', {params: {
        toId: to_user,
        fromId: from_user
    }}).then((data) => {
        this.setState({
            infos: data,
            isLoading: true
        });
        client = handle(localStorage.getItem('uid'),(data) => {
            let newList = [...this.state.infos];
            newList.push(JSON.parse(data.content));
            this.setState({
                infos: newList
            });
        });
    });
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面8：架构图，用户A → IM 服务器 → MongoDB（消息存储）。
画面13：架构图，socket 客户端 → socket 服务端（Map(session)）→ 订阅 → 发送消息。
画面14：架构图，socket 客户端 → socket 服务端（Map(session)）→ 订阅 → 发送消息。

5) 无。
