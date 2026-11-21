# 09-分配角色：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\09-分配角色：代码实现_【海量资源尽在 ubkz.com】.mp4
- 时长 7分6秒（音频 426s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们找到我们的idea在我们的idea当中呢可以给它来一个方法当然这个方法呢是也是放到用户这个这一端了在用户这一端呢我就写到最上边了就叫分配角色那对于分配角色我们如何去完成呢首先大的思路各位肯定要有我们先去配置一个方法这个方法指定上我们相关的一些配置的一些参数那好了这边呢可以给它来一个我们的请求
[00:36] 来一个我们的方法OK那我们来看一下对于我们请求的链接是什么那请求链接叫做user-就是分配角色拿过来好了我们的请求方式呢叫做put那我这边就是put那接下来注意我们的参数有ID
[01:01] 当前的请求ID有肉IDS指的是它一个数组列表所以对于我这个代码呢参数必然是有那我们这边参数呢我就以MAP的形式进行接收所以我这边写一个MAP结合当然了这些不管是MAP还是对象都是SpriteVC为我们做好的死去类型的Object好了我这边就叫做MAPOK那好了接下来呢我们把这个方法构造成功了之后
[01:30] 我不太喜欢他这个程序报错我就直接构造一个成功的返回succes代表成功的返回那各位来看我这个分配角色分配角色其实它的返回呢就是这几个值啊就是这几个值所以我们不需要关注其他太多的那接下来我想跟各位说的是分配角色我们应该如何进行分配那分配角色呢其实比较简单首先呢我们应该获取到我们的
[01:59] 被分配的用户ID那接着呢第二件事获取到我们角色的ID列表ID集合那由于我们这个工程呢是使用SpringDataGPA配置了多对多那么可以借助多对多它内部的一些机制直接设置他们的关系自动的进行更新就能更新他们之间的多对多关系的数据
[02:29] 所以我们这个代码写起来不难那我们首先呢一步一步的来看获取到了ID获取的结合之后接着做第三步就是调用Service完成角色分配好了获取被分清的ID那怎么去做很简单map打点get那我们传递的一个参数名称呢就叫ID好了那这样一来死菌类型的user ID就已经有了当然了这边需要做一个强制转型死菌类型
[03:02] 好了那接下来呢获取到角色的ID列表好了来历史集合死君类型OK比如说我就叫做肉IDS那等于这边呢同样也需要做一个强制转型map打点get我们这边传递的参数名字叫做肉IDS肉IDS好了那接下来呢我们就可以调用Service完成操作肉serviceservice不是肉啊user Service
[03:42] 打点我们可以进行分配那这个分配方法呢我就打点就是assign rows就可以了那当然了我需要传递两个参数第一个就是user id第二个就是我们的row ids那对于Service方法还没有那我们找到Service方法去填写一个分配权限的这么一个分配角色的这么一个方法其实就可以了userservice写到最下面分配角色public view id开始分配
[04:18] 好了里面接受的是一个死菌类型的user idlist类型的我们叫做row idsok好了那这Service代码呢我们又如何去写呢其实不难首先呢第一件事根据id查询用户这是第二件事设置用户的id集合设置用户的角色集合好了接着第三件事更新用户集合
[04:57] 好了那根据ID查询呢比较简单了user.do打点findbyID把userID传进去好了千万别忘了打点get那这样一来得到了用户对象那用户对象搞定了之后我们开始去设置它这个用户集合所以我需要构造一把set肉就叫肉丝了肉丝等于new一个hashi set
[05:34] 好了那接下来呢在底下iter 放循环注意放循环的时候row ids 死菌row id 那一个一个的row id其实我们看一下这个row对象究竟有没有所以这边呢我需要注入进来row 的dook那在这边我们就可以row do 打点find by idrow id 放进去打点get得到了角色那得到角色
[06:10] 我们需要把它放到角色集合当中肉丝点add肉好了那这样一来那这样一来我这边有了角色的一个集合那就是说我要把用户给用户分配给用户分配上这张角色那怎么给他分配只需要设置用户和角色集合之间的关系就可以了OK设置关系user打点set它有一个set方法set肉丝把肉丝放进去那这样一来
[06:42] 用户里面就包含了一个ROS的集合那我一会更新用户的时候它就会自动的把我们这个多表关系给我维护上好了user打点save userOK那这样一来我分配角色这个代码咱们就已经写好了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现用户与角色的分配功能，包括控制器层、服务层和数据访问层的代码编写与调试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PermissionController.java 文件，包含 findAll 和 findById 两个 GET 请求方法，用于查询权限列表和单个权限。
画面2：展示 API 文档页面，列出 /user、/user/assignRoles、/login、/profile 等接口，用于用户管理。
画面3：展示 UserController.java 文件，包含 save 方法，用于保存用户信息。
画面4：展示 API 文档页面，显示 /user/assignRoles 接口的请求体和响应体结构。
画面5：展示 UserController.java 文件，正在编写 assignRoles 方法的 PUT 请求处理逻辑。
画面6：展示 UserController.java 文件，继续编写 assignRoles 方法，准备调用服务层。
画面7：展示 UserController.java 文件，完成 assignRoles 方法的 PUT 请求处理逻辑。
画面8：展示 UserService.java 文件，正在编写 assignRoles 方法，用于处理用户角色分配逻辑。
画面9：展示 UserService.java 文件，正在编写 findUserById 方法，用于根据用户 ID 查询用户信息。
画面10：展示 UserService.java 文件，正在导入 Role 类，用于处理角色对象。
画面11：展示 UserService.java 文件，完成 findUserById 方法的实现。
画面12：展示 UserService.java 文件，完成 assignRoles 方法的实现，包括获取用户、创建角色集合、遍历角色 ID 并查询角色对象。
画面13：展示 UserService.java 文件，完成 assignRoles 方法的实现，包括将角色对象添加到用户的角色集合中。
画面14：展示 RoleService.java 文件，显示其包路径和导入的依赖类。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@RequestMapping(value = "/permission", method = RequestMethod.GET)
public Result findAll(@RequestParam Map map) {
    List<Permission> list = permissionService.findAll(map);
    return new Result(ResultCode.SUCCESS,list);
}

