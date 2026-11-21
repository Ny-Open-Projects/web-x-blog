# 10_自媒体文章自动审核_标题与内容匹配度计算

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\10_自媒体文章自动审核_标题与内容匹配度计算【海量资源尽在 666java.com】.mp4
- 时长 6分13秒（音频 373s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就接着往下写啊下面咱们要去说一下当前那个审核文章啊的标题与内容的匹配度那这个大家有没有什么思路呢咱们现在要做的一个事呢就是说当前标题啊跟你的内容必须要匹配要不然的话我不让你审核通过那这个咱们现在其实这个事你本身呢是一个不是绝对的事是吧但是咱们现在呢尽量的用代码去的形式啊用代码的形式去表现
[00:29] 现在我这边有个工具列我简单去说一下这个工具列这个工具列其实它可以去有一个方法是它是吧这个方法就主要是传两个字母串它就是来去比对比对什么呢第二个字母串在第一个字母串的一个占有率就是出现的几率有多少那这时候咱们就尽可能的是能够让它去比对当前字母串与字母串之间的这种出现的程度
[00:58] 好当然这个这种方式可能也不是最完善的但是在相对来说呢也是可行的也是可行的啊那行那在下面呢咱们就简单举个例子啊你看啊当前的话呢这是一个是一个字母范儿是吧比如说这是内容是吧下面是标题标题叫A毫无它两个应该是没有任何关系的你看当前这个content里边呢它也没有A的出现是吧没有A的出现啊这时候你可以去计算一下它会去返回一个
[01:27] double的话就是一个数值类型的应该算是百分比吧好咱们去执行一下啊执行完之后你会发现是0是吧就是完全不匹配那完全不匹配的话这时候呢咱们就让它审核不通过比如说我这里边假如说我这里边去加一个Vue因为这里边是Vue出现了两次啊我在这去加一个Vue那加两个吧好吧我们来看一下啊我再一个也行再一个啊
[01:59] 那就会去拿这个452中拿这个452去这个452中去找看有没有找着或者出现的频率有多少这时候你看是不是就不是0了咱们可以再多加几个比如说多加两个我们再去试一试那是0.05现在是不是0.1这个是不是往上涨了没问题啊那这个出现的几率因为增多了所以说它就会去这个数字就会往上增长那这时候咱们就宽泛一些
[02:29] 咱们再去用的时候啊这个工具力啊在用的工具力的时候咱们就这么定义如果说它不是零啊不是零就算是出现了那出现以后呢咱们就算是匹配上啊如果它是零的话呢那它就没有匹配上啊那它就没有匹配上啊咱们暂且先这么定义因为这些东西刚才说了就本身呢它不是一个非常准确的东西啊比如说你写了一篇文章这文章呢可能只有五个字单击的文章有一万字
[02:56] 但这个东西你不好匹配除非说你去阅读是吧用人工去阅读这个可能会更好一些但要用程序计算的话呢这东西呢没有绝对的正确好吧但是咱们尽量的去用程序去保证当前的这种正确的东西或者正确的标题跟正确的文章去匹配好吧那行那咱们下面呢就来去写一下咱们就可以去到一下当前的
[03:25] computer这个一个工具链啊首先呢咱们在这啊去加一个什么呢先去拿到当前contentcontent是谁呢wmnews.getcontent是吧然后是还有个啊叫stun的titlewmnews.gettitle好吧然后呢咱们就可以去调整前的方法了啊好当前的工具链computer下面是哪个方法呢是
[03:56] 传第一个啊就是content顺序不能出错啊第二个是title最终呢他就会返回来一个w比如说咱们叫啊叫这个东西啊然后呢咱们就去判断判断的话咱们暂且呢就先去认为刚才说了啊他如果说有写错了啊大于零啊大于零那这时候呢咱们就是审核通过审核通过啊
[04:32] 这样说吧叫文章标题与内容匹配导致通过匹配啊审核通过了好吧然后下面呢咱们还会再去说另外一个啊如果说匹配的话怎么着是吧这咱们可以直接小于零啊直接小于零好小于零的时候呢咱们需要做什么事呢它不匹配不匹配的话咱们要去通知用户或者修改用户的状态说你这个啊文章审核没有通过
[05:06] 那这时候咱们就可以去调用上前的update然后需要出来三个参数是吧wmnews刚才那边封装的啊好适合通过我说需要去通过通过是2是吧2啊好还有啥呢你说啊随时计划说你的文章标题与内容不比
[05:36] 不该是小于0,你还是等一等好,然后这是一个然后这时候咱们就可以直接累称了因为它审核没有通过就没有要再往下去审核了好,然后下面还有一个就是它如果说它不等于0的话咱们就直接往下走就可以了因为它没有小于0的时候咱们也可以这样写它是等于0或者小于等于0好吧小于等于0
[06:08] 小1.0的话他们都不行那这时候他大1.0他就审核通过去了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

