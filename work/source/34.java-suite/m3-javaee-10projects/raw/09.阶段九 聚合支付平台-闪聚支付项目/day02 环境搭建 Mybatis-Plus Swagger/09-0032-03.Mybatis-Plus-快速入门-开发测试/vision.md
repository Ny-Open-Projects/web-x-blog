# 画面线理解：03.Mybatis-Plus-快速入门-开发测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\03.Mybatis-Plus-快速入门-开发测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:37, 01:27, 01:55, 02:43, 03:04, 03:23, 04:01, 04:23, 04:57, 05:20, 05:38, 06:15, 06:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:35:41

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 MyBatis-Plus 框架进行数据库操作，并编写单元测试。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了项目结构，包含 src/main/java 下的 cn.itecast.mp 包，以及 src/main/resources/application.properties。
- 展示了 User.java 实体类代码，其中包含 @TableName("tb_user") 注解和多个 @TableField 注解。
画面2：
- 展示了 UserMapper.java 接口代码，继承自 BaseMapper<User>。
- 展示了 BaseMapper 中的常用方法，如 insert、selectById、selectList 等。
画面3：
- 展示了 SpringBootApplication.java 文件，其中包含 @SpringBootApplication 注解。
- 展示了 @SpringBootApplication 注解的源码，包含 @ComponentScan、@EnableAutoConfiguration 等。
画面4：
- 展示了 SpringBootApplication.java 文件，其中包含 @MapperScan 注解，指定扫描包为 "cn.itecast.mp.mapper"。
画面5：
- 展示了在项目中右键创建新包的对话框，提示输入新包名。
画面6：
- 展示了在项目中右键创建新类的对话框，提示输入类名。
画面7：
- 展示了 UserMapperTest.java 文件，其中包含 @SpringBootTest 注解。
画面8：
- 展示了 UserMapperTest.java 文件，其中包含 @RunWith(SpringRunner.class) 注解。
画面9：
- 展示了 UserMapperTest.java 文件，其中包含 @SpringBootTest 注解和 @RunWith(SpringRunner.class) 注解。
画面10：
- 展示了 MyApplication.java 文件，其中包含 @SpringBootApplication 注解。
- 展示了编译错误信息，提示 "MyApplication" 类必须在名为 "MyApplication.java" 的文件中声明。
画面11：
- 展示了 UserMapperTest.java 文件，其中包含测试方法 testSelect()。
- 展示了测试方法中的代码，调用 userMapper.selectList() 方法。
画面12：
- 展示了 UserMapperTest.java 文件，其中包含测试方法 testSelect()。
- 展示了测试方法中的代码，调用 userMapper.selectList() 方法。
画面13：
- 展示了 BaseMapper.java 文件，其中包含 deleteById、deleteBatchIds、update 等方法。
画面14：
- 展示了 MyBatis-Plus 的介绍文档，其中包含 MyBatis-Plus 的介绍、官网、GitHub 地址、码云地址等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@TableMame("tb_user")
public class User {
    @TableId("id")//指定主键字段名
    private Long id;
    @TableField("user_name")//指定对应字段名
    private String userName;
    private String password;
    @TableField("NAME")
    private String name;
    @TableField("AGE")
    private Integer age;
    private String email;
    @TableField("birthday")
    private LocalDate birthday;
}
```
画面2：
```java
package cn.itecast.mp.mapper;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
/**
 * Created by Administrator.
 */
public interface UserMapper extends BaseMapper<User> {
}
```
画面3：
```java
@SpringBootApplication
public class SpringBootApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringBootApplication.class, args);
    }
}
```
画面4：
```java
@SpringBootApplication
@MapperScan("cn.itecast.mp.mapper")
public class SpringBootApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringBootApplication.class, args);
    }
}
```
画面7：
```java
@RunWith(SpringRunner.class)
@SpringBootTest
public class UserMapperTest {
}
```
画面8：
```java
@RunWith(SpringRunner.class)
@SpringBootTest
public class UserMapperTest {
    @Autowired
    private UserMapper userMapper;
}
```
画面9：
```java
@RunWith(SpringRunner.class)
@SpringBootTest
public class UserMapperTest {
    @Autowired
    private UserMapper userMapper;
    @Test
    public void testSelect() {
        List<User> users = userMapper.selectList(null);
        System.out.println(users);
    }
}
```
画面13：
```java
package com.baomidou.mybatisplus.core.mapper;
import java.io.Serializable;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.ResultMap;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org
