# 20-提交申请：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\20-提交申请：代码实现_【海量资源尽在 ubkz.com】.mp4
- 时长 15分54秒（音频 954s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那现在呢我们已经完成了申请的一个发起那这个申请发起了之后接下来呢咱们就来看最后一项就是叫做提交申请那对于这个提交申请而言呢是这样的就是说啊咱们在页面上可以看到你的这个流程呢可以进行通过驳回如果是你发起的我们这边是不是还可以做撤销这些操作呀
[00:27] 那不管是哪个操作其实我们都叫做提交申请只不过提交的数据不一样而已比如说撤销我们提交的就是说撤销这么一个状态如果说这边驳回那就是驳回一个状态如果这边是通过那其实就是一个通过的这么一个状态而已所以对于我们来说咱们接下来要完成的提交其实很简单就是把
[00:51] 你相应的数据传递到我们的Controller当中接着完成我们的操作就可以了好了那接下来呢咱们可以一起呢打开F12来看一下比如说呢我这边有通过的流程随便填通过一点击确定它发送一个commit那commit过来之后会发送一个handler option代表的是我的中间的通过原因好了handler type
[01:18] 注意这个handler type2代表的是通过那还有handler user id就是处理人的id还有process id就是当前这个流程的id而已那不管是这个还是我们这边的驳回其实都是一样的刚才是2驳回我们再来看这回是不是就变成3了没错吧那同理呢还有这边我撤销我们的请求那撤销同时同样的也是在这边要填写相内容只不过4是一个撤销的一个状态而已
[01:51] 所以呢接下来我要跟各位来聊的就是我们最后要完成的这个提交的这么一个工作那对提交的这个工作而言咱们回到control了补充一个新的方法提交提交审核那提交审核同样的control c拿过来control v拷过来好了这边呢我们请起一个小小的名字呢就叫做就叫做提交吧instance n n s t n
[02:25] 直接从这边抄了IntentsCommit拿过来IntentsCommit接下来咱们的请求方式这边是一个put请求一定要注意接下来我们传递的这些数据注意这边先叫commercate我们这边传递过来的数据是什么其实就是我们这边POC task instance就是我们的任务就是它不管是提交什么什么都是传过来一个任务
[02:56] 那传递过来之后有option能够对应上tab能够对应上user id能够对应上pulse id是不是也能够对应上没错吧所以对于我们而言咱要做的事情呢就是接收一个任务实力的一个对象就可以了任务实力的这么一个对象那接下来我们这边同样也是调用Service只不过这回就是committaskintents传递过来那后面同样有我们的company id能接受吗
[03:28] 好了那接下来呢这个control的代码我们写好了接下来这边呢要说一下我们这里面呢有一个提交的状态就是说呢这边有一个handler type那这个handler type如果是2代表审核通过3审核不通过4撤销没错啦好了那接下来呢在Service当中呢我们可以给它补充一个新的Service方法好了这个Service方法呢咱们就来看一下应该如何去写
[03:58] 首先呢是这样子咱们来看一下它能传递过来的这个对象里面有什么样的参数那对象的参数呢我们回到这边把这一段Ctrl C拷过来Ctrl V拿过来咱们来说明一下好了首先呢上边就是我们的操作说明操作说明其实也就是你的审核原因驳回原因撤销原因好了那这边代表的是我们的处理类型处理类型好了那接下来底下代表的是我们的处理人
[04:30] 那最后一个Pulse ID代表的是我们的业务流程ID有这么几个参数能够拿过来那我们这边要去完成这个审核提交我们应该怎么做那需要各位一定要明确那在我们这边现在给我们传递的是这个Task Instant对象那我们是应该找到上面这个主表把里面的数据做相的处理如果你是撤销我们要把主表状态改成撤销如果是
[05:00] 活回我们改成活回没错吧所以我们要对上面的这个表也要操作那底的这个表我们是不是要把一条数据保存进去是不是就可以了那当了咱们操作了我们表之外呢还要去操作activity为我们准备的这些流程相关的内容那如果是通过了我们开始找下一个流程如果没有通过我们是不是就可以做相当的处理没错吧所以咱们这边呢要有这么一个小小的操作首先呢第一项要去查询我们的
[05:30] 业务流程对象那业务流程对象呢咱们查询了之后接下来第二件事就是设置我们的业务流程的这个状态好了那接下来第三件事那第三件事呢是这样的第三件事呢哎是这样的咱们要做的事情就是根据不同的操作类型完成不同的业务处理
[06:02] 好了如果说呢是这样的如果就是审核是通过那我们这边就获取下一个如果审核通过我们就是完成当前的任务好了那接下来3.2如果是审核不通过或者是撤销那其实不管是撤销还是审核不通过其实对于我们这个流程来说就没有任何的意义了
[06:30] 我们可以就是删除我们的ACTIVITI流程好了这个删除流程不要怕在activity当中我们只是把它的一个当前这个流程实例的表给它删掉了但是具体的业务其实还能够查询到这个没关系因为我们这边如果不通过或者撤销对我们的流程来说activity来说就没什么意义了没错吧所以这个就是我们的相应的一些业务的处理当然了底下这边我们可能要做的第四件事就是
[07:00] 要更新我们的业务业务流程对象保存我们的业务的任务任务任务对象OK那接着咱们开始一起来看首先的第一个查询业务流程对象那查询流程对象呢我们首先呢获取到这个Prosess ID等于TaskIntents.getProsess ID没错吧那获取了
[07:30] ID之后我们可以根据DO来进行查询PROC注意instance DO点FindByID把这个ID传进去点Get那这样一来我们得到了相应的对象好了那这个相应的对象我们有了之后那接下来设置它的状态Intense.setState那这个State其实就是你这个传递过来的这个状态就可以了
[08:03] 当然我们这边不叫状态叫做tab没错吧好了那接下来咱们继续往下去看继续往下去看好了那接下来呢就是要根据不同的处理类型咱们完成不同的操作就需要做一个判断if task intents.get这个tab好了注意啊如果是2的话比较特殊这个是一个死剧类型所以我这边就是ecos来做判断好了在上边else在下边
[08:40] OK好了那接下来呢咱们就来看一下这个R呢比较特殊我们先说底下这些那如果审核不通过我们就可以把这个流程呢给它删掉那流程删掉呢需要用到的一个Service就是activity我们准备好了run time Service它跟我们的运行时有关好了run time Service.delete把我们这个year把我们这个流程删掉delete persist intense好了那接下来
[09:14] 那第一个好了这边是PoursesIntents那我们这边传的参数究竟怎么做呢其实这个参数有朋友说直接把这个PoursedID传递过来注意不行这个是我们自己的ID我们要删应该删人家Activity的ID那所以我们这边需要将这边补充一下吧就是查询出ACTI VI TI中的流程实例那查询这个流程实例呢其实也没有那么难啊
[09:46] 好了Service.create流程实例的query点注意我们用什么查好了我们这边用的是business key因为我们之前说过咱们我们自己的表和人家那边的表唯一产生的联系就是我们把我们自己业务表的ID是不是放给了它这个流程实例所以我们这边直接把这个我们自己的ID我们的业务ID拿过去点好了就是
[10:19] single result这样一来得到的是人家的流程实例好了这边我说一下就是根据自己的业务ID去查询ACTI VITI中的流程实例好了所以咱们这边呢要删除就比较简单了点get ID当然了这边呢还有一个参数就是你为什么要删把我们这边的删除原因给它写过来OK好了那这样一来呢咱们这个流程呢上面
[10:51] 删除的咱们已经搞定了接着关注一下审核通过那审核通过这边呢有一个小小的处理了那如果审核通过我们要做的事情好了是这样咱们就以这个任何一个流程为为例啊你现在部门审批人审核通过了那我们要做的事情是不是就是activity调用一下这个方法那接下来就流转到下一个了没错吧那这是一种情况那还有一种情况就是说直接是人事审批是不是直接下面就没有节点了没错吧
[11:21] 所以对于我们这边而言呢那对于我们这边而言咱要做的事情呢就需要做一个处理首先把当前任务节点给它执行完成那接着判断一下有没有下一个节点如果有下一个节点我们现在还是审批中的一个状态如果没有下一个节点我们当前的这个任务是不是才是真真正正的已经审批完成了没错吧
[11:46] 所以呢我们这个代码的写法呢这边相对来说就有一点点麻烦首先第一个查询出当前节点好了接下来呢这边呢再补充上并完成当前节点任务好了那接下来呢如果当前这个节点咱们已经搞定了的话那接下来咱们就查询出下一个任务节点那这边如果存在下一个那这个意味着我们的流程没有结束
[12:19] 如果存在下一点认为你的流程没有结束如果不存在下一个节点代表的是我们的任务任务已经结束了没错了所以我们就开始来看一下先查询当前的这个节点查询当前这个节点呢咱们之前的代码其实已经写过了我就把这个代码拷过来Ctrl C拿到这边来当前节点查询出来那当前节点查询出来之后我们可以
[12:51] 就把这个当前节点呢给它完成掉这个咱们之前代码也写过了完成一个节点任务OK没错了好了那接下来呢底下就是去查询下一个任务节点那下一个任务节点呢跟我们之前的套路都是一模一样的跟我们之前套路都是一模一样的好了这边呢如果不等于NOW代表的是流程没有结束流程没有结束把我们这个流程的状态给它改回来点setstate
[13:32] 还改成1没错吧好了那接下来如果这个不存在下一个节点else代表的是我们的流程结束把这个流程状态呢给它设置为真真正正的审批通过这么一个状态能接受吗各位好了那这样一来呢咱们这个代码呢其实写的差不多了当然这边呢还有一个小小的问题就是这儿需要一个u的对象那这个u的对象咱们也是通过微幅的形式给它查印出来好了这边呢直接拷过来
[14:07] 我也写到上边了task.get根据U的ID查我们这边U的ID是不是已经获取到了好了那这样一来咱们就已经把这个基本的逻辑方法呢写好了基本逻辑方法写好了好了那接下来最后这边咱们需要更新一下业务流程对象并且保存我们相应的这些数据更新.saveIntents传递过去
[14:41] 好了那接下来呢还要去保存一下我们当前的这个task intents.save但是我们在save这个对象之前这玩意儿是不是没有ID啊所以我们这边点设置一些基本参数设置id uuid抱歉就是id worker.next加上那还有一些其他的附加属性比如说setplus id我们其实已经有了比如说呢这边还有一个就是处理人的名称
[15:16] 那处理人的名称同样的我们也可以通过user.getUserName来获取到嗯这个没什么问题啊那这应该是set当了我们还可以设置一下它的处理时间setA time new一个data好了接着把这个对象呢给它保存进去OK那这样一来我们这个代码呢就已经哎写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 iHRM 系统中通过代码实现审批流程的发起与提交，包括前端请求、后端控制器与服务层的代码逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前位于“3.3 发起申请”下的“3.3.1 需求分析”，内容包括业务数据构造、开启动作、执行第一个Task等需求说明。
画面2：前端页面显示审批列表，弹窗提示“通过审核”，同时浏览器开发者工具显示了提交的请求体，包含 handleOpinion、processId、handleType 等字段。
画面3：IntelliJ IDEA 中展示 ProcessController.java 的代码，包含 @RequestMapping 注解的两个方法：instanceDetail 和 startProcess。
画面4：展示 AuditService.java 中的 commit 方法，其中包含根据 department_id 和 company_id 获取参数值的逻辑，以及构建 SQL 查询语句。
画面5：在 commit 方法中，通过 String 类型的 handleType 判断审批类型（2=通过，3=不通过，4=撤销），并开始构建业务逻辑。
画面6：在 commit 方法中，使用 StringBuilder 构建 SQL 语句，并调用 userGroup.getSql() 方法获取 SQL 模板。
画面7：在 commit 方法中，使用 runtimeService 的 deleteParticipantGroup、deleteProcessInstance、deleteEvent 等方法处理流程实例。
画面8：在 commit 方法中，根据 handleType 的值（2 或 3）分别调用 runtimeService 的 deleteProcessInstance 方法或 createTaskQuery 方法。
画面9：展示 commit 方法中，通过 taskInstance.getHandleType() 获取处理类型，并设置 processInstance 的状态。
画面10：在 commit 方法中，通过 runtimeService.createProcessInstanceQuery() 查询流程实例，并根据 handleType 设置状态。
画面11：展示 startProcess 方法，用于发起流程，包括构建 ProcessInstance 对象、设置属性、查询流程定义并启动流程。
画面12：在 startProcess 方法中，通过 runtimeService.createProcessInstanceQuery() 查询流程实例，并根据 handleType 设置状态。
画面13：在 startProcess 方法中，通过 taskService.createTaskQuery() 查询任务，并根据是否存在下一个节点设置流程状态。
画面14：在 startProcess 方法中，通过 runtimeService.createProcessInstanceQuery() 查询流程实例，并根据 handleType 设置状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
//查询申请的详情数据
/**
 * 会签：申请对象的id
 */
