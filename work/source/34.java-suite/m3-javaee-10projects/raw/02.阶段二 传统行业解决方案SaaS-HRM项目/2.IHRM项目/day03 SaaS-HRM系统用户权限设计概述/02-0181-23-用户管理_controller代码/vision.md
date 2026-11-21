# 画面线理解：23-用户管理：controller代码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\23-用户管理：controller代码_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:30, 00:45, 01:10, 01:54, 02:12, 02:43, 02:59, 03:24, 03:42, 04:27, 04:47, 05:29, 05:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:40:19

1) 这一组画面整体在讲什么（一句话）：
演示在 Spring Boot 项目中，如何在 UserController 中实现分页查询功能，包括引入 Pageable、PageResult 类，以及使用 @RequestParam Map 接收分页参数。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 UserService.java 文件，其中包含 save 和 update 方法，用于保存和更新用户数据，涉及 IdWorker 生成 ID、设置密码、状态等操作。
画面 2: 展示项目结构，聚焦在 UserContoller.java 文件，位于 com.ihm.system.controller 包下。
画面 3: 展示 UserController.java 文件，其中包含 findALL 和 findById 方法，用于查询企业部门列表和单个部门信息。
画面 4: 展示 UserController.java 文件，其中包含 save 方法，用于保存部门信息，设置企业 ID。
画面 5: 展示 UserController.java 文件，其中包含 setCompanyId 方法，用于设置企业 ID。
画面 6: 展示 UserController.java 文件，其中包含 update 和 delete 方法，用于更新和删除用户。
画面 7: 展示 UserController.java 文件，其中在 findALL 方法中尝试使用 @RequestParam Map 接收分页参数，但编译器提示“Cannot resolve symbol 'Map'”。
画面 8: 展示 UserController.java 文件，其中在 findALL 方法中尝试使用 @RequestParam Map 接收分页参数，但编译器提示“Cannot resolve symbol 'Map'”。
画面 9: 展示 UserController.java 文件，其中在 findALL 方法中尝试使用 @RequestParam Map 接收分页参数，但编译器提示“Cannot resolve symbol 'Map'”。
画面 10: 展示 UserController.java 文件，其中在 findALL 方法中尝试使用 @RequestParam Map 接收分页参数，但编译器提示“Cannot resolve symbol 'Map'”。
画面 11: 展示项目结构，聚焦在 PageResult.java 文件，位于 com.ihm.common.entity 包下。
画面 12: 展示 UserController.java 文件，其中在 findALL 方法中使用 PageResult 类封装分页结果。
画面 13: 展示 UserController.java 文件，其中在 findALL 方法中使用 PageResult 类封装分页结果。
画面 14: 展示 UserController.java 文件，其中在 findALL 方法中使用 PageResult 类封装分页结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import java.util.List;
import java.util.Map;

@Service
public class UserService {
    @Autowired
    private UserDAO userDAO;
    @Autowired
    private IdWorker idWorker;

    /*
     * 1.保存用户
     */
    public void save(User user) {
        //设置主键id
        String id = idWorker.nextId()+"";
        user.setPassword("123456");//设置初始密码
        user.setEnableState(1);
        user.setUserId(id);
        //调用dao保存
        userDAO.save(user);
    }

