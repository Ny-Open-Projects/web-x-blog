# 画面线理解：10.商户注册-获取短信验证码-接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\10.商户注册-获取短信验证码-接口测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:12, 00:22, 01:07, 01:48, 02:22, 02:50, 03:08, 03:42, 04:01, 04:20, 04:40, 04:48, 04:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:54:13

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Postman 测试获取短信验证码的接口，并展示后端 Java 代码实现逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程文档，内容为“2.3.2.3 接口测试”，说明使用 Postman 测试获取验证码接口：http://localhost:57010/merchant/sms?phone=17717171717。
画面 2：IDE 中显示 MerchantController.java 代码，包含注释“发送手机验证码”和“Return 验证码对应的key”，以及方法 `public String sendMsg(String phone)`。
画面 3：Swagger UI 页面，显示“闪聚支付-商户应用API文档”，包含接口 /hello、/h1、/merchants/{id}、/sms。
画面 4：Postman 界面，显示“Create New”窗口，包含“Request”、“Collection”、“Environment”等选项。
画面 5：Postman 界面，鼠标悬停在“API Documentation”选项上。
画面 6：Swagger UI 页面，显示 GET /sms 接口，参数为 phone（手机号），并有“Execute”按钮。
画面 7：IDE 中显示 MerchantController.java 代码，包含注释“获取手机验证码”和“Return 验证码对应的key”，以及方法 `public String sendMsg(String phone)`。
画面 8：Postman 界面，显示 GET 请求，URL 为 http://localhost:57010/merchant/sms?phone=124432，Body 中包含 JSON 数据。
画面 9：Redis Desktop Manager 界面，显示连接到 localhost:6379，选中 redis-01，日志显示连接成功。
画面 10：课程文档页面，内容为“2.3.2.3 接口测试”，说明使用 Postman 测试获取验证码接口：http://localhost:57010/merchant/sms?phone=17717171717。
画面 11：IDE 中显示 MerchantController.java 代码，包含注释“获取手机验证码”和“Return 验证码对应的key”，以及方法 `public String sendMsg(String phone)`。
画面 12：IDE 中显示 SendService.java 代码，包含注释“发送验证码”，以及方法 `public String sendMsg(String phone)`。
画面 13：IDE 中显示 SendService.java 代码，包含注释“发送验证码”，以及方法 `public String sendMsg(String phone)`。
画面 14：课程文档页面，内容为“2.3.2.3 接口测试”，说明使用 Postman 测试获取验证码接口：http://localhost:57010/merchant/sms?phone=17717171717。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
/**
 * 发送手机验证码
 * @param phone 手机号
 * @return 验证码对应的key
 */
@Override
public String sendMsg(String phone) {
    // 同验证短信发送请求的地址
    String sms_url = url + "/generate?name=" + sms + "&effectiveTime=" + effectiveTime;
    ...
}
```

画面 7：
```java
/**
 * 获取手机验证码
 * @param id
 * @return
 */
@GetMapping("/sms")
public String getSmsCode(@RequestParam(value = "phone", required = true, dataType = "string") String phone) {
    return smsService.sendMsg(phone);
}

@GetMapping("/hello")
public String hello() {
    return "hello";
}
```

画面 12：
```java
/**
 * 发送验证码
 * @param phone 手机号
 * @return 验证码对应的key
 */
@Override
public String sendMsg(String phone) {
    // 同验证短信发送请求的地址
    String sms_url = url + "/generate?name=" + sms + "&effectiveTime=" + effectiveTime;
    ...
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
