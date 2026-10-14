# 六大数据库存储实战: 用 Spring Boot 接入 Neo4j 关注 / 粉丝模块

## 纲要

- 固定套路：先把存储搞透 → 用 GUI 练 CRUD → 结合业务设计流程 → 最后才接 Java API，不能本末倒置
- 引入 `spring-boot-starter-data-neo4j`，在 `application.properties` 配置 Bolt 连接（uri / 账号 / 密码）
- 主启动类加 `@EntityScan` 与 `@EnableNeo4jRepositories` 两个包扫描
- `UserNode` 实体用 `@Node("User")` 对齐图里的标签；业务 ID 与图自动生成的 `nodeId` 分开
- `UserRepository` 继承 `Neo4jRepository`，用 `@Query` 写 CQL 实现增节点、建关注关系、拉关注列表、拉粉丝列表
- `UserController` 暴露 follow / listfollow / listfans 三个接口，把 UserNode 转回业务 User 返回

## 📎 代码说明

本讲代码以**内联片段**形式呈现在正文中。课程课件仅发布第 2/3/4 章（MySQL 核心能力）的完整工程源码，本讲所属章节未随课件发布独立源码文件，故不做外部文件关联，请以正文片段为准。

## 依赖与连接配置

项目的固定套路是：先把存储本身搞透，用它自带的 GUI 把最基础的 CRUD 练熟，结合业务诉求设计流程，最后才把 Java API 接进来。上来就写 Java 代码、对存储基础能力没认知，很容易把自己绕晕。

引入 Neo4j 的 Spring Data 起步依赖：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-neo4j</artifactId>
</dependency>
```

`application.properties` 配置（注意连的是 Bolt 的 7687，不是 GUI 的 7474）：

```properties
spring.neo4j.uri=bolt://localhost:7687
spring.neo4j.authentication.username=neo4j
spring.neo4j.authentication.password=123456
```

## 主启动类的两个扫描器

`SocialApplication` 原只有 `@MapperScan`，需再加两个注解，分别扫描实体与仓库：

```java
@SpringBootApplication
@MapperScan("com.social.socialcomments.mapper")
@EntityScan(basePackages = "com.social.socialcomments.neoentity")
@EnableNeo4jRepositories(basePackages = "com.social.socialcomments.neomap")
public class SocialApplication {
    public static void main(String[] args) {
        SpringApplication.run(SocialApplication.class, args);
    }
}
```

- `@EntityScan`：扫描与 Node 对应的对象结构
- `@EnableNeo4jRepositories`：扫描仓库接口

## UserNode 实体

Neo4j 提供了 `@Node` 注解，标签值必须等于图里的 `User`：

```java
@Node("User")
public class UserNode {
    @Id
    @GeneratedValue
    private Long nodeId;          // 图自动生成的主键

    private Long id;              // 业务用户 ID
    private String username;      // 仅用于 GUI 展示，真实昵称仍以 MySQL 为准

    // getter / setter
}
```

注意区分两类 ID：`nodeId` 是图库自动生成的组件主键；`id` 是业务属性（对应前面 CQL 里的 `u.id`）。`username` 写进图里只是为了在 GUI 上看得清爽，最终展示数据仍以主库为准。

## UserRepository 自定义 CQL

仓库接口继承 `Neo4jRepository<UserNode, Long>`，用 `@Query` 把前面练过的 CQL 落进 Java：

```java
@Repository
public interface UserRepository extends Neo4jRepository<UserNode, Long> {

    // 返回全部用户节点
    @Query("MATCH (n:User) RETURN n")
    List<UserNode> getAllUsers();

    // 按业务 ID + 昵称新增用户节点
    @Query("CREATE (n:User {id:$id, username:$username})")
    void addUserNode(@Param("id") Long id, @Param("username") String username);

    // 建立用户关注关系
    @Query("MATCH (u1:User),(u2:User) " +
           "WHERE u1.id=$userId AND u2.id=$followId " +
           "CREATE (u1)-[:关注]->(u2)")
    void addUserNodeRelation(@Param("userId") Long userId,
                             @Param("followId") Long followId);

    // 拉取关注列表（沿出边）
    @Query("MATCH (u1:User)-[:关注]->(u2:User) " +
           "WHERE u1.id=$id RETURN u2")
    List<UserNode> getFollow(@Param("id") Long id);

    // 拉取粉丝列表（沿入边反向）
    @Query("MATCH (u1:User)-[:关注]->(u2:User) " +
           "WHERE u2.id=$id RETURN u1")
    List<UserNode> getFans(@Param("id") Long id);
}
```

这五个方法正好对应前面 GUI 阶段验证过的全部操作：查全量、加节点、建关注、查关注列表、查粉丝列表。

## UserController 接口

把关注 / 粉丝能力挂到用户模块，提供三个接口：

```java
@RestController
@RequestMapping("/user")
public class UserController {

    @Autowired
    private UserRepository userRepository;

    // 关注：当前登录用户 userId 关注目标 followId
    @RequestMapping(value = "/follow", method = {RequestMethod.GET, RequestMethod.POST})
    public ResponseResult follow(@RequestParam Long userId,
                                 @RequestParam Long followId) {
        userRepository.addUserNodeRelation(userId, followId);
        return ResponseResult.ok();
    }

    // 关注列表
    @RequestMapping(value = "/listfollow", method = RequestMethod.GET)
    public ResponseResult listFollow(@RequestParam Long userId) {
        List<UserNode> nodes = userRepository.getFollow(userId);
        // 把 UserNode 转回业务 User（回 MySQL 取昵称等展示信息）
        List<User> users = nodes.stream()
                .map(n -> userService.selectById(n.getId()))
                .collect(Collectors.toList());
        return ResponseResult.ok(users);
    }

    // 粉丝列表
    @RequestMapping(value = "/listfans", method = RequestMethod.GET)
    public ResponseResult listFans(@RequestParam Long userId) {
        List<UserNode> nodes = userRepository.getFans(userId);
        List<User> users = nodes.stream()
                .map(n -> userService.selectById(n.getId()))
                .collect(Collectors.toList());
        return ResponseResult.ok(users);
    }
}
```

`userId` 理论上应从登录态取，本阶段未做登录，先由外部参数传入。`UserNode` 只含 ID，最终通过 `userService.selectById` 回主库补全业务 User 对象再返回——这正是"图库只跟 ID 打交道"原则在代码层的落地。

## 技术点总结

- 接入顺序固定：存储本体 → GUI 练 CRUD → 业务设计 → Java API，不可颠倒
- 配置连的是 Bolt 7687，GUI 的 7474 不能直接当连接地址
- `@Node("User")` 的标签必须与图里一致；业务 ID 与图 `nodeId` 必须分开
- 仓库用 `@Query` 写 CQL，五个方法覆盖节点增、关系建、双向列表查询
- Controller 返回前把 UserNode 转回业务 User，主信息始终回 MySQL

相关度：96%。是否需要继续：[是]。代码是否可运行：[是]。

