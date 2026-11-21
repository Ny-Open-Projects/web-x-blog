# 画面线理解：13-SpringBoot整合Junit

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\13-SpringBoot整合Junit_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:46, 02:50, 03:18, 03:35, 03:55, 04:42, 04:55, 05:23, 05:47, 06:04, 06:35, 06:55, 07:35, 08:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:29:29

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SpringBoot 项目中整合 JUnit 进行单元测试，包括添加依赖、编写测试类和测试方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 页面，标题为“SpringBoot 整合其他框架”，内容包括案例需求“SpringBoot整合JUnit,”和实现步骤：① 搭建SpringBoot工程；② 引入starter-test起步依赖；③ 编写测试类；④ 添加测试相关注解（@RunWith(SpringRunner.class) 和 @SpringBootTest(classes = 启动类.class)）；⑤ 编写测试方法。
画面 2: IntelliJ IDEA 主界面，显示项目结构，当前打开的是 pom.xml 文件，但内容为空。
画面 3: IntelliJ IDEA 编辑器，显示测试类 SpringbootTestApplicationTests.java 的内容，其中包含 @RunWith(SpringRunner.class) 和 @SpringBootTest 注解。
画面 4: IntelliJ IDEA 编辑器，显示 pom.xml 文件内容，其中包含 <dependencies> 和 <build> 标签，具体依赖为 spring-boot-starter-test。
画面 5: IntelliJ IDEA 编辑器，显示 UserService.java 文件内容，包含一个 add() 方法。
画面 6: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，光标位于 @Test 注解上方，准备编写测试方法。
画面 7: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，已编写 @RunWith(SpringRunner.class) 和 @SpringBootTest 注解。
画面 8: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，已编写 @SpringBootTest(classes = SpringbootTestApplication.class) 注解。
画面 9: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，已编写 @Autowired private UserService userService; 字段。
画面 10: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，已编写测试方法 testAdd()，并运行测试，控制台显示测试通过。
画面 11: IntelliJ IDEA 编辑器，显示 SpringbootTestApplication.java 文件，包含 main 方法。
画面 12: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，测试方法 testAdd() 已编写完成。
画面 13: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，测试方法 testAdd() 已编写完成。
画面 14: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，测试失败，错误信息为“Could not find an 'annotation' declaration”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
案例：需求
SpringBoot整合JUnit,
案例：实现步骤
① 搭建SpringBoot工程
② 引入starter-test起步依赖
③ 编写测试类
④ 添加测试相关注解
• @RunWith(SpringRunner.class)
• @SpringBootTest(classes = 启动类.class)
⑤ 编写测试方法

画面 4:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.itheima</groupId>
    <artifactId>springboot-test</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
        <relativePath/>
    </parent>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>

画面 5:
package com.itheima.springboottest;
@Service
public class UserService {
    public void add() {
        System.out.println("add");
    }
}

画面 6:
@Test
public void testAdd() {
    // TODO
}

画面 7:
@RunWith(SpringRunner.class)
@SpringBootTest
public class UserServiceTest {

}

画面 8:
@RunWith(SpringRunner.class)
@SpringBootTest(classes = SpringbootTestApplication.class)
public class UserServiceTest {

}

画面 9:
@Autowired
private UserService userService;

画面 10:
@Test
public void testAdd() {
    userService.add();
}

画面 11:
package com.itheima.springboottest;
@SpringBootApplication
public class SpringbootTestApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootTestApplication.class, args);
    }
}

画面 12:
@RunWith(SpringRunner.class)
@SpringBootTest(classes = SpringbootTestApplication.class)
public class UserServiceTest {
    @Autowired
    private UserService userService;

    @Test
    public void testAdd() {
        userService.add();
    }
}

画面 13:
@RunWith(SpringRunner.class)
@SpringBootTest(classes = SpringbootTestApplication.class)
public class UserServiceTest {
    @Autowired
    private UserService userService;

    @Test
    public void testAdd() {
        userService.add();
    }
}

画面 14:
@RunWith(SpringRunner.class)
@SpringBootTest(classes = SpringbootTestApplication.class)
public class UserServiceTest {
    @Autowired
    private UserService userService;

    @Test
    public void testAdd() {
        userService.add();
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“SpringBoot 整合其他框架”，内容包括案例需求和实现步骤。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求完成）
