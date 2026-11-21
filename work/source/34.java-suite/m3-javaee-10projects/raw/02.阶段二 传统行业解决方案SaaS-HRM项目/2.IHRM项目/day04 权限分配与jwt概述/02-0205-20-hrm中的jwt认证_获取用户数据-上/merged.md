# 20-hrm中的jwt认证：获取用户数据-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\20-hrm中的jwt认证：获取用户数据-上_【海量资源尽在 ubkz.com】.mp4
- 时长 10分20秒（音频 620s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 用户呢现在已经登录成功了那接下来呢我们就开始做我们刚才分析的第二件事就是获取用户信息那获取用户信息呢首先呢咱们先不管什么健全不健全这件事我们先把整个的一个流程先让它能够跑通可以吧所以接下来呢我们来看一下获取用户信息单纯咱们去做应该如何去做呢很简单那用户发送请求发送过来之后我先不管你有没有token
[00:31] 我先把方法解好最后我再把token的内容加上其实就可以了所以在这边的第一件事呢我们先去查询用户当然我们现在先用的这个用户ID呢随便先给他来个1先去查那能把数据先构造好那最后我们再把这个ID先给他替换掉那我们查询好了之后接着第一件事接着第二件事我们是不是就是构造我们的返回数据
[00:57] 查询用户比较简单Find by ID其实就可以了那接着构造返回数据这个其实就比较复杂了因为我们这个返回数据呢要求的数据比较多我们可以看一下API接口获取个人信息那请求过来之后有code的flagmessage不用多说有一个data那data现在代表的是一个对象而这个对象比较复杂既不是我们的用户信息不是我们的角色信息也不是我们的权限信息它里面有很多内容
[01:23] 有mobile有username有company有ros等等等等一大堆所以呢这回呢我们不能简单粗暴的就是给他搞一个用户出来我们这边就设计自己封装一个直对象把这些给他都搞定好了所以对于我们来说呢今天要完成这个个人信息的获取其中根据ID查构造返回数据那构造返回数据我们需要自己去搞一个直对象填上mobileusernamecompanyros等等这些属性
[01:52] 那肉丝这些属性里面又有menus又有pounds又有APS其实咱们玩过权限管理其实各位就能明白这个代表的是你当前角色有什么当前这个人这个角色当中包含什么样的菜单那包含你什么样的这个按钮包含你有什么样的API那这些内容其实就是我们权限标识OK这些我们都清楚了之后那我们开始着手去写我们的代码好了在这边呢我打开我的
[02:23] 工程那在这个工程还是user Controller当中我补充一个新的方法atrequire mapping跟这边我就直接拷过来了好了这个方法呢主要目的就是用户登录成功之后之后获取用户信息那有没有参数呢一个参数都没有好了那这边请求的叫做profilep r o f l eprofile好了这边也叫profile
[02:58] 好了里面的这个代码呢我们就都删掉了都删掉了那我们执行的流程首先第一件事获取用户ID接着第二件事根据用户根据用户ID查询用户好了接着第三件事构建我们的返回值对象好了第三件第四件事第四件事我们就是响应数据其实就可以了那接下来呢我们一个一个来去
[03:29] 去做获取用户ID那这个用户ID应该怎么做呢咱们先把它搞成一个固定的值固定的值比如说呢在这里面我随便用一个比如说就叫1就叫1所以这边呢使讯user ID等于1一会儿我们再用JWT去解决它好了那接下来呢第二件事根据user ID查询user Service打点find by
[04:03] ID把user ID放进去那我们能够得到一个用户对象那得到用户对象接着呢这个用户对象里面的内容就太多了太多了并且呢不符合我们的响应内容那这个时候我们怎么办呢还是跟之前的套路一样如果有这种比较特殊的响应数据的话我们把它放到当前系统模块下的一个raise
[04:29] 放到当前系统模块下的一个叫做response文件夹下构造一个指对象其实就可以了好了那这边右键创建一个class比如说呢就叫做pro profile resultok那这个profile result里面要有什么样的内容呢我们可以根据API一个一个的来看那这一段呢它有什么我就都call过来了ctrl c拿过来ctrl vok其中private死菌类型的
[05:01] mobile这个都不用多说写多个other namecompany还有一个肉丝注意这个肉丝里面是不是又有key是一个menu里面是一个数组pounds里面是一个数组api里面是不是又是一个数组啊所以这边呢怎么去描述更加合适呢我觉得用一个map集合来描述更加合适所以我这个肉丝是一个map集合那这个map集合里面呢
[05:35] 它第一个keymenu它里面接收一数组第二个keypounds接收一数组第三个keyaps接收一数组那这样一来我当前的这个就不需要了那这些我们都已经分析清楚了之后呢在这边呢可能用到了set方法可能用到了get方法都填写完成那注意我们就开始构造它我写一构造方法那这个构造方法呢我个人习惯啊因为用户数据里面所有的数据都有
[06:05] 所以我通过用户去构造这些内容完全可以那怎么做类似点mobile等于user.getmobile类似点username等于user.getusername好了类似点company注意是企业名称user.getcompanyname用户里面都有那这边肉丝那肉丝里面接收的是三个我们叫做数组
[06:31] 能把这三个数组呢也可以给它构造出来第一个叫做menus第二个叫做points还有一个叫做apsok这个其实指的是用户权限相关的内容为什么要在登录的时候要获取这些呢是因为我们做权限管理的时候都知道我们前端要控制它的菜单要控制它的按钮所以这些必须要获取到ok那接着我们可以一起来看一下如何去做好了那其实很简单根据我们用户
[07:03] 根据我们现在用的SpringDataJP它的一些特性里面有对象导航查询你查询出用户之后直接用户打点get肉丝就能够得到所有的角色信息在自动的自动发动查询自动帮您获取到那获取到了之后我们可以iter报循环那循环的是它的每一个角色那一个角色里面有很多的权限这些不都是需要的权限吗所以我们就开始肉打点get
[07:32] 叫做 permissionsok那 permissions 有了之后perms那接下来呢我们是不是就可以还是双层循环循环我们当前的这个权限那这样一来我们去构造manus pounds和aps它里面的标识就简单的很多了好了注意这边不用 list 了我用一个 set因为有可能这边有一些重名的所以我把这个重名也过滤一下
[08:06] 里面是死菌数组死菌好了manus等于new一个hashiset那应该有三个才对不同类型的一个一样的一个好了那接下来呢我们在当中做判断构造其实就可以了当然了这些内容呢在我这个讲义当中都已经给各位准备好了那我在这直接Ctrl C拿过来Ctrl V比较并复制这都比较简单OK
[08:52] 拷过来的内容呢就是会有点点问题啊好了那接下来这个code在哪code其实就是我们sginecode等于perm.getcode那这样一来我们就已经把这三个构造好那构造好了之后放到map集合里面即可map.ros类似点ros.put好了一个一个的放进来那这边呢我copy一下
[09:38] 第一个好了接着第二个接着第三个好了那这个呢勾导方法我们写好了之后接下来呢在我Controller这边那返回就so easy了直接返回因为我们这边指对象通过我们的勾导方法已经勾造了那这样一来我们直接return好了这边呢就可以new一个我们叫做profile result通过我们的user对象进行勾造好了这样一来我这个代码其实就已经都写好了
[10:18] OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的 HRM 系统中用户登录和获取用户权限信息的后端代码实现过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示登录接口返回的 JSON 数据结构，包含 code、message、data 字段，data 中包含 mobile、username、company、menus、points、apis 等信息。
画面2：展示 API 文档中登录接口的响应示例，结构与画面1一致。
画面3：展示 UserContoller.java 中的 login 方法，接收 mobile 和 password，调用 userService.findUserByMobile 查询用户，验证密码，成功则生成 JWT token 并返回。
画面4：展示 UserContoller.java 中的 profile 方法，接收 userId，调用 userService.findById 查询用户，返回 ProfileResult 对象。
画面5：展示 ProfileResult.java 类的定义，包含 mobile、username、company、roles 字段。
画面6：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面7：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面8：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面9：展示多个开发工具窗口的切换，包括 IDEA、Postman、SQLyog、PowerDesigner 等。
画面10：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面11：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面12：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。
画面13：展示 ProfileResult.java 类中添加了 @Getter 和 @Setter 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
{
  "code": 0,
  "message": "string",
  "data": {
    "mobile": "string",
    "username": "string",
    "company": "string",
    "menus": [
      "string"
    ],
    "points": [
      "string"
    ],
    "apis": [
      "string"
    ]
  }
}

