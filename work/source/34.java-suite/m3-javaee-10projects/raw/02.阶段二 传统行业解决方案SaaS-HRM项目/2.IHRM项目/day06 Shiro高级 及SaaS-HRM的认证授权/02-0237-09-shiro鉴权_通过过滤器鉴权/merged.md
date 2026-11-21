# 09-shiro鉴权：通过过滤器鉴权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\09-shiro鉴权：通过过滤器鉴权_【海量资源尽在 ubkz.com】.mp4
- 时长 5分53秒（音频 354s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们看过了这个登录的这些认证相关逻辑的一个测试代码那这些我们看过了之后接下来咱们来看一下就是说如何判断你请求某一个URL是否具有相应的权限那其实在Shera当中对某一个请求的URL进行权限的一个判断呢其实有两种方式第一种呢就是可以借助我们的过滤器
[00:26] 第二种呢其实可以借助我们的注解那我们先来看举一个简单的例子比如说我要访问user.home这个接口或者这个我们请求地址我这边写的是anno那如果说我要想让它具备某种权限才能访问那怎么做呢这边我们就可以借助过滤器的形式来做那具备某种权限用的是permissuser那这个过滤器那我们可以进行一个配置
[00:53] 把上面这句话Ctrl C拿过来Ctrl V好了这边具有某种某种权限才能访问好了那这边呢我们要PERMS比如说呢这个具有的权限叫什么呢注意user-home那在我数据库当中呢刚才已经补充了这么一个user-home的这么一个权限注意codeuser-home那如果说你当前登录这个人
[01:32] 具备user.home这么一个权限我才能让你访问那接下来就是说如果不具备指定的权限那它呢会跳转到我们指定的set这个unauthorized的ul地址也就是会跳转到这个also arrowcode等于2那返回一个未授权的这么一句话那好了接下来我们来看一下这个呢其实就是使用
[02:07] 过滤器的形式配置我们请求地址的权限依赖权限好了那这个我们配置好了之后呢我们可以一起重新启动一下当前的这个工程再来做一测试好了同样打开postman那在这边注意user-homeuser-home我已经写好了来走send好了一发送它告诉我未登录
[02:36] 因为我就是没登录因为我这边配置它有个从上到下加载的一个过程那首先呢检测到它没有登录那没有登录我就可以先去完成一个登录操作好了为了方便我这边再来一个login那这边呢跟各位来看一下就是我这边的数据库里面的用户有很多条数据库里面的用户有很多条一号用户叫张三二号用户和三号用户李四那看一下角色角色有系统管理员和普通管理员
[03:06] 那用户和角色只有1号用户分配了一个角色那2号3号用户什么角色都没有2号3号都没角色它就没有相应的权限那所以在这边要跟各位来声明的就是说只有1号用户有角色那2 3号都没角色相应的2 3号用户也没有权限任何权限都没有那1号用户的权限有很多所有权限都有在这张表里面都有体现1号角色里面有12345
[03:34] 就是驱动管理员有所有的权限那一句话该哭一号用户有所有权限二三什么都没有好了那接着呢我们来看一下我是李四什么权限都没有我登录登录这个不影响但是我再去访问UterGunHome的时候你走是不是就代表是为授权啊那如果我这边登录换成张三走登录成功那这边我们再来看
[04:04] 好了放完个文储备成功因为张三是不是才有权限那我想跟各位说的是为什么这边切换选项卡也没问题是因为这个其实就是跟浏览器差不多它共享cookie共享cookie里面的叫做session id好了那这个是跟各位来聊的第一种我们判断它具备权限的一种方式那除了这种方式之外那如果说呢你这个判断需要某种权需要某种角色才能访问那怎么做依赖的叫做角色
[04:35] 那这个怎么做呢其实也比较简单同样的Ctrl C拿过来Ctrl V同样的找它的过滤器Rose那这个Rose比如说我们的角色角色名称我存的全部都全名只有系统管理员才能访问那我这边就是系统管理员添加上其实就可以了好了那这个呢我们也可以重新启动一下做一个简单的演示上面Pulse代表的是
[05:07] 必须具备这个权限底下这个ros必须具备这个角色那我们之前都知道用户一号用户张三就这角色那好了我们再去做一个测试同样的是张三我先登录一下好了这边登录成功分配了新的session id而这边再去user home没问题那好了这边呢我去换成李四登录我们每次登录session id都是重新分配吧好了session id
[05:40] OK那走各位来看这回同样也是位数权这个就是跟各位来看了一下通过过滤器的形式指定你是否具备某种权限指定你是否具备某种角色的方式

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置 Shiro 权限过滤器，通过代码设置 URL 访问权限规则，并结合数据库角色权限进行验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "anon"，表示无需认证即可访问。
- 代码片段：`filterMap.put("/user/home", "anon");`
- 代码片段：`filterFactory.setFilterChainDefinitionMap(filterMap);`

画面 2:
- 展示 Shiro 权限过滤器的说明文档，列出各种过滤器（如 anon, authc, user, perms, roles, rest 等）及其作用。
- 文档中说明了 perms(user) 和 roles(admin) 等过滤器的用法。

画面 3:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "anon"。
- 代码片段：`filterMap.put("/user/home", "anon");`

画面 4:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "perms[user-home]"，表示需要具有 "user-home" 权限才能访问。
- 代码片段：`filterMap.put("/user/home", "perms[user-home]");`

画面 5:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "perms[user-home]"。
- 代码片段：`filterMap.put("/user/home", "perms[user-home]");`

画面 6:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "perms[user-home]"。
- 代码片段：`filterMap.put("/user/home", "perms[user-home]");`

