# 12_app搜索_查询联想词接口开发完成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\12_app搜索_查询联想词接口开发完成【海量资源尽在 666java.com】.mp4
- 时长 10分24秒（音频 625s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们来完成查询联想词联想词的借口啊那这联想词呢其实就是说客户输入关键词之后呢咱们会给他去展示某一些联想词那这个咱们来看一下这个借口定义啊首先呢这个借口是当前这个路径是吧然后是当前的一个user search DTO还是这个还是这个DTO啊但是DTO里边咱们需要去设置哪些参数呢咱们可以看一眼啊打开当前的user search DTO
[00:30] 这里边咱们有一个非常关键的就是search words就是你搜索的词根据当前用户输入搜索的词咱们再去联想其他的词是这么个效果行再往下看返回的话就是返回一个列表就可以了返回当前这个表中的数据就可以当然你再查出来咱们可以打开这个表叫APisocet还有什么words找到当前的这个表
[01:01] 大家来找一找啊是它是吧APIsocet Words联想词那目前联想词呢其实我就设置了几个啊第一个是黑码其实里边都包含了黑码当我输入黑码的时候呢它应该给我查询出来这三个这三个啊那很显然我输入黑码能查出这三个那怎么查呀很显然是不是模糊查询对吧对就是模糊查询啊现在咱们下面呢就来先去完成MAP这个MAP的话就是一个模糊查询啊
[01:34] 这里边有两个条件有两条件第一个条件就是你输入的词这个就是你要查询多少条多少条行咱们来写现在卖破这个卖破的话咱们还是得打开当前的model因为它是另外一张表每一个表咱们都会去创建一个卖破接口来考进去把这个打包没错没问题然后没问题之后咱们就来去创建咱们的卖破文件打开再拷贝一个来一改
[02:19] 是SS是吧ISO C O C I T E是吧Words好了那这样的话就算是完了咱们检查一下VSS OC A T E没有问题点OK然后咱们在这就把它给删了删完之后这个就应该改了干啥呢好吧然后下面咱们就来把这个Map文件也拷过来这里边就是一个网络插群就一个插群
[02:54] 我考过来之后来看一眼啊比如说我现在要求一个like啊like啊也是加警号这是一个站位符是吧那这个是limit那你输入这个参数的时候应该是带两个什么版本号对吧在那版本号啊行那下面呢咱们就来继续往下写继续写那个呢就还是写咱们的Service那这Service呢其实还是在咱们之前那个Service去写就可以了叫什么呃AP article search Service就这好吗
[03:22] 这里边咱们再去定义一个方法这个方法咱们就叫做search associate好吧来response resultsearch associateassociat没问题没有实现然后这里边是goeser这不对是吧我看对不对对goeser search DTO好
[03:54] dto 还是 设置完之后咱们在这也去写一个注释好吧这是什么 连想词查询这样模糊查询 模糊查询行 那咱们下面就写它的实现它的实现是 搜索 给SS 加完之后咱们下面就来去写当前接口写当前实现率首先你还得去
[04:31] 不用想先去把当前那个什么前这个东西买回是不是注意来叫APAPASOISOCETWORDS是吧好出来之后呢咱们在这去注入完之后呢咱们就可以去查询了啊查询之前呢咱们首先的还是得去判断这里边有条件啊条件的话呢是有第一个是关键词二个呢就是前的条数这条数咱们条数最好是控制一下修点什么
[05:01] get page size
[05:31] 然后下面是有什么APP还是找到当前的美举啊说你的参数啊有问题也可以说参数非法也行参数非法无效参数好吧咱们再往下看啊那这时候呢如果说这行过了之后那咱们就可以去查询啊查询的话就简单了啊直接有一个然后第一个
[06:04] 就是当前的dto中的什么好的words好的words然后第二只呢就是dto的什么adpagesize好最终咱们返回一个列表列表的话咱们就可以去创造目前的哪目前的response result里边response result然后点ok然后把它把它装进去是的好吧
[06:32] 这样的话咱们Service就算是写完了写完之后咱们就往下写啥呢就还是得去写当前的API是吧API的话咱们再去定一个方法public response result然后咱们叫做search outwards associateassist ok然后当前还是user search cto
[07:02] 完了啊用这个是连想词他寻连想词他寻啊行那这个加上之后呢其实里边还少了一步啊因为刚才说了啊就这块内容呢咱们在这啊应该呢需要给他加上什么呢加上一个百分号是吧这刚才忘加了啊就在这加上啊比如说这个呢是个模糊查询啊某种差距啊所以说你在这拼接一个字母份嗯呀然后在后边呢再去加一个啊是啥呢
[07:37] 前面也是百分号这样就没问题了API写完之后咱们就可以写controllercontroller直接点进去就可以在这写了叫search好加完之后咱们就在这就可以去输入是吧直接用它就可以查询好DTO装进去完事了当然这里边还要写叫什么postmyping这里边咱们写啥
[08:10] 写写的呢其实跟也是根据当前的东西去查询我们叫ISOSOSO反过来啊这个笔记保持一致的啊好了这样的话咱们就写完了啊写完之后呢在这还要再去加一个啊写完之后咱们在这再去测试一下啊去测试吧测试的话呢咱们找到这关系的测试类好拷贝一份拷贝一份之后呢咱们那咱们图要是传啥值呢这样啊
[08:46] 这个咱们还要再去写这叫啥考过来s大写当前的这个东西路径咱们也要改路径的话其实是这个路径好那就改完了主要是看你传什么参数咱们还是dto.什么咱们首先来设置一个什么setpagesize比如说20咱们就差20条再一个就是你设置一个关键词关键词的话就是设置一个什么
[09:21] 比如说咱们去搜一个什么黑码有黑码啊因为这里边是不是有黑码呀大家看数据了其实里边有黑码啊有黑码什么大黑码广州黑码还有黑码成语言啊这样的话他应该是搜出来三条数据才对行吧那咱们一会来测一下看看效果好稍等正在加载啊这每次加载都很慢啊大家一定要耐心等着
[09:57] 好完了啊完了之后呢咱们可以看一下这个数据啊这个数据的话是不是拿到了你看当前黑马程序员上海黑马程序员还有广州黑马程序员是不是都拿到了当然如果说你要是去查传志啊就只查这两个字他也能去搜到当前的传志播客因为目前的话就是啥呢就是模糊查询对吧行那目前咱们这个接口啊就是当前那个什么查询联想词的接口咱们就说到这里啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现文章搜索功能，包括控制器测试、实体类、MyBatis Mapper 映射文件、服务层逻辑和单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 画面显示 IntelliJ IDEA 中的测试类 ArticleSearchControllerTest。
- 代码：`public void testHotKeywords() throws Exception { UserSearchDto dto = new UserSearchDto(); dto.setHotDate("2019-06-24"); MockMultipartRequestBuilder builder = MockMvcRequestBuilders.post("/api/v1/article/search/load_hot_keywords").contentType(MediaType.APPLICATION_JSON_VALUE).content(Mapper.writeValueAsBytes(dto)).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print()); }`
- 测试结果：Tests passed: 1 of 1 in 148ms。

