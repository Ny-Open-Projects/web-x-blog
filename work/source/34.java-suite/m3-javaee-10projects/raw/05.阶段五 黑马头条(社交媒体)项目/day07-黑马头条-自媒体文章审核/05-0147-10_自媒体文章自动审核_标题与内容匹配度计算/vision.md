# 画面线理解：10_自媒体文章自动审核_标题与内容匹配度计算

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\10_自媒体文章自动审核_标题与内容匹配度计算【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:15, 03:19, 03:31, 03:40, 03:51, 03:58, 04:02, 04:13, 04:17, 05:08, 05:13, 05:44, 06:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:22:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中编写一个用于计算文章标题与内容相似度的工具类，并在业务逻辑中调用该工具类进行校验。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 2: 展示 Compute.java 文件中的 main 方法，用于演示相似度计算功能，其中定义了标题和内容字符串，并调用 SimilarDegree 方法计算相似度。
画面 3: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 4: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 5: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 6: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 7: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 8: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 9: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 10: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 11: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 12: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 13: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。
画面 14: 展示 ReviewMediaArticleServiceImpl.java 文件中审核文章的逻辑，其中包含对文章状态、发布时间、发布状态的判断，并调用 reviewSuccessSaveAll 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1:
```java
if (wNews.getStatus() == 0 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() > 0) {
    reviewSuccessSaveAll(wNews);
    return;
}
if (wNews.getStatus() == 1) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 阿里接口
    if (wNews.getPublishImg() != null) {
        if (wNews.getPublishImg().getTime() > new Date().getTime()) {
            //修改文章的状态为 8
            updateFollows(wNews, (short) 8, message: "待发布");
        } else {
            //立即发布
            reviewSuccessSaveAll(wNews);
        }
    } else {
        //立即发布
        reviewSuccessSaveAll(wNews);
    }
}
```

画面 2:
```java
package com.heima.utils.common;

import ...

public class Compute {
    public static void main(String[] args) {
        String content = "测试公司由于业务拓展，需要进行小程序相关的开发。本课程全线开发者努力，决定学习";
        String title = "测试";
        double ds = SimilarDegree(content, title);
        System.out.println(ds);
    }

    public static double SimilarDegree(String strA, String strB) {
        String newStrA = romaStr(strA);
        String newStrB = romaStr(strB);
        //用拉丁字母字符串长度作为分母，把字符串作为分子计算字母串相似度
        int temp = Math.max(newStrA.length(), newStrB.length());
        int temp1 = LongestCommonSubstring(newStrA, newStrB).length();
        return (double) temp1 / temp;
    }
}
```

画面 3:
```java
if (wNews.getStatus() == 0 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() > 0) {
    reviewSuccessSaveAll(wNews);
    return;
}
if (wNews.getStatus() == 1) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 阿里接口
    if (wNews.getPublishImg() != null) {
        if (wNews.getPublishImg().getTime() > new Date().getTime()) {
            //修改文章的状态为 8
            updateFollows(wNews, (short) 8, message: "待发布");
        } else {
            //立即发布
            reviewSuccessSaveAll(wNews);
        }
    } else {
        //立即发布
        reviewSuccessSaveAll(wNews);
    }
}
```

画面 4:
```java
if (wNews.getStatus() == 0 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() > 0) {
    reviewSuccessSaveAll(wNews);
    return;
}
if (wNews.getStatus() == 1) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 阿里接口
    if (wNews.getPublishImg() != null) {
        if (wNews.getPublishImg().getTime() > new Date().getTime()) {
            //修改文章的状态为 8
            updateFollows(wNews, (short) 8, message: "待发布");
        } else {
            //立即发布
            reviewSuccessSaveAll(wNews);
        }
    } else {
        //立即发布
        reviewSuccessSaveAll(wNews);
    }
}
```

画面 5:
```java
if (wNews.getStatus() == 0 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() > 0) {
    reviewSuccessSaveAll(wNews);
    return;
}
if (wNews.getStatus() == 1) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 阿里接口
    if (wNews.getPublishImg() != null) {
        if (wNews.getPublishImg().getTime() > new Date().getTime()) {
            //修改文章的状态为 8
            updateFollows(wNews, (short) 8, message: "待发布");
        } else {
            //立即发布
            reviewSuccessSaveAll(wNews);
        }
    } else {
        //立即发布
        reviewSuccessSaveAll(wNews);
    }
}
```

画面 6:
```java
if (wNews.getStatus() == 0 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() > 0) {
    reviewSuccessSaveAll(wNews);
    return;
}
if (wNews.getStatus() == 1) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 阿里接口
    if (wNews.getPublishImg() != null) {
        if (wNews.getPublishImg().getTime() > new Date().getTime()) {
            //修改文章的状态为 8
            updateFollows(wNews, (short) 8, message: "待发布");
        } else {
            //立即发布
            reviewSuccessSaveAll(wNews);
        }
    } else {
        //立即发布
        reviewSuccessSaveAll(wNews);
    }
}
```

画面 7:
```java
if (wNews.getStatus() == 0 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() > 0) {
    reviewSuccessSaveAll(wNews);
    return;
}
if (wNews.getStatus() == 1) {
    //审核文章的标题与内容的匹配度
    //审核文章内容 阿里接口
    if (wNews.getPublishImg() != null) {
        if (wNews.getPublishImg().getTime() > new Date().getTime()) {
            //修改文章的状态为 8
            updateFollows(wNews, (short) 8, message: "待发布");
        } else {
            //立即发布
            reviewSuccessSaveAll(wNews);
        }
    } else {
        //立即发布
        reviewSuccessSaveAll(wNews);
    }
}
```

画面 8:
```java
if (wNews.getStatus() == 0 && wNews.getPublishTime() != null && wNews.getPublishTime().getTime() > 0) {
    reviewSuccessSaveAll(wNews);
    return;
}
if (wNews.getStatus() == 1) {
    //审核文章的标题与内容的匹配
