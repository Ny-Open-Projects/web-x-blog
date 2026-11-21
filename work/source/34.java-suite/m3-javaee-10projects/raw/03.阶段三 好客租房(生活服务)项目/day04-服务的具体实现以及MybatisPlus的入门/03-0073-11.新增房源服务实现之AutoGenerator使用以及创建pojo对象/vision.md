# 画面线理解：11.新增房源服务实现之AutoGenerator使用以及创建pojo对象

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\11.新增房源服务实现之AutoGenerator使用以及创建pojo对象【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:53, 02:44, 03:37, 04:10, 05:25, 06:20, 07:36, 08:39, 09:38, 11:07, 12:03, 13:05, 13:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:45:53

1) 这一组画面整体在讲什么（一句话）：
使用 MyBatis-Plus 的 AutoGenerator 插件，基于数据库表结构自动生成 Java 实体类（Entity）和对应的 Mapper 文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 PDF 文档中关于编写 BasePojo 文件的说明，要求所有 pojo 类继承该类并包含 created、updated 字段。
画面 2：展示 Navicat Premium 中的数据库表结构，包含 `tb_house_resources` 表的 CREATE TABLE 语句，定义了字段如 id、title、estateId、buildingNum 等。
画面 3：在 IntelliJ IDEA 中展示 Maven 项目结构，焦点在 `pom.xml` 文件，显示了父工程的配置。
画面 4：展示 PDF 文档中关于数据源配置的说明，包含 `PackageConfig` 的配置代码片段。
画面 5：在 IntelliJ IDEA 中展示 `CodeGenerator.java` 文件，显示了 `main` 方法中初始化 `AutoGenerator` 并配置数据源和包路径的代码。
画面 6：在 IntelliJ IDEA 中展示 `pom.xml` 文件的 `<dependencies>` 部分，列出了 MyBatis-Plus、Freemarker、MySQL Connector 等依赖。
画面 7：在 IntelliJ IDEA 中展示 `CodeGenerator.java` 文件的开头部分，导入了 MyBatis-Plus 相关的包和类。
画面 8：在 IntelliJ IDEA 中展示 `CodeGenerator.java` 文件中配置 `InjectionConfig` 的代码。
画面 9：在 IntelliJ IDEA 中展示生成的 `TbHouseResources.java` 文件，显示了继承 `BasePojo` 的类结构和部分字段。
画面 10：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了类定义和部分字段。
画面 11：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了类定义和部分字段。
画面 12：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了 `rent`、`rentMethod`、`paymentMethod` 等字段。
画面 13：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了 `houseType`、`coveredArea`、`useArea` 等字段。
画面 14：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了 `floor`、`orientation` 等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
package cn.itcast.haoke.dubbo.server.pojo;
import lombok.Data;
import java.util.Date;
@Data
public abstract class BasePojo implements java.io.Serializable{
    private Date created;
    private Date updated;
}
```

画面 2：
```sql
CREATE TABLE `tb_house_resources` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL COMMENT '楼盘名称',
  `province` varchar(10) DEFAULT NULL COMMENT '所在省',
  `city` varchar(10) DEFAULT NULL COMMENT '所在市',
  `address` varchar(100) DEFAULT NULL COMMENT '详细地址',
  `year` varchar(10) DEFAULT NULL COMMENT '建楼年份',
  `type` varchar(10) DEFAULT NULL COMMENT '房屋类型',
  `property_coos` varchar(10) DEFAULT NULL COMMENT '物业公司',
  `developers` varchar(20) DEFAULT NULL COMMENT '开发商',
  `created` datetime DEFAULT NULL COMMENT '创建时间',
  `updated` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1006 DEFAULT CHARSET=utf8 COMMENT='楼盘表';
```

画面 3：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>itcast-haoke-manage-dubbo-server</artifactId>
        <groupId>cn.itcast.haoke.manage</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>itcast-haoke-manage-dubbo-server-generator</artifactId>
</project>
```

