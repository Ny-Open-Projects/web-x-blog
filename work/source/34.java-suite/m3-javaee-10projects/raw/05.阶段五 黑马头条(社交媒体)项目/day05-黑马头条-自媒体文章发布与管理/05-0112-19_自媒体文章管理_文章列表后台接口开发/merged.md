# 19_自媒体文章管理_文章列表后台接口开发

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\19_自媒体文章管理_文章列表后台接口开发【海量资源尽在 666java.com】.mp4
- 时长 10分12秒（音频 613s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们来完成下面的接口是文章列表后台接口那这个后台接口呢主要是这样啊主要呢就是在当前的这一块你发布完章之后呢这有一个内容列表那这个列表呢就可以去查询所有的内容那主要是文章信息啊文章信息呢主要呢是有这有这些条件啊首先呢是状态啊还有就是
[00:24] 频道的列表比如说你选择哪个频道的是吧还有一个时间段一个开始时间和一个结束时间最终咱们是要分页查询好吧分页查询啊行那这个需求咱们就说到这啊然后往下看啊往下看咱们就看这个接口啊接口定义的话呢比较简单就是说目前的话咱们只需要去有一个newnew list就完事了啊操作成功之后呢你把这个数据封装到地址中就完事了好吧当然这里边还有个东西咱们要去说就是这个
[00:51] 那这个呢咱们看一下这参数啊就是参数的话就是跟刚才这个分析的参数是一样的啊咱们可以找到当前这个类好这里边始源是一个状态是吧然后第二个呢就是当前的开始时间陪助时间还有你的频道或者是你的什么keywords你可以去搜索啊你可以去搜索啊但是在目前搜索的话并没有做啊但是这个你也可以呃后期的话如果说有有一些搜索框的话咱们也可以去进行搜索好吧
[01:22] 那行那这个说完之后咱们就先去写MAP这MAP的话都是去查询并且分页那很显然是有几个两个一个是查询根据条件查询第二个是要统计第二个要统计行把这两个考过来找到咱们的MAP搜一下叫newsMAP可以找到当前的接口第一个是再说一遍一个是当前的
[01:54] 根据条件查询返回是个例子集合第二个是返回一个count这里边参数是有两个是吧都有两个所以说在这儿就写一下什么param写错了at param然后把这个给标示一下是dto然后第二个是什么param是uid要根据前的用户id去查询上面这个下面这个一样咱们就直接去拷贝一下就可以了好dto然后这是uid
[02:28] 那是完之后咱们下面就可以去写他的麦普文件这个麦普文件都是一些查询好我来看一下上面这个就是查询所有的列表你返回的是所有的字段条件是当前的UID然后还有什么有可能是有你的状态有可能是你的频道是吧还有你的开始时间开始时间和结束时间还有一个就是当前的什么当前的一个这东西就是有个keywords
[03:03] 那这个里边还有一个参数这个参数是配置和什么size是吧那这个是怎么来的呢这个你可以再看这个这个当前这个类刚才说条件是有这么多条件他还要分页分页的话你看他是不是继承了一个叫配置request TTO啊按到里边就有size和配置好吧你还检查一下参数这个类咱们之前是用过的好吧
[03:25] 行那这个咱们这个Map文件就设置完了下面也是一样下面只是没有分页条件是一样的好吧条件是一样的行那么下面就来去写当前的Service这个Service的话就在当前的media中然后还是news Service里边去写这个逻辑就可以打开当前news Service好再去加一个方法方法呢就叫什么发行用户发行文章里边public response without
[03:54] 目视反为他啊最终是listi user好吧就叫就叫他啊然后这个参数呢是wm news然后是page request好吧嗯说完之后呢在这其他主持啊什么查询文章列表好吧那下面呢就来去写他的实现好拉到最后拉到最后在这写一个
[04:26] 叫listbyuser好吧行那加加进来之后啊那咱们就可以去评断了啊我现在还是第一步什么呢要去判断参数dto点什么dto1.1.1好吧等1.1.1然后呢咱们可以直接return一个错误什么呢response redout点说你的参数有问题啊app完了收完之后啊咱们下面再往下看再看啊
[04:58] 这时候咱们就可以去进行检测检测啥呢检测当前的参数这个参数咱们之前也写过就是这里边当前这个配置有可能会出问题有可能你没有传或者说你传的值过大是吧等于在这稍微去检查一下就是DTO什么TagTrim这时候不能初始化两个值初始化两个值是吧要是
[05:22] 不符合规则咱们就设置个1这个不符合规则就设置个默认值是10当然如果复合的话咱们就按传过来的这个值去设置就可以了好吧那行啊那最终呢咱们就可以去查询了啊这查询的话就用谁啊Arm News MacR有一个Select哪个是不是第一个啊是不是像这个啊这个里边啊咱们需要两个参数啊DTTO好拿这个呢这个是需要个运输外地咱们还是用什么
[05:51] WM Thread local.getuser.getid拿到ID之后呢咱们这个就是UIDUID好吧把这个UID给传过来就可以了那这样就可以了最终它返回的是啥呢返回的返回的就是一个列表就是一个比如说怎么叫data4好吧就是一个列表拿到列表之后咱们还要再去拿到另外一个数据哪个数据WM news讲什么
[06:22] 他有一个统计是吧统计还是DTO还是什么呢还是UID是吧最终是拿到一个count好这就是总少数叫total也行total设置完之后咱们就可以去响应了响应的时候对这时候咱们就不太一样了这里边我要去做一下我怎么写一会咱们写完之后咱们再解释好吧咱们使用一个page requestpage request result
[06:57] 然后呢是response result然后干嘛呢等于new一个page request response result好了啊这里边啊咱们就可以传两个参数dt第一个呢就是前的什么tto中的配的配置然后第二个呢是tto中的什么get sizesize三个呢就是咱们的total是它的一些资源条件啊
[07:27] 还要再往里边去设置一些纸比如set什么date就是dates除了这里边这里边有y还有一个东西咱们要去设置叫sethosthost是啥呢host有时候在说这个host的话其实就是当前图片访问的一个路径其实怎么写叫fuel server基本最终你把当前这个response result把它翻回就可以了你可以看这个它是不是继承了response result
[07:57] 是可以的啊这样的话这样为什么要这么做呢其实这么做的方式呢就是为了能够这个是在当前返回职中去拿到一些什么一些分页的参数还有你的数据啊你的数据是在Date中House呢为了拿House刚才说了因为这个Date里边啊因为你目前查询出来的这个东西呢它并没有带请求的地址是吧所以说呢你要告诉它一个House这个House就是你当前图片服务器的地址
[08:26] 方便前台去拼接方便前台去拼接那行那这个咱们说完之后咱们下面就来去写它的Controller也就是它的接口打开当前的这个地咱们还是找到当前的哪个就是news Controller API好这去写一下啥意思response result再个public吧publicresponse result
[08:59] 然后是叫list user然后条件是他说了就是wm user不是news news pagerequest DTO加完之后咱们在这加注是吧什么要什么用户查询用户查询文章列表是分页我又不说了后面咱们肯定是要分页的
[09:29] 那行那这个说完之后啊那咱们下面就来去找到他的Controller在这写下啊叫什么listuser加上加上之后啊咱们在这首先呢要去加一个东西嗯加什么东西啊加一个postpostmyping啊这里边要去设置设置值了啊第一个是什么就这一个是吧list就叫list就可以了啊这个呢是要什么request body好这加完之后啊咱们最终呢就可以去
[10:00] 要用当前的Service.list.dto进去就完事了好吧这个咱们就算是完了啊那接口咱们就先开发到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个新闻内容管理系统的后端实现，重点是通过分页查询、条件筛选和数据映射来处理文章列表和图片素材。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个JSON在线解析器，其中包含一个包含文本和图片类型的JSON数组，用于模拟文章内容数据结构。
画面2：展示一个新闻管理后台的“内容列表”页面，显示文章状态筛选、分类筛选和时间范围筛选功能，当前无数据。
画面3：展示IDEA中`WinNewsMapper.java`文件，定义了`insertNews`和`selectBySelective`等方法，用于插入和分页查询文章数据。
画面4：展示`WinNewsMapper.xml`文件中的SQL映射，包含`selectBySelective`查询语句，使用`<if>`标签进行多条件动态拼接。
画面5：展示`WinNewsMapper.xml`中`countSelectBySelective`的SQL语句，用于统计符合条件的文章总数。
画面6：展示`NewsService.java`接口，定义了`saveNews`和`listByUser`等方法，用于处理新闻保存和分页查询业务。
画面7：展示`NewsServiceImpl.java`中处理图片上传的逻辑，包含对`fileServerUrl`的替换和异常处理。
画面8：展示`NewsServiceImpl.java`中`listByUser`方法的实现，创建`Map<String, Object>`并返回数据。
画面9：展示`NewsServiceImpl.java`中`listByUser`方法的实现，使用`while`循环和`ThreadLocal`进行数据处理。
画面10：展示`NewsServiceImpl.java`中`listByUser`方法的实现，使用`vulNewsMapper`进行数据查询并封装`PageResponseResult`。
画面11：展示`NewsServiceImpl.java`中`listByUser`方法的实现，设置`PageResponseResult`的`host`和`data`属性。
画面12：展示IDEA项目结构，聚焦于`heima-leadnews-media`模块下的`src/main/java`目录。
画面13：展示`NewsControllerApi.java`文件，定义了`submitNews`、`saveDraft`和`listByUser`等API接口。
画面14：展示`NewsController.java`文件，定义了`@PostMapping("/submit")`、`@PostMapping("/save_draft")`和`@PostMapping("/list")`等控制器方法。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面3：
```java
int insertNews(@Param("dto") NewsDto dto),
// ...
List<Follows> selectBySelective(@Param("dto") FollowsPageDto dto, Long uid)
// ...
int countSelectBySelective(@Param("dto") FollowsPageDto dto, Long uid);
```