//根据ID查询
@RequestMapping(value = "/permission/{id}", method = RequestMethod.GET)
public Map map = permissionService.findById(id);
return new Result(ResultCode.SUCCESS,map);
```

画面3：
```java
@RequestMapping(value = "/user", method = RequestMethod.POST)
public Result save(@RequestBody User user) {
    //1.设置公司ID
    user.setCompanyId(companyId);
    //2.设置公司名称
    user.setCompanyName(companyName);
    //3.调用Service保存企业
    userService.save(user);
}
```

画面5：
```java
@RequestMapping(value = "/user/assignRoles", method = RequestMethod.PUT)
public Result save(@RequestBody Map<String,Object> map) {
    //1.获取用户ID
    String userId = (String) map.get("id");
    //2.获取角色ID列表
    List<String> roleIds = (List<String>) map.get("roleIds");
    //3.调用Service完成角色分配
    userService.assignRoles(userId,roleIds);
    return new Result(ResultCode.SUCCESS);
}
```

画面8：
```java
if(!StringUtils.isEmpty(map.get("hosDept"))){
    if("0".equals(String) map.get("hosDept")){
        list.add(criteriaBuilder.isNull(root.get("departmentId")));
    }else{
        list.add(criteriaBuilder.equal(root.get("departmentId"),map.get("hosDept")));
    }
}
return criteriaBuilder.and(list.toArray(new Predicate[list.size()]));
```

画面9：
```java
public void assignRoles(String userId,List<String> roleIds) {
    //1.根据ID查询用户
    User user = userDao.findById(userId).get();
    //2.设置用户的角色集合
    Set<Role> roles = new HashSet<>();
    //3.遍历角色ID
    for (String roleId : roleIds) {
        //4.查询角色对象
        Role role = roleDao.findById(roleId).get();
        //5.添加到角色集合
        roles.add(role);
    }
    //6.更新用户
    user.setRoles(roles);
    //7.保存用户
    userDao.save(user);
}
```

画面14：
```java
package com.ihrm.system.Service;
import com.ihrm.common.utils.IdWorker;
import com.ihrm.system.dao.PermissionDao;
import com.ihrm.system.domain.Permission;
import com.ihrm.system.domain.Role;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.*;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

