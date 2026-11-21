# 32.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\32.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 3分45秒（音频 226s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对我们今天的内容呢做一个简单的一个总结啊今天呢我们讲了这么几个内容那么我们首先讲的是猫狗DB的一个入门那么我们也是用了比较长的一个时间去讲这个部分的内容啊也希望大家呢通过这样的一个讲解呢去了解一个猫狗DB然后呢对他的使用的有个基本的一些这个认知和一些入门
[00:24] 那么也希望大家在做项目的时候也可以把 MongoDB作为你的一个技术选型的一个选择OK好那么在我们做了一些基本的入门之后我们学了它的一些Java API的一些操作然后也希望大家动手去写一写这样一些代码那么就有助于我们对MongoDB的一些生物的了解那么后面我们又去学习了SpringDataMongoDB的这样一个项目对MongoDB的一个支持那么
[00:53] 它这样的一个作用呢其实就是简化MangoDB的一些API的操作那么其实我们在用完之后呢也会发现它的确做到了一个简化这样的一个目的那么也希望大家还是那句话去敲一下这个代码那么只有你动手去敲那么才能够去体会到它的一些这个比较爽的一些地方是吧
[01:12] OK好那么在我们去学完芒果DB之后呢我们去搭建了我们的一个微聊这个系统然后在微聊这个系统呢我们去实现了我们的一个Message DAO那么这个呢也是基于芒果DB去做一个实现希望大家动手聚焦然后呢后面我们又去编写了一些WebSocket我们相关的一些逻辑什么的发送消息啊接收消息啊等等一些逻辑那么在我们写完之后呢我们去又提供了两个服务一个是查询历史消息
[01:39] 一个查询的用户的列表那么当我们去把我们这个服务全部都已经提供好之后我们去整合了我们的前台那么整合那前台我们在这个里面会涉及到一些JS的一些修改那么我其实不太希望大家自己去跟我一样去做这样的一些修改而是什么呢你可以拿到我提供给你们的代码去做一些参考
[02:04] 因为我们毕竟是属于后端的工程师那么我们不要过多的去把一些精力分散到我们的前端上面去那么只要我们能够大致能够读懂前端的一些代码能够去做一些简单的修改能够完成我们的功能就可以了OK好那么大家如果你的前端是学的非常好的功底也非常的强能够去做出很多的一些这种效果
[02:28] 当然我是很开心的也是愿意让大家这样去做的OK但是呢其实考虑到我们更多的是后端的工程师那么可能在前端这块相对会弱一些那么大家呢也可以参考我提供的代码去完成这样的功能就可以了好那么我们的审核全台之后呢是不是实现了一些这个查询好友的列表包括这个好友的单聊的功能以及这个发送消息和接收消息啊等等一些这样的一些功能
[02:58] 然后最后呢我们去提供了一个这个分布式的一个socket的一个解决方案那么这个呢也是做了这样的一个分析简单的分析吧等到我们后面去做具体实现的时候呢我们再回过头来我们再来一次分析然后呢帮助大家去理解这个问题它究竟是个什么样的问题那么为什么这样去解决那么我们解决具体又该怎么去做等等我们再去做具体的一个实现那么OK好那么
[03:25] 这个呢以上呢就是我们今天的一些主要的大概的一些内容吧那么具体详细内容呢我们就不重复了那么也希望大家呢能够去认真仔细的去学习中的其中一些内容啊那么有问题呢也可以一起跟我去做一些交流OK好那么我们这个今天的一个小节呢我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

