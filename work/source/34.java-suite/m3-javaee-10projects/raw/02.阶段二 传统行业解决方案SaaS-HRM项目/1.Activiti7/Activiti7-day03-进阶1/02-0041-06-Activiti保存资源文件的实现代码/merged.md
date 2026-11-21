# 06-Activiti保存资源文件的实现代码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\06-Activiti保存资源文件的实现代码_【海量资源尽在 ubkz.com】.mp4
- 时长 11分44秒（音频 704s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们就把具体的步骤所对应的代码一起来实现一把我们先来看第一个步骤就是得到我们的Process Engine的对象叫做Process Engine它怎么去得到呢我们可以通过Process Engine之里头的Get Default Process Engine下一个步骤我们就可以去
[00:26] 得到我们的这个report Service对吧report Service我们可以通过啊processengine.getreport Service这样我们就可以得到一个repositreport Service对吧就他啊姓名字叫这个那下一步我们就可以得到我们的这个process叫做process process啊叫definitionprocess definition query对象对吧我们一样可以通过调用他的curate啊
[00:56] Process Definition Queue类于是我们就可以生成出一个Process Definition Queue类的对象下一个步骤我们就应该针对它进行条件的设置这个条件设置我们可以还通过Process Definition Queue类去设置它的流程定义的P我们就可以通过这个方法底头去写上注意这个参数是什么
[01:26] 参数是我们的流程定义的key那这个流程定义的key因为我们是一套请假的流程所以我们这张可以写上我们请假这套流程的唯一的key比如说叫做holary那下一个步骤我们就可以再去执行我们的查询操作对吧那因为我们这里头目前部署的流程只有唯一的一套对吧
[01:54] 只有唯一的一套请假流程所以我可以用single result通过single result一查肯定结果就是唯一的一个流程的定义信息这样我们就查到了我们的具体的流程定义信息通过流程定义信息我们就可以进一步去得到它的流程部署的ID部署ID又如何去得到比如说我可以这样去做
[02:20] 我们可以通过我们的Process Defonition里头有一个叫做Get Deployment ID这样我们就拿到了部署的ID号而它是一个实践类型比如说就直接起名字叫做Deployment ID好这样我们就完成了我们的Deployment ID的查询查到Deployment ID下一个环节我们就可以来实现一把叫做Input Stream
[02:49] 比如说我们这里头有png的一个文件流那这个文件流怎么去得到注意这是我们今天新学的一个方法reported Service里头有一个叫做get resource as stream有一个这样的方法这个方法我们一看就能够看出来它需要传两个string类型对吧那第一个string和第二个string的这个参数分别代表什么好我们现在一起针对于我们的get report
[03:19] getResourceAsStream这个方法方法的参数说明方法的参数说明那我们的第一个参数第一个参数代表的是什么含义呢我们的第一个参数代表的是我们的部署ID就是我们的部署ID而第二个参数代表什么意思呢第二个参数
[03:48] 第二个参数在这里边我们要写的是我们的这个流程真正的这个图片的名字就是叫做第二个参数代表我们的这个资源名称这就是这两个参数现在我们就可以一起来搞一把其中第一个我们这个deployment ID其中我们刚才都已经生成了
[04:16] 那第二个参数是什么呢我们在这要说了是呃possessdefinition我们假说是png的话我们就可以有一个get叫做dgramresourcename这就是我们的这个dgram图嘛对吧图资源的名字那这样这个方法其实代表的就是获取我们的这个图片资源的名称啊所以呢这个方法啊代表获取图片
[04:45] 获取啊就是我们的这个png啊图片资源啊的名称是这个意思啊好这样我们的基本上啊就完成了我们的这个图片资源的获取对吧那就按照这个名字来就可以啊可以换一换啊然后呢我们这个时候再走啊那我还可以进一步再去得到一个新的这个新的这个流信息
[05:15] 那这个流信息其实就是我们的这个BPMN文件那BPMN文件所对应的所对应的后边的这个方法要注意一下啊它就不是叫getDigramResourceName你想想我们这个点get的方法各位呢我们在这里头还有一个叫做getResourceName的这个方法getResourceName的这个方法
[05:42] 就可以获取到我们的 BPMN 文件的资源名称这个方法是代表获取我们的 BPMN 文件的名称这个意思好这样我们就完成了我们的
[06:10] 输入流两个工作就做完了那下一步我们就可以来构建我们的这个输出流对吧那输出流又是怎么去构建啊我们这一次要注意啊根据我们早期啊给各位分析的这个思路我们是打算把这个具体的文件存到这个资料目录下去对不对所以呢我从这上面把这个路径烤下来然后现在我们就开始来构造我们的这个alt
[06:40] 那我主要是一个比如说我我们这边也是来一个啊叫做png的啊png的os等于然后真正去new一个文件的output的视频这是我想做的啊用一个fail output的视频然后具体这里边就应该把我们把我们的这个路径给它写写入进来吧然后还有一个就是啊
[07:06] 在这个资料目录下你真正期望它起一个什么样的名字对吧那这样我们也双杠给它隔开然后再去加上一个参数那你想你原来叫什么名字我就叫什么名字对吧所以我们如果说我们的这个PNG文件原来在数据库里头存的是一个什么样的名字那我这一次我期望也想用这个名字这就是这一次我们大致的这个
[07:35] 思路思路就是这样的啊所以呢这就我们完成了第一个工作啊当然我们这边呢我们这边需要去加入一个这个这个这个这个老包对吧我们要干干完一件这样的事情啊然后呢我们不管这个输出流啊不管不光是有这一个对不对我们应该还有一项啊还有一项那这个时候我就可以再次给他拿过来啊那就是比如说我们就来一个叫
[08:06] BPMN文件的一个输出流同样我们这边就可以把这个Dgram这个单词给它弄掉对吧弄掉好我们这时候再来看一下叫做GetResourceLamb这样我们就得到了我们的BPMN文件的名称我们的输入流和输出流都已经构建出来了现在其实我们打算用的是comos-io包里头的方法comos-io.xx这个版本
[08:37] 中的方法来实现我们的这个文件的读写这样我们就可以免去程序员自己去做这样的工作那注意啊我这边这个讲义里头呢给各位提供的这个方法呢他是直接自己去读对吧那这个方法其实已经被人家封装了所以如果我们引入了commo.io的情况下那我们这个工作是非常简单就可以做那其中这里面就提供有一个叫做IO油条丝
[09:06] 里头有一个这样的方法叫点点点copyIOU条式点看一下点copy点copyIOU我看看是不是我在这个过程中导脱了包我们可以再检查一下来看一下我们这边呢提供的这个IOU条式这里上面
[09:44] 目前是没有导包对吧下面我们就直接把导包的工作给它做了IOU跳试就是一个方法这个地方我们应该用的是比如说我就直接来一个IOU跳试点点copy我们这两个参数应该一个是pngis还有一个是alt叫做pngos对吧
[10:15] 这样我们就完成了具体的这行编写下一个工作我们一样的也可以通过我们这个IOU条式但是要注意我们的这个IOU条式真正的这个方法来源应该是来源于IOU条式.topic然后我们就应该写的是我们的这个BPMIS然后是BP
[10:46] mmos 对吧这样我们就完成了这个输入流输出流啊那最后一个环节啊就是我们的这个呃dime关闭流资源对吧那关闭流资源呢一般我们是先关这个输出流啊输出流那我们就可以比如说 pngos 啊点 close 一下啊然后呢我们的这个呃ppmmos 啊点 close 一下对吧然后呢我们的
[11:15] 下一个步骤我们就可以来叫做 pngis.prod一下然后下一个就是 bpmnis.prod一下对吧那这就是我们大致上的实现的思路就是这样的但你发现它这个过程中是有异常的对吧那我们现在可以在这个方法上面去加一个这样的签住就可以了对吧这样我们基本上就完成了我们的具体的编码工作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

