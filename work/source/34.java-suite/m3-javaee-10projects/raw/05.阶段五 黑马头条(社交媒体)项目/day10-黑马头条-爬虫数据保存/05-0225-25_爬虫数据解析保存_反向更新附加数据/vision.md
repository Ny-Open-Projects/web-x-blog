# 画面线理解：25_爬虫数据解析保存_反向更新附加数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\25_爬虫数据解析保存_反向更新附加数据【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:42, 01:08, 01:25, 01:45, 02:13, 02:48, 03:09, 03:49, 04:07, 04:38, 05:07, 05:43, 06:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:16:53

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 代码中通过 `CrawlerNewsAdditionalService` 服务类，根据 `CrawlerParseItem` 对象中的数据，填充并更新 `CNewsAdditional` 实体对象，最终调用服务方法完成数据持久化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `CrawlerThreadPool` 的 `submit()` 方法，用于提交任务。代码中根据 `handleType` 判断是正向还是反向处理，并记录处理开始时间。
画面 2: 在 `updateAdditional` 方法中，通过 `crawlerNewsAdditionalService.getAdditionalByUrl(parseItem.getUrl())` 获取 `CNewsAdditional` 对象。弹出窗口显示该方法的参数和返回值类型。
画面 3: 在 `updateAdditional` 方法中，设置 `cNewsAdditional` 对象的 `newsId` 为 `null`，并记录日志“开始更新文章附加数据”。
画面 4: 在 `updateAdditional` 方法中，设置 `cNewsAdditional` 对象的 `newsId` 为 `null`，并记录日志“开始更新文章附加数据”。
画面 5: 在 `updateAdditional` 方法中，设置 `cNewsAdditional` 对象的 `newsId` 为 `null`，并记录日志“开始更新文章附加数据”。
画面 6: 切换到 `CNewsAdditionalMapper.xml` 文件，显示了 `getAdditionalByUrl` 方法的 SQL 映射配置。
画面 7: 在 `updateAdditional` 方法中，设置 `cNewsAdditional` 对象的 `readCount` 为 `parseItem.getReadCount()`。
画面 8: 在 `updateAdditional` 方法中，设置 `cNewsAdditional` 对象的 `likeCount` 为 `parseItem.getLikeCount()`。
画面 9: 在 `updateAdditional` 方法中，设置 `cNewsAdditional` 对象的 `commentCount` 为 `parseItem.getCommentCount()`。
画面 10: 在 `updateAdditional` 方法中，设置 `cNewsAdditional` 对象的 `nextUpdateHours` 为 `getNxtUpdateHours()` 方法的返回值。
画面 11: 在 `updateAdditional` 方法中，调用 `crawlerNewsAdditionalService.updateAdditional(cNewsAdditional)` 方法。
画面 12: 在 `updateAdditional` 方法中，调用 `crawlerNewsAdditionalService.updateAdditional(cNewsAdditional)` 方法。
画面 13: 在 `updateAdditional` 方法中，记录日志“更新文章附加数据完成，耗时：0”。
画面 14: 展示 `CrawlerHtmlParsePipeline` 类的 `handleHtml` 方法，用于处理 HTML 数据并提交任务。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
CrawlerThreadPool.submit(() -> {
    if (CrawlerEnum.HandleType.FORWARD.name().equals(parseItem.getHandleType())) {
        Log.info("开始处理消息, url: {}, handleType: {},", parseItem.getUrl(), parseItem.getHandleType());
        addParseItemMessage(parseItem);
    } else if (CrawlerEnum.HandleType.REVERSE.name().equals(parseItem.getHandleType())) {
        updateAdditional(parseItem);
    }
    Log.info("处理文章数据结束, url: {}, handleType: {}, 耗时: {}", parseItem.getUrl(), parseItem.getHandleType(), System.currentTimeMillis() - startTime);
});
```

画面 2:
```java
cNewsAdditional = crawlerNewsAdditionalService.getAdditionalByUrl(parseItem.getUrl());
```

画面 3:
```java
private void updateAdditional(CrawlerParseItem parseItem) {
    long currentTimeMillis = System.currentTimeMillis();
    Log.info("开始更新文章附加数据");
    if (null != parseItem) {
        cNewsAdditional = crawlerNewsAdditionalService.getAdditionalByUrl(parseItem.getUrl());
    }
}
```

画面 4:
```java
private void updateAdditional(CrawlerParseItem parseItem) {
    long currentTimeMillis = System.currentTimeMillis();
    Log.info("开始更新文章附加数据");
    if (null != parseItem) {
        cNewsAdditional = crawlerNewsAdditionalService.getAdditionalByUrl(parseItem.getUrl());
    }
}
```

画面 5:
```java
private void updateAdditional(CrawlerParseItem parseItem) {
    long currentTimeMillis = System.currentTimeMillis();
    Log.info("开始更新文章附加数据");
    if (null != parseItem) {
        cNewsAdditional = crawlerNewsAdditionalService.getAdditionalByUrl(parseItem.getUrl());
    }
}
```

画面 6:
```xml
<!-- CNewsAdditionalMapper.xml -->
```

画面 7:
```java
cNewsAdditional.setReadCount(parseItem.getReadCount());
```

画面 8:
```java
cNewsAdditional.setLikeCount(parseItem.getLikeCount());
```

画面 9:
```java
cNewsAdditional.setCommentCount(parseItem.getCommentCount());
```

画面 10:
```java
cNewsAdditional.setNextUpdateHours(getNxtUpdateHours() + DateUtils.addHours(parseItem.getUpdateTime()));
```

画面 11:
```java
crawlerNewsAdditionalService.updateAdditional(cNewsAdditional);
```

画面 12:
```java
crawlerNewsAdditionalService.updateAdditional(cNewsAdditional);
```

画面 13:
```java
Log.info("更新文章附加数据完成，耗时：{}", System.currentTimeMillis() - currentTimeMillis);
```

画面 14:
```java
import java.util.List;
import java.util.Map;

import static com.mongodb.Bytes.getType;

@Component
@Slf1j
public class CrawlerHtmlParsePipeline extends abstractHtmlParsePipeline(CrawlerParseItem) {

    /**
     * 快速处理入口
     * @param parseItem
     */
    @Override
    public void handleHtml(CrawlerParseItem parseItem) {
        long currentTimeMillis = System.currentTimeMillis();
        Log.info("数据加入线程池进行执行, url: {}, handleType: {},", parseItem.getUrl(), parseItem.getHandleType());
        CrawlerThreadPool.submit(() -> {
            if (CrawlerEnum.HandleType.FORWARD.name().equals(parseItem.getHandleType())) {
                Log.info("开始处理消息, url: {}, handleType: {},", parseItem.getUrl(), parseItem.getHandleType());
                addParseItemMessage(parseItem);
            } else if (CrawlerEnum.HandleType.REVERSE.name().equals(parseItem.getHandleType())) {
                updateAdditional(parseItem);
            }
            Log.info("处理文章数据结束, url: {}, handleType: {}, 耗时: {}", parseItem.getUrl(), parseItem.getHandleType(), System.currentTimeMillis() - currentTimeMillis);
        });
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
