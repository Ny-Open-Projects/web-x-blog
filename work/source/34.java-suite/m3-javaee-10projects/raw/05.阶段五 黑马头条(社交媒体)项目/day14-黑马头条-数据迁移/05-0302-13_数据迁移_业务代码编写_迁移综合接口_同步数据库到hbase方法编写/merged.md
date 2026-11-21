# 13_数据迁移_业务代码编写_迁移综合接口_同步数据库到hbase方法编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\13_数据迁移_业务代码编写_迁移综合接口_同步数据库到hbase方法编写【海量资源尽在 666java.com】.mp4
- 时长 11分57秒（音频 717s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好继续刚才咱们是查询了一个列表现在咱们要查询一个这个就比较好查了好咱们下面去写一下首先你要去判断一个东西就是当前的李亚波等于那他等于那的话咱们直接就可以return211return就可以了然后下面咱们就继续往下看第一回来看如果说他到这了之后咱们要去封装了我现在要去打给看见出来
[00:32] 先是等于一个None然后呢下面呢咱们就可以去查询那什么呢AEP Article Service而有一个叫做Slack Get By ID是吧Get By ID啊把ID传进去最终呢就能去拿到一个AEP Article好拿到它之后呢就可以去判断None不等于不等于啊AEP Article然后呢咱们就可以去设值了首先设的第一个值呢
[01:04] 设置之前呢你还得去new出来又一个AP然后是来设置set article就是当前那个AP article下面还有一些东西是吧分别要去查询配置内容还有当前的作者是吧那咱们首先呢要去查询AP article content Service.一个叫做curate by article id那这个呢就是
[01:37] article.getid 是吧它返回的就是一个对象那这个呢叫什么对象呢叫做 ap content article content 好吧然后呢就可以去设置了设置呗不是它.setapcontent这是content啊别弄错了然后把它呢给装进去好ok那第二对象完了那第三个第三个其实也是类似是吧ap然后是 article config
[02:11] Service而有一个叫做curate by article id还是当前的article.get id是吧然后最终的你就能拿到一个当前的ap article config然后呢是再装进去啊article.partity然后.set一个叫做ap article config然后是把它装进去啊那这个装进去之后啊还剩最后一个
[02:39] 最后一个是哪个呢就是当前的作者信息啊我们要去再查ap author Service点有一个叫做get by id这id啊就是ap article中的get author id啊这一定要别弄错了啊好点呢最终返回的就是一个什么ap author然后是再去装到这个对象里边就可以了啊点setset ap author
[03:10] 那个APOFTER装进去好那这样的话就算是说完了啊你把这个对象给返回这样啊那这样咱们这个这个方法咱们先先不先不写啊先写下边两个方法啊先写下边两个那下边两个呢其实呢咱们刚刚写的这个大的和这个根据ID查的都是为这两个这两个方法去服务的
[03:35] 好吧那咱们下面去来看一下首先是从db中去同步到哪hbase那这个东西该怎么去写呢非常简单在这首先你要去调获取到数据咱们可以在这先去印个东西吧点这东西都知道吧获取时间然后呢六逻辑就是你要去获取到前的集合就是刚才咱们那个什么为同步的集合然后是拿到当前的这个集合
[04:05] 这个结果之后呢你就可以去做同步了啊应该是保存到HBase中然后呢你先去判断一下它不等于None然后是它等于None然后呢并且呢它不等于不等于什么.isEmpty然后呢就可以去做操作了这时候咱们可以在这打印个日志什么呢开始进行定时数据到哪啊HBase
[04:37] 同步好筛选出未同步的数据数据量啊咱们讲个量吧好吧然后下面的是当前的article他点size好吧行那这个拿到之后啊咱们下面呢就可以去做一个同步那同步该怎么去同步呢那你说你看这里边有一个叫做h base叫storage啊按的点有一个叫做add这里边装的呀其实都是什么呢你看这边装机盒的话是一个
[05:15] list 记号里边装的是 hbase storage那这个有没有啊那咱们现在是不是叫 article quantity那并没有是吧咱们先把这个方法给写出来啊好这么个方法那第一个呢是表名表名的话咱们其实有一个常量啊咱们之前是讲过的啊叫叫什么来着叫 hbaseconstance.r这个表啊然后第二个ok那关键是第二个怎么拿这第二个也好拿啊好拿呢你看啊
[05:45] 点有一个get没有get我们可以循环一下我这写出来然后咱们再讲然后是它会用一个spam然后是map这里边咱们会有一个叫做找一找没有吗这个好这个然后这个是啥意思最终它就可以去做一个集合这个集合返回的你看是不是h被死了吗
[06:21] HBase Storage ClientList你把它装到这合适吗合适是不是合适合适完这个网站这样就装完了为什么会有这么个东西其实都是在哪定义的在Article Quality中去定义了一个Get HBase Storage这个Storage就主要是来去进行数据进行展唤咱们可以看一下可以找到当前的Get HBase Storage
[06:50] 这个其实就是啥呢这就是先去给你设了一个loading key是吧再给你设一个回调然后最终的其实就是这个方法你看他先会去拿到AP article去转了然后拿到content转了content转了还有什么author也转了那转换的过程其实就是咱们之前做测试的过程你可以看一下就是去拿到这个数据之后然后去往这个什么数据里边去
[07:15] entry list就往里边去一个一个去设置属性当然这个是你的bin name是吧然后是把你的进去好点进去点这个吧点这个比较合适他就是拿到你的属性做成key然后是做成value然后最终是设置到哪设置到了一个前的叫entry list这样的话你的所有的属性都已经设置进去了这样其实咱们定义这个类的作用就是说
[07:50] 方便一些因为啊咱们现在所有的文章相关的数据呢咱们统一都会封装成这一个类然后呢再去转换成HBaseStorage然后再去存储到哪存储到当前的HBase中是吧行啊那这样的话咱们就算是保存了啊那保存完之后啊保存完之后呢下面呢咱们可以再去往下写嗯这个呢就是啊嗯在这再去加个这东西吧else啊
[08:21] 主要的是来打印日志log.info然后是定时数据库定时定时然后是数据库到HBase又找到数据那这是一个下面还有一个咱们因为在这记录了个时间所以说咱们把这个号时也给打印一下log.info然后是定时数据库
[09:00] 数据库到hbase同步结束耗时耗时多长时间呢这个好写叫system-r-g-r-g刚才定义的一个什么那行那这样的话就做完了做完之后咱们下面还有一个咱们也把这个给写下其实跟这个类似这个是没有参数是吧是没有参数的下面还有一个有参数的
[09:30] 那有参数的那更简单了咱们就不需要去做循环转换了咱们只要去转换一次就可以了在这就加上还是再去加一个lawSystem.他好拿到他之后呢就可以在这打印打印开始进行异步数据库到HBase那为什么要异步呢因为这个是到监听去调用的用一条一条的去做嘛
[10:03] Article ID,号号,括号,然后是Article ID, 啊,CICLE,就它,那现在这个设置完之后啊,咱们现在在这去判断一下,说说啊,None不等于当前的Article ID,这时候呢,就可以去查询了啊,查询什么呢?
[10:25] get,这个方法是有的啊,你把这个Article ID放进去,这个是需要去转换一下吧,打入None value,好吧,
[10:36] 最终是拿到一个当前的这个ArticleQuantity然后你就可以再去判断一下如果说它不等于None的时候不等于ArticleQuantityNone不等于它这时候你就可以去做同步同步的方式还是一样他们可以直接去调当前的HBaseStorage最终就能拿到一个HBaseStorage然后你就可以叫storage.client.add这个是装一个就可以了
[11:07] 这个表名还是HBaseConstance.有一个名然后呢就是把这个对象放进去那这样的话就算是行了啊保存完之后啊咱们下面呢再去在这去打印一下啊log.info那是一步数据库到HBase同步完成耗时先把这个ID打印出来一下啊
[11:37] 再设一个号时一个就是ArticleID第二个是System.R.G.这样的话咱们就算是设置完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Heima-LedNews 项目中，实现文章数量服务的迁移逻辑，包括根据文章 ID 查询文章数量、组装 ArticleQuantity 对象，并将数据同步到 HBase 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 编辑器中显示 ArticleQuantityServiceImpl.java 文件。
- 代码片段：`if (null == articleQuantityList && articleQuantityList.isEmpty()) { Log.info("%s生成articleQuantity列表完成, size: %d", "articleQuantityList.size()); }`
- 代码片段：`return null;`
- 代码片段：`@Override public ArticleQuantity getArticleQuantityByArticleId(long id) { return null; }`

