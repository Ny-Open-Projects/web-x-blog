# 10-Activiti7与SpringBoot整合-bpmn流程定义

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\10-Activiti7与SpringBoot整合-bpmn流程定义_【海量资源尽在 ubkz.com】.mp4
- 时长 11分7秒（音频 667s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好当我们做完了这个activity与我们Spring Boot整合的这个Spring Secure的这个部分之后对于我们而言就是需要去添加我们的BPMN文件那BPMN文件早期我们就直接放在这个resources目录下就可以对吧那各位同学思考一下我们这一次还能直接这么做吗对吧那你是否还想得起我们当时在这个
[00:31] 在讲这个开发文档的时候给各位介绍我们task runtime和我们的这个process runtime的时候我在介绍process runtime的时候个别给各位提了一个点那个点是什么还能想得起来吗那就是说我们的这个流程部署它可以自动帮助我们完成那它怎么样自动帮助我们去完成这个流程的部署呢对吧那我们的BPMN文件放置有没有要求啊
[01:01] 想起来了吗?
[01:03] 应该是在对应的这个位置叫Process Defaults Needed to be pressed inside必须放置在我们的这个目录下哪个目录?
[01:20] 是这个目录下所以我们需要去创建一个这样的目录就是叫做Processes这样的一个目录那我就直接
[01:31] 把我们的目录给它创建出来比如说叫做Processes这样的一个目录在这个目录下面我们可以进一步去创建我们的BPMN文件对不对这样我就可以去创建我们的BPMN文件了比如说我这个地方就直接可以去写一个我们的这一次的BPMN文件比如说我去搞一个叫做叫做我们的 other
[02:01] 或者说我们直接叫做比如说叫做team01叫做ok这样我就有了一个这样的BPMN文件那在这个BPMN文件里头我就可以去把我们早期所学过的内容是不是再给它重复一遍呢start event对吧然后呢我们可以去搞几个这样的用户节点比如说我们在做这个工作的时候首先呢
[02:31] 首先我可以经过我们的start event如果start event把这个工作做好了我们下一步比如说我们这个地方就叫做force的可以吧这是我们的第一个工作那我们的第一个工作如果做好没有任何问题我们将来就可以再去做我们的第二个工作那这个部分我可以再去拖一个比如说在这里来一个second叫second
[02:58] 那完了我们最后我再去加入一个我们的叫做end event对不对这样我们呢只要把这个连线啊给它创建起来那这就是我们的第一个第一个节点啊好这个我再去把这个任务啊重新再扔一下吧这是我们的第一个这是我们第一个到第二个啊好我们再走最后到达我们的这个end event这样我们就基本做完了对不对这个流程定义啊
[03:29] 但我们今天在这里面呢给各位再介绍一个点那这个点也比较简单我们原来一般就是在这个assign部分去指定我们指定的这个任务执行人对不对后续呢我们又给各位讲了一个叫做continued user这个continued user代表的是我们的这个候选用户对吧比如说张商里是玩武比如说你可以在这写一排用逗号隔开对不就可以了比如说这是我们的第一个用户x逗号y逗号z
[03:58] 是不是就相当于XYZ是我们的三个不同的用户对吧这是一种方式除了这种我们还可以有一种叫做Condydeck的Groups这就是我们的用户组我们的用户组将来也是可以直接在这设置的因为我们在用这个Condydeck的User的时候你会发现其实他们就是一组对不对比如说XYZ比如说或者改成张三李四王五赵六对吧那这个就是一组
[04:25] 但是不同的地方是你在这里头必须把它们都列举在这这就不太方便了对不对因为我们很多时候这个用户的信息可能并不是直接在这里写死的因为你写XYZ他是不是也要提前把这三个用户信息给他设置在这里头对不对但是很多时候我只知道你是属于比如说是属于我们公司的管理员或者说你我只知道你们你呢我只知道
[04:53] 将来这个任务是由我们公司的行政这个部门来发布对吧至于到底是行政的哪一个人我并不知道就是说我在这个设置这个组的时候我不知道所以说这个时候用它优势更明显一些那这个部分我们呢要特别注意一下就是我们要去学会区分我们的这个区分我们的这个用户组
[05:21] 比如说我给各位特别标注一下这是我们的用户组的关系我给各位再写一个放在这里面第一个我们将来在设置的时候可以直接去设置assign对不对assign这是直接设置直接设置任务的执行人对不对任务的执行人
[05:50] 除了这个之外我们还有一个就是叫做DIATCandidate-user那这种方式主要就是设置我们的候选用户对吧设置我们的候选用户那候选用户之间他们的这个格式是比如说我将来这里头第一我们可以用王武可以来执行这个任务然后我逗号隔开然后我们张商也可以执行这个任务
[06:20] 对吧然后我们比如说赵六也可以执行这个任务那这样我们将来就是用逗号隔开他们但是这种方式的它对应的特点依然是虽然我们将来一个任务有多过执行人对不对依然相当于依然要指定具体的用户信息对不对
[06:48] 但是有很多时候我们的这个流程真正在跑的时候我并不知道将来这个流程到底是由谁或者说由张三李是王武这三个人的其中一个我不知道那这个时候我们就有必要去设置我们CandyDark的叫做Group这个属性这个属性最大的好处就是它是设置一个组对不对比如说我就知道我们公司的这个
[07:16] 关于流程流程相关的信息发布的都是由公司的行政来指定的它的特点它的特点不需要不需要知道具体具体的用户信息我只知道主名就可以只需要只需要知道主名就可以这是这种方式它的最大的特点是这样的
[07:47] 那对于我们这个项目而言我们的这个组名又是什么呢因为我们开始说过在我们的这两个Split Security类中其中这个类是不是放的是我们用户权限的配置信息那从这个用户权限的配置信息中各位可以看到我们这里头其实是有一个组叫做GroupActivateTeam这就是我们的这个组名还有一个组是叫做OtherTeam
[08:16] 那我打算这次走节点的时候用这两个用这个组用这个组里头的这个用户信息来走那我们写的时候要注意Sprung Secure Rate要求我们如果要去加入组的信息的话必须与Group下滑线开头后面才是真正的组名所以我在这边copy一下然后再回到我们的这个Team01然后就可以去设置我们的这个叫做Con
[08:45] countytech的group子这样我们就设置好了我们的这个组名一样的它这个部分你说也是在这个组里头去找一个人去执行就可以了对吧这样我们基本上就完成了我们的这个用户完成了我们的整个这个流程定义信息在这个部分我们特别的地方就是加入了一个组的概念对吧而这个组的概念这个名字不得是随便起
[09:15] 这个各位一定要注意它对的这个名字一定要对上我们的Spring Securator它的这个主信息对不对对上这个主信息当然你要是用这里头的信息你就可以直接写other team也是可以的好这样我们基本上就完成了我们的这个activity的BPMN文件的制作放在这几个要点第一个是必须有processes目录而且放在这下面
[09:44] 好处是什么呢将来它会自动去把Process文件加下的所有的BPMN文件一并扔到我们的这个Activity所对应的那个数据库表这个这个这个这个这个对应的这个表里面去就扔到这个部署的信息里面去就扔这里头来了啊所以呢这是它好的地方它不好的地方也是很明显啊因为你这么扔的话假如说我这一次
[10:12] 我搞了五套流程其中有一个流程我没开发好还没想好怎么做那对不起他也会跟着一起扔进来所以说他这个部分有好的地方就有不好的地方对不对好的地方就是的确是简单快捷不好的地方就是粗暴对不对管你行不行管你同不同意比如说这里头BPM文件有10个直接就一下给你一并扔进去就是这样来
[10:40] 当然从它的角度来思考也是可以理解你的BPMN文件放在这个位置是不是其实就说明你想扔进去你想扔进去那你就放在这个位置你不想扔进去比如说我就直接在resource里再去搞一个BPMN文件那是不会扔进去的所以这一点过于大家注意好这样我们基本上完成了这个BPMN文件的一个制作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

