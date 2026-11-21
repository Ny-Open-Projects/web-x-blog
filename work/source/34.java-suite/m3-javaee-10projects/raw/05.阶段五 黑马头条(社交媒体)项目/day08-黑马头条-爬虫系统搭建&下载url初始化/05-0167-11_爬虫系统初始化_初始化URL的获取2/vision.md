# 画面线理解：11_爬虫系统初始化_初始化URL的获取2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\11_爬虫系统初始化_初始化URL的获取2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:01, 01:38, 02:31, 04:13, 05:21, 06:16, 07:07, 08:16, 09:17, 10:17, 11:17, 12:20, 13:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:35:36

1) 这一组画面整体在讲什么（一句话）：
演示如何在爬虫项目中，通过继承抽象类并重写方法，实现对初始URL列表的解析和转换为CrawlerParseItem对象。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示抽象类 AbstractOriginalDataProcess 的 handle 方法和 getComponentType 方法，用于定义数据处理流程。
画面2：展示实现类 CsdnOriginalDataProcess，开始编写 parseOriginalRequestData 方法，用于解析初始URL。
画面3：展示项目结构，聚焦在 ProcessFlow.java 文件，准备实现 getPriority 方法。
画面4：展示 ProcessFlow.java 文件，光标位于 getPriority 方法的末尾，准备编写方法体。
画面5：展示 AbstractOriginalDataProcess 类，正在选择父类 AbstractProcessFlow。
画面6：展示 CsdnOriginalDataProcess 类，正在选择父类 AbstractOriginalDataProcess。
画面7：展示 AbstractOriginalDataProcess 类，光标位于 getComponentType 方法的 return null 语句。
画面8：展示 CsdnOriginalDataProcess 类，光标位于 getPriority 方法的 return 0 语句。
画面9：展示 CsdnOriginalDataProcess 类，正在使用 Stream API 对 initCrawlerUrlList 进行处理。
画面10：展示 CsdnOriginalDataProcess 类，完成对 initCrawlerUrlList 的 Stream 处理，创建 ParseItem 对象。
画面11：展示 CsdnOriginalDataProcess 类，正在使用 Stream API 对 initCrawlerUrlList 进行处理。
画面12：展示 CrawlerEnum.java 文件，定义了 ReturnDataType 枚举，包含 HTML 和 JSON。
画面13：展示 CrawlerEnum.java 文件，定义了 DocumentType 枚举，包含 INIT、HELP、PAGE、OTHER。
画面14：展示 CsdnOriginalDataProcess 类，完成对 initCrawlerUrlList 的 Stream 处理，设置 DocumentType 和 setHandleTypes。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public abstract class AbstractOriginalDataProcess extends AbstractProcessFlow {
    @Override
    public void handle(ProcessFlowData processFlowData) {
    }

    @Override
    public CrawlerEnum.ComponentType getComponentType() {
        return null;
    }
}
```

画面2：
```java
@Component
public class CsdnOriginalDataProcess extends AbstractOriginalDataProcess {
    @Autowired
    private CrawlerConfig crawlerConfig;

    @Override
    public List<ParseItem> parseOriginalRequestData(ProcessFlowData processFlowData) {
        List<ParseItem> parseItemList = null;
        //从CrawlerConfigProperty 中获取初始URL列表
        List<String> initCrawlerUrlList = crawlerConfig.getInitCrawlerUrlList();
        if (null != initCrawlerUrlList && !initCrawlerUrlList.isEmpty()) {
            parseItemList = initCrawlerUrlList.stream().map(url -> {
                ParseItem parseItem = new CrawlerParseItem();
                parseItem.setUrl(url);
                return parseItem;
            }).collect(Collectors.toList());
        }
        return null;
    }
}
```

画面3：
```java
package com.heima.crawler.process.original;
public abstract class AbstractOriginalDataProcess extends AbstractProcessFlow {
    @Override
    public void handle(ProcessFlowData processFlowData) {
    }

    @Override
    public CrawlerEnum.ComponentType getComponentType() {
        return null;
    }

    @Override
    public int getPriority() {
        return 0;
    }
}
```

画面4：
```java
public int getPriority() {
    return 0;
}
```

画面5：
```java
package com.heima.crawler.process.original;
public class AbstractOriginalDataProcess extends AbstractProcessFlow {
```

画面6：
```java
package com.heima.crawler.process.original.impl;
public class CsdnOriginalDataProcess extends AbstractOriginalDataProcess {
```

画面7：
```java
package com.heima.crawler.process.original;
import com.heima.crawler.process.AbstractProcessFlow;
import com.heima.crawler.process.entity.ProcessFlowData;
import com.heima.model.crawler.enums.CrawlerEnum;

public abstract class AbstractOriginalDataProcess extends AbstractProcessFlow {
    @Override
    public void handle(ProcessFlowData processFlowData) {
    }

