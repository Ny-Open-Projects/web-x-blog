# 画面线理解：05_图片缓存_图片缓存逻辑编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day13-黑马头条-项目优化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day13-黑马头条-项目优化\05_图片缓存_图片缓存逻辑编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:13, 03:01, 03:44, 05:02, 05:58, 07:26, 08:27, 09:09, 09:49, 10:49, 12:08, 13:28, 14:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:48:37

1) 这一组画面整体在讲什么（一句话）：
实现一个用于缓存文章封面图片的服务，通过 FastDFS 下载图片并存入 Redis，同时支持清除缓存。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程大纲，当前在“1.3 Images缓存服务获取热点文章，处理图片”部分，介绍缓存服务需实现的功能：解析文章封面图片URL、获取图片并存入Redis，注意只缓存fastdfs中的图片。
画面2：展示项目结构，定位到 `com.heima.images.service.CacheImageService` 接口，准备实现该接口。
画面3：在IDE中右键点击接口，准备新建实现类。
画面4：展示 `CacheImageService` 接口定义，包含 `cache2Redis` 方法和 `resetCache` 方法。
画面5：展示 `CacheImageServiceImpl` 类的实现，开始编写 `cache2Redis` 方法。
画面6：在 `cache2Redis` 方法中，使用 `FastDfsClient` 下载图片，代码中包含 `fastDfsClient.downloadFile(group, file)`。
画面7：在 `cache2Redis` 方法中，对 URL 进行解析，使用 `String url = imgUrl.substring(0, imgUrl.indexOf("://"))`。
画面8：在 `cache2Redis` 方法中，对 URL 进行解析，使用 `String group = imgUrl.substring(index + 3, index + 3 + groupString.length())`。
画面9：在 `cache2Redis` 方法中，对 URL 进行解析，使用 `String group = imgUrl.substring(index + 3, index + 3 + groupString.length())`。
画面10：在 `cache2Redis` 方法中，使用 `StringRedisTemplate` 的 `resetCache` 方法清除缓存。
画面11：在 `CacheImageServiceImpl` 类中，定义 `StringRedisTemplate` 成员变量。
画面12：在 `CacheImageServiceImpl` 类中，定义 `FastDfsClient` 和 `StringRedisTemplate` 成员变量，并设置 `EXPIRE` 常量。
画面13：在 `cache2Redis` 方法中，设置 `EXPIRE` 常量值为 `60 * 60 * 24`。
画面14：在 `cache2Redis` 方法中，设置 `EXPIRE` 常量值为 `60 * 60 * 24`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public interface CacheImageService {
    // 缓存图片到Redis
    @Param imgUrl
    byte[] cache2Redis(String imgUrl, boolean isCache);

    // 清除图片缓存
    @Param imageKey
    void resetCache(Redis(String imageKey));
}
```

画面4：
```java
public interface CacheImageService {
    // 缓存图片到Redis
    @Param imgUrl
    byte[] cache2Redis(String imgUrl, boolean isCache);

    // 清除图片缓存
    @Param imageKey
    void resetCache(Redis(String imageKey));
}
```

画面5：
```java
import com.heima.images.service.CacheImageService;
import lombok.extern.log4j.Log4j2;
import org.springframework.stereotype.Service;

@Service
@Log4j2
public class CacheImageServiceImpl implements CacheImageService {
```

画面6：
```java
public class CacheImageServiceImpl implements CacheImageService {
    @Override
    public byte[] cache2Redis(String imgUrl, boolean isCache) {
        // 从fastdfs下载图片
        FastDfsClient fastDfsClient = new FastDfsClient();
        Map<String, String> map = formatPath(imgUrl);
        String group = map.get("group");
        String file = map.get("file");
        byte[] ret = fastDfsClient.downloadFile(group, file);
        return ret;
    }
```

画面7：
```java
private Map<String, String> formatPath(String imgUrl) {
    String url = imgUrl.substring(0, imgUrl.indexOf("://"));
    return new HashMap<>();
}
```

画面8：
```java
private Map<String, String> formatPath(String imgUrl) {
    String url = imgUrl.substring(0, imgUrl.indexOf("://"));
    String group = imgUrl.substring(index + 3, index + 3 + groupString.length());
    return new HashMap<>();
}
```

画面9：
```java
private Map<String, String> formatPath(String imgUrl) {
    String url = imgUrl.substring(0, imgUrl.indexOf("://"));
    String group = imgUrl.substring(index + 3, index + 3 + groupString.length());
    return new HashMap<>();
}
```

画面10：
```java
private StringRedisTemplate redisTemplate;

@Override
public void resetCache(String imageKey) {
    redisTemplate.opsForValue().set(imageKey, "");
}
```

画面11：
```java
private StringRedisTemplate redisTemplate;
```

画面12：
```java
public class CacheImageServiceImpl implements CacheImageService {
    @Autowired
    private FastDfsClient fastDfsClient;
    @Autowired
    private StringRedisTemplate redisTemplate;
    final long EXPIRE = 60 * 60 * 24;
```

画面13：
```java
public class CacheImageServiceImpl implements CacheImageService {
    @Autowired
    private FastDfsClient fastDfsClient;
    @Autowired
    private StringRedisTemplate redisTemplate;
    final long EXPIRE = 60 * 60 * 24;
```

画面14：
```java
public class CacheImageServiceImpl implements CacheImageService {
    @Autowired
    private FastDfsClient fastDfsClient;
    @Autowired
    private StringRedisTemplate redisTemplate;
    final long EXPIRE = 60 * 60 * 24;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
