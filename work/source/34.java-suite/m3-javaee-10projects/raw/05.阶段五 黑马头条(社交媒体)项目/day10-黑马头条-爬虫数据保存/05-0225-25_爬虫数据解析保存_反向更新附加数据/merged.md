# 25_爬虫数据解析保存_反向更新附加数据

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\25_爬虫数据解析保存_反向更新附加数据【海量资源尽在 666java.com】.mp4
- 时长 6分1秒（音频 362s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来完成逆向抓取这个啊就去更新当前的附加图文信息啊就是这个方法是吧也就是下边这个啊那咱们下面就就来去写下那这个呢其实最主要的就是来去更新当前的附加图文信息就可以了那咱们在这还是老套路啊直接去拿到一个时间先去记录下这个时间啊然后咱们在这去呃直接去点那个info然后是开始更新
[00:32] 当的什么附加数据好这是一个啊然后下面咱们就开始去判断啊判断的话呢其实还是从当前的因为咱们要去从passitem中去取数据所以说它不能为空啊然后呢咱们就可以去拿数据了这更新的话首先呢你得在咱们的数据库中得有值对吧得有值啊所以说呢咱们在这啊先去先去查callercaller
[01:02] newsadditionalservice.err有一个getadditionalURL咱们先去根据这个URL去查一次getURL查到一个对象之后这个对象叫clnewsadditional吧clnewsadditional这个对象是不能为空的你要有为空的话那就是新登了是吧等于当前的clnewsadditional
[01:34] 这时候咱们就可以去更新了更新之前我要去设置两个事第一个是set一个叫做news id你设立文档第二个呢dlnews.r有什么set一个叫做urur也设置文档那你说设置文档干嘛呀你看刚前这块咱们要去保存的时候其实稍等更新我到更新update这个
[02:06] 其实呢它是有条件的是有条件的如果说为None的话呢这个值就不复制了也就是说这块的目的呢其实设置为None就是在数据库中其实真正的不修改不修改其实呢咱们才设置为None因为设置为None的时候这个字段就不会再动了所以说在这需要去设置两个值这两个值你不能动一个是当前的文章ID一个是URL行那这是两个咱们继续往下看
[02:35] 除了这个设置完之后还要设置啥呢你看当前一个叫做set一个叫做read count这个呢就是一个什么现在阅读量是吧passatm.getread count好一个再往下看啊clnews而set一个叫做我们有一个lex command也行啊是评论量是吧我们叫passatm.get command好接着往下看clnews
[03:07] set一个叫做lex也是pass item.getlex接着往下走还有啥呢这里边其实咱们还要再去设立一个更新的时间跟下一次更新的时间这个还是按照之前的套路是一样的是一样的你怎么办呢下次更新的时间你可以这么搞咱们还是要去通过get nextupdate hour先去获取当前那个时间的间隔
[03:39] 然后是zeronews.getupdatetime根据这个时间去获取一个间隔一个间隔间隔之后呢这时候咱们就可以去往里面设置了.set一个叫做setnextupdate这时候呢你要去一个date.youtube.addhours第一个呢就是new一个
[04:07] 然后第二个呢就是你刚刚算出来这个值叫next update hours好吧这样的话就能计算出下一个更新的时间还有就是serial news没了啊这样的话咱们就设置完了是吧没有其他的值要更新了咱们最主要的是更新这些值就可以了啊嗯行那这个设置完之后啊设置完之后啊这里边好像还少一个是吗这个那不用啊没事了咱们现在就可以直接保存了是吧
[04:37] 有一个叫做save不是save叫update点update然后怎么办呢然后就是把当前那个放进去这样就可以了总感觉少一个是吧咱们在这还得去加一个因为这个更新的次数咱们好像没有设是吧比如说你在这去设立一个update num这个就是谁呀就是当前的值加1就可以
[05:11] 这样的话我们算是真正的去设完了啊那设完之后啊咱们在下面就可以去再去记录一个日志log.info然后这怎么写啊说更新更新文章的附加数据完成然后是耗时耗时多长时间呢计算一下啊system.他减去他那行那这个咱们这个
[05:42] 代码就算是写完了其实这个里边当前这个列啊写了很多是吧咱们大概写了有四五百行代码啊四百行代码啊三百行不到四百行那这个内容还是挺多的大家大家呢去写的时候呢一定要履行思路然后下面呢咱们就来去测一下好吧就来去测一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

