# 10-用户登录-代码实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们接下来讲解用户登录这一块

那用户登录这一块呢

我们得先看一下它的表结构

那表结构比较简单

第一个是user name

用户登录的一个用户名

第二个是password

用户登录的一个密码

还有phone,email,currytime,update

还有reclaim,name

这些我都不看了

我们只看前面这两个就OK了

登录的时候

我们只需要根据前两个查询就可以了

它的密码呢

注意一下用了md5进行加密

所以我们密码匹配的时候

要用md5进行匹配

好我们先来实现一下这个登录

把我们的用户微服务打开

在这里我们写一个登录

返回user find by id

行这里写了

接着给它写一个实现

这个就是我们的用户登录

那这一块呢

直接用我们的

通讯器来写一下

我们的用户登录呢

通用mapper去实现就行了

by primary key

可以了

我们这里呢

要调用一次

用户登录

写个public result login

行我们开始写这里

get mapping

value

写个login

接收两个参数

第一个是用户名

第二个是password

好了这一块我们就搞定了

user name

接收两个参数

那现在我们登录这一块呢

怎么去登录呢

第一要先根据用户名

查询用户

对吧

那么查询之后

有可能用户不存在

这是一个

还有可能有什么现象呢

密码错误

那如果都正确的话

那就登录成功

好我们按照这几个点来处理一下

把这几个问题分别处理一下

先查询用户

user

等于是用户名

等于user service

fund by id

user name给他

好如果用户存在呢

存在user是不是就不顶空了呀

很顶空就不存在

result提示一下

写个force

写个status code

点arrow

提示账号不存在

好了在这一块

接着我们看密码错误

也是一样的

密码错误的

这应该是user.getpassword.ecourse

注意密码是md5加密了

所以这里要进行加密匹配

好了

这个如果说密码不正确的话

我们也要提示

最后是登录成功

那么登录成功这一块呢

我们先把这个响应的数据先给写一下

那这个就响应去了

这个就是ok了

后面这个是登录成功了

登录成功了

我们需要把令牌给用户

所以我们这里还要生成令牌才行

那我们先看一下令牌的载荷是什么

payload

我们就写个叫

payload

等于6hashmap

这里写个string

写个object

payload.

点

foot一下

把用户名给他

点

好

用户名给他

除了用户名我们还给点别的

用户自己的名字叫做name

还有一个是什么呢

那还有个phone

手机号都给他

user.get username

user.get name

可以了

还有一个是我们这一块

对应的一个手机号

user.get phone

好都可以了

接着不要忘了生成令牌jwt

tokenutil.

我们选择用户令牌生成令牌

第一个是随机数

点

托斯君

第二个是什么呢

注意第二个是当前载荷

payload

第三个是我们的

有效时间

我随便给个

好了

这是这一块

令牌生成之后我们要把它响应给用户的

token

好这个令牌我们要响应给用户

可以了登录这一块就搞定了

我们接着启动一下这个用户微服务

然后我们就开始设定这个用户微服务

现在我们来测试一下登录是否有效

在这里输入一个地址

18083

直接输入登录地址

user

login

user name

it黑码

password

it黑码

好回测一次

那么用户这一块密码错误

我们看一下看

it黑码

it

黑码

好我们看这一块它的密码是错误的

看看为什么密码是错误的呢

在这里打个断点

重来一次

过来了

首先用户是存在的

user.getpassword

password

行往后面走

这里是密码匹配了

咱得加个感叹号才行

对不对

加个感叹号就可以了

行

这是这一块我们来启动测试一次

测试一次之后呢我们

等会就来

看一下令牌生成的一个结果是什么

怎么样的

好再刷新一次

等后台服务器

等后台服务启动

再刷一次

诶来了

跳过

那么这个令牌数据就过来了

这个令牌数据的是遵循了jwt的一个格式

你看这里会有一个点

还有另外一个点

有两个点的

咱就不找了

这个不好找

行

