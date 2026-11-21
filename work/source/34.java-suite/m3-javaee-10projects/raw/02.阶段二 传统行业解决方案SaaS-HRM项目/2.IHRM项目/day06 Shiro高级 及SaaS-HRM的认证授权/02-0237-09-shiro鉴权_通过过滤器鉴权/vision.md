# 画面线理解：09-shiro鉴权：通过过滤器鉴权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\09-shiro鉴权：通过过滤器鉴权_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:39, 00:46, 00:56, 01:30, 02:18, 02:23, 02:27, 02:56, 04:19, 04:29, 04:42, 04:59, 05:02, 05:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:32:34

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