画面4：
```xml
<select id="selectBySelective"
        resultType="com.heima.model.medias.VulNews">
    <include refid="Base_Column_list"/>
    from vul_news
    where
    user_id = #{dto.userId}
    and status = #{dto.status}
    and channel_id = #{dto.channelId}
    and title like concat('%', #{dto.keyword}, '%')
    and publish_time <![CDATA[>]]> #{dto.beginPubDate}
    and publish_time <![CDATA[<]]> #{dto.endPubDate}
    <if test="dto.page != null and dto.size != null">
        limit #{dto.page} , #{dto.size}
    </if>
</select>
```

画面5：
```xml
<select id="countSelectBySelective" resultType="java.lang.Integer">
    select count(1)
    from vul_news
    where
    user_id = #{uid}
</select>
```

画面6：
```java
public interface NewsService {
    // ...
    public ResponseResult saveNews(@Param("dto") NewsDto dto, Short type);
    // ...
    public ResponseResult listByUser(@Param("dto") FollowsPageDto dto);
}
```

画面7：
```java
if ("image".equals(map.get("type"))) {
    countImageNum++;
    String url = String.valueOf(map.get("value"));
    if (url.startsWith(fileServerUrl)) {
        url = url.replace(fileServerUrl, "");
    }
    // ...
}
```

