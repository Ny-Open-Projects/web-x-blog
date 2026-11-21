# 画面线理解：07.Mybatis-Plus-通用CRUD-主键生成策略

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\07.Mybatis-Plus-通用CRUD-主键生成策略【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:11, 01:36, 02:10, 02:47, 03:13, 03:56, 04:22, 04:46, 05:26, 05:52, 06:36, 07:00, 07:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:38:30

1) 这一组画面整体在讲什么（一句话）：
讲解 MyBatis-Plus 中主键生成策略的几种方式，包括自增、手动设置、UUID、ID_WORKER 和 ID_WORKER_STR，并通过代码和测试演示其效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 MyBatis-Plus 主键生成策略的文档内容。
- 代码片段：
  ```java
  package com.baomidou.mybatisplus.annotation;

  import lombok.Getter;

  /**
   * 生成ID类型枚举类
   * @author hubin
   * @since 2015-11-10
   */
  @Getter
  public enum IdType {
      /**
       * 数据库ID自增
       */
      AUTO(0),
      /**
       * 该类型为主键自增类型
       */
  }
  ```

画面2：
- 展示了 `IdType` 枚举类的完整定义，包含 `AUTO`、`ID_WORKER`、`UUID`、`ID_WORKER_STR` 等常量。
- 代码片段：
  ```java
  /**
   * 全局唯一ID (idworker)
   */
  ID_WORKER(3),
  /**
   * 全局唯一ID (UUID)
   */
  UUID(4),
  /**
   * 字符串全局唯一ID (idworker 的字符串表示)
   */
  ID_WORKER_STR(5),
  private final int key;

  IdType(int key) {
      this.key = key;
  }
  ```

画面3：
- 展示了测试类 `UserMapperTest` 中的 `testInsert` 方法，用于插入用户数据。
- 代码片段：
  ```java
  public void testInsert() {
      User user = new User();
      user.setUserName("管理员");
      user.setPassword("111111");
      user.setAge(20);
      user.setUserName("zaoaoa");
      user.setBirthday(localDateTime);
      int i = userMapper.insert(user);
      System.out.println(i);
  }
  ```

画面4：
- 展示了 `User` 实体类的定义，其中包含主键字段 `id`。
- 代码片段：
  ```java
  @TableId(value = "id", type = IdType.AUTO) //指定主键的字段名
  private Long id;
  ```

画面5：
- 展示了测试类 `UserMapperTest` 中的 `testInsert` 方法，其中 `user.setId(100)` 被注释掉。
- 代码片段：
  ```java
  // user.setId(100);
  ```

画面6：
- 展示了文档中关于手动设置主键的说明。
- 代码片段：
  ```java
  @TableId(value = "ID", type = IdType.INPUT)
  private Long id;
  ```

画面7：
- 展示了测试结果，显示测试通过。
- 控制台输出：
  ```
  Tests passed: 1 of 1 test
  ```

画面8：
- 展示了 `User` 实体类中 `id` 字段的类型被修改为 `String`。
- 代码片段：
  ```java
  @TableId(value = "id", type = IdType.UUID)
  private String id;
  ```

画面9：
- 展示了文档中关于 `UUID` 主键生成策略的说明。
- 代码片段：
  ```java
  @TableId(value = "ID", type = IdType.UUID)
  private String id;
  ```

画面10：
- 展示了测试类 `UserMapperTest` 中的 `testInsert` 方法，其中 `user.setId(100)` 被注释掉。
- 代码片段：
  ```java
  // user.setId(100);
  ```

画面11：
- 展示了测试结果，显示测试通过。
- 控制台输出：
  ```
  Tests passed: 1 of 1 test
  ```

画面12：
- 展示了数据库表 `t_user` 的数据，其中 `id` 字段为自增的数字。
- 数据库表结构：
  ```
  id | user_name | password | age | email | birthday
  ```

画面13：
- 展示了文档中关于 `ID_WORKER_STR` 主键生成策略的说明。
- 代码片段：
  ```java
  @TableId(value = "ID", type = IdType.ID_WORKER_STR)
  private String id;
  ```

画面14：
- 展示了文档中关于 `ID_WORKER_STR` 主键生成策略的说明。
- 代码片段：
  ```java
  @TableId(value = "ID", type = IdType.ID_WORKER_STR)
  private String id;
  ```
