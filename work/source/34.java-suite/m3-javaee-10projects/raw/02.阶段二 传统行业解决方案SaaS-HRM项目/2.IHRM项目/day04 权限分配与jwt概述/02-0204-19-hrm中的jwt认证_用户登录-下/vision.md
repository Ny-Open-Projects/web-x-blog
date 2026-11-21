# 画面线理解：19-hrm中的jwt认证：用户登录-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\19-hrm中的jwt认证：用户登录-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:25, 00:37, 00:55, 01:09, 01:50, 02:07, 02:22, 02:37, 03:02, 03:33, 03:51, 04:58, 05:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:01:22

1) 这一组画面整体在讲什么（一句话）：
在 Spring Boot 项目中，演示如何在 UserController 中实现用户登录功能，包括使用 JWT 生成令牌、将用户信息封装到令牌中，并展示相关配置和数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 UserController.java 中，展示登录方法的逻辑，使用 JwtUtils.createJwt() 生成 JWT 令牌。
画面 2: 在 UserController.java 中，将 JwtUtils.createJwt(user.getId(), user.getUsername()) 作为登录成功后的返回值。
画面 3: 在 UserController.java 中，登录成功后，将用户信息（如 companyId、companyName）放入 Map 中，再调用 JwtUtils.createJwt() 生成令牌。
画面 4: 在 UserController.java 中，使用 User 类的 getCompanyId() 方法获取公司 ID。
画面 5: 在 UserController.java 中，使用 User 类的 getCompanyName() 方法获取公司名称。
画面 6: 展示了 SAAS-HRM 系统的 API 文档，登录接口 /login 的参数和响应。
画面 7: 在 UserController.java 中，将生成的令牌 token 作为返回值。
画面 8: 在 UserController.java 中，将登录方法的参数从 String 类型改为 @RequestBody Map<String, String> loginMap。
画面 9: 在 UserController.java 中，使用 @RequestBody Map<String, String> loginMap 作为登录方法的参数，并调用 loginMap.get("mobile") 获取手机号。
画面 10: 在 UserController.java 中，将登录方法的参数改为 @RequestBody Map<String, String> loginMap，并使用 loginMap.get("mobile") 和 loginMap.get("password") 获取手机号和密码。
画面 11: 在 application.yml 中，展示数据库配置信息，包括 driver-class-name、url、username、password 等。
画面 12: 在 application.yml 中，展示 JWT 配置信息，包括 jwt: config:。
画面 13: 在 SQLyog 中，展示用户表（user）的数据，包括 mobile、username、password 等字段。
画面 14: 展示了 SAAS-HRM 系统的 API 文档，登录接口 /login 的响应示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public Result login(String mobile,String password) {
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        jwtUtils.createJwt(user.getId(),user.getUsername());
    }
}
```

画面 2:
```java
else {
    //登录成功
    jwtUtils.createJwt(user.getId(),user.getUsername());
}
```

画面 3:
```java
else {
    //登录成功
    Map<String,Object> map = new HashMap<>();
    map.put("companyId",user.getCompanyId());
    map.put("companyName",user.getCompanyName());
    jwtUtils.createJwt(user.getId(),user.getUsername());
}
```

画面 4:
```java
map.put("companyId",user.getCompanyId());
```

画面 5:
```java
map.put("companyName",user.getCompanyName());
```

画面 7:
```java
String token = jwtUtils.createJwt(user.getId(), user.getUsername());
return new Result(ResultCode.SUCCESS,token);
```

画面 8:
```java
public Result login(@RequestBody Map<String,String> loginMap) {
```

画面 9:
```java
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
```

画面 10:
```java
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        Map<String,Object> map = new HashMap<>();
        map.put("companyId",user.getCompanyId());
        map.put("companyName",user.getCompanyName());
        String token = jwtUtils.createJwt(user.getId(), user.getUsername(), map);
        return new Result(ResultCode.SUCCESS,token);
    }
}
```

画面 11:
```yaml
#数据库配置
spring:
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/hrm?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
```

画面 12:
```yaml
jwt:
  config:
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
