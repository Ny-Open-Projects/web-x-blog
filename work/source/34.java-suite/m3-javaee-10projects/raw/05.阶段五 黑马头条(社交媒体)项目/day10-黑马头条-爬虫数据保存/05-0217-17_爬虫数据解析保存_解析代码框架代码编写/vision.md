# 画面线理解：17_爬虫数据解析保存_解析代码框架代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\17_爬虫数据解析保存_解析代码框架代码编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:53, 01:18, 03:08, 04:10, 04:39, 05:31, 05:59, 06:34, 07:33, 08:30, 09:43, 10:33, 11:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:10:55

1) 这一组画面整体在讲什么（一句话）：
讲解 CrawlerHtmlParsePipeline 类的实现细节，包括如何处理爬虫解析后的数据、设置优先级、前置参数处理以及根据 handleType 分发消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“3.8 CrawlerHtmlParsePipeline类”的标题和内容，说明该类用于解析后的数据存储，因数据量大，需控制并发线程数。
画面2：在IDE中展示 CrawlerHtmlParsePipeline 类的继承结构，它继承自 AbstractHtmlParsePipeline。
画面3：展示 CrawlerHtmlParsePipeline 类中的 getPriority() 方法，返回值为 1000。
画面4：在 preParameterHandle 方法中，使用 StringUtils.toString 获取 readCount 字段值。
画面5：在 preParameterHandle 方法中，对 readCount 字段值进行 split 处理。
画面6：在 preParameterHandle 方法中，将处理后的 readCount 值存入 itemAll。
画面7：展示一个流程图，内容为：是否匹配 -> 获取对象 -> 解析数据 -> 保存文章 -> 保存数据消息 -> 结束。
画面8：在 preParameterHandle 方法中，使用 log.info() 输出日志。
画面9：在 handleData 方法中，记录当前时间戳，并使用 CrawlerThreadPool.submit() 提交任务。
画面10：在 handleData 方法中，使用 CrawlerEnum.HandleType 判断 handleType。
画面11：在 handleData 方法中，根据 handleType 判断是否为 REVERSE 类型。
画面12：在 handleData 方法中，调用 addParseItemMessage 方法。
画面13：在 handleData 方法中，调用 additional 方法。
画面14：展示 updatedAdditional 方法和 addParseItemMessage 方法的定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.heima.crawler.process.parse.imp;
import com.heima.crawler.process.parse.AbstractHtmlParsePipeline;
public class CrawlerHtmlParsePipeline extends AbstractHtmlParsePipeline(CrawlerParseItem {
```

画面3：
```java
@Override
public int getPriority() {
    return 1000;
}
```

画面4：
```java
String readCount = StringUtils.toString(itemAll.get("readCount"));
```

画面5：
```java
readCount = readCount.split(regexp)[1];
```

画面6：
```java
itemAll.put("readCount", readCount);
```

画面8：
```java
log.info("开始处理消息，url: {}, handleType: {}", parseItem.getUri(), parseItem.getHandleType());
```

画面9：
```java
long currentMillis = System.currentTimeMillis();
log.info("数据加入线程池进行执行。url: {}, handleType: {}, parseItem.getUri(), parseItem.getHandleType());
CrawlerThreadPool.submit(() -> {
```

画面10：
```java
if (CrawlerEnum.HandleType.REVERSE.name().equals(parseItem.getHandleType())) {
```

画面11：
```java
} else if (CrawlerEnum.HandleType.REVERSE.name().equals(parseItem.getHandleType())) {
```

画面12：
```java
private void addParseItemMessage(CrawlerParseItem parseItem) {
```

画面13：
```java
additional(CrawlerParseItem parseItem) {
    addParseItemMessage(parseItem);
```

画面14：
```java
private void updatedAdditional(CrawlerParseItem parseItem) {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面7：流程图结构如下：
- 是否匹配 → 获取对象
- 获取对象 → 解析数据
- 解析数据 → 保存文章
- 保存文章 → 保存数据消息
- 保存数据消息 → 结束

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
