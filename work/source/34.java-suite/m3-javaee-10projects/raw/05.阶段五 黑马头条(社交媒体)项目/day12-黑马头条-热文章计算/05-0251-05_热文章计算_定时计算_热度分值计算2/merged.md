# 05_热文章计算_定时计算_热度分值计算2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\05_热文章计算_定时计算_热度分值计算2【海量资源尽在 666java.com】.mp4
- 时长 3分1秒（音频 181s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们继续啊这个取出一千条数据怎么去取出呢这样啊那首先呢先去排一个序比如这个是已经干嘛呢这个啊这个是已经设置获取到的热点的文章的数据对吧所以说咱们在这啊先去排下序打什么呢有一个salt里边呢咱们可以去拧一个comparecompare一次啊然后呢是怎么办呢这里边其实咱们之前是写过的对吧
[00:32] 这个要干嘛呢?
[00:35] 直接去判断啊O1.2有一个get然后呢是小于O2.2通过这个分值呢我们就看一下它在干嘛呢?
[00:51] 等于1吗?
[00:53] 要不然在干嘛呢?
[00:56] 等于等于负1直接去return就可以了把它给删掉
[01:05] 那这样的话咱们就能呢去获取一个顺序拿到一个顺序啊拿到完顺序之后呢下面呢咱们就可以去取值了那这取值刚才说了有可能是超过1000条的所以说咱们在这儿先去判断一下啊判断判断前的hotarticlelist.size不说是大于1000这时候咱们要去结怎么去结呢你直接可以return啊return什么呢hot
[01:38] article list.sublist我们可以从0到哪啊接到1000我们去1000条数据可以了好吧不然呢咱们就直接return什么呢我们先当前的outarticle list完事了那行这样的话咱们这个当前计算文章的分值啊就做完了啊咱们可以简单再去回顾一下看一下啊首先呢
[02:05] 这个计算分值的话呢你要通过当前你查出来的这个文章的信息先去计算分值啊这个计算分值的方式呢就是比较简单了啊干嘛呢你首先要初止化当前这个耗特的信息然后呢去最重要的是计算分值这个分值其实就是这些维度哪些维度呢前的喜欢是吧点然后是当前的这种叫收藏数是吧收藏数啊还有是评论数还有什么
[02:34] 还有一个阅读数最终这个分值就计算出来了然后这个分值比较高的咱们做了一个排序啊做了排序分值比较高的是放到前边然后呢再去把前一天天文章去拿出来那这个文章呢就是当前的热点文章数据好吧行那这个那这个计算啊咱们以后呢都是这么去计算好吧行那这个当前的计算文章的分值呢咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中编写和调试一个用于计算热门文章列表的 Java 服务类，核心逻辑包括初始化文章对象、计算综合评分、排序并截取前1000条数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `computeHotArticle` 方法的初始结构，包含初始化 `hotArticlesList` 和遍历 `aparticles` 的循环，准备计算每个文章的评分。
画面2：在循环中调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中，然后添加到 `hotArticlesList`。
画面3：在循环内部，为 `hot` 对象调用 `initHotBaseApArticle` 方法初始化基础属性。
画面4：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面5：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面6：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面7：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面8：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面9：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面10：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面11：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面12：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面13：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。
画面14：在循环内部，调用 `computeScore` 方法计算评分，并将结果设置到 `hot` 对象中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public List<ApHotArticles> computeHotArticle(List<ApArticle> aparticles) {
    List<ApHotArticles> hotArticlesList = new ArrayList<>();
    ApHotArticles hot = null;
    for (ApArticle aparticle : aparticles) {
        hot = initHotBaseApArticle(aparticle);
        Integer score = computeScore(aparticle);
        hot.setScore(score);
        hotArticlesList.add(hot);
    }
    //通过排序取出前1000条数据
    hotArticlesList.sort(new Comparator<ApHotArticles>() {
        @Override
        public int compare(ApHotArticles o1, ApHotArticles o2) {
            return o1.getScore() < o2.getScore() ? 1 : -1;
        }
    });
    if (hotArticlesList.size() > 1000) {
        return hotArticlesList.subList(0, 1000);
    }
    return hotArticlesList;
}
```

画面2：
```java
public List<ApHotArticles> computeHotArticle(List<ApArticle> aparticles) {
    List<ApHotArticles> hotArticlesList = new ArrayList<>();
    ApHotArticles hot = null;
    for (ApArticle aparticle : aparticles) {
        hot = initHotBaseApArticle(aparticle);
        Integer score = computeScore(aparticle);
        hot.setScore(score);
        hotArticlesList.add(hot);
    }
    //通过排序取出前1000条数据
    hotArticlesList.sort(new Comparator<ApHotArticles>() {
        @Override
        public int compare(ApHotArticles o1, ApHotArticles o2) {
            return o1.getScore() < o2.getScore() ? 1 : -1;
        }
    });
    if (hotArticlesList.size() > 1000) {
        return hotArticlesList.subList(0, 1000);
    }
    return hotArticlesList;
}
```

画面3：
```java
public List<ApHotArticles> computeHotArticle(List<ApArticle> aparticles) {
    List<ApHotArticles> hotArticlesList = new ArrayList<>();
    ApHotArticles hot = null;
    for (ApArticle aparticle : aparticles) {
        hot = initHotBaseApArticle(aparticle);
        Integer score = computeScore(aparticle);
        hot.setScore(score);
        hotArticlesList.add(hot);
    }
    //通过排序取出前1000条数据
    hotArticlesList.sort(new Comparator<ApHotArticles>() {
        @Override
        public int compare(ApHotArticles o1, ApHotArticles o2) {
            return o1.getScore() < o2.getScore() ? 1 : -1;
        }
    });
    if (hotArticlesList.size() > 1000) {
        return hotArticlesList.subList(0, 1000);
    }
    return hotArticlesList;
}
```

画面4：
```java
public List<ApHotArticles> computeHotArticle(List<ApArticle> aparticles) {
    List<ApHotArticles> hotArticlesList = new ArrayList<>();
    ApHotArticles hot = null;
    for (ApArticle aparticle : aparticles) {
        hot = initHotBaseApArticle(aparticle);
        Integer score = computeScore(aparticle);
        hot.setScore(score);
        hotArticlesList.add(hot);
    }
    //通过排序取出前1000条数据
    hotArticlesList.sort(new Comparator<ApHotArticles>() {
        @Override
        public int compare(ApHotArticles o1, ApHotArticles o2) {
            return o1.getScore() < o2.getScore() ? 1 : -1;
        }
    });
    if (hotArticlesList.size() > 1000) {
        return hotArticlesList.subList(0, 1000);
    }
    return hotArticlesList;
}
```

画面5：
```java
public List<ApHotArticles> computeHotArticle(List<ApArticle> aparticles) {
    List<ApHotArticles> hotArticlesList = new ArrayList<>();
    ApHotArticles hot = null;
    for (ApArticle aparticle : aparticles) {
        hot = initHotBaseApArticle(aparticle);
        Integer score = computeScore(aparticle);
        hot.setScore(score);
        hotArticlesList.add(hot);
    }
    //通过排序取出前1000条数据
    hotArticlesList.sort(new Comparator<ApHotArticles>() {
        @Override
        public int compare(ApHotArticles o1, ApHotArticles o2) {
            return o1.getScore() < o2.getScore() ? 1 : -1;
        }
    });
    if (hotArticlesList.size() > 1000) {
        return hotArticlesList.subList(0, 1000);
    }
    return hotArticlesList;
}
```

画面6：
```java
public List<ApHotArticles> computeHotArticle(List<ApArticle> aparticles) {
    List<ApHotArticles> hotArticlesList = new ArrayList<>();
    ApHotArticles hot = null;
    for (ApArticle aparticle : aparticles) {
        hot = initHotBaseApArticle(aparticle);
        Integer score = computeScore(aparticle);
        hot.setScore(score);
        hotArticlesList.add(hot);
    }
    //通过排序取出前1000条数据
    hotArticlesList.sort(new Comparator<ApHotArticles>() {
        @Override
        public int compare(ApHotArticles o1, ApHotArticles o2) {
            return o1.getScore() < o2.getScore() ? 1 : -1;
        }
    });
    if (hotArticlesList.size() > 1000) {
        return hotArticlesList.subList(0, 1000);
    }
    return hotArticlesList;
}
```

画面7：
```java
public List<ApHotArticles> computeHotArticle(List<ApArticle> aparticles) {
    List<ApHotArticles> hotArticlesList = new ArrayList<>();
    ApHotArticles hot = null;
    for (ApArticle aparticle : aparticles) {
        hot = initHotBaseApArticle(aparticle);
        Integer score = computeScore(aparticle);
        hot.setScore(score);
        hotArticlesList.add(hot);
    }
    //通过排序取出前1000条数据
    hotArticlesList.sort(new Comparator<ApHotArticles>() {
        @Override
        public int compare(ApHotArticles o1, ApHotArticles o2) {
            return o1.getScore() < o2.getScore() ? 1 : -1;
        }
    });
    if (hotArticlesList.size() > 1000) {
        return hotArticlesList.subList(0, 1000);
    }
    return hotArticlesList;
}
```

画面8：
```java
public List<ApHotArticles> computeHotArticle(List<ApArticle> aparticles) {
    List<ApHotArticles> hotArticlesList = new ArrayList<>();
    ApHotArticles hot =