画面 2：
- 代码片段：`if (null == articleQuantityList && articleQuantityList.isEmpty()) { Log.info("%s生成articleQuantity列表完成, size: %d", "articleQuantityList.size()); }`
- 代码片段：`else { Log.info("%s生成articleQuantity列表完成, size: %d", "articleQuantityList.size()); }`
- 代码片段：`return articleQuantityList;`
- 代码片段：`@Override public ArticleQuantity getArticleQuantityByArticleId(long id) { if (null == id) { return null; } ArticleQuantity articleQuantity = null; if (null != articleId) { articleQuantity = new ArticleQuantity(); articleQuantity.setArticleId(articleId); apArticleContentService.getArticleId(articleId); } return null; }`

画面 3：
- 代码片段：`@Override public ArticleQuantity getArticleQuantityByArticleId(long id) { if (null == id) { return null; } ArticleQuantity articleQuantity = null; if (null != articleId) { articleQuantity = new ArticleQuantity(); articleQuantity.setArticleId(articleId); apArticleContentService.getArticleId(articleId); } return null; }`
- 代码片段：`apArticleConfigService.getArticleId(articleId);`

画面 4：
- 代码片段：`@Override public ArticleQuantity getArticleQuantityByArticleId(long id) { if (null == id) { return null; } ArticleQuantity articleQuantity = null; if (null != articleId) { articleQuantity = new ArticleQuantity(); articleQuantity.setArticleId(articleId); apArticleContentService.getArticleId(articleId); } return null; }`
- 代码片段：`apArticleConfigService.getArticleId(articleId);`

