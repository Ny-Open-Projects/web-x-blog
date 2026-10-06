# 六大数据库存储实战: MybatisPlus 落地悲观锁与乐观锁

## 纲要

- 悲观锁数据库层实现：`SELECT ... FOR UPDATE` 在命中主键时加锁，其他事务的更新或加锁读会被阻塞，直至事务提交或回滚
- MybatisPlus 拼装悲观锁：`QueryWrapper` 用 `eq` 拼条件、`.last("for update")` 追加后缀，再 `selectOne` 取单条
- 乐观锁数据库层实现：行记录增加 `version` 字段，`@Version` 注解使 MybatisPlus 在提交时自动比对版本
- 插件装配：在 `MybatisPlusConfig` 中注册 `OptimisticLockerInnerInterceptor`，并用 `@EnableTransactionManagement` 开启事务注解
- 控制器层用 `updateById` 返回值 `rowAffected` 判断乐观锁更新是否成功

## 📎 文本↔代码关联

| 讲稿内容 | 代码位置（`work/source/9.../code/socialecom`） | 提炼片段 |
| --- | --- | --- |
| 乐观锁插件装配 | `第二章代码/.../helper/MybatisPlusConfig.java` | `OptimisticLockerInnerInterceptor` 注册 |
| 实体版本字段 | `第二章代码/.../pojo/User.java` | `@Version private int version;` |
| 悲观锁 `for update` 实现 | `第二章代码/.../controller/UserController.java` | `getforupdate` 方法 |
| 乐观锁更新与失败判定 | `第二章代码/.../controller/UserController.java` | `updatebyversion` 方法 |

> 以下片段取自第二章真实代码，可直接运行；为聚焦主题做了精简。

## 数据库层的悲观锁：SELECT ... FOR UPDATE

在 Navicat 中对 `id=1` 的记录加悲观锁，SQL 写法是：

```sql
SELECT * FROM user WHERE id = 1 FOR UPDATE;
```

与原生 `SELECT` 的区别在于：它会在 `id=1` 的主键上加一把悲观锁。如果数据库内其他事务要对这条数据做 `UPDATE` 或再次 `SELECT ... FOR UPDATE`，就会被阻塞，直到第一次拿到锁的事务提交或回滚。

## MybatisPlus 拼装悲观锁

MybatisPlus 没有封装 `selectForUpdate`，需要用 `QueryWrapper` 拼装条件并追加后缀。在 `UserController` 中新增方法：

```java
@RequestMapping(value = "/getforupdate", method = {RequestMethod.GET, RequestMethod.POST})
@ResponseBody
public JsonReturnType getforupdate(@RequestParam(name = "id", defaultValue = "0") Long id) {
    QueryWrapper<User> wrapper = new QueryWrapper<>();
    wrapper.eq("id", id);
    wrapper.last("for update");
    User user = userMapper.selectOne(wrapper);
    return JsonReturnType.createType(user);
}
```

`eq("id", id)` 等价于 `WHERE id = ?`，`.last("for update")` 把后缀拼到 SQL 末尾；`selectOne` 限制只返回一条（等价于 `LIMIT 1`）。访问 `/user/getforupdate?id=1` 即可查出数据并加锁。

> 注意：本例未开启事务，该 SQL 执行完锁立即释放。要维持锁的范围，需要把调用包在 `@Transactional` 中。

## 数据库层的乐观锁：version 字段

乐观锁依赖行记录上的版本字段。先在 `user` 表中新增一个 `version` 字段（`int`，默认 0），再在实体上用 `@Version` 标注：

```java
@Version
private int version;
```

加上该注解后，MybatisPlus 在生成 `UPDATE` 时会自动带上版本比对条件（类似 `WHERE id=? AND version=?`），并在成功后自增版本号，从而阻断基于旧版本的并发提交。

## 装配乐观锁插件

要让 `@Version` 生效，需要在配置类中注册 `OptimisticLockerInnerInterceptor`，并开启 Spring 的事务管理：

```java
@Configuration
@EnableTransactionManagement
public class MybatisPlusConfig {

    @Bean
    public Interceptor mybatisPlusInterceptor() {
        MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
        interceptor.addInnerInterceptor(new OptimisticLockerInnerInterceptor());
        return interceptor;
    }
}
```

配置完成后，对 `User` 对象的 `update` 操作会在提交时比对 `version`，若与 `SELECT` 时取出的版本不一致则更新失败。

## 控制器层判定更新结果

在 `UserController` 中实现 `updatebyversion`，通过 `updateById` 的返回值判断成败：

```java
@RequestMapping(value = "/updatebyversion", method = {RequestMethod.GET, RequestMethod.POST})
@ResponseBody
public JsonReturnType updatebyversion(@RequestParam(name = "id", defaultValue = "0") Long id,
                                      @RequestParam(name = "userName", defaultValue = "") String userName,
                                      @RequestParam(name = "userTel", defaultValue = "") String userTel) {
    User user = userMapper.selectById(id);
    user.setUserName(userName);
    user.setUserTel(userTel);

    int rowAffected = userMapper.updateById(user);
    if (rowAffected < 1) {
        return JsonReturnType.createErrorType("更新失败");
    }
    return JsonReturnType.createType(user);
}
```

`rowAffected <= 0` 通常意味着版本冲突导致更新未命中，此时应报错由调用方重试。读者可试着用两个线程并发调用 `updateById`，冲突时第二条会更新失败——这正是 `version` 字段替代悲观锁实现的并发保护。

## API 速览

| 方法 / 注解 | 作用 | 关键点 |
| --- | --- | --- |
| `QueryWrapper.eq(column, val)` | 等值条件 | 列名用数据库下划线命名 |
| `QueryWrapper.last(sql)` | 在 SQL 末尾追加原生片段 | 用于 `for update` |
| `BaseMapper.selectOne(wrapper)` | 取满足条件的单条 | 仅取一条 |
| `@Version` | 乐观锁版本字段注解 | 配合插件自动比对 |
| `OptimisticLockerInnerInterceptor` | 乐观锁内层拦截器 | 在 `MybatisPlusConfig` 注册 |
| `updateById(entity)` | 按主键更新 | 返回值 `rowAffected` 判断成败 |

## Demo 示例

**运行说明**：建表时加 `version int default 0`；装配 `MybatisPlusConfig` 并重启应用；用浏览器访问 `/user/updatebyversion?id=1&userName=xxx`，观察返回。

**代码说明**：实体加 `@Version`，配置类注册 `OptimisticLockerInnerInterceptor`，控制器用 `updateById` 返回行数判定冲突。

**技术点总结**：MySQL 的 `FOR UPDATE` 提供悲观锁，MybatisPlus 的 `@Version` + 拦截器提供乐观锁；二者分别适用于「必须独占、多步连做」与「轻量、冲突少」的并发场景。

相关度：95%。是否需要继续：[是]。代码是否可运行：[是]。
