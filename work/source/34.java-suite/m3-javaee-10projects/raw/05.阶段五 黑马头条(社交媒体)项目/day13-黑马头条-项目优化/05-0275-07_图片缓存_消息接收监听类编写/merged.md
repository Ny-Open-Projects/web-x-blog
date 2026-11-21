# 07_图片缓存_消息接收监听类编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\07_图片缓存_消息接收监听类编写【海量资源尽在 666java.com】.mp4
- 时长 4分27秒（音频 268s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那们下面就继续往下讲这里边咱们还有最后一块内容就是说怎么样创建消息监听类去监听消息这个监听的消息就是当前文章文章的微服务去发送的消息去处理图片的消息这时候咱们可以再去这儿去创建一个监听类创建一个包叫KafkaEner然后你在这去创建一个类
[00:35] 这里就叫做hot article listener让他去干嘛呢让他去一层实现实现一个叫做Kafkalistener这个是有一个字母片试试这个范型吧一个是他第二个是他Ctrl I有两个方法首先得让他让Spring去管理再去加一个log4.2好加上之后下面咱们就可以去注入一些东西
[01:06] 首先这个消息名称咱们要去注入谁啊就要去注入当前的一个叫做KafkaOPIC config好就他写错了啊就这么写吧写全点啊当的是AutoWire下面还有一个啊下面咱们要去转换成从JSON转换过来所以说咱们要去这里一个object-mypro这是mypro需要去注入
[01:36] 然后还有一个咱们需要去调用当前刚才写的这个Service所以说还要在这去去把当前的hot article servicehot article image Service就它把它也注入进来这时候咱们就可以去设置消息了首先消息的名称是.get一个hot article就是它然后下面咱们就可以去接收咱们的消息
[02:09] 我们先去打印个日志login货说是接收到hot热点文章吧热点文章热文章热文章消息为这个就是当前的date这个date没有是吧这样我们就把这个改了改成date这个就是好然后第二个咱们还要继续往上讲继续
[02:46] 你就可以去拿到当前的date点有一个叫做value这个value其实就是当前的一个真正的数据数据的话其实这个是个图串所以说你要干嘛呢你要用当前的myport点有一个叫read value然后这个就是value然后它要改成什么类型呢这有一个ap-hot-article-message
[03:16] 他转换过来的就是当前的一个message这个咱们需要去try cache一下那拿到之后呢这时候呢你就可以去调用当前的hot article image Service.把当前这个message装进去OK那这样的话就算是调用完成了在完成之后啊咱们在这可以再去打印个东西想log点error说干嘛呢接收消息
[03:54] 失败失败啊好当前的类呢咱们可以去设置一下当然你也可以把这消息给联系一下说咱们的这种错误消息是啥呢错误消息直接是个亿就可以了那行那这样的话咱们就算是设置完了啊做完之后呢咱们一会儿啊咱们就可以启动项目来去来去测试一下好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面10: 在 `HotArticleListener.java` 中，为 `Mapper` 字段选择 `ObjectMapper` 类型。
画面11: 在 `HotArticleListener.java` 中，为 `Mapper` 字段选择 `@JsonParser` 注解。
画面12: 在 `HotArticleListener.java` 中，使用 `Mapper.readValue` 方法将 JSON 字符串反序列化为 `ApiHotArticleMessage` 对象。
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
package com.heima.images.Kafka.listener;

import com.heima.common.Kafka.KafkaListener;
```

画面4:
```java
import lombok.extern.log4j.Log4j2;
import org.apache.Kafka.clients.consumer.Consumer;
import org.apache.Kafka.clients.consumer.ConsumerRecord;
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

