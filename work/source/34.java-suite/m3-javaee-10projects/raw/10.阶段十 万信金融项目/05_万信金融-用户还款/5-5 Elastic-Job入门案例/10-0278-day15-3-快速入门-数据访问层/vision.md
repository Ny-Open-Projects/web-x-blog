# 画面线理解：day15-3-快速入门-数据访问层

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-5 Elastic-Job入门案例
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-5 Elastic-Job入门案例\day15-3-快速入门-数据访问层_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:39, 01:00, 02:01, 02:47, 03:06, 03:23, 06:33, 07:20, 08:00, 13:03, 13:52, 15:24, 15:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:30:46

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Elastic-Job 框架在 Spring Boot 项目中实现分库分表的定时任务，包括项目初始化、依赖配置、数据源配置、实体类定义和分片查询接口的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，目录包含 src/main/java、src/main/resources、src/test 等标准 Maven 结构，以及 application.properties 配置文件。
画面2：展示 pom.xml 文件中添加 Spring Boot Web 依赖。
画面3：展示 pom.xml 文件中添加 MySQL 数据库驱动依赖和 Lombok 依赖。
画面4：展示 application.properties 文件中配置 Spring Boot 的 server.port、数据源连接信息、MyBatis 的 mapper 文件路径和类型别名包。
画面5：展示 User.java 实体类，包含 ID、用户名、密码、姓名、年龄等字段，并使用 @TableId 和 @TableField 注解。
画面6：展示 User.java 实体类中 @TableId 注解的 ID 字段。
画面7：展示 application.properties 文件中配置 ZooKeeper 服务地址、作业命名空间、分片总数和 cron 表达式。
画面8：展示 UserMapper 接口定义，包含注释说明分片查询逻辑。
画面9：展示 UserMapper.java 文件的初始状态，准备编写分片查询方法。
画面10：展示 UserMapper.java 文件中定义分片查询方法的返回类型和参数。
画面11：展示 pom.xml 文件中添加 Elastic-Job 依赖。
画面12：展示 UserMapper.java 文件中导入必要的包。
画面13：展示 UserMapper.java 文件中编写分片查询方法的 SQL 语句。
画面14：展示 UserMapper.java 文件中完成分片查询方法的定义，继承 BaseMapper 并使用 @Select 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
elastic-job-springboot CA\Users\ap
├── .idea
├── src
│   └── main
│       ├── java
│       │   └── com.ithema.elasticjob
│       │       ├── config
│       │       ├── dao
│       │       ├── job
│       │       └── pojo
│       └── resources
│           └── application.properties
└── target
```

画面2：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

画面3：
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.47</version>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
```

画面4：
```properties
server.port=8081
spring.application.name=elastic-job-springboot
logging.level.root=info

spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true&failOverReadOnly=false&allowMultiQueries=true
spring.datasource.username=root
spring.datasource.password=123

# 设置Mapper接口所对应的XML文件位置
mybatis-plus.mapper-locations = classpath*:mapper/*.xml
# 设置别名扫描路径
mybatis-plus.type-aliases-package = com.ithema.elasticjob.pojo
```

画面5：
```java
@TableId("ID")
private Long id;
@TableField("USER_NAME")
private String userName;
@TableField("PASSWORD")
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
```

画面7：
```properties
# zookeeper服务地址
zookeeper.connectstring = localhost:2181
# 作业命名空间
myjob.namespace = elastic-job-example
# 分片总数
myjob.count = 3
# cron表达式(定时策略)
myjob.cron = 0/5 * * * * ?
```

画面8：
```java
public interface UserMapper extends BaseMapper<User> {
    // 通过mod取余进行分片
    @Select("SELECT * FROM `tb_user` WHERE mod(#shardingTotalCount)#= #{shardingItem}")
    List<User> queryUserById(@Param("shardingTotalCount") int count,
                             @Param("shardingItem") int item);
}
```

画面10：
```java
List<User> queryUserById(int shardingTotalCount, int shardingItem);
```

画面11：
```xml
<dependency>
    <groupId>com.dangdang</groupId>
    <artifactId>elastic-job-lite-spring</artifactId>
    <version>2.1.5</version>
</dependency>
```

画面12：
```java
import com.ithema.elasticjob.User;
import java.util.List;
```

画面13：
```java
@Select("select * from tb_user where MOD(id,#{shardingTotalCount})=#{shardingItem}")
List<User> queryUserById(@Param("shardingTotalCount") int shardingTotalCount,
                         @Param("shardingItem") int shardingItem);
```

画面14：
```java
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.ithema.elasticjob.User;
import org.apache.ibatis.annotations.Select;
import java.util.List;

public interface UserMapper extends BaseMapper<User> {
    @Select("select * from tb_user where MOD(id,#{shardingTotalCount})=#{shardingItem}")
    List<User> queryUserById(@Param("shardingTotalCount") int shardingTotalCount,
                             @Param("shardingItem") int shardingItem);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：PPT标题为“5. 数据访问层”，下方展示 UserMapper 接口定义代码。
画面7：PPT标题为“2.2 入门案例”，下方展示 application.properties 配置文件内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