画面 5：
- 代码片段：`@Override public ArticleQuantity getArticleQuantityByArticleId(long id) { if (null == id) { return null; } ArticleQuantity articleQuantity = null; if (null != articleId) { articleQuantity = new ArticleQuantity(); articleQuantity.setArticleId(articleId); apArticleContentService.getArticleId(articleId); } return null; }`
- 代码片段：`apArticleConfigService.getArticleId(articleId);`

画面 6：
- 代码片段：`@Override public ArticleQuantity getArticleQuantityByArticleId(long id) { if (null == id) { return null; } ArticleQuantity articleQuantity = null; if (null != articleId) { articleQuantity = new ArticleQuantity(); articleQuantity.setArticleId(articleId); apArticleContentService.getArticleId(articleId); } return null; }`
- 代码片段：`apArticleConfigService.getArticleId(articleId);`

画面 7：
- 代码片段：`@Override public void dTBase() { long currentMillis = System.currentTimeMillis(); }`
- 代码片段：`@Override public void dTBase(Integer articleId) { }`

画面 8：
- 代码片段：`@Override public void dTBase() { long currentMillis = System.currentTimeMillis(); }`
- 代码片段：`@Override public void dTBase(Integer articleId) { }`

画面 9：
- 代码片段：`@Override public void dTBase() { long currentMillis = System.currentTimeMillis(); }`
- 代码片段：`@Override public void dTBase(Integer articleId) { }`

画面 10：
- 代码片段：`@Override public void dTBase() { long currentMillis = System.currentTimeMillis(); }`
- 代码片段：`@Override public void dTBase(Integer articleId) { }`

画面 11：
- 代码片段：`@Override public void dTBase() { long currentMillis = System.currentTimeMillis(); }`
- 代码片段：`@Override public void dTBase(Integer articleId) { }`

画面 12：
- 代码片段：`@Override public void dTBase() { long currentMillis = System.currentTimeMillis(); }`
- 代码片段：`@Override public void dTBase(Integer articleId) { }`

画面 13：
- 代码片段：`@Override public void dTBase() { long currentMillis = System.currentTimeMillis(); }`
- 代码片段：`@Override public void dTBase(Integer articleId) { }`

画面 14：
- 代码片段：`@Override public void dTBase() { long currentMillis = System.currentTimeMillis(); }`
- 代码片段：`@Override public void dTBase(Integer articleId) { }`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