这是我们这个用户登录

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是《秒杀系统》系列课程中“用户登录”功能的实现教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 Spring Boot 项目中实现一个完整的用户登录接口。核心内容包括：定义用户登录的 RESTful API、编写控制器（Controller）层的登录方法、调用服务层（Service）进行用户查询和密码校验、使用 JWT（JSON Web Token）生成登录凭证，并最终通过浏览器测试接口。整个过程强调了前后端分离架构下的数据交互和安全验证。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，展示课程大纲，明确当前章节为“2.2 用户登录”。
*   **00:05 - 00:15**: 讲师展示数据库表结构 `tb_user` 的 SQL 创建语句，说明用户信息存储在数据库中。
*   **00:15 - 00:30**: 讲师在 `UserController` 中编写 `@GetMapping("/login")` 的登录接口方法，定义了接收用户名和密码的参数。
*   **00:30 - 00:45**: 讲师在 `UserController` 中编写登录逻辑，首先调用 `userService.findById(username)` 查询用户。
*   **00:45 - 00:55**: 讲师编写用户不存在的判断逻辑，返回错误信息。
*   **00:55 - 01:05**: 讲师编写密码校验逻辑，使用 `DigestUtils.md5DigestAsHex` 对用户密码和输入密码进行 MD5 加密后比较。
*   **01:05 - 01:15**: 讲师编写登录成功逻辑，使用 `UUID` 生成唯一 ID，并调用 `JwtUtil.generateTokenUser` 方法生成 JWT。
*   **01:15 - 01:25**: 讲师在 `UserController` 中返回包含 `flag=true`、`code=20000` 和 `message="登录成功！"` 的 JSON 响应。
*   **01:25 - 01:35**: 讲师在浏览器中访问 `http://localhost:18083/user/login?username=itheima&password=itheima`，成功获取登录凭证。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**: “第3章 热点隔离+抢单实现” -> “2.2 用户登录”。
*   **数据库表结构**: `CREATE TABLE tb_user ( ... ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';`。

#### 代码关键内容

*   **用户登录接口定义**:
    ```java
    @GetMapping(value = "/login")
    public Result login(String username, String password) throws Exception {
        // 1. 根据用户名查询用户信息
        User user = userService.findById(username);
        // 2. 用户不存在
        if (user == null) {
            return new Result(flag: false, StatusCode.ERROR, message: "账号不存在！");
        }
        // 3. 密码错误
        if (!user.getPassword().equals(DigestUtils.md5DigestAsHex(password.getBytes()))) {
            return new Result(flag: false, StatusCode.ERROR, message: "密码错误！");
        }
        // 4. 登录成功
        String uid = UUID.randomUUID().toString();
        Map<String, Object> payload = new HashMap<>();
        payload.put("uid", uid);
        payload.put("username", user.getUsername());
        payload.put("phone", user.getPhone());
        payload.put("nickname", user.getNickname());
        payload.put("created", user.getCreated());
        payload.put("updated", user.getUpdated());
        payload.put("name", user.getName());
        String token = JwtUtil.generateTokenUser(uid, payload, 3600 * 1000);
        return new Result(flag: true, StatusCode.OK, message: "登录成功！");
    }
    ```

*   **JWT 生成工具类方法**:
    ```java
    public static String generateTokenUser(String uid, Map<String, Object> payload, long ttlMillis) {
        // 生成 JWT 的核心逻辑（此处为示意，实际代码可能包含密钥、过期时间等参数）
        return Jwts.builder()
            .setSubject(uid)
            .setClaims(payload)
            .setExpiration(new Date(System.currentTimeMillis() + ttlMillis))
            .signWith(SignatureAlgorithm.HS256, "your-secret-key")
            .compact();
    }
    ```

*   **用户服务层方法**:
    ```java
    public User findById(String username) {
        // 伪代码，实际会查询数据库
        return userMapper.selectByUsername(username);
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库表结构设计**
    *   **描述**: 讲师首先展示了用户表 `tb_user` 的 SQL 创建语句，明确了用户信息（如用户名、密码、手机号、注册时间等）的存储结构。这为后续的用户查询和登录功能奠定了数据基础。

*   **场景二：登录接口开发**
    *   **描述**: 讲师在 `UserController` 中逐步编写 `login` 方法。首先定义了接口路径和参数，然后通过 `userService.findById(username)` 查询用户。接着，通过 `if (user == null)` 判断用户是否存在，不存在则返回错误信息。随后，通过 `DigestUtils.md5DigestAsHex` 对用户密码和输入密码进行 MD5 加密比较，校验密码是否正确。最后，如果登录成功，生成一个包含用户信息的 JWT，并返回给前端。

*   **场景三：JWT 生成与返回**
    *   **描述**: 讲师在登录成功后，使用 `UUID` 生成一个唯一的用户 ID，并将用户信息（如用户名、手机号、昵称等）封装到一个 `Map` 中。然后调用 `JwtUtil.generateTokenUser` 方法生成 JWT，并将其作为响应的一部分返回给前端。JWT 通常包含用户身份信息和过期时间，用于后续的接口访问认证。

*   **场景四：浏览器测试**
    *   **描述**: 讲师在浏览器中访问 `http://localhost:18083/user/login?username=itheima&password=itheima`，成功获取了登录凭证。这验证了登录接口的正确性，前端可以通过解析返回的 JWT 来实现用户身份的认证和授权。
