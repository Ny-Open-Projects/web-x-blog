# 07.圈子功能实现之编写pojo代码

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\07.圈子功能实现之编写pojo代码_【海量资源尽在 666java.com】.mp4
- 时长 5分34秒（音频 334s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么接下来呢我们来编写一些基础的代码就是我们podo这个代码那么这个呢我们还是去写到啊就是我们去写到哪里呢写到我们这个double这个工程啊就是写到我们的一个double工程中这个要注意一下然后呢我们来看一下找到我们的这个项目啊在之前我们是不是有一个这个mite炭化double这个项目
[00:27] 然后呢下面有interface我们还是把它写到这个里面来因为呢我们去实现我们探花的时候呢还是要去编写这个double这样的一个服务的所以说呢我们要写到这个工程中来那么首先第一个呢就是我们的发布表publish这张表那么我们来看一下它的一些这个注解那么这三个注解就不用解释了对吧大家应该非常清楚然后呢这个呢是我们去指定
[00:53] 它与我们的mongodb中所映射的我们的表名是什么那么叫圈子publish然后去实现我们的一个序列化的一个接口那么因为我们在double去对象把对象需要做一个序列化要去实现它然后去给定一个序列化的一个ID那么下面这么一堆属性就和我们前面所讲的我们的表结构就一样了OK好那我们这个就
[01:21] 不一一去展开了然后我们就直接把它来做一个拷贝然后把它丢到哪里丢到这个下面来丢到这好嘞好那么我们第一个这个pozo就搞定了那么接下来我们来看一下第二个
[01:35] 那么第二个呢这个呢是我们的一个相册表它呢是用于存储我们的自己发布的数据的对吧那么这个呢和我们之前也是类似啊但是要注意的是呢在我们的相册表中呢它呢只保存的谁呢就是我们的public id也就是我们的发布id啊它并不会用于存储这发布的一些信息数据的这一点要注意一下好那我们来把它拷贝一下然后呢回到我们这个puzzle这个里面来这是这个相册表
[02:04] 然后呢下面这个呢是我们的时间线表啊那么在时间线表中呢我们要去保存它的一个这个UID和这个Public ID啊这两个呢我们要去做一个保存那么时间线表呢我们每一张用户呢都有一张这样的表所以说呢在这个位置呢我们设置这个名字其实呢我们是用不着的啊因为在后面呢我们会重新给它设置名字因为每个用户
[02:30] 会根据ID的不同那么我们去写不同这个表明我们会在后面的去跟一个下滑线一个Ulername去给它定义它的一个表明的OK好那么这个呢是我们的时间线表那么把这个时间线表呢我们同样呢也拷贝到什么呢拷贝到我们这个没有拷贝到来拷贝一下到这儿呢来拷贝一下这个时间线啊这张表那么我们去把它格式化一下
[03:01] 好嘞好那么再往下面走呢这个呢是评论表那么评论表呢是所有用户的评论呢都是放在这一表里面所以他就不会去做一个以用户去做一个分表了那么我们可以大致来看一下他的一些这个内容对吧还是呢去做序列化然后呢这个ID还有public ID然后呢还有评论的类型123这个别搞错了OK好那么这个呢其实就是这个评论表
[03:30] 然后呢我们就做一个这个拷贝那么接着我们继续往下面看那么下面这个呢是一个叫Uris表那么这个表呢是什么表呢我们来把它拷贝过来我们来看一下啊那么其实这张表呢是我们的好友表啊这个是我们的一个啊好友表那么目前呢我们还没有设计到好友这个业务那么在我们后面所要讲的我们这个
[03:52] 消息中的我们会涉及到这个好友所以说呢我们现在呢先暂时呢我们使用一个这个us这个表来代替我们这个好友就是后面这个好友啊因为到后面我们具体再讲啊那么呃在这个好友表中呢我们其实可以看一下他呢会呃哪些内容啊来看一下那么首先可以看到他的一个映射到我们的一个蒙狗中的一个用户是这个呃就是我们的一个数据库呢是这个探花啊us
[04:21] 然后呢下面会记录这么几个ID一个呢是UID就是用户的ID比如说我张三这个用户的ID为1那这个值呢他就是1那么Fred ID就是好友的ID你比如说张三有一个好友是李四那么李四的ID呢是5那么这个ID的值呢就是5这个大家理解了吧然后呢下面呢这个呢就是一个时间
[04:45] 打了我们这个时间的我们就进入这个Data吧然后到后面其实其实目前这个时间的我们用不着那么应该的我们把它设置为一个Lung那么这个到具体的结构的后面我们可能会做一个调整但是我们因为我们现在的在去写这个圈子的时候会设立到一点点的
[05:04] 这个好友的这个逻辑啊所以我们暂时呢先把这个结构呢先拿出来然后呢我们先拿一个最简单这样的一个结构啊先来使用啊先保证我们圈子的一个逻辑呢能够走通OK好那么这个是一个好友表那么到这里呢我们基础的一个这个Pozo呢是不是就已经都搞定了那么就是这么几个核心的表其实最核心的是四张表但是需要有一个好友表来做一个配合OK好那么关于这个Pozo的一个编写那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中定义用于 MongoDB 数据库的 POJO 实体类，包括 Publish、Album、Timeline、Comment 和 Users 等类，每个类都使用 Lombok 注解和 @Document 注解进行配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Publish 类的代码，包含 @Data、@NoArgsConstructor、@AllArgsConstructor 和 @Document 注解，以及 id、userId、medias、seeList、notSeeList、longitude、latitude、locationName、created 等字段。
画面2：展示 Publish 类的代码，光标在注释“// 发布表，对应评论”处，内容与画面1相同。
画面3：展示项目结构，突出 Publish.java 文件，同时显示了 Album.java 和 Timeline.java 文件的部分代码。
画面4：展示 Album 类的代码，包含 @Data、@NoArgsConstructor、@AllArgsConstructor 和 @Document 注解，以及 id、publishId、created 字段。
画面5：展示 Album 类的代码，光标在注释“// 相册表，用于存储自己发布的数据，每一个用户一张表进行存储”处，内容与画面4相同。
画面6：展示 Timeline 类的代码，包含 @Data、@NoArgsConstructor、@AllArgsConstructor 和 @Document 注解，以及 userId、publishedId、date 字段。
画面7：展示 Timeline 类的代码，光标在注释“// 时间线表，用于存储发布（或跟评）的数据，每一个用户一张表进行存储”处，内容与画面6相同。
画面8：展示 Album 类的代码，光标在注释“// 相册表，用于存储自己发布的数据，每一个用户一张表进行存储”处，内容与画面4相同。
画面9：展示 Timeline 类的代码，光标在注释“// 时间线表，用于存储发布（或跟评）的数据，每一个用户一张表进行存储”处，内容与画面6相同。
画面10：展示 Comment 类的代码，包含 @Data、@NoArgsConstructor、@AllArgsConstructor 和 @Document 注解，以及 id、publishId、commentType、content、userId、isParent、parentid、created 字段。
画面11：展示 Comment 类的代码，光标在注释“// 评论表”处，内容与画面10相同。
画面12：展示 Comment 类的代码，光标在注释“// 评论表”处，内容与画面10相同。
画面13：展示 Users 类的代码，包含 @Data、@NoArgsConstructor、@AllArgsConstructor 和 @Document 注解，以及 id、userId、friendId、date 字段。
画面14：展示 Album 类的代码，光标在注释“// 相册表，用于存储自己发布的数据，每一个用户一张表进行存储”处，内容与画面4相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;
/**
 * 发布表，对应评论
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "quanzi_publish")
public class Publish implements java.io.Serializable {
    private static final long serialVersionUID = -8732308321082804771L;
    private ObjectId id; //主键id
    private Long userId; //用户id
    private String text; //文字
    private List<String> medias; //媒体数据，图片或小视频 url
    private List<Long> seeList; //谁可以看：1-公开，2-私密，3-部分可见，4-不给谁看
    private List<Long> notSeeList; //不给谁看的列表
    private String longitude; //经度
    private String latitude; //纬度
    private String locationName; //位置名称
    private Date created; //发布时间
}
```

画面3：
```java
package com.tanhua.dubbo.server.pojo;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;
/**
 * 相册表，用于存储自己发布的数据，每一个用户一张表进行存储
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "quanzi_album")
public class Album implements java.io.Serializable {
    private static final long serialVersionUID = 4321830950922168171L;
    private ObjectId id; //主键id
    private ObjectId publishId; //发布id
    private Long created; //发布时间
}
```

画面4：
```java
package com.tanhua.dubbo.server.pojo;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;
/**
 * 相册表，用于存储自己发布的数据，每一个用户一张表进行存储
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "quanzi_album")
public class Album implements java.io.Serializable {
    private static final long serialVersionUID = 4321830950922168171L;
    private ObjectId id; //主键id
    private ObjectId publishId; //发布id
    private Long created; //发布时间
}
```

画面6：
```java
package com.tanhua.dubbo.server.pojo;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;
/**
 * 时间线表，用于存储发布（或跟评）的数据，每一个用户一张表进行存储
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "quanzi_time_line")
public class Timeline implements java.io.Serializable{
    private static final long serialVersionUID = 9096178416317502524L;
    private ObjectId userId; //好友id
    private ObjectId publishedId; //发布id
    private Long date; //发布的时间
}
```

画面10：
```java
package com.tanhua.dubbo.server.pojo;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;
/**
 * 评论表
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "quanzi_comment")
public class Comment implements java.io.Serializable{
    private static final long serialVersionUID = -291788258125767614L;
    private ObjectId id;
    private ObjectId publishId; //发布id
    private Integer commentType; //评论类型：1-点赞，2-评论，3-喜欢
    private String content; //评论内容
    private Long userId; //评论人
    private Boolean isParent = false; //是否为父节点，默认是否
    private ObjectId parentid; //父节点id
    private Long created; //发布时间
}
```

画面13：
```java
package com.tanhua.dubbo.server.pojo;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;
/**
 * 用户表
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "tanhua_users")
public class Users implements java.io.Serializable{
    private static final long serialVersionUID = 60031359460820874230L;
    private ObjectId id;
    private Long userId; //用户id
    private Long friendId; //好友id
    private Date date; //时间
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

