# 画面线理解：21.地图找房功能实现之整合MongoDB进行开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\21.地图找房功能实现之整合MongoDB进行开发【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:45, 01:40, 02:41, 03:48, 05:13, 06:31, 07:20, 07:52, 08:39, 09:26, 10:00, 10:40, 11:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:23:45

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现基于 MongoDB 的房屋数据查询功能，包括定义实体类、编写服务层代码、配置数据源以及前端页面展示。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 PDF 文档“5.6.1 导入依赖”，内容为“5.6.6.3 编写pojo”，并列出目录结构，当前页码为 34。
画面2: 显示 IntelliJ IDEA 中的 `application.properties` 文件，内容为 Dubbo 注册中心和 Redis 集群配置。
画面3: 显示 PDF 文档“5.6.3 编写pojo”，内容为 `MongoHouse` 实体类的 Java 代码，包含 `@Data`、`@AllArgsConstructor`、`@NoArgsConstructor`、`@JsonSerialize` 等注解。
画面4: 显示 IntelliJ IDEA 中创建 `MongoHouseService` 类的弹窗。
画面5: 显示 PDF 文档“5.6.3 编写pojo”，内容为 `MongoHouseService` 类的 Java 代码，包含 `@Service` 注解和 `@Autowired` 注解。
画面6: 显示 PDF 文档“5.6.3 编写pojo”，内容为 `MongoHouseService` 类的 Java 代码，包含 `@Autowired` 注解和 `queryHouseData` 方法的定义。
画面7: 显示 IntelliJ IDEA 中 `MongoHouseService` 类的 Java 代码，内容为 `queryHouseData` 方法的实现，包含 `Query` 查询条件和 `List<MapHouseXY>` 的构造。
画面8: 显示 IntelliJ IDEA 中 `MongoHouseService` 类的 Java 代码，内容为 `queryHouseData` 方法的实现，包含 `List<MapHouseXY>` 的构造。
画面9: 显示 IntelliJ IDEA 中 `MapHouseDataFetcher` 类的 Java 代码，内容为 `dataFetcher` 方法的实现，包含 `System.out.println` 输出调试信息。
画面10: 显示 PDF 文档“5.6.3 编写pojo”，内容为前端 JavaScript 代码，包含 `render` 函数和 `div` 标签。
画面11: 显示浏览器中前端页面，内容为“地图找房”页面，包含“2层”、“3层”等按钮和一个红色标记点。
画面12: 显示浏览器中前端页面，内容为“地图找房”页面，显示了地图和多个房屋标记点。
画面13: 显示 PDF 文档“5.6.1 导入依赖”，内容为 MongoDB 查询示例，包含 `db.house.find` 的查询语句和返回结果。
画面14: 显示浏览器中前端页面，内容为“地图找房”页面，显示了地图和多个房屋标记点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```
dubbo.registry.address = zookeeper://172.16.55.185:2181
dubbo.registry.client = zkclient
# redis集群配置
spring.redis.jedis.pool.max-wait = 5000
spring.redis.jedis.pool.maxIdle = 100
spring.redis.jedis.pool.minIdle = 10
spring.redis.timeout = 10
spring.redis.cluster.nodes = 172.16.55.185:6379,172.16.55.185:6380
spring.redis.cluster.max-redirects=5
```

画面3:
```
package cn.itcast.haoke.dubbo.api.pojo;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "house") // 指定表的名称
public class MongoHouse {
    @Id
    @JsonSerialize(using = ToStringSerializer.class)
    private ObjectId id;
    private String title;
    private String desc;
    private String price;
    private String area;
    private String houseType;
    private String houseDirection;
    private String houseStatus;
    private String houseImg;
    private String houseUrl;
    private String houseLocation;
    private String houseAddress;
    private String housePhone;
    private String houseEmail;
    private String houseWebsite;
    private String houseDescription;
    private String houseTags;
    private String houseKeywords;
    private String houseNote;
    private String houseRemark;
    private String houseRemark2;
    private String houseRemark3;
    private String houseRemark4;
    private String houseRemark5;
    private String houseRemark6;
    private String houseRemark7;
    private String houseRemark8;
    private String houseRemark9;
    private String houseRemark10;
    private String houseRemark11;
    private String houseRemark12;
    private String houseRemark13;
    private String houseRemark14;
    private String houseRemark15;
    private String houseRemark16;
    private String houseRemark17;
    private String houseRemark18;
    private String houseRemark19;
    private String houseRemark20;
    private String houseRemark21;
    private String houseRemark22;
    private String houseRemark23;
    private String houseRemark24;
    private String houseRemark25;
    private String houseRemark26;
    private String houseRemark27;
    private String houseRemark28;
    private String houseRemark29;
    private String houseRemark30;
    private String houseRemark31;
    private String houseRemark32;
    private String houseRemark33;
    private String houseRemark34;
    private String houseRemark35;
    private String houseRemark36;
    private String houseRemark37;
    private String houseRemark38;
    private String houseRemark39;
    private String houseRemark40;
    private String houseRemark41;
    private String houseRemark42;
    private String houseRemark43;
    private String houseRemark44;
    private String houseRemark45;
    private String houseRemark46;
    private String houseRemark47;
    private String houseRemark48;
    private String houseRemark49;
    private String houseRemark50;
    private String houseRemark51;
    private String houseRemark52;
    private String houseRemark53;
    private String houseRemark54;
    private String houseRemark55;
    private String houseRemark56;
    private String houseRemark57;
    private String houseRemark58;
    private String houseRemark59;
    private String houseRemark60;
    private String houseRemark61;
    private String houseRemark62;
    private String houseRemark63;
    private String houseRemark64;
    private String houseRemark65;
    private String houseRemark66;
    private String houseRemark67;
    private String houseRemark68;
    private String houseRemark69;
    private String houseRemark70;
    private String houseRemark71;
    private String houseRemark72;
    private String houseRemark73;
    private String houseRemark74;
    private String houseRemark75;
    private String houseRemark76;
    private String houseRemark77;
    private String houseRemark78;
    private String houseRemark79;
    private String houseRemark80;
    private String houseRemark81;
    private String houseRemark82;
    private String houseRemark83;
    private String houseRemark84;
    private String houseRemark85;
    private String houseRemark86;
    private String houseRemark87;
    private String houseRemark88;
    private String houseRemark89;
    private String houseRemark90;
    private String houseRemark91;
    private String houseRemark92;
    private String houseRemark93;
    private String houseRemark94;
    private String houseRemark95;
    private String houseRemark96;
    private String houseRemark97;
    private String houseRemark98;
    private String houseRemark99;
    private String houseRemark100;
```

画面6:
```
static {
    BAI_DU_ZOOM.put(19, 20d / 1000);
    BAI_DU_ZOOM.put(18, 50d / 1000);
    BAI_DU_ZOOM.put(17, 100d / 1000);
    BAI_DU_ZOOM.put(16, 200d / 1000);
    BAI_DU_ZOOM.put(15, 400d / 1000);
    BAI_DU_ZOOM.put(14, 800d / 1000);
    BAI_DU_ZOOM.put(13, 1600d / 1000);
    BAI_DU_ZOOM.put(12, 3200d / 1000);
    BAI_DU_ZOOM.put(11, 6400d / 1000);
    BAI_DU_ZOOM.put(10, 128
