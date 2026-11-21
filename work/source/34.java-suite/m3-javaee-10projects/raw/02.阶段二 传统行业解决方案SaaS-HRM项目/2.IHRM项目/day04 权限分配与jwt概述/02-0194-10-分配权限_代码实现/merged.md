# 10-分配权限：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\10-分配权限：代码实现_【海量资源尽在 ubkz.com】.mp4
- 时长 10分1秒（音频 601s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了分配角色呢这个代码比较简单那接着除了分配角色之外我们这边呢还有一个就是用就是角色这边其实还有一个叫做分配权限的这么一个功能那简单的看一下分配权限呢其实这个传递的参数IDPermission IDS跟我们刚才是一样的并且呢这边它也有返回跟我们刚才基本上都是一模一样的所以两个比较像我们就先把这两个Java代码都写好
[00:30] 那我们接下来就把这个分配权限的这个功能也想写好那分配权限其实就是对角色他究竟能够访问什么菜单究竟能够访问什么按钮究竟能够访问什么API的一个实现那我们在处理的过程当中呢有一个需要各位注意的细节问题是这样就是我们都知道我们前端的权限呢其实分成了我们的菜单
[00:56] 那菜单里面又有按钮那我想问各位一句话如果说你能够访问这个按钮那我想问这个按钮背后它的这个按钮背后它的API你能不能访问是不是逻辑上是这样的你如果能够访问这个按钮的话它背后是不是所带的这个API必然也能够访问啊所以对于我们来说对于我们来说前端你去分配权限的时候前端你去分配权限的时候我这边只显示的只有
[01:26] 菜单这是菜单那底下是一个一个的按钮底下是一个一个按钮所以对于我这个需求来说我如果勾选上了这个菜单或者勾选上了这个按钮那这个菜单或者这个按钮背后所联系到的我们叫做API权限必然也就可以给它自动分配了就这么一个逻辑好了这个逻辑各位能够看懂的话那接下来我们就可以完成整个分配的这么一个过程
[01:56] 好了呢这个呢是对角色的一个操作所以我在角色这边添加一个我们分配角色的一个方法当了这个代码呢跟我们这边control的代码跟我们分配我们分配权限的这个代码跟分配角色的这个代码差不多所以我就直接从分配角色这边call过来然后呢我们简单的做一个修改改一改其实就可以了好了这边叫做分配权限那么分配权限请求的参数呢我们再来看一下有ID好了还有一个叫做
[02:32] Permiss ID那这个呢其实就是被分配的角色的ID那底下这个就是获取我们的叫做全线的ID列表好了那接下来调用Service完成我们全线分配那Service就是row Service去完成全线分配就可以了PEERMS好了那接下来这边就是row ID写的稍微规范一点row ID好了PEERMSPE PE
[03:07] RMIDS好了现在稍微好看一点好了那接下来呢我们可以在Row Survey当中添加一个分配权限的方法那分配权限的方法PublicView IDOK拿过来那传递的参数呢首先第一个死菌类型的我们叫做Row ID好了第二个我们是List死菌类型的PRMIDS
[03:43] 好了我们这个分配的思路呢也是跟刚才差不多啊跟方用户分配角色角色分配权限都是差不多因为是多对多关系所以我们跟刚才的逻辑是一样的第一个先获取分配的角色对象好了接着第二件事构造角色的权限集合好了第三件事设置角色和权限的关系好了接着第四件事
[04:14] 更新角色即可好了那么一个一个来看首先呢在这边肉ID呢我已经有了permission呢DU呢我也已经搞进来了那接下来分配角色对象肉ID打点find by ID肉ID传进去打点叫做get那这样一来得到我们的角色那角色有了之后构造集合set这里面存的是permission
[04:46] 好了就叫perms等于new一个hashiset好了那构造集合呢其实比较简单了iter for循环进行构造注意我们循环的是全线列表全线的id列表那构造它这个全线列表的时候需要各位要注意一下我们这边呢需要通过permission do进行查询点find by id
[05:17] Row Permission ID那这样一来我们就能得到这么一个打点get抱歉打点get那这样一来呢我们就能得到它的权限了那得到权限之后呢需要各位注意一个点啊就是说我们现在前端传递的内容它这个ID啊只有我们的菜单和我们这个按钮那不管是菜单和按钮背后必然还有API
[05:48] 所以我们需要自动的对于它所背后的这些API权限进行复制啊,因为我们前端肯定不分配API,我们只是知道菜单,只是知道按钮,那背后执行的逻辑,我们自动的帮它进行划分,那背后进行划分,那是怎么做的呢?
[06:07] 咱们就以这张图为例,其实一个员工管理,他这个菜单进入的是一个页面,这个页面呢,可能里面有一个按钮,那这个按钮后边是不是挂载了我们的一个API啊?
[06:20] 所以你会发现这个是一个父子级关系父子级关系那如果说员工这边有按钮那按钮底下背后就必然有一个API那他们找的时候我们是不是用这个我们就可以用当前按钮的ID这个ID作为副ID从数据库里查以他作为ID他作为副ID从数据库查那副ID不就代表他的爸爸吗所以找他的爸爸
[06:53] 看一下他这个他的爸爸的ID是不是就是他那如果是我们自动对他复试全线那当然了我们这边需要各位注意的点其中其中我们这边要查的时候要根据副ID查那副ID就是你当前划分全线的ID那同时我们只查询API那所以呢我在这边呢的需求就很明确了我需要根据副ID和我们叫做
[07:25] 类型查询权限权限列表查询的是API权限列表那这个代码如何去做呢其实不难其实不难Permission.do我们可以在Permission.do当中呢写一个方法得到的是粒子集合好了这个就是Find By那Find ByType类型And
[08:00] 除了类型之外还有PID那我们这边呢可以传递一些参数比如说呢int类型的tab那比如说死菌类型的PID即可那DU我补充好了这个方法那我们在Service上直接可以打点调用find by tab and PID那tab我们查评的全部都是3我们写过了一个常量content打点API下来那好了PID用的什么就是permission
[08:30] 打点get idok那这样一来呢我们这个list集合呢其实也就写好了api list那接着把这api list附给我们的permissionadd allapi listok那api的权限这个就是自动赋予api权限那api权限我们给了之后呢当然我们当前的这个菜单或者当前的这个按钮权限也应该告诉他所以呢接下来呢我们就可以
[09:08] Promission打点ADDOK这个就是当前菜单或按钮的权限那这样一来我们已经把箱的这些呢全部Promission抱歉写错了那当前这样一来我们就把当前的菜单或者按钮权限给了当然了这个背后它设计的API权限也自动复制那我们构造到了一个set集合里那我们就可以
[09:41] 设置赛结合和角色的关系row打点set我们叫做permissions把我们这个permissions放进去接着更新角色即可row.do.saverow好了那这样一来我这个分配权限的方法也已经写好了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SaaS-HRM 系统中通过后端 Java 代码实现角色与权限的分配功能，包括前端界面操作、API 文档、控制器与服务层代码编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 HRM 系统的员工列表页面，左侧导航栏选中“员工”，页面显示员工编号、姓名、手机号、部门等信息。
画面 2: 展示 API 文档页面，列出与角色相关的 API 接口，包括 POST /role（添加角色）、GET /role（获取角色列表）、PUT /role/{roleId}（修改角色）、DELETE /role/{roleId}（删除角色）等。
画面 3: 展示前端界面，弹出“为【人事经理】分配权限”的对话框，其中“员工管理”下的“用户删除按钮”、“删除用户角色”、“用户修改按钮”等选项被勾选。
画面 4: 展示 IntelliJ IDEA 中 RoleController.java 的代码，包含添加角色、更新角色、删除角色的注解和方法。
画面 5: 展示 IntelliJ IDEA 中 RoleController.java 的代码，新增了保存权限分配的 PUT /user/assignRoles 接口方法。
画面 6: 展示 IntelliJ IDEA 中 RoleService.java 的代码，包含 assignPerms 方法的注释和部分实现。
画面 7: 展示 IntelliJ IDEA 中 RoleService.java 的代码，光标位于 assignPerms 方法的注释“//3. 设置角色和权限的关系”处，提示“Press Ctrl+空格 to choose the selected...”。
画面 8: 展示 IntelliJ IDEA 中 RoleService.java 的代码，assignPerms 方法中已添加注释“//3. 设置角色和权限的关系”。
画面 9: 展示 IntelliJ IDEA 中 RoleService.java 的代码，assignPerms 方法中已添加注释“//3. 设置角色和权限的关系”，并弹出一个“SaaS-HRM系统API文档 - Google Chrome”窗口。
画面 10: 展示前端界面，弹出“为【人事经理】分配权限”的对话框，所有权限选项均未勾选。
画面 11: 展示 IntelliJ IDEA 中 PermissionDao.java 的代码，定义了继承自 JpaRepository 的接口。
画面 12: 展示 IntelliJ IDEA 中 RoleService.java 的代码，光标位于 assignPerms 方法中，提示“Press Ctrl+空格 to choose the selected...”。
画面 13: 展示 IntelliJ IDEA 中 RoleService.java 的代码，assignPerms 方法中已添加注释“//3. 设置角色和权限的关系”，并添加了权限赋值逻辑。
画面 14: 展示 IntelliJ IDEA 中 RoleService.java 的代码，assignPerms 方法中已添加注释“//3. 设置角色和权限的关系”，并添加了设置角色权限关系和保存角色的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```java
package com.ihrm.system.Controller;