@RequestMapping(value = "/instance/{id}", method = RequestMethod.GET)
public Result instanceDetail(@PathVariable String id) throws IOException {
    //调用Service层查询id配置
    ProcInstance instance = auditService.findInstanceDetail(id);
    return new Result(ResultCode.SUCCESS,instance);
}

//流程申请
@RequestMapping(value = "/startProcess", method = RequestMethod.POST)
public Result startProcess(@RequestBody Map map) throws IOException {
    //调用Service
    auditService.startProcess(map,companyId);
    return new Result(ResultCode.SUCCESS);
}

//提交审核
```

画面4：
```java
else if (department_id.equals(param)) {
    paramValue = user.getDepartmentId();
}
else if (company_id.equals(param)) {
    paramValue = user.getCompanyId();
}
String sql = userGroup.getSql().replaceAll("\\$\\{", "+" + param + "\\}", paramValue);
Query query = entityManager.createNativeQuery(sql);
query.unwrap().setResultTransformer(Transformers.aliasToBean(User.class));
users.addAll(query.getResultList());
return users;
```

画面5：
```java
//提交审核
handleType; // 处理类型（2审批通过，3审批不通过，4撤销）
ProcTaskInstance
handleOpinion: "xxxxxx"
handleType: "4"
handleUserId: "1863785989926227968"
processId: "11755933854653552192"
```

画面6：
```java
public void commit(ProcTaskInstance taskInstance, String companyId) {
    //1.查询当前流程对象
    String processId = taskInstance.getProcessId();
    ProcInstance instance = procInstanceDao.findById(processId).get();
    //2.设置业务流程状态
    instance.setProcessState(taskInstance.getHandleType());
    //3.根据不同操作类型，完成不同的业务处理
    if ("2".equals(taskInstance.getHandleType())) {
        //3.1 如果审批通过，完成当前的任务
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
        //3.2 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    } else {
        //3.3 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    }
}
```

画面7：
```java
public void commit(ProcTaskInstance taskInstance, String companyId) {
    //1.查询当前流程对象
    String processId = taskInstance.getProcessId();
    ProcInstance instance = procInstanceDao.findById(processId).get();
    //2.设置业务流程状态
    instance.setProcessState(taskInstance.getHandleType());
    //3.根据不同操作类型，完成不同的业务处理
    if ("2".equals(taskInstance.getHandleType())) {
        //3.1 如果审批通过，完成当前的任务
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
        //3.2 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    } else {
        //3.3 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    }
}
```

画面8：
```java
public void commit(ProcTaskInstance taskInstance, String companyId) {
    //1.查询当前流程对象
    String processId = taskInstance.getProcessId();
    ProcInstance instance = procInstanceDao.findById(processId).get();
    //2.设置业务流程状态
    instance.setProcessState(taskInstance.getHandleType());
    //3.根据不同操作类型，完成不同的业务处理
    if ("2".equals(taskInstance.getHandleType())) {
        //3.1 如果审批通过，完成当前的任务
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
        //3.2 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    } else {
        //3.3 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    }
}
```

画面9：
```java
//提交审核
handleType; // 处理类型（2审批通过，3审批不通过，4撤销）
ProcTaskInstance
handleOpinion: "xxxxxx"
handleType: "4"
handleUserId: "1863785989926227968"
processId: "11755933854653552192"
```

画面10：
```java
public void commit(ProcTaskInstance taskInstance, String companyId) {
    //1.查询当前流程对象
    String processId = taskInstance.getProcessId();
    ProcInstance instance = procInstanceDao.findById(processId).get();
    //2.设置业务流程状态
    instance.setProcessState(taskInstance.getHandleType());
    //3.根据不同操作类型，完成不同的业务处理
    if ("2".equals(taskInstance.getHandleType())) {
        //3.1 如果审批通过，完成当前的任务
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
        //3.2 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    } else {
        //3.3 如果审批不通过，取消当前的流程
        runtimeService.deleteProcessInstance(processInstance.getId(), taskInstance.getHandleOpinion());
    }
}
```

画面11：
```java
public void startProcess(Map map, String companyId) {
    //1.构造业务数据
    String userId = (String) map.get("userId");
    String processKey = (String) map.get("processKey");
    String processName = (String) map.get("processName");
    User user = FeignClientService.getUserInfoByUserId(userId);
    ProcInstance instance = new ProcInstance();
    BeanUtils.copyProperties(user, instance);
    instance.setUserId(userId);
    instance.setProcessId(IdGenerator.nextId());
    instance.setProcessKey(processKey);
    instance.setProcessName(processName);
    instance.setApplyTime(new Date());
    instance.setProcessState("1");
    instance.setData(JSON.toJSONString(map));
    instance.setCompanyId(companyId);
    //2.查询流程定义
    ProcessDefinition definition = repositoryService.createProcessDefinitionQuery()
            .processDefinitionKey(processKey)
            .latestVersion()
            .singleResult();
    //3.并启动流程
    Map vars = new HashMap<>();
    vars.put("days", map.get("duration"));
    ProcessInstance process

