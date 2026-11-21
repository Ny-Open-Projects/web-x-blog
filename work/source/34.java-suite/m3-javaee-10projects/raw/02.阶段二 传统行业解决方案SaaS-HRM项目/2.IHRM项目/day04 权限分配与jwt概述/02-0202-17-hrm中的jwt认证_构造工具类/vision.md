# 画面线理解：17-hrm中的jwt认证：构造工具类

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\17-hrm中的jwt认证：构造工具类_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:32, 01:31, 02:35, 03:24, 03:44, 04:17, 04:59, 05:53, 06:14, 06:33, 07:11, 07:46, 08:16, 08:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:59:59

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
