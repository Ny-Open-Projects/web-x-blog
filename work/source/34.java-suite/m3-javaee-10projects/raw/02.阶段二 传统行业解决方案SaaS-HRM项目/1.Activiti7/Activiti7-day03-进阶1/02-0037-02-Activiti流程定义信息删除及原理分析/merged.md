# 02-Activiti流程定义信息删除及原理分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\02-Activiti流程定义信息删除及原理分析_【海量资源尽在 ubkz.com】.mp4
- 时长 13分38秒（音频 819s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那刚才我们已经完成了我们的这个流程定义的基本信息的一个查询对吧并借助于我们的循环来实现我们流程定义信息的一个输出那现在呢我们就继续往后来思考假如说在我们查询的这套流程里头比如说这里头循环里头有很多套流程定义的时候那我们这个时候就可以根据自己的情况对不对比如说其中有某一套流程
[00:27] 我认为现在这套流程已经不需要了或者说这套流程已经过时了对吧我们公司决定不再使用这套流程那这个时候我们就有必要怎么办呢来把这一套流程定义删掉对吧那现在我们就一起来学习一下如何去删除一套流程定义信息因为我们的这个流程一旦发布进来的时候一旦部署进来的时候我们这里边就会存储有我们的这一套
[00:56] 流程的基本的资源信息当我整个流程定义都不需要的时候那是不是这些表中的数据也意味着要清楚所以现在我们可以一起来学习一下怎么样将我们已经部署成功的流程定义删掉这里的各位可以看到它还是借助于我们的Repository Service
[01:24] 并且去调用里头的delete deployment这个方法就可以完成删除我们现在也可以一起来做一下这个实验好现在我们就回到这边来这个部分我就可以copy再认出一个我把这个名字直接改了这个就直接不是叫做query了我就改成叫deletedelete process definitionOK就放到这了
[01:54] 这里边的代码我也稍微做一些调整比如说我们来看一下第一个这个地方不再是删除我们的流程定义信息了不再是查询了应该是改成我们的删除对吧删除流程定义删除已经部署已经部署的流程定义对于我而言你像这个Repository Service我都没有必要去变它对吧我们变就是把这几个步骤直接
[02:27] 都暂时性给它去掉那去掉下面就需要去加入我们的第三个步骤对吧那就是直接去叫做执行执行删除我们的这个流程定义删除我们的这个流程定义那只需要通过Repository Service里头调用它的这个删除我们的一套流程的部署定义对不对是这个吧Delete
[02:56] deleta deployment但是这个地方你需要藏一个参数这个参数呢代表的是啥意思啊是我们的deployment id那好现在我们再去执行的时候各位同学就会有一个困惑啊就是呢你比如说我这个代码我都写到是比较简单来一个叫deleta deployment问题是这个参数我写什么对不对因为我不知道我们的这个部署id对吧
[03:26] 好那这个地方我给各位写一下参数参数代表我们的流程流程部署的ID因为我们部署的本质不就是在把一套流程定义部署进去吗所以我们现在如果要去删除这一套流程定义的话那你要知道你部署的时候它的部署ID是什么我们的部署ID又去怎么样拿到它
[03:56] 这个各位呢我们再来做一个实验刚才在我们查询我们的这个流程定义信息的时候如果我在后面给各位多加上这么一个输出比如说这人就写上叫做流程部署的ID我呢把流程部署的ID我也想让他输出那这个时候我就可以通过process definition.get我们看看有没有一个叫deployment的ID
[04:25] 如果有这个deployment ID我们输出也就是说我如果先做我们的流程定义信息的查询我这么一查我就一定会拿到一个deployment ID当我把deployment ID拿到了那我这个地方写什么就自然知道了当然啊我们也可以把这两个过程是活在一起啊比如说如果你要合在一起的话啊那就应该是我们的这个查询啊以及我们的这个便利的工作应该是放在这
[04:55] 还得放到这上面来对吧因为你便利完了之后将来是如果如果你便利完了就相当于要把这一行代码直接挪到哪里头挪到这里边来对不对挪到这里边所以说我查到一个流程定义信息那行我就给你删掉了对吧这样是可以的我们呢干脆就直接这样做你看啊先呢我把这个代码跑一下因为我把这个代码一旦跑完那我们的这个部署的ID号就拿到了
[05:24] 那部署的ID号拿到了那我这个地方填什么的问题我就已经很明确了只要把我们刚才查到的我们的部署ID号是1只要把1写到这里面来我们的流程我们的流程的部署信息以及流程定义的一些资源文件的信息将来就会通通被删掉我们也可以做一下测试现在我们来观察我们原来早期的这张表中
[05:54] 是不是有记录啊这表有记录这个property表原来是一直都有记录的啊我们也思考一下啊当我把这个流程定义部署信息给它删掉deployment是不是就没了那我们的流程定义信息呢对吧那我们主要就是观察这样的一些表RU的表我们已经说过我们的流程一旦跑完这些表就会全都变空了现在问题是我们的HI的这一堆表是否
[06:24] 当我们把这个流程的定义信息部署信息都删掉了那我们HR的这一堆信息是否也要被删掉呢对吧注意啊我这个流程应该是刚才我已经被清空了我清空了然后清空了之后呢我们并没有去走这个具体的流程啊为啥呢各位同学你要注意一下我们这个表里头昨天看的这些基础数据现在一个都没了
[06:53] 没有的具体原因是什么我给各位分析一下是我们今天开始在这边是不是又用这一副文件压缩文件的方式我们又部署来流程的然后在做这个工作之前我开始提前把它全都给它全都给它删了就是我们做这个工作的时候用这一副文件做这个部署的时候我们其实很多
[07:20] 用它做部署的时候我们那时候好像是把这个数据库表中的所有数据都清空了啊所以现在我们只有这个流程的这个流程定义的一些信息啊以及我们的这个流程部署的一些信息但是这个部署呢并没有真正的去走我们的这个流程真正去执行我们的每一个流程啊所以你发现现在还是请假当对吧张商做请假当对吧这是这个原因啊
[07:50] 那如果说有的时候我们希望能够看到我们的这个历史记录表中将来有记录而且呢我们要确定当我这个流程被删除的时候我们就是说这个流程定义信息被删除的时候我们原来的这一堆历史记录表中的这一堆数据是否也会被删除对吧但是因为现在我们这些表中没有任何的记录所以呢现在我们看不出效果
[08:17] 为了达到这个效果我有必要做一个重复性的工作就是啥呢我们需要把我们的这个start instance这个代码就重新让它跑一下对吧好这个时候我们直接再执行一下那各位同学这个时候你就可以看到我们的这个start instance已经启动了对吧那如果你再去观察的话我们很多表中就已经有记录了比如说你再去观察这个表中就有记录了然后这个表中就也开始有记录了那我们现在呢就开始啊
[08:51] 可以再把我们昨天写过的代码再去跑一次比如说我们这个时候就直接可以上来说张三李四王五都去完成一把自己的任务就可以了对吧好这时候我呢就可以啊我直接先这么做吧那我们的这个张三就完成自己的任务看起来好我们这个时候再测一下啊走张三完成自己的任务这个时候张三就完成任务了然后我们再去走啊那就是
[09:25] 李四对吧李四完成自己的任务这时候再执行一下李四就完成任务了好然后再去走就是我们的王武完成任务那这样的话我们又恢复到我们原来刚才这个参数好这时候我们再去看呢王武完成任务了那王武完成任务了那我们应该说这个表中所有的记录就会更多了对吧部门经理总经理这样的一些内容就全都上来了
[10:00] 我们恢复了早期我们想要的这样的一些数据对吧那问题是什么啊现在我们要做一个思考的工作就是当我们的这个流程的这个定义信息部署信息全都被删除的时候就是这个信息被删除的时候我们是否也会把HI开头的这一堆表中的历史记录被删除的对吧
[10:27] 那我们现在可以重新再回到我们的deleted process definition中来做一个测试我们来看一下效果好这个工作就做完了这个工作做完了我们现在就要观察我们这些表又是有哪些表将来会受到影响比如说我们做流程定义信息删除的时候这张表就被删掉了那意思就是我们的这个beta rate这个里头所存的png图片
[11:04] 和BPMN这两张表这两条记录被删掉了我们再看看PropertyProperty本来就一直就有是我们Aggregate本身的一些信息我们再看看那这个表中的记录会不会删掉吗不会被删掉因为这个流程只要它原来跑完了那我们历史记录就应该给它保存在这里头尽管这个流程将来可能不存在了对吧但是曾经我这个流程经历了哪些步骤我们还是可以知道的
[11:34] 那我们这个时候再往后走那大家会猜一下我的感觉里头就是我们的history历史记录的这些信息应该都会被保存都会被保存这个就好比是什么呢比如说我们现在已经长大成人了那你比如说对于我们这个人的成长经历比如说你的档案信息对吧可能要一直保存在那除非有一天
[12:03] 你这个人已经不存在了你的不存在了你的档案信息可能也还会持续保存比较可为我们这个时候再来看一下再往后走这些历史记录的信息该有的应该说原来有的现在一直也持续会有我们现在来看一下我们的部署信息这时候各位可以看到我们的部署表中的记录都已经被删掉了没有了
[12:34] 那再看看我们的这个流程定义的信息现场表中记录也被删掉了对吧model表一直就没有记录啊好这时候我们可以看到啊我们的这个assist definition这个表中的记录也被删掉了啊这样呢我们基本上就可以确定我们的这个流程定义信息的删除和我们这个流程部署其实对应的影响的表是一模一样的
[13:02] 对吧因为你流程定义信息部署进我们的这个activity的时候是主要把这个定义信息放在这三张表中那现在你说你的定义信息不需要了那时候将来还是从这三张表中去删数据就可以了所以呢我们这一次真正影响的这个删除的时候那我们也写一下背后影响的表那就是这三张表对吧好
[13:33] 我们关于我们的这个流程定义信息的这个删除给各位介绍到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码操作 Activiti 工作流引擎，包括查询、启动、完成任务以及删除流程定义，并展示对应的数据库表结构和操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 显示 IntelliJ IDEA 中的 Java 代码，用于查询流程定义。
- 代码片段：
  ```java
  List(ProcessDefinition) list = processDefinitionQuery.processDefinitionKey("holiday")
  .orderByProcessDefinitionVersion()
  .desc().list();
  ```
  ```java
  for(ProcessDefinition processDefinition : list){
      System.out.println("流程定义ID：" + processDefinition.getId());
      System.out.println("流程定义名称：" + processDefinition.getName());
      System.out.println("流程定义的Key：" + processDefinition.getKey());
      System.out.println("流程定义的版本号：" + processDefinition.getVersion());
  }
  ```
