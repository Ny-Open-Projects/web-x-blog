# 09.环信用户系统集成之获取管理员权限（测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\09.环信用户系统集成之获取管理员权限（测试）_【海量资源尽在 666java.com】.mp4
- 时长 2分49秒（音频 169s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来测试一下刚刚我们所写的这个Service中的这个方法那么我们还是回到SSO工程然后呢去编写一个测试用例我们来测试一下那我们就把这个来拷贝一下吧拷贝一下它然后呢我们去test就是我们这个环信然后环信的一个tokenservice好那我们来打开它来看一下然后这个里面我们需要注的就是
[00:28] 所以刚刚我们所写的那个还信token Service把它注入进来然后我们去做一个test一个get一个token这样的一个测试然后我们去通过this.Service.gettoken去做一个获取那么拿到这个token之后我们把这个token就打印出来
[00:53] 好嘞那么我们在这个位置去打一个断点那么接下来呢我们来debug去启动它好那我们来等待它的一个启动好那么请求呢就进入了对吧然后呢我们就跟踪一下呃走先去到ready时之后去做一个命中那么现在呢我们肯定是没有数据的对吧所以呢我们就拿到生蛋了啊然后呢我们去拼接这个url来看一下这个url的一个
[01:20] 情况是这样的一个地址然后呢我们继续往下面走去拼接我们这个请求的参数然后呢去请求环境的接口然后呢是不是就拿到响应了然后呢我们继续往下面走拿到这个body那我们来看一下这个是响应体那么这个呢是响应体我们来看一下它的值应该是
[01:46] 这样来看吧这样的话就看清楚了对吧这个呢就是access token就这样的一个值然后呢下面是我们的有效期时间然后呢我们往下面走分别拿到这两个值对吧一个是我们的access token还有就是有效期时间然后呢我们给它去做了一个减去一天的这样的一个时间然后呢把它存储到我们的ready store最后呢做一个返回
[02:13] 好通过好这样的话呢我们这个测试是不是就OK了那我们再次做一次这个测试那我们来看一下从Redis中的命中的一个情况好我们等待它的一个执行好那么这个断点呢就来了然后呢我们去执行一下走那么显然呢它肯定是会通过我们的通过我们Redis呢去命中数据其实命中了然后呢判断不为空那我们就直接按return
[02:41] 这样的话呢我们就满足我们这样的一个使用场景的一个需求了OK好那么关于这个测试呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过测试类调用 HuanXinTokenService 获取并缓存 OAuth2 访问令牌，并通过调试器观察执行过程和返回结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
要点：展示 HuanXinTokenService.java 中 getToken 方法的实现，包含从 HTTP 响应体中解析 access_token 和 expires_in，以及将 token 存入 Redis 的逻辑。

画面 2：
要点：展示 HuanXinTokenService.java 中的类成员变量定义，包括静态常量 tokenRedisKey 和 @Autowired 注入的 redisTemplate。

画面 3：
要点：展示 TestHuanXinTokenService.java 中的 @Test 方法 testSend，用于测试短信服务。

画面 4：
要点：展示 TestHuanXinTokenService.java 中的 import 语句，包含 org.springframework.boot.test.context.SpringBootTest 和 org.junit.Test。

画面 5：
要点：展示 TestHuanXinTokenService.java 中的 import 语句，包含 org.springframework.boot.test.context.SpringBootTest。

画面 6：
要点：展示 TestHuanXinTokenService.java 中的 @Test 方法 testGetToken，用于测试 getToken 方法。

画面 7：
要点：在调试模式下，断点位于 HuanXinTokenService 的 getToken 方法中，准备执行。

画面 8：
要点：调试器执行到 getToken 方法中，变量 url 被赋值为 "http://al.../token"，并创建了参数 Map。

画面 9：
要点：调试器执行到 getToken 方法中，变量 body 被赋值为 JSON 字符串，包含 application 和 access_token 字段。

画面 10：
要点：调试器执行到 getToken 方法中，变量 body 的值被完整显示。

画面 11：
要点：调试器执行到 getToken 方法中，将 token 存入 Redis，并返回 access_token。

画面 12：
要点：调试器执行完毕，TestHuanXinTokenService.testGetToken 方法的测试完成。

画面 13：
要点：调试器执行到 getToken 方法中，准备执行。

画面 14：
要点：调试器执行完毕，TestHuanXinTokenService.testGetToken 方法的测试完成，控制台输出 token 值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
String body = responseEntity.getBody();
try {
    JsonNode jsonNode = MAPPER.readTree(body);
    String accessToken = jsonNode.get("access_token").asText();
    // 过期时间，提前一天失效
    Long expiresIn = jsonNode.get("expires_in").asLong() - 86400;
    // 将Token值存储到本地，存储到Redis中
    this.redisTemplate.opsForValue().set(tokenRedisKey, accessToken, expiresIn, TimeUnit.SECOND);
    return accessToken;
} catch (Exception e) {
    e.printStackTrace();
}
return null;
```

画面 2：
```java
private static final ObjectMapper MAPPER = new ObjectMapper();
@Autowired
private RedisTemplate<String, String> redisTemplate;
private static final String tokenRedisKey = "HUANXIN_TOEKN";
```

画面 3：
```java
@Test
public void testSend() {
    this.smsService.sendSms(mobile: "15800807944");
    System.out.println(code);
}
```

画面 4：
```java
import org.springframework.boot.test.context.SpringBootTest;
import org.junit.Test;
import net.bytebuddy.asm.Advice;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test

