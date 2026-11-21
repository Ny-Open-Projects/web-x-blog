# 画面线理解：07.Elasticsearch实现位置查询之编码实现（更新用户地理位置）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\07.Elasticsearch实现位置查询之编码实现（更新用户地理位置）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 03:05, 04:07, 05:08, 07:21, 09:08, 11:05, 12:08, 13:25, 14:39, 15:37, 16:45, 18:28, 19:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:26:12

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Elasticsearch 实现用户地理位置信息的增删改查功能，包括实体类定义、控制器接口、服务层逻辑及索引/映射的动态创建。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构和 UserLocationES 实体类的定义，包含 @Document 注解指定索引名、类型和分片副本数。
画面2：展示 UserLocationES 实体类的完整代码，包含 @Id、@GeoPointField、@Field 等注解定义字段。
画面3：展示 UserLocationController 中的 updateUserLocation 方法，接收参数并调用服务层。
画面4：展示 UserLocationController 中的 updateUserLocation 方法，参数解析和异常处理。
画面5：展示 UserLocationService 中的 updateLocation 方法，开始编写逻辑。
画面6：展示 UserLocationService 中的代码，判断索引是否存在并创建。
画面7：展示 UserLocationService 中的代码，判断类型是否存在并创建映射。
画面8：展示 UserLocationService 中的代码，使用 GetQuery 查询用户位置数据。
画面9：展示 UserLocationService 中的代码，创建新 UserLocationES 对象并设置属性。
画面10：展示 UserLocationService 中的代码，构建 IndexQuery 并执行索引操作。
画面11：展示 UserLocationService 中的代码，构建 UpdateRequest 并执行更新操作。
画面12：展示 UserLocationService 中的代码，使用 UpdateRequest 更新数据。
画面13：展示 UserLocationService 中的代码，使用 IndexQuery 索引数据。
画面14：展示 UserLocationService 中的代码，使用 UpdateRequest 更新数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.tanhua.es.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.elasticsearch.common.geo.GeoPoint;
import org.springframework.data.elasticsearch.annotations.Document;
import org.springframework.data.elasticsearch.annotations.Field;
import org.springframework.data.elasticsearch.annotations.FieldType;
@Data
@Document(indexName = "tanhua", type = "user_location", shards = 6, replicas = 2)
public class UserLocationES {
```

画面2：
```java
@Document(indexName = "tanhua", type = "user_location", shards = 6, replicas = 2)
public class UserLocationES {
    @Id
    private Long userId; //用Pid
    @GeoPointField
    private GeoPoint location; //x:经度 y:纬度
    @Field
    private String address; //位置描述
    @Field(type = FieldType.Long)
    private Long created; //创建时间
    @Field(type = FieldType.Long)
    private Long updated; //更新时间
    @Field(type = FieldType.Long)
    private Long lastUpdated; //上次更新时间
}
```

画面3：
```java
@PostMapping
public ResponseEntity<UserLocationES> updateUserLocation(@RequestBody Map<String, Object> param) {
    try {
        Long userId = Long.valueOf(param.get("userId").toString());
        Double longitude = Double.valueOf(param.get("longitude").toString());
        Double latitude = Double.valueOf(param.get("latitude").toString());
        String address = param.get("address").toString();
        boolean result = this.userLocationService.updateUserLocation(userId, longitude, latitude, address);
        if (result) {
            return ResponseEntity.ok(null);
        }
    } catch (NumberFormatException e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INSUFFICIENT_STORAGE).build();
}
```

画面4：
```java
@PostMapping
public ResponseEntity<UserLocationES> updateUserLocation(@RequestBody Map<String, Object> param) {
    try {
        Long userId = Long.valueOf(param.get("userId").toString());
        Double longitude = Double.valueOf(param.get("longitude").toString());
        Double latitude = Double.valueOf(param.get("latitude").toString());
        String address = param.get("address").toString();
        boolean result = this.userLocationService.updateUserLocation(userId, longitude, latitude, address);
        if (result) {
            return ResponseEntity.ok(null);
        }
    } catch (NumberFormatException e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INSUFFICIENT_STORAGE).build();
}
```

画面5：
```java
@Service
public class UserLocationService {
    @Autowired
    private ElasticsearchTemplate elasticsearchTemplate;
    public boolean updateUserLocation(Long userId, Double longitude, Double latitude, String address) {
        if (!this.elasticsearchTemplate.indexExists(UserLocationES.class)) {
            this.elasticsearchTemplate.createIndex(UserLocationES.class);
        }
        return false;
    }
}
```

画面6：
```java
if (!this.elasticsearchTemplate.indexExists(UserLocationES.class)) {
    this.elasticsearchTemplate.createIndex(UserLocationES.class);
}
if (!this.elasticsearchTemplate.typeExists(index: "tanhua", type: "user_location")) {
    this.elasticsearchTemplate.putMapping(UserLocationES.class);
}
return false;
```

画面7：
```java
if (!this.elasticsearchTemplate.typeExists(index: "tanhua", type: "user_location")) {
    this.elasticsearchTemplate.putMapping(UserLocationES.class);
}
```

画面8：
```java
// 判断用户的地理位置数据是否存在，如果存在，进行更新操作，如果不存在，插入新的数据
GetQuery getQuery = new GetQuery();
getQuery.setId(userId.toString());
UserLocationES ul = this.elasticsearchTemplate.queryForObject(getQuery, UserLocationES.class);
```

画面9：
```java
// 判断用户的地理位置数据是否存在，如果存在，进行更新操作，如果不存在，插入新的数据
GetQuery getQuery = new GetQuery();
getQuery.setId(userId.toString());
UserLocationES ul = this.elasticsearchTemplate.queryForObject(getQuery, UserLocationES.class);
if (null == ul) {
    // 新增位置数据
    UserLocationES userLocationES = new UserLocationES();
    userLocationES.setAddress(address);
    userLocationES.setCreated(System.currentTimeMillis());
    userLocationES.setLastUpdated(userLocationES.getCreated());
    userLocationES.setUpdated(userLocationES.getCreated());
    userLocationES.setUserId(userId);
    userLocationES.setLocation(new GeoPoint(latitude, longitude));
}
```

画面10：
```java
IndexQuery indexQuery = new IndexQueryBuilder().withObject(userLocationES).build();
this.elasticsearchTemplate.index(indexQuery); //保存数据到Elasticsearch中
```

画面11：
```java
UpdateRequest updateRequest = new UpdateRequestBuilder().withId(userId.toString())
        .withClass(UserLocationES.class)
        .withUpdateRequest(updateRequest).build();
this.elasticsearchTemplate.update(updateRequest);
```

画面12：
```java
Map<String, Object> map = new HashMap<>();
UpdateRequest updateRequest = new UpdateRequest();
updateRequest.doc(map);
UpdateQuery updateQuery = new UpdateQueryBuilder().withId(userId.toString())
        .withClass(UserLocationES.class)
        .withUpdateRequest(updateRequest).build();
this.elasticsearchTemplate.update(updateQuery);
```

画面13：
```java
// 判断类型是否存在，如果不存在，需要创建
if (!this.elasticsearchTemplate.typeExists(index: "tanhua", type: "user_location")) {
    // 创建类型
    this.elasticsearchTemplate.putMapping(UserLocationES.class);
}
```

画面14：
```java
// 判断索引是否存在，如果不存在需要创建
if (!this.elasticsearchTemplate.indexExists(UserLocationES.class)) {
    // 创建索引
    this.elasticsearchTemplate.createIndex(UserLocationES.class);
}
// 判断类型是否存在，如果不存在，需要创建
if (!this.elasticsearchTemplate.typeExists(index: "tanhua", type: "user_location")) {
    // 创建类型
    this.elasticsearchTemplate.putMapping(UserLocationES.class);
}
// 判断用户的地理位置数据是否存在，如果存在，进行更新操作，如果不存在，插入新的数据
GetQuery getQuery = new GetQuery();
getQuery.setId(userId.toString());
UserLocationES ul = this.elasticsearchTemplate.queryForObject(getQuery, UserLocationES.class);
if (null == ul) {
    // 新增位置数据
    UserLocationES userLocationES = new UserLocationES();
    userLocationES.setAddress(address);
    userLocationES.setCreated(System.currentTimeMillis());
    userLocationES.setLastUpdated(userLocationES.getCreated());
    userLocationES.setUpdated(userLocationES.getCreated());
    userLocationES.setUserId(userId);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
