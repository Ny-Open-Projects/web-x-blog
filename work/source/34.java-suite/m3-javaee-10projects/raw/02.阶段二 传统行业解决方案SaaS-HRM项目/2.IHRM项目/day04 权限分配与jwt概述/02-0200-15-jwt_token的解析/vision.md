# 画面线理解：15-jwt：token的解析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\15-jwt：token的解析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:36, 00:47, 01:06, 01:45, 01:52, 02:04, 02:16, 02:44, 03:08, 03:13, 03:19, 03:25, 03:44, 04:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:58:17

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
画面14：在 IntelliJ IDEA 中，展示了 “ParseJwtTest.java” 文件的代码，终端显示“Exception in thread "main" io.jsonwebtoken.SignatureException: JWT signature does not match locally computed signature. JWT validity cannot be verified.”，表示 JWT 解析失败，签名不匹配。

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
