# 画面线理解：09_自媒体文章自动审核_审核主逻辑编写2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\09_自媒体文章自动审核_审核主逻辑编写2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:15, 00:39, 00:53, 01:10, 01:18, 02:04, 02:20, 03:01, 03:17, 04:13, 04:22, 04:35, 04:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:21:21

1) 这一组画面整体在讲什么（一句话）：
在 Java 项目中，通过修改 `ReviewMediaArticleServiceImpl` 类中的代码，实现对文章状态的更新逻辑，包括判断文章发布时间并更新状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `ReviewMediaArticleServiceImpl.java` 文件中，对 `wNews` 对象的 `publishTime` 进行判断的 if 语句块，其中注释说明“审核通过后待发布文章，判断发布时间”。
画面 2: 鼠标选中 `if (wNews.getStatus() == 0)` 条件语句，准备进行修改。
画面 3: 鼠标光标位于 `if (wNews.getStatus() == 0)` 语句中，准备进行编辑。
画面 4: 鼠标选中 `reviewSuccessSaveAll(wNews)` 方法，准备进行修改或查看其定义。
画面 5: 鼠标光标位于 `if (wNews.getPubl...` 语句中，准备进行编辑。
画面 6: 鼠标光标位于 `if (wNews.getPubl...` 语句中，准备进行编辑。
画面 7: 鼠标光标位于 `updateWNews(wNews)` 方法调用处，准备进行编辑。
画面 8: 展示 `WnNews.java` 文件，定义了 `wNews` 实体类的属性，包括 `id`, `userId`, `title`, `type`, `channelId`, `labels`, `createdTime`, `submittedTime`, `status`, `publishTime`, `reason` 等。
画面 9: 展示 `ReviewMediaArticleServiceImpl.java` 文件中，对 `wNews` 对象的 `status` 进行设置的代码块，注释说明“修改 wNews 的状态为 8”。
画面 10: 鼠标光标位于 `reviewSuccessSaveAll(wNews)` 方法调用处，准备进行编辑。
画面 11: 展示 `WnNews.java` 文件，定义了 `wNews` 实体类的属性。
画面 12: 展示 `ReviewMediaArticleServiceImpl.java` 文件中，对 `wNews` 对象的 `status` 进行设置的代码块。
画面 13: 鼠标光标位于 `wNews.setStatus(status)` 方法调用处，准备进行编辑。
画面 14: 鼠标光标位于 `wNewsMapper.updateByPrimaryKeySelective(wNews)` 方法调用处，准备进行编辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
//审核通过后待发布文章，判断发布时间
if (wNews.getStatus() == 8 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() != 0) {
    reviewSuccessSaveAll(wNews);
    return;
}
//审核文章
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 2:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 3:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 4:
```java
//审核通过后待发布文章，判断发布时间
if (wNews.getStatus() == 8 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() != 0) {
    reviewSuccessSaveAll(wNews);
    return;
}
```

画面 5:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 6:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 7:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 8:
```java
package com.heima.model.media.po;

import java.util.Date;

public class WnNews {
    private Integer id;
    @Encrypt
    protected Long userId;
    private String title;
    private Short type;
    @Encrypt
    private Integer channelId;
    private String labels;
    private Date createdTime;
    private Date submittedTime;
    private Short status;
    private Date publishTime;
    private String reason;
    @Encrypt
}
```

画面 9:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 10:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 11:
```java
package com.heima.model.media.po;

import java.util.Date;

public class WnNews {
    private Integer id;
    @Encrypt
    protected Long userId;
    private String title;
    private Short type;
    @Encrypt
    private Integer channelId;
    private String labels;
    private Date createdTime;
    private Date submittedTime;
    private Short status;
    private Date publishTime;
    private String reason;
    @Encrypt
}
```

画面 12:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 13:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

画面 14:
```java
if (wNews.getStatus() == 0) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 内容接口
    //审核文章中的图片信息，阿里接口
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
