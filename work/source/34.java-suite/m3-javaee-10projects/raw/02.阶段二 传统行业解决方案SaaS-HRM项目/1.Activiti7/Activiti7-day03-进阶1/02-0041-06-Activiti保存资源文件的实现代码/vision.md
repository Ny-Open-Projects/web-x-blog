# 画面线理解：06-Activiti保存资源文件的实现代码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\06-Activiti保存资源文件的实现代码_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:39, 01:56, 02:29, 04:23, 05:12, 06:34, 07:37, 08:09, 08:50, 09:29, 09:45, 11:03, 11:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:39:31

1) 这一组画面整体在讲如何通过 Activiti 的 RepositoryService 查询流程定义并导出其 BPMN 图文件。

2) 按时间顺序列出每张画面的要点：
画面1: 代码中初始化 ProcessEngine，并准备获取 RepositoryService。
画面2: 通过 ProcessEngine 获取 RepositoryService。
画面3: 创建 ProcessDefinitionQuery 并设置查询条件 processDefinitionKey 为 "holiday"。
画面4: 执行查询，获取 ProcessDefinition 对象，并获取其 deploymentId。
画面5: 调用 repositoryService.getResourceAsStream 方法，准备获取 BPMN 图文件的输入流。
画面6: 代码中注释说明 getResourceAsStream 方法的两个参数含义。
画面7: 代码中注释说明 getResourceAsStream 方法的两个参数含义。
画面8: 代码中创建 FileOutputStream，准备将 BPMN 图文件写入本地磁盘。
画面9: 代码中创建 FileOutputStream，准备将 BPMN 图文件写入本地磁盘。
画面10: 代码中使用 InputStream 的 read 方法读取资源并写入 OutputStream。
画面11: 代码中注释说明 getResourceAsStream 方法的两个参数含义。
画面12: 代码中注释说明 getResourceAsStream 方法的两个参数含义。
画面13: 代码中注释说明 getResourceAsStream 方法的两个参数含义。
画面14: 代码中使用 FileUtils.copy 方法复制 InputStream 到 OutputStream，并关闭流。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
public class QueryBpmnFile {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.设置查询条件
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置查询条件
        processDefinitionQuery.processDefinitionKey("holiday");//参数是流程定义的key
        //5.执行查询操作，查询出想要的流程定义
        ProcessDefinition processDefinition = processDefinitionQuery.singleResult();
        //6.通过流程定义信息，得到部署ID
        String deploymentId = processDefinition.getDeploymentId();
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.构建出OutputStream流
        //9.输入流，输出流的转换
        //10.关闭流
    }
}
```

画面2:
```java
public class QueryBpmnFile {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.设置查询条件
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置查询条件
        processDefinitionQuery.processDefinitionKey("holiday");//参数是流程定义的key
        //5.执行查询操作，查询出想要的流程定义
        ProcessDefinition processDefinition = processDefinitionQuery.singleResult();
        //6.通过流程定义信息，得到部署ID
        String deploymentId = processDefinition.getDeploymentId();
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.构建出OutputStream流
        //9.输入流，输出流的转换
        //10.关闭流
    }
}
```

画面3:
```java
public class QueryBpmnFile {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.设置查询条件
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置查询条件
        processDefinitionQuery.processDefinitionKey("holiday");//参数是流程定义的key
        //5.执行查询操作，查询出想要的流程定义
        ProcessDefinition processDefinition = processDefinitionQuery.singleResult();
        //6.通过流程定义信息，得到部署ID
        String deploymentId = processDefinition.getDeploymentId();
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.构建出OutputStream流
        //9.输入流，输出流的转换
        //10.关闭流
    }
}
```

画面4:
```java
public class QueryBpmnFile {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.设置查询条件
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置查询条件
        processDefinitionQuery.processDefinitionKey("holiday");//参数是流程定义的key
        //5.执行查询操作，查询出想要的流程定义
        ProcessDefinition processDefinition = processDefinitionQuery.singleResult();
        //6.通过流程定义信息，得到部署ID
        String deploymentId = processDefinition.getDeploymentId();
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.构建出OutputStream流
        //9.输入流，输出流的转换
        //10.关闭流
    }
}
```

画面5:
```java
public class QueryBpmnFile {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.设置查询条件
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置查询条件
        processDefinitionQuery.processDefinitionKey("holiday");//参数是流程定义的key
        //5.执行查询操作，查询出想要的流程定义
        ProcessDefinition processDefinition = processDefinitionQuery.singleResult();
        //6.通过流程定义信息，得到部署ID
        String deploymentId = processDefinition.getDeploymentId();
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.构建出OutputStream流
        //9.输入流，输出流的转换
        //10.关闭流
    }
}
```

画面6:
```java
public class QueryBpmnFile {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.设置查询条件
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置查询条件
        processDefinitionQuery.processDefinitionKey("holiday");//参数是流程定义的key
        //5.执行查询操作，查询出想要的流程定义
        ProcessDefinition processDefinition = processDefinitionQuery.singleResult();
        //6.通过流程定义信息，得到部署ID
        String deploymentId = processDefinition.getDeploymentId();
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.构建出OutputStream流
        //9.输入流，输出流的转换
        //10.关闭流
    }
}
```

画面7:
```java
public class QueryBpmnFile {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.设置查询条件
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置查询条件
        processDefinitionQuery.processDefinitionKey("holiday");//参数是流程定义的key
        //5.执行查询操作，查询出想要的流程定义
        ProcessDefinition processDefinition = processDefinitionQuery.singleResult();
        //6.通过流程定义信息，得到部署ID
        String deploymentId = processDefinition.getDeploymentId();
        //7.通过repositoryService的方法，实现获取图片信息及bpmn文件信息(输入流)
        //8.构建出OutputStream流
        //9.输入流，输出流的转换
        //10.关闭流
    }
}
```

画面8:
```java
public class QueryBpmnFile {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.获取RepositoryService对象
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.设置查询条件
        ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
        //4.设置查询条件
        processDefinitionQuery.processDefinitionKey("holiday");//参数是流程定义的key
        //5.执行查询操作，查询出想要的流程定义
        ProcessDefinition processDefinition = processDefinitionQuery.singleResult();
        //6
