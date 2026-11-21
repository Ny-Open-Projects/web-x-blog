# 画面线理解：23-SasSHRM中基于shiro的认证授权：用户授权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\23-SasSHRM中基于shiro的认证授权：用户授权_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:07, 01:55, 02:29, 03:25, 04:05, 05:03, 06:00, 07:02, 07:48, 08:29, 09:09, 09:53, 10:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:42:38

1) 这一组画面整体在讲一个基于 Spring Boot 和 Shiro 的 HRM 系统的开发与功能演示，包括项目结构、核心配置、控制器逻辑、自定义异常处理及前端界面操作。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示项目结构，选中 `hrm_system` 模块，目录结构包含 `src/main/java`、`src/test`、`target`、`pom.xml` 等。
画面 2: 展示 `hrm_system` 模块下的 `java` 目录结构，包含 `controller`、`dao`、`service` 等子包。
画面 3: 展示 `CompanyApplication.java` 文件内容，包含 Spring Boot 启动类和 `@Bean` 注解配置。
画面 4: 展示 `CompanyApplication.java` 文件内容，包含 `@Bean` 注解配置 `JwtUtils` 和 `IdWorker`。
画面 5: 展示 `DepartmentController.java` 文件内容，包含 `@RequestMapping` 注解的 `save` 和 `findAll` 方法。
画面 6: 展示 `CustomSessionManager.java` 文件内容，包含 `getSessionId` 方法，用于获取 session ID。
画面 7: 展示 HRM 系统的前端界面，显示工作日历和快速导航。
画面 8: 展示 SQL 查询工具界面，显示 `bs_user` 表的数据。
画面 9: 展示 HRM 系统的员工列表页面。
画面 10: 展示 `UserController.java` 文件内容，包含 `update`、`delete` 方法和 `main` 方法用于测试 MD5 加密。
画面 11: 展示 `hrm_common` 模块下的 `exception` 包结构。
画面 12: 展示 `ResultCode.java` 文件内容，包含 `ResultCode` 枚举类，定义了各种操作码。
画面 13: 展示 HRM 系统的前端界面，显示导航菜单。
画面 14: 展示 HRM 系统的员工列表页面，点击“查看”按钮弹出提示框。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 3:
```java
package com.ihrm.company;
import ...
//1.配置springboot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm")
//2.配置jpa注解的扫描
@EntityScan(value = "com.ihrm.domain.company")
public class CompanyApplication {
    //启动方法
    public static void main(String[] args) {
        SpringApplication.run(CompanyApplication.class, args);
    }
    @Bean
    public IdWorker idWorker() {
        return new IdWorker();
    }
}
```

画面 4:
```java
package com.ihrm.company;
import ...
//1.配置springboot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm")
//2.配置jpa注解的扫描
@EntityScan(value = "com.ihrm.domain.company")
public class CompanyApplication {
    //启动方法
    public static void main(String[] args) {
        SpringApplication.run(CompanyApplication.class, args);
    }
    @Bean
    public JwtUtils jwtUtils() {
        return new JwtUtils();
    }
    @Bean
    public IdWorker idWorker() {
        return new IdWorker();
    }
}
```

画面 5:
```java
@RequestMapping(value = "/department", method = RequestMethod.POST)
public Result save(@RequestBody Department department) {
    //企业id，目前使用固定值，以定解决
    department.setCompanyId(companyId);
    //2.调用service完成保存
    departmentService.save(department);
    //3.构造返回结果
    return new Result(ResultCode.SUCCESS);
}
//查询企业的部门表
@RequestMapping(value = "/department", method = RequestMethod.GET)
public Result findAll(Long companyId) {
    //1.指定企业
    Company company = companyService.findById(companyId);
    //2.查询部门列表
    List<Department> list = departmentService.findAll(companyId);
    //3.构造返回结果
    DeptListResult deptListResult = new DeptListResult(company, list);
    return new Result(ResultCode.SUCCESS, deptListResult);
}
```

画面 6:
```java
/**
 * 头信息中携带sessionid
 * 请求头：Authorization: sessionid
 * 指定sessionid的获取方式
 */
protected Serializable getSessionId(ServletRequest request, ServletResponse response) {
    //获取请求头中的sessionid
    String id = WebUtils.getHttpHeader(request, "Authorization");
    if (StringUtils.isEmpty(id)) {
        //如果没有携带，生成新的sessionid
        return super.getSessionId(request, response);
    } else {
        //请求头信息：bearer sessionid
        id = id.replaceAll(" ", "Bearer", replacement: "");
        //设置sessionid
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE, "header");
        request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
        return id;
    }
}
```

画面 10:
```java
@RequestMapping(value = "/user/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable(value = "id") String id, @RequestBody User user) {
    //1.设置修改的部门id
    user.setCompanyId(id);
    //2.调用service更新
    userService.update(user);
    return new Result(ResultCode.SUCCESS);
}
//快捷删除
@RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE, name = "API-USER-DELETE")
public Result delete(@PathVariable(value = "id") String id) {
    userService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
public static void main(String[] args) {
    String password = new Md5Hash(source: "123456", salt: "1380000003", hashIterations: 3).toString();
    System.out.println(password);
}
```

画面 12:
```java
public enum ResultCode {
    SUCCESS(true, 10000, "操作成功！"),
    FAIL(false, 10001, "操作失败！"),
    UNAUTHENTICATED(false, 10002, "用户未登录！"),
    UNAUTHORIZED(false, 10003, "权限不足！"),
    SERVER_ERROR(false, 99999, "服务器异常，请稍后重试！"),
    //用户操作返回码
    MOBILEORPASSWORDDERROR(false, 10001, "用户名或密码错误");
    //企业操作返回码
    ENTERPRISEOPERATIONERROR(false, 10002, "企业操作失败");
    //其他操作返回码----
    //操作是否成功
    boolean success;
    //操作码
    int code;
    //操作信息
    String message;
    ResultCode(boolean success, int code, String message) {
        this.success = success;
        this.code = code;
        this.message = message;
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
