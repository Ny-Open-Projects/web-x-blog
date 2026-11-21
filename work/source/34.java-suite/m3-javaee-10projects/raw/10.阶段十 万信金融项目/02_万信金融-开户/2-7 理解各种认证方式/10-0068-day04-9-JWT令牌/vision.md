# 画面线理解：day04-9-JWT令牌

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-7 理解各种认证方式
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-7 理解各种认证方式\day04-9-JWT令牌_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:27, 02:21, 03:03, 03:49, 05:08, 05:27, 06:32, 06:41, 07:05, 08:11, 10:13, 12:11, 13:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:46:55

1) 这一组画面整体在讲什么（一句话）：
讲解JWT（JSON Web Token）的结构组成、工作原理、优缺点及安全机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 内容：介绍JWT是什么，定义为JSON Web Token (RFC 7519)，由Header、Payload、Signature三部分组成，用点（.）分隔。
- 代码示例：Header部分示例：
  {
    "alg": "HS256",
    "typ": "JWT"
  }

画面2：
- 内容：弹出记事本窗口，内容为“授权：我能干什么 授权一定发生在认证之后 有些功能你能使用，有些功能你不能使用”，并提及MySQL、视频网站VIP会员、token令牌、session、JWT令牌格式为JSON。

画面3：
- 内容：与画面1相同，展示JWT令牌结构的Header部分示例。

画面4：
- 内容：继续讲解JWT令牌结构，展示Header部分示例，并开始介绍Payload部分。
- 代码示例：Header部分示例：
  {
    "alg": "HS256",
    "typ": "JWT"
  }

画面5：
- 内容：展示JWT令牌的Payload部分示例，内容为JSON格式，包含iss、exp、sub等字段。
- 代码示例：Payload部分示例：
  {
    "sub": "1234567890",
    "name": "456",
    "admin": true
  }

画面6：
- 内容：讲解JWT令牌的Signature部分，说明其用于防止JWT内容被篡改，通过将Header和Payload进行Base64Url编码后，用点（.）连接，再用header中声明的签名算法进行签名。
- 代码示例：签名算法示例：
  HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    secret
  )

画面7：
- 内容：切换到PowerPoint编辑界面，显示一个文本框，内容为“{......} . {......} . {......}”。

画面8：
- 内容：在PowerPoint中，将多个窗口（如记事本、PDF、数据库）拖拽到幻灯片上，用于演示不同组件的交互。

画面9：
- 内容：与画面4相同，展示JWT令牌的Header部分示例。

画面10：
- 内容：讲解JWT令牌的签名部分，展示签名算法示例，并开始介绍JWT令牌的优点。
- 代码示例：签名算法示例：
  HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    secret
  )

画面11：
- 内容：展示一个生成的JWT令牌示例，包含Header、Payload、Signature三部分。
- 代码示例：生成的JWT令牌示例：
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYXV0aG9yaXphdGlvbiI6dHJ1ZSwiZXhwIjoxNTE2MjM5MDIyfQ.4s34567890123456789012345678901234567890123456789012345678901234

画面12：
- 内容：讲解JWT令牌的优点，包括基于JSON、可自定义内容、基于token认证、非对称加密算法安全。
- 代码示例：无。

画面13：
- 内容：继续讲解JWT令牌的优点，包括基于JSON、可自定义内容、基于token认证、非对称加密算法安全。
- 代码示例：无。

画面14：
- 内容：讲解JWT令牌的缺点，包括数据量较大、每次请求需传输、签名操作带来CPU和带宽开销。
- 代码示例：无。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
{
  "alg": "HS256",
  "typ": "JWT"
}

画面5：
{
  "sub": "1234567890",
  "name": "456",
  "admin": true
}

画面6：
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)

画面11：
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYXV0aG9yaXphdGlvbiI6dHJ1ZSwiZXhwIjoxNTE2MjM5MDIyfQ.4s34567890123456789012345678901234567890123456789012345678901234

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：什么是JWT？
内容：JWT令牌结构：Header、Payload、Signature三部分组成，每部分中间用点（.）分隔，比如：xxxxx.yyyyy.zzzzz。

画面5：
标题：Payload
内容：第二部分是负载，内容也是一个json对象，它可以存放有效信息的地方，它可以存放jwt提供的现成字段，比如：iss（签发者），exp（过期时间戳），sub（面向的用户）等，也可自定义字段。这部分不建议存放敏感信息，因为此部分可以解码还原原始内容。一个例子：
{
  "sub": "1234567890",
  "name": "456",
  "admin": true
}

画面6：
标题：Signature
内容：第三部分是签名，此部分用于防止jwt内容被篡改。这个部分使用base64url将前两部分进行编码，编码后使用点（.）连接组成字符串，最后使用header中声明 签名算法进行签名。一个例子：
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)

画面12：
标题：JWT令牌的优点：
1. JWT基于json，非常方便解析。
2. 可以在令牌中自定义丰富的内容，易扩展。
3. 基于token认证这种方式服务端不用存储认证数据，易维护，扩展性强，token 存在 localStorage 可避免 CSRF，并且可以实现web和app统一认证机制。
4. 通过非对称加密算法及数字签名技术，JWT防止篡改，安全性高。

画面14：
标题：JWT令牌的缺点：
token由于自包含信息，因此一般数据量较大，而且每次请求都需传递，因此比较占带宽。另外，token的签名签操作也会给cpu带来额外的负担。但是随着硬件的提升和带宽的提高，这些缺点变得越来越不足。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
