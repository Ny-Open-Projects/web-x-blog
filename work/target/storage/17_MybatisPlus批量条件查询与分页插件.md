# 17. 六大数据库存储实战: MybatisPlus 批量、条件查询与分页插件

## 纲要

- 批量查询：`selectBatchIds` 接收 ID 列表，底层转换为 `IN (...)` 语句，未命中返回空数组
- 条件查询：`QueryWrapper` 用 `eq` 做等值、`like` 做模糊匹配；用 `StringUtils.isEmpty` 跳过空条件避免误拼
- 避坑：请求参数设默认值会导致 `id=0` 被误拼进 SQL；用 `required = false` + 判空规避
- 分页插件：在 `MybatisPlusConfig` 注册 `PaginationInnerInterceptor`，`Page` + `selectPage` 返回 `IPage`，`getRecords()` 取数据列表

## 📎 文本↔代码关联

本讲对应课件源码（去品牌化副本，位于 `code/socialecom/`；包名已由原占位包名统一改写为 `com.social.ecom`）：

| 代码文件 | 正文提及 | 职责 |
| --- | --- | --- |
| `code/socialecom/第二章代码/socialecom/src/main/java/com/social/ecom/pojo/User.java` | 7 次 | 实体类，主键 `IdType.AUTO` 自增，含乐观锁 `version` 字段，含自动填充时间字段 |
| `code/socialecom/第二章代码/socialecom/src/main/java/com/social/ecom/base/JsonReturnType.java` | 7 次 | 统一 JSON 返回结构（code / message / data） |
| `code/socialecom/第二章代码/socialecom/src/main/java/com/social/ecom/helper/MybatisPlusConfig.java` | 4 次 | MyBatis-Plus 配置类（乐观锁插件 / 分页插件） |
| `code/socialecom/第二章代码/socialecom/src/main/java/com/social/ecom/controller/UserController.java` | 1 次 | HTTP 接口层，路由前缀 `/user`；端点：`/get`、`/create`、`/update`、`/getforupdate`、`/updatebyversion`、`batchget`、`getbycondition` |

## 批量查询

`BaseMapper` 提供 `selectBatchIds`，直接接收一个 ID 列表，底层自动转换为 `IN (1,2,3)` 语句：

```java
@RequestMapping(value = "batchget", method = {RequestMethod.GET})
@ResponseBody
public JsonReturnType batchget(@RequestParam(name = "ids", defaultValue = "") List<Integer> ids) {
    List<User> userList = userMapper.selectBatchIds(ids);
    return JsonReturnType.createType(userList);
}
```

Spring MVC 会把 GET 参数 `ids=1,2,3` 自动转成 `List`。访问 `/user/batchget?ids=1,2,3` 即可批量取数；传入不存在的 ID 返回空数组，不会报错。

## 条件查询

复杂查询使用 `QueryWrapper` 拼装多条件。每个字段先判空，非空才拼进 SQL，避免把默认值误当成查询条件：

```java
@RequestMapping(value = "getbycondition", method = {RequestMethod.GET})
@ResponseBody
public JsonReturnType getbycondition(@RequestParam(name = "id", required = false) Long id,
                                     @RequestParam(name = "userName", defaultValue = "") String userName,
                                     @RequestParam(name = "userTel", defaultValue = "") String userTel) {
    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    if (id != null) {
        queryWrapper.eq("id", id);
    }
    if (!StringUtils.isEmpty(userName)) {
        queryWrapper.like("user_name", userName);
    }
    if (!StringUtils.isEmpty(userTel)) {
        queryWrapper.like("user_tel", userTel);
    }
    List<User> userList = userMapper.selectList(queryWrapper);
    return JsonReturnType.createType(userList);
}
```

两个要点：

- **列名用数据库下划线命名**（`user_name`），不是实体驼峰名。
- **`like` 用于模糊匹配**；密码等字段不适合做模糊查询，应排除。
- **请求参数不要带会误触发的默认值**：早期版本给 `id` 设了 `defaultValue = "0"`，导致 `id=0` 被拼进 `WHERE id = 0`；改成 `required = false` 后，未传参时 `id` 为 `null` 即可跳过。

各条件默认以 `AND` 连接；若需 `OR` 或更复杂的组合，可在 `QueryWrapper` 中嵌套 `or()`/嵌套 `and()`，这部分留作练习。

## 分页插件

列表拉取通常伴随分页。先在 `MybatisPlusConfig` 中注册分页拦截器（指定数据库类型为 MySQL，对应 `LIMIT`）：

```java
@Bean
public Interceptor mybatisPlusInterceptor() {
    MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
    // 乐观锁拦截器
    interceptor.addInnerInterceptor(new OptimisticLockerInnerInterceptor());
    // 分页拦截器，适配 MySQL
    interceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
    return interceptor;
}
```

控制器中构造 `Page` 对象并调用 `selectPage`：

```java
@RequestMapping(value = "getbycondition", method = {RequestMethod.GET})
@ResponseBody
public JsonReturnType getbycondition(@RequestParam(name = "id", required = false) Long id,
                                     @RequestParam(name = "userName", defaultValue = "") String userName,
                                     @RequestParam(name = "page", defaultValue = "1") Integer currentPage,
                                     @RequestParam(name = "size", defaultValue = "20") Integer size) {
    Page<User> page = new Page<>(currentPage, size);

    QueryWrapper<User> queryWrapper = new QueryWrapper<>();
    if (id != null) {
        queryWrapper.eq("id", id);
    }
    if (!StringUtils.isEmpty(userName)) {
        queryWrapper.like("user_name", userName);
    }

    IPage<User> userPage = userMapper.selectPage(page, queryWrapper);
    return JsonReturnType.createType(userPage.getRecords());
}
```

返回的 `IPage` 内部包含：

- `records`：当前页数据列表（对接 App 一般只需它）
- `total`：命中总数（底层自动执行 `SELECT COUNT`）
- `size` / `current`：每页条数 / 当前页

对于 App 类应用，通常不需要暴露总页数和页码，直接取 `getRecords()` 返回即可。验证时 `page=1&size=2` 只取两条，`page=2` 取第三条。

## API 速览

| 方法 | 作用 | 备注 |
| --- | --- | --- |
| `selectBatchIds(Collection)` | 按 ID 列表批量查询 | 转 `IN (...)` |
| `QueryWrapper.like(col,val)` | 模糊匹配 | 左/右 `%` 由调用方拼接 |
| `QueryWrapper.eq(col,val)` | 等值匹配 | 默认 `AND` 连接 |
| `new Page<>(current,size)` | 构造分页对象 | 页码从 1 起 |
| `selectPage(Page,wrapper)` | 分页查询 | 返回 `IPage` |
| `IPage.getRecords()` | 取当前页数据 | 对接前端常用 |

## Demo 示例

**运行说明**：在 `MybatisPlusConfig` 注册 `PaginationInnerInterceptor` 后重启；访问 `/user/getbycondition?page=1&size=2` 与 `page=2&size=2` 验证分页；`/user/batchget?ids=1,2,3` 验证批量。

**代码说明**：`Page` + `selectPage` 由插件自动改写 SQL 追加 `LIMIT`；条件查询注意判空与列名下划线。

**技术点总结**：MybatisPlus 用 `QueryWrapper` 把条件查询对象化，用分页拦截器把分页标准化；掌握判空、列名映射、分页返回结构，就能覆盖绝大多数列表类接口需求。

