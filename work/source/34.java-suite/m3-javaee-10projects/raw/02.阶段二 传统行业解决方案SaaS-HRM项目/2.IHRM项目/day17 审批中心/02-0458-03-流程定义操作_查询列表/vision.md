# 画面线理解：03-流程定义操作：查询列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\03-流程定义操作：查询列表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:45, 01:00, 01:40, 01:58, 02:08, 02:47, 03:27, 03:36, 03:51, 04:13, 04:30, 04:42, 05:01, 05:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:01:24

1) 这一组画面整体在讲如何使用 Activiti 的 RepositoryService 查询流程定义，并通过测试类验证查询结果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 AuditTest.java 文件，其中包含测试方法 test() 和 testActiviti()，用于测试流程组和流程定义的查询。
画面2：IDEA 主界面，显示项目结构，选中 AuditTest.java。
画面3：切换到 ProcessTest.java 文件，准备编写测试类。
画面4：在 ProcessTest.java 中，开始编写测试方法 findALL()。
画面5：使用 repositoryService.createProcessDefinitionQuery() 创建查询对象。
画面6：为查询对象设置租户 ID。
画面7：调用 latestVersion() 方法获取最新版本的流程定义列表。
画面8：在控制台中查看查询结果，输出流程定义的数量。
画面9：调试模式下查看变量值，确认查询结果。
画面10：查看流程定义的详细信息，包括名称、版本、租户 ID 等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
@Test
public void test() {
    List<ProcessGroup> list = processGroupDao.findAll();
    System.out.println(list.size());
}

/**
 * 测试activiti流程库
 * 使用activiti提供的接口测试
 * activiti提供的资源
 */
@AutoWired
private RepositoryService repositoryService;

@Test
public void testActiviti() {
    List<ProcessDefinition> list = repositoryService.createProcessDefinitionQuery().list();
    System.out.println(list.size());
}
```

画面3：
```java
package com.ihrm.audit;
import xxx;
@RunWith(SpringUnit4ClassRunner.class)
public class ProcessTest {

    /**
     * 注入activiti提供的service
     */
    RepositoryService repositoryService;

    @Autowired
    private RepositoryService repositoryService;
}
```

画面5：
```java
ProcessDefinitionQuery query = repositoryService.createProcessDefinitionQuery();
```

画面6：
```java
query.processDefinitionTenantId("仲智摇");
```

画面7：
```java
List<ProcessDefinition> list = query.latestVersion().list();
```

画面8：
```java
System.out.println(list.size());
```

画面9：
```java
query.latestVersion().list();
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
