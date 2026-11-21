# 画面线理解：13.Mybatis-Plus-代码生成器

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\13.Mybatis-Plus-代码生成器【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:52, 01:30, 01:52, 02:21, 02:58, 03:50, 04:26, 05:08, 05:50, 06:21, 06:56, 07:32, 08:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:42:09

1) 这一组画面整体在讲如何使用 MyBatis-Plus 的代码生成器（AutoGenerator）自动生成项目中的实体类、Mapper 接口、Service 和 Controller 层代码。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 展示了 IntelliJ IDEA 中一个 Spring Boot 项目的结构，包含 `src/main/java` 下的 `com.itcast` 包，以及 `test` 包下的 `UserMapperTest` 测试类。
- `UserMapperTest.java` 中的代码：
  ```java
  wrapper.likeRight("name", val: "张");
  wrapper.select("id", "name");
  List<User> users = this.userMapper.selectList(wrapper);
  for (User user : users) {
      System.out.println(user);
  }
  ```

画面 2:
- 展示了 Typora 中的 PPT 内容，标题为“6 代码生成器”。
- 画面中显示了“2) 获取官方案例”的代码片段：
  ```java
  package cn.itcast.mp_generator;
  import com.baomidou.mybatisplus.core.exceptions.MybatisPlusException;
  import com.baomidou.mybatisplus.core.toolkit.StringPool;
  import com.baomidou.mybatisplus.generator.AutoGenerator;
  import com.baomidou.mybatisplus.generator.config.InjectionConfig;
  import com.baomidou.mybatisplus.generator.config.po.TableInfo;
  import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;
  import java.util.ArrayList;
  import java.util.List;
  import java.util.Scanner;
  ```

画面 3:
- 展示了 `MpGenerator` 类的代码，其中定义了表名数组：
  ```java
  private static final String[] TABLE_NAMES = new String[][]{
      "t_user",
      "c_user"
  };
  ```

画面 4:
- 展示了 Windows 资源管理器中的文件，包含 `shangjue.zip` 和 `generator.zip` 两个压缩文件。

画面 5:
- 展示了 IntelliJ IDEA 中名为 `generator` 的项目结构，其中 `src/main/java` 下的 `com.itcast` 包和 `generator` 包可见。

画面 6:
- 展示了 `controller.java.ftl` 模板文件的内容，其中包含用于生成 Controller 类的 FreeMarker 模板代码：
  ```java
  @RestController
  @Controller
  @Api(value = "", tags = "", description="")
  class ${table.controllerName} {
  ```

画面 7:
- 展示了 `MyBatisPlusGenerator.java` 中的 `main` 方法，用于配置代码生成器：
  ```java
  public static void main(String[] args) {
      // 代码生成器
      AutoGenerator autoGenerator = new AutoGenerator();
      // 主要配置
      GlobalConfig globalConfig = new GlobalConfig();
      String projectPath = System.getProperty("user.dir");
      String projectName = "/generator";
      globalConfig.setOutputDir(projectPath + "/src/main/java");
      globalConfig.setAuthor("author");
      globalConfig.setOpen(false);
      globalConfig.setDbType(ID_WORKER);
      autoGenerator.setGlobalConfig(globalConfig);
  ```

画面 8:
- 展示了 `MyBatisPlusGenerator.java` 中的 `outputFile` 方法，用于自定义输出文件路径：
  ```java
  public String outputFile(TableInfo tableInfo) {
      return projectPath + "/src/main/resources/mapper/" + packageConfig.getModule() + "/" + tableInfo.getEntityName() + "Mapper" + StringPool.XML;
  }
  ```

画面 9:
- 展示了控制台输出，显示 MyBatis-Plus 代码生成器成功连接到 MySQL 数据库并开始生成代码。

画面 10:
- 展示了 `User.java` 实体类的代码，包含 `username`、`password`、`name` 和 `age` 等字段。

画面 11:
- 展示了控制台输出，显示 MyBatis-Plus 代码生成器成功生成了文件。

画面 12:
- 展示了 Typora 中的 PPT 内容，标题为“策略配置”，其中包含设置命名策略和实体类属性的代码：
  ```java
  StrategyConfig strategy = new StrategyConfig();
  strategy.setNaming(NamingStrategy.underline_to_camel);
  strategy.setColumnNaming(NamingStrategy.underline_to_camel);
  strategy.setEntityLombokModel(true);
  strategy.setRestControllerStyle(true);
  strategy.setInclude(TABLE_NAMES);
  strategy.setTablePrefix("th_");
  strategy.setEntityBooleanColumnRemovePrefix(true);
  mpg.setStrategy(strategy);
  mpg.execute();
  ```

画面 13:
- 展示了 `entity.java.ftl` 模板文件的内容，其中包含用于生成实体类的 FreeMarker 模板代码：
  ```java
  import io.swagger.annotations.ApiModel;
  import io.swagger.annotations.ApiModelProperty;
  <!--#if entityLombokModel-->
  import lombok.Data;
  <!--#end-->
  import com.baomidou.mybatisplus.annotation.TableName;
  ```

画面 14:
- 展示了 Typora 中的 PPT 内容，标题为“6 代码生成器”，其中包含对 `AutoGenerator` 的介绍和在 `pom.xml` 中引入依赖的代码：
  ```xml
  <dependency>
      <groupId>com.baomidou</groupId>
      <artifactId>mybatis-plus-generator</artifactId>
      <version>3.1.8c</version>
  </dependency>
  ```
