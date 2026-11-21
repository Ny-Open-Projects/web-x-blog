# 画面线理解：04-部门微服务：保存部门

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\04-部门微服务：保存部门_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:31, 01:10, 01:50, 02:16, 02:31, 02:53, 03:12, 03:30, 05:13, 05:24, 05:39, 05:54, 06:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:28:40

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