import com.ihrm.system.Controller;
@RquestMapping("/sys")
public class RoleController extends BaseController{
    @Autowired
    private RoleService roleService;

    //添加角色
    @RequestMapping(value = "/role", method = RequestMethod.POST)
    public Result add(@RequestBody Role role) throws Exception {
        role.setCompanyId(companyId);
        roleService.save(role);
        return Result.SUCCESS();
    }

    //更新角色
    @RequestMapping(value = "/role/{id}", method = RequestMethod.PUT)
    public Result update(@PathVariable(name = "id") String id, @RequestBody Role role) throws Exception {
        roleService.update(role);
        return Result.SUCCESS();
    }

    //删除角色
    @RequestMapping(value = "/role/{id}", method = RequestMethod.DELETE)
    public Result delete(@PathVariable(name = "id") String id) throws Exception {
        roleService.delete(id);
        return Result.SUCCESS();
    }
}
```

画面 5:
```java
//添加角色
@RequestMapping(value = "/role", method = RequestMethod.POST)
public Result add(@RequestBody Role role) throws Exception {
    role.setCompanyId(companyId);
    roleService.save(role);
    return Result.SUCCESS();
}

//更新角色
@RequestMapping(value = "/role/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable(name = "id") String id, @RequestBody Role role) throws Exception {
    roleService.update(role);
    return Result.SUCCESS();
}

