# 画面线理解：18-hrm中的jwt认证：需求分析与用户登录-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\18-hrm中的jwt认证：需求分析与用户登录-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:54, 03:20, 05:14, 05:47, 06:12, 07:24, 08:10, 08:46, 09:10, 09:50, 10:49, 11:37, 12:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:00:51

1) 这一组画面整体在讲什么（一句话）：
讲解在 Spring Boot 项目中实现 JWT（JSON Web Token）用户登录与权限控制的流程，包括工具类创建、登录流程、用户信息获取及权限校验等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDEA中“5.3 JWT工具类”页面，代码为在`hrm_common`工程中创建`JwtUtil`类，代码如下：
```java
@ConfigurationProperties("jwt.config")
public class JwtUtil {
    private String key;
    private long ttl;
    public String getKey() {
        return key;
    }
    public void setKey(String key) {
        this.key = key;
    }
    public long getTtl() {
        return ttl;
    }
    public void setTtl(long ttl) {
        this.ttl = ttl;
    }
}
```

画面2：展示登录流程图，左侧为“用户名”、“密码”、“登录”输入框，右侧为“登录”步骤：1.根据用户名查询用户；2.比较密码；3.生成token；4.响应数据。

画面3：在登录流程图基础上，增加“获取用户信息”模块，标注请求头为“token数据”，并指向右侧“获取用户信息”模块，该模块内容为：获取用户信息，请求头：token数据。

画面4：在登录流程图基础上，完善“获取用户信息”模块，内容为：1.获取头信息中的token；2.从token中提取userid；3.查询用户；4.构造数据。

画面5：展示IDEA中`UserController.java`文件，代码为：
```java
@RequestMapping(value = "/user/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable("id") String id, @RequestBody User user) {
    user.setId(id);
    userService.update(user);
    return new Result(ResultCode.SUCCESS);
}

// 删除注释
@RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable("id") String id) {
    userService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

画面6：在`UserController.java`中，对`update`方法进行注释，代码为：
```java
// 根据id删除
@RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable("id") String id) {
    userService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

画面7：在`UserController.java`中，对`delete`方法进行注释，代码为：
```java
// 删除注释
@RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable("id") String id) {
    userService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

画面8：展示IDEA中`UserDao.java`文件，代码为：
```java
package com.ihrm.system.dao;
import ...
public interface UserDao extends JpaRepository<User,String>,JpaSpecificationExecutor<User> {
    Page<User> findAll(Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User
