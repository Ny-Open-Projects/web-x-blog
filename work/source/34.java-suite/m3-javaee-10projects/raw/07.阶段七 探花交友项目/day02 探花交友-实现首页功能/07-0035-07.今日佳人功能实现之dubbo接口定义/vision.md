# 画面线理解：07.今日佳人功能实现之dubbo接口定义

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\07.今日佳人功能实现之dubbo接口定义_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:29, 00:57, 01:24, 01:48, 02:08, 02:38, 03:11, 03:43, 03:59, 05:08, 06:07, 06:41, 06:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:21:46

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Dubbo 和 MongoDB 实现推荐服务的接口定义与数据模型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示项目结构，聚焦于 pom.xml 文件，其中包含 MongoDB、commons-lang3、joda-time 和 netty-all 的依赖配置。
画面 2：在项目结构中选中 resources 目录，准备进行后续操作。
画面 3：打开并查看 RecommendUser.java 文件，显示其包名和类声明。
画面 4：展示 RecommendUser.java 文件内容，包含 @Id、@Indexed 等注解和字段定义。
画面 5：继续展示 RecommendUser.java 文件，聚焦于 @Id 注解和 id 字段。
画面 6：继续展示 RecommendUser.java 文件，聚焦于 score 字段。
画面 7：继续展示 RecommendUser.java 文件，聚焦于 date 字段。
画面 8：在 RecommendUser.java 文件中添加 Lombok 注解，如 @AllArgsConstructor、@NoArgsConstructor。
画面 9：在项目结构中右键点击 java 目录，弹出菜单选项。
画面 10：切换到 Typora 编辑器，显示 day02.md 文件中“2.3.1. 编写接口”部分，包含 RecommendUserApi 接口的定义。
画面 11：在 IntelliJ IDEA 中打开 RecommendUserApi.java 文件，显示接口方法 queryWithMaxScore 和 queryPageInfo。
画面 12：在 RecommendUserApi.java 文件中右键点击，弹出菜单选项。
画面 13：打开 PageInfo.java 文件，显示其类定义和字段。
画面 14：切换到 Typora 编辑器，显示 day02.md 文件中“2.3.2. 编写实现”部分，包含 application.properties 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```xml
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongodb-driver-sync</artifactId>
    <version>3.9.1</version>
</dependency>
<!--其他工具包依赖-->
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
</dependency>
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.9.9</version>
</dependency>
<dependency>
    <groupId>io.netty</groupId>
    <artifactId>netty-all</artifactId>
    <version>4.1.32.Final</version>
</dependency>
```

画面 4：
```java
package com.tanhua.dubbo.server.pojo;
import org.springframework.data.annotation.Id;
public class RecommendUser implements java.io.Serializable {
    private static final long serialVersionUID = 5874126832504390567L;
    @Id
    private ObjectId id; //主键id
    @Indexed
    private Long userId; //推荐的用户id
    @Indexed
    private Long toUserId; //用户id
    private Double score; //推荐得分
    private String date; //日期
}
```

画面 10：
```java
package com.tanhua.dubbo.server.api;
import com.tanhua.dubbo.server.vo.PageInfo;
import com.tanhua.dubbo.server.pojo.RecommendUser;
public interface RecommendUserApi {
    /**
     * 查询一位积分最高的推荐用户
     * @param userId
     * @return
     */
    RecommendUser queryWithMaxScore(Long userId);
    /**
     * 按照时间倒序
     * @param userId
     * @param pageNum
     * @param pageSize
     * @return
     */
    List<RecommendUser> queryPageInfo(Long userId, Integer pageNum, Integer pageSize);
}
```

画面 13：
```java
public class PageInfo<T> implements java.io.Serializable {
    private static final long serialVersionUID = -2105385689859184204L;
    /**
     * 总条数
     */
    private Integer total;
    /**
     * 当前页
     */
    private Integer pageNum;
    /**
     * 一页显示的大小
     */
    private Integer pageSize;
    /**
     * 数据列表
     */
    private List<T> records = Collections.emptyList();
}
```

画面 14：
```properties
# Spring boot application
spring.application.name = itcast-tanhu-dubbo-service
dubbo.scan.basePackages = com.tanhua.dubbo.server
dubbo.application.name = dubbo-provider-tanhu
dubbo.protocol.name = dubbo
dubbo.protocol.port = 20880
dubbo.registry.address = zookeeper://192.168.31.81:2181
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 10：PPT 标题为“2.3.1. 编写接口”，内容包含接口定义。
画面 14：PPT 标题为“2.3.2. 编写实现”，内容包含 application.properties 配置。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