//删除角色
@RequestMapping(value = "/role/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(name = "id") String id) throws Exception {
    roleService.delete(id);
    return Result.SUCCESS();
}

//分配权限
@RequestMapping(value = "/user/assignRoles", method = RequestMethod.PUT)
public Result save(@RequestBody Map<String, Object> map) {
    String userId = (String) map.get("id");
    List<String> roleIds = (List<String>) map.get("roleIds");
    userService.assignRoles(userId, roleIds);
    return new Result(ResultCode.SUCCESS);
}
```

画面 6:
```java
@Autowired
private IdWorker idWorker;
@Autowired
private RoleDao roleDao;
@Autowired
private PermissionDao permissionDao;

//分配权限
public void assignPerms(String roleId, List<String> permIds) {
    //1.获取角色对象
    //2.获取角色的权限集合
    //3.设置角色和权限的关系
    //4.更新角色
}

//添加角色
public void save(Role role) {
    //填充其他参数
    role.setId(idWorker.nextId() + "");
    roleDao.save(role);
}

//更新角色
public void update(Role role) {
    //更新角色
    roleDao.save(role);
}
```

画面 7:
```java
//3. 设置角色和权限的关系
//4. 更新角色
```

画面 8:
```java
//3. 设置角色和权限的关系
```

画面 9:
```java
//3. 设置角色和权限的关系
```

画面 11:
```java
package com.ihrm.system.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;

public interface PermissionDao extends JpaRepository<Permission, String>, JpaSpecificationExecutor<Permission> {
}
```

画面 12:
```java
//3. 设置角色和权限的关系
```

画面 13:
```java
//3. 设置角色和权限的关系
Permission permission = permissionDao.findById(permId).get();
List<Permission> apiList = permissionDao.findByTypeAndPid(PermissionConstants.PERMISSION_API, permission.getPid());
perms.addAll(apiList);
perms.add(permission);
```

画面 14:
```java
//3. 设置角色和权限的关系
role.setPermissions(perms);
roleDao.save(role);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

