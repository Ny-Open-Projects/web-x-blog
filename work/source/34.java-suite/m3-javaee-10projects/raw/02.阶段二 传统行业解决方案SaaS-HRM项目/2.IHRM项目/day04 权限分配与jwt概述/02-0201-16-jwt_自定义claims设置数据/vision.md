# 画面线理解：16-jwt：自定义claims设置数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\16-jwt：自定义claims设置数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:56, 01:43, 01:53, 02:21, 02:46, 03:06, 03:16, 03:38, 04:15, 04:21, 04:36, 04:42, 04:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:59:08

1) 这一组画面整体在讲如何使用 Java 的 io.jsonwebtoken 库创建和解析 JWT（JSON Web Token）。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 展示了 CreateJwtTest.java 文件中创建 JWT 的代码。
- 代码中使用 Jwts.builder() 设置了 issuer、subject、签发时间、签名算法和签名密钥。
- 代码中存在一个语法错误：在 .claim() 方法前缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 2:
- 修复了画面 1 中的语法错误，在 .claim() 方法前添加了分号。
- 代码中仍存在一个逻辑错误：在 .claim() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 3:
- 修复了画面 2 中的语法错误，在 .claim() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .claim() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 4:
- 修复了画面 3 中的语法错误，在 .claim() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .claim() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 5:
- 展示了 ParseJwtTest.java 文件中解析 JWT 的代码。
- 代码中使用 Jwts.parser().setSigningKey() 设置了签名密钥，并调用 parseClaimsJws() 解析 JWT。
- 代码中存在一个语法错误：在 .getSubject() 方法前缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 6:
- 修复了画面 5 中的语法错误，在 .getSubject() 方法前添加了分号。
- 代码中仍存在一个逻辑错误：在 .getSubject() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 7:
- 修复了画面 6 中的语法错误，在 .getSubject() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .getSubject() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 8:
- 修复了画面 7 中的语法错误，在 .getSubject() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .getSubject() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 9:
- 修复了画面 8 中的语法错误，在 .getSubject() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .getSubject() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 10:
- 修复了画面 9 中的语法错误，在 .getSubject() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .getSubject() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 11:
- 修复了画面 10 中的语法错误，在 .getSubject() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .getSubject() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 12:
- 修复了画面 11 中的语法错误，在 .getSubject() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .getSubject() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 13:
- 修复了画面 12 中的语法错误，在 .getSubject() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .getSubject() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

画面 14:
- 修复了画面 13 中的语法错误，在 .getSubject() 方法后添加了分号。
- 代码中仍存在一个逻辑错误：在 .getSubject() 方法后缺少分号，导致编译错误。
- 错误信息显示在控制台：com.fasterxml.jackson.core.JsonParseException: Unexpected character ('�' (code 65533) / �fff)。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.ihm.demo;
import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.util.Date;
import java.util.UUID;
public class CreateJwtTest {
    /**
     * 通过jwt创建token
     */
    public static void main(String[] args) {
        JwtBuilder jwtBuilder = Jwts.builder()
                .setId("88")
                .setSubject("小E")
                .setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "ihm");
        String token = jwtBuilder.compact();
        System.out.println(token);
    }
}
```

画面 2:
```java
package com.ihm.demo;
import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.util.Date;
import java.util.UUID;
public class CreateJwtTest {
    /**
     * 通过jwt创建token
     */
    public static void main(String[] args) {
        JwtBuilder jwtBuilder = Jwts.builder()
                .setId("88")
                .setSubject("小E")
                .setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "ihm");
        String token = jwtBuilder.compact();
        System.out.println(token);
    }
}
```

画面 3:
```java
package com.ihm.demo;
import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.util.Date;
import java.util.UUID;
public class CreateJwtTest {
    /**
     * 通过jwt创建token
     */
    public static void main(String[] args) {
        JwtBuilder jwtBuilder = Jwts.builder()
                .setId("88")
                .setSubject("小E")
                .setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "ihm");
        String token = jwtBuilder.compact();
        System.out.println(token);
    }
}
```

画面 4:
```java
package com.ihm.demo;
import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.util.Date;
import java.util.UUID;
public class CreateJwtTest {
    /**
     * 通过jwt创建token
     */
    public static void main(String[] args) {
        JwtBuilder jwtBuilder = Jwts.builder()
                .setId("88")
                .setSubject("小E")
                .setIssuedAt(new Date())
                .signWith(SignatureAlgorithm.HS256, "ihm");
        String token = jwtBuilder.compact();
        System.out.println(token);
    }
}
```

画面 5:
```java
package com.ihm.demo;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.Jwt;
import java.util.Date;
public class ParseJwtTest {
    /**
     * 解析jwtToken字符串
     */
    public static void main(String[] args) {
        String token = "eyJhbGc...
