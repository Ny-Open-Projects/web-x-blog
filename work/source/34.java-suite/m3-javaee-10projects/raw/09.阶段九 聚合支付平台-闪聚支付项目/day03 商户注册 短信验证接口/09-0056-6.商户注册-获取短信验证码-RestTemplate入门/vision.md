# 画面线理解：6.商户注册-获取短信验证码-RestTemplate入门

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\6.商户注册-获取短信验证码-RestTemplate入门【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 04:45, 05:43, 06:46, 07:43, 09:07, 10:01, 11:22, 12:50, 13:42, 15:32, 16:45, 17:23, 18:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:51:59

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 RestTemplate 调用 HTTP 接口获取验证码，并解决因字符编码导致的中文乱码问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“2.3 获取短信验证码”，子标题“2.3.1 RestTemplate技术预研”，介绍 RestTemplate 是 Spring 提供的用于访问 RESTful 服务的客户端。
画面 2: PPT 页面，展示在 `shaniupay-merchant-application` 工程中引入 OkHttp 依赖的 XML 配置片段，其中 `<artifactId>` 标签内容被遮挡。
画面 3: PPT 页面，展示在父工程中规范 OkHttp 版本的 XML 配置片段，其中 `<version>` 标签内容被遮挡。
画面 4: IDE 界面，显示项目结构，选中 `MerchantApplicationBootstrap.java` 文件，右侧编辑器显示依赖配置，其中 `okhttp` 依赖的版本号被高亮。
画面 5: IDE 界面，显示 `MerchantApplicationBootstrap.java` 文件，代码中定义了 `RestTemplate` Bean。
画面 6: IDE 界面，显示 `MerchantApplicationBootstrap.java` 文件，代码中将 `RestTemplate` 的构造函数改为 `new OkHttp3ClientHttpRequestFactory()`。
画面 7: IDE 界面，显示 `RestTemplateTest.java` 文件，代码中使用 `@RunWith(SpringRunner.class)` 注解。
画面 8: IDE 界面，显示 `RestTemplateTest.java` 文件，代码中定义了 `@Test` 方法 `getHtml()`，并展示 `RestTemplate` 的 `exchange` 方法签名。
画面 9: IDE 界面，显示 `RestTemplateTest.java` 文件，代码中设置 URL 为 `http://www.baidu.com/`，并调用 `getForObject` 方法获取响应体。
画面 10: IDE 界面，显示 `RestTemplateTest.java` 文件，控制台输出了百度首页的 HTML 内容。
画面 11: IDE 界面，显示 `MerchantApplicationBootstrap.java` 文件，代码中获取 `RestTemplate` 的消息转换器列表。
画面 12: PPT 页面，标题为“解决：配置 StringHttpMessageConverter 消息转换器，使用 utf-8 字符集”，并展示修改 `RestTemplate` 定义方法的代码。
画面 13: IDE 界面，显示 `RestTemplateTest.java` 文件，代码中 `getHtml()` 方法的 URL 被注释掉。
画面 14: PPT 页面，展示 `RestTemplateTest.java` 文件中 `getHtml()` 方法的代码，以及测试结果说明“网页内容中文乱码解决方案”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
</dependency>
```

画面 3:
```xml
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
    <version>3.8.1</version>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
    <version>3.8.1</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>2.0.2.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter</artifactId>
    <version>2.0.2.RELEASE</version>
</dependency>
```

画面 5:
```java
@Bean
RestTemplate restTemplate() {
    return new RestTemplate();
}
```

画面 6:
```java
@Bean
RestTemplate restTemplate() {
    return new RestTemplate(new OkHttp3ClientHttpRequestFactory());
}
```

画面 7:
```java
package com.shaniupay.merchant;

import lombok.extern.slf4j.Slf4j;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@Slf4j
@RunWith(SpringRunner.class)
@SpringBootTest
public class RestTemplateTest {
}
```

画面 8:
```java
exchange(String url, HttpMethod method, HttpEntity<?> requestEntity, ParameterizedTypeReference<?> responseType)
```

画面 9:
```java
String url = "http://www.baidu.com/";
ResponseEntity<String> forEntity = restTemplate.getForObject(url, String.class);
String body = forEntity.getBody();
System.out.println(body);
```

画面 11:
```java
List<HttpMessageConverter<?>> messageConverters = restTemplate.getMessageConverters();
return restTemplate;
```

画面 12:
```java
@Bean
RestTemplate restTemplate() {
    RestTemplate restTemplate = new RestTemplate(new OkHttp3ClientHttpRequestFactory());
    //消息转换器列表
    List<HttpMessageConverter<?>> messageConverters = restTemplate.getMessageConverters();
    //配置消息转换器StringHttpMessageConverter，并设置utf-8
    messageConverters.set(1,
            new StringHttpMessageConverter(StandardCharsets.UTF_8));
    return restTemplate;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题“2.3 获取短信验证码”，子标题“2.3.1 RestTemplate技术预研”。
画面 2: 标题“1、认识RestTemplate”，内容介绍 RestTemplate 是 Spring 提供的用于访问 RESTful 服务的客户端。
画面 3: 标题“在父工程已规范了okhttp的版本”，内容展示 XML 配置。
画面 12: 标题“解决：配置 StringHttpMessageConverter 消息转换器，使用 utf-8 字符集”，内容展示修改 `RestTemplate` 定义方法的代码。
画面 14: 标题“通过测试发现可以成功获取百度的网页内容”，内容说明“网页内容中文乱码解决方案”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
