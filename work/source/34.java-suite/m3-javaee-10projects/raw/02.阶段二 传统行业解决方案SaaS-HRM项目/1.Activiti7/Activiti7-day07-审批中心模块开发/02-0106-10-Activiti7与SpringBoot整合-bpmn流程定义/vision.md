# 画面线理解：10-Activiti7与SpringBoot整合-bpmn流程定义

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\10-Activiti7与SpringBoot整合-bpmn流程定义_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:37, 00:51, 01:00, 01:34, 01:46, 03:10, 05:11, 06:52, 07:46, 08:21, 09:17, 09:39, 10:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:39:35

1) 这一组画面整体在讲如何在 Spring Boot 项目中配置 Activiti 工作流引擎的用户权限和流程定义。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 IntelliJ IDEA 中打开项目，展示 DemoApplicationConfiguration 类的代码，其中定义了 UserDetailsService 并初始化 InMemoryUserDetailsManager。
画面 2: 在 GitHub 页面查看 Activiti 示例代码，展示如何使用 TaskRuntime API 创建任务，并说明需要 ROLE_ACTIVITI_USER 权限。
画面 3: 在 GitHub 页面查看 ProcessRuntime API 的接口定义，说明其与 TaskRuntime API 类似，也需要 ROLE_ACTIVITI_USER 权限。
画面 4: 在 GitHub 页面查看 ProcessRuntime API 的代码示例，展示如何注入 ProcessRuntime 和 SecurityUtil，并开始使用 ProcessRuntime。
画面 5: 在 IntelliJ IDEA 中，展示创建新文件的菜单，同时显示 DemoApplicationConfiguration.java 文件中定义用户和角色的代码。
画面 6: 在 IntelliJ IDEA 中，展示 application.yml 文件，其中配置了 activiti 的数据库连接信息。
画面 7: 在 Activiti Designer 中，展示一个简单的 BPMN 流程图，包含 StartEvent、UserTask、EndEvent。
画面 8: 在 Windows 资源管理器中，展示 Activiti7-day05 新项目文件夹下的多个 .avi 视频文件。
画面 9: 在记事本中打开“用户组关系.txt”，其中包含关于 Assignee 和 Candidate-user 的说明。
画面 10: 在 Activiti Designer 中，展示流程图，将第一个 UserTask 的 Candidate Groups 设置为 "team01"。
画面 11: 在 IntelliJ IDEA 中，展示 DemoApplicationConfiguration.java 文件，其中定义了用户和角色的数组。
画面 12: 在 Activiti Designer 中，展示流程图，将第一个 UserTask 的 Assignee 设置为 "wangwu"。
画面 13: 在 IntelliJ IDEA 中，展示项目结构，其中 application.yml 文件被选中。
画面 14: 在 MySQL Workbench 中，展示 activiti 的数据库表，其中包含流程定义和部署信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Configuration
public class DemoApplicationConfiguration {
    private Logger logger = LoggerFactory.getLogger(DemoApplicationConfiguration.class);

    @Bean
    public UserDetailsService myUserDetailsService() {
        InMemoryUserDetailsManager inMemoryUserDetailsManager = new InMemoryUserDetailsManager();
        inMemoryUserDetailsManager.createUser(new User("salaboy", "password", new SimpleGrantedAuthority("ROLE_ACTIVITI_USER")));
        inMemoryUserDetailsManager.createUser(new User("ryandamore", "password", new SimpleGrantedAuthority("ROLE_ACTIVITI_USER")));
        inMemoryUserDetailsManager.createUser(new User("eramdaires", "password", new SimpleGrantedAuthority("ROLE_ACTIVITI_USER")));
        inMemoryUserDetailsManager.createUser(new User("other", "password", new SimpleGrantedAuthority("ROLE_ACTIVITI_USER")));
        inMemoryUserDetailsManager.createUser(new User("admin", "password", new SimpleGrantedAuthority("ROLE_ACTIVITI_ADMIN")));
        return inMemoryUserDetailsManager;
    }
```

画面 5:
```java
String[][] usersGroupsAndRoles = {
    {"salaboy", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
    {"ryandamore", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
    {"eramdaires", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
    {"other", "password", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
    {"admin", "password", "ROLE_ACTIVITI_ADMIN", "GROUP_otherTeam"}
};
```

画面 6:
```yaml
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/activiti?useUnicode=true&characterEncoding=utf8&useSSL=false
    username: root
    password: root
```

画面 11:
```java
String[][] usersGroupsAndRoles = {
    {"salaboy", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
    {"ryandamore", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
    {"eramdaires", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
    {"other", "password", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
    {"admin", "password", "ROLE_ACTIVITI_ADMIN", "GROUP_otherTeam"}
};
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7: BPMN 流程图结构：
- StartEvent → UserTask (id: "first")
- UserTask (id: "first") → UserTask (id: "second")
- UserTask (id: "second") → EndEvent

画面 10: BPMN 流程图结构：
- StartEvent → UserTask (id: "first")
- UserTask (id: "first") → UserTask (id: "second")
- UserTask (id: "second") → EndEvent
- UserTask (id: "first") 的 Candidate Groups 设置为 "team01"

画面 12: BPMN 流程图结构：
- StartEvent → UserTask (id: "first")
- UserTask (id: "first") → UserTask (id: "second")
- UserTask (id: "second") → EndEvent
- UserTask (id: "first") 的 Assignee 设置为 "wangwu"

5) 不要评价画面美观，不要输出与课程无关的内容。
