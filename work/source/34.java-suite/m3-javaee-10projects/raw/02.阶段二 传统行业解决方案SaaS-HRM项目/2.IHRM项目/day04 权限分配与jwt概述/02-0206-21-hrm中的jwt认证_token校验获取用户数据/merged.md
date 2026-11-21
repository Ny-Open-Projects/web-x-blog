# 21-hrm中的jwt认证：token校验获取用户数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\21-hrm中的jwt认证：token校验获取用户数据_【海量资源尽在 ubkz.com】.mp4
- 时长 12分20秒（音频 741s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 我们这个代码都写好了之后呢其实写的代码比较快我们可以做一个简单的说明在这边ID我们一会儿再去获取那根据ID获取用户那获取用户了之后这边的这个写法呢应该各位都能看懂吧这个其实就是调用构造方法的形式去得到一个我们的返回对象OK把返回对象以构造方法的形式创建一个result那这边呢有我们的构造方法
[00:32] OK好那这样一来我们代码就看得清晰一点当然了对于我这个new profile result这个方法里面呢各位来看其中呢就是想方设法的跟我们的响应进行挂钩那这边呢有mobilecompany等等都复制了这边还有个肉丝那肉丝里面点扑的哎各位这个肉丝这有点问题不知道各位有没有发现啊我应该对它进行一个初始化卡西麦跑
[00:58] OK那这样一来就没啥问题了那我们代码都写好了之后我们可以重新启动一下当前的工程好了这个工程呢再重启我打开Postman我们开始做一个验证的过程好了这边呢我已经把这个链接呢准备好了拷过来之后呢咱们可以一起来做一个测试看一下效果走send方法好了这边数据已经给我查询出来了我们一起来看一下Data有Mobile有Username
[01:31] 好了有company等等只不过现在这个SaaS管理员他什么权限都没有而已OK那这样一来我们这个profile方法已经都写好那已经都写好了之后接下来关注的就是最后一项操作那最后一项操作是什么呢我们总不能你每回发profile我都查询用户为一的吧那这个就太不合理了我们是不是应该你登录是哪个用户我这边应该给你查询哪个用户啊那这句话就又回到了我们这张图形
[02:01] 那你首先进行登录我已经把token返回给你了已经返回给你了那你这回再去请求的时候请求profile是不是应该在投信息当中把token数据给我携带上啊那在我讲义当中呢跟各位说了一个我们之间的一个声明或者我们之间的一个小小的约定我们之间的约定是这样的你请求我的时候你在你请求投当中加一个投信息Authoration
[02:29] 那你这个Name的名称是什么呢就是Bee加空格加Token所以呢你这个请求投信息当中必然会包含这么一个内容Bee当然了这个Bee是我们约定俗成的一种做法你想叫他就叫他不叫他无所谓好了加一空格Token那别忘了这个Token当中我们刚才设置了很多的内容设置了他的ID你登录登录ID登录用户ID还有你当前登录的Subject不就是用户名
[03:05] 当然了我们在这token里面还包含了我们叫做company当然了还包含了company name那我们现在你发送过我的这个token是不是token里面必然包含这些内容啊那必然包含这些内容的话我们只需要是不是解析你这个token从token当中获取你的ID这样一来我们整个的用户ID就已经获取到了所以接下来我们要完成的点
[03:32] 就围绕在如何获取token以及如何从token当中解析得到用户内容那我们如何去做呢其实很简单我们关注的还是我们刚才的profile方法在上方我们要补充其他的内容好了在这边我们开始从请求投信息中获取我们的token数据
[04:03] 那怎么从请求灯当中获取token数据呢首先第一个获取请求投信息而这个请求投信息它的名称等于我们刚才看过叫做Authorsation啊啊错了Authorsation就是它Ctrl C拿过来好了接着第二件事第二件事我们这个Authorsation呢它的我们之间做的一个约定呢刚才咱们也看过它是以比尔空格的形式来构造的
[04:35] bier空格的形式来构造的所以呢我们获取了之后替换我们这个bier加空格那接下来呢我们就可以解析我们的token那解析好了之后获取我们叫做clamps好了那接着我们一个一个来完成它首先获取请求投信息那请求投信息如何获取注意我们可以在profile这边得到我们的http requestserver
[05:10] lat serv requestrequest那有了request之后呢我们可以在这边request打点getheader我们的header明星associationok那这样一来呢我们就能得到了当前这个头的所有内容那么可以做一个简单的判断if如果当前的这个头它是空我们是不是就不能访问的啊点is empty如果它是空
[05:43] 这个Spring提供那个方法判断为空的之前我们也看过那如果是空的话我们可以抛出一个异常new一个我们叫做common errorcommon exception那这个common exception呢我们可以传递也是我们这个result code那这个就是您还未登录让他去登录吧点注意注意我这边抛出了一个异常那抛出异常我们之前是不是就玩过一个叫做
[06:11] 异常的全局处理那异常全局处理是不是就会捕获到我这个异常接着呢把我们这个异常转化为能够实行的持别的json并反应反回做响应ok好了那这边呢我们已经获取到了token内容token的信息但是现在还是以bier开头的所以我们接下来提取到tokenstringtoken就等于我们得到的这个投信息的内容打点replace
[06:40] 那么replace就是可以做一个简单粗暴的事情就是别人空格让它转化成空就可以了哎这样一来替换了那替换了之后接下来我们开始进行解析那解析token呢比较简单还是我们的jwt utils打点pams jwt把token传过来ok那这样一来我们得到了我们自己想的内容那得到了内容之后user id我们就可以通过pams打点
[07:13] get id进行获取那这样一来id就已经获取到了好了当然了这些步骤呢咱们也可以简单的梳理一下第一个第二个ok第三个解析那最后获取clams之后得到id那这样一来我整个的咱们这个用户获取的过程就已经结束了我们这边呢可以重新启动一下当前我们这个工程好了这边呢先不管它了
[07:49] 那我在这边呢去构造我们两个请求第一个呢是我们的用户登录login好了login呢可能会发送一些数据算了这边是login吧数据已经有了login好了这边呢就是我们的profile当然了我们profile呢简单的来看post提交post提交好了我们的登录呢也是一个post提交没问题我们可以从数据库里面找一条数据啊就13800138003
[08:28] 就是他注意这个人叫张三好了请求的密码1234561OK那接着注意走策划成功代表登录成功那登录成功注意这边有tokencopy那注意现在呢我们模拟前端访问profile模拟前端访问的时候我们就需要自己给他搞一个header出来那这个header他叫什么名字我们一会再说好了B E A R EBell空格
[09:02] 这是我们的值是叫BAR抱歉这个写错了好了替换因为我们的约定是BAR加空格加上我们的token好了接着它的名字呢叫做Authentication也call过来那这样一来我就模拟了一个头那这个头信息包含我们所有内容并且这人是张三的那这回我再去获取信息走好了这边报了一个错我们简单的来看一下它抛出的是一个Hamlet的一长简单的看一下
[09:41] 其实我们这边可以推断出来是这样的就是说呢在这边ID没有获取到那这个user ID没有获取到的原因是什么呢我简单的看了一下是这样的就是说呢我们往里存的时候注意我们往里存的时候common ID那我这边呢刚才写这工具列的时候直接放了一个setClamS那这ClamS其实已经覆盖了我们刚才写的ID和这个name所以呢解决这个问题的方法呢很简单
[10:15] 解决这个问题的方法呢很简单首先呢就是在这边我们可以不用这个client set clamps了我们这边的循环一个一个的往里面设置其实也可以那我这边把这个工具类呢做一个简单的修改for循环就是回到我们刚才写的那种方式map stringobject好了mapentryentry好了接下来就是map.entrysetmap.entry
[11:00] ok那接下来呢我们就可以通过jwt builder一个一个的往里面setclam点clam好了一个一个的往里设置其实就可以了这边呢就可以entry.getkeykeyvalue的形式entry.getvalue一个一个设置进去ok那这样一来呢我们这个方法呢
[11:23] 就做了一个简单的改造那改造了之后我们再去重启一下当前我们的服务好了接着再去完成我们这个登录和我们这个用户信息的一个获取看一下情况这边的登录不管他了我重新登录一把走send给我来看重新登录的数据token也获取到了那接下来在这边这回呢我是重新的一个新的token所以呢把这个value部分呢做一个简单的替换bill空格没问题
[11:57] 重新拿到的我们的token信息那好了继续走send各位来看一下效果那这样一来其实已经查询出来了并且张三一没问题传至博客OK他有这些权限OK那这样一来我们已经完成了基于JWT的我们token的签发已经token的信息交验OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package com.ihm.system.Controller;
import com.ihm.common.entity.Result;
import com.ihm.common.exception.CommonException;
import com.ihm.common.utils.JwtUtils;
import com.ihm.system.Service.UserService;
import io.Swagger.annotations.Api;
import io.Swagger.annotations.ApiOperation;
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

