# 画面线理解：21-hrm中的jwt认证：token校验获取用户数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\21-hrm中的jwt认证：token校验获取用户数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:57, 01:54, 02:19, 03:23, 04:34, 05:38, 06:37, 07:52, 08:33, 09:36, 10:35, 11:17, 12:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:02:45

1) 这一组画面整体在讲什么（一句话）：
实现用户登录功能，包括登录校验、JWT令牌生成与返回、以及用户信息查询接口的开发。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示UserController.java中登录成功后生成JWT令牌的代码逻辑，包含map构建和token生成。
画面2：展示ProfileResult类的构造方法，用于封装用户角色、菜单和权限信息。
画面3：展示UserController.java中登录成功后的profile方法，用于获取用户信息。
画面4：展示PPT内容，讲解JWT解析方法及修改application.yml配置文件添加JWT配置。
画面5：展示登录流程图，包括登录时的用户名密码校验、生成token、返回token，以及获取用户信息时的token验证和数据构造。
画面6：展示ProfileResult类的构造方法，用于封装用户角色、菜单和权限信息。
画面7：展示UserController.java中profile方法的代码，包含从请求头获取token并解析的逻辑。
画面8：展示UserController.java中profile方法的代码，包含从请求头获取token并解析的逻辑。
画面9：展示Postman中发送登录请求，请求体包含mobile和password参数。
画面10：展示Postman中发送登录请求，请求体包含mobile和password参数。
画面11：展示UserController.java中登录成功后生成JWT令牌的代码逻辑，包含map构建和token生成。
画面12：展示JwtUtils.java中createJwt方法的代码，用于生成JWT令牌。
画面13：展示JwtUtils.java中createJwt方法的代码，用于生成JWT令牌。
画面14：展示PPT内容，讲解登录成功后返回token的实现方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
Map<String, Object> map = new HashMap<>();
map.put("companyId", user.getCompanyId());
map.put("companyName", user.getCompanyName());
String token = JwtUtils.createJwt(user.getId(), user.getUsername(), map);
return new Result(ResultCode.SUCCESS, token);
```

画面2：
```java
import java.util.Set;
@Getter
@Setter
public class ProfileResult {
    private String mobile;
    private String username;
    private String company;
    private Map<String, Object> roles = new HashMap<>();
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
                if (perm.getType() == 1) {
                    menus.add(code);
                } else if (perm.getType() == 2) {
                    points.add(code);
                } else {
                    apis.add(code);
                }
            }
        }
    }
}
```

画面3：
```java
if (user == null || !user.getPassword().equals(password)) {
    return new Result(ResultCode.MOBILEPASSWORDERROR);
} else {
    Map<String, Object> map = new HashMap<>();
    map.put("companyId", user.getCompanyId());
    map.put("companyName", user.getCompanyName());
    String token = JwtUtils.createJwt(user.getId(), user.getUsername(), map);
    return new Result(ResultCode.SUCCESS, token);
}
```

画面4：
```java
public Claims parseJWT(String token) {
    Claims claims = null;
    try {
        claims = Jwts.parser()
                .setSigningKey(key)
                .parseClaimsJws(token).getBody();
    } catch (Exception e) {
    }
    return claims;
}
```

画面4：
```yaml
jwt:
  config:
    key: saas-ihm
    ttl: 360000
```

画面5：
无代码或配置。

画面6：
```java
@Getter
@Setter
@NoArgsConstructor
public class ProfileResult {
    private String mobile;
    private String username;
    private String company;
    private Map roles;
    public ProfileResult(User user) {
        this.mobile = user.getMobile();
        this.username = user.getUsername();
        this.company = user.getCompanyName();
        //角色权限
        Set<String> menus = new HashSet<>();
        Set<String> points = new HashSet<>();
        Set<String> apis = new HashSet<>();
        for (Role role : user.getRoles()) {
            for (Permission perm : role.getPermissions()) {
                String code = perm.getCode();
                if (perm.getType() == 1) {
                    menus.add(code);
                } else if (perm.getType() == 2) {
                    points.add(code);
                } else {
                    apis.add(code);
                }
            }
        }
    }
}
```

画面7：
```java
import org.springframework.util.StringUtils;
if (StringUtils.isEmpty(authorization)) {
    throw new CommonException("token不能为空");
}
String token = authorization;
```

画面8：
```java
import org.springframework.util.StringUtils;
if (StringUtils.isEmpty(authorization)) {
    throw new CommonException("token不能为空");
}
String token = authorization;
```

画面9：
无代码或配置。

画面10：
无代码或配置。

画面11：
```java
else {
    Map<String, Object> map = new HashMap<>();
    map.put("companyId", user.getCompanyId());
    map.put("companyName", user.getCompanyName());
    String token = JwtUtils.createJwt(user.getId(), user.getUsername(), map);
    return new Result(ResultCode.SUCCESS, token);
}
```

画面12：
```java
public String createJwt(String id, String name, Map<String, Object> map) {
    //1.设置有效时间
    long now = System.currentTimeMillis();
    long exp = now + ttl;
    //2.构建JWT
    JwtBuilder jwtBuilder = Jwts.builder()
            .setId(id)
            .setSubject(name)
            .setIssuedAt(new Date())
            .signWith(SignatureAlgorithm.HS256, key);
    //3.根据map设置claims
    for (Map.Entry<String, Object> entry : map.entrySet()) {
        jwtBuilder.claim(entry.getKey(), entry.getValue());
    }
    return jwtBuilder.compact();
}
```

画面13：
```java
public String createJwt(String id, String name, Map<String, Object> map) {
    //1.设置有效时间
    long now = System.currentTimeMillis();
    long exp = now + ttl;
    //2.构建JWT
    JwtBuilder jwtBuilder = Jwts.builder()
            .setId(id)
            .setSubject(name)
            .setIssuedAt(new Date())
            .signWith(SignatureAlgorithm.HS256, key);
    //3.根据map设置claims
    for (Map.Entry<String, Object> entry : map.entrySet()) {
        jwtBuilder.claim(entry.getKey(), entry.getValue());
    }
    return jwtBuilder.compact();
}
```

画面14：
```java
@Bean
public JwtUtil jwtUtil() {
    return new util.JwtUtil();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：
标题：5.4 登录成功签发token
内容：
(1) 配置JwtUtil，修改hrm_system工程的启动类
```java
@Bean
public JwtUtil jwtUtil() {
    return new util.JwtUtil();
}
```
(2) 添加登录方法
```java
package com.ihm.system.controller;
import com.ihm.common.entity.Result;
import com.ihm.common.exception.CommonException;
import com.ihm.common.utils.JwtUtils;
import com.ihm.system.service.UserService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
```

画面5：
标题：登录流程图
内容：
登录：
1. 根据用户名查询用户
2. 比较密码
3. 生成token
4. 返回
获取用户信息：
1. 查询用户（id: 1）
2. 构造返回数据

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
