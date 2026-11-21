# 19.功能开发之编写接口服务（发送验证码）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\19.功能开发之编写接口服务（发送验证码）_【海量资源尽在 666java.com】.mp4
- 时长 15分7秒（音频 907s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么前面呢我们已经编写完成了发送短信验证码的这个接口那么接下来呢我们就来看一下那么我们现在就需要为我们的前端呢去提供这个接口服务了那么下面呢我们来看一下我们这个MOOC接口那么就是那么我们后端和前端呢在做这个对接的时候啊那我们先以这个MOOC接口啊为准
[00:26] 然后大家先把这个定义好然后我们这双方的再去做开发那么我们打开这个地址我们来看一下那么这个地址其实就是去描述了一些我们接口的信息比如说这个是我们的MOOC的一个地址那么当然了要注意这个是我们其实前面这个大家可以忽略它那么重点我们从这个URA开始看那么我们去开发的时候是开发这个URA后面的一些东西
[00:54] 然后呢他请求参数来看一下那么请求参数的类型呢是这个application json这种类型那么他请求的一个参数是一个份那就是有一个手机号那么响应呢是没有的响应是空的那这个是什么意思呢就是说如果我们的短信验证码发送成功的话那么我们需要响应给前端的是状态码呢是200那么如果不是如果不成功呢来看一下在这个位置
[01:24] 那么我们需要打开来看一下那么响应的状态码就要变成什么变成500并且我们要添加什么我们响应了一个错误的信息那么这个错误信息是我们需要自定义的所以说有两个字段一个是error code一叫做error message那么这个是就需要我们去把它去完成了好那么接下来我们就具体来编写服务
[01:51] 那么首先呢我们其实需要一个编写这个error result就刚刚我们所看到这个error code和这个error message那我们来编写一下那我们还是进入到我们这个进入到这个sso这个下面然后呢首先创建一个目录叫做vo那么vo呢就去放我们一些啊制定的一些对象那我们把这个呢就拷过来那么其中呢是有两个啊之段一个叫做error code一个叫做error message那么这个位置呢去
[02:20] 加了一个注解也是LumBook的注解叫build那么当然了我们还是需要给他加一个date这样的一个注解那么没有这个的话后面会有点问题那我们就把它加上来那么需要一个来call一下把它call过来那么是需要这样的一个注解的导入ok好那么到这里我们基本已经就实现了他的一个基础的一个需求就是有了一个响应这个error
[02:48] 那么如果正常的话是没有返回的直接响应200就可以了那么接下来我们这样我们先把下面的Service就是sm Service那么刚刚我们是不是在这个里面已经写了一个叫做send message就是send sm这个就发送短信的验证码那么下面我们需要去写一个
[03:13] 我们的去发送验证码之后呢去存储到我们这个readyist这样的一个逻辑啊那么我们就把这个代码直接拷贝过来吧因为这代码逻辑呢比较简单啊那我们给讲一下大家就明白了那我们把它丢到上面来吧丢到这里那么在这个位置呢需要用这个readyist template那我们就需要把这个readyist template直接注入进来就可以了那么呃在下面的这个位置啊
[03:41] 那么在之前我们是不是application中是不是已经编写了一些相关的配置那么可以打开来看一下那么之前在这个里面我们已经有了这样一个配置那么所以我们在这就可以直接去注入我们的一个redis template那么还有错误错误是一个日志我们来定一个日志把这个日志给拷过来那么拷过来之后我们来解读一下代码那么把相关的
[04:09] 包我们也拷贝进来我导入萨拉芬然后拿到它好那么下面我们来看一下在这个位置我们定义了一个叫做send check code就是验证码然后我们需要去传入一个手机号然后在这个位置我们首先去通过我们的redis我们去做一个获取
[04:36] 那么如果我们能够获取到我们之前的一个验证码就是说这个手机号是拼到这个位置来了对吧那么这个是我们保存的redis中的一个key那么如果在我们的就是这个手机号在我们redis中有数据的话那就代表什么呢代表你上一次所发送验证码的还未失效还处于有效状态那么继续可以使用所以我们直接就return它那么一个是code一个是messagecode是为1
[05:06] 那么如果没有Ribbon时钟没有的话那么我们就去调用我当前的这个发送短信验证码的这个逻辑去做一个发送把手机号呢传递给他那么发送完成之后呢我们做一个判断那么如果等于空那就代表什么呢这个位置发送失败了下面这个发送失败了那么发送失败呢那我们就去返回一个发送错误的就可以了
[05:33] 那么如果代码走到这的话那么就说明我们这个短信的验证码就已经发送成功了那么所以它的code是3那message是ok那么在发送成功之后那我们需要将我们的这个验证码去保存到ready是中那么两分钟后失效那我们要用这个逻辑去做一个set操作把这个验证码扣进去存进去
[06:00] 然后这个位置是不是有我们的一个redis中的一个key最后返回就可以了如果整个过程的出现异常的话那么就返回这个异常的这样的一个这样的一个code为是的这样的一个reduce那么到这里我们已经编写完成了这个Service中的逻辑那么接下来我们就来写一下在Controller中的逻辑那么我们在这个位置也需要去创建一个包叫做Controller
[06:33] 那么在Controller下面呢我们再来写一个类啊这叫什么呢sm啊Controller好然后呢我们给他去写一个叫做什么呢呃先写叫restcontroller啊是我们rest4的一个接口然后再写一个request mapping那么这个里面应该怎么写呢要注意了就要跟着我们这个接口文档来了来看一下那么接口文档呢是叫user这个login那么我们就写一个这个user吧
[07:02] 然后下面我们写一个login那么public返回值要注意那么由于我们要返回响应状态码所以我们在这个位置要返回的是叫做什么response responseEdit那么t我们给它返回是一个object那么我们这个就叫什么叫send 嘛send code然后我们在这去写一个什么post mapping
[07:35] 那么因为发起的是一个post请求可以看一下在这个位置post请求那么我们就写一个login这样的一个逻辑了那么在这个里面参数是什么参数它提交的是一个手机号要注意了那么参数的提交类型是一个json类型那么所以在这个位置我们需要去通过一个requestrequest body去做一个获取
[08:06] 那么就需要把我们的json去反序列化成什么我们就直接反序列化成一个map那么来一个object那么叫做paramok好这样就拿到了那么我们怎么样去拿到我们手机号就是通过param点什么get一个什么的份然后它要转成一个字幕创那我们就这么来转是20 value of
[08:35] 去转一下那么这个呢其实就拿到我们所需要的这个什么呢手机号那么拿到手机号之后呢我们需要调用我们这个Service去做一个发送那我们就去把我们这个sms这样的一个Service去注入进来那么把它注入进来那么注入进来之后呢我们就可以去干嘛呢是不是调用这个send messagesend这个check code去做一个发送了
[09:06] OK那么它的返回值注意了它的返回值是一个同样的也是一个这个map那么我们就需要去判断判断它这个里面的一些这个状态码点该是什么刚才我们讲到是不是有个叫code对吧可以来看一下它的返回值中是不是有个code和message对吧那么我们就拿到这个code那么code其实我们需要把它转成是一个int类型对吧
[09:34] 那我们就来转一下吧那么这么来转点value of去转一下那么我们还是需要这个是什么呢那就我们直接来强转吧那么它拿到是一个object那么就直接强转好了强转成什么呢强转成是一个我们的int类型对吧然后呢我们最后呢其实我们需要拿到它的一个int value最终的这个code的这个值那么我们就这么来吧
[10:08] int一个code等于它因为我们要做一些判断那么如果code等于3的话那么code等于3可以看到在刚刚逻辑中如果等于3的话是不是就是发送成功了那么就需要在我们这个位置去return一下return什么的response active点什么的点ok那么没有响应那就是什么那么这个就是叫什么发送发送成功发送成功
[10:37] 那么如果是发送不成功的话那么我们判断一下else if那么如果这个code等于几呢来看一下那么如果等于1的话那么就是上一次的这个还没有失效那么还是可用的那么我们就这么来玩吧那么等于1的话等于1的话那么其实等于1也属于什么呢发送失败那么只是说他
[11:07] 不用重新再发送了那么之前的那个还未失效啊还可以去使用但是它也属于发送失败但其他的也属于就是其他的情况呢也是属于发送失败的所以说呢最后啊最后我们应该这么玩就是最后我们一个return一个什么呢return一个我们response edit点什么呢stace定一个呃我们叫做http stace
[11:36] 然后点internet server error就是500然后点然后做一个body那么body用放什么就放我们刚刚的什么arrow result那么我们是不是可以写到这个位置来叫做arrow result那么我们定刚刚所定的这个arrow result那么由于我们给它加了一个build注解那么我可以直接通过build去做一个构建然后我们去给它设置什么比如说arrow code
[12:03] 那么我们可以来看一下在我们的这个MOOC中呢它其实是有这样的一个逻辑比如说这个有几个0呢这是6个0对吧然后呢还有一个叫做error message那么error message呢可以我们可以写一个短信发送失败那么这个相当于是我们有一个默认的一个这个error result对吧那么我们就这个我们还是
[12:33] 不能用它来接收那么我应该用一个build来做一个接收那么就是就叫这个buildOK好那么这个build那么通过这个build点build就可以得到我们这个对象了那么默认情况下面我们会给他发送的是这个短信发送失败那么如果等于1这个情况要注意了我们就不能这么去写了那我们应该这么来玩点这个edit code那我就不能叫6个0了我给他来一个比如说
[13:03] 5个0加一个1然后呢点来一个error一个message那么error message这个从哪来呢就需要通过我们刚刚的这个响应中的返回值中啊有一个message那我们就通过这个message来那么就通过一个什么呢叫send check code点get谁呢get message那么这个呢其实就拿到这个message那么然后我们看他所需要的是一个string类型
[13:34] 那就直接toStream直接toStream好那么就把它丢到这来那么我们应该是通过一个Stream这样定义好这样的话是不是就OK了那么也就是说如果说正常情况反回的是200那么如果是非正常情况那响应的是500但是后面这个内容需要有不同的情况默认走的是它那么如果是我们我们就是
[14:04] 还未生效还未失效的话那么走的是他这样的一个逻辑这个就是像什么呢叫上一次发送的验证码还未失效这样的一个逻辑好那么这个其实就是我们的什么逻辑这个叫做发送验证码这个接口OK好那么这个接口是不是我们就搞定了大家可能有时候在这个位置有点奇怪就是
[14:35] 我们这个名字为什么叫login呢其实我们在发验证吧并不是登录啊但是呢这个是前端呢就是这样去做个定义了那我们我们就跟着他这个定义来吧那么也不要去纠结这个名字了OK好那么到这里呢我们这个逻辑呢就算是编写完成了那么接下来呢我们就可以跑起来来测试一下啊那么我们呢就先来到这个里面啊找到我们的这个obligation然后呢我们去做一个run一个启动
[15:04] 好 那我们来等待它的一个执行

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目中实现短信验证码功能的完整代码流程，包括接口定义、服务层实现、控制器层编写和配置文件设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了项目中用于定义接口的文档，其中包含一个 mock 接口的地址：https://mock.boxugu.com/project/764/interface/api/11011。
画面 2: 展示了项目结构，重点在 `com.tanhua.sso.Service` 包下的 `TestSmsService.java` 文件，其中定义了一个 `ErrorResult` 类，用于封装错误信息。
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
画面 14: 展示了 `MyApplication.java` 文件的代码，其中使用了 `@MapperScan` 注解扫描 Mapper 接口，并使用 `@SpringBootApplication` 注解启动 Spring Boot 应用。

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
package com.tanhua.sso.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
public class SmsController {
}
```

画面 8:
```java
package com.tanhua.sso.Controller;
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
package com.tanhua.sso.Controller;
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