画面 4：
```java
PackageConfig pc = new PackageConfig();
pc.setModuleName(scanner(tp, "模块名"));
pc.setParent("cn.itcast.haoke.dubbo.server");
mpg.setPackageInfo(pc);
```

画面 5：
```java
throw new MybatisPlusException("请输入正确的" + tip + "!");
public static void main(String[] args) {
    AutoGenerator mpg = new AutoGenerator();
    GlobalConfig gc = new GlobalConfig();
    String projectPath = System.getProperty("user.dir");
    gc.setOutputDir(projectPath + "/src/main/java");
    gc.setAuthor("itcast");
    gc.setOpen(false);
    mpg.setGlobalConfig(gc);
    DataSourceConfig dsc = new DataSourceConfig();
    dsc.setUrl("jdbc:mysql://172.16.55.185:3306/haoke?useUnicode=true&characterEncoding=utf-8&autoReconnect=true&allowMultiQueries=true");
    dsc.setDriverName("com.mysql.jdbc.Driver");
    dsc.setUserName("root");
    dsc.setPassword("root");
    mpg.setDataSource(dsc);
    PackageConfig pc = new PackageConfig();
    pc.setModuleName(scanner(tp, "模块名"));
    pc.setParent("cn.itcast.haoke.dubbo.server");
    mpg.setPackageInfo(pc);
}
```

画面 6：
```xml
<dependencies>
    <!-- freemarker 模板引擎 -->
    <dependency>
        <groupId>org.freemarker</groupId>
        <artifactId>freemarker</artifactId>
        <version>2.3.28</version>
    </dependency>
    <dependency>
        <groupId>com.baozimou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.0.5</version>
        <optional>true</optional>
    </dependency>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.47</version>
        <optional>true</optional>
    </dependency>
</dependencies>
```

画面 7：
```java
package cn.itcast.haoke.generator;
import com.baozimou.mybatisplus.core.toolkit.StringTool;
import com.baozimou.mybatisplus.generator.AutoGenerator;
import com.baozimou.mybatisplus.generator.config.*;
import com.baozimou.mybatisplus.generator.config.rules.NamingStrategy;
import com.baozimou.mybatisplus.generator.engine.FreemarkerTemplateEngine;
import org.apache.commons.lang3.StringUtil;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
```

画面 8：
```java
InjectionConfig cfg = new InjectionConfig() {
```

画面 9：
```java
@Data
@EqualsAndHashCode(callSuper = true)
@Accessors(chain = true)
public class TbHouseResources extends BasePojo {
    private static final long serialVersionUID = 1L;
    /**
     * 房源标题
     */
    private String title;
    /**
     * 楼盘id
     */
    private Long estateId;
    /**
     * 楼号（栋）
     */
    private String buildingNum;
```

画面 10：
```java
public class HouseResources extends BasePojo {
    private static final long serialVersionUID = 1L;
    /**
     * 房源标题
     */
    private String title;
    /**
     * 楼盘id
     */
    private Long estateId;
    /**
     * 楼号（栋）
     */
    private String buildingNum;
```

画面 11：
```java
package cn.itcast.haoke.dubbo.server.pojo;
import ...
@Data
@Accessors(chain = true)
@TableName("tb_house_resources")
public class HouseResources extends BasePojo {
    private static final long serialVersionUID = 1L;
    /**
     * 房源标题
     */
    private String title;
    /**
     * 楼盘id
     */
    private Long estateId;
```

画面 12：
```java
private Integer rent;
    /**
     * 租赁方式，1-整租，2-合租
     */
    private Boolean rentMethod;
    /**
     * 支付方式，1-付一押一，2-付三押一，3-付六押一，4-年付押一，5-其它
     */
    private Boolean paymentMethod;
    /**
     * 户型，如：2室1厅1卫
     */
    private String houseType;
    /**
     * 建筑面积
     */
    private String coveredArea;
    /**
     * 使用面积
     */
    private String useArea;
```

画面 13：
```java
private String buildingUnit;
