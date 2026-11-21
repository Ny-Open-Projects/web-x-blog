# 画面线理解：12.探花功能实现之喜欢功能实现（dubbo接口实现）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\12.探花功能实现之喜欢功能实现（dubbo接口实现）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:15, 02:50, 03:30, 04:17, 04:50, 05:25, 06:10, 07:11, 08:16, 09:35, 10:23, 11:07, 11:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:30:47

1) 这一组画面整体在讲什么（一句话）：
实现用户点赞功能的 Java 代码，包括定义实体类、接口、实现类以及单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 UserLike 实体类定义，包含 @Document 注解和字段。
画面 2: 展示 UserLikeApi 接口，定义了 saveUserLike、isMutualLike、deleteUserLike 三个方法。
画面 3: 展示 UserLikeApiImpl 类的初始结构，实现接口的三个方法。
画面 4: 在 UserLikeApiImpl 中注入 MongoTemplate。
画面 5: 在 saveUserLike 方法中构建查询条件，检查是否存在。
画面 6: 在 saveUserLike 方法中创建 UserLike 实例并设置属性。
画面 7: 在 saveUserLike 方法中调用 mongoTemplate.save 保存对象并返回 ID。
画面 8: 在 isMutualLike 方法中构建查询条件，检查是否为相互喜欢。
画面 9: 在 isMutualLike 方法中使用 Criteria.where 构建查询条件。
画面 10: 在 isMutualLike 方法中构建查询条件并调用 remove 方法。
画面 11: 展示 TestUserLikeApiImpl 类的初始结构，实现接口的三个方法。
画面 12: 在 TestUserLikeApiImpl 中编写 testSave、testIsMutualLike、testDeleteUserLike 三个测试方法。
画面 13: 在 testIsMutualLike 方法中打印相互喜欢的测试结果。
画面 14: 展示 TestUserLikeApiImpl 的完整代码，包含三个测试方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
@Document(collection = "user_like")
public class UserLike implements java.io.Serializable {
    private static final long serialVersionUID = 673996663629466523L;
    private ObjectId id;
    private Long userId; //用户ID，自己
}
```

画面 2:
```java
/**
 * 保存喜欢
 * @param userId
 * @param likeUserId
 * @return
 */
String saveUserLike(Long userId, Long likeUserId);

/**
 * 相互喜欢
 * @param userId
 * @param likeUserId
 * @return
 */
Boolean isMutualLike(Long userId, Long likeUserId);

/**
 * 删除用户喜欢
 */
```

画面 3:
```java
package com.tanhua.dubbo.server.api;

public class UserLikeApiImpl implements UserLikeApi {
    @Override
    public String saveUserLike(Long userId, Long likeUserId) {
        return null;
    }

    @Override
    public Boolean isMutualLike(Long userId, Long likeUserId) {
        return null;
    }

    @Override
    public Boolean deleteUserLike(Long userId, Long likeUserId) {
        return null;
    }
}
```

画面 4:
```java
@Autowired
private MongoTemplate mongoTemplate;
```

画面 5:
```java
Query query = Query.query(Criteria.where("userId").is(userId)
        .and("likeUserId").is(likeUserId));
```

画面 6:
```java
UserLike userLike = new UserLike();
userLike.setId(ObjectId.get());
userLike.setLikeUserId(likeUserId);
userLike.setUserId(userId);
userLike.setCreated(System.currentTimeMillis());
```

画面 7:
```java
this.mongoTemplate.save(userLike);
return userLike.getId().toHexString();
```

画面 8:
```java
public Boolean isMutualLike(Long userId, Long likeUserId) {
    Query query = Query.query(Criteria.where("userId").is(userId)
            .and("likeUserId").is(likeUserId));
    this.mongoTemplate.remove(query, UserLike.class);
    return null;
}
```

画面 9:
```java
Criteria criteria = Criteria.where("userId").is(userId).and("likeUserId").is(likeUserId);
```

画面 10:
```java
Query query = Query.query(Criteria.where("userId").is(userId)
        .and("likeUserId").is(likeUserId));
DeleteResult deleteResult = this.mongoTemplate.remove(query, UserLike.class);
return deleteResult.getDeletedCount() == 1;
```

画面 11:
```java
package com.tanhua.dubbo.server.api;

@Service(version = "1.0.0")
public class UserLikeApiImpl implements UserLikeApi {
```

画面 12:
```java
@Test
public void testSave() {
    this.userLikeApi.saveUserLike(userId: 11, likeUserId: 21);
    this.userLikeApi.saveUserLike(userId: 11, likeUserId: 31);
    this.userLikeApi.saveUserLike(userId: 21, likeUserId: 11);
}

@Test
public void testIsMutualLike() {
    System.out.println(this.userLikeApi.isMutualLike(userId: 11, likeUserId: 21));
    System.out.println(this.userLikeApi.isMutualLike(userId: 21, likeUserId: 11));
    System.out.println(this.userLikeApi.isMutualLike(userId: 11, likeUserId: 31));
}

@Test
public void testDeleteUserLike() {
    System.out.println(this.userLikeApi.deleteUserLike(userId: 11, likeUserId: 21));
    System.out.println(this.userLikeApi.deleteUserLike(userId: 11, likeUserId: 31));
    System.out.println(this.userLikeApi.deleteUserLike(userId: 21, likeUserId: 11));
}
```

画面 13:
```java
@Test
public void testIsMutualLike() {
    System.out.println(this.userLikeApi.isMutualLike(userId: 11, likeUserId: 21));
    System.out.println(this.userLikeApi.isMutualLike(userId: 21, likeUserId: 11));
    System.out.println(this.userLikeApi.isMutualLike(userId: 11, likeUserId: 31));
}
```

画面 14:
```java
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestUserLikeApiImpl {
    @Autowired
    private UserLikeApi userLikeApi;

    @Test
    public void testSave() {
        this.userLikeApi.saveUserLike(11, 21);
        this.userLikeApi.saveUserLike(11, 31);
        this.userLikeApi.saveUserLike(21, 11);
    }

    @Test
    public void testIsMutualLike() {
        System.out.println(this.userLikeApi.isMutualLike(11, 21));
        System.out.println(this.userLikeApi.isMutualLike(21, 11));
        System.out.println(this.userLikeApi.isMutualLike(11, 31));
    }

    @Test
    public void testDeleteUserLike() {
        System.out.println(this.userLikeApi.deleteUserLike(11, 21));
        System.out.println(this.userLikeApi.deleteUserLike(11, 31));
        System.out.println(this.userLikeApi.deleteUserLike(21, 11));
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
