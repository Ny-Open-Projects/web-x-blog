# 画面线理解：10.Mybatis-Plus-通用CRUD-查询操作

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\10.Mybatis-Plus-通用CRUD-查询操作【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:26, 02:59, 04:06, 04:54, 05:50, 06:49, 08:02, 09:08, 10:31, 12:34, 13:29, 14:30, 15:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:40:12

1) 这一组画面整体在讲 MyBatis-Plus 框架中查询操作的多种方式，包括根据 ID 查询、批量查询、条件查询、分页查询等。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 MyBatis-Plus 文档中 4.4 查询操作章节，重点是 4.4.1 selectById 方法定义，代码为：
```java
/**
 * 根据 ID 查询
 * @param id 主键ID
 */
I selectById(Serializable id),
```
画面2: 展示了测试类中 `testDelete20` 方法，使用 `userMapper.deleteBatchIds(Arrays.asList(101, 102, 103));` 批量删除用户，并在控制台输出删除结果。

画面3: 展示了测试类中 `testSelectOne` 方法，使用 `QueryWrapper<User> queryWrapper = new QueryWrapper<>();` 构建查询条件，并调用 `userMapper.selectOne(queryWrapper)` 查询单条记录。

画面4: 展示了 `testSelectOne` 方法的调试日志，显示了 SQL 执行语句和查询结果，返回的用户对象包含 id=101, name=张三, password=123456。

画面5: 展示了测试类中 `testSelectOne` 方法的代码，其中注释说明“根据条件查询，只能查询出一条记录，否则报错”。

画面6: 展示了测试类中 `testSelectCount` 方法，使用 `QueryWrapper<User> queryWrapper = new QueryWrapper<>();` 构建查询条件，并调用 `userMapper.selectCount(queryWrapper)` 查询符合条件的记录数。

画面7: 展示了 MyBatis-Plus 文档中 4.4 查询操作章节，重点是 4.4.6 selectPage 方法定义，以及分页插件的配置代码：
```java
package cn.itcast.mp;

import com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@MapperScan("cn.itcast.mp.mapper") //设置mapper接口的扫描包
public class MybatisPlusConfig {
```

画面8: 展示了项目结构，其中 `src/main/java` 下的 `config` 包中包含 `MybatisPlusConfig.java` 文件。

画面9: 展示了 `MybatisPlusConfig` 类的代码，其中定义了分页插件的 Bean：
```java
/**
 * 分页插件
 */
@Bean
public PaginationInterceptor paginationInterceptor() {
    return new PaginationInterceptor();
}
```

画面10: 展示了测试类中 `testSelectPage` 方法，使用 `Page<User> page = new Page<>(1, 3);` 创建分页对象。

画面11: 展示了 `testSelectPage` 方法的代码，其中设置了分页参数：
```java
//用构造方法设置当前页码，每页记录数
int pageIndex = 1; //当前页码
int size = 3; //每页记录数
Page<User> userPage = userMapper.selectPage(page, queryWrapper); //分页查询
long pages = userPage.getPages(); //总页数
```

画面12: 展示了 `testSelectPage` 方法的调试日志，显示了查询结果，其中 `userPage` 对象包含 `pages=1`, `current=1`, `size=3`, `records=[User@50086]`。

画面13: 展示了 `testSelectPage` 方法的调试日志，显示了查询结果，其中 `userPage` 对象包含 `pages=1`, `current=1`, `size=3`, `records=[User@50086]`。

画面14: 展示了 MyBatis-Plus 文档中 4.4 查询操作章节，重点是 4.4.6 selectPage 方法定义，以及分页插件的配置代码：
```java
package cn.itcast.mp;

import com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@MapperScan("cn.itcast.mp.mapper") //设置mapper接口的扫描包
public class MybatisPlusConfig {
```

3) 无

4) 无

5) 无
