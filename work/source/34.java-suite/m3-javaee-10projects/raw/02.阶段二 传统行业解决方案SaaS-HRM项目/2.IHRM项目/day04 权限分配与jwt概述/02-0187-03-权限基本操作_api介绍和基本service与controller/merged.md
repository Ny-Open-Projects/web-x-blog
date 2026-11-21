# 03-权限基本操作：api介绍和基本service与controller

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\03-权限基本操作：api介绍和基本service与controller_【海量资源尽在 ubkz.com】.mp4
- 时长 7分10秒（音频 430s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] DO实体类都写好了之后接下来我们关注的其实就是Controller和我们的Service业务逻辑层那写Controller和写我们Service的依据呢其实就是我们的API接口那在今天这边呢我已经把这些API接口也给各位准备好了全线相关的首先呢各位来看增加那对于增加来说呢其实请求的地址跟我们之前的差不多只不过人家增加的时候这边你会发现有一个人家的备注
[00:32] 就是说你添加过来的有很多的内容那各位来看里面有ID descriptionname typepid codeAPI level还有menu还有pwncut什么什么这些那各位如果注意的话你会发现这个一个里面它好像包含了我们刚才实体类里面的所有包含了我们的所有那这里面我们实体类呢还得打开看一下权限API里面什么什么level什么什么method还有
[01:03] menu里面什么menu还有compound等等好像包含了所有那也就意味着它一个方法既能保存API权限又能保存按钮权限又能保存菜单权限那你怎么知道你现在保存的究竟是菜单按钮还是API呢注意人家这边说了有一个值不同类型代表不同的也就是tap也就是说我们需要根据tap值来进行判断如果tap
[01:32] 它代表的是如果tab它代表的是一个比如说1那就是菜单2按钮3API所以这边不同类型要做不同的处理那这是第一个好了接着还有第二个get那get代表的是查询所有的列表那查询列表的时候这边呢也有很多个人家get传递过来的一些参数第一个类型按照类型查人家可能第一个就说呢我要只传1只查菜单传2只查按钮传3只查API
[02:01] 那如果传0他说了我查菜单查按钮这是人家的要求那还有一个PIDPID就是副ID我查一下这个比如说这个菜单下它有多少个按钮或者这个菜单下它有多少个API所以有可能要传副ID当然了空代表没有嘛那还有接着还有第三个Unvisible就是说0代表查询全部就是我不管你什么了只要有我就查1
[02:29] 它代表的是只查企业的所以这几个是要有一个并行的一个判断的OK好了这是我们的第二个结率表还有第三个根据ID查询那根据ID查询人家会传递一个ID过来并且这边各位来看人家的响应人家的响应人家响应的时候会要你这里面的所有内容还是跟刚才一样这一个实体里面可能包含了全线的实体可能还包含了API的可能还包含了按钮了还包含了我们菜单的
[02:59] 还是之前那句话还是之前那句话跟你的类型有关你如果传递的是API那就是API相关的属性给它进行提供如果传递的是菜单那就是菜单属性如果传递的是按钮那就是按钮属性OK这个也说清楚了接下来呢还有一个删除那根据删除根据ID删除那这个其实没有哎这错了这个是根据ID修改那这个根据ID修改其实跟我们之前根据新增权限基本上是一样的
[03:29] 当然还有最后一个删除删除其实没什么可说的删除权限删除人家资源就可以了OK好了这个就是跟各位简单的来看了一下我们这个API那接下来我们跟之前稍微做一点点不同的处理因为思维层里面的EO逻辑可能是相对来说现在有点复杂了所以我个人先把Controller给它写好那在这边呢找到Controller找到Controller补充一个方法
[03:59] 补充一个类比如说呢我就叫做permi ssiontrol Controller全线Controller好了里面的配置跟之前基本上都是大同小异的Ctrl c拿过来Ctrl v 给几个注解那接下来呢在这里面我要去完成这么几个方法这个方法名呢我也从这边call了我也从这边call过来了好了简单的各位来看一下首先呢第一个叫做保存里面的业务逻辑先不管
[04:33] 里面的业务逻辑先不管先不让他报错好了那这边请求的呢注意看人家的请求地址请求的地址就叫permission所以我这边permission注意了系统微服务前面加了已经加了前缀SOS好了那接下来第二个呢叫做翻到查询列表查询列表呢同样也是permission中间还是那句话中间我先不管它全部都删掉好了这边呢为了
[05:09] 这边直接跟上面一样好了接着根据ID查询先不管它全部都写这样它不报错好了这边请求的也是Promission把ID拿过来一样的套路修改一样的套路好了根据ID删除一样的套路OK那这样一来我基本Controller的大的架子其实也已经搞好了
[05:45] OK这个大的架子我们搞好了之后接下来呢我们来看Service那跟之前的套路一样Service我也想把基本的架子给它搞过来那这个Service呢我就叫做permissionpermission没问题serviceOK好那这个里面呢跟之前写Controller是一样的咱们就稍微快一点permission dealpermission deal
[06:22] 好了那接下来呢里面的save方法呢这边点save啊算了咱们来一个快点的吧碰到大写userreplace all碰见小写userreplace allok好了那接下来呢把箱子内容做一个简单的修改就可以了保存先不管它更新也不管它根据来的查留着翻照一会儿再说
[07:03] OK那这样一来呢咱们基本的把这个结构其实先给它已经搭建A出来了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个权限管理模块的前后端实现，包括API文档、实体类、控制器和Service层的代码编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示API文档，显示权限模块的POST、GET、PUT、DELETE四个接口，以及Models部分的Permission和PermissionList。
画面2：IDEA中展示项目结构，当前选中的是`PermissionApiDao.java`，代码为`public interface PermissionApiDao extends JpaRepository<PermissionApi, String>, JpaSpecification`。
画面3：IDEA中展示`PermissionPoint.java`实体类代码，包含注解`@Entity`、`@Table`，以及字段`id`、`pointClass`、`pointIcon`、`pointStatus`。
画面4：API文档中展示GET /permission接口的参数，包括type、pid、entVisible三个必填参数。
画面5：API文档中展示GET /permission接口的响应示例，JSON结构包含code、message、data字段，data中包含id、description、type等字段。
画面6：API文档中展示DELETE /permission/{permissionId}接口的参数，仅包含permissionId。
画面7：IDEA中展示`PermissionPoint.java`实体类代码，光标在`pointStatus`字段上。
画面8：IDEA中展示`UserController.java`控制器代码，包含保存用户和查询企业列表的两个方法。
画面9：IDEA中展示`PermissionController.java`控制器代码，包含保存权限的POST方法。
画面10：IDEA中展示`PermissionController.java`控制器代码，包含查询权限列表的GET方法。
画面11：IDEA中展示`PermissionController.java`控制器代码，包含根据ID查询权限的GET方法。
画面12：IDEA中展示`PermissionService.java`服务类代码，光标在`@Autowired`注解上，下方有自动补全建议。
画面13：IDEA中展示`PermissionService.java`服务类代码，光标在`public void save(Permission permission)`方法内，正在设置权限ID。
画面14：IDEA中展示`PermissionService.java`服务类代码，光标在`public void deleteById(String id)`方法内，正在执行删除操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.ihrm.system.dao;

