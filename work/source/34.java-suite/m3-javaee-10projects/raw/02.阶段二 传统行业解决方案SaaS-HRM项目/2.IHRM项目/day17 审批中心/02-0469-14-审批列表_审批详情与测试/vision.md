# 画面线理解：14-审批列表：审批详情与测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\14-审批列表：审批详情与测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:30, 01:03, 02:22, 02:40, 02:57, 03:20, 03:38, 05:26, 05:48, 06:05, 06:41, 07:19, 07:29, 08:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:10:05

1) 这一组画面整体在讲什么（一句话）：
演示一个请假审批系统的前后端交互，重点展示控制器层如何接收请求、调用服务层查询数据，并在前端页面展示审批列表和详情。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示ProcessController.java中instanceList方法的代码，用于分页查询审批列表，接收ProcInstance对象和分页参数。
画面2：展示ProcessController.java中instanceDetail方法的代码，用于根据ID查询审批详情。
画面3：展示AuditService.java中findInstanceDetail方法的代码，用于根据ID查询审批详情。
画面4：展示ProcessController.java中instanceDetail方法的代码，用于根据ID查询审批详情。
画面5：展示项目结构，包含controller、service、dao等包，以及AuditService.java文件。
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
    //1.调用service分页查询
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
    //调用service根据id查询
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
│   │               ├── controller
│   │               │   └── ProcessController.java
│   │               ├── service
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