画面 2:
- 画面显示 UserSearchDto 类的定义，包含字段如 equipmentId, searchWords, tag, hotDate, pageNo, pageSize。

画面 3:
- 画面显示 ApAssociateWordsMapper.xml 文件内容，包含 resultMap 和 sql 标签。
- 代码：`<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleConfig"> <result column="id" property="id"/> <result column="is_comment" property="isComment"/> <result column="is_forward" property="isForward"/> <result column="is_down" property="isDown"/> <result column="is_delete" property="isDelete"/> </resultMap> <sql id="Base_Column_List"> id, article_id, is_comment, is_forward, is_down, is_delete </sql> <select id="selectById" resultType="com.heima.model.article.pojos.ApArticleConfig" parameterType="int"> select <include refid="Base_Column_List"/> from ap_article_config where article_id = #{id} </select>`

画面 4:
- 画面显示 ApAssociateWordsMapper.xml 文件内容，包含 resultMap 和 sql 标签。
- 代码：`<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApArticleConfig"> <result column="id" property="id"/> <result column="is_comment" property="isComment"/> <result column="is_forward" property="isForward"/> <result column="is_down" property="isDown"/> <result column="is_delete" property="isDelete"/> </resultMap> <sql id="Base_Column_List"> id, article_id, is_comment, is_forward, is_down, is_delete </sql> <select id="selectById" resultType="com.heima.model.article.pojos.ApArticleConfig" parameterType="int"> select <include refid="Base_Column_List"/> from ap_article_config where article_id = #{id} </select>`