import ...

/**
 * 企业数据访问接口
 */
public interface PermissionApiDao extends JpaRepository<PermissionApi, String>, JpaSpecification
```

画面3：
```java
@Entity
@Table(name = "pe_permission_point")
public class PermissionPoint implements Serializable {
    private static final long serialVersionUID = -1087411490113957485L;

    // 主键
    @Id
    private String id;

    // 权限代码
    private String pointClass;
    private String pointIcon;
    private String pointStatus;
}
```

画面8：
```java
@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @RequestMapping(value = "/user", method = RequestMethod.POST)
    public Result save(@RequestBody User user) {
        user.setCompanyId(companyId);
        user.setCompanyName(companyName);
        // 保存用户
        userService.save(user);
        // 返回结果
        return new Result(ResultCode.SUCCESS);
    }

    @RequestMapping(value = "/user", method = RequestMethod.GET)
    public Result findAll(int page, int size, @RequestParam Map map) {
        map.put("companyId", companyId);
        // 返回结果
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面9：
```java
import java.util.Map;

// 1. 解决跨域
@CrossOrigin
// 2. 设置访问路径
@RestController
@RequestMapping(value = "/sys")
public class PermissionController {
    // 保存
    @RequestMapping(value = "/permission", method = RequestMethod.POST)
    public Result save(@RequestBody User user) {
        // 保存权限
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面10：
```java
// 查询列表
@RequestMapping(value = "/permission", method = RequestMethod.GET)
public Result findAll(int page, int size, @RequestParam Map map) {
    return new Result(ResultCode.SUCCESS, pageResult);
}
```

画面11：
```java
// 根据ID查询
@RequestMapping(value = "/permission/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) {
    User user = userService.findById(id);
    return new Result(ResultCode.SUCCESS, user);
}
```

画面12：
```java
@Service
public class PermissionService {
    @Autowired
    private PermissionDao permissionDao;
    @Autowired
    private PermissionMenuDao permissionMenuDao;
    @Autowired
    private PermissionPointDao permissionPointDao;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi;
    @Autowired
    private PermissionApiDao permissionApiDao;
    @Autowired
    private PermissionMenu permissionMenu;
    @Autowired
    private PermissionPoint permissionPoint;
    @Autowired
    private PermissionApi permissionApi