画面 7:
- Postman 发送 POST 请求到 http://localhost:8081/user/home，返回 500 Internal Server Error，错误信息为 "Project does not have permission [user-home]"。
- 请求体内容：`{"username":"admin","password":"123456"}`

画面 8:
- 数据库管理工具显示 shiro_db 数据库中的权限表（如 permissions）和用户表（如 user）。
- 表中显示了用户和权限的映射关系。

画面 9:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "roles[系统管理员]"，表示需要具有 "系统管理员" 角色才能访问。
- 代码片段：`filterMap.put("/user/home", "roles[系统管理员]");`

画面 10:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "roles[系统管理员]"。
- 代码片段：`filterMap.put("/user/home", "roles[系统管理员]");`

画面 11:
- 展示 Shiro 权限过滤器的说明文档，列出各种过滤器（如 anon, authc, user, perms, roles, rest 等）及其作用。
- 文档中说明了 perms(user) 和 roles(admin) 等过滤器的用法。

画面 12:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "roles[系统管理员]"。
- 代码片段：`filterMap.put("/user/home", "roles[系统管理员]");`

画面 13:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "roles[系统管理员]"。
- 代码片段：`filterMap.put("/user/home", "roles[系统管理员]");`

画面 14:
- 编辑器显示 ShiroConfiguration.java 文件内容，正在配置 filterMap，将 "/user/home" 映射为 "roles[系统管理员]"。
- 代码片段：`filterMap.put("/user/home", "roles[系统管理员]");`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
//2.设置安全管理器
filterFactory.setSecurityManager(securityManager);
//3.通用配置（跳转登录页面，为授权跳转的页面）
filterFactory.setLoginUrl("/autherror?code=1");//跳转url地址
filterFactory.setUnauthorizedUrl("/autherror?code=2");//未授权的url
//4.设置过滤器集合
//
//设置所有的过滤器，有Map
// key = 扫描的url地址
// value = 过滤器类型
Map<String,String> filterMap = new LinkedHashMap<>();
//filterMap.put("/user/home","anon");//当前请求地址可以匿名访问
filterMap.put("/user/**","authc");//当前请求地址必须认证之后才可以访问
filterFactory.setFilterChainDefinitionMap(filterMap);
return filterFactory;
```

画面 4:
```java
Map<String,String> filterMap = new LinkedHashMap<>();
//filterMap.put("/user/home","anon");//当前请求地址可以匿名访问
filterMap.put("/user/home","perms[user-home]");//不具指定的权限，跳转到setUnauthorizedUrl地址
filterMap.put("/user/**","authc");//当前请求地址必须认证之后才可以访问
filterFactory.setFilterChainDefinitionMap(filterMap);
return filterFactory;
```

画面 9:
```java
Map<String,String> filterMap = new LinkedHashMap<>();
//filterMap.put("/user/home","anon");//当前请求地址可以匿名访问
filterMap.put("/user/home","roles[系统管理员]");//不具指定的权限，跳转到setUnauthorizedUrl地址
filterMap.put("/user/**","authc");//当前请求地址必须认证之后才可以访问
filterFactory.setFilterChainDefinitionMap(filterMap);
return filterFactory;
```

画面 12:
```java
Map<String,String> filterMap = new LinkedHashMap<>();
//filterMap.put("/user/home","anon");//当前请求地址可以匿名访问
filterMap.put("/user/home","roles[系统管理员]");//不具指定的权限，跳转到setUnauthorizedUrl地址
filterMap.put("/user/**","authc");//当前请求地址必须认证之后才可以访问
filterFactory.setFilterChainDefinitionMap(filterMap);
return filterFactory;
```

画面 13:
```java
Map<String,String> filterMap = new LinkedHashMap<>();
//filterMap.put("/user/home","anon");//当前请求地址可以匿名访问
filterMap.put("/user/home","roles[系统管理员]");//不具指定的权限，跳转到setUnauthorizedUrl地址
filterMap.put("/user/**","authc");//当前请求地址必须认证之后才可以访问
filterFactory.setFilterChainDefinitionMap(filterMap);
return filterFactory;
```

画面 14:
```java
Map<String,String> filterMap = new LinkedHashMap<>();
//filterMap.put("/user/home","anon");//当前请求地址可以匿名访问
filterMap.put("/user/home","roles[系统管理员]");//不具指定的权限，跳转到setUnauthorizedUrl地址
filterMap.put("/user/**","authc");//当前请求地址必须认证之后才可以访问
filterFactory.setFilterChainDefinitionMap(filterMap);
return filterFactory;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
- PPT 标题：Shiro 权限过滤器说明
- 表格数据：
  - anon: 无参，开放权限，可以理解为匿名用户或游客
  - authc: 无参，需要认证
  - logout: 无参，注销，执行后会直接跳转到 shiroFilterFactoryBean.setLoginUrl() 设置的 url
  - authcBasic: 无参，表示 httpBasic 认证
  - user: 无参，表示必须存在用户，当登录输入时不做检查
  - ssl: 无参，表示 SSL 协议，协议为 https
  - perms(user): 参数可写多个，表示需要某个或某些权限才能通过，多个参数时写 perms[user, admin]，当有多个参数时必须都通过才算通过，多个参数时写 roles[admin, user]，当有多个参数时必须都通过才算通过
  - roles(admin): 参数可写多个，表示是某个或某些角色才能通过，多个参数时写 roles[admin, user]，当有多个参数时必须都通过才算通过
  - rest(user): 根据请求的方法，相当于 perms[user-method]，其中 method 为 post, get, delete 等
  - port[8081]: 当请求的 URL 端口不是 8081 时，跳转到当前访问主机 HOST 的 8081 端口

画面 11:
- PPT 标题：Shiro 权限过滤器说明
- 表格数据：
  - anon: 无参，开放权限，可以理解为匿名用户或游客

