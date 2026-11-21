# 15-jwt：token的解析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\15-jwt：token的解析_【海量资源尽在 ubkz.com】.mp4
- 时长 5分7秒（音频 307s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们创建好了token之后呢其实接下来要做的事呢其实就是要把这个token给它解析出来那这个就好比我们之后要完成的操作用户登录到我们的系统我们验证了它的用户名密码之后可以给它生成这么一个token加密字幕串那把这个加密字幕串签发给了我们的客户端客户端接下来再去完成其他操作的时候是不是就携带着这个token串去访问我们的接口
[00:28] 那我们服务端呢就要想方设法的对这个token创进行一个解析那在这边呢我们搞一个解析token字幕创的一个测试类好了bill就叫做parenceparence我们叫做jwt testok还是以闷方法的形式来一个简单测试psvm那我们这边解析我们的jwttoken字幕创那我们这边怎么解析呢其实
[01:01] 也很简单我们可以一起来看一下我们的讲义在这边呢我们进行解析还是借助这个JWTS这个对象调用他的Pencils方法然后呢注意很希望各位要明白的一点我们要将当前加密这个字符串的这个私钥信息我们自己的一个私钥信息告他我要通过这个私钥信息对于我们的Token进行解析那接着拿到我们
[01:27] 这个token字幕创意里面咱们私有的数据get body那就可以一个一个的获取到了那接下来呢我们就可以一起来看一下那JWT1S工具类打点Paris那打点Paris呢接着需要指定我们这边的加密的这么一个我们的私钥究竟是什么我们一起来看一下好了set我们的私钥信息
[01:55] 好了那我们的CL呢刚才叫做IHRM好了那继续再进行打点我们就开始进行解析我们的字符串好了其实我们解析的字符串主要目的就是得到这个CLEMS这个CLEMS其实就是我们存储的我们CL的一些数据OK那这个字符串在哪呢我们可以使用tokentoken等于那接下来呢就把我们生成的这个字符串拿过来Ctrl C放到这边Ctrl V
[02:26] OK这边最大化那接下来呢把我们这个token chart呢传递过来好了接下来注意你现在这样一解析的话其实得到的是我们所有的内容那对于我们来说只要我们关注的或者我们私有的一些数据打点get body即可那这样一来我们就能得到一个climb对象那得到了climb对象我们所有的私有数据就是我们设置的这些数据全部存放在我们这个climb对象当中
[02:57] 所以接下来呢我们就可以通过Claim对象拿到我们所需要的一些内容比如说呢Claims打点Get ID好了比如说呢Claims打点我们叫做Get Subject比如说呢还可以Claims打点我们有设置了一个叫做时间是吧先发的时间那好了接下来呢我们可以把这几个内容全部给它打印出来一起来看一下效果SOT
[03:30] OK这个打印呢我就直接call了省得浪费时间OK那我们解析看一下效果注意我刚才存的ID应该是叫88subject小白然后呢里面还给了一个当前时间那我们一起来看一下走好了那各位来看就目前来说呢它已经把我们存储的这些数据全部都解析出来了那有的朋友就是说呢我刚才这个密钥自己签名的密钥写的是一个IHM如果我写了一个123随便写写错了那各位来看
[04:08] 我再去执行我这个怎么还能执行成功呢这个ABCD刚才应该是没保存啊这个这回其实就报错了比如说ABCD随后再来IHRM123随便写随便写我再试一下那这个其实就已经报错了
[04:48] 好了那这样一来呢我们这个效果其实就已经演示出来了如果说那个签名不错的报错的话或者签名签错的话那就解决不出来当然了如果说你这个token传失败了我这边随便加了一个1我再执行其实跟刚才的效果一样它必然也会出错吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Java 的 io.jsonwebtoken 库创建和解析 JWT（JSON Web Token）。

