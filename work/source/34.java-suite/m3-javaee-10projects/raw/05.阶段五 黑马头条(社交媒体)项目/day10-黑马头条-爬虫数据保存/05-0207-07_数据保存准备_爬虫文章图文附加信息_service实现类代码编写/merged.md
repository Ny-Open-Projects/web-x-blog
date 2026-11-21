# 07_数据保存准备_爬虫文章图文附加信息_service实现类代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\07_数据保存准备_爬虫文章图文附加信息_service实现类代码编写【海量资源尽在 666java.com】.mp4
- 时长 11分14秒（音频 674s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们下面就继续啊那这个方法咱们稍微改改啊这个呢不是自赃啊这个是获取什么呢获取增量的数据啊获取增量增量的统计数据啊一会咱们会去实现这个方法啊那下面咱们就来去先写什么呢先写咱们这个当前的实现类在当前的这个impl里面然后是写一个类impl然后呢是让它去实现刚才这个接口啊
[00:33] 好啊 到家回车包是扛着挨啊实现这些所有的方法然后在这去加一个Service然后是加一个log4j2啊再加一个super warning好吧直接加上啊super warning好然后呢你这个啊就反正咱们也需要去注入当前的mypro咱们直接去注入进去啊private然后是啊怎么叫什么呢叫new crnews是吧crnews additional mypro
[01:07] 然后咱们就叫他把它给注入进来OK没事了加完之后咱们下面就可以去解决方法第一个是保存保存的话其实就比较简单直接去保存就可以了点有一个insert但你也可以用下面这个你也可以用上面这个咱们用下面这个好吧是CLnews.additional完了这个东西就还是相对来说还是比较简单的然后咱们下面继续
[01:37] 下面继续让还有哪些呢还有当前这个东西就是查询应该是查询所需要的时间的某一个值是吧应该是列表啊那这个呢其实也比较简单啊好来看一下啊这家newsmyper.有一个叫什么来着有一个叫slack的listneed是不是update的这里边传的呢就是当前的时间
[02:04] 它返回的就是某一个列表你把这个列表返回就可以了好吧OK 返回这事就算是结束了然后接着我想看这里边还有一个curry list这个其实更简单是吧咱们直接去clnews.mypr.还有一个叫做slagged list这个传的就是clnews.audition完了ok下面还有一个叫jack
[02:34] 这个check跟上面那个其实差不多先说这个checkexit这个其实就是要根据当前的URL去查询就可以了这个咱们之前写过比如说咱们有一个叫做CLnewsadditional然后往里边去填写一个什么URL把当前的URL转进去
[03:03] 然后你就可以去调用Mapper去查询了del select list把当前的参数传进去然后最终它就能去找到一个列表这个列表的话咱们就去判断不等于当前的CL News这个东西然后并且非按的也不为空del is 什么点这时候你直接里程什么里程 true 就可以了
[03:33] 好吧忽然找不着就干嘛这就是一个是吧咱们下面呢那这个的话该怎么写呢咱们可以看一下啊这样咱们先不写这个啊先写这个好吧先写这个啊这个呢就是根据当前的URL去查询对吧来点过来啊这个其实咱们也可以去找到这啊咱们把这个代码给拷过来拷过来之后呢咱们再说
[04:04] 这是不是要查询一个URL查询一个对象是吧咱们直接不用远程出了啊还是用上面的代码啊因为它都是通过URL去查询嘛所以说呢这个代码是适用的啊但是这个东西啊你返回的时候就不能这么返回了你应该返回谁啊返回的是当前的什么get是吧拿到第一个就可以了好吧咱的话咱们就返回那OK然后下面这个啊紧接着咱们写这个那这东西呢其实就是什么
[04:34] 要用当前的这个单数或者这个方法就可以了这个方法啊然后是当然了咱们也可以去干嘛呢也可以在这啊可以在这先去判断一下比如说student utils.is not the url如果它不于空的话呢这个呢你就可以去调到当前的然后是url它返回的就是一个对象点万它返回的就是一个对象
[05:05] 然后咱们就可以去判断判断啥判断的方式就是说如果说不等于之前的谁之前的D深到UR就他这时候咱们就可以return什么return一个不然的话咱们就return一个force就可以了行这样方法咱们就算是写完了当然这里边还有没写完的还有这三个咱们一块再去写一下
[05:37] 那这个是更新是吧CL news my apple.applete-applete直接根据当前这个主件去更新就可以啊好来当然这个防止出问题咱们也可以用下边这个也可以用下边这个当然你可以选择啊下边这个也是啊下边这个的话就是根据条件这个每一个条件他都会有一个非空的判断啊会比较好一些好吧
[06:05] 下面咱们就来去重点去说一说下面这两个方法该怎么去写一个是to pass item另外一个是curate increment pass item先来看第一个那这个东西呢最终呢就是把你的这个对象集合转成这么个集合那你说该怎么去转呢其实呢你就要去拿东西了拿东西啊最终呢咱们要返回它咱们可以先去干嘛呢先去定义一个比如说咱们叫ars
[06:34] item list等于new一个re list然后呢下面呢咱们就可以去先去做循环啊说none不等于之前的additional list并且呢并且是这个咱们经常写啊然后是additional listr is empty它不会空那这时候呢你就可以去循环了啊循环的话就是tell for
[07:05] 那循环之后呢那这时候啊咱们就可以在这去创建一个passItem等于什么呢那也不能等于直接去new啊应该是构造当前的东西咱们可以写一个当前的那什么呢passItemOK啊这里边呢咱们要去传一个参数就可以了参数呢就是当前的CLnewsAdditional这方法不一样啊
[07:36] 这时候你就要去构建出来,比如说我们在这写一个public,返回的是passItem然后怎么叫,to,拷过来吧这个参数就是它这里边咱们主要是来去编写一些逻辑如果说它有了它有的话,这时候咱们可以判断如果说passItem等于
[08:17] 这时候就把当前对象去装到这个集合中就可以了.add好把这个task item装进去好这样就完事了你把这个集合返回就可以了重点咱们还是就这东西这个东西该怎么去写其实这个也是比较简单首先你要在这你要在这先去写一个东西比如说怎么样最终要去换成caller
[08:48] 有一个叫passItem最终咱们要去返回这个对象因为这个对象是一个子这里边其实是有一个URL的就咱们刚才说了最终咱们要去重新发请求都是往这个对象中去封装成一个URL往这个URL去组织所以说咱们在这先去构建一个它先它等于NUM下面咱们就可以去判断了
[09:17] 这判断的话呢就是为了那个防止出错啊说他不等于不等于那的时候ok这时候呢咱们就可以扭出来一个他嗯扭出来谁呀扭出来他等于扭一个他扭出来之后呢你往里边去设置就可以了下面这个啊然后.setur就设这个ur就可以了然后是clnews audition.getur
[09:50] 往这里边去转换了一个URL把这个对象给返回就可以了OK那这样我们就结束了当然这里边还有最后一个方法这个方法其实更好写一下其实更简单因为这个转换的方式咱们已经写完了因为它最终也是要去干嘛也是要去返回这种东西并且根据时间所以说您需要先去查询
[10:20] 这个插曲的话呢其实咱们上面已经写了看到了吗这啊这有一个叫做currylist by need update看到了吧所以说呢咱们在这啊直接调用就可以了啊curry我把当前那个current date传进去最终它返回的就是一个集合这个集合这块是不是一样的呀不是从这个集合中去换呗那转换的方式呢就比较简单了啊咱们呢就可以直接去调用
[10:52] 要传的是一盒啊ZL News好最终返回的就是一个US item然后你把这个US item好那目前的话呢这个啊目前这个所有的直线类啊里边的方法咱们都已经做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个新闻爬虫系统中“额外新闻”服务的 Java 代码实现，包括服务接口、实现类、数据映射器和对象转换逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 CrawlerNewsAdditionalService 接口定义，包含 updateAdditional、toParseItem、queryIncrementParseItem 等方法。
画面 2: 展示 CrawlerNewsAdditionalServiceImpl 类的实现，包含私有成员变量和方法声明。
画面 3: 展示 CrawlerNewsAdditionalServiceImpl 中的 queryListByNeedUpdate 方法，使用了 cNewsAdditionalMapper。
画面 4: 展示 CrawlerNewsAdditionalServiceImpl 中的 checkExist 方法，用于检查 URL 是否存在。
画面 5: 展示 CrawlerNewsAdditionalServiceImpl 中的 checkExist 方法，通过 cNewsAdditionalMapper 查询数据。
画面 6: 展示 CrawlerNewsAdditionalServiceImpl 中的 checkExist 方法，完成数据查询并判断是否为空。
画面 7: 展示 CrawlerNewsAdditionalServiceImpl 中的 getAdditionalByUrl 方法，用于根据 URL 获取新闻数据。
画面 8: 展示 CrawlerNewsAdditionalServiceImpl 中的 updateAdditional 方法和 toParseItem 方法。
画面 9: 展示 CrawlerNewsAdditionalServiceImpl 中的 toParseItem 方法，开始编写转换逻辑。
画面 10: 展示 CrawlerNewsAdditionalServiceImpl 中的 toParseItem 方法，调用 CrawlerParseItem 的构造函数。
画面 11: 展示 CrawlerNewsAdditionalServiceImpl 中的 toParseItem 方法，定义了 List<ParseItem> 的变量。
画面 12: 展示 CrawlerNewsAdditionalServiceImpl 中的 toParseItem 方法，使用 for 循环遍历 additionalList。
画面 13: 展示 CrawlerNewsAdditionalServiceImpl 中的 toParseItem 方法，调用 toParseItem 方法进行对象转换。
画面 14: 展示 CrawlerNewsAdditionalServiceImpl 中的 toParseItem 方法，完成转换并返回结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public boolean checkExist(String url);
// 更新
@Param
cNewsAdditional
// 转换数据为parseItem
@Param
additionalList
// Return
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList);
// 查询增量的统计数据
@Param
currentDate
// Return
```

画面 2:
```java
import java.util.Date;
import java.util.List;
@SuppressWarnings("all")
public class CrawlerNewsAdditionalServiceImpl implements CrawlerNewsAdditionalService {
    private N
    @Override
    public void saveAdditional(CNewsAdditional cNewsAdditional) {
        cNewsAdditionalMapper.insert(Select
    }
```

画面 3:
```java
@SuppressWarnings("all")
public class CrawlerNewsAdditionalServiceImpl implements CrawlerNewsAdditionalService {
    private CNewsAdditionalMapper cNewsAdditionalMapper;
    private CNewsAdditional cNewsAdditional;
    public void saveAdditional(CNewsAdditional cNewsAdditional) {
        cNewsAdditionalMapper.insert(Select
    }
    @Override
    public List<CNewsAdditional> queryList(CNewsAdditional cNewsAdditional) {
        return null;
    }
```

画面 4:
```java
@Override
public List<CNewsAdditional> queryListByNeedUpdate(Date currentDate) {
    List<CNewsAdditional> cNewsAdditionals = cNewsAdditionalMapper.selectListByNeedUpdate(currentDate);
    return cNewsAdditionals;
}
@Override
public List<CNewsAdditional> queryList(CNewsAdditional cNewsAdditional) {
    return cNewsAdditionalMapper.selectList(cNewsAdditional);
}
@Override
public boolean checkExist(String url) {
    CNewsAdditional cNewsAdditional = new CNewsAdditional();
    return false;
}
@Override
public CNewsAdditional getAdditionalByUrl(String url) {
```

画面 5:
```java
@Override
public List<CNewsAdditional> queryListByNeedUpdate(Date currentDate) {
    List<CNewsAdditional> cNewsAdditionals = cNewsAdditionalMapper.selectListByNeedUpdate(currentDate);
    return cNewsAdditionals;
}
@Override
public List<CNewsAdditional> queryList(CNewsAdditional cNewsAdditional) {
    return cNewsAdditionalMapper.selectList(cNewsAdditional);
}
@Override
public boolean checkExist(String url) {
    CNewsAdditional cNewsAdditional = new CNewsAdditional();
    cNewsAdditional.setUrl(url);
    List<CNewsAdditional> cNewsAdditionals = cNewsAdditionalMapper.selectList(cNewsAdditional);
    if (null != cNewsAdditionals && !cNewsAdditionals.isEmpty()) {
        return true;
    }
    return false;
}
@Override
public CNewsAdditional getAdditionalByUrl(String url) {
```

画面 6:
```java
@Override
public CNewsAdditional getAdditionalByUrl(String url) {
    if (StringUtils.isEmpty(url)) {
        return false;
    }
    return false;
}
@Override
public void updateAdditional(CNewsAdditional cNewsAdditional) {
```

画面 7:
```java
@Override
public void updateAdditional(CNewsAdditional cNewsAdditional) {
    cNewsAdditionalMapper.updateByPrimaryKeySelective(cNewsAdditional);
}
@Override
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList) {
    return null;
}
@Override
public List<ParseItem> queryIncrementParseItem(Date currentDate) {
    return null;
}
```

画面 8:
```java
@Override
public void updateAdditional(CNewsAdditional cNewsAdditional) {
    cNewsAdditionalMapper.updateByPrimaryKeySelective(cNewsAdditional);
}
@Override
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList) {
    return null;
}
@Override
public List<ParseItem> queryIncrementParseItem(Date currentDate) {
    return null;
}
```

画面 9:
```java
@Override
public void updateAdditional(CNewsAdditional cNewsAdditional) {
    cNewsAdditionalMapper.updateByPrimaryKeySelective(cNewsAdditional);
}
@Override
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList) {
    List<ParseItem> parseItemList = new ArrayList<>();
    if (null == additionalList || additionalList.isEmpty()) {
        return parseItemList;
    }
    for (CNewsAdditional cNewsAdditional : additionalList) {
        ParseItem parseItem = toParseItem(cNewsAdditional);
        if (parseItem != null) {
            parseItemList.add(parseItem);
        }
    }
    return parseItemList;
}
@Override
public List<ParseItem> queryIncrementParseItem(Date currentDate) {
    return null;
}
```

画面 10:
```java
@Override
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList) {
    List<ParseItem> parseItemList = new ArrayList<>();
    if (null == additionalList || additionalList.isEmpty()) {
        return parseItemList;
    }
    for (CNewsAdditional cNewsAdditional : additionalList) {
        ParseItem parseItem = toParseItem(cNewsAdditional);
        if (parseItem != null) {
            parseItemList.add(parseItem);
        }
    }
    return parseItemList;
}
@Override
public ParseItem toParseItem(CNewsAdditional cNewsAdditional) {
    if (cNewsAdditional == null) {
        return null;
    }
    CrawlerParseItem crawlerParseItem = new CrawlerParseItem();
    crawlerParseItem.setUrl(cNewsAdditional.getUrl());
    return crawlerParseItem;
}
@Override
public List<ParseItem> queryIncrementParseItem(Date currentDate) {
    return null;
}
```

画面 11:
```java
@Override
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList) {
    List<ParseItem> parseItemList = new ArrayList<>();
    if (null == additionalList || additionalList.isEmpty()) {
        return parseItemList;
    }
    for (CNewsAdditional cNewsAdditional : additionalList) {
        ParseItem parseItem = toParseItem(cNewsAdditional);
        if (parseItem != null) {
            parseItemList.add(parseItem);
        }
    }
    return parseItemList;
}
@Override
public ParseItem toParseItem(CNewsAdditional cNewsAdditional) {
    if (cNewsAdditional == null) {
        return null;
    }
    CrawlerParseItem crawlerParseItem = new CrawlerParseItem();
    crawlerParseItem.setUrl(cNewsAdditional.getUrl());
    return crawlerParseItem;
}
@Override
public List<ParseItem> queryIncrementParseItem(Date currentDate) {
    return null;
}
```

画面 12:
```java
@Override
public List<ParseItem> toParseItem(List<CNewsAdditional> additionalList) {
    List<ParseItem> parseItemList = new ArrayList<>();
    if (null == additionalList || additionalList.isEmpty()) {
        return parseItemList;
    }
    for (CNewsAdditional cNewsAdditional : additionalList) {
        ParseItem parseItem = toParseItem(cNewsAdditional);
        if (parseItem != null) {
            parseItemList.add(parseItem);
        }
    }
    return parseItemList;
}
@Override
public ParseItem toParseItem(CNewsAdditional cNewsAdditional) {
    if (cNewsAdditional == null) {
        return null;
    }
    CrawlerParseItem crawlerParseItem = new CrawlerParseItem();
    crawlerParseItem.setUrl(cNewsAdditional.getUrl());
    return crawlerParseItem;
}
@Override
public List<ParseItem> queryIncrementParseItem(Date currentDate) {
    return null;
}
```

画面 13:
```java
@Override