画面3：
@RequestMapping(value = "/login", method = RequestMethod.POST)
public Result login(@RequestBody Map<String, String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    User user = userService.findUserByMobile(mobile);
    if (user == null || !user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    } else {
        Map<String, Object> map = new HashMap<>();
        map.put("companyName", user.getCompanyName());
        map.put("username", user.getUsername());
        String token = jwtUtils.createJwt(user.getId(), user.getUsername(), map);
        return new Result(ResultCode.SUCCESS, token);
    }
}

画面4：
@RequestMapping(value = "/profile", method = RequestMethod.POST)
public Result profile() {
    String userId = "1";
    User user = userService.findById(userId);
}

画面5：
package com.ihrm.domain.system;

public class ProfileResult {
    private String mobile;
    private String username;
    private String company;
    private Map<String, Object> roles;
}

画面6：
package com.ihrm.domain.system;

import lombok.Getter;
import lombok.Setter;
import java.util.Map;

@Getter
@Setter
public class ProfileResult {
    private String mobile;
    private String username;
    private String company;
    private Map<String, Object> roles;
}

画面10：
public ProfileResult(User user) {
    this.mobile = user.getMobile();
    this.username = user.getUsername();
    this.company = user.getCompanyName();
    Set<Role> roles = user.getRoles();
    Set<String> menus = new HashSet<>();
    Set<String> points = new HashSet<>();
    Set<String> apis = new HashSet<>();
    for (Role role : roles) {
        Set<Permission> perms = role.getPermissions();
        for (Permission perm : perms) {
            String code = perm.getCode();
            if (perm.getPerType() == 1) {
                menus.add(code);
            } else if (perm.getPerType() == 2) {
                points.add(code);
            } else {
                apis.add(code);
            }
        }
    }
    this.roles.put("menus", menus);
    this.roles.put("points", points);
    this.roles.put("apis", apis);
}

画面13：
public ProfileResult(User user) {
    this.mobile = user.getMobile();
    this.username = user.getUsername();
    this.company = user.getCompanyName();
    Set<Role> roles = user.getRoles();
    Set<String> menus = new HashSet<>();
    Set<String> points = new HashSet<>();
    Set<String> apis = new HashSet<>();
    for (Role role : roles) {
        Set<Permission> perms = role.getPermissions();
        for (Permission perm : perms) {
            String code = perm.getCode();
            if (perm.getPerType() == 1) {
                menus.add(code);
            } else if (perm.getPerType() == 2) {
                points.add(code);
            } else {
                apis.add(code);
            }
        }
    }
    this.roles.put("menus", menus);
    this.roles.put("points", points);
    this.roles.put("apis", apis);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