    /*
     * 2.更新用户
     */
    public void update(User user) {

    }
```

画面 2:
```java
package com.ihm.system.controller;

public class UserController {

}
```

画面 3:
```java
/**
 * 查询企业部门列表
 * @param companyId
 */
@RequestMapping(value = "/department", method = RequestMethod.GET)
public Result findAll() {
    Company company = companyService.findById(companyId);
    //1.完成查询
    List<Department> list = departmentService.findAll(companyId);
    //2.构造返回结果
    DeptListResult deptlistResult = new DeptListResult(ResultCode.SUCCESS, list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}

/**
 * 根据id查询department
 */
@RequestMapping(value = "/department/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) {
    Department department = departmentService.findById(id);
    return new Result(ResultCode.SUCCESS, department);
}
```

画面 4:
```java
import java.util.List;
//1.解决跨域
@CrossOrigin
//2.声明restcontroller
@RestController
//3.设置访问路径
@RequestMapping(value = "/sys")
public class UserController extends BaseController {
    @Autowired
    private DepartmentService departmentService;

    /**
     * 保存
     */
    @RequestMapping(value = "/department", method = RequestMethod.POST)
    public Result save(@RequestBody Department department) {
        //企业id: 自动使用当前企业id，以后会解决
        department.setCompanyId(companyId);
        //2.调用service保存
        departmentService.save(department);
        //3.返回结果
        return new Result(ResultCode.SUCCESS);
    }
```

画面 5:
```java
//设置企业id
public void setCompanyId(String companyId) {
    this.companyId = companyId;
}
```

画面 6:
```java
/**
 * 修改用户
 */
@RequestMapping(value = "/user/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable(value = "id") String id, @RequestBody User user) {
    //1.修改用户信息
    user.setId(id);
    //2.调用service更新
    userService.update(user);
    //3.返回结果
    return new Result(ResultCode.SUCCESS);
}

/**
 * 根据id删除
 */
@RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) {
    userService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

画面 7:
```java
/**
 * 查询企业用户列表
 */
@RequestMapping(value = "/user", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map) {
    Company company = companyService.findById(companyId);
    //1.完成查询
    List<User> list = userService.findAll(companyId);
    //2.构造返回结果
    DeptListResult deptlistResult = new DeptListResult(ResultCode.SUCCESS, list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

画面 8:
```java
/**
 * 查询企业用户列表
 */
@RequestMapping(value = "/user", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map) {
    Company company = companyService.findById(companyId);
    //1.完成查询
    List<User> list = userService.findAll(companyId);
    //2.构造返回结果
    DeptListResult deptlistResult = new DeptListResult(ResultCode.SUCCESS, list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

画面 9:
```java
/**
 * 查询企业用户列表
 */
@RequestMapping(value = "/user", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map) {
    Company company = companyService.findById(companyId);
    //1.完成查询
    List<User> list = userService.findAll(companyId);
    //2.构造返回结果
    DeptListResult deptlistResult = new DeptListResult(ResultCode.SUCCESS, list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

画面 10:
```java
/**
 * 查询企业用户列表
 */
@RequestMapping(value = "/user", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map) {
    Company company = companyService.findById(companyId);
    //1.完成查询
    List<User> list = userService.findAll(companyId);
    //2.构造返回结果
    DeptListResult deptlistResult = new DeptListResult(ResultCode.SUCCESS, list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

画面 11:
```java
package com.ihm.common.entity;

/**
 * 分页
 */
{
    "success": "成功",
    "code": 10000,
    "message": "ok",
    "data": {
        "total": //总条数
        "rows": //数据列表
    }
}

@Builder
@AllArgsConstructor
@NoArgsConstructor
public class PageResult<T> {
    private Long total;
    private List<T> rows;
}
```

画面 12:
```java
/**
 * 查询企业用户列表
 */
@RequestMapping(value = "/user", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map) {
    Company company = companyService.findById(companyId);
    //1.完成查询
    List<User> list = userService.findAll(companyId);
    //2.构造返回结果
    DeptListResult deptlistResult = new DeptListResult(ResultCode.SUCCESS, list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

画面 13:
```java
/**
 * 查询企业用户列表
 */
@RequestMapping(value = "/user", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map) {
    Company company = companyService.findById(companyId);
    //1.完成查询
    List<User> list = userService.findAll(companyId);
    //2.构造返回结果
    DeptListResult deptlistResult = new DeptListResult(ResultCode.SUCCESS, list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

画面 14:
```java
package com.ihm.system.controller;
import com.ihm.common.controller.BaseController;
import com.ihm.common.entity.PageResult;
import com.ihm.common.entity.Result;
import com.ihm.common.entity.ResultCode;
import com
