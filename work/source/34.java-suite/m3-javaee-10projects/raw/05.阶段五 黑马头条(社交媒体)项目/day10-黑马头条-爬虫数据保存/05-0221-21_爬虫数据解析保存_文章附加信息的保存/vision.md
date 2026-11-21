# 画面线理解：21_爬虫数据解析保存_文章附加信息的保存

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\21_爬虫数据解析保存_文章附加信息的保存【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 01:23, 02:25, 03:12, 03:54, 04:37, 05:07, 05:43, 07:14, 08:36, 09:48, 10:40, 11:52, 13:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:14:04

1) 这一组画面整体在讲什么（一句话）：
在 Java 项目中，实现一个新闻爬虫的解析管道，将爬取到的新闻数据（CrawlerParseItem）转换为业务实体（CNews），并设置额外属性如阅读数、点赞数、更新时间等，同时处理下一次更新时间的计算。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 CrawlerHttpParsePipeline.java 中，定义 addAdditionalData 方法，准备记录处理耗时。
画面 2: 在方法中，使用 System.currentTimeMillis() 获取当前时间戳，用于后续计算耗时。
画面 3: 在方法中，使用 Log.info 记录“文章附加数据处理完成，耗时：0”日志。
画面 4: 在方法中，使用 if 条件判断 parseItem 和 cNews 是否为 null，若不为 null，则调用 crawlerNewsAdditionalService 的方法。
画面 5: 在方法中，使用 if 条件判断 parseItem 是否为 null，若为 null 则创建新的 CNewsAdditional 对象。
画面 6: 在方法中，使用 CNewsAdditional 对象的 setNewsId、setReadCount、setLikes、setUrl 等方法设置新闻数据。
画面 7: 在方法中，使用 CNewsAdditional 对象的 setUpdatedTime 方法设置更新时间。
画面 8: 在方法中，使用 CNewsAdditional 对象的 setUpdateTime 方法设置下次更新时间。
画面 9: 在方法中，使用 getNewsId 方法获取新闻 ID。
画面 10: 在方法中，使用 getUpdateHour 方法获取下次更新时间。
画面 11: 在方法中，使用 crawler.nextupdatehours=4, 16, 64, 128, 256 设置下次更新时间。
画面 12: 在方法中，使用 getUpdateHour 方法获取下次更新时间。
画面 13: 在方法中，使用 getUpdateHour 方法获取下次更新时间。
画面 14: 在方法中，使用 CNewsAdditional 对象的 setUpdateTime 方法设置下次更新时间。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private void addAdditionalData(CrawlerParseItem parseItem, CNews cNews) {
    long currentTimeMillis = System.currentTimeMillis();
    // ...
}
```

画面 2:
```java
long currentTimeMillis = System.currentTimeMillis();
```

画面 3:
```java
Log.info("文章附加数据处理完成，耗时：0");
```

画面 4:
```java
if (parseItem != null && cNews != null) {
    cNews = crawlerNewsAdditionalService.toCNewsAdditional(parseItem, cNews);
}
```

画面 5:
```java
if (null != parseItem) {
    cNewsAdditional = new CNewsAdditional();
}
```

画面 6:
```java
cNewsAdditional.setNewsId(cNews.getTdId()); //文章id
cNewsAdditional.setReadCount(parseItem.getReadCount()); //阅读数
cNewsAdditional.setComment(parseItem.getCommentCount()); //回复数
cNewsAdditional.setLikes(parseItem.getLikes()); //点赞数
cNewsAdditional.setUrl(parseItem.getUrl());
```

画面 7:
```java
cNewsAdditional.setUpdatedTime(new Date()); //更新时间
```

画面 8:
```java
cNewsAdditional.setUpdateTime(new Date()); //下次更新时间
```

画面 9:
```java
private CNews toCNewsAdditional(CrawlerParseItem parseItem, CNews cNews) {
    if (null != parseItem) {
        cNewsAdditional = new CNewsAdditional();
        cNewsAdditional.setNewsId(cNews.getTdId()); //文章id
        cNewsAdditional.setReadCount(parseItem.getReadCount()); //阅读数
        cNewsAdditional.setComment(parseItem.getCommentCount()); //回复数
        cNewsAdditional.setLikes(parseItem.getLikes()); //点赞数
        cNewsAdditional.setUrl(parseItem.getUrl());
        cNewsAdditional.setUpdatedTime(new Date()); //更新时间
        cNewsAdditional.setUpdateTime(new Date()); //下次更新时间
        return cNewsAdditional;
    }
}
```

画面 10:
```java
private int getNextUpdateHour(Integer updateHour) {
    if (StringUtils.isBlank(updateHour)) {
        return 0;
    }
    return nextUpdateHour;
}
```

画面 11:
```properties
webdriver.chrome.driver=D:/develop/chromedriver_win32/chromedriver.exe
# linux
webdriver.chrome.driver=/usr/local/bin/chromedriver/chromedriver
proxy.get.url=http://www.89ip.cn/tqdl.html?api=1&num=500&port=Address&isp=
proxy.validate.url=http://mypi.kkha.com/
proxy.isUsedProxyIp=false
csdn.comment.url=http://blog.csdn.net/author/Phoenix/comment/list/{id}/page{&size=100}
crux.cookie.name=cs_v2
crawler.init.url.prefix=https://www.csdn.net/nav/
crawler.init.url.suffix=java
crawler.help.nextPagingSize=0
#爬虫页面面向百度系数
crawler.help.nextPagingSize=10
#设置下次更新时间
crawler.nextupdatehours=4, 16, 64, 128, 256
```

画面 12:
```java
private String nextUpdateHour;
private int getNextUpdateHour(Integer updateHour) {
    if (StringUtils.isBlank(updateHour)) {
        return 0;
    }
    return nextUpdateHour;
}
```

画面 13:
```java
private int getNextUpdateHour(Integer updateHour) {
    if (StringUtils.isBlank(updateHour)) {
        return 0;
    }
    return nextUpdateHour;
}
```

画面 14:
```java
cNewsAdditional.setUpdateTime(DateUtils.addHours(new Date(), nextUpdateHour));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
