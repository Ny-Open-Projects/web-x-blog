# 07-Activiti保存资源文件的效果展示

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\07-Activiti保存资源文件的效果展示_【海量资源尽在 ubkz.com】.mp4
- 时长 2分5秒（音频 126s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们仔细观察这时候各位可以看到我们在刚才所编写的代码里头已经有一些问题其中第一个问题就是我们的PNGIS各位可以观察我们的PNGIS是因为这个i写成了小写这是一个低级的错误这个是我们一眼就可以看出来的除了这个错我们的copy方法目前依然存在问题这个问题其实也是一个低级的问题
[00:29] 我们可以一起来看一下在我们这一次倒包的时候其实已经倒的不对了倒的是上底下的对吧那我们正常我们应该倒的是Como子底下的IOU调试对吧那各位你要做这个工作我们在加完这个Como子IO的坐标之后最好你刷新一下对吧你刷新一下将来这个地方就可以看到我们的这个Como子IO里头的这个IOU调试工具列它可以来完成
[00:58] 帮助我们完成这个文件的这个文件输出流和输入流的转换工作啊那好下面呢我们就可以直接呢一起来运行看一下我们的这个执行效果啊如果我们成功的话将打开在低盘的这个D03资料目录下看到我们想要的内容对吧那目前D03资料目录下应该是没有这个这个这个文件啊那现在呢我就开始去执行一下啊好我们这个是走
[01:29] 来看一下它的这个执行效果啊好这边已经执行完了啊那执行完我们再回到我们的这个目录下这时候呢各位就可以看到我们的这个两个文件了啊一个是我们的PPPMN文件而另外一个是我们的这个一个是PNG文件一个是BPMN文件啊来看一下这是我们的BPMN文件对吧这是过过节点的信息啊
[01:57] 因为我们做的是一个请假流程吧对吧好我们这个效果啊就展示到这啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码从 Activiti 流程引擎中查询并导出 BPMN 图和 PNG 图片文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Java 代码，通过 repositoryService 获取流程定义的部署 ID 和资源名称，然后创建 InputStream 读取 BPMN 和 PNG 文件。
画面2：代码中高亮显示了 IOException 的异常处理部分。
画面3：展示 Java 代码的导入语句和类注释，说明了从 Activiti 的 jar 包中读取资源文件的方法。
画面4：展示项目依赖库，高亮显示了 commons-io-2.0.0.jar。
画面5：代码中高亮显示了 OutputStream 的创建部分。
画面6：代码中高亮显示了 IOUtils.copy 方法的调用部分。
画面7：展示 Windows 资源管理器，当前目录为空。
画面8：在 IntelliJ IDEA 中右键点击文件，弹出“Run”菜单。
画面9：在 IntelliJ IDEA 中点击“Run”按钮，准备执行 QueryBpmnFile.java。
画面10：程序运行日志显示成功执行，输出了 SQL 语句和连接信息。
画面11：程序运行日志显示执行完成，退出码为 0。
画面12：显示 Windows 系统的“正在加载...”界面。
画面13：展示 Windows 资源管理器，目录中包含 holiday.bpmn 和 holiday.png 两个文件。
画面14：展示 Windows 资源管理器，目录中包含 holiday.bpmn 和 holiday.png 两个文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
//1.执行查询语句，查询出想要的流程定义
ProcessDefinition processDefinition = processDefinitionQuery.singleResult();
//2.通过流程定义，得到部署ID
String deploymentId = processDefinition.getDeploymentId();
//3.通过repositoryService的方法，实现获取图片bpmn文件中（输入流）
//getRepositoryStream方法参数说明：第一个参数是部署ID，第二个参数是图片名称
//processDefinition.getDiagramResourceName() 代表获取png图片文件名称
//processDefinition.getDiagramResourceName() 代表获取bpmn文件名称
InputStream pngIs = repositoryService
        .getResourcesAsStream(deploymentId,processDefinition.getDiagramResourceName());
InputStream bpmIs = repositoryService
        .getResourcesAsStream(deploymentId,processDefinition.getDiagramResourceName());
//4.构建出OutputStream流
OutputStream pngOs = 
        new FileOutputStream(name: "G:\\Activiti7开发计划\\Activiti7-day03\\资料\\"+processDefinition.getDiagramResourceName());
OutputStream bpmOs = 
        new FileOutputStream(name: "G:\\Activiti7开发计划\\Activiti7-day03\\资料\\"+processDefinition.getDiagramResourceName());
