# 21_爬虫数据解析保存_文章附加信息的保存

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\21_爬虫数据解析保存_文章附加信息的保存【海量资源尽在 666java.com】.mp4
- 时长 13分18秒（音频 799s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去完成当前这个附加信息的保存操作首先你还是得再去刷这个顺序你必须得先去保存当前的文章然后才能去保存当前的一个附加信息因为保存附加信息的时候咱们需要用到文章的信息好吧然后这时候咱们还是主要主要就是保存这时候咱们就可以先去记录还是老套路system点什么
[00:28] 然后是拿到一个时间然后下面呢咱们就可以记录日志log.info说啥呢说开始文章这样处理处理文章附加信息数据好吧然后下面呢咱们就可以真正的去保存了保存之前呢还是得去做判断说none不等于谁呀不等于当前那个past定写的是none
[01:00] 不等于谁不等于当前那个CL News这两个都不能等于NOW然后这时候呢咱们还能去保存那保存在这里边啊咱们还是去从这个里边跟这个里边呢去追加一些数据也就是说把这些数据是挪到了当前的什么CL News Audition里边啊这时候呢咱们还是再去封装一个方法好吧CL NewsCL News AuditionTL好吧
[01:30] 然后这个参数就是当前的第一个passItem第二个就是saleNews它返回的就是一个返回的就是saleNewssaleNews然后additional好就是它然后咱们下面就可以去保存了保存的color这个好些有是吧saleNewsadditionalService.2我们有一个saveAdditional
[02:02] 然后你把当前那个CL News Audition放进去这样的话就算是保存成功了啊那最后呢你在这去打印一个东西就可以了loginfo这里边写是文章附加数据处理完成然后耗时耗时多长时间呢咱们在这去写一下system然后是.2它-好那这个就算是处理完了啊
[02:32] 注意完之后,这个东西咱们没有,咱们就创建出来来咱们继续,这是什么呢转换数据,是吧转换数据最终的是additional然后这里边咱们主要是从这个跟这个方式往这边去转,是吧好,那咱们首先在这儿先去创建一个CL News Edition好,等于什么呢,等于是那,好吧,先等于那然后下面咱们就来去判断呗
[03:04] 其实判断都行,你判断一下也行,如果是Atom它不等于None的话,下面我们就可以去用它去Nu一个,Nu一个当前的CL News Additional,好,下面你就可以去设置了,比如说咱们要去设置一个这种文章ID,比如说CL News Additional.set有一个叫做News ID,那这个是谁?
[03:31] 这就是cellnews中的setid是吧这是文章id啊文章id好然后接着往下看cellnewsadditional.set什么呢set一个阅读数阅读数read.setreadcount然后这个呢是从plus term中.set有一个叫做readcount然后接着往下看啊这个出示加上也行是吧
[04:03] 阅读好接着往下看CLnewsAdditional点咱们有一个set有一个command这个呢其实是一个回复数是吧这里边有啊item点有一个叫做command count这样啊这个它好像是也没有问题是吧这是什么这是回复数然后是CLnews
[04:37] additional.set下面设置一个点赞数吧这个也是passitem.getlikes接着我要看CLnewsCLnewsadditional.r里面有一个setur然后是passitem.getur好,这是完了这个就是什么呢这是点赞是吧
[05:10] 一圆了就没了一个写的了UR然后再往下CLnewsAdditional.有一个setupdatetime这个呢其实你就直接去new一个date就可以了好吧new一个date然后下面还有CLnewsAdditional.set什么有一个叫做createTime是吧createTime
[05:43] 这个是有一个new一个也是new一个data就可以啊下面就是有一个更新的次数怎么要去设置啊更新的次数clnewsadditional.set有一个叫做update num这个默认给个0diss给0就可以了因为现在啊你是新增数据新增数据之前呢咱们先给一个00就是diss下面咱还有一个东西就是设置什么呢
[06:14] 在这上面写下设置设置下次通信时间那这个时间该怎么去弄呢那这个时间呢其实呢咱们在当前的这个地儿啊你可以打开这打开当前的这个配置文件里边呢其实在这去设了一个啊比如说你当年时间是现在
[06:40] 咱们4小时后再更新还有16小时后再更新还有64小时128小时后还有256小时之后咱们都要去更新这个文章这个呢只是为了什么为了你逆向查询逆向然后同时呢再去更新当前的这个数据就可以了好吧那这个时间该怎么去算呢首先呢你要获取到啊获取到当前这种下次更新的时间间隔时间啊
[07:09] 那这样啊咱们可以去拿到一个叫get我们可以说明个方法叫get next update然后是hoursous这里边传的参数呢就是刚刚咱们设置这个东西叫clnewsadditional.getupdate time根据这个时间呢咱们再去计算
[07:37] 反回的就是一个时间的间隔int我可以设置一个next nextupdatehour然后这个设置完之后这个方法没有是吧没有什么一会再去创建然后下面咱们就可以去设置什么呢设置下次更新时间不用这么写设置下次
[08:16] 更新时间然后呢然后咱们接着往下看啊下面的话呢我们就可以去设置了啊CL News, Audition, PR咱们有一个set next有一个叫做Num需要更新的time啊update time这个呢这个是怎么办呢
[08:42] 这个呢其实呢咱们就可以呢通过当前的一个时间当前的时间啊去计算出多少时间计算出多少个小时就可以了啊那这个咱们可以用一个DataUtilDataUtilC-R里面有一个AddAll一个呢就是当前的当前的时间然后第二个呢第二个参数啊第二个参数就是你的NextUpdateAll这样的话它能
[09:10] 就能用当前时间去计算啊到底是下一个是什么时间下一个更新的点是什么时间好吧嗯行那拿到这个之后啊那这个东西呢怎么还是要再去考验一下啊这是计算时间这是计算什么计算更新次数啊当然这个咱们直接去return就可以了return什么呢return当前的CL News Additional这样就可以了啊那下面咱们就来去写一下当前的这个东西
[09:43] 刚才说了,这个其实你需要去读取谁?
[09:47] 读取当前的这个值那这个值怎么读?
[09:51] 这个值的话其实咱们也好读,是吧?
[09:55] 咱们在这儿,定一个属性private 它是一个string,比如说就是个 stringstring 也不行,咱们用一个 integer 也行它是个数组
[10:14] 它是个数组是吧它是个数组的话那这样咱们先去把它给注入进来肯定先是一个字幕串是吧一会咱们再去再去拼接再去截取就可以了这个就叫它也行是吧咱们把这个up大写然后咱们就可以去注入了用哪个Y6是吧然后是里边写一个标签符大括号
[10:45] 多少伙大括号把它给拼进去好像不对因为你需要把前面的东西也给拿过来这样的话咱们就算是注进来了注进来之后下面该怎么去用的这样咱们先得去干嘛先得去判断一下应该这样说先得去判断一下它有没有值是吧可以在这去判断一下怎么判断就是说咱们有一个叫做streetutus.is
[11:18] not empty就是他不为空的话这时候咱们就可以去split然后干嘛呢与座号分割座号分割好这个其实就是一个数组这个数组咱们叫做update our array吧ray好吧拿了这个之后这个之后我们上面就可以直接去直接去这么着直接去return就可以了
[11:47] 瑞克啥呢瑞克当前的这个书组里边的这个count就是update name这个呢就能去取出一个值不能去取出一个值啊这个好像有问题是吧那这样咱们就用integer啊integer.pass in把后面的东西装进去好吧那这样就可以了啊还不行吗应该是这个啊那这样就可以了啊
[12:17] 这样设置完之后呢就能去取出某一个某一个的值比如说你第零次那就是拿到的次如果说第一次拿到是16第二次拿到的是64是吧这样的话它就能去根据当前你返回的然后呢再去相加你的什么再去相加你的下一次更新的时间好然后这里边还有一个还有一个参数啊如果说它要是这东西没值就没有读到值那怎么办呢咱们可以给一个默认值
[12:46] 可以给个默认值这个默认值咱们就可以怎么着就是说return count这样写写一个updateNum就是2的这个次方是吧我们可以给个默认值好吧行这样的话咱们就算是写完了整个当前的additional就是要新增的这一块数据咱们也做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

