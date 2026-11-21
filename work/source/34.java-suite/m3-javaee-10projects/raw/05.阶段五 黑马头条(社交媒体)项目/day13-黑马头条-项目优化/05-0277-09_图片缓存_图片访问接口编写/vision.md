# 画面线理解：09_图片缓存_图片访问接口编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\09_图片缓存_图片访问接口编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:34, 03:05, 04:10, 05:09, 06:26, 07:55, 09:13, 10:25, 11:02, 12:07, 12:36, 13:15, 13:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:51:33

1) 这一组画面整体在讲什么（一句话）：
改造文章首页图片接口，实现通过 Redis 缓存和 Base64 编码处理图片请求。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示文章首页接口改造的上下文，代码中包含 `ImagesController` 和 `CacheImageService` 的部分实现，以及注释“2.文章首页接口改造”。
画面 2：展示 `ImagesControllerApi` 接口定义，包含 `@GetMapping`、`@RequestParam` 等注解。
画面 3：展示 `ImagesController` 类实现，继承 `ImagesControllerApi`，方法 `getImage` 初始为 `return null;`。
画面 4：在 `@GetMapping` 注解中设置 `value="/get"`，并提示 `produces` 默认值。
画面 5：在 `@GetMapping` 注解中设置 `produces=MediaType.IMAGE_JPEG_VALUE, method=RequestMethod.GET`。
画面 6：在 `getImage` 方法中，使用 `redisTemplate.opsForValue().get(path)` 获取缓存值。
画面 7：展示 `CacheImageService` 的类结构，包含 `cacheRedis` 方法。
画面 8：在 `getImage` 方法中，使用 `Base64` 解码并读取图片。
画面 9：在 `getImage` 方法中，添加日志和缓存判断逻辑。
画面 10：展示 `HotArticleServiceImpl` 中的 `handleImage` 方法，处理热文图片。
画面 11：展示 `getImage` 方法中 `redisTemplate.opsForValue().get(path)` 的调试信息。
画面 12：展示 `getImage` 方法中 `Base64` 解码和 `ImageIO.read` 读取图片的完整逻辑。
画面 13：展示 `getImage` 方法中 `@GetMapping` 注解的完整配置。
画面 14：展示 `getImage` 方法中 `redisTemplate.opsForValue().get(path)` 的调试信息和最终返回。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
package com.heima.article;
// ...
public class HotArticleServiceImpl extends AbstractHotArticleService {
    // ...
    @Override
    public void handleImage(ApHotArticleMessage message) {
        // ...
    }
}
```

画面 2：
```java
package com.heima.images.api;
public interface ImagesControllerApi {
    @GetMapping("/api/v1/images")
    public String getImage(@RequestParam("path") String path);
}
```

画面 3：
```java
package com.heima.images.controller;
import com.heima.images.api.ImagesControllerApi;
import lombok.extern.log4j.Log4j2;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@Controller
@RequestMapping("/api/v1/images")
public class ImagesController implements ImagesControllerApi {
    @Override
    public BufferedImage getImage(String u) {
        return null;
    }
}
```

画面 4：
```java
@GetMapping(value = "/get")
public BufferedImage getImage(String u) throws Exception {
    // ...
}
```

画面 5：
```java
@GetMapping(value = "/get", produces = MediaType.IMAGE_JPEG_VALUE, method = RequestMethod.GET)
public BufferedImage getImage(String u) throws Exception {
    // ...
}
```

画面 6：
```java
String baseCode = redisTemplate.opsForValue().get(path);
```

画面 7：
```java
CacheImageService cacheImageService;
```

画面 8：
```java
byte[] source = Base64Utils.decode(baseCode);
BufferedImage bufferedImage = ImageIO.read(new ByteArrayInputStream(source));
```

画面 9：
```java
String baseCode = redisTemplate.opsForValue().get(path);
if (StringUtils.isEmpty(baseCode)) {
    // 从缓存中获取数据
    byte[] bytes = cacheImageService.cacheRedis(path, isCache: false);
    BufferedImage bufferedImage = ImageIO.read(new ByteArrayInputStream(bytes));
    return bufferedImage;
}
```

画面 10：
```java
public void handleImage(ApHotArticleMessage message) {
    ApHotArticleMessage hotarticles = message.getData();
    log.info("处理热文图片开始articleId: {}, message: {}", hotarticles.getArticleId(), JSON.toJSONString(hotarticles));
    ApArticleContent aparticleContent = aparticleContentMapper.selectById(hotarticles.getArticleId());
    if (null != aparticleContent) {
        ApArticleContent content = zipUtil.unzip(aparticleContent.getContent());
        // ...
    }
}
```

画面 11：
```java
String baseCode = redisTemplate.opsForValue().get(path);
```

画面 12：
```java
byte[] source = Base64Utils.decode(baseCode);
BufferedImage bufferedImage = ImageIO.read(new ByteArrayInputStream(source));
log.info("图片访问请求结束path: {}", path);
return bufferedImage;
```

画面 13：
```java
@GetMapping(value = "/get", produces = MediaType.IMAGE_JPEG_VALUE, method = RequestMethod.GET)
public BufferedImage getImage(String u) throws Exception {
    String path = u;
    if (u.startsWith("http")) {
        path = InitConfig.PREFIX + u;
    }
    log.info("图片访问请求开始path: {}", path);
    String baseCode = redisTemplate.opsForValue().get(path);
    if (StringUtils.isEmpty(baseCode)) {
        // 从缓存中获取数据
        byte[] bytes = cacheImageService.cacheRedis(path, isCache: false);
        BufferedImage bufferedImage = ImageIO.read(new ByteArrayInputStream(bytes));
        return bufferedImage;
    }
}
```

画面 14：
```java
String baseCode = redisTemplate.opsForValue().get(path);
if (StringUtils.isEmpty(baseCode)) {
    byte[] bytes = cacheImageService.cacheRedis(path, isCache: false);
    BufferedImage bufferedImage = ImageIO.read(new ByteArrayInputStream(bytes));
    return bufferedImage;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