//5.输入流，输出流，commons-io.jar中的方法
IOUtils.copy(pngIs,pngOs);
IOUtils.copy(bpmIs,bpmOs);
//6.关闭流
pngOs.close();
bpmIs.close();
```

画面3：
```java
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngines;
import org.activiti.engine.RepositoryService;
import org.activiti.engine.repository.ProcessDefinition;
import org.activiti.engine.repository.ProcessDefinitionQuery;
import org.apache.commons.io.IOUtils;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
//1.
//需求：
//1.从Activiti的act_ge_bytearray表中读取两个资源文件
//2.将两个文件保存到本地
//3.将两个文件保存到本地
//4.将两个文件保存到本地
//5.将两个文件保存到本地
//6.将两个文件保存到本地
//7.将两个文件保存到本地
//8.将两个文件保存到本地
//9.将两个文件保存到本地
//10.将两个文件保存到本地
//11.将两个文件保存到本地
//12.将两个文件保存到本地
//13.将两个文件保存到本地
//14.将两个文件保存到本地
//15.将两个文件保存到本地
//16.将两个文件保存到本地
//17.将两个文件保存到本地
//18.将两个文件保存到本地
//19.将两个文件保存到本地
//20.将两个文件保存到本地
//21.将两个文件保存到本地
//22.将两个文件保存到本地
//23.将两个文件保存到本地
//24.将两个文件保存到本地
//25.将两个文件保存到本地
//26.将两个文件保存到本地
//27.将两个文件保存到本地
//28.将两个文件保存到本地
//29.将两个文件保存到本地
//30.将两个文件保存到本地
//31.将两个文件保存到本地
//32.将两个文件保存到本地
//33.将两个文件保存到本地
//34.将两个文件保存到本地
//35.将两个文件保存到本地
//36.将两个文件保存到本地
//37.将两个文件保存到本地
//38.将两个文件保存到本地
//39.将两个文件保存到本地
//40.将两个文件保存到本地
//41.将两个文件保存到本地
//42.将两个文件保存到本地
//43.将两个文件保存到本地
//44.将两个文件保存到本地
//45.将两个文件保存到本地
//46.将两个文件保存到本地
//47.将两个文件保存到本地
//48.将两个文件保存到本地
//49.将两个文件保存到本地
//50.将两个文件保存到本地
//51.将两个文件保存到本地
//52.将两个文件保存到本地
//53.将两个文件保存到本地
//54.将两个文件保存到本地
//55.将两个文件保存到本地
//56.将两个文件保存到本地
//57.将两个文件保存到本地
//58.将两个文件保存到本地
//59.将两个文件保存到本地
//60.将两个文件保存到本地
//61.将两个文件保存到本地
//62.将两个文件保存到本地
//63.将两个文件保存到本地
//64.将两个文件保存到本地
//65.将两个文件保存到本地
//66.将两个文件保存到本地
//67.将两个文件保存到本地
//68.将两个文件保存到本地
//69.将两个文件保存到本地
//70.将两个文件保存到本地
//71.将两个文件保存到本地
//72.将两个文件保存到本地
//73.将两个文件保存到本地
//74.将两个文件保存到本地
//75.将两个文件保存到本地
//76.将两个文件保存到本地
//77.将两个文件保存到本地
//78.将两个文件保存到本地
//79.将两个文件保存到本地
//80.将两个文件保存到本地
//81.将两个文件保存到本地
//82.将两个文件保存到本地
//83.将两个文件保存到本地
//84.将两个文件保存到本地
//85.将两个文件保存到本地
//86.将两个文件保存到本地
//87.将两个文件保存到本地
//88.将两个文件保存到本地
//89.将两个文件保存到本地
//90.将两个文件保存到本地
//91.将两个文件保存到本地
//92.将两个文件保存到本地
//93.将两个文件保存到本地
//94.将两个文件保存到本地
//95.将两个文件保存到本地
//96.将两个文件保存到本地
//97.将两个文件保存到本地
//98.将两个文件保存到本地
//99.将两个文件保存到本地
//100.将两个文件保存到本地
//101.将两个文件保存到本地
//102.将两个文件保存到本地
//103.将两个文件保存到本地
//104.将两个文件保存到本地
//105.将两个文件保存到本地
//106.将两个文件保存到本地
//107.将两个文件保存到本地
//108.将两个文件保存到本地
//109.将两个文件保存到本地
//110.将两个文件保存到本地
//111.将两个文件保存到本地
//112.将两个文件保存到本地
//113.将两个文件保存到本地

