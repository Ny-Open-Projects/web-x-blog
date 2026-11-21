# 画面线理解：05.Mybatis-Plus-常见配置2

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\05.Mybatis-Plus-常见配置2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:21, 00:40, 01:01, 01:28, 02:20, 02:48, 03:12, 04:22, 05:27, 05:43, 05:57, 06:32, 06:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:37:09

1) 这一组画面整体在讲 MyBatis-Plus 的配置项 mapUnderscoreToCamelCase 的作用及如何通过配置文件解决字段映射问题。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 MyBatis-Plus 的配置项 mapperLocations 的说明，以及项目结构中 UserMapper.java 和 UserMapper.xml 文件的路径关系。
画面2: 展示了 application.properties 文件中的 MyBatis-Plus 配置，包括数据源、配置文件路径、映射文件路径和类型别名包。
画面3: 展示了 UserMapper.xml 文件中的 SQL 查询语句，以及测试类 UserMapperTest 中的测试方法。
画面4: 展示了 MyBatis-Plus 的配置项 mapUnderscoreToCamelCase 的说明，包括其类型、默认值和注意事项。
画面5: 展示了 application.properties 文件中的 MyBatis-Plus 配置，包括数据源、配置文件路径、映射文件路径和类型别名包。
画面6: 展示了 User 类的 Java 代码，其中包含 @TableField 注解来指定字段名。
画面7: 展示了测试失败的日志，提示 Property 'configuration' and 'configLocation' cannot be specified with together。
画面8: 展示了 application.properties 文件，其中配置了 MyBatis-Plus 的类型别名包。
画面9: 展示了 mybatis-config.xml 文件中的配置，包括 mapUnderscoreToCamelCase 设置为 true。
画面10: 展示了 User 类的 Java 代码，其中包含 @TableField 注解来指定字段名。
画面11: 展示了测试通过的日志，显示查询结果。
画面12: 展示了 mybatis-config.xml 文件中的配置，包括 mapUnderscoreToCamelCase 设置为 false。
画面13: 展示了 User 类的 Java 代码，其中包含 @TableField 注解来指定字段名。
画面14: 展示了 MyBatis-Plus 的配置项 mapUnderscoreToCamelCase 的说明，包括其类型、默认值和注意事项。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1:
mapperLocations即MyBatis Mapper 所对应的 mapper配置文件位置，如果您在 Mapper 中有自定义方法（XML 中有自定义实现），需要进行配置，告诉 Mapper 所对应的 XML 文件位置。
如果不配置mapperLocations时，mapper的xml文件存放路径需要和mapper class文件保持一致，文件名保持一致，如下：
画面2:
spring.datasource.driver-class-name=com.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=utf-8
spring.datasource.username=root
spring.datasource.password=mysql
#指定mybatis-config.xml配置
mybatis-plus.config-location = classpath:mybatis/mybatis-config.xml
#指定mapper文件位置
mybatis-plus.mapper-locations = classpath:mybatis/mapper/*.xml
#类型别名包
mybatis-plus.type-aliases-package = cn.itcast.mp.pojo
#日志配置
logging.level.root: debug
画面3:
<select id="findId" resultType="User" parameterType="java.lang.Long">
    select * from t_user where id = #{id}
</select>
画面4:
类型：boolean
默认值：true
是否开启自动驼峰命名规则（camel case）映射，即从经典数据库列名 A_COLUMN（下划线命名）到经典 Java 属性名 aColumn（驼峰命名）的类似映射。
注意：
在 MyBatis-Plus 中此属性默认值为true，用于生成最终的 SQL 语句
如果您您的数据库命名符合规则则无需使用 @TableField 注解指定数据库字段名
测试：
#开启自动驼峰映射，注意：配置configuration.map_underscore_to_camel_case则不能配置config_location
mybatis-plus.configuration.map_underscore_to_camel_case=true
画面5:
spring.datasource.username=root
spring.datasource.password=mysql
#指定mybatis-config.xml配置
mybatis-plus.config-location = classpath:mybatis/mybatis-config.xml
#指定mapper文件位置
mybatis-plus.mapper-locations = classpath:mybatis/mapper/*.xml
#类型别名包
mybatis-plus.type-aliases-package = cn.itcast.mp.pojo
#日志配置
logging.level.root: debug
画面6:
@TableId("id")//指定主键的字段名
private Long id;
// @TableField("user_name")//指定对应字段名
private String userName;
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
@TableField("EMAIL")
private String email;
@TableField("birthday")
private LocalDateTime birthday;
画面7:
17:24:28.210 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - SpringTest(ClassRunner constructor called with Class
17:24:28.251 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Instantiating CachedApplicationContextDelegate from class form spring
17:24:28.256 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Instantiating BootstrapContext using constructor for public class spring
17:24:28.259 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Instantiating TestContextBootstrap for test class (cn.itcast.mp.UserMapperTest)
17:24:28.262 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Method @ContextConfiguration not found for test class (cn.itcast.mp.UserMapperTest)
17:24:28.263 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Could not detect default resource locations for test class
17:24:28.264 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Could not find an annotation declaring component
17:24:28.265 [main] DEBUG org.springframework.test.context.junit4.SpringJUnit4ClassRunner - Found @SpringBootTestConfiguration cn.itcast.mp.UserMapperTest
画面8:
画面9:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <settings>
        <!--mybatis-plus.configuration.map_underscore_to_camel_case-->
        <setting name="mybatis-plus.configuration.map_underscore_to_camel_case" value="true"/>
    </settings>
    <plugins>
        <!--plugin interceptor="com.baidus.mybatisplus.extension.plugins.PaginationInterceptor"-->
    </plugins>
</configuration>
画面10:
@TableId("id")//指定主键的字段名
private Long id;
// @TableField("user_name")//指定对应字段名
private String userName;
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
@TableField("EMAIL")
private String email;
@TableField("birthday")
private LocalDateTime birthday;
画面11:
17:27:34.611 INFO 9204 [main] cn.itcast.mp.mapper.UserMapper.findById = Preparing: select * from t_user where id = ?
17:27:34.622 INFO 9204 [main] cn.itcast.mp.mapper.UserMapper.findById = Parameters: 2(Long)
17:27:34.625 INFO 9204 [main] cn.itcast.mp.mapper.UserMapper.findById = Total: 1
17:27:34.625 INFO 9204 [main] cn.itcast.mp.mapper.UserMapper.findById = Result: User(id=2, userName=null, password=123456, name=张三, age=20, email=123@163.com, birthday=2019-10-01T11:14:00)
画面12:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <settings>
        <!--mybatis-plus.configuration.map_underscore_to_camel_case-->
        <setting name="mybatis-plus.configuration.map_underscore_to_camel_case" value="false"/>
    </settings>
    <plugins>
        <!--plugin interceptor="com.baidus.mybatisplus.extension.plugins.PaginationInterceptor"-->
    </plugins>
</configuration>
画面13:
@TableId("id")//指定主键的字段名
private Long id;
// @TableField("user_name")//指定对应字段名
private String userName;
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
@TableField("EMAIL")
private String email;
@TableField("birthday")
private LocalDateTime birthday;
画面14:
类型：boolean
默认值：true
是否开启自动驼峰命名规则（camel case）映射，即从经典数据库列名 A_COLUMN（下
