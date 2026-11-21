# 14_自媒体文章管理_发布文章业务代码编写1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\14_自媒体文章管理_发布文章业务代码编写1【海量资源尽在 666java.com】.mp4
- 时长 23分14秒（音频 1395s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就把这个实现类啊给实现方法给写一下啊那这个方法呢可能比较多内容比较多啊比较复杂大家一定要注意看啊跟着思路往下走好吧来首先呢咱们是要看断前的参数文章内容是否为空是吧如果说为空的话咱们就返回一个这种什么参数有问题是吧好直接判断啊就是DTO等于等于那过着啥呢
[00:31] BTO.getcontent这个咱们用一个什么呢用一个当前的工具列utils.isNotEmpty把它的装进去 围空吗然后你看它这是围空吗来去判断啊也可以这样啊再加个非好吧那话就是不围空它就是围空啊这样就围空了两个非不就是围空了吗那围空的话呢咱们就在这啊
[01:04] 在这呢可以这样这样这样写可能不太好是吧呃就可以了啊好吧如果说它为空那这时候呢咱们就直接去return什么东西啊response without点然后是直接说你这个参数啊有问题好了那就可以了啊那下面呢咱们就说啊如果说本次为修改操作的话那我就先删除数据库关联数据那这个呢其实呢就这样啊咱们要去判断
[01:36] 目前是否是修改的话你主要是判断啥呢DTO中的什么有一个IDID啊IDGETID如果说ID啊它不等于NUM就说明啥呢说明修改那这时候咱们就可以删除啊删除关系就是它是吧OK好到这RELATE就是根据当前的DTO中的什么GETID就可以了好吧那这个咱们就做完了啊
[02:05] 下面呢咱们要去将用户提交的文章内容解析为MAP结构的数据那这个呢其实是为了为了能够提取当前的图片文章内容的图片信息文章内容的图片信息那这时候咱们首先啊先去干嘛呢先去把这个内容给拿到内容的话怎么着dto.getcontent好那这个就是content啊拿到content之后呢咱们呢首先呢这个结构
[02:33] 大家知道啊那这结构你要是不清晰的话呢你可能就不知道怎么解析是吧所以说啊咱们在这啊先去看一下之前的数据是怎么存的咱们打开一个new其实就这个就是content咱们可以双击一下然后是跑到一个json.json好吧好考到这考到这我们又考全是吧咱们就这样啊嗯这样考就可以了啊ctrl c一下再靠一下
[03:08] 这考也考不全是吧这个内容应该太多了应该是啊好这样考全了啊保险完之后呢咱们在这再去重新拷贝一下我给大家数据拿到了啊你看我现在最外层是一个通过号然后里边是各个对象看到了吗是是这个情况吧但这个这个咱们顺便去分析一下吧那这里边有个texttext的话其实就是文本里边如果说是image的话呢就是当前某一个图片这能看明白吧text就是文本啊image就是
[03:42] 它每个对象是不一样的好吧行那咱们下面呢就来去解析首先咱们已经知道了它最外层啥呢最外层是一个大括号那就是咱们可以转换成一个集合是吧好那咱们下面呢就来去转换集合那转换集合是这样啊转换集合的话呢咱们需要干嘛呢需要用到一个object map所以说咱们在这啊去先注入一个我们一个叫什么object map这个呢是dex它提供的一个类啊
[04:12] 然后是注入进来之后呢咱们在这直接去这边有一个readvalue啊你可以去第一个第一个就是啊你可以根据某一个字符算转成什么样的类型是吧第一个啊把content转成什么呢转成一个listlist.class最终是转一下啊它就是一个list里边呢咱们都知道里边装的是一个麦克风啊那是一个麦克风key value嘛key value啊
[04:44] 行那咱们下面呢就可以直接用麦普去接收这样就可以了好吧这块他是说有问题啊要干嘛呢这块呢咱们需要去开启一下要去开启一下行那这个那你这里边拿到之后呢咱们需要去解析需要去解析啊因为最终呢咱们还是需要拿到图片的需要拿到图片啊所以说咱们在这啊专门的去定义一个方法去
[05:14] 抽取信息在这写啊抽取信息怎么抽呢比如说啊咱们直接解析ESESURL然后是提取URL然后是信息最终呢是把谁拿到呢是当前那个list集合最终要响应回来的数据呢是一个map一个mapStringStringObject
[05:47] 这个咱们叫什么叫叫叫叫叫他吧exacp好吧map就info吧那这个好像写错了是extract好那这样的话咱们就算是设置完了方法没有是吧没有就加进来就创建一个好吧然后创建完之后咱们在这就顺便的去写一下这个方法主要是干嘛用呢是抽取
[06:23] 抽取图片信息好吧那这历史里这里边啊就有目前咱们需要的图片信息那拿到图片之后干嘛呢咱们其实咱们之前分析过拿到图片就是为了能够保存它的关系什么关系呢文章跟当前的图片的关系所以说你要先去拿到这个图片然后最终拿到图片的ID再保存当前文章跟图片的关系就可以好吧行那咱们下面呢下面就先去拿到当前的一个图片啊
[06:53] 咱们可以去编例一下listr4这里边咱们怎么拿首先你可以去直接去认证再说了这个结构大家已经很清晰了这个结构里边是image的话它就是图片是吧所以说你在这直接去判断就可以怎么判断就是说当前如果说你type不是typeimage
[07:26] map.get是谁啊你都知道了这就是image对啊gettype如果说type是image的话呢它就是图片那这时候我们就可以把这个图片给保存了给保存了那这个保存的话怎么保存呢其实咱们还在这在这再去创建一个类念一个map好吧念一个map你说map里边是一个stream然后是object
[07:57] 然后怎么叫啥呢叫myperlux等于new一个hashi map创建完之后呢这儿你可以直接去添加而铺的之前呢咱们还是要考虑一些问题啊有问题比如说这里边啊这个值啊万一打开这个啊万一呢它是包含了当前的这种什么啊访问的服务器的地址的话这时候咱们需要去替换一下
[08:29] 需要去替换一下所以说怎么办在这你要去先去拿到当前的这个值好吧这个值怎么拿谁有卖婆点get谁get谁你可以再看一下这个结构如果说是找到当前一个对象之后咱们是不是可以拿到通过value去拿你说这去valuevalue的话用的咱们就可以去拿到一个
[08:55] 这个值是obj的,他们可以去强转一下强转成一个str,比如说它就是个str然后这是image的URL这个咱们可以这样写,就是str的value of你把它给装进去就可以了,好吧,转换一下
[09:22] 完后呢还要再去看他说了你要去判断前是否包含什么呢是否包含当前的服务器的地址所以说你密室有点死那特无位置位置谁呢就是费用就费用了他们没有是吧其实咱们在之前的一种文件中已经写了一个类东西是吧可以说你直接考虑一下他啊这儿再去重新去注入一个东西
[09:53] 叫fillServerPath好吧fillServerPath叫URL可以啊URL吧那咱们在这可以直接用一个value打进来注进来啊拷贝一下好那拿到这个之后呢咱们可以往下看啊如果说是他结尾的如果说是以他结尾的话呢咱们呢就把它给替换一下怎么替换呢就是当前的mul.r
[10:24] replacereplacereplace一个是谁啊一个是就是非欧然后第二个呢空替换成空就可以了这时候呢你就可以把它呢放进去了啊而putput之后呢这里边还还少个东西是吧咱们呢为了能够去方便的去做东西啊咱们下面呢就可以干嘛呢就可以放一些东西
[10:55] 那放东西的时候怎么放呢其实咱们可以去设置一个下标或者说设置一个数量设置一个图片的数量那这数量怎么去做呢其实数量咱们后期还会再用咱们先定义咱们用到的时候咱们可以再说首先咱们在这再去定义一个东西比如说有个intholder这个order的话是为了能够排序用的保存图片的时候排序用的你要去定义一个什么东西定义一个图片的数量ontimage number
[11:25] 好吧等于零等于零啊这个呢是欧洲的话呢咱们可以去在这随便去设比如说爱的家家啊这个呢就是你要去统计当年普遍信息的话就是抗客抗的家家这个啊给咱们后期会用这个是为了排序啊是为了排序啊行那这个咱们铺的的时候呢咱们第一个值呢就可以把它给他设置为啥呢哎给他设置为当前的一个欧的欧的啊比如说欧的可以吧
[11:56] older 包错了是吧older 包错了没有事啊spin.volume off把older装进去就完事了那这样就可以了啊然后呢你说你得循环完了啊循环完之后其中咱们要去返回呀在这啊你返回呀那怎么返回呀返回一个map呀比如说在这啊再去创建一个mapres.new一个hashi map然后你可以往里边去装两个东西res.put
[12:27] 第一个装的就是前面这个图片的和图片的MAP好把这个简号删了这是一个然后下面还有再装一个res.put前面的数量你要去装进去数量的话咱们就叫到它吧count image number好吧好那这样就完了最终你把这个MAP给返回完成了res完成好吧前面这样的话返回的MAP信息中就换了两部分第一部分
[13:02] 第一部分就是当前的一个图片的集合图片的卖博集合应该这样说啊第二个呢就是当前图片的数量当前图片的数量好吧那行那这个咱们就算是解析完了啊解析完之后呢咱们现在就可以去拿到这两个纸啊一个呢就是怎么拿呀第一个是get是吧通过第一个谁啊要拿到当前那个集合当前那个图片的信息ALS是吧
[13:30] 用的是拿到一个集合这个集合这个其实应该是个卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖卖
[14:04] 这是第一个,抽取图片的信息图片信息好,继续把数量拿走图片数量,拿呀还是用它是吧还是用这个方,里面的契合然后是点get这什么来着还知道吗count image是number最终咱们就可以去拿到当前的
[14:39] 数量int我们叫countimagenumber好吧我们可以去强转一下强转成int就可以了行那这个图片数量拿到了啊拿到完之后呢咱们下面就可以去保存文章了啊这个卡到上面保存完文章之后呢咱们才会真正的去干嘛呢去保存他们的关系好吧行那这个保存文章不容易了啊那咱们在这儿可以直接去转一下保存文章的时候咱们还需要去复写值啊比如说咱们在这儿啊
[15:11] 可以直接干嘛呢创建一个WM News创建一个当前的对象这个参数是没有的啊所以说咱们先用一个Utils.copy properties就是把当前的属性可以拷过去拷过去啊这个呢目标是谁目标是DTO然后源是谁啊应该错了第一个是源第二个目标啊WM News好吧就是把当前的对比的属性拷到这里边
[15:40] 这里边当然这个里边还没有全所以说咱们还要再去做一个图段再往下走往下走的话咱们首先有一个DTO.getType什么Type其实就是图或者图图或者图图咱们下面就来去ecos一下这里边咱们需要去判断到底是哪一种方式去存的所以说咱们在这可以去设置一些值
[16:11] 设置值啊那这设置值的话咱们再往下看啊那这个它是什么值呢是这样啊那呢打开这个表啊这个表里边呢其实现在呢现在啊打开当前这个对象其实这个type这个type的话呢目前的话呢你看是无图单图或者多图其实这个呢咱们在数据展示的时候啊或者说你那个从前代网络传的时候这块内容呢其实已经传了有了吗有了单图
[16:42] 三储无储或者是自动或者是自动啊那下面呢咱们就来去设置一下啊在这呢咱们可以去让他去设置为看他是不是等于自动的自动啊自动的时候怎么保存然后其他值咱们就按取值的数据保存就可以了好吧那其实呢咱们在那个当前的某一个这种就这个东西constance里边啊咱们有一个值叫什么呢
[17:13] wmnews什么呢有一个type-auto这个auto呢是一个-1咱们在前台去传过来的时候就是一个-1不说它是-1的话呢咱们是一种方式去保存还有呢就是还有一种另外一种方式如果说你要是传具体的值的话呢咱们是另外一种保存方式只是呢传的值是不一样所以说咱们在这啊再去抽一个方法叫favorwmnews
[17:44] 好吧WM News啊然后呢咱们又可以去设置一些值这个两个参数是差不多的啊但是参数哪一块不一样呢你看如果说它是自动的话呢咱们就把这个就把这个数量给它传过去好来看一下啊往下走第一个是WM News第二个呢就是当前的数量当前的数量啊但它是一个自动啊这个值的话你是自己可以说了算的咱们也可以按照一些规则去设置啊第三个是Type
[18:13] 这个type的话就可以去决定你是增还是修改下面这个呢下面这个啊如果说它不是自动的话呢咱们还是传这些参数这个呢就是要传到欧洲的gettype这个啊这个呢是前三种是前三种三图或者是五图只有自动的时候你需要你才需要单独的去处理它那个图片如果说是前三个的话它传什么你设置什么就可以了好吧好 大家看啊
[18:43] 然后第三个呢就是还是太薄了好这时候呢咱们又出了一个方法叫save不要binose这时候咱们要去把这个方法给创建出来好那这个呢其实就是保存的呢保存文章保存文章啊那咱们下面就来去实现一下啊那保存的话呢咱们再来分析一下其实呢咱们就主要是来判断当前这个类型就可以了啊但是保存的时候呢咱们需要用到用户信息
[19:13] 所以说咱们也需要去把这运动信息给拿到首先咱们还是要去判断一下当前的这种类型咱们可以判断一下EF不啥呢比如说有一个其实就这个就像当前这个传统的这个值如果说它等于等于谁呢如果说它等于当前的WMD这种constants如果说是比如说singlesingle是个单图找到这个单图
[19:46] 有第一个是吧如果是等于1的话呢咱们就可以去设置一个1比如说咱们可以wmnews.settype其实呢就是就是当前这个值好吧这种方式啊这是一种情况还有else if你们再去判断啊如果说当前这个值啊它是大于等于谁呀大于等于这个money打开它啊放它点这边有一个money
[20:19] 应该是3啊应该是3嗯哪呢如果他大于等于3的话呢其实对这种情况呢咱们就设置为多图就可以了啊如果你要是再大的话那也是也是当前的多图这个东西你说你的图片呢有十张十张也不行十张也是一个多图好吧那一种情况叫啥呢这种情况的话就是无图就是无图啊就是这种情况啊咱们在这儿去设置一个
[20:55] 它有一个叫做NAND第一个好吧是一个无图就是三种情况第一个是真图二是多图第三个是无图好吧这首符信拿到之后咱们就可以去设置一些值比如说你补圈这里边其实还少一些东西比如说里边还少一个STATUSSET STATUSSTATUS其实就是你传过来的type好吧行再往下看
[21:27] wm news 还少啥呢点set这里边还有一个user id那这user id怎么拿呀刚才说了user id是wm Thread local点get user是不是就能拿到它现在user啊拿到user之后你直接去把当前的id给拿到就可以了好吧然后再往下啊wm news点set create time我们拗一个好吧
[21:55] 然后下面还有一个wmnews.rset是一个submit这也是一个new的data非常简单然后再往下的话其实还有一个able怎么一下去设置一下就是当前的一个是否有效是吧able咱们默认给它个1就是有效好吧在这咱们可以去强转一下叫short它就是一个short的类型这样的话就设置完了设置完之后就可以保存了
[22:24] 保存的时候大家注意保存的时候咱们还要再去判断一下判断什么呢判断当前地址里边WM News里边get id到底是否等于空它等于空中不等于空又该怎么办其实也都很清晰了现在是等于空就是保存不等于空就是修改在这你可以直接用WM Newsmypool.insert
[22:55] 把当前的Wappsnews转进去就完了好吧然后下面这个呢还是Map.update就还是Wappsnews转进去就可以了这是修改现在这个保存咱们就先说到这里好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现文章内容的保存功能，包括参数校验、JSON 数据解析、图片信息提取、文章类型判断和数据库持久化操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 NewsServiceImpl.java 文件中 saveNews 方法的开头部分，包含对 dto 参数的空值和内容为空的校验，以及调用 wuNewsMaterialMapper 的方法。
画面 2: 展示 saveNews 方法中对 dto.getId() 的判断，用于处理用户首次操作或修改操作。
画面 3: 展示在 saveNews 方法中添加了 ObjectMapper 字段的声明。
画面 4: 展示 saveNews 方法中添加了 try-catch 块，用于捕获 IO 异常并打印堆栈信息。
画面 5: 展示 extractUrlInfo 方法的实现，用于从图片 URL 列表中提取图片信息。
画面 6: 展示 NewsServiceImpl.java 文件的顶部，包含多个 @Autowired 注解的字段声明。
画面 7: 展示 extractUrlInfo 方法中用于遍历图片 URL 列表并提取图片信息的代码。
画面 8: 展示 saveNews 方法中使用 ObjectMapper 将 JSON 字符串解析为 List<Map>，并调用 extractUrlInfo 方法提取图片信息。
画面 9: 展示 saveNews 方法中对 dto.getType() 与文章类型常量进行比较的逻辑。
画面 10: 展示 saveNews 方法中根据图片数量设置文章类型（单图、多图、无图）的逻辑。
画面 11: 展示 saveNews 方法中设置文章状态、用户信息、创建时间等字段的代码。
画面 12: 展示 saveNews 方法中根据文章类型调用不同的 save 方法（saveNews 或 saveNewsWithImages）。
画面 13: 展示 saveNews 方法中设置文章状态、用户信息、创建时间等字段的代码。
画面 14: 展示 saveNews 方法中根据文章类型调用不同的 save 方法（saveNews 或 saveNewsWithImages）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Override
public ResponseResult saveNews(WallNewsDto dto, Short type) {
    //如果用户传递参数为空或文章内容为空则返回错误
    if (dto == null || StringUtils.isEmpty(dto.getContent())) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
    }
    //如果用户本次为首次操作那么去删除数据库中关联的数据
    if (dto.getId() != null) {
        wuNewsMaterialMapper.deleteById(dto.getId());
    }
