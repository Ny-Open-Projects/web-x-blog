# 六大数据库存储实战: 项目接入 MySQL 读写分离数据源

## 纲要

- 引入 `dynamic-datasource-spring-boot-starter`（3.2.0）实现多数据源与读写分离
- `application` 注掉单数据源，改配 `spring.datasource.dynamic`：primary=master + master/slave 两组
- slave 端口是 3307（对应上一节的从库容器），可加 `slave1` 后缀兼容多从库
- 方法加 `@DS("slave")` 走从库；不加则走 primary（master）
- 验证：清 Redis 缓存后，手动改从库数据，访问接口返回从库值，证明路由生效

## 一、引入动态数据源依赖

在 `pom.xml` 加入动态数据源 starter，替换原本单一数据源的方案：

```xml
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>dynamic-datasource-spring-boot-starter</artifactId>
    <version>3.2.0</version>
</dependency>
```

## 二、配置 master / slave 双数据源

把原先单一的 `spring.datasource` 配置注掉，改成 `dynamic` 多数据源。primary 设为主库 master：

```yaml
spring:
  datasource:
    dynamic:
      primary: master            # 默认走主库
      datasource:
        master:
          url: jdbc:mysql://localhost:3306/test?useUnicode=true&characterEncoding=utf8
          username: root
          password: 123456
          driver-class-name: com.mysql.cj.jdbc.Driver
        slave:                    # 从库，端口 3307
          url: jdbc:mysql://localhost:3307/test?useUnicode=true&characterEncoding=utf8
          username: root
          password: 123456
          driver-class-name: com.mysql.cj.jdbc.Driver
```

注意 slave 的端口是 **3307**（上一节从库容器的映射端口），不是 3306。为兼容未来多从库，可写成 `slave1` 这样的后缀。

## 三、用 @DS 路由读写

默认情况下，Service 方法走 primary（master）。要让查询走从库，只需在方法上加 `@DS("slave")`：

```java
@Service
public class ItemService {

    // 默认走 master（写）
    public void saveItem(Item item) {
        itemMapper.insert(item);
    }

    // 显式走 slave（读）
    @DS("slave")
    public Item getItemDetail(Long itemId) {
        return itemMapper.selectById(itemId);
    }
}
```

不加 `@DS` 一律走主库；加了 `@DS("slave")` 就路由到从库。读写分离由此通过数据源默认指向完成。

```mermaid
flowchart LR
    A[ItemService 方法] -->|无 @DS| M[(master 3306 写)]
    A -->|@DS slave| S[(slave 3307 读)]
```

## 四、验证路由真的生效

清掉 Redis 缓存（避免缓存命中掩盖数据库路由），访问商品详情 `SEtwo`：

```bash
redis-cli
select 1
flushall        # 清缓存，强制走数据库
```

为确认走的是从库而非主库，测试时直接手动改从库数据（生产严禁，仅测试）：把从库 item 名改成 `SE3`，主库仍是 `SE2`。再访问接口——返回的是 `SE3`，说明请求确实路由到了从库。

加上 `@DS("slave")` 后，读写分离就靠数据源默认指定完成路由，无需在业务代码里手写连接切换。

## 技术点总结

- 用 `dynamic-datasource-spring-boot-starter` 接管多数据源，primary 指定默认主库。
- 配置 master（3306）/ slave（3307）两组 JDBC，slave 可加序号后缀兼容多从。
- `@DS("slave")` 走从库，无注解走主库（primary）。
- 验证法：清缓存 + 改从库数据，接口返回从库值即证明读写分离路由生效。
- 此节与 5-14 的 Docker 主从部署前后衔接，构成"部署 + 接入"完整闭环。

相关度：92%。是否需要继续：[否]。代码是否可运行：[是]。
