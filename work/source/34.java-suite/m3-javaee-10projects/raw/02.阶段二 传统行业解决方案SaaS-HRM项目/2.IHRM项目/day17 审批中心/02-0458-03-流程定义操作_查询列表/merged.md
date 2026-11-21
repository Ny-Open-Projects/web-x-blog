# 03-流程定义操作：查询列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\03-流程定义操作：查询列表_【海量资源尽在 ubkz.com】.mp4
- 时长 5分47秒（音频 347s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好 那么我们接下来呢就可以通过Activity内置的一些API咱们完成流程定义这个对象的查询以及对它进行挂起和激活的这些操作那首先我们来看第一项那对于这个查询所有已定义的这些流程呢我们可以通过Activity提供的一个内置对象叫做Repository Service
[00:28] 那在之前的课程当中各位应该已经学过了Report Series其实可以理解为一个资源的一个对象可以通过这个对象咱们查询出Activity当中的一些内置的一些属性好了我们回到咱们的代码部分首先我们通过单元测试类的形式一起来看一下我们已经定义的这些流程怎么给它查询出来那在这边我去定义对应的一个单元测试类好了
[00:57] 通过其中的一个Ctrl C,Ctrl V,call一份吧好了起一个名字呢PoCESS,PoCESSOK好了那接下来在里面呢我们需要注入Repository Service提供的查询的Service好了这个呢就叫做Repository ServiceR E P O S I T O R YRepositoryS E R V I C Z好了那我们
[01:32] 把这个代码呢补充一下reported Service好了那接下来里面的内容呢咱们先把它删掉那接下来呢咱们现在先去测试一个就是测试测试查询所有的流程定义对象咱们先来查询那查询的话at test public view id我们叫做finder all
[02:01] 那对于这个查询所有的零成定义对象那我们可以借助Repository Service那通过这个Service我们开始构建一个查询对象那查询什么的对象就叫做Process Definition Query各位看到了吧好了那这样一来我们构建了一个流程定义的可以把它理解为查询器那这个流程定义查询器我们构建好了之后那接下来那我们查询这些所有定义好的这些流程那有没有
[02:32] 条件呢当然有我们是一个SaaS系统那是不是就要根据咱们之前设置好的这个租户ID来进查询没错吧所以我们接下来就可以添加一些查询条件这个我分开写好了这个第一个我们获取了获取我们流程定义的查询对象query好了那接下来呢我们可以
[02:58] 就是添加一些添加一些查询的叫做条件那添加的查询条件就在query当中往里面设置就可以了好了那query点设置查询条件我们是用的租户ID放进去那注意啊我们现在测试的呢就是传至播客没错吧那设置好了查询条件之后接下来第三个步骤我们其实就可以查询了那这边的查询怎么办就是通过query
[03:30] 这边各位来看各位来看通过query点好了注意那对于在activity当中呢它有很多的版本号那我们查询的肯定是最后一个版本这边呢就设置一下它的版本号继续再来查点list这个比较简单查询的是一个list集合
[03:54] 好了那接下来呢咱们就已经把对应的这些流程呢都已经查询出来了那查询出来之后SOT我们一起打印一下查询出来的这个对象OK那注意这边呢为了各位上课呢看起来更加清晰一点我们通过debug的形式来运行看一下效果好了这边打一段点好了这个启动呢稍微是有一点点慢的各位耐心等待一下
[04:33] 好了现在呢已经启动进来了并且呢已经定位到我们设置断点的位置那注意咱们继续往下走一步来继续走好了各位来看现在呢已经查询出了一个粒子集合那这个粒子集合我们点开来看它的size呢一共有一条没错吧那看到我们数据库各位也能知道里面有一条数据没问题那注意接着打开这一条我们来看一下里面的内容呢其实就是
[05:02] 得到的里面的对象流程定义对象那流程定义有我们的名称好了有我们的描述信息还有一个比较关键的就是我们的流程的这个key唯一的一个key好了接下来里面相应的数据咱们是不是就已经查明出来了那需要各位一定一定要注意的是这边有一个状态某某状态看到了吗那这个某某状态其实描述的就是当前这个流程是否已经被挂起
[05:32] 那如果这个是一的话那指的是一个激活状态或者可用状态如果不是一其实就变成的是一个挂体状态OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
     * 注入activiti提供的Service
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

