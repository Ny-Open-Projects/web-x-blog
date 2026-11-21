# 23-SasSHRM中基于shiro的认证授权：用户授权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\23-SasSHRM中基于shiro的认证授权：用户授权_【海量资源尽在 ubkz.com】.mp4
- 时长 11分2秒（音频 662s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 完成了系统微服务我们的share的一个构造并且我们是验证了一下用户的认证和判断它是否登录的这么一个逻辑那如果说在企业微服务里面我们想要类似的功能如何去做呢其实也比较简单在企业微服务里面我们不涉及到认证的过程我们只是需要借助share帮我们进行全新的一个验证以及它是否登录的这么一个提示那所以对于我们来说呢如何去做很简单
[00:30] 不需要添加额外的代码咱们只需要做一个基本的配置就可以了那这个配置首先呢打开我们这边企业微服务的配置文件那企业微服务呢我们知道也要想获取用户数据同样的也要有我们叫做Redis的相应配置把Redis这一段Ctrl C拿到企业微服务里好了那接下来呢就是对于使用Sherlock有一个Sherlock的自己的配置文件我们也是从系统微服务之间call过去一个就可以了Ctrl C也call过来
[01:07] OK那靠过来之后呢我们需要做一些简单的改造首先呢就是说对于我们现在的这个room不需要用user我们其实用hrmroom即可OK那这样一来我们这个企业微服务就已经改造完成了当然了上边这边有一个不存在的包我们把它做一个修改好了那这样一来我们企业微服务已经改造成功了那改造成功了这边呢还是希望跟各位简单的再来提一下是在这儿就是说我们这个过滤器的配置
[01:37] 过滤器的配置在这个里面呢我们其实这个不要其实也可以那需要各位注意的是我们所有企业微服务里面的请求地址也是需要叫做登录或者认证之后才能够访问好了这个我们也改造好了之后我们就可以启动一把企业微服务来启动好了启动好了企业微服务呢我们也是可以做一个简单的测试来看一下效果打开Postman
[02:14] 好了post们呢我已经打开了那接下来呢我们就可以访问一下咱们的企业微服务localhost冒号9001那么可以随意找一个案例一起来看一下效果好了在这边呢我就比如说呢以企业微服务里面的部门来举例好了打开部门Controller那我们请求的地址呢咱们就是company下的我们这边呢就拿他企业部门列表了
[02:52] OK各位来看目前来说没有登录没有登录的话我发送请求他是不是应该让我去登录才可以那点send给我来看你还没有登录那接下来呢就是说在我这边sys-login去登录一把走好了告诉我登录成功但是登录成功我这边企业就能访问吗部门就能访问吗那各位我们再来走你会发现还是告诉我你没登录那为什么没登录是因为我们这边的是不是投信息还没有设置啊
[03:21] 所以我们还需要去设置我们的投信息那这个投信息呢设置起来呢相对来说有点有点啰嗦啊那我在这边呢就找到它投信息的名字这个就比较繁琐了拿过来好了我们B2开头Ctrl C拿过来好了接下来我们登录的得到的Session IDCtrl C也拿过来走各位来看现在是不是就代表我已经登录成功了
[03:57] OK那这样一来我们的企业微服务和我们的系统微服务已经全部都配置成功了那全部都配置成功了之后就是说呢我们可以把整个的这个案例和我们的前端都结合起来OK那这样一来我们的企业微服务里面Sherlock其实也已经配置成功了那配置成功之后呢其实我们就可以把我们的后端代码和我们的前端代码联合的全部都加在到一起咱们来看一下
[04:28] 我们今天改的内容究竟能不能使用以及用户授权的过程应该如何操作好了在这边呢把所有的代码都关掉我已经打开了我前端的VS Code并且已经启动成功了那接下来呢我们只需要打开浏览器好了在上面呢Localhost 8080访问OK好了呢首先我们来验证一下登录究竟受不受影响那我们都知道有三个用户账号1 2 3
[04:56] 那对于我们来说二代表的是一个企业的他的一个超级管理员好了那接下来登录进来来各位来看登录并不会受到任何的影响并且这边的查询组织架构也没有问题员工查询也没有问题等等等等都可以好了其实这就意味着我们不会对我们的前端产生任何的影响并且能够正常的访问好了那前端的这边员工呢刚才由于咱们也做了一点点基础的设置所以呢
[05:24] 我们先新增一个员工看一下效果究竟可不可以比如说呢这边就来一个我们叫做LL手机号呢随便输13800就1380012345我就来14了这个其实用什么都无所谓反正一会要都删掉它好了随便来一个转正时间也随便填提交好了这边呢保存成功保存成功我们回到数据库刷新一把需要各位关注的是LL
[05:56] 它的密码MD5加密的没什么问题好了这些都没什么并且是一个普通用户我们刚才修改过内容好了那这个我们看过了之后接下来就是关注我们这个整个权限里面的最后一个就是如何借助share进行授权其实借助share授权呢是比较简单的比如说呢我们还是以用户删除为例那么的前端呢控制了我们的菜单控制了我们的按钮
[06:26] 但是API还没有做,那API我们是不是就可以借助Sherlock它的权限控制来做?
[06:32] 那我们都知道点击删除的时候,访问的其实是我们的用户Controller当中的一个方法。
[06:37] 好了,我们一起来找到我们的代码当中的用户Controller,UserController。
[06:43] 那在UserController里面我们执行的是Delete方法。
[06:48] 那我想要对delete的方法进行控制我们应该如何去做呢首先希望各位一定一定要注意就是说我们要借助share的话需要你把所有的接口也就是我们的API录入到我们的权限的设置当中全部都要录入进来比如说呢用户管理这边它有很多的按钮用户删除按钮我们绑定了查看一下用户删除按钮那在用户删除按钮下我们给它添加了API的一个权限
[07:18] 那比如说就是删除那所以呢对于你要访问的这个接口要做闲控制所有的这个API都应该进行绑定上绑定上之后再对它进行负责权限那我们对删除按钮绑定的权限绑定的这个删除按钮的权限我们可以一起来看一下它的权限标志API user delete这是我们的标识也就是我们查询出来的那个API标识那对于我们而言如何对这个标识进行控制我们都知道
[07:45] 那这个API对应的是我们删除的这个控制方法所以我在上边借助注解request permission那你必须具备API user delete这个权限才能够对它进行删除好了呢这个我们配置上了之后接下来千万千万别忘了一件事情那我们现在使用注解的形式进行用户的授权注解的形式进行用户授权如果你没有具有不具备当前权限的话
[08:17] 它会抛出异常所以注解一出场我们必然要对异常进行控制好了在common Controller当中在commonexceptionhandler当中好了我们要对咱们的异常进行控制那我们这个异常控制我们其实可以写到这里面当然了也可以写一个新的我们叫做方法
[08:42] 好了找到我们之前写好的base exception handler把里面这段代码呢直接control ccall到我们的工程这边ok call过来好了接下来呢就是说我们这边的返回值全部都是返回的result做一个做一个简单的改造就可以了returnnew一个我们叫做result这么一个对象那我们可以借助我们写好的一些枚举类里面呢有权限不足的一个提示我们把它抄过来就可以了权限不足ok关掉copyok那这样一来
[09:15] 我们对于授权两个操作就已经搞定了首先第一件事我们在需要进行权益控制的方法上以注解的形式配置第二个由于用了注解权限不足的时候会抛出异常针对抛出异常的时候我们怎么做写一个异常处理类就可以了接下来我们就可以重新启动一下系统微服务我们来验证一下用户是否对用户的删除权限能否控制住
[09:48] 返回我们的浏览器在这边在这边那我现在登录的是我们这个企业的一个超级管理员那我需要对这个权限呢做一个简单的分配比如说呢咱们有一个用户叫做JBZ我们给他分配了一个角色那这个角色是人事经理那我们来看一下就是对于咱们这个人事经理而言他的权限他的权限有很多注意我已经把用户删除按钮去掉了用户删除按钮没有那他也就意味着
[10:19] 这个人就是咱们JBZ这个用户他不能删OK好那接下来这边我退出切换JBZ进行登录走好了对于员工来说注意这个删除按钮我之前已经放开了就没在前端进行判断没在前端进行判断那注意我这边点击删除我们来看一下有什么效果好了当我点删除确定各位来看已经告诉我权限不足了
[10:50] 所以呢这样一来我们就可以通过share住结结合他的这个异常控制完成用户授权的这个操作OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个基于 Spring Boot 和 Shiro 的 HRM 系统的开发与功能演示，包括项目结构、核心配置、控制器逻辑、自定义异常处理及前端界面操作。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示项目结构，选中 `hrm_system` 模块，目录结构包含 `src/main/java`、`src/test`、`target`、`pom.xml` 等。
画面 2: 展示 `hrm_system` 模块下的 `java` 目录结构，包含 `Controller`、`dao`、`Service` 等子包。
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
//1.配置Spring Boot的包扫描
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
//1.配置Spring Boot的包扫描
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
    //2.调用Service完成保存
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
    //2.调用Service更新
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