- 控制台输出显示流程定义信息，包括 ID、名称、Key 和版本号。

画面 2:
- 显示 MySQL Workbench 中的 `information_schema` 数据库视图，列出 Activiti 的表结构。
- 表结构注释：
  ```
  act_hi_identitylink 参与者信息
  act_hi_procinst 流程实例
  act_hi_taskinst 任务实例
  act_ru_execution 执行表
  act_ru_identitylink 参与者信息
  act_ru_task 任务
  ```
- 注释说明：处理当前用户的任务，背后操作的表包括 `act_hi_actinst`、`act_hi_identitylink`、`act_hi_taskinst`、`act_ru_identitylink`、`act_ru_task`。

画面 3:
- 显示 IntelliJ IDEA 中的 Java 代码，用于删除流程定义。
- 代码片段：
  ```java
  public static void main(String[] args) {
      //1.得到ProcessEngine对象
      ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
      //2.得到RepositoryService对象
      RepositoryService repositoryService = processEngine.getRepositoryService();
      //3.得到ProcessDefinitionQuery对象，它是一个查询器
      ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
      //4.设置条件，查询出当前的所有流程定义，查询条件：流程定义的key=“holiday”
      //orderByProcessDefinitionVersion() 设置排序方式，根据流程定义的版本号进行排序
      List<ProcessDefinition> list = processDefinitionQuery.processDefinitionKey("holiday")
      .orderByProcessDefinitionVersion()
      .desc().list();
      //5.遍历流程定义信息
      for(ProcessDefinition processDefinition : list){
          System.out.println("流程定义ID：" + processDefinition.getId());
          System.out.println("流程定义名称：" + processDefinition.getName());
          System.out.println("流程定义的Key：" + processDefinition.getKey());
          System.out.println("流程定义的版本号：" + processDefinition.getVersion());
      }
  }
  ```