```

画面 2:
```java
    //如果用户本次为首次操作那么去删除数据库中关联的数据
    if (dto.getId() != null) {
        wuNewsMaterialMapper.deleteById(dto.getId());
    }
```

画面 3:
```java
    private ObjectMapper objectMapper;
```

画面 4:
```java
    } catch (IOException e) {
        e.printStackTrace();
    }
```

画面 5:
```java
private Map<String, Object> extractUrlInfo(List<Map> list) {
    Map<String, Object> materials = new HashMap<>();
    for (Map map : list) {
        if ("image".equals(map.get("type"))) {
            materials.put("url", map.get("url"));
        }
    }
    return materials;
}
```

画面 6:
```java
@Autowired
private WmNewsMapper wmNewsMapper;

@Autowired
private WmNewsMaterialMapper wmNewsMaterialMapper;

@Autowired
private ObjectMapper objectMapper;
```

画面 7:
```java
private Map<String, Object> extractUrlInfo(List<Map> list) {
    Map<String, Object> materials = new HashMap<>();
    int order = 0;
    int countImageNum = 0;
    for (Map map : list) {
        if ("image".equals(map.get("type"))) {
            materials.put("url", map.get("url"));
            countImageNum++;
        }
    }
    materials.put("countImageNum", countImageNum);
    return materials;
}
```

画面 8:
```java
try {
    List<Map> list = objectMapper.readValue(content, List.class);
    //抽取信息
    Map<String, Object> extractInfo = extractUrlInfo(list);
    //图片信息
    materials = (Map<String, Object>) extractInfo.get("materials");
    //图片数量
    int countImageNum = (int) extractInfo.get("countImageNum");
    //保存或修改文章的数据
    //保存图片与当前文章的关系
    //保存图片与当前文章的关系
    //保存图片与当前文章的关系
} catch (IOException e) {
    e.printStackTrace();
}
```

画面 9:
```java
if (dto.getType().equals(dto.getType())) {
```

画面 10:
```java
if (countImageNum == WmMediaConstants.VM_NEWS_SINGLE_IMAGE) {
    walleNews.setType(WmMediaConstants.VM_NEWS_SINGLE_IMAGE);
} else if (countImageNum == WmMediaConstants.VM_NEWS_MANY_IMAGE) {
    walleNews.setType(WmMediaConstants.VM_NEWS_MANY_IMAGE);
} else {
    walleNews.setType(WmMediaConstants.VM_NEWS_NO_IMAGE);
}
```

画面 11:
```java
if (countImageNum == WmMediaConstants.VM_NEWS_SINGLE_IMAGE) {
    walleNews.setType(WmMediaConstants.VM_NEWS_SINGLE_IMAGE);
} else if (countImageNum == WmMediaConstants.VM_NEWS_MANY_IMAGE) {
    walleNews.setType(WmMediaConstants.VM_NEWS_MANY_IMAGE);
} else {
    walleNews.setType(WmMediaConstants.VM_NEWS_NO_IMAGE);
}
```

画面 12:
```java
private void saveNews(WallNewsDto dto, Short type) {
    if (countImageNum == WmMediaConstants.VM_NEWS_SINGLE_IMAGE) {
        walleNews.setType(WmMediaConstants.VM_NEWS_SINGLE_IMAGE);
    } else if (countImageNum == WmMediaConstants.VM_NEWS_MANY_IMAGE) {
        walleNews.setType(WmMediaConstants.VM_NEWS_MANY_IMAGE);
    } else {
        walleNews.setType(WmMediaConstants.VM_NEWS_NO_IMAGE);
    }
    walleNews.setUserId(user.getId());
    walleNews.setCreatedTime(new Date());
    walleNews.setSubmittedTime(new Date());
    walleNews.setStatus(type);
    walleNews.setArticleId(dto.getArticleId());
    walleNews.setChannelId(dto.getChannelId());
    walleNews.setContent(dto.getContent());
    walleNews.setUrl(dto.getUrl());
    walleNews.setUrlTitle(dto.getUrlTitle());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrlType());
    walleNews.setUrlType(dto.getUrl