2) 按时间顺序列出每张画面的要点：
画面1：在 IntelliJ IDEA 中，右键点击项目目录，选择“Analyze”选项，准备对项目进行分析。
画面2：在 IntelliJ IDEA 中，运行了名为 “ParseJwtTest” 的 Java 类，终端显示“Process finished with exit code 0”，表示程序成功执行。
画面3：展示了一个 PPT 页面，标题为“第4章 权限管理与JWT鉴权”，内容包含“1. 权限管理”、“2. 分页插件”、“3. 分页插件”、“4. 定义的认证机制”、“5. HRM中的TOKEN实现与验证”。
画面4：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，其中包含对 JWT 的解析方法。
画面5：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，其中包含对 JWT 的解析方法。
画面6：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，其中包含对 JWT 的解析方法。
画面7：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，其中包含对 JWT 的解析方法。
画面8：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，其中包含对 JWT 的解析方法。
画面9：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，其中包含对 JWT 的解析方法。
画面10：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，其中包含对 JWT 的解析方法。
画面11：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，其中包含对 JWT 的解析方法。
画面12：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，其中包含对 JWT 的解析方法。
画面13：在 IntelliJ IDEA 中，展示了 “CreateJwtTest.java” 文件的代码，其中包含创建 JWT 的代码。
画面14：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，终端显示“Exception in Thread "main" io.jsonwebtoken.SignatureException: JWT signature does not match locally computed signature. JWT validity cannot be verified.”，表示 JWT 解析失败，签名不匹配。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
void main(String[] args) {
    JwtBuilder = Jwts.builder().setId("88").setSubject("小白")
    setIssuedAt(new Date())
    signWith(SignatureAlgorithm.HS256, "ihrm");
    token = jwtBuilder.compact();
    System.out.println(token);
}

画面2：
public class ParseJwtTest {
    public static void main(String[] args) {
        String token = "eyJhbc..."; // JWT token
        Claims claims = Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
        System.out.println(claims.getId());
        System.out.println(claims.getSubject());
        System.out.println(claims.getIssuedAt());
    }
}

画面3：
public class ParseJwtTest {
    public static void main(String[] args) {
        String token = "eyJhbc..."; // JWT token
        Claims claims = Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
        System.out.println(claims.getId());
        System.out.println(claims.getSubject());
        System.out.println(claims.getIssuedAt());
    }
}

画面4：
public class ParseJwtTest {
    public static void main(String[] args) {
        Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
    }
}

画面5：
public class ParseJwtTest {
    public static void main(String[] args) {
        Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
    }
}

画面6：
public class ParseJwtTest {
    public static void main(String[] args) {
        Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
    }
}

画面7：
public class ParseJwtTest {
    public static void main(String[] args) {
        Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
    }
}

画面8：
public class ParseJwtTest {
    public static void main(String[] args) {
        String token = "eyJhbc...";
        Claims claims = Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
    }
}

画面9：
public class ParseJwtTest {
    public static void main(String[] args) {
        String token = "eyJhbc...";
        Claims claims = Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
    }
}

画面10：
public class ParseJwtTest {
    public static void main(String[] args) {
        String token = "eyJhbc...";
        Claims claims = Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
    }
}

画面11：
public class ParseJwtTest {
    public static void main(String[] args) {
        String token = "eyJhbc...";
        Claims claims = Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
    }
}

画面12：
public class ParseJwtTest {
    public static void main(String[] args) {
        String token = "eyJhbc...";
        Claims claims = Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
    }
}

画面13：
public class CreateJwtTest {
    public static void main(String[] args) {
        JwtBuilder jwtBuilder = Jwts.builder().setId("88").setSubject("小白")
            .setIssuedAt(new Date())
            .signWith(SignatureAlgorithm.HS256, "ihrm");
        String token = jwtBuilder.compact();
        System.out.println(token);
    }
}

画面14：
public class ParseJwtTest {
    public static void main(String[] args) {
        String token = "eyJhbc...";
        Claims claims = Jwts.parser().setSigningKey("ihrm").parseClaimsJwt(token).getBody();
        System.out.println(claims.getId());
        System.out.println(claims.getSubject());
        System.out.println(claims.getIssuedAt());
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
标题：第4章 权限管理与JWT鉴权
内容：
1. 权限管理
2. 分页插件
3. 分页插件
4. 定义的认证机制
5. HRM中的TOKEN实现与验证

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