画面 4:
- 显示 IntelliJ IDEA 中的 Java 代码，用于查询流程定义。
- 代码片段：
  ```java
  List(ProcessDefinition) list = processDefinitionQuery.processDefinitionKey("holiday")
  .orderByProcessDefinitionVersion()
  .desc().list();
  ```
  ```java
  for(ProcessDefinition processDefinition : list){
      System.out.println("流程定义ID：" + processDefinition.getId());
      System.out.println("流程定义名称：" + processDefinition.getName());
      System.out.println("流程定义的Key：" + processDefinition.getKey());
      System.out.println("流程定义的版本号：" + processDefinition.getVersion());
  }
  ```
- 控制台输出显示流程定义信息，包括 ID、名称、Key 和版本号。

画面 5:
- 显示 IntelliJ IDEA 中的 Java 代码，用于删除流程定义。
- 代码片段：
  ```java
  public class DeleteProcessDefinition {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到RepositoryService对象
          RepositoryService repositoryService = processEngine.getRepositoryService();
          //3.执行删除流程定义，参数代表流程部署的id
          repositoryService.deleteDeployment("1");
      }
  }
  ```

画面 6:
- 显示 IntelliJ IDEA 中的 Java 代码，用于查询流程定义。
- 代码片段：
  ```java
  public class QueryProcessDefinition {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到RepositoryService对象
          RepositoryService repositoryService = processEngine.getRepositoryService();
          //3.得到ProcessDefinitionQuery对象，它是一个查询器
          ProcessDefinitionQuery processDefinitionQuery = repositoryService.createProcessDefinitionQuery();
          //4.设置条件，查询出当前的所有流程定义，查询条件：流程定义的key=“holiday”
          //orderByProcessDefinitionVersion() 设置排序方式，根据流程定义的版本号进行排序
          List<ProcessDefinition> list = processDefinitionQuery.processDefinitionKey("holiday")
          .orderByProcessDefinitionVersion()
          .desc().list();
          //5.遍历流程定义信息
          for(ProcessDefinition processDefinition : list){
              System.out.println("流程定义ID：" + processDefinition.getId());
              System.out.println("流程定义名称：" + processDefinition.getName());
              System.out.println("流程定义的Key：" + processDefinition.getKey());
              System.out.println("流程定义的版本号：" + processDefinition.getVersion());
          }
      }
  }
  ```
