# 07-搭建配置user-service工程

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\07-搭建配置user-service工程_【海量资源尽在 ubkz.com】.mp4
- 时长 12分6秒（音频 727s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 搭建配置user-Service工程在这一小节中我们的主要目标是配置user-Service工程并能够根据用户ID查询数据库中的用户那么这个目标在直白的去分析的话也就是要去实现这么一个需求可以访问一个浏览器中可以访问的地址然后再输出用户数据好
[00:32] 这是一个请求地址如何在我们的这个user-Service中能够处理这样的一个请求所以我们去分析它的一个实现步骤一添加启动器依赖那这个启动器依赖呢在我们的springboard工程中都要去添加至少你这是一个web工程所以我们要添加spring-book-starter-web这样的一个启动器加好后呢接下来你会发现它要去查询数据库所以通用map我们要加过来好
[01:03] 加完这些启动器依赖以后呢我们Springboard工程必少不了的还有是要编写创建我们的启动引导类和配置文件那配置文件要来做什么配置文件呢要去修改配置文件中的参数比如说你要去连接我们的数据库那要指定这些连接的参数完了以后接下来我们去编写测试代码
[01:34] 测试代码测试代码我们希望可以用一个Mapper去操作数据库用UserService实现查询业务UserController实现我们处理这样的一个请求好这些代码我们都要去编写编写完以后接下来我们再去启动我们的项目进行一个测试成功的标准就是在浏览器地址栏输入这个地址以后呢可以输出我们的数据库中用户信息
[02:04] 现在我们就打开IDEA按照我们的实现步骤一步步实现第一个是添加启动器依赖那这个依赖呢既然是一个web工程所以我们要去添加一个web的启动器好 去添加一个dependenciesspring-bo-starter-web好 加完以后呢接下来要去操作连接数据库那么我们相关的一些依赖也要加过来找到我们的副工程中已经定义好的我们只要把它引用过来使用就可以了
[02:35] 那在复工程中只是一个依赖坐标的管理它没有真正的去依赖我们在子工程模块中再去引入这些dependencies版本号已经在复工程中被管理了所以可以去掉依赖就加好加好后呢接下来再去编写启动引导类和配置文件那找到我们的这个工程要去添加创建启动引导类那曾经跟大家介绍过一个插件可以去创建这
[03:06] 启动引导类和配置文件那么右击点击创建的一个启动引导类的名称con.ithema.user.userapplication是否要生成配置文件要生成点击OK好生成了生成后接下来我们再去添加配置去修改我们的配置项
[03:34] 好就在这边我们要去连接数据库包括我们刚才在测试时指定的一个应用服务器的端口是9091那么来去改一下好server.port不是8080是9091好完后接下来你再去指定它的一个数据源就是datasourcedatasource中我们有一个比如说driver class好驱动的那就是mysql好完后接下来你再去配置它的一个urlurl
[04:03] 配置它的值是jdbc mysql localhost端口是3306然后连接的数据库我们现在也是没有的我们要一个spring cloud这么一个数据库好要去创建一回完了接下来呢再去指定连接的用户名user root接着是password rootok这些指定后呢我们又用了
[04:34] 通用Mapper所以我们指定一下它的一个别名包的扫描我们来指定mybattles.pyaliases-package好这一个我们指定一下con.it.hemma.user.pojo我们假设呢这一个工程中的实体类包放到这个路顶下现在这个包也是不存在的我们要去创建包括实体类根本也不存在OK我们先去把这个包创建一下
[05:05] 有一个package有了以后呢我们引入一个这样的实体类在我们用springboard工程中那个user就可以拿来用那我们在资料中也提供了user就是它接着我们打开来看一下里面的内容帮路径这不对那我们其他的是要用到的我们把它复制过来这个就实体类过来了过来后呢这边也不需要去修改什么也用了lamborg然后接下来
[05:43] 我们去创建数据库刚才用到了一个库呢叫做Spring Cloud我们现在是没有这么一个库的我们去创建一下连接好新建数据库新建数库名称指定叫做Spring Cloud字符集UTF8UTF8好点击确定数据库也就有了有了以后呢我们在这边把我们的数据库表给导进去这边资料中有一个tb消化线user.sql把它拖过来
[06:17] 好导入OK我们的数据库跟表也有了有了后呢回到我们的IDEA中OK这些准备好以后呢我们再去编写测试代码还有启动引导类中不要忘了我们用了mybates也就是通用Mapper中的一个Mapper扫描的注解要加上at Mapper scan用的是TK开头的
[06:48] 那么Mapper路径是放在it黑马点user.Mapper这么一个路径下现在也没有那我们去创建这样的Mapper创建一个接口叫做点user.Mapper这个接口就有了要去应用通用Mapper要去继承我们的一个叫做Mapper的接口指定实体类是userOK
[07:21] 那我们的这个Mapper就已经编写好了好了以后接下来我们去编写它的业务类Service.userService好里面呢我们要去做事情利用Mapper去查询数据首先它自己呢是一个Service然后我们再注入MapperAltwire注入privateUserMapper好UserMapper就有了我们提供一个方法就是查询
[07:55] 一个用户query by idreturn user map.select by primary key根据id去查询数据那么的user呢是刚才的引入的一个实体就是这个id好给过来这一个方法做的事情是根据主件查询用户好这是用户id
[08:30] 返回的就是我们的用户好这是业务方法业务方法完那后呢接下来再到我们的处理器编写一个处理器类Controller.usercontroller表示它是一个处理器at rest Controller然后我们的一个映射路径request mapping是user
[09:02] 里面应该注入我们的用方法去查询用户信息一样的AutoWire注入刚才我们的叫做UserServiceOK UserService业务对象就有了我们再去编写一个方法查询用户然后我们再利用这个UserService点好这个去查询怎么进入我们的这个方法的GetMapping我们把这个路径中的
[09:42] ID给获取到随at pass variable long ID好就拿到了并返回一个这样的用户输出到浏览器是以JSON格式输出因为我们用的是Rest Controller它自动会在所有方法中都添加Respond BodyOK这是我们的处理器处理器编写完以后呢你整个要测试的代码也就差不多已经编写完了完了以后呢只差去启动我们的一个
[10:12] 启动引导类然后再去测试那么现在来去启动它启动好以后呢按照我们的分析是要可以访问我们的这个地址的OK9091user8处理器我们刚才已经写了路径的ID我们也获取到了端口我们改的也是9091如果启动不报错的话那么我们现在就可以打开浏览器呢去访问好所以我们来打开看一下
[10:43] 访问地址是他我们回车没有问题是可以访问到的好那前面其实在这一个springboard的时候我们也做过没有什么太特别OK那回到笔记中来小结一下刚才这个服务提供工程user跟Service中做的事情其实就是正常的一个springboard工程的搭建只是我们添加了启动器依赖这个呢怕大家直接从我们的讲义中复制会有问题我们把它拿过来
[11:14] 还就是编写了编写配置文件一样的你把它拿过来依赖依赖的话呢我们是加了三个这样的依赖好我们来看一下到我们的碰文件那也就是他那这个碰文件中我们加了依赖有这一些还有就是我们的配置文件的配置项我们回到IDA中拿过来配置项application.yml这里边加的配置好
[11:56] 再到我们的笔记中OK这就是我们的一个user-Service工程的一个搭建配置测试完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
构建一个基于 Spring Cloud 的用户服务（user-Service），包含添加依赖、配置数据库、编写实体类、Mapper、Service 和 Controller 层代码，并最终启动应用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 PPT 页面，标题为“7. 搭建配置 user-Service 工程”，目标是配置 user-Service 工程并能根据用户 id 查询数据库中用户。需求是可以通过 http://localhost:9091/user/ 输出用户数据。
画面 2: 在 IntelliJ IDEA 中，展示 user-Service 项目的 pom.xml 文件，正在编辑依赖部分，高亮显示了 <artifactId>spring-boot-starter-web</artifactId>。
画面 3: 在 IntelliJ IDEA 中，展示 user-Service 项目的 pom.xml 文件，正在编辑依赖部分，高亮显示了 <artifactId>mybatis-spring-boot-starter</artifactId>。
画面 4: 在 IntelliJ IDEA 中，展示 application.yml 文件，配置了 server.port、spring.datasource 等数据库连接参数。
画面 5: 在 Notepad++ 中，展示 User.java 实体类的代码，包含 id、username、password、name、age、sex、birthday、created、updated 等字段。
画面 6: 在 IntelliJ IDEA 中，展示 User.java 实体类的代码，与画面 5 内容一致。
画面 7: 在 IntelliJ IDEA 中，展示 UserMapper.java 接口文件，内容为 public interface UserMapper extends Mapper<T>。
画面 8: 在 IntelliJ IDEA 中，展示 UserService.java 服务层代码，包含 @Service 注解和 queryById 方法。
画面 9: 在 IntelliJ IDEA 中，展示 UserController.java 控制器层代码，内容为空。
画面 10: 在 IntelliJ IDEA 中，展示 UserController.java 控制器层代码，添加了 @RestController、@RequestMapping("/user") 注解，并编写了 queryById 方法。
画面 11: 在 IntelliJ IDEA 中，展示 UserApplication.java 启动类，右键弹出菜单，选择“Run 'UserApplication'”。
画面 12: 展示 PPT 页面，标题为“7. 搭建配置 user-Service 工程”，列出实现步骤：1. 添加启动器依赖（web、通用Mapper）；2. 创建启动引导类和配置文件；3. 修改配置文件中的参数；4. 编写测试代码（UserMapper, UserService, UserController）；5. 测试。
画面 13: 展示 PPT 页面，标题为“7. 搭建配置 user-Service 工程”，列出实现步骤中的第一项“添加启动器依赖”，并展示对应的 Maven 依赖配置代码。
画面 14: 展示 PPT 页面，标题为“7. 搭建配置 user-Service 工程”，列出实现步骤中的第一项“添加启动器依赖”，并展示对应的 Maven 依赖配置代码。

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
    url: jdbc:mysql://localhost:3306/Spring Cloud
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
package com.ithema.user.Mapper;
import com.ithema.user.pojo.User;
import tk.mybatis.Mapper.common.Mapper;
public interface UserMapper extends Mapper<User> {

画面 8:
package com.ithema.user.Service;
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
package com.ithema.user.Controller;

画面 10:
package com.ithema.user.Controller;
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
<!--通用Mapper启动器-->
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
<!--通用Mapper启动器-->
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
画面 1: 标题“7. 搭建配置 user-Service 工程”，子标题“目标：配置 user-Service 工程并能够根据用户 id 查询数据库中用户”，“分析：需求：可以访问 http://localhost:9091/user/ 输出用户数据”。
画面 12: 标题“7. 搭建配置 user-Service 工程”，子标题“目标：配置 user-Service 工程并能够根据用户 id 查询数据库中用户”，“分析：需求：可以访问 http://localhost:9091/user/ 输出用户数据”，“实现步骤”列表。
画面 13: 标题“7. 搭建配置 user-Service 工程”，子标题“目标：配置 user-Service 工程并能够根据用户 id 查询数据库中用户”，“分析：需求：可以访问 http://localhost:9091/user/ 输出用户数据”，“实现步骤”列表中的第一项“添加启动器依赖”，并展示对应的 Maven 依赖配置代码。
画面 14: 标题“7. 搭建配置 user-Service 工程”，子标题“目标：配置 user-Service 工程并能够根据用户 id 查询数据库中用户”，“分析：需求：可以访问 http://localhost:9091/user/ 输出用户数据”，“实现步骤”列表中的第一项“添加启动器依赖”，并展示对应的 Maven 依赖配置代码。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

