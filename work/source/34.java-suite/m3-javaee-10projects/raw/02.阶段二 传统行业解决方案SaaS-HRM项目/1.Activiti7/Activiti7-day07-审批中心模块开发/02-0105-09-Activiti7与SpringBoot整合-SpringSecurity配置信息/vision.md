# 画面线理解：09-Activiti7与SpringBoot整合-SpringSecurity配置信息

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\09-Activiti7与SpringBoot整合-SpringSecurity配置信息_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:01, 01:51, 03:10, 05:45, 06:42, 07:25, 08:39, 09:16, 10:10, 11:01, 11:49, 12:47, 13:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:38:55

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SpringBoot 项目中集成 Activiti7，包括添加依赖、配置 SpringSecurity 安全框架、使用新 API 实现工作流开发等步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“SpringBoot 整合 Activiti7 的”，列出整合步骤：1. 添加 SpringBoot 整合 Activiti7 的坐标；2. 添加 SpringSecurity 安全框架的整合配置信息；3. 使用 Activiti7 新支持的类来实现工作流开发；4. 使用新的 API 实现工作流开发，主要包括流程定义查询、启动流程实例、任务的查询、任务的完成。
画面 2: 展示 IntelliJ IDEA 中的 Maven 项目结构和 pom.xml 文件内容，其中包含 Activiti7 的 Spring Boot Starter 依赖。
画面 3: 展示课程 PPT 页面，标题为“3.1 SpringBoot 整合 Activiti7 的”，内容与画面 1 相同。
画面 4: 展示 Windows 资源管理器，路径为“activiti-examples-master”，列出多个 Activiti 示例项目文件夹。
画面 5: 展示 Windows 资源管理器，路径为“activiti-api-spring-integration-example”，列出 DemoApplication.java、DemoApplicationConfiguration.java 和 SecurityUtil.java 等文件。
画面 6: 展示 IntelliJ IDEA 中 SecurityUtil.java 文件内容，其中包含 @Component 注解、@Autowired 注解和 loginAs 方法。
画面 7: 展示 Windows 资源管理器，路径为“activiti-examples-master”，列出 DemoApplicationConfiguration.java 和 SecurityUtil.java 文件。
画面 8: 展示 IntelliJ IDEA 中 DemoApplicationConfiguration.java 文件内容，其中包含 @Configuration 注解和 configure 方法，用于配置 UserDetailsService。
画面 9: 展示 IntelliJ IDEA 中 DemoApplicationConfiguration.java 文件内容，其中包含 configure 方法的详细代码，用于创建 InMemoryUserDetailsManager 并注册用户。
画面 10: 展示 Windows 资源管理器，路径为“activiti-api-spring-integration-example”，列出 DemoApplicationConfiguration.java 文件。
画面 11: 展示 IntelliJ IDEA 中 pom.xml 文件内容，其中包含 Activiti7 的 Spring Boot Starter 依赖。
画面 12: 展示 Windows“服务”管理器界面，显示 MySQL 服务状态为“已启动”。
画面 13: 展示 IntelliJ IDEA 中 SecurityUtil.java 文件内容，其中包含 loginAs 方法。
画面 14: 展示 IntelliJ IDEA 中 application.yml 文件内容，其中包含数据库连接配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<project>
    <dependencies>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-spring-boot-starter</artifactId>
            <version>7.0.0.Beta2</version>
        </dependency>
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.4.5</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.7</version>
        </dependency>
    </dependencies>
    <build>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </build>
</project>
```

画面 6:
```java
@Component
public class SecurityUtil {
    @Autowired
    private UserDetailsService userDetailsService;

    public void loginAs(String username) {
        UserDetails user = userDetailsService.loadUserByUsername(username);
        if (user == null) {
            throw new IllegalStateException("User " + username + " doesn't exist, please provide a valid user name.");
        }
        SecurityContextHolder.setContext(new SecurityContextImpl(new Authentication() {
            @Override
            public Collection<? extends GrantedAuthority> getAuthorities() { return user.getAuthorities(); }
            @Override
            public Object getCredentials() { return user.getPassword(); }
            @Override
            public Object getDetails() { return user; }
            @Override
            public Object getPrincipal() { return user; }
            @Override
            public boolean isAuthenticated() { return true; }
            @Override
            public void setAuthenticated(boolean b) throws IllegalArgumentException {}
        }));
    }
}
```

画面 8:
```java
@Configuration
public class DemoApplicationConfiguration {
    @Bean
    public UserDetailsService myUserDetailsService() {
        InMemoryUserDetailsManager inMemoryUserDetailsManager = new InMemoryUserDetailsManager();
        String[][] usersGroupsAndRoles = {
            {"salboby", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
            {"erdmdeiros", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
            {"other", "password", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
            {"admin", "password", "ROLE_ACTIVITI_ADMIN", "GROUP_adminTeam"}
        };
        for (String user : usersGroupsAndRoles) {
            List<String> authoritiesStrings = Arrays.asList(Arrays.copyOfRange(user, 2, user.length));
            logger.info("> Registering new user: " + user[0] + " with the following Authorities: " + authoritiesStrings + "]");
            inMemoryUserDetailsManager.createUser(new User(user[0], passwordEncoder().encode(user[1]), authoritiesStrings.stream().map(s -> new SimpleGrantedAuthority(s)).collect(Collectors.toList())));
        }
        return inMemoryUserDetailsManager;
    }
}
```

画面 9:
```java
public void configure(AuthenticationManagerBuilder auth) throws Exception {
    auth.userDetailsService(myUserDetailsService());
}
```

画面 14:
```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/activiti?useUnicode=true&characterEncoding=utf8&autoReconnect=true&failOverReadOnly=false&maxReconnects=10
    username: root
    password: root
    driver-class-name: com.mysql.jdbc.Driver
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“SpringBoot 整合 Activiti7 的”，内容为整合步骤列表。
画面 3: PPT 标题为“3.1 SpringBoot 整合 Activiti7 的”，内容与画面 1 相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