- 控制台输出显示流程定义信息，包括 ID、名称、Key 和版本号。

画面 7:
- 显示 MySQL Workbench 中的 `information_schema` 数据库视图，列出 Activiti 的表结构。
- 表结构注释：
  ```
  act_hi_identitylink 参与者信息
  act_hi_procinst 流程实例
  act_hi_taskinst 任务实例
  act_ru_execution 执行表
  act_ru_identitylink 参与者信息
  act_ru_task 任务
  ```
- 注释说明：处理当前用户的任务，背后操作的表包括 `act_hi_actinst`、`act_hi_identitylink`、`act_hi_taskinst`、`act_ru_identitylink`、`act_ru_task`。

画面 8:
- 显示 MySQL Workbench 中的 `information_schema` 数据库视图，列出 Activiti 的表结构。
- 表结构注释：
  ```
  act_hi_identitylink 参与者信息
  act_hi_procinst 流程实例
  act_hi_taskinst 任务实例
  act_ru_execution 执行表
  act_ru_identitylink 参与者信息
  act_ru_task 任务
  ```
- 注释说明：处理当前用户的任务，背后操作的表包括 `act_hi_actinst`、`act_hi_identitylink`、`act_hi_taskinst`、`act_ru_identitylink`、`act_ru_task`。

画面 9:
- 显示 IntelliJ IDEA 中的 Java 代码，用于启动流程实例。
- 代码片段：
  ```java
  public class ActivitiStartInstance {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到RuntimeService对象
          RuntimeService runtimeService = processEngine.getRuntimeService();
          //3.创建流程实例，流程定义的key=“holiday”
          ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
          //4.输出流程实例的ID
          System.out.println("流程部署ID：" + processInstance.getDeploymentId());
          System.out.println("流程实例ID：" + processInstance.getId());
          System.out.println("活动ID：" + processInstance.getActivityId());
      }
  }
  ```
- 控制台输出显示流程部署 ID、流程实例 ID 和活动 ID。

画面 10:
- 显示 IntelliJ IDEA 中的 Java 代码，用于完成任务。
- 代码片段：
  ```java
  public class ActivitiCompleteTask {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到TaskService对象
          TaskService taskService = processEngine.getTaskService();
          //3.查询当前用户任务
          Task task = taskService.createTaskQuery()
          .processDefinitionKey("holiday")
          .taskAssignee("wangwu")
          .singleResult();
          //4.处理任务，给当前用户任务列表的查询操作的话，任务ID：task.getId();
          taskService.complete(task.getId());
          //5.输出任务的id
          System.out.println(task.getId());
      }
  }
  ```
- 控制台输出显示任务 ID。

画面 11:
- 显示 IntelliJ IDEA 中的 Java 代码，用于完成任务。
- 代码片段：
  ```java
  public class ActivitiCompleteTask {
      public static void main(String[] args) {
          //1.得到ProcessEngine对象
          ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
          //2.得到TaskService对象
          TaskService taskService = processEngine.getTaskService();
          //3.查询当前用户任务
          Task task = taskService.createTaskQuery()
          .processDefinitionKey("holiday")
          .taskAssignee("lishi")
          .singleResult();
          //4.处理任务，给当前用户任务列表的查询操作的话，任务ID：task.getId

