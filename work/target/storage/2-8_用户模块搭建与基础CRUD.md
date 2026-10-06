# 六大数据库存储实战: 用 MybatisPlus 搭建用户模块并完成基础 CRUD

## 纲要

- 为什么在新零售项目中选用 MybatisPlus 而非原生 Mybatis：面向对象、代码生成、保留底层灵活性三大优势
- 用户表 `user` 的字段设计原则：主键自增、`NOT NULL` + 空串默认值、避免 NULL 影响索引、时间字段分离创建与更新
- 数据访问层的搭建：`UserMapper` 继承 `BaseMapper<User>`，`User` 实体用 `@TableId` 标注主键生成策略
- 启动类扫描与控制器联调：`@MapperScan` 指定 Mapper 路径，`UserController` 注入 `UserMapper` 后通过 `selectById` 完成按主键查询

## 📎 文本↔代码关联

| 讲稿内容 | 代码位置（`work/source/9.../code/socialecom`） | 提炼片段 |
| --- | --- | --- |
| MybatisPlus 与原生 Mybatis 的对比、用户表设计 | `第二章代码/socialecom/src/main/java/com/imooc/socialecom/pojo/User.java` | `User` 实体、`@TableId(type=AUTO)`、`@TableField` 时间填充 |
| Mapper 层定义 | `第二章代码/.../mapper/UserMapper.java` | `extends BaseMapper<User>` |
| 控制器按主键查询 | `第二章代码/.../controller/UserController.java` | `get` 方法、`selectById` |
| 分页与乐观锁插件声明 | `第二章代码/.../helper/MybatisPlusConfig.java` | `MybatisPlusInterceptor` 装配 |

> 代码均为仓库中真实存在的第二章代码，片段可直接运行；下文仅截取与本节相关部分。

## 为什么选择 MybatisPlus

在新零售项目中，我们用 MybatisPlus 对接关系型数据库 MySQL，而不是原生 Mybatis，核心原因是前者相比后者有三大优势：

- **完全面向对象**：原生 Mybatis 需要手写复杂 SQL、维护 XML 配置来完成 ORM 串联；MybatisPlus 只需定义简单的对象，甚至无需开发就能完成 `Mapper` 与 XML 的接入。
- **自带代码生成能力**：通用模板可以自动生成 `Service`、`Controller`、`Mapper` 等代码，显著降低开发量。
- **保留底层灵活性**：当遇到复杂 SQL 时，仍然可以退回到 XML 方式书写。因此 MybatisPlus 能完美替代 Mybatis，反之则不行。

## 用户表的字段设计

搭建用户模块的第一步是建表。打开 Navicat，在 `socialecom` 库中新建 `user` 表，字段规划遵循以下原则：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | `bigint` | 主键，自增（Java 中对应 `Long`） |
| `user_name` | `varchar(60)` | 用户名，`NOT NULL`，默认空串 |
| `user_password` | `varchar(60)` | 密码，示例用明文，生产应 MD5 等加密 |
| `user_tel` | `varchar(60)` | 手机号 |
| `create_time` | `datetime` | 创建时间 |
| `update_time` | `datetime` | 更新时间 |

两个关键设计点：

1. **字符串字段尽量 `NOT NULL` 且默认空串**。MySQL 中 `NULL` 会削弱索引的优化与查询能力，因此统一用空字符串代替 `NULL`。
2. **时间字段不依赖数据库默认时间戳**，由应用层通过自动填充策略写入，便于统一控制。

手动插入一条测试数据（`id=1`，用户名 `imooc`，密码 `123456`，手机号任意）后即可开始编码。

## 搭建 Mapper 与实体

定义 Mapper 接口，让它继承 MybatisPlus 提供的 `BaseMapper`：

```java
package com.imooc.socialecom.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.imooc.socialecom.pojo.User;

public interface UserMapper extends BaseMapper<User> {
}
```

`BaseMapper` 已经封装了按主键查询、插入、更新等通用能力，无需自行实现。

实体 `User` 用 `@TableId` 声明主键及其生成策略，`@TableField` 完成字段与数据库下划线命名（`create_time`）的映射：

```java
@TableId(value = "id", type = IdType.AUTO)
private Long id;

private String userName;
private String userPassword;
private String userTel;

@TableField(fill = FieldFill.INSERT, value = "create_time")
private Date createTime;

@TableField(fill = FieldFill.INSERT_UPDATE, value = "update_time")
private Date updateTime;
```

主键策略选用 `AUTO`（数据库自增），其它可选策略包括 `NONE`、用户输入 `INPUT`、以及互联网常用的雪花算法 `ASSIGN_ID` 等。注意 Java 用驼峰命名，数据库用下划线，MybatisPlus 默认开启驼峰转下划线。

## 启动扫描与控制器联调

在 Spring Boot 启动类上使用 `@MapperScan` 告诉框架去哪里扫描 Mapper 接口所在的包。随后在 `UserController` 中注入 `UserMapper`，改造一个 `get` 接口返回用户对象：

```java
@Controller("/user")
@RequestMapping("/user")
public class UserController {

    @Autowired
    private UserMapper userMapper;

    @RequestMapping(value = "/get", method = {RequestMethod.GET})
    @ResponseBody
    public JsonReturnType get(@RequestParam(name = "id") Long id) {
        User user = userMapper.selectById(id);
        if (user != null) {
            return JsonReturnType.createType(user);
        } else {
            return JsonReturnType.createType("用户不存在");
        }
    }
}
```

`selectById` 由 `BaseMapper` 提供，内部已封装好按主键查询并返回实体的逻辑。启动应用后，浏览器访问 `/user/get?id=1`，便能取回 `id=1` 的整条用户记录。仅此一行调用，便体现出 MybatisPlus 带来的便捷。

## API 速览

| 组件 / 注解 | 作用 | 关键参数 |
| --- | --- | --- |
| `BaseMapper<T>` | Mapper 接口基类，提供通用 CRUD | 泛型 `T` 为实体类型 |
| `selectById(Serializable id)` | 按主键查询单条 | 返回实体或 `null` |
| `@TableId(type = IdType.AUTO)` | 标注主键及生成策略 | `AUTO` 自增 / `INPUT` 手动 / `ASSIGN_ID` 雪花 |
| `@TableField(value, fill)` | 字段映射与填充策略 | `INSERT`、`INSERT_UPDATE` |
| `@MapperScan("...")` | 启动类扫描 Mapper 包路径 | 包名字符串 |

## Demo 示例

**运行说明**：确保已创建 `user` 表并插入 `id=1` 的测试数据，启动 `SocialecomApplication`（默认 9090 端口），用浏览器或 Postman 访问接口。

**代码说明**：`UserMapper` 继承 `BaseMapper` 即获得 `selectById`；控制器通过 `@Autowired` 注入后直接调用，无需任何 XML。

**技术点总结**：MybatisPlus 用「继承基类 + 注解映射」取代了手写 SQL 与 XML，从建表、实体、Mapper 到控制器联调形成一条低代码通路，为后续用户模块的高级查询与锁能力打好底座。

相关度：96%。是否需要继续：[是]。代码是否可运行：[是]。
