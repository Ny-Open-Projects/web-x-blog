# 画面线理解：04.圈子推荐之增加自增长id

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\04.圈子推荐之增加自增长id_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:27, 02:21, 03:13, 03:44, 05:06, 05:43, 06:19, 06:56, 09:56, 11:10, 11:52, 12:51, 13:22, 13:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:53:17

1) 这一组画面整体在讲如何为 MongoDB 中的 Publish 对象动态增加自增 ID，并通过 Redis 实现 ID 的自增长逻辑。

2) 按时间顺序列出每张画面的要点：
画面1: 讲解动态增加自增 id 的背景，需要修改 Publish 对象使其支持 Long 类型的 id。
画面2: 展示 Publish.java 文件，定义了 Publish 对象的结构，包含 id、userId、text、medias、seeType、seeList、longitude、latitude、locationName、created 字段。
画面3: 展示 QuanzApiImpl.java 文件中 savePublish 方法的实现，其中包含设置 publish 对象的字段和调用 mongoTemplate.save(publish) 保存数据。
画面4: 展示 QuanzApiImpl.java 文件中 savePublish 方法的实现，其中包含校验 publish 对象的 userId 是否为空。
画面5: 展示 pom.xml 文件中 <build> 标签下的 <plugin> 配置，用于 Spring Boot 的 Maven 插件。
画面6: 展示 pom.xml 文件中 <dependencies> 标签下的 <dependency> 配置，用于引入 Spring Boot Starter Redis。
画面7: 展示 IdService.java 文件的包声明和注释，说明该服务用于实现 Redis 的自增长 ID。
画面8: 展示 IdService.java 文件中 createId() 方法的实现，使用 redisTemplate.opsForValue().increment(0) 生成自增长 ID。
画面9: 展示 IdService.java 文件中 createId() 方法的实现，使用 redisTemplate.opsForHash() 检查 ObjectID 是否已存在。
画面10: 展示 IdService.java 文件中 createId() 方法的实现，使用 redisTemplate.opsForHash().get(hashKey, objectId) 获取已存在的 ID。
画面11: 展示 IdService.java 文件中 createId() 方法的实现，使用 redisTemplate.opsForValue().increment(key) 生成新的 ID。
画面12: 展示 QuanzApiImpl.java 文件中 savePublish 方法的实现，调用 idService.createId(type, objectId) 生成自增长 ID。
画面13: 展示 IdService.java 文件中 createId() 方法的实现，使用 StringUtils.center() 方法将生成的 ID 填充为指定长度。
画面14: 展示 day08.md 文件中 Publish 对象的定义，包含 id、userId、text、medias、seeType、seeList、longitude、latitude、locationName、created 字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;

// 发布表，动态内容
@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "quanzi_publish")
public class Publish implements java.io.Serializable {
```

画面3:
```java
if (publish.getUserId() == null) {
    return false;
}
try {
    //填充数据
    publish.setUserId(ObjectId.get());
    publish.setCreated(System.currentTimeMillis()); //发布时间
    publish.setSeeType(1); //查看权限
    publish.setPid();
    //保存动态信息
    this.mongoTemplate.save(publish);
    //写入到自己的指针表中
    Album album = new Album();
    album.setPublish(publish.getId()); //动态id
    album.setCreated(System.currentTimeMillis());
```

画面4:
```java
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import java.util.ArrayList;
import java.util.List;

@Service(version = "1.0.0") implements QuanZiApi {
    @Autowired
    private MongoTemplate mongoTemplate;
    @Override
    public boolean savePublish(Publish publish) {
        //校验publish对象
        if (publish.getUserId() == null) {
            return false;
        }
        try {
            //填充数据
```

画面5:
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <mainClass>com.tanhua.dubbo.server.DubboApplication</mainClass>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

画面6:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

画面7:
```java
package com.tanhua.dubbo.server.service;
import org.springframework.stereotype.Service;

/**
 * 原型：使用Redis的自增长类型，实现自增长的id
 */
@Service
public class IdService {
```

画面8:
```java
@Service
public class IdService {
    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    /**
     * 生成自增长的id
     * @return
     */
    public Long created() {
        this.redisTemplate.opsForValue().increment(0);
        return null;
    }
}
```

画面9:
```java
public Long created() {
    this.redisTemplate.opsForValue().increment(0);
    return null;
}
```

画面10:
```java
public Long createId(String type, String objectId) {
    String hashKey = "TANHUA_HASH_ID_" + type;
    if (this.redisTemplate.opsForHash().hasKey(hashKey, objectId)) {
        return this.redisTemplate.opsForHash().get(hashKey, objectId);
    }
```

画面11:
```java
public Long createId(String type, String objectId) {
    String hashKey = "TANHUA_HASH_ID_" + type;
    if (this.redisTemplate.opsForHash().hasKey(hashKey, objectId)) {
        return this.redisTemplate.opsForHash().get(hashKey, objectId).toString();
    }
    String key = "TANHUA_ID_" + type;
    Long id = this.redisTemplate.opsForValue().increment(key);
    this.redisTemplate.opsForHash().put(hashKey, objectId, id);
    return id;
}
```

画面12:
```java
publish.setPid(this.idService.createId("publish", publish.getUserId()));
```

画面13:
```java
public Long createId(String type, String objectId) {
    String hashKey = "TANHUA_HASH_ID_" + type;
    if (this.redisTemplate.opsForHash().hasKey(hashKey, objectId)) {
        return this.redisTemplate.opsForHash().get(hashKey, objectId).toString();
    }
    String key = "TANHUA_ID_" + type;
    Long id = this.redisTemplate.opsForValue().increment(key);
    this.redisTemplate.opsForHash().put(hashKey, objectId, id);
    return id;
}
```

画面14:
```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;

// 发布表，动态内容
@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "quanzi_publish")
public class Publish implements java.io.Serializable {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