画面8：
```java
Map<String, Object> res = new HashMap<>();
res.put("materials", materials);
res.put("countImageNum", countImageNum);
return res;
```

画面9：
```java
while (true) {
    wait(Long.timeout, int nanos);
    if (ThreadLocalUtils.get() != null) {
        // ...
    }
}
```

画面10：
```java
Long uid = WulNewsUtils.getUid();
List<VulNews> datas = vulNewsMapper.selectBySelective(dto, uid);
int total = vulNewsMapper.countSelectBySelective(dto, uid);
PageResponseResult responseResult = new PageResponseResult(dto.getPage(), dto.getSize(), total);
responseResult.setData(datas);
```

画面11：
```java
responseResult.setHost(fileServerUrl);
responseResult.setData(datas);
return responseResult;
```

画面12：
```text
src
├── main
│   └── java
│       └── com.heima.media
│           ├── config
│           ├── Controller
│           ├── Service
│           └── NewsService
└── test
```

画面13：
```java
public ResponseResult submitNews(@RequestBody NewsDto dto);
public ResponseResult saveDraft(@RequestBody NewsDto dto);
public ResponseResult listByUser(@Param("dto") FollowsPageDto dto);
```

画面14：
```java
@PostMapping("/submit")
public ResponseResult submitNews(@RequestBody NewsDto dto) {
    return newsService.saveNews(dto, (short) 1);
}

@PostMapping("/save_draft")
public ResponseResult saveDraft(@RequestBody NewsDto dto) {
    return newsService.saveNews(dto, (short) 2);
}

@PostMapping("/list")
public ResponseResult listByUser(@RequestBody FollowsPageDto dto) {
    return newsService.listByUser(dto);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。

