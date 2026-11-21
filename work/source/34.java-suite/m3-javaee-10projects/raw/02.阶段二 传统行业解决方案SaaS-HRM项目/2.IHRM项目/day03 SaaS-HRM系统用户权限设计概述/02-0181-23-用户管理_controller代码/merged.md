# 23-用户管理：controller代码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\23-用户管理：controller代码_【海量资源尽在 ubkz.com】.mp4
- 时长 5分57秒（音频 357s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那Service呢我们也已经写好了那最后就是我们有一个do层Controller这么一层那跟刚才的套路一样从其他的地方Controller ccopy一个Controller放到系统模块里把它放到c1trol112controller这个包下我叫做user controlleruser Controller那user Controller里面的代码呢其实跟刚才这个部门的基本上都差不多基本增长改查
[00:33] 好了我从这边呢直接把这个代码拿过来我们做一个简单的改造其实就可以了OK那还有我们最上边的配置要配置它的跨域问题等等等等这些内容好了对于我们系统模块呢访问的全部都是system请求地址好了system当然了我们这边可以给它改成sys简单一些好了接下来里面的autoware我们就可以进行一个简单的改造好了做一个修改
[01:09] department改成大写userreplace all还有小写的department改成小写的userreplace allOK那这样一来基本的这些内容呢我们已经构造的都差不多了那接着对于细节问题做一个简单的修改那首先呢我们保存封装到user对象里打一下包
[01:30] 好了对于用户来说保存的时候我们可以设置这个用户他所属的企业也可以设置这个用户他所属的企业名称那好了我这边补充上他企业的名称和企业ID这边就是一个冗余的一个思想因为我查用户的时候可能要调用出企业的一个名称这边写company name当然了company name因为我们这边继承了flareflare里面都已经设置好了
[02:01] 好了保存写好了那接下来呢就是查询全部查询全部一会儿再说Find by IDFind by ID也有好了接着再修改修改呢也没有什么问题好了最后一个根据ID删除这个都是没有问题的那接下来我们着重关注的其实就是Find All那对于Find All来说呢我们这边看一下API查询全部那Find All会查询传递配置和size以及
[02:31] HASP, DEC, DTP, Department ID 等等那对于配置和 Size 来说他们请求的全部都是 Get 方法那 Get 方法很简单我们可以把参数直接配置到参数列表那你请求的参数呢有 Page,有 Size, Page, Inter, SizeOK 两个参数搞定了那接下来把底下这几个是不是可以构造成一个 Map 集合那 Map 集合可以借助一个 Path Param
[03:00] Path Param那么可以借助Path Param把我们请求的这些参数封装到一个Map集合里面就可以了OK倒下包Path Param写错了抱歉Request Param把它封装到一个Map集合里面就可以了一下包OK那接下来呢我们这里面的方法其实就比较简单了我们可以通过User Service打点Find All翻到里面把Map传递过去
[03:39] 把配置和sales都传递过去就可以了当然了我们这边得到的是一个配置user配置这么一个对象配置userOK那需要各位注意的是啊我们这个配置user呢就需要对它进行一个构造一个返回结果那对于我们构造的返回结果其实怎么构造是一个问题那在我们这边呢
[04:15] result当中我们构造的时候其实全部把它带分页的放置到一个公共的返回的模型当中这个公共的返回模型呢就叫做page result那page result里面有total有rosesroses代表的是列表total代表的是我们的一个总数量那所以呢我在这边需要去构造page result有时候就userpage result等于new一个page
[04:45] result那这个配置result里面的参数需要两个第一个呢就是我们的列表第二个就是有多少条那列表呢其实在SpringData这一批分钟的配置对象里面有所以我们这边可以拿过来打点get content得到list好了打点get total点get total elements得到它的总条数即可嗯这边呢有点问题啊换一个位置呢OK可以了
[05:25] 那这样一来我们已经构造好了PageResult那接下来呢我们就可以做一个返回Result呢把PageResult放到里面哎就可以了那PageResult里面其实里面呢就是有total有ros下桥符合我们API返回标志的有total有rosOK那这样一来我们的Controller其实也就已经写好了当然了这个里面呢还有一个简单的问题啊把它改掉这些不用的tunmood给它删掉OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 Spring Boot 项目中，如何在 UserController 中实现分页查询功能，包括引入 Pageable、PageResult 类，以及使用 @RequestParam Map 接收分页参数。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 UserService.java 文件，其中包含 save 和 update 方法，用于保存和更新用户数据，涉及 IdWorker 生成 ID、设置密码、状态等操作。
画面 2: 展示项目结构，聚焦在 UserContoller.java 文件，位于 com.ihm.system.Controller 包下。
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
package com.ihm.system.Controller;

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
        //2.调用Service保存
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
    //2.调用Service更新
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
package com.ihm.system.Controller;
import com.ihm.common.Controller.BaseController;
import com.ihm.common.entity.PageResult;
import com.ihm.common.entity.Result;
import com.ihm.common.entity.ResultCode;
import com

