# 画面线理解：07-搭建配置user-service工程

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\07-搭建配置user-service工程_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:31, 02:21, 03:10, 04:40, 05:28, 06:25, 07:26, 08:03, 08:50, 09:26, 10:17, 11:01, 11:46, 12:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:10:44

1) 这一组画面整体在讲什么（一句话）：
构建一个基于 Spring Cloud 的用户服务（user-service），包含添加依赖、配置数据库、编写实体类、Mapper、Service 和 Controller 层代码，并最终启动应用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 PPT 页面，标题为“7. 搭建配置 user-service 工程”，目标是配置 user-service 工程并能根据用户 id 查询数据库中用户。需求是可以通过 http://localhost:9091/user/ 输出用户数据。
画面 2: 在 IntelliJ IDEA 中，展示 user-service 项目的 pom.xml 文件，正在编辑依赖部分，高亮显示了 <artifactId>spring-boot-starter-web</artifactId>。
画面 3: 在 IntelliJ IDEA 中，展示 user-service 项目的 pom.xml 文件，正在编辑依赖部分，高亮显示了 <artifactId>mybatis-spring-boot-starter</artifactId>。
画面 4: 在 IntelliJ IDEA 中，展示 application.yml 文件，配置了 server.port、spring.datasource 等数据库连接参数。
画面 5: 在 Notepad++ 中，展示 User.java 实体类的代码，包含 id、username、password、name、age、sex、birthday、created、updated 等字段。
画面 6: 在 IntelliJ IDEA 中，展示 User.java 实体类的代码，与画面 5 内容一致。
画面 7: 在 IntelliJ IDEA 中，展示 UserMapper.java 接口文件，内容为 public interface UserMapper extends Mapper<T>。
画面 8: 在 IntelliJ IDEA 中，展示 UserService.java 服务层代码，包含 @Service 注解和 queryById 方法。
画面 9: 在 IntelliJ IDEA 中，展示 UserController.java 控制器层代码，内容为空。
画面 10: 在 IntelliJ IDEA 中，展示 UserController.java 控制器层代码，添加了 @RestController、@RequestMapping("/user") 注解，并编写了 queryById 方法。
画面 11: 在 IntelliJ IDEA 中，展示 UserApplication.java 启动类，右键弹出菜单，选择“Run 'UserApplication'”。
画面 12: 展示 PPT 页面，标题为“7. 搭建配置 user-service 工程”，列出实现步骤：1. 添加启动器依赖（web、通用Mapper）；2. 创建启动引导类和配置文件；3. 修改配置文件中的参数；4. 编写测试代码（UserMapper, UserService, UserController）；5. 测试。
画面 13: 展示 PPT 页面，标题为“7. 搭建配置 user-service 工程”，列出实现步骤中的第一项“添加启动器依赖”，并展示对应的 Maven 依赖配置代码。
画面 14: 展示 PPT 页面，标题为“7. 搭建配置 user-service 工程”，列出实现步骤中的第一项“添加启动器依赖”，并展示对应的 Maven 依赖配置代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
<artifactId>spring-cloud-dependencies</artifactId>
<version>${spring-cloud.version}</version>
<scope>import</scope>
</dependency>

画面 2:
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-web</artifactId>
</dependency>

画面 3:
<dependency>
<groupId>tk.mybatis</groupId>
<artifactId>mybatis-spring-boot-starter</artifactId>
</dependency>

画面 4:
server:
  port: 9091
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/springcloud
    username: root
    password: root

画面 5:
@Table(name = "user")
public class User {
    @Id
    @KeySql(useGeneratedKeys = true)
    private long id;
    //用户名
    private String username;
    //密码
    private String password;
    //姓名
    private String name;
    //年龄
    private Integer age;
    //性别：男性->女性
    private Integer sex;
    //出生日期
    private Date birthday;
    //创建时间
    private Date created;
    //更新时间
    private Date updated;
    //备注
    private String remark;
}

画面 6:
@Table(name = "user")
public class User {
    @Id
    @KeySql(useGeneratedKeys = true)
    private long id;
    //用户名
    private String username;
    //密码
    private String password;
    //姓名
    private String name;
    //年龄
    private Integer age;
    //性别：男性->女性
    private Integer sex;
    //出生日期
    private Date birthday;
    //创建时间
    private Date created;
    //更新时间
    private Date updated;
    //备注
    private String remark;
}

画面 7:
package com.ithema.user.mapper;
import com.ithema.user.pojo.User;
import tk.mybatis.mapper.common.Mapper;
public interface UserMapper extends Mapper<User> {

画面 8:
package com.ithema.user.service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class UserService {
    @Autowired
    private UserMapper userMapper;
    public User queryById(Long id) {
        return userMapper.selectByPrimaryKey(id);
    }
}

画面 9:
package com.ithema.user.controller;

画面 10:
package com.ithema.user.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService userService;
    public User queryById(Long id) {
        return userService.queryById(id);
    }
}

画面 11:
package com.ithema.user;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class UserApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserApplication.class, args);
    }
}

画面 12:
实现步骤：
1. 添加启动器依赖（web、通用Mapper）；
2. 创建启动引导类和配置文件；
3. 修改配置文件中的参数；
4. 编写测试代码（UserMapper, UserService, UserController）；
5. 测试。

画面 13:
<dependencies>
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-web</artifactId>
</dependency>
<!--通用mapper启动器-->
<dependency>
<groupId>tk.mybatis</groupId>
<artifactId>mybatis-spring-boot-starter</artifactId>
</dependency>
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
</dependency>
</dependencies>

画面 14:
<dependencies>
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-web</artifactId>
</dependency>
<!--通用mapper启动器-->
<dependency>
<groupId>tk.mybatis</groupId>
<artifactId>mybatis-spring-boot-starter</artifactId>
</dependency>
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
</dependency>
</dependencies>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题“7. 搭建配置 user-service 工程”，子标题“目标：配置 user-service 工程并能够根据用户 id 查询数据库中用户”，“分析：需求：可以访问 http://localhost:9091/user/ 输出用户数据”。
画面 12: 标题“7. 搭建配置 user-service 工程”，子标题“目标：配置 user-service 工程并能够根据用户 id 查询数据库中用户”，“分析：需求：可以访问 http://localhost:9091/user/ 输出用户数据”，“实现步骤”列表。
画面 13: 标题“7. 搭建配置 user-service 工程”，子标题“目标：配置 user-service 工程并能够根据用户 id 查询数据库中用户”，“分析：需求：可以访问 http://localhost:9091/user/ 输出用户数据”，“实现步骤”列表中的第一项“添加启动器依赖”，并展示对应的 Maven 依赖配置代码。
画面 14: 标题“7. 搭建配置 user-service 工程”，子标题“目标：配置 user-service 工程并能够根据用户 id 查询数据库中用户”，“分析：需求：可以访问 http://localhost:9091/user/ 输出用户数据”，“实现步骤”列表中的第一项“添加启动器依赖”，并展示对应的 Maven 依赖配置代码。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
