# 画面线理解：16-Activiti流程部署的zip包方式的补充

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\16-Activiti流程部署的zip包方式的补充_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:35, 01:22, 02:16, 03:07, 03:25, 03:49, 04:51, 05:45, 06:52, 07:31, 08:04, 09:07, 10:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:29:36

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 流程定义部署的两种方式：单个文件部署和压缩包部署，并通过代码演示具体实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面，标题为“6.2.1 什么是流程定义部署”，内容说明将线下定义的流程部署到 Activiti 数据库中，可通过 API 逐个添加 bpmn 和 png 文件，或打包成 zip 部署。
画面2：展示 PPT 页面，标题为“6.2.2 单个文件部署方式”，内容说明分别部署 bpmn 和 png 文件，并展示部分 Java 代码，用于获取 repositoryService 并创建部署对象。
画面3：展示 PPT 页面，标题为“6.2.3 压缩包部署方式”，内容说明将 holiday.bpmn 和 holiday.png 压缩成 zip 包，并展示部分 Java 代码，用于创建 ZipInputStream 并部署。
画面4：展示 Windows 资源管理器，显示 holiday.bpmn、holiday.png 文件，弹出“压缩文件”对话框，提示“请确认是否将此文件夹存入同名 zip 文件”。
画面5：展示 IntelliJ IDEA 编辑器，显示 ActivitiDeployment.java 文件，代码中包含 ProcessEngine 和 RepositoryService 的初始化，以及部署流程的代码。
画面6：展示 IntelliJ IDEA 编辑器，显示 ActivitiDeployment.java 文件，代码中高亮显示了部署流程的代码部分。
画面7：展示 PPT 页面，内容为“定义压缩输入流”和“获取 repositoryService”，并展示部分 Java 代码，用于创建 ZipInputStream。
画面8：展示 IntelliJ IDEA 编辑器，显示 ActivitiDeployment.java 文件，代码中高亮显示了获取 ClassLoader 和创建 InputStream 的部分。
画面9：展示 IntelliJ IDEA 编辑器，显示 ActivitiDeployment.java 文件，代码中高亮显示了创建 ZipInputStream 的部分。
画面10：展示 IntelliJ IDEA 编辑器，显示 ActivitiDeployment.java 文件，代码中高亮显示了创建 Deployment 对象并添加资源的部分。
画面11：展示 PPT 页面，内容为“定义压缩输入流”和“获取 repositoryService”，并展示部分 Java 代码，用于创建 ZipInputStream。
画面12：展示 IntelliJ IDEA 编辑器，显示 ActivitiDeployment.java 文件，代码中高亮显示了部署流程的代码部分。
画面13：展示 MySQL Workbench，显示 SQL 查询窗口，执行了“create database activiti;”和“use activiti;”等语句，并展示部分 SQL 代码，用于创建数据库和表。
画面14：展示 IntelliJ IDEA 编辑器，显示 ActivitiDeployment.java 文件，代码中高亮显示了部署流程的代码部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
将线下定义的流程部署到 activiti 数据库中，这就是流程定义部署，通过调用 activiti 的 api 将流程定义的 bpmn 和 png 两个文件一个一个添加部署到 activiti 中，也可以将两个文件打包成 zip 包进行部署。
```
画面2：
```
分别将 bpmn 文件和 png 图片文件部署。
@Test
public void deployProcess() {
// 获取repositoryService
```
画面3：
```
// 流程部署对象
Deployment deployment = repositoryService.createDeployment()
.addInputStream("holiday.bpmn", inputStream_bpmn)
.addInputStream("holiday.png", inputStream_png)
.deploy();
System.out.println("流程部署id：" + deployment.getId());
System.out.println("流程部署名称：" + deployment.getName());
```
画面4：
```
压缩文件
请确认是否将此文件夹存入同名 zip 文件？
```
画面5：
```
public class ActivitiDeployment {
    public static void main(String[] args) {
        //1.获取ProcessEngine对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        //2.得到RepositoryService实例
        RepositoryService repositoryService = processEngine.getRepositoryService();
        //3.执行部署
        Deployment deployment = repositoryService.createDeployment()
                .addClasspathResource("diagram/holiday.bpmn") //添加.bpmn文件
                .addClasspathResource("diagram/holiday.png") //添加.png文件
                .name("请假申请流程")
                .deploy();
        //4.输出部署的一些信息
        System.out.println(deployment.getName());
        System.out.println(deployment.getId());
    }
}
```
画面6：
```
//1.获取ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.执行部署
Deployment deployment = repositoryService.createDeployment()
        .addClasspathResource("diagram/holiday.bpmn") //添加.bpmn文件
        .addClasspathResource("diagram/holiday.png") //添加.png文件
        .name("请假申请流程")
        .deploy();
//4.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```
画面7：
```
// 定义压缩输入流
InputStream inputStream = this
        .getClass()
        .getClassLoader()
        .getResourceAsStream(
                "diagram/holiday.zip");
ZipInputStream zipInputStream = new ZipInputStream(inputStream);
// 获取repositoryService
RepositoryService repositoryService = processEngine
        .getRepositoryService();
// 流程部署
Deployment deployment = repositoryService.createDeployment()
        .addZipInputStream(zipInputStream)
        .deploy();
System.out.println("流程部署id：" + deployment.getId());
System.out.println("流程部署名称：" + deployment.getName());
```
画面8：
```
//1.获取ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.转化成InputStream流
InputStream is = this.getClass().getClassLoader().getResourceAsStream("diagram/holiday.bpmn");
//4.执行部署
Deployment deployment = repositoryService.createDeployment()
        .addClasspathResource("diagram/holiday.bpmn") //添加.bpmn文件
        .addClasspathResource("diagram/holiday.png") //添加.png文件
        .name("请假申请流程")
        .deploy();
//4.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```
画面9：
```
//1.获取ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.转化成InputStream流
InputStream is = ActivitiDeployment.class.getClassLoader().getResourceAsStream("diagram/holiday.bpmn");
ZipInputStream zipInputStream = new ZipInputStream(is);
//4.执行部署
Deployment deployment = repositoryService.createDeployment()
        .addZipInputStream(zipInputStream)
        .name("请假申请流程")
        .deploy();
//4.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```
画面10：
```
//1.获取ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.转化成InputStream流
InputStream is = ActivitiDeployment.class.getClassLoader().getResourceAsStream("diagram/holiday.bpmn");
ZipInputStream zipInputStream = new ZipInputStream(is);
//4.执行部署
Deployment deployment = repositoryService.createDeployment()
        .addZipInputStream(zipInputStream)
        .name("请假申请流程")
        .deploy();
//4.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```
画面11：
```
// 定义压缩输入流
InputStream inputStream = this
        .getClass()
        .getClassLoader()
        .getResourceAsStream(
                "diagram/holiday.zip");
ZipInputStream zipInputStream = new ZipInputStream(inputStream);
// 获取repositoryService
RepositoryService repositoryService = processEngine
        .getRepositoryService();
// 流程部署
Deployment deployment = repositoryService.createDeployment()
        .addZipInputStream(zipInputStream)
        .deploy();
System.out.println("流程部署id：" + deployment.getId());
System.out.println("流程部署名称：" + deployment.getName());
```
画面12：
```
//1.获取ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.转化成InputStream流
InputStream is = ActivitiDeployment.class.getClassLoader().getResourceAsStream("diagram/holiday.bpmn");
ZipInputStream zipInputStream = new ZipInputStream(is);
//4.执行部署
Deployment deployment = repositoryService.createDeployment()
        .addZipInputStream(zipInputStream)
        .name("请假申请流程")
        .deploy();
//4.输出部署的一些信息
System.out.println(deployment.getName());
System.out.println(deployment.getId());
```
画面13：
```
DROP DATABASE IF EXISTS activiti;
CREATE DATABASE activiti;
USE activiti;
```
画面14：
```
//1.获取ProcessEngine对象
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
//2.得到RepositoryService实例
RepositoryService repositoryService = processEngine.getRepositoryService();
//3.转化成InputStream流
InputStream is = ActivitiDeployment.class.getClassLoader().getResourceAsStream("diagram/holiday.bpmn");
