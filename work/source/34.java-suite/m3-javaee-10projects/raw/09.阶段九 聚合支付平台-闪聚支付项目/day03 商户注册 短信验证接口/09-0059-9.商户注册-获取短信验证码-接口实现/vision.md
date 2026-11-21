# 画面线理解：9.商户注册-获取短信验证码-接口实现

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\9.商户注册-获取短信验证码-接口实现【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:37, 01:40, 02:17, 02:57, 03:37, 04:30, 05:01, 05:23, 06:27, 07:05, 07:54, 08:26, 08:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:53:45

1) 这一组画面整体在讲什么（一句话）：
演示如何在商户平台应用中通过 RestTemplate 调用短信服务接口获取验证码，并在服务层封装该逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Nacos 配置中心界面，要求编辑 merchant-application.yaml 配置文件，配置短信服务的 url 和 effectiveTime。
画面2：展示 IntelliJ IDEA 中的 RestTemplateTest.java 文件，演示如何使用 RestTemplate 发起 POST 请求获取验证码。
画面3：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面4：展示 Nacos 配置中心界面，配置文件中 url 字段被高亮显示，effectiveTime 为 600。
画面5：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面6：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面7：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面8：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面9：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面10：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面11：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面12：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面13：展示 SmsServiceImp.java 文件，正在编写获取验证码的业务逻辑，URL 中包含 effectiveTime 参数。
画面14：展示商户注册页面，用户填写手机号、账号、密码等信息，点击“注册”按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
在nacos上配置验证码的接口地址
1. 登录nacos，编辑merchant-application.yaml配置：
2. 配置如下参数
sms:
  url: "http://localhost:56085/sailing"
  effectiveTime: 600
```

画面2：
```
Map<String, Object> body = new HashMap<>();
body.put("mobile", "133456");
//请求头
HttpHeaders httpHeaders = new HttpHeaders();
//指定Content-Type: application/json
httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//请求体
HttpEntity<Map<String, Object>> httpEntity = new HttpEntity<>(body, httpHeaders);
//向后端请求
ResponseEntity<Map> exchange = restTemplate.exchange(url, HttpMethod.POST, httpEntity, Map.class);
log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
Map bodyMap = exchange.getBody();
System.out.println(bodyMap);
Map result = (Map) bodyMap.get("result");
Map bodyMap = exchange.getBody();
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
System.out.println(key);
return key;
```

画面3：
```
//向短信服务发送请求获取验证码
String url = "http://localhost:56085/sailing/generate?effectiveTime=600&name=sms";
```

画面4：
```
sms:
  url: "http://localhost:56085/sailing"
  effectiveTime: 600
```

画面5：
```
//向短信服务发送请求获取验证码
String url = "http://localhost:56085/sailing/generate?effectiveTime=600&name=sms";
```

画面6：
```
//向短信服务发送请求获取验证码
String url = "http://localhost:56085/sailing/generate?effectiveTime=600&name=sms";
```

画面7：
```
//请求体
HttpHeaders httpHeaders = new HttpHeaders();
//指定Content-Type: application/json
httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//请求体
HttpEntity<Map<String, Object>> httpEntity = new HttpEntity<>(body, httpHeaders);
//向后端请求
ResponseEntity<Map> exchange = restTemplate.exchange(sms_url, HttpMethod.POST, httpEntity, Map.class);
```

画面8：
```
import java.util.Map;
//Author Administrator
//@version 1.0
//服务
public class SmsServiceImpl implements SmsService{
    @Value("${sms.url}")
    String url;
    @Value("${sms.effectiveTime}")
    String effectiveTime;
}
```

画面9：
```
//向短信服务发送请求获取验证码
String sms_url = url + "/generate?name=sms&effectiveTime=" + effectiveTime;
```

画面10：
```
//请求体
HttpHeaders httpHeaders = new HttpHeaders();
//指定Content-Type: application/json
httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//请求体
HttpEntity<Map<String, Object>> httpEntity = new HttpEntity<>(body, httpHeaders);
//向后端请求
ResponseEntity<Map> exchange = restTemplate.exchange(sms_url, HttpMethod.POST, httpEntity, Map.class);
```

画面11：
```
//请求体
HttpHeaders httpHeaders = new HttpHeaders();
//指定Content-Type: application/json
httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//请求体
HttpEntity<Map<String, Object>> httpEntity = new HttpEntity<>(body, httpHeaders);
//向后端请求
ResponseEntity<Map> exchange = restTemplate.exchange(sms_url, HttpMethod.POST, httpEntity, Map.class);
```

画面12：
```
log.info("请求验证码服务，得到响应:{}", JSON.toJSONString(exchange));
Map bodyMap = exchange.getBody();
System.out.println(bodyMap);
Map result = (Map) bodyMap.get("result");
String key = (String) result.get("key");
System.out.println(key);
return key;
```

画面13：
```
//向短信服务发送请求获取验证码
String sms_url = url + "/generate?name=sms&effectiveTime=" + effectiveTime;
```

画面14：
无代码或配置内容。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：2.3.2.2 接口实现
子标题：1. 配置验证码服务的接口地址
内容：在nacos上配置验证码的接口地址
步骤：
1. 登录nacos，编辑merchant-application.yaml配置：
2. 配置如下参数

画面14：
标题：商户注册成功
内容：1、用户填写手机号、账号、密码等信息
表单字段：
- 账号
- 密码
- 手机号
- 验证码
按钮：
- 注册

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
