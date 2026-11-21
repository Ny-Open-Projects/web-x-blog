# 画面线理解：18.功能开发之发送短信验证码

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\18.功能开发之发送短信验证码_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:34, 02:55, 04:19, 04:59, 05:54, 07:17, 07:54, 08:43, 10:15, 11:48, 12:50, 13:31, 14:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:09:19

1) 这一组画面整体在讲如何在云之讯平台创建应用、获取短信验证码接口，并在 Spring Boot 项目中编写代码调用该接口发送短信。

2) 按时间顺序列出每张画面的要点：
画面 1: 在云之讯开发者控制台的“应用管理”页面，查看已创建的应用“tanhua”和“hello-001”，并准备点击“申请上线”按钮。
画面 2: 点击“申请上线”后弹出“添加号码”窗口，要求输入“商户ID”、“用户验证码”、“图片验证码”和“输入验证码”。
画面 3: 页面跳转至短信模板查询页面，但内容为空。
画面 4: 查看云之讯开放平台的短信接口文档，显示了请求参数和 JSON 响应示例。
画面 5: 在 Typora 编辑器中打开项目文档，定位到“3.6.4. 编写代码”章节，准备编写配置类。
画面 6: 在 IntelliJ IDEA 中打开 `RestTemplateConfig.java` 文件，编写配置类 `RestTemplateConfig`，用于配置 `RestTemplate` 和 `ClientHttpRequestFactory`。
画面 7: 在 IntelliJ IDEA 中打开 `SmsService.java` 文件，查看类结构和成员变量。
画面 8: 在 `SmsService.java` 中，为 `@Service` 注解的类添加 `@Autowired` 注解，注入 `RestTemplate`。
画面 9: 在 `SmsService.java` 中编写 `sendSms` 方法，构造请求参数并使用 `restTemplate.postForEntity` 发送请求，解析响应体。
画面 10: 在云之讯开发者控制台的“短信”页面，弹出“验证手机”窗口，输入手机号、图片验证码和输入验证码。
画面 11: 查看云之讯开放平台的短信接口文档，显示了 JSON 响应示例。
画面 12: 在 IntelliJ IDEA 中创建新类 `TestSmsService.java`。
画面 13: 在 `TestSmsService.java` 中编写测试代码，调用 `smsService.sendSms` 方法。
画面 14: 在 Typora 编辑器中查看“3.6.6. mock接口”章节，显示了 mock 接口的地址和请求参数。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 5:
```markdown
3.6.4. 编写代码
配置RestTemplateConfig：
```

画面 6:
```java
package com.tanhua.sso.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.client.ClientHttpRequestFactory;
import org.springframework.http.client.SimpleClientHttpRequestFactory;
import org.springframework.http.converter.StringHttpMessageConverter;

@Configuration
public class RestTemplateConfig {

    @Bean
    public RestTemplate restTemplate(ClientHttpRequestFactory factory) {
        RestTemplate restTemplate = new RestTemplate(factory);
        restTemplate.getMessageConverters().set(1, new StringHttpMessageConverter(Charset.forName("UTF-8")));
        return restTemplate;
    }

    @Bean
    public ClientHttpRequestFactory simpleClientHttpRequestFactory() {
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setReadTimeout(5000); // 单位为ms
        factory.setConnectTimeout(5000); // 单位为ms
        return factory;
    }
}
```

画面 7:
```java
package com.tanhua.sso.service;

import org.springframework.stereotype.Service;

@Service
public class SmsService {
```

画面 8:
```java
@Service
public class SmsService {

    @Autowired
    private RestTemplate restTemplate;
```

画面 9:
```java
public String sendSms(String mobile) {
    String url = "https://open.ucpass.com/sms/sendsms";
    Map<String, Object> params = new HashMap<>();
    params.put("sid", "*******");
    params.put("token", "*******");
    params.put("appid", "*******");
    params.put("templateid", "*******");
    params.put("mobile", mobile);
    // 生成6位随机数
    params.put("param", RandomUtils.nextInt(100000, 999999));
    ResponseEntity<String> responseEntity = this.restTemplate.postForEntity(url, params, String.class);
    String body = responseEntity.getBody();
    try {
        JsonNode jsonNode = MAPPER.readTree(body);
```

画面 12:
```java
package com.tanhua.sso.service;

public class TestSmsService {
```

画面 13:
```java
public class TestSmsService {

    @Autowired
    private SmsService smsService;

    public void test() {
        String result = smsService.sendSms("158****7941");
        System.out.println(result);
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 5: 标题为“3.6.4. 编写代码”，内容包含“配置RestTemplateConfig”。
画面 14: 标题为“3.6.6. mock接口”，内容包含“地址：https://mock.boxuegu.com/project/164/interface/api/11011”，以及“请求参数”和“返回数据”表格。

5) 无。
