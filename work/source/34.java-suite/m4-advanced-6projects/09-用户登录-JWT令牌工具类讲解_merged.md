# 09-用户登录-JWT令牌工具类讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们讲解用户登录,用户在抢单的时候是必须要先登录的,所以我们这个功能得先做一下。

那用户登录之后,在其他的服务里面要人识别用户的身份,那这个该怎么做呢?

我们这一块采用JWT令牌,用JWT令牌保存用户的一个身份信息。

那用户每次抢单的时候,需要把这个JWT令牌携带过去,携带过去之后那边会去解析对应的JWT令牌。

一旦解析成功,那就表示这个用户身份信息没有问题,就允许他去抢单了。

好,那这个JWT令牌这一块呢,我们就不去详细讲解了。

我们这里给大家提供了一个工具类,这个工具类用于生成令牌,我们把这个工具类讲解一下。

在我们这个工程里面,COMM工程里,有一个工具类,这里有一个叫做JWT-Util。

这个工具类呢,我们介绍一下。

上面这两个是密钥,这个呢是给管理员生成令牌的。

给管理员生成令牌,他们唯一不同点是密钥不同。

好,下面这个是给我们普通用户生成令牌的。

那普通用户生成令牌,用上面这个密钥。

生成令牌呢,其实方法在下面这里。

这一块我们就不去详细讲解,大家可以去看一下就可以了。

好,生成了令牌之后,我们接着就可以去用令牌了。

用令牌很多时候要解析令牌的正确性,那这一块会解析令牌。

令牌呢,你传的时候,可以传BARER,也可以不传,都行。

解析令牌之后,会把令牌的明文信息给你返回过去。

那我们这里也做一个简单的测试。

这个测试呢,这是生成普通用户的令牌。

这里写的是username等于网5,A,C,B,D,这是谁写的一些数据。

我们生成一下这个令牌。

生成之后,我们把令牌打印一次,然后再解析一次令牌。

右键运行。

好,令牌就生成了。

这块是我们对的JWT令牌。

这一块是JWT令牌。

这一块是令牌的一个明文信息。

那如果你想生成管理员的令牌,这一块只需要换一下就行了。

换成谁呢?我们简单介绍一下。

admin的就可以了。

好,右键运行。

他们这一块流程没有什么区别,只是说密钥不同而已。

看这一块,生成也是没有问题的。

但是问题点在解析这一块。

解析的时候呢,注意,我们这个解析啊,

用的是当前这个密钥在解析的。

这个是普通用户的密钥。

而我们要解析的话,应该用管理员的密钥。

所以这个管理员这儿有点小问题。

我们可以把它换一下,测试一下就行了。

但是一会儿我们还是得换回来哈。

好,测试一次。

这个就没有问题了。

好,OK。

我们把这个给换回去。

这个就是我们JWT令牌工具类的一个使用。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于“秒杀系统”技术课程中“用户登录”模块的讲解，具体聚焦于使用 JWT（JSON Web Token）技术来实现用户身份认证。讲师通过 IntelliJ IDEA 开发环境，演示了如何在 `seckill-common` 模块中创建 `JwtTokenUtil` 工具类，用于生成管理员和普通用户的 JWT 令牌，并展示了如何解析和验证这些令牌。整个过程旨在为后续的抢购功能提供安全的身份验证机制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 PPT 上展示课程大纲，当前章节为“2.1 Jwt令牌”。
*   **00:00:05 - 00:00:15**: 讲师在 PPT 上解释 JWT 的作用：用于实现用户登录，登录成功后，每次抢购时需要识别用户身份，因此采用 JWT 令牌保存用户信息。
*   **00:00:15 - 00:00:30**: 讲师在 PPT 上说明，JWT 令牌的生成逻辑中，管理员和普通用户的令牌密钥是不同的。
*   **00:00:30 - 00:00:45**: 讲师在 PPT 上指出，需要在 `seckill-common` 工程中添加 `JwtTokenUtil` 类，并在 `com.seckill.util` 包下实现。
*   **00:00:45 - 00:01:00**: 讲师切换到代码编辑器，展示 `JwtTokenUtil` 类的初始代码结构，包括 `SECRETUSER` 和 `SECRETADMIN` 两个静态常量字段。
*   **00:01:00 - 00:01:15**: 讲师在代码中定义了 `generateTokenAdmin` 和 `generateTokenUser` 两个静态方法，分别用于生成管理员和普通用户的令牌。
*   **00:01:15 - 00:01:30**: 讲师在代码中定义了 `generateToken` 方法，用于实际生成 JWT 令牌，该方法接收用户 ID、负载信息和有效期，并使用指定的密钥进行签名。
*   **00:01:30 - 00:01:45**: 讲师在代码中定义了 `parseToken` 方法，用于解析 JWT 令牌，提取其中的负载信息。
*   **00:01:45 - 00:02:00**: 讲师在 `main` 方法中编写了测试代码，用于生成一个普通用户的 JWT 令牌并打印出来。
*   **00:02:00 - 00:02:15**: 讲师运行代码，成功生成并打印出一个 JWT 令牌。
*   **00:02:15 - 00:02:30**: 讲师在 `main` 方法中修改代码，将生成令牌的逻辑改为使用管理员密钥 `SECRETADMIN`。
*   **00:02:30 - 00:02:45**: 讲师再次运行代码，成功生成并打印出一个管理员的 JWT 令牌。
*   **00:02:45 - 00:03:00**: 讲师在 `parseToken` 方法中修改密钥，使其使用管理员密钥 `SECRETADMIN` 来解析令牌。
*   **00:03:00 - 00:03:15**: 讲师再次运行代码，成功解析并打印出管理员令牌的负载信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**:
    *   **章节标题**: “2.1 Jwt令牌”。
    *   **核心概念**: JWT 用于用户登录和身份识别。
    *   **技术细节**: 管理员和普通用户的令牌密钥不同。
    *   **代码位置**: `seckill-common` 工程中的 `com.seckill.util.JwtTokenUtil` 类。

