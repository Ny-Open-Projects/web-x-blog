# 22.实现微聊系统之定义MessageDAO接口

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day08-MongoDB入门以及实现微聊即时通讯功能
- 源文件：03.阶段三 好客租房(生活服务)项目\day08-MongoDB入门以及实现微聊即时通讯功能\22.实现微聊系统之定义MessageDAO接口【海量资源尽在 ubkz.com】.mp4
- 时长 3分40秒（音频 220s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们来定义我们的DAO的接口啊那么我们把它称之为叫做Message DAO那么我们来写一下这个接口那么首先呢我们需要创建一个包就是DAO这个包那么我们需要在这个下面去创包当然了是和这个Pojo是平挤的这样一个包啊所以呢我们可以点击这个位置在这点击New一个Project来一个什么呢来一个叫做DAO对吧
[00:28] 然后呢我们有了这个DAO这个包之后啊那么下面我们就可以去编写一个接口那么这个接口的名字就叫messagemessage DAO然后呢它呢是一个接口在接口中呢我们将定义一系列的一些方法那么我们来参考讲义啊我们来看一下大概要定义哪些方法那么首先呢是咱们来拷贝一下吧拷贝到这那么我们可以看到
[00:57] 它呢是有这么几个方法啊那么把这个相关的一些包呢我们导入进来match的对象ok这个是object id对象好嘞然后呢下面呢还有一个呢是叫做sale啊就是我们的去新增我们的消息然后呢去加一个叫新增消息好然后呢最后一个呢是根据消息id呢去做一个删除那么我们来看一下它几个方法啊这几个方法
[01:27] OK那么首先第一个呢是查询点对点的消息聊天的记录那么这个是什么意思呢就是我我又比如说啊现在我有两个用户啊这个呢是我这个A这个用户对吧这个是我B这个用户对吧那么我A和B之间的一个双向的一个这个聊天记录那么我需要通过这个方法呢把它去查询出来OK所以呢我们可以看到在在在这个位置呢它传入了
[01:56] form id和to id那么form就是从谁发过来的对吧to呢就是发给谁的哎OK那么反过来呢那就是把这两个位置回颠倒一下那么他的这个然后并且呢会做一个分页啊配置和这个ros那么大家去玩这个微信的时候应该也会这样的体验那么比如说再多的信息消息的话我们就需要往上面再拉去看的历史消息那么他会有一个分页啊这样的一个效果那么这是这个方法那么下面这个方法呢是
[02:26] 我们通过这个ID就是消息的这个ID去查找这个消息的数据OK好这是第二个第三个呢是我们去更新消息的一个状态因为前面呢我们说过消息状态呢有两个一个是已读一个是未读那就是已发送啊一个是未读那么在这个意思就是已发送已发送它其实就是属于未读状态对吧那么当你已读的时候呢就变成已读这个状态了
[02:54] OK那么所以呢有些时候呢我们比如说这个消息本身是未读的那么我们现在已经把它读过这个消息了那我们就需要去修改一下它的消息的一个状态啊所以这个方法它也是有用的啊有必要的存在的啊然后呢下面呢是新增消息这个就不用说了肯定得有对吧我们需要把新的消息保存到我们的芒果DB里面去那么下面这个呢是根据消息的ID去删除我们的消息数据这个呢可能我们暂时在业务中的暂时用不着
[03:23] 但是呢我们为了我们的DU的一个完整性CRU定了我们来保证它都有啊所以呢我们就把这个方法也加上来了OK这个呢就是我们的一个接口那么接下来呢我们就要去实现啊我们的这个接口好那么关于这个接口这个定义呢我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