    @Override
    public CrawlerEnum.ComponentType getComponentType() {
        return null;
    }
}
```

画面8：
```java
@Component
public class CsdnOriginalDataProcess extends AbstractOriginalDataProcess {
    @Autowired
    private CrawlerConfig crawlerConfig;

    @Override
    public List<ParseItem> parseOriginalRequestData(ProcessFlowData processFlowData) {
        return null;
    }

    @Override
    public int getPriority() {
        return 0;
    }
}
```

画面9：
```java
import java.util.List;

@Component
public class CsdnOriginalDataProcess extends AbstractOriginalDataProcess {
    @Autowired
    private CrawlerConfig crawlerConfig;

    @Override
    public List<ParseItem> parseOriginalRequestData(ProcessFlowData processFlowData) {
        List<ParseItem> parseItemList = null;
        List<String> initCrawlerUrlList = crawlerConfig.getInitCrawlerUrlList();
        if (initCrawlerUrlList != null && !initCrawlerUrlList.isEmpty()) {
            initCrawlerUrlList.stream().map(url -> {
                ParseItem parseItem = new CrawlerParseItem();
                parseItem.setUrl(url);
                return parseItem;
            }).collect(Collectors.toList());
        }
        return null;
    }

    @Override
    public int getPriority() {
        return 0;
    }
}
```

画面10：
```java
import java.util.List;

@Component
public class CsdnOriginalDataProcess extends AbstractOriginalDataProcess {
    @Autowired
    private CrawlerConfig crawlerConfig;

    @Override
    public List<ParseItem> parseOriginalRequestData(ProcessFlowData processFlowData) {
        List<ParseItem> parseItemList = null;
        List<String> initCrawlerUrlList = crawlerConfig.getInitCrawlerUrlList();
        if (initCrawlerUrlList != null && !initCrawlerUrlList.isEmpty()) {
            parseItemList = initCrawlerUrlList.stream().map(url -> {
                ParseItem parseItem = new CrawlerParseItem();
                parseItem.setUrl(url);
                return parseItem;
            }).collect(Collectors.toList());
        }
        return null;
    }

    @Override
    public int getPriority() {
        return 0;
    }
}
```

画面11：
```java
import java.util.List;

@Component
public class CsdnOriginalDataProcess extends AbstractOriginalDataProcess {
    @Autowired
    private CrawlerConfig crawlerConfig;

    @Override
    public List<ParseItem> parseOriginalRequestData(ProcessFlowData processFlowData) {
        List<ParseItem> parseItemList = null;
        List<String> initCrawlerUrlList = crawlerConfig.getInitCrawlerUrlList();
        if (initCrawlerUrlList != null && !initCrawlerUrlList.isEmpty()) {
            parseItemList = initCrawlerUrlList.stream().map(url -> {
                ParseItem parseItem = new CrawlerParseItem();
                parseItem.setUrl(url);
                return parseItem;
            }).collect(Collectors.toList());
        }
        return null;
    }

    @Override
    public int getPriority() {
        return 0;
    }
}
```

画面12：
```java
public enum ReturnDataType {
    HTML, JSON
}
```

画面13：
```java
public enum DocumentType {
    INIT, HELP, PAGE, OTHER
}

public enum ComponentType {
    NORMAL, PAGEPROCESSOR, PIPELINE, DOWNLOAD
}
```

画面14：
```java
import java.util.List;

@Component
public class CsdnOriginalDataProcess extends AbstractOriginalDataProcess {
    @Autowired
    private CrawlerConfig crawlerConfig;

    @Override
    public List<ParseItem> parseOriginalRequestData(ProcessFlowData processFlowData) {
        List<ParseItem> parseItemList = null;
        List<String> initCrawlerUrlList = crawlerConfig.getInitCrawlerUrlList();
        if (initCrawlerUrlList != null && !initCrawlerUrlList.isEmpty()) {
            parseItemList = initCrawlerUrlList.stream().map(url -> {
                ParseItem parseItem = new CrawlerParseItem();
                parseItem.setUrl(url);
                parseItem.setDocumentType(CrawlerEnum.DocumentType.INIT);
                parseItem.setHandleTypes(processFlowData.getHandleTypes());
                return parseItem;
            }).collect(Collectors.toList());
        }
        return null;
    }

    @Override
    public int getPriority() {
        return 0;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
