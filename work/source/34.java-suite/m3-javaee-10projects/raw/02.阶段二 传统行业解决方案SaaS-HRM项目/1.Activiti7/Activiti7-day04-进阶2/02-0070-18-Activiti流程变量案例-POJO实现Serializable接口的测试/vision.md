# 画面线理解：18-Activiti流程变量案例-POJO实现Serializable接口的测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\18-Activiti流程变量案例-POJO实现Serializable接口的测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:04, 00:08, 00:13, 00:29, 00:35, 00:53, 01:08, 01:46, 01:58, 02:05, 02:08, 02:12, 02:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:03:43

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中通过 Java 代码创建流程实例、设置流程变量，并通过 TaskService 完成任务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 VariableTest.java 文件中通过 TaskService 创建并完成任务的代码。
- 代码注释说明了各步骤：1. 获取 ProcessEngine；2. 获取 TaskService；3. 查询当前用户任务；4. 若任务不为空则完成任务并打印日志。

画面2：
- 展示了 VariableTest.java 文件中通过 RuntimeService 启动流程实例并设置变量的代码。
- 代码注释说明了各步骤：1. 获取 ProcessEngine；2. 获取 RuntimeService；3. 定义流程键和变量 Map；4. 创建 Holiday 对象并放入 Map；5. 启动流程实例并打印流程信息。

画面3：
- 展示了 VariableTest.java 文件中通过 RuntimeService 启动流程实例并设置变量的代码。
- 代码注释说明了各步骤：1. 获取 ProcessEngine；2. 获取 RuntimeService；3. 定义流程键和变量 Map；4. 创建 Holiday 对象并放入 Map；5. 启动流程实例并打印流程信息。

画面4：
- 展示了 Holiday.java 文件的内容，定义了一个实现 Serializable 接口的 Holiday 类，包含 id、holidayName、beginDate、endDate、num、reason、type 等字段及 getter/setter 方法。

画面5：
- 展示了 VariableTest.java 文件中通过 RuntimeService 启动流程实例并设置变量的代码。
- 代码注释说明了各步骤：1. 获取 ProcessEngine；2. 获取 RuntimeService；3. 定义流程键和变量 Map；4. 创建 Holiday 对象并放入 Map；5. 启动流程实例并打印流程信息。

画面6：
- 展示了 VariableTest.java 文件中通过 RuntimeService 启动流程实例并设置变量的代码。
- 代码注释说明了各步骤：1. 获取 ProcessEngine；2. 获取 RuntimeService；3. 定义流程键和变量 Map；4. 创建 Holiday 对象并放入 Map；5. 启动流程实例并打印流程信息。

画面7：
- 展示了 VariableTest.java 文件中通过 RuntimeService 启动流程实例并设置变量的代码。
- 代码注释说明了各步骤：1. 获取 ProcessEngine；2. 获取 RuntimeService；3. 定义流程键和变量 Map；4. 创建 Holiday 对象并放入 Map；5. 启动流程实例并打印流程信息。

画面8：
- 展示了 VariableTest.java 文件中通过 RuntimeService 启动流程实例并设置变量的代码。
- 代码注释说明了各步骤：1. 获取 ProcessEngine；2. 获取 RuntimeService；3. 定义流程键和变量 Map；4. 创建 Holiday 对象并放入 Map；5. 启动流程实例并打印流程信息。

画面9：
- 展示了 Holiday.java 文件的内容，定义了一个实现 Serializable 接口的 Holiday 类，包含 id、holidayName、beginDate、endDate、num、reason、type 等字段及 getter/setter 方法。
- 同时显示了控制台日志，记录了数据库连接、事务提交等信息。

画面10：
- 展示了 Holiday.java 文件的内容，定义了一个实现 Serializable 接口的 Holiday 类，包含 id、holidayName、beginDate、endDate、num、reason、type 等字段及 getter/setter 方法。
- 同时显示了控制台日志，记录了数据库连接、事务提交等信息。

画面11：
- 展示了 Holiday.java 文件的内容，定义了一个实现 Serializable 接口的 Holiday 类，包含 id、holidayName、beginDate、endDate、num、reason、type 等字段及 getter/setter 方法。
- 同时显示了控制台日志，记录了数据库连接、事务提交等信息。

画面12：
- 展示了 Holiday.java 文件的内容，定义了一个实现 Serializable 接口的 Holiday 类，包含 id、holidayName、beginDate、endDate、num、reason、type 等字段及 getter/setter 方法。
- 同时显示了控制台日志，记录了数据库连接、事务提交等信息。

画面13：
- 展示了 Holiday.java 文件的内容，定义了一个实现 Serializable 接口的 Holiday 类，包含 id、holidayName、beginDate、endDate、num、reason、type 等字段及 getter/setter 方法。
- 同时显示了控制台日志，记录了数据库连接、事务提交等信息。

画面14：
- 展示了 Holiday.java 文件的内容，定义了一个实现 Serializable 接口的 Holiday 类，包含 id、holidayName、beginDate、endDate、num、reason、type 等字段及 getter/setter 方法。
- 同时显示了控制台日志，记录了数据库连接、事务提交等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
public class VariableTest {
    public static void main(String[] args) {
        //1.获取ProcessEngine
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取TaskService
        TaskService taskService = processEngine.getTaskService();
        //3.查询当前用户是否有任务
        String key = "myProcess_1";
        Task task = taskService.createTaskQuery().processDefinitionKey(key)
                .taskAssignee("zhaoliu").singleResult();
        //4.如果task!=null,说明当前用户有任务
        if(task!=null){
            taskService.complete(task.getId());
            System.out.println("任务执行完毕");
        }
    }
}
```

画面2：
```java
public static void main(String[] args) {
    //1.获取ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值为 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(5F);
    map.put("holiday",holiday);
    //4.启动流程实例，并且设置流程变量的值
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
    //5.输出实例信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
}
```

画面3：
```java
public static void main(String[] args) {
    //1.获取ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值为 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(5F);
    map.put("holiday",holiday);
    //4.启动流程实例，并且设置流程变量的值
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
    //5.输出实例信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
}
```

画面4：
```java
package com.ithemo.day04;

import java.io.Serializable;
import java.util.Date;

/**
 * 请实现Serializable接口，否则在存储这个pojo时就会报错
 */
public class Holiday implements Serializable {
    private Integer id;
    private String holidayName;//申请人名字
    private Date beginDate;//开始日期
    private Date endDate;//结束日期
    private Float num;//请假天数
    private String reason;//事由
    private String type;//请假类型

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getHolidayName() {
        return holidayName;
    }
}
```

画面5：
```java
public static void main(String[] args) {
    //1.获取ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值为 myProcess_1
    String key = "myProcess_1";
    Map<String, Object> map = new HashMap<>();
    Holiday holiday = new Holiday();
    holiday.setNum(5F);
    map.put("holiday",holiday);
    //4.启动流程实例，并且设置流程变量的值
    ProcessInstance processInstance = runtimeService.startProcessInstanceByKey(key, map);
    //5.输出实例信息
    System.out.println(processInstance.getName());
    System.out.println(processInstance.getProcessDefinitionId());
}
```

画面6：
```java
public static void main(String[] args) {
    //1.获取ProcessEngine
    ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    //2.获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    //3.流程定义的key值为
