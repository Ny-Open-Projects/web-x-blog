# 画面线理解：07.圈子功能实现之编写pojo代码

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\07.圈子功能实现之编写pojo代码_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:38, 01:27, 01:34, 01:56, 02:05, 02:45, 02:52, 02:59, 03:15, 03:32, 03:40, 05:18, 05:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:37:21

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
