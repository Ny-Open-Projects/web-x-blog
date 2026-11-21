# 04-部门微服务：保存部门

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\04-部门微服务：保存部门_【海量资源尽在 ubkz.com】.mp4
- 时长 6分26秒（音频 387s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] OK我们的第U层Service层呢都写的差不多了那接下来呢就是关注我们最外层也就是Web层也就是我们的控制器类好了在这边呢找到我的Controller这个包下去创建一个部门管理的Controller右键来一个ClassDepartmentControllerOK好了呢这Department的Controller当中呢首先第一件事
[00:34] 你写上类千万别忘了第一件事解决跨域好了第二件事声明reset Controller好了接着第三件事我们可以设置比如说呢我可以设置当前这个Controller的比如说副路径请求副路径那好了接下来呢我们把这三个呢都给它搞定解决跨域ata crossOK
[01:05] 那好了接着声明reset controllerat reset controllerOK也比较简单那接下来第三个设置附路径request mappingOKvalue等于那希望各位要注意的是我这个部门管理呢其实是企业管理的一个子的这么一项那所以我们请求的这个路径我准备请求路径变成company下的比如说department
[01:36] 所以我这个请求的附路径呢就应该是companyOK那这样一来这样一来我们已经把这个类其实已经声明好了那声明好了之后接下来呢我们就可以遵照的API先把这几个方法都给它挪列出来增加列表根据ID删除修改删除根据ID查询等等那好了我们一来看首先呢public注意web层呢我们返回的响应对象就是一个result
[02:08] 这是固定的我们昨天设置好了那接下来呢siu那siu方法好了这个就是我们叫做保存那siu方法的时候呢我们可以设置它的请求路径requestmappingvalue等于那各位来看一下post方式提交请求的路径department所以我这边直接就是department-depart
[02:46] Department好了那我们的请求方式Method叫做PostOK那既然是一个Post请求那我们观察了一下增加的这个请求的这些数据恰巧和我们Department实体类基本上是一模一样的所以我们直接就可以借助AddRequest买品把它封装到我们的部门对象当中
[03:16] OK这边直接return那为了不报错好看一些抱歉request body写错了好了那这样一来我这个基本的保存的这个轮廓其实就已经写好那已经写好了之后呢我们接下来就可以通过Service去调用保存的方法那但是通过Service保存之前呢需要跟各位来聊一个比较重要的问题就是说呀
[03:46] 我们这里面你保存的其实是一个部门那这个部门应该归属于某一个企业才对A企业它有自己的部门B企业也应该有自己部门考虑昨天我们说过的隔离性是不是需要设置一个企业的ID那这个企业的ID究竟从哪来我们今天先不用关注我们先把这个企业ID默认先给它设置成一那我们之后会解决
[04:12] 那只有当企业ID设置好了之后我们是不是再去调用Service再去完成我们的保存操作其实就可以了那所以对于我们来说有两件事要做第一件事设置保存的企业IDOK接着第二件事调用Service完成保存企业的这么一个工作好了第三件事才是构造返回结果
[04:39] OK那接着我们一里来看首先设置企业ID这边呢先声明一把企业ID我们今天呢先目前使用固定值1我们以后会解决好了所以在这边呢我先死菌类型的先来一个企业IDcompanyID那就等于1了OK那好了接着设置到部门对象当中打点setdepartmentsetcompany
[05:15] ID Company ID 设人序OK 那好了接下来调用 Service那 Service 目前还没有需要 Autoware 依赖注入进来PrivateDepartmentServiceDepartment Service接着调用 Department Service 打点我们有一个 C5 方法OK 那这样一来那这样一来第二件事也搞定了那接着构造返回结果那构造返回结果的时候我们需要一个 Result那直接就可以ReturnNew 一个
[05:47] result那我们都知道成功的时候result可以接收这么一个枚举这个枚举里面有true还有我们的响应编码还有我们的操作那我这边是不是直接可以把这个枚举对象存进去就可以了打点sys好了为什么这样做是因为我们的API决定的我们的API只需要三个属性codesys和message
[06:17] OK那这样一来呢我们这个返回其实也已经哎构造成功了那这样一来我保存就已经搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中编写部门信息的 RESTful API 控制器，包括引入注解、定义请求映射、接收 JSON 数据、调用服务层并返回统一结果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 DepartmentService.java 文件，其中包含 @Service 注解、@Autowired 注解注入的 DepartmentDao 和 IdWorker，以及 save() 和 update() 方法。
画面2：展示 DepartmentController.java 文件的初始状态，准备编写控制器。
画面3：在 DepartmentController.java 中导入 Spring Web 相关注解，如 @RestController、@CrossOrigin、@RequestMapping 等。
画面4：展示 API 文档页面，显示 departmentId 参数和 Department 实体的 JSON 示例。
画面5：在 DepartmentController.java 中添加 @RequestMapping(value = "/company") 注解。
画面6：展示多窗口工作环境，包括 IDEA、浏览器、终端等。
画面7：在 DepartmentController.java 中添加 @RequestMapping(value = "/department", method = RequestMethod.POST) 注解。
画面8：在 DepartmentController.java 中输入 @RequestMapping 注解，IDE 提示方法名。
画面9：在 DepartmentController.java 中添加 @RequestBody Department department 参数。
画面10：展示 Department 类的属性和方法，用于接收 JSON 数据。
画面11：在 DepartmentController.java 中添加 @Autowired 注解注入 DepartmentService。
画面12：在 DepartmentController.java 中编写 save 方法，设置企业 ID。
画面13：展示 ResultCode.java 文件，定义了操作成功、失败、未授权、服务器错误等枚举常量。
画面14：在 DepartmentController.java 中返回 new Result(ResultCode.SUCCESS)。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class DepartmentService {
    @Autowired
    private DepartmentDao departmentDao;
    @Autowired
    private IdWorker idWorker;
    /**
     * 1.保存部门
     */
    public void save(Department department) {
        //设置主键id
        String id = idWorker.nextId()+"";
        department.setId(id);
        //调用dao保存部门
        departmentDao.save(department);
    }
    /**
     * 2.更新部门
     */
    public void update(Department department) {
        //根据id查询
    }
}
```

画面3：
```java
import org.springframework.web.bind.annotation.CrossOrigin;
@RestController
@RequestMapping
@CrossOrigin
@RestControllerAdvice
@ResponseStatus
@JsonTypeResolver
```

画面5：
```java
@RequestMapping(value = "/company")
```

画面7：
```java
@RequestMapping(value = "/department", method = RequestMethod.POST)
```

画面9：
```java
@RequestMapping(value = "/department", method = RequestMethod.POST)
public Result save(@RequestBody Department department) {
```

画面11：
```java
@Autowired
private DepartmentService departmentService;
```

画面12：
```java
String companyId = "1";
department.setCompanyId(companyId);
departmentService.save(department);
return null;
```

画面14：
```java
return new Result(ResultCode.SUCCESS);
```

画面13：
```java
public enum ResultCode {
    SUCCESS(true, 10000, "操作成功"),
    FAIL(false, 10001, "操作失败"),
    UNAUTHENTICATED(false, 10002, "您还未登录"),
    UNAUTHORISE(false, 10003, "权限不足"),
    SERVER_ERROR(false, 99999, "抱歉，系统繁忙，请稍后重试");
    //操作是否成功
    boolean success;
    //操作返回码
    int code;
    //提示信息
    String message;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

