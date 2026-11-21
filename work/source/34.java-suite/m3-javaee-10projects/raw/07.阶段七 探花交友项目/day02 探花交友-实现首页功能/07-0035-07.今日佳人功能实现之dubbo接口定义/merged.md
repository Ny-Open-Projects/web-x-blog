# 07.今日佳人功能实现之dubbo接口定义

- 阶段：07.阶段七 探花交友项目
- 章节：day02 探花交友-实现首页功能
- 源文件：07.阶段七 探花交友项目\day02 探花交友-实现首页功能\07.今日佳人功能实现之dubbo接口定义_【海量资源尽在 666java.com】.mp4
- 时长 7分2秒（音频 423s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来编写这个double服务那么首先呢我们是需要去写一个pozo类对吧就是跟我们之前所定义的这个结构啊就是我们的表结构呢要一次的这样的一个pozo类那么我们来创建一个下面这个pozo这个类吧就叫recommend user啊这样的一个类那么我们把这个包名呢我们来拷贝一下然后呢在这个位置来创建一个
[00:29] 这个包然后呢下面呢我们将去在这个在这个Pojo这个包下面呢我们来创建一个这个叫CommandUser这样的一个类啊那我们来看一下那么写一个这样的一个类啊那么首先我们需要注意的是呢这个类呢将用于我们的Double
[00:51] 的这个服务之间的一个传输对不对所以呢他一定需要去实现一个什么呢序列化的一个接口那这个首先呢这个别忘记啊然后呢我们要去给他去生成一个什么呢可序列化的这样的一个ID然后呢我们下面是不是写一些这个字段那么这个字段呢要跟我们之前所定义的一个结构一致呢那我们就把这个呢就拷贝过来来看一下那么在这个位置呢我们是
[01:20] 把这个呢是注射掉了这样我们先打开啊先打开好那我们把相关的一些包呢导入进来那么把这个包呢导入进来然后呢把它呢index的那么也导入进来然后呢我们就使用哎我们来看一下啊它使用的是什么呢使用的是我们这个mongodb啊spring下面mongodb这个这个别导错了那么就应该哎它呢我看一下啊那么重新来导入一下
[01:51] 那么导的是这个啊这个OK把它导入进来这样的话就OK了那么这个是不是跟我们的之前的表结构的定义呢要保持一致啊这样的一个结构那么UID和toUID啊UID toUID还还score还有个data而上面这个这个ID呢是我们的一个组件啊它的一个object ID一个组件那么在讲义中呢我们把这个组件呢其实注释掉了啊
[02:20] 那么为什么要注释掉呢原因是呢那我们在后面呢会遇到一个问题啊需要把它注释掉啊当然了我们现在呢暂时呢我们就先把它先打开先打开然后后面我们遇到问题了我们再说啊然后呢我们需要呢给我们的这个类呢添加我们的这个data这个注解对吧然后呢再加一个什么呢没有参数的和什么呢全参数的啊这样的一个
[02:48] 这样的一个这个注解了那么这是这三个这个注解那么其实我们还需要一个注解是我们需要去指定它的一个所映射的一个表那我们要通过什么呢通过这个document这样的一个注解来指定它的一个表明是什么呢recommendUra这样的一个表那么我们就把它呢就拷贝过来吧那么就拷到下面这个位置来OK那么这样的话呢我们是不是就完成了这个对象
[03:17] 和我们这个表的这样的一个映射了对吧哎OK好那么呃这样的话呢我们这个Pozole呢就搞定了那么接下来呢我们将啊使用这个Pozole呢来定义我们的一些这个接口那么下面我们来看一下这个接口的一个定义啊那么我们要定义一个RecommendUser这样的一个API那我们先把这个API这个包呢我们先创建出来然后呢在这哎在这
[03:43] 创建一个这个包创建一个这个包然后API这个包呢我们就这样我们先写这个定一个这个接口吧然后我们一点一点来看啊然后呢有一个interface这样的一个这个接口那么首先呢我们需要定义的一个方法就是去查询什么呢最大的得分的啊这样的一个推荐用户那么它的一个参数呢就是这个user这个ID
[04:10] 然后它的一个返回值呢就是recommendure这样的一个对象哎呀OK然后呢我们把这个呢就来拷贝过来这是我们要去根据这个用户啊去做查询给他所推荐的啊最高的这样的一个用户了比如说张三呢有很多的用户去推荐给张三啊然后呢我们当然要查询这个什么今日佳人那么就要查询这个
[04:34] 缘分之最高的这个用户啊那所以说就需要定义这样的一个方法了那么下面呢我们就需要去查询一个什么呢查询我们的一个这个列表啊查询一个列表那么我们通过一个query page info然后查询一个page info这个对象呢也是需要我们自己去定义一下啊然后呢我们把这个呢先拷贝过来OK好那么
[05:03] 我们来看一下这个方法啊那么配置info呢现在我们还没有那么一会儿我们来定一下这个配置info那么这个方法的这个参数呢我们可以看到有三个参数一个呢是user id啊一个呢就是我们的一个配置number还有一个什么呢就是配置size那么就是因为显然呢是这是要做一个什么分页查询因为我们给一个用户呢去推荐这个用户的话那么
[05:27] 它肯定不只是一个对吧会有很多所以必然会涉及到一个什么分页这样的一个功能所以说在这个位置要有分页这两个参数然后我们可以看到这个方法上面的定义是需要按照一个时间排序这可能会有点问题那我们就按照什么我们就按照我们的一个得分得分排序倒序做一个排序那我们把这个讲义也改一下这块是稍微有点问题的
[05:57] 那我按照这个得分去做一个排序了OK好那么接下来呢我们把这个PageInfo呢我们也创建出来然后呢我们需要在这个包下面呢我们来创建一个包叫做什么呢VO这个包那么注意这个VO和Pojo呢是不一样的VO是我们并不是实体的这个并啊是一些普通的一些加密并对象那我们把这个呢也拷贝过来那么我们就丢到这吧那么我们来看一下这个PageInfo啊这个是
[06:25] 相对比较简单的这样的一个配置info了那么来看一下那么里面有一些总条数以及我们的配置number还有配置size还有什么records就是我们的一些数据的一个列表它末日是一个空的这样的一个集合ok好那么我们来回过头来看一下我们 API那么它导入包之后这不就ok了
[06:49] 对吧好那么到目前为止是不是我们就已经完成了一个这个接口这样的一个定义对不对OK好那么关于我们这个接口这个定义呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
spring.application.name = itcast-tanhu-dubbo-Service
dubbo.scan.basePackages = com.tanhua.dubbo.server
dubbo.application.name = dubbo-provider-tanhu
dubbo.protocol.name = dubbo
dubbo.protocol.port = 20880
dubbo.registry.address = ZooKeeper://192.168.31.81:2181
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 10：PPT 标题为“2.3.1. 编写接口”，内容包含接口定义。
画面 14：PPT 标题为“2.3.2. 编写实现”，内容包含 application.properties 配置。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

