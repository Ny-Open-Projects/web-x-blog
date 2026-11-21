# 画面线理解：07_图片缓存_消息接收监听类编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\07_图片缓存_消息接收监听类编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:35, 00:51, 01:02, 01:28, 01:42, 01:56, 02:11, 02:36, 03:00, 03:08, 03:30, 03:42, 04:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:50:21

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现一个 Kafka 消费者监听器，用于处理热点文章图片的业务逻辑。

2) 按时间顺序列出每张画面的要点：
画面1: 在 `HotArticleImageServiceImpl.java` 中，展示 `CacheImageService` 字段的定义和 `handleHotImage` 方法的开头部分，用于处理热点文章图片。
画面2: 在 IDEA 中，通过“New”菜单创建一个新类，准备编写 Kafka 监听器。
画面3: 在 `HotArticleListener.java` 中，定义了类的包名和继承 `KafkaListener<String>`。
画面4: 在 `HotArticleListener.java` 中，导入 Kafka 相关的包，并选择 `Log4j2` 作为日志框架。
画面5: 在 `HotArticleListener.java` 中，为 `Log` 字段选择 `Log4j2` 的 `Logger` 类型。
画面6: 在 `HotArticleListener.java` 中，导入 `@Component` 和 `@Slf4j` 注解，并开始编写 `topic` 方法。
画面7: 在 `HotArticleListener.java` 中，添加 `@Slf4j` 注解并引入 `HotArticleImageService` 依赖。
画面8: 在 `HotArticleListener.java` 中，编写 `topic` 方法，返回 Kafka 主题名。
画面9: 在 `HotArticleListener.java` 中，编写 `onMessage` 方法，记录日志并接收消息。
画面10: 在 `HotArticleListener.java` 中，为 `mapper` 字段选择 `ObjectMapper` 类型。
画面11: 在 `HotArticleListener.java` 中，为 `mapper` 字段选择 `@JsonParser` 注解。
画面12: 在 `HotArticleListener.java` 中，使用 `mapper.readValue` 方法将 JSON 字符串反序列化为 `ApiHotArticleMessage` 对象。
画面13: 在 `HotArticleListener.java` 中，调用 `hotArticleImageService.handleImage` 方法处理图片。
画面14: 在 `HotArticleListener.java` 中，完成 `onMessage` 方法的编写，包含日志记录和异常处理。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```java
private ApiArticleContentMapper apArticleContentMapper;
private ApiArticleMapper apArticleMapper;
private CacheImageService cacheImageService;
@Override
public void handleHotImage(ApiHotArticleMessage message) {
    ApiHotArticles hotArticles = message.getHotArticles();
    Log.info("处理热文图片开始#ArticleId: {}, message: {}", hotArticles.getArticleId(), JSON.toJSONString(message));
    // 内容中的图片进行操作
    ApiArticleContent apArticleContent = apArticleContentMapper.selectByArticleId(hotArticles.getArticleId());
    if (null == apArticleContent) {
        String content = ZipUtils.unzip(apArticleContent.getContent());
        JSONArray array = JSON.parseArray(content);
        for (int i = 0; i < array.size(); i++) {
```

画面3:
```java
package com.heima.images.kafka.listener;

import com.heima.common.kafka.KafkaListener;
```

画面4:
```java
import lombok.extern.log4j.Log4j2;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;
import org.springframework.util.StringUtils;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;
import org.springframework.web.context.request.async.AsyncRequestTimeoutException;
import org.springframework.web.context.request.async.DeferredResult;
import org.springframework.web.context.request.async.WebAsyncManager;
import org.springframework.web.context.request.async.WebAsyncTask;
import org.springframework.web.context.request.async.WebAsyncTaskExecutor;
import org.springframework.web.context.request.async.WebAsyncTaskHandler;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptor;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChain;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context.request.async.WebAsyncTaskHandlerInterceptorChainAdapter;
import org.springframework.web.context
