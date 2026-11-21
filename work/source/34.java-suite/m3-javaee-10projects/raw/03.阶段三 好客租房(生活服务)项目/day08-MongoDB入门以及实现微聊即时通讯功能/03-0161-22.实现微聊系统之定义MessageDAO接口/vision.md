# 画面线理解：22.实现微聊系统之定义MessageDAO接口

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\22.实现微聊系统之定义MessageDAO接口【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:23, 00:43, 00:48, 00:54, 01:01, 01:07, 01:19, 01:28, 02:25, 02:45, 03:06, 03:20, 03:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:47:35

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中定义用户数据静态映射、创建消息数据访问对象（DAO）接口并定义其方法，用于后续的 MongoDB 操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 UserData.java 文件，其中定义了静态 Map<Long, User> USER_MAP，并初始化了5个用户数据（ID 1001 至 1005）。
画面2：与画面1基本相同，仅光标位置不同。
画面3：在 IntelliJ IDEA 中创建 MessageDAO.java 文件，弹出“Create New Class”对话框。
画面4：展示 PDF 讲义第48页，内容为 MessageDAO 接口的注释说明，包括方法 findListByFromAndTo 的参数和返回值。
画面5：展示 MessageDAO.java 文件，内容为空。
画面6：在 MessageDAO.java 文件中，光标位于方法 findListByFromAndTo 的定义处。
画面7：展示 MessageDAO.java 文件，光标位于方法 updateMessageState 的定义处。
画面8：展示 PDF 讲义第41页，内容为 MessageDAO 接口的注释说明，包括方法 saveMessage 和 deleteMessage。
画面9：展示 MessageDAO.java 文件，光标位于方法 findMessageById 的定义处。
画面10：展示 MessageDAO.java 文件，光标位于方法 findListByFromAndTo 的定义处。
画面11：展示 Message.java 文件，定义了消息实体类，包含 id、msg、status、send_date、read_date、from、to 等字段，并标注了 @Indexed 注解。
画面12：展示 MessageDAO.java 文件，光标位于方法 saveMessage 的定义处。
画面13：展示 MessageDAO.java 文件，光标位于方法 deleteMessage 的定义处。
画面14：展示 MessageDAO.java 文件，光标位于方法 findListByFromAndTo 的定义处。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package cn.itcast.haoke.im.pojo;
import java.util.HashMap;
import java.util.Map;

public class UserData {
    public static final Map<Long,User> USER_MAP = new HashMap<>();

    static {
        USER_MAP.put(1001L, User.builder().id(1001L).username("zhangsan").build());
        USER_MAP.put(1002L, User.builder().id(1002L).username("lisi").build());
        USER_MAP.put(1003L, User.builder().id(1003L).username("wangwu").build());
        USER_MAP.put(1004L, User.builder().id(1004L).username("zhaoliu").build());
        USER_MAP.put(1005L, User.builder().id(1005L).username("zunqi").build());
    }
}
```

画面3：
```java
package cn.itcast.haoke.im.dao;

public interface MessageDAO {
```

画面4：
```java
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
    List<Message> findListByFromAndTo(Long fromId, Long toId, Integer page, Integer rows);

```

画面6：
```java
List<Message> findListByFromAndTo(Long fromId, Long toId, Integer page, Integer rows);
```

画面7：
```java
UpdateResult updateMessageState(ObjectId id, Integer status);
```

画面8：
```java
Message saveMessage(Message message);

/**
 * 根据消息id删除数据
 * @param id
 * @return
 */
DeleteResult deleteMessage(String id);
```

画面9：
```java
Message findMessageById(String id);
```

画面10：
```java
List<Message> findListByFromAndTo(Long fromId, Long toId, Integer page, Integer rows);
```

画面11：
```java
public class Message {
    @Id
    private ObjectId id;
    private String msg;
    /*
     * 消息状态，1-未读，2-已读
     */
    private Integer status;
    @Indexed
    @Field("send_date")
    private Date sendDate;
    @Indexed
    @Field("read_date")
    private Date readDate;
    @Indexed
    private User from;
    @Indexed
    private User to;
}
```

画面12：
```java
Message saveMessage(Message message);
```

画面13：
```java
DeleteResult deleteMessage(String id);
```

画面14：
```java
List<Message> findListByFromAndTo(Long fromId, Long toId, Integer page, Integer rows);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：PDF 讲义第48页标题为“4.1. 创建工程 itcast-haoke-im”，内容为 MessageDAO 接口方法的注释说明。
画面8：PDF 讲义第41页标题为“新增消息数据”，内容为 MessageDAO 接口方法的注释说明。
画面11：PDF 讲义第41页标题为“新增消息数据”，内容为 MessageDAO 接口方法的注释说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
