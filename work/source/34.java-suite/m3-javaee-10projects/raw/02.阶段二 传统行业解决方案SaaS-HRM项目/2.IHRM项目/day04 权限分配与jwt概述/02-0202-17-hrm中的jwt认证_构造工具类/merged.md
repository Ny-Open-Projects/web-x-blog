# 17-hrm中的jwt认证：构造工具类

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\17-hrm中的jwt认证：构造工具类_【海量资源尽在 ubkz.com】.mp4
- 时长 8分57秒（音频 538s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们看过了当前JWT的一个基本的使用接下来在我们的系统当中刚才说过了要完成第一个其实就是基于JWT的一个身份认证的这么一个操作所以接下来在我们这个工程当中就使用JWT的形式我们来看一下如何完成我们一个用户的登录以及看一下如何获取当前登录的这些数据
[00:27] 那我们应该怎么做呢首先呢就是对于JWT操作来说我们可以把它封装到一个工具类当中通过工具类的形式我们操作起来更加方便一点当然工具类的代码比较简单都跟我们之前写的差不多那在这边呢我去定位到我们的common包在我们的common包下写一个我们的工具类就放到Utils下了好了这边呢创建一个class这个工具类叫什么名字呢其实很无所谓了JWT Utils
[01:00] 好了那接下来那在这当中呢我可以给它一些基本的一些属性的一些设置比如说呢我们可以死郡private死郡类型的来一个key当然了至于这个key究竟代表什么含义指的是我们签名的私钥就是我们设置签名的时候不是要设置一个自己独一无二的字幕串并且这个字幕串不能让人家去知道吗好了这个就是我们签名的私钥私钥好了那除了签名私钥之外呢还可以给它来一个比如说private love类型的叫做TTL
[01:33] 那这个TTL代表什么含义是因为我们签发的这个签名啊有可能带有失效性所以这边可以给他设置一个签名的时间签名的我们叫做失效时间OK那好了由于我要设置到他的用他的get set方法所以这里面呢我配置上getterand setter好了这些都比较简单那接下来呢在这个工具类当中我们要提供两个方法第一个就是
[02:01] 设置签名token设置认证token还有一个解析我们叫做解析token字符串获取clamsok那好了接下来我们来看一下这两个方法如何去做首先呢第一个方法呢比较简单也不难我们之前都写过我就从之前的这边代码呢准备考一段过来好了
[02:36] 方法名称呢就叫做publicpublic得到的是一个字符串嘛死菌方法名称呢比如说我就叫做crate JWT好了那接下来把我们这个call过来的代码呢call过来拿过来那接下来就是对于我这个创建认证的时候呢要不要一些参数咱们可以做一个简单的声明由于这个里面可以设置一些ID和我们的一些subjects指的是我们的一些自己定义的一些内容那我们可以这样做就是set ID
[03:05] 我们可以把它理解为我们登录登录用户的 id登录用户 id 好了那这个 subject就是我们登录用户名好了那所以至于我这个方法呢需要这么两个参数第一个参数就是死菌类型的 id第二个参数死菌类型的比如说呢我就叫做 name 了当然了还有一些比如说呢我们可以自己指定一些 key value 的私有数据那这些呢我就传递一个 map 集合进来其实就可以好了死菌类型
[03:42] Object,Object,Map,那好了,接下来呢,我们可以把这个方法呢,一起给它补充,哎,完整,那这边呢,由于我们有一个失效时间的一个说明,所以我先呢,去配置一下,或者设置我们的失效时间,那设置了失效时间,那接下来第二件事呢,就是我们可以创建,我们叫做JWT Builder,那好了,接下来第三件事,我们可以根据,根据Map,
[04:14] 设置Klems好了接着第四件事我们第四件事我们是不是就可以获取就是创建创建token那对于这个失效时间呢我们需要进行一个计算因为我传过来TTL其实代表的是是在当前时间的基础之上我这个失效比如说呢60秒那就是它的有效期就是60秒比如说呢600秒那就是10分钟所以对于我们来说需要对当前时间进行一个计算
[04:44] 那比如说呢我可以设置一个lang类型的lang类型的它叫做now就是当前时间那当前时间很简单了system.system..current 10秒设置找到我们当前毫秒数那有了当前毫秒之后呢接下来设置一个它的失效时间yp那失效时间呢很简单呢我们就可以通过now加上我们的ttl就可以了加上我们的ttl
[05:18] 就可以了那这样一来呢我们失效时间已经准备好了那准备好了之后接下来根据我们刚才call过来的内容去创建JW Builder那创建JW Builder的时候呢ID就是我们传递过来的参数以及我们的NameOK好了那接下来呢这边我们的签名私钥我们可以通过key的方式给它指定好了那这边呢我们的数据太固定了所以这两个client也不要了
[05:44] 那这样一来我已经构造好了builder那构造好了builder就是根据map去设置clam那根据map去设置那也不难来一发循环好了那我们就可以map.entry好了死菌类型的object类型好了entrymap.entryset那接下来那怎么去做呢也不难jwtbuilder.好了我们可以setclams
[06:17] 当然了这个setClamS直接就是MAP集合那我们可以直接就设置MAP集合更加简单一些点setClamS把MAP集合存进去那好了接下来创建token那注意在创建token之前呢我们需要把这个失效时间也给它指定上啊打点setExpansion失效那里面接收的是你失效的一个data所以我new一个
[06:48] data 出来我们已经算好了他的毫秒数拿过来ok 那这样一来呢我们这个在builder就已经都搞定了搞定了之后接来我们可以通过zw builder帮我们创建出token接着进行返回就可以了returnok 那这样一来呢我这个工具类就已经写好了当然了是我们设置认证字符创的
[07:12] 那除了认证字符创之外呢我们还可以去解析token那解析token呢其实就更简单了我们解析token获取的是clams所以这边呢来一方法publicclamsc-l-e-i-m-sclamsok那好了这边呢p-a-r-s-eclamsc-w-t好了那注意这边你传的参数呢其实就是我们的一个token字符创了因为对于我们来说对于我们来说我上边登录成功调用给你生成
[07:45] 好了接下来你请求借口的时候我解析token获取到Klems拿到里面的数据那就是这么一个流程那接下来我们解析如何去做呢其实跟我们之前写的代码都一样都一样Ctrl C直接拿过来Ctrl V好了只不过呢我现在呢自己的私钥呢变成了key是一个动态传递的一个内容好了那这边的代码呢其实我们就已经都写好了接着return即可
[08:15] 好了这样一来我这个基本的工具类就已经写好了当然了这个工具类呢还少一点点配置那我要做到的事情是key跟ttl是以我们配置文件的形式给我传递过来那我们就要用到Springboard的配置文件所以我上面来一个atconfigurationpropertyproperties找一下找一下第一个就是
[08:42] 好了那我们这边呢可以做呢很简单我一会设置的时候呢哪个A服务要用我就给他设置一个比如说叫做JWT.confOK那这样一来我这个工具类就已经写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Spring Boot 项目中，通过编写 JwtUtils 工具类，实现 JWT 令牌的生成与解析功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录结构，当前位于“5.3 JWT工具类”章节，内容为在 hrm_common 工程中创建 JwtUtils 工具类。
画面2：在 IntelliJ IDEA 中，为 JwtUtils 类导入 lombok 的 @Getter 和 @Setter 注解。
画面3：在 JwtUtils 类中添加注释和私有成员变量 key 和 ttl。
画面4：开始编写 createJwt 方法，使用 JwtBuilder 设置 ID、主题、签发时间。
画面5：设置签名算法为 HS256，并添加公司 ID 和公司名称的声明。
画面6：继续完善 createJwt 方法，设置签发时间、签名算法和声明。
画面7：在方法中设置失效时间，使用 System.currentTimeMillis() 获取当前时间戳。
画面8：在方法中设置失效时间，使用 System.currentTimeMillis() 获取当前时间戳。
画面9：在方法中设置失效时间，使用 System.currentTimeMillis() 获取当前时间戳。
画面10：在方法中设置失效时间，使用 System.currentTimeMillis() 获取当前时间戳。
画面11：在方法中设置失效时间，使用 System.currentTimeMillis() 获取当前时间戳。
画面12：在方法中设置失效时间，使用 System.currentTimeMillis() 获取当前时间戳。
画面13：在方法中设置失效时间，使用 System.currentTimeMillis() 获取当前时间戳。
画面14：在方法中设置失效时间，使用 System.currentTimeMillis() 获取当前时间戳。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
在 hrm_common 工程中创建 jwtUtil 工具类
@configurationProperties("jwt.config")
public class JwtUtil {
private String key;
private long ttl;
public string getkey() {
return key;
}
public void setkey(string key) {
this.key = key;
}
public long getttl() {
return ttl;
}
public void settl(long ttl) {
this.ttl = ttl;
}

画面2：
package com.hrm.common.util;
public class JwtUtils {
//签名私钥
private String key;
private Long ttl;
}

画面3：
package com.hrm.common.util;
import lombok.Getter;
import lombok.Setter;
@Getter
@Setter
public class JwtUtils {
//签名私钥
private String key;
//签名有效期
private Long ttl;
}

画面4：
package com.hrm.common.util;
import lombok.Getter;
import lombok.Setter;
@Getter
@Setter
public class JwtUtils {
//签名私钥
private String key;
//签名有效期
private Long ttl;
}
/**
 * 设置认证token
 * id:登录用户id
 * subject:登录用户名
 */
public String createJwt(String id, String name, Map<String, Object> map) {
JwtBuilder jwtBuilder = Jwts.builder().setId("88").setSubject("小白")
.setIssuedAt(new Date())
.signWith(SignatureAlgorithm.HS256, "ihrm")
.claim("companyId", "123456")
.claim("companyName", "让乔传智播客教育股份有限公司")
String token = jwtBuilder.compact();
System.out.println(token);
}

画面5：
package com.hrm.common.util;
import lombok.Getter;
import lombok.Setter;
@Getter
@Setter
public class JwtUtils {
//签名私钥
private String key;
//签名有效期
private Long ttl;
}
/**
 * 设置认证token
 * id:登录用户id
 * subject:登录用户名
 */
public String createJwt(String id, String name, Map<String, Object> map) {
JwtBuilder jwtBuilder = Jwts.builder().setId("88").setSubject("小白")
.setIssuedAt(new Date())
.signWith(SignatureAlgorithm.HS256, "ihrm")
.claim("companyId", "123456")
.claim("companyName", "让乔传智播客教育股份有限公司")
String token = jwtBuilder.compact();
System.out.println(token);
}

画面6：
package com.hrm.common.util;
import lombok.Getter;
import lombok.Setter;
@Getter
@Setter
public class JwtUtils {
//签名私钥
private String key;
//签名有效期
private Long ttl;
}
/**
 * 设置认证token
 * id:登录用户id
 * subject:登录用户名
 */
public String createJwt(String id, String name, Map<String, Object> map) {
JwtBuilder jwtBuilder = Jwts.builder().setId("88").setSubject("小白")
.setIssuedAt(new Date())
.signWith(SignatureAlgorithm.HS256, "ihrm")
.claim("companyId", "123456")
.claim("companyName", "让乔传智播客教育股份有限公司")
String token = jwtBuilder.compact();
System.out.println(token);
}

画面7：
package com.hrm.common.util;
import java.util.Date;
import java.util.Map;
import java.util.Properties;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.atomic.AtomicReference;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicLongArray;
import java.util.concurrent.atomic.AtomicReferenceArray;
import java.util.concurrent.atomic.AtomicMarkableReference;
import java.util.concurrent.atomic.AtomicStampedReference;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicLongArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceArrayFieldUpdater;
import java.util.concurrent.atomic.AtomicMarkableReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicStampedReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent

