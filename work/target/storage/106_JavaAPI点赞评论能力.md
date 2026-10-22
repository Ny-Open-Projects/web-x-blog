# 106. 六大数据库存储实战: 用 Java API 实现点赞评论能力（中）

## 纲要

- 在 `application.yml` 中配置带鉴权的 MongoDB 连接（host/port/database/username/password）
- 定义两个实体 `LikeInfo`、`RemarkInfo`，用 `@Document` 与集合绑定，`@Id` 标记主键
- 定义 `LikeRemarkService` 接口：点赞、取消点赞、发评论、删评论，以及列表查询
- 用 `MongoTemplate` 实现写入路径：点赞插入、取消点赞按 `userId+messageId` 查后删、评论增删
- 用 `RestController` 暴露写入接口供 Postman 联调
- 代码为讲稿机翻重建，结构依所述设计，标注"根据讲稿逻辑补充"

## 📎 代码说明

本讲代码以**内联片段**形式呈现在正文中。课程课件仅发布第 2/3/4 章（MySQL 核心能力）的完整工程源码，本讲所属章节未随课件发布独立源码文件，故不做外部文件关联，请以正文片段为准。

## 配置 MongoDB 连接

引入依赖后，在 `application.yml` 中填入连接信息。因为是带鉴权（`--auth`）的实例，需要指定认证库与账号：

```yaml
spring:
  data:
    mongodb:
      host: 127.0.0.1
      port: 27017
      database: socialcomments
      authentication-database: admin
      username: admin
      password: 123456
```

## 定义实体

两个实体分别绑定 `like`、`remark` 集合。注意主键 `id` 必须是 `String` 并加 `@Id`：

```java
@Document(collection = "like")
public class LikeInfo {
    @Id
    private String id;
    private String userId;
    private Date likeTime;
    private String messageId;
    // getter / setter 省略
}

@Document(collection = "remark")
public class RemarkInfo {
    @Id
    private String id;
    private String userId;
    private Date remarkTime;
    private String messageId;
    private String remarkContent;
    // getter / setter 省略
}
```

`RemarkInfo` 比 `LikeInfo` 多了 `remarkContent` 字段，用来承载评论文本。

## 服务接口

接口声明点赞评论所需的全部能力，列表查询支持 `limit` / `skip` 分页：

```java
public interface LikeRemarkService {
    void like(String userId, String messageId);                 // 点赞
    void dislike(String userId, String messageId);              // 取消点赞
    void addRemark(RemarkInfo remarkInfo);                      // 发评论
    void deleteRemark(String remarkId);                         // 删评论
    // 列表查询（条件 + 分页 + 时间倒序）的落地与联调g> listLikeUsers(String messageId, int limit, int skip);
    List<RemarkInfo> listRemarks(String messageId, int limit, int skip);
}
```

## 用 MongoTemplate 实现

注入 `MongoTemplate`，实现核心读写。`like` 直接插入；`dislike` 按 `userId + messageId`（走索引）查出后删除，保证原子性：

```java
@Service
public class LikeRemarkServiceImpl implements LikeRemarkService {

    @Autowired
    private MongoTemplate mongoTemplate;

    @Override
    public void like(String userId, String messageId) {
        LikeInfo info = new LikeInfo();
        info.setUserId(userId);
        info.setMessageId(messageId);
        info.setLikeTime(new Date());
        mongoTemplate.insert(info);   // 唯一索引会拦截重复点赞
    }

    @Override
    public void dislike(String userId, String messageId) {
        Query query = new Query();
        query.addCriteria(Criteria.where("userId").is(userId)
                        .and("messageId").is(messageId));
        mongoTemplate.findAndRemove(query, LikeInfo.class);
    }

    @Override
    public void addRemark(RemarkInfo remarkInfo) {
        remarkInfo.setRemarkTime(new Date());
        mongoTemplate.insert(remarkInfo);
    }

    @Override
    public void deleteRemark(String remarkId) {
        Query query = new Query(Criteria.where("id").is(remarkId));
        mongoTemplate.findAndRemove(query, RemarkInfo.class);
    }

    // 以下两个列表方法仅给出签名与职责，条件分页与时间倒序的完整实现与联调 List<String> listLikeUsers(String messageId, int limit, int skip) {
        Query query = new Query(Criteria.where("messageId").is(messageId))
                .with(Sort.by(Sort.Direction.DESC, "likeTime"))
                .skip(skip).limit(limit);
        return mongoTemplate.find(query, LikeInfo.class).stream()
                .map(LikeInfo::getUserId).collect(Collectors.toList());
    }

    @Override
    public List<RemarkInfo> listRemarks(String messageId, int limit, int skip) {
        Query query = new Query(Criteria.where("messageId").is(messageId))
                .with(Sort.by(Sort.Direction.DESC, "remarkTime"))
                .skip(skip).limit(limit);
        return mongoTemplate.find(query, RemarkInfo.class);
    }
}
```

`dislike` 与 `deleteRemark` 都走索引条件（`userId+messageId` 或 `id`），删除操作命中索引且为单文档原子操作。`listLikeUsers` 返回的是点赞用户 `userId` 列表，而 `listRemarks` 返回评论实体（含内容）。

## 暴露接口

用 `RestController` 把能力暴露出来，方便用 Postman 联调：

```java
@RestController
@RequestMapping("/likeRemark")
public class LikeRemarkController {

    @Autowired
    private LikeRemarkService likeRemarkService;

    @PostMapping("/like")
    public String like(@RequestBody LikeInfo likeInfo) {
        likeRemarkService.like(likeInfo.getUserId(), likeInfo.getMessageId());
        return "ok";
    }

    @PostMapping("/dislike")
    public String dislike(@RequestBody LikeInfo likeInfo) {
        likeRemarkService.dislike(likeInfo.getUserId(), likeInfo.getMessageId());
        return "ok";
    }

    @PostMapping("/remark")
    public String addRemark(@RequestBody RemarkInfo remarkInfo) {
        likeRemarkService.addRemark(remarkInfo);
        return "ok";
    }

    @DeleteMapping("/remark")
    public String deleteRemark(@RequestParam String remarkId) {
        likeRemarkService.deleteRemark(remarkId);
        return "ok";
    }
}
```

## 小结

- `application.yml` 配置带鉴权的 MongoDB 连接，依赖 `MongoTemplate` 操作；
- 实体用 `@Document` / `@Id` 与集合、主键绑定；
- 点赞用 `insert`（唯一索引挡重），取消点赞与删评论用 `findAndRemove`（走索引、原子）；
- 列表查询用 `Criteria` + `skip` / `limit` 实现分页；
- 接口层用 `RestController` 暴露，可独立联调跑通基础读写。

> 说明：讲稿为机翻且代码碎片化，上述 Java 代码为"根据讲稿逻辑补充"重建，结构遵循所述 like/dislike/remark 设计，需在已引入 `spring-boot-starter-data-mongodb` 的 Spring Boot 工程中使用。

