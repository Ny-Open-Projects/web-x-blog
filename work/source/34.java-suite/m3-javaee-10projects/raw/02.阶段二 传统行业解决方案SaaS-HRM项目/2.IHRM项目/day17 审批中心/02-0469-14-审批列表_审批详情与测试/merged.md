# 14-审批列表：审批详情与测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\14-审批列表：审批详情与测试_【海量资源尽在 ubkz.com】.mp4
- 时长 8分23秒（音频 503s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们现在呢已经把这个列表的方法写好了那列表方法写好了之后啊我们等一下会去测试那因为我们有了列表呢可能还会查询它的详情所以为了我一会儿不用那么频繁的重启我把列表写好之后接下来呢我们就开始编写一个新的方法就是去查询我们的这个申请的这个详情数据详情的这个数据就是为了我们一会儿操作起来
[00:32] 不用老重启啊好了那接下来那同样的我们开始Ctrl C Ctrl Vcopy一段先去把这个方法结构给它写出来那中间的这些都删掉都删掉好了那这边那我们这边的方法呢就叫做Intense好了把这个ID传回来就可以了哎这是我们的参数参数就是我们的哎申请对象的ID
[01:09] 好了那接下来中间我们可以通过pass variable的形式得到对应的ID此具类型IDOK这个没问题那我们这个请求方式不想多说了可能是get好了那这边呢写一个方法就是intense detail吧那注意啊那对于这个方法结构咱们写出来了之后接下来我想说那这个方法呢其实很简单就是调用Service根据ID查询
[01:43] 根据ID查询查询其实就可以了那Service我们就用audit-Service.find这个intents好了ID传下去那得到对应的返回就是这个intents那最终构造返回结果这个都比较简单没错了好了那接下来在Service当中添加一个方法就是根据我们的ID去查询
[02:18] 申请数据详情那这个就更简单了你要查详情是不是就直接根据ID查就行了所以留点FileByID查进去点这个方法比较简单OK那这样一来呢咱们这个根据ID查询的这个方法呢也已经写好了那这些写好了之后我们可以一起重新启动一下
[02:50] 咱们的微服务找到页面来看效果好了这边呢我去重新启动时间比较长我先暂停一下那这边呢我的服务呢已经启动成功了回到我们的页面一起来试一下现在呢刷新那这边呢应该还没启动啊没有反应过来那接着再来刷新好了各位会发现现在呢已经有了这么一条记录没错吧那接下来呢我们来看一下这个查看详情一点查看
[03:20] 各位发现你请假提交的这些内容呢其实已经展示出来了那对于这个需要各位说明一下就是咱们查看这个详情的时候打开F2再来看点击查看详情那这边呢会发送请求最终得到我们的数据结果那得到数据结果我们查询的数据库表不言而喻就是我们自己业务的流程实例表
[03:47] ID等等等等这些都没问题但是有一个PLC date这个是我们请假的业务数据比如请假类型比如开始时间业务时间请假时长还有我们这边的申请原因这些是我们的业务数据那业务数据呢请假加班离职可能不一样那在我们的数据库当中是不是把它以JSON的形式以字符串的形式提供到数据库里啊所以各位来看我这边查询出来的时候虽然你看着
[04:17] 像杰森但是这边没转化没有变类型格式那其实这玩意儿是一个杰森的字符串其实是一个死菌字符串那这个死菌字符串在页面前端的时候就需要做一个处理我们找到这个页面前端来看我们这回的数据就需要通过杰森把这个字符串数据转化为这个字符串好了这个其实就是我们的一个小小的技巧在里面由于这里面的
[04:48] 咱们的流程比较多不同的流程业务数据可能不一样那我们存到一个表里怎么办可以以一个json自动创来进行传递那接下来我们显示的时候就需要对这个自动创把它转化为一个规向并展示到另一边好了那这样一来呢咱们这个列表还有我们对应的这些就已经做过了那我们看一下我发起的这个就是我申请人itcast那带审批的当前审批人就是itcast这个呢
[05:17] 我在数据库刚刚加一条记录我这个当前审批人就是我如果我把这个当前审批人随便加一个给成一找到页面我发起的没问题这个好像有点问题是吧这些都不能点这些都不能点咱们来看一下问题就在出在什么地方随便点两个离职审批这边发起请求
[05:49] 那发起请求对应的参数都有那肯定就是代码部分了那我们回到我们的代码找到Controller参数已经封装过来了配置和size都没问题那接下来呢应该就是出到Service这边那在Service这边哦各位能够看到我这边是不是条件虽然已经封装了一大堆但是我这边反过来是个no代表没有条件没错吧那并且呢我们这边刚才看到了其实
[06:16] 有审批类型审批状态还有当前节点处理人就找到待审批的是不是还有一个叫做我发起的就是查询发起人那发起人这个对应的咱们也把它补充上发起人对应的就在这边申请人叫做user id其实这个很简单就是跟之前的流程都是一模一样的好了改一下get user id好了user idget user id没问题那接下来底下这边就是构造
[06:48] 完整的条件cb.and好了我们开始就是list.toArray这个逻辑呢都是差不多的里面构造一个数组你有一个rendicate数组那这个数组的长度就是我们list的长度set好了那这样一来呢咱们这个就已经都没啥问题了好了那接下来咱们重新启动一下当前这个微服务
[07:19] 这边的微服务已经启动成功了回到我们的页面刷新一把来看一下一次可能会有一个零失负没事好了接着那各位来看我们发送的是请假的流程我查一下离职的OK没有查请假的没问题我查这个请假通过的没有我查审计中的没问题是不是有接下来我发起的有这么一条请假流程带审批的各位发现这个应该没问题
[07:49] 那接下来呢我把这个数据库的数据呢改一下回到这边我把这个当前节点处理的这个ID我改成123456那接着再去查一下带审批的哎是不是没有了那我发起的现在有一条我把我发起的就是U字ID改成123456那理论上那我这边我发起的是不是也应该查不到了好哎各位来看这样一来是不是咱们就已经完成了整个列表的查询当了也包含
[08:20] 这些详情处理没错吧OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个请假审批系统的前后端交互，重点展示控制器层如何接收请求、调用服务层查询数据，并在前端页面展示审批列表和详情。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示ProcessController.java中instanceList方法的代码，用于分页查询审批列表，接收ProcInstance对象和分页参数。
画面2：展示ProcessController.java中instanceDetail方法的代码，用于根据ID查询审批详情。
画面3：展示AuditService.java中findInstanceDetail方法的代码，用于根据ID查询审批详情。
画面4：展示ProcessController.java中instanceDetail方法的代码，用于根据ID查询审批详情。
画面5：展示项目结构，包含Controller、Service、dao等包，以及AuditService.java文件。
画面6：前端页面显示“待审批”列表，用户点击“通过”按钮。
画面7：前端页面显示请假详情弹窗，包含申请人信息和请假类型等字段。
画面8：数据库管理工具中显示“proc_instance”表，提示“是否保存这些修改？”。
画面9：前端页面显示“待审批”列表，用户点击“通过”按钮。
画面10：展示AuditService.java中getInstanceList方法的代码，用于分页查询审批列表。
画面11：展示AuditService.java中getInstanceList方法的代码，用于分页查询审批列表。
画面12：展示AuditService.java中getInstanceList方法的代码，用于分页查询审批列表。
画面13：前端页面显示“待审批”列表，无数据。
画面14：前端页面显示请假详情弹窗，包含申请人信息和请假类型等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@RequestMapping(value = "/instance/{page}/{size}",method = RequestMethod.PUT)
public Result instanceList(@RequestBody ProcInstance instance,@PathVariable int page,@PathVariable int size) throws IOException {
    //1.调用Service分页查询
    Page pages = auditService.getInstanceList(instance,page,size);
    //2.page对象转换为自己的PageResult对象
    PageResult pr = new PageResult(pages.getTotalElements(),pages.getContent());
    //3.返回
    return new Result(ResultCode.SUCCESS,pr);
}
```

画面2：
```java
@RequestMapping(value = "/instance/{id}",method = RequestMethod.PUT)
public Result instanceDetail(@RequestBody ProcInstance instance,@PathVariable int page,@PathVariable int size) throws IOException {
    return new Result(ResultCode.SUCCESS);
}
```

画面3：
```java
if(StringUtils.isEmpty(instance.getProcessKey())){
    list.add(cb.equal(root.get("processKey"),instance.getProcessKey()));
}
//审批状态(多个,每个状态之间使用“,”隔开)
if(StringUtils.isEmpty(instance.getProcessState())){
    Expression<String> exp = root.getString("processState");
    list.add(exp.in(instance.getProcessState().split(",")));
}
//当前节点的处理人
if(StringUtils.isEmpty(instance.getProcCurrNodeUserId())){
    list.add(cb.like(root.get("procCurrNodeUserId").as(String.class), "%"+instance.getProcCurrNodeUserId()+"%");
}
return null;
}
//调用dao进行Specification查询
return procInstanceDao.findAll(spec,new PageRequest(page-1,size));
//根据id查询审批详情
public ProcInstance findInstanceDetail(String id) {
```

画面4：
```java
@RequestMapping(value = "/instance/{id}",method = RequestMethod.GET)
public Result instanceDetail(@PathVariable String id) throws IOException {
    //调用Service根据id查询
    ProcInstance instance = auditService.findInstanceDetail(id);
    return new Result(ResultCode.SUCCESS,instance);
}
```

画面5：
```java
// 项目结构
src
├── main
│   ├── java
│   │   └── com
│   │       └── ihrm
│   │           └── audit
│   │               ├── Controller
│   │               │   └── ProcessController.java
│   │               ├── Service
│   │               │   └── AuditService.java
│   │               └── dao
│   │                   ├── ProcInstanceDao.java
│   │                   └── ProcInstance.java
│   └── resources
```

画面10：
```java
public Page getInstanceList(ProcInstance instance, int page, int size) {
    //1.创建Specification，用于查询
    Specification<ProcInstance> spec = new Specification<ProcInstance>() {
        @Override
        public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder cb) {
            List<Predicate> list = new ArrayList<>();
            //审批类型
            if(!StringUtils.isEmpty(instance.getProcessKey())){
                list.add(cb.equal(root.get("processKey"),instance.getProcessKey()));
            }
            //审批状态(多个,每个状态之间使用“,”隔开)
            if(!StringUtils.isEmpty(instance.getProcessState())){
                Expression<String> exp = root.getString("processState");
                list.add(exp.in(instance.getProcessState().split(",")));
            }
            //当前节点的处理人
            if(!StringUtils.isEmpty(instance.getProcCurrNodeUserId())){
                list.add(cb.like(root.get("procCurrNodeUserId").as(String.class), "%"+instance.getProcCurrNodeUserId()+"%"));
            }
            //发起人
            if(!StringUtils.isEmpty(instance.getUserId())){
                list.add(cb.equal(root.get("userId").as(String.class),instance.getUserId()));
            }
            return null;
        }
    };
    //调用dao进行Specification查询
    return procInstanceDao.findAll(spec,new PageRequest(page-1,size));
}
```

画面11：
```java
public Page getInstanceList(ProcInstance instance, int page, int size) {
    //1.创建Specification，用于查询
    Specification<ProcInstance> spec = new Specification<ProcInstance>() {
        @Override
        public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder cb) {
            List<Predicate> list = new ArrayList<>();
            //审批类型
            if(!StringUtils.isEmpty(instance.getProcessKey())){
                list.add(cb.equal(root.get("processKey"),instance.getProcessKey()));
            }
            //审批状态(多个,每个状态之间使用“,”隔开)
            if(!StringUtils.isEmpty(instance.getProcessState())){
                Expression<String> exp = root.getString("processState");
                list.add(exp.in(instance.getProcessState().split(",")));
            }
            //当前节点的处理人
            if(!StringUtils.isEmpty(instance.getProcCurrNodeUserId())){
                list.add(cb.like(root.get("procCurrNodeUserId").as(String.class), "%"+instance.getProcCurrNodeUserId()+"%"));
            }
            //发起人
            if(!StringUtils.isEmpty(instance.getUserId())){
                list.add(cb.equal(root.get("userId").as(String.class),instance.getUserId()));
            }
            return null;
        }
    };
    //调用dao进行Specification查询
    return procInstanceDao.findAll(spec,new PageRequest(page-1,size));
}
```

画面12：
```java
public Page getInstanceList(ProcInstance instance, int page, int size) {
    //1.创建Specification，用于查询
    Specification<ProcInstance> spec = new Specification<ProcInstance>() {
        @Override
        public Predicate toPredicate(Root<ProcInstance> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder cb) {
            List<Predicate> list = new ArrayList<>();
            //审批类型
            if(!StringUtils.isEmpty(instance.getProcessKey())){
                list.add(cb.equal(root.get("processKey"),instance.getProcessKey()));
            }
            //审批状态(多个,每个状态之间使用“,”隔开)
            if(!StringUtils.isEmpty(instance.getProcessState())){
                Expression<String> exp = root.getString("processState");
                list.add(exp.in(instance.getProcessState().split(",")));
            }
            //当前节点的处理人
            if(!StringUtils.isEmpty(instance.getProcCurrNodeUserId())){
                list.add(cb.like(root.get("procCurrNodeUserId").as(String.class), "%"+instance.getProcCurrNodeUserId()+"%"));
            }
            //发起人
            if(!StringUtils.isEmpty(instance.getUserId())){
                list.add(cb.equal(root.get("userId").as(String.class),instance.getUserId()));
            }
            return null;
        }
    };
    //调用dao进行Specification查询
    return procInstanceDao.findAll(spec,new PageRequest(page-1,size));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

