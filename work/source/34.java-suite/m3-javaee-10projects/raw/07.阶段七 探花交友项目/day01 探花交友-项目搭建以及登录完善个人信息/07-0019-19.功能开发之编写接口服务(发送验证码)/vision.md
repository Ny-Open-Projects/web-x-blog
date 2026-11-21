# 画面线理解：19.功能开发之编写接口服务（发送验证码）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\19.功能开发之编写接口服务（发送验证码）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 02:14, 03:08, 03:51, 05:13, 06:07, 07:00, 08:03, 08:54, 10:19, 11:40, 12:50, 14:07, 15:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:10:13

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中实现短信验证码功能的完整代码流程，包括接口定义、服务层实现、控制器层编写和配置文件设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了项目中用于定义接口的文档，其中包含一个 mock 接口的地址：https://mock.boxugu.com/project/764/interface/api/11011。
画面 2: 展示了项目结构，重点在 `com.tanhua.sso.service` 包下的 `TestSmsService.java` 文件，其中定义了一个 `ErrorResult` 类，用于封装错误信息。
画面 3: 展示了 `SmsService.java` 文件中的 `sendSms` 方法，用于向短信平台发送验证码，其中包含请求 URL、参数（如 `sid`, `token`, `appid`, `templateid`, `mobile`）和生成随机验证码的逻辑。
画面 4: 展示了 `BaseMapper.java` 文件中的部分方法，包括 `update`、`selectById` 和 `selectBatchIds` 等用于数据库操作的接口。
画面 5: 展示了 `SmsService.java` 文件中 `sendSms` 方法的完整代码，包括构建请求参数、发送请求并解析响应体的逻辑。
画面 6: 展示了 `SmsService.java` 文件中 `sendCheckCode` 方法的完整代码，包括发送短信、处理异常、将验证码存入 Redis 以及返回结果的逻辑。
画面 7: 展示了 `SmsController.java` 文件的初始代码，包含 `@RequestMapping` 和 `@RestController` 注解。
画面 8: 展示了 `SmsController.java` 文件中 `@PostMapping("login")` 方法的代码，用于处理登录请求。
画面 9: 展示了 `SmsController.java` 文件中 `@PostMapping("login")` 方法的代码，其中定义了 `smsService` 字段并开始编写方法体。
画面 10: 展示了 `SmsService.java` 文件中 `sendCheckCode` 方法的代码，其中包含获取 Redis 中的验证码、判断是否过期、调用 `sendSms` 方法、存入 Redis 以及返回结果的逻辑。
画面 11: 展示了 `SmsController.java` 文件中 `@PostMapping("login")` 方法的代码，其中使用了 `@Autowired` 注解注入 `SmsService`，并开始编写方法体。
画面 12: 展示了 `SmsController.java` 文件中 `@PostMapping("login")` 方法的代码，其中使用了 `ErrorResult.ErrorResultBuilder` 构建返回结果，并根据 `code` 值返回不同的响应。
画面 13: 展示了 `SmsController.java` 文件中 `@PostMapping("login")` 方法的代码，其中在 `code == 1` 的情况下，将错误信息设置到 `builder` 中并返回。
画面 14: 展示了 `MyApplication.java` 文件的代码，其中使用了 `@MapperScan` 注解扫描 mapper 接口，并使用 `@SpringBootApplication` 注解启动 Spring Boot 应用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
地址：https://mock.boxugu.com/project/764/interface/api/11011
```

画面 2:
```java
package com.tanhua.sso.vo;
import lombok.Builder;
@Builder
public class ErrorResult {
    private String errCode;
    private String errMsg;
}
```

画面 3:
```java
public String sendSms(String mobile) {
    String url = "https://open.ucpaas.com/ol/sms/sendsms";
    Map<String, Object> params = new HashMap<>();
    params.put("sid", "566523e850c8b5e92d512a8dab6f");
    params.put("token", "41fabadd9a221ab4a439548b4dc88433");
    params.put("appid", "dd7d74e604284a4b9cc668c6591c84c7");
    params.put("templateid", "487656");
    params.put("mobile", mobile);
    // 生成6位验证码
    params.put("param", RandomUtils.nextInt(100000, 999999));
    ResponseEntity<String> responseEntity = this.restTemplate.postForEntity(url, params, String.class);
    String body = responseEntity.getBody();
    try {
        JsonNode jsonNode = MAPPER.readTree(body);
        //000000 表示发送成功
        if (StringUtils.equals(jsonNode.get("code").textValue(), "000000")) {
            return String.valueOf(jsonNode.get("param"));
        }
    }
```

画面 4:
```java
/**
 * 根据 whereEntity 条件，更新记录
 * @param entity 实体对象（set 条件值，可以为 null，里面的 entity 用于生成 where 条件）
 * @param updateWrapper 实体对象包装类（可以为 null，里面的 entity 用于生成 where 条件）
 */
int update(@Param(Constants.ENTITY) T entity, @Param(Constants.WRAPPER) Wrapper<T> updateWrapper);

/**
 * 根据 ID 查询
 * @param id 主键ID
 */
T selectById(Serializable id);

/**
 * 查询（根据ID 批量查询）
 * @param idList 主键ID列表（不能为 null 以及 empty）
 */
List<T> selectBatchIds(@Param(Constants.COLLECTION) Collection<? extends Serializable> idList);
```

画面 5:
```java
public String sendSms(String mobile) {
    String url = "https://open.ucpaas.com/ol/sms/sendsms";
    Map<String, Object> params = new HashMap<>();
    params.put("sid", "566523e850c8b5e92d512a8dab6f");
    params.put("token", "41fabadd9a221ab4a439548b4dc88433");
    params.put("appid", "dd7d74e604284a4b9cc668c6591c84c7");
    params.put("templateid", "487656");
    params.put("mobile", mobile);
    // 生成6位验证码
    params.put("param", RandomUtils.nextInt(100000, 999999));
    ResponseEntity<String> responseEntity = this.restTemplate.postForEntity(url, params, String.class);
    String body = responseEntity.getBody();
    try {
        JsonNode jsonNode = MAPPER.readTree(body);
        //000000 表示发送成功
        if (StringUtils.equals(jsonNode.get("code").textValue(), "000000")) {
            return String.valueOf(jsonNode.get("param"));
        }
    }
```

画面 6:
```java
String code = this.sendSms(mobile);
if (null == code) {
    result.put("code", 2);
    result.put("msg", "发送短信验证码失败");
    return result;
}
//发送验证码成功
result.put("code", 3);
result.put("msg", "ok");
this.redisTemplate.opsForValue().set(redisKey, code, Duration.ofMinutes(2));
return result;
} catch (Exception e) {
    LOGGER.error("发送验证码出错！" + mobile, e);
    result.put("code", 4);
    result.put("msg", "发送验证码码出现异常");
    return result;
}
```

画面 7:
```java
package com.tanhua.sso.controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
public class SmsController {
}
```

画面 8:
```java
package com.tanhua.sso.controller;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RequestMapping("user")
@RestController
public class SmsController {
    @PostMapping("login")
    public ResponseEntity<Object> sendCheckCode(@RequestHeader Map<String, Object> param) {
    }
}
```

画面 9:
```java
package com.tanhua.sso.controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;
@RequestMapping("user")
@RestController
public class SmsController {
    private SmsService smsService;
    @PostMapping("login")
    public ResponseEntity<Object> sendCheckCode(@RequestBody Map<String, Object> param) {
        String phone = String.valueOf(param.get("phone"));
    }
}
```

画面 10:
```java
Map<String, Object> result = new HashMap<>(initialCapacity: 2);
try {
    String redisKey = "CHECK_CODE_" + mobile;
    String value = this.redisTemplate.opsForValue().get(redisKey);
    if