画面 5:
- 画面显示 ApArticleSearchServiceImpl.java 文件内容，包含 hotKeywords 和 searchAssociate 方法的定义。

画面 6:
- 画面显示 ApArticleSearchServiceImpl.java 文件内容，正在编辑 searchAssociate 方法。
- 代码：`public ResponseResult searchAssociate(UserSearchDto dto) { if (dto.getPageSize() > 50 || dto.getPageSize() < 0) return null; }`

画面 7:
- 画面显示 ApArticleSearchServiceImpl.java 文件内容，正在编辑 searchAssociate 方法。
- 代码：`public ResponseResult searchAssociate(UserSearchDto dto) { if (dto.getPageSize() > 50 || dto.getPageSize() < 0) return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID); return null; }`

画面 8:
- 画面显示 ApArticleSearchServiceImpl.java 文件内容，正在编辑 searchAssociate 方法。
- 代码：`public ResponseResult searchAssociate(UserSearchDto dto) { if (dto.getPageSize() > 50 || dto.getPageSize() < 0) return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID); apAssociateWordsMapper.selectByAssociateWords(dto.getSearchWords(), dto.getPageSize()); return null; }`

画面 9:
- 画面显示 ArticleSearchControllerApi.java 文件内容，包含 clearUserSearch 和 loadHotKeywords 方法的定义。

画面 10:
- 画面显示 ArticleSearchControllerApi.java 文件内容，包含 clearUserSearch 和 loadHotKeywords 方法的定义。
- 代码：`@PostMapping("/clear_search") public ResponseResult clearUserSearch(UserSearchDto dto) { return aparticleSearchService.clearUserSearch(dto); } @PostMapping("/load_hot_keywords") public ResponseResult hotKeywords(@RequestBody UserSearchDto dto) { return aparticleSearchService.hotKeywords(dto.getHotDate()); }`

画面 11:
- 画面显示 ArticleSearchControllerTest.java 文件内容，测试代码与画面 1 相同。

画面 12:
- 画面显示 ArticleSearchControllerTest.java 文件内容，正在编辑测试代码。
- 代码：`MockMvcRequestBuilders.post("/api/v1/article/search/associate_search").contentType(MediaType.APPLICATION_JSON_VALUE).content(Mapper.writeValueAsBytes(dto)).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print());`

画面 13:
- 画面显示测试结果，测试通过。
- 代码：`ArticleSearchControllerTest > testSearchAssociate()`

画面 14:
- 画面显示 ApAssociateWordsMapper.xml 文件内容，包含 resultMap 和 sql 标签。
- 代码：`<resultMap id="BaseResultMap" type="com.heima.model.article.pojos.ApAssociateWords"> <id column="id" property="id"/> <result column="associate_words" property="associateWords"/> <result column="created_time" property="createdTime"/> </resultMap> <sql id="Base_Column_List"> id, associate_words, created_time </sql> <select id="selectByAssociateWords" resultMap="BaseResultMap"> select <include refid="Base_Column_List"/> from ap_associate_words where associate_words like #{searchWords} limit #{limit} </select>`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
（已在上文第 2 点中完整列出）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 或架构图/流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