*   **代码关键内容**:
    *   **类定义**: `public class JwtTokenUtil {`
    *   **密钥常量**:
        ```java
        public static final String SECRETUSER = "Sp116a005YaNS7605Lmf5q+USL.INSLiK5bCP6ZuF55ge66yR"; //用户
        public static final String SECRETADMIN = "ADMINsp116a005YaNS7605Lmf5q+USL.INSLiK5bCP6ZuF55ge66yR"; //管理员
        ```
    *   **生成令牌方法**:
        ```java
        public static String generateTokenAdmin(String uid, Map<String, Object> payload, long ttlMillis) throws Exception {
            return generateToken(uid, payload, ttlMillis, SECRETADMIN);
        }

        public static String generateTokenUser(String uid, Map<String, Object> payload, long ttlMillis) throws Exception {
            return generateToken(uid, payload, ttlMillis, SECRETUSER);
        }
        ```
    *   **核心生成方法**:
        ```java
        public static String generateToken(String uid, Map<String, Object> payload, long ttlMillis, String secret) throws Exception {
            SignatureAlgorithm signatureAlgorithm = SignatureAlgorithm.HS256;
            long nowMillis = System.currentTimeMillis();
            Date now = new Date(nowMillis);
            Key signingKey = new SecretKeySpec(secret.getBytes(), signatureAlgorithm.getJcaName());
            Map<String, Object> header = new HashMap<>();
            header.put("typ", "JWT");
            header.put("alg", "HS256");
            JwtBuilder builder = Jwts.builder().setId(uid)
                    .setIssuedAt(now)
                    .setSubject(uid)
                    .setHeader(header)
                    .signWith(signatureAlgorithm, signingKey);
            builder.addClaims(payload);
            return builder.compact();
        }
        ```
    *   **解析令牌方法**:
        ```java
        public static Map<String, Object> parseToken(String token) {
            if (token.startsWith("Bearer")) {
                token = token.substring(6).trim();
            }
            SignatureAlgorithm signatureAlgorithm = SignatureAlgorithm.HS256;
            Key signingKey = new SecretKeySpec(SECRETUSER.getBytes(), signatureAlgorithm.getJcaName());
            Claims claims = Jwts.parser()
                    .setSigningKey(signingKey)
                    .parseClaimsJws(token)
                    .getBody();
            return claims;
        }
        ```
    *   **测试代码**:
        ```java
        public static void main(String[] args) throws Exception {
            Map<String, Object> payload = new HashMap<>();
            payload.put("username", "wangwu");
            payload.put("aaa", "ccc");
            payload.put("bbb", "ddd");
            String token = generateTokenUser(UUID.randomUUID().toString(), payload, 10000000L);
            System.out.println(token);
            System.out.println(parseToken(token));
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：JWT 令牌的引入与设计** (00:00:00 - 00:00:45)
    *   讲师在 PPT 上展示课程大纲，明确当前讲解的是“2.1 Jwt令牌”。
    *   讲师解释了 JWT 的作用：在用户登录后，用于在每次抢购时识别用户身份。
    *   讲师强调，为了安全，管理员和普通用户的令牌密钥是不同的。
    *   讲师指出，需要在 `seckill-common` 工程中创建 `JwtTokenUtil` 类来实现这些功能。

*   **场景二：JWT 令牌的生成与解析** (00:00:45 - 00:02:45)
    *   讲师在代码编辑器中展示 `JwtTokenUtil` 类的初始代码结构。
    *   讲师定义了 `SECRETUSER` 和 `SECRETADMIN` 两个密钥常量。
    *   讲师定义了 `generateTokenAdmin` 和 `generateTokenUser` 方法，分别用于生成管理员和普通用户的令牌。
    *   讲师定义了核心的 `generateToken` 方法，该方法使用 `Jwts` 工具类，设置令牌的头部、主体和签名。
    *   讲师定义了 `parseToken` 方法，用于解析 JWT 令牌并提取负载信息。
    *   讲师在 `main` 方法中编写了测试代码，首先生成一个普通用户的令牌并打印。
    *   讲师修改代码，将生成令牌的密钥改为管理员密钥 `SECRETADMIN`，并再次运行，成功生成并打印出管理员令牌。
    *   讲师修改 `parseToken` 方法，使其使用管理员密钥 `SECRETADMIN` 来解析令牌，并再次运行，成功解析并打印出管理员令牌的负载信息。

*   **场景三：代码调试与
