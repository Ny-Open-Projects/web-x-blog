# day10-5-标的信息检索-内容检索服务-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-5-标的信息检索-内容检索服务-功能实现1_【海量资源尽在 666java.com】.mp4
- 时长 18分2秒（音频 1082s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把接口定义好接下来呢咱就创建该接口的实现类最终呢实现标底的检索功能这个功能呢编码起来还是比较麻烦的大家可以看一下这个代码非常多因为呢我们是通过Elasticsearch的官方API实现了它这个API使用起来不是那么的间接有点麻烦那咱接下来先把这个实现类创建一下咱找到Service
[00:32] 然后再拗一个类啊这个名字呢我们跟蒋艺宝是一致project index Service ampere然后呢先在这加一个注解吧at什么呀Service然后呢他要实现谁啊对我们前面定义的那个接口叫project index Service为什么还会报错呀因为是不是里边有个方法我们要重写是不是好我们把这个方法生成一下
[01:09] 就是这个方法那在具体编码实现这个检索功能之前呢我们需要先注入两样东西哪两个东西呢大家看一看这两个东西都是咱一会要用的第一个就是这个核心对象这个谁啊这扣端对吧我们使用的是高级别的这个扣端这也是官方推荐使用的要把它注进来它是不是在那个配置类当中我们前面是不是在配置的类当中已经给它配好大家瞅一眼在这是它吧
[01:40] 对不对这不是并注解吗所以说我们就可以通过automobile把它注进来然后还要注意一个东西这东西and value注解大家应该能猜到这个值是在哪里这个值是不是在Apollo上是不是咱可以去Apollo上瞅一眼登一下Apollo我们是配到内容检索微服务里边当时让大家瞅过最下面Spring Boot es
[02:08] 这里边呢我们配了一个叫万信p2p.es.index这个我们当时给大家介绍过这是咱索引库的名字是不是这就是咱索引库的名字因为我们在进行查询检索的时候一定是要知道这个索引库的名字嘛而这个名字呢我们是配到Apollo里边所以我们这可以通过add value注进把它给注进来这样比较灵活所以说呢我们首先要先注入这俩东西相当于是一个准备工作吧好我们先注入一下
[02:43] 这个呢没导进来咱自己手动的导一下包然后接下来的话咱就回到这个方案里边开始编码实现标的检索功能刚才让大家瞅了眼这个功能最终编写出来的代码是比较多对吧所以咱接下来要拆分拆分步骤一点一点来编写这是咱之前给大家强调过的一些经验教训是不是那咱大概要分成八个步骤
[03:15] 因为咱前面刚才给大家说了这个Elasticsearch官方的这个API使用起来不简洁编写代码会比较麻烦都拿8个步骤咱接下来一个一个来第一步我们先创建整体的一个搜索请求对象这是我们的核心对象将来就指望他来干什么来进行检索查询所以我们先把这个核心对象先创建出来第二步就是
[03:49] 我们先针对什么呀搜索条件来进行封装啊搜索条件其实这些步骤啊你可以看这个方法的参考就行了你看这个方法参考里边你看我们前面说过这个DTO这里边不就是条件吗然后接下来后边这里啊是什么呀对分页的数据再往后这俩是什么呀排序的数据反正你这个步骤里边肯定是有这几步的那你看咱第二步其实就是封装这个条件的
[04:22] 那第三步呢我们看看第三步第三步的话我们要创建又一个核心对象啊创建什么核心对象叫SEARCH SEARCH S O U R C E B U I L D R对象这个对象啊是总的一个封装的一个对象啥意思呢就是这个对象他要封装这个条件就是你最终封装好的条件要放到这里边
[04:55] 而且他还要封装啥对他还要封装排序的信息还要封装分野的信息他是一个总的一个封装对象啊我在这给你写一下总的封装对象这里边都可以封装啥呀来我你累一下所有东西都要封装到他这里边可以封装条件还要封装啥对还可以设置也就是封装的意思设置排序参数对不对还要干什么呀
[05:31] 还剩下谁啊对还要设置什么呀对分页参数所有的这些东西最终全是放到了谁呀search source builder这个对象那我们接下来就有一步就是完成封装完成全部的一个封装那该封装的都封装好了接下来该干嘛那接下来其实就该执行搜索执行搜索就是从ES的索性库里边开始产生数据了
[06:08] 那搜索执行完之后接下来无非就是该拿到结果了是不是所以说接下来就是在获取搜索的什么呀结果就拿到结果拿到结果之后呢拿到结果之后呢我们要循环封装因为你查询出来的数据有可能多条嘛所以我们要循环封装成DTO对象
[06:39] 因为你通过Elasticsearch本身的API查出来的东西它肯定不可能直接就是咱想要的这个什么呀对DTO对象不是的所以我们得便利它的这个结果然后我们人工的去把它封装成我们想要的什么呀对DTO对象封装好之后呢最后一步最后一步了啊就是还要再封装啊封装成什么呀封装为我们最终要的是配给VO嘛是不是最终是要封装为配给VO
[07:10] 对象并返回返回谁啊返回给交易中心嘛是不是因为是交易中心远程调用的什么内容检索服务所以说我们这边执行完最终这个结果是要返回给交易中心的所以你看我们这个功能实现起来就有点麻烦一共我们给它拆分成了八个步骤咱接下来一点一点来编写这个代码就行了首先呢就是第一步我们说了要创建搜索请求对象
[07:39] 这个对象的将来在执行的时候执行搜索的时候就要用但是我们需要提前先创建那这个对象怎么创建呢我们直接六就行了六哪个类呢叫search requestsearch就这个search request直接拧那在六的时候呢你需要调用他的代三构造啊这个参数呢其实就是呃所有库的名字就是你得告诉他你要查哪个库
[08:12] 或者说你要从哪个库里边查询数据我们是不是把这个库的名字注入到这个projectindex这个属性里面所以说你把它往这一放就OK了这就是第一步啊这叫请求对象然后接下来第二步第二步我们说了是不是主要是针对这个条件进行封装就是dtu对象里边是不是要对他进行封装那这个条件怎么进行封装呢这个跟之前我们从数据库查询这个逻辑是一样的
[08:41] 我们是不是要把这里边条件取出来挨个做非空判断对吧凡是不为空的我们就要把它封装成条件将来进行查询如果这个是直是空的那证明客户就不想按照这个条件进行查询那我们就不对他进行什么呀封装所以这个逻辑差不多但是API肯定不一样那这里边的话第一步我们要先创建条件封装对象
[09:10] Elasticsearch的API里边有专门一个对象是封装什么条件我们这样采用的对象是叫BoolqueryBuilderBoolqueryBuilderBool叫什么BoolqueryBuilder就是它这个对象我们不是Nu出来的不是Nu出来是通过一个类的一个静态方法叫
[09:40] query builders就是他他有个方法就是不玩query就是他那么这个专门封装条件的对象我们就造出来造出来之后怎么办呢是不是就该往这里边封装条件了那都封装哪些条件呢我们说了是不是要判断DCO对象里边谁不为空对吧不为空的就是条件我要往这里边放所以接下来这一步就是2.2的是不是2.2就是干什么呀对非空判断
[10:14] 飞空判断并封装条件那么怎么进行飞空判断呢无非还是用我们以前说的string youtube对吧他的一些方法来从这里边取出来属性的值挨个进行判断就行了所以说这里边要用什么if那这里边就是stringstring youtube我们用阿帕奇的这个是吧就他就行啊有一个方法叫咱以前用过叫is not
[10:49] blank对没错那判断谁呢条件我们是不是都在这个DTO对象里边你就从这里边取呗咱挑几个啊因为这个条件太多了啊我这里边就挑两两三个给大家演示一下就行了点我们比如说我们可以根据标的名字吧进行一个查询是不是那如果名字不为空那我接下来是不是这个名字就要作为条件是不是封装到这个对象里边
[11:17] 那这里边怎么封装呢我们需要调用他的一个master然后我们这个条件应该是什么样呢我们的条件应该是名字等于谁吗哎这个呢跟数据库不太一样我们前面学过Elasticsearch我们这个地方应该用什么查询是不是叫termquery就是词条查询是不是啊词条叫termquery那咱接下来就走一下这个termquery啊就是curb builders.
[11:48] 你看这里边它是封装好了各种各样的查询我不知道大家还有没有印象你像这个term query就是词条查询是不是包括这个是范围的查询是不是还有其他咱之前都学过哪些查询是不是还有分词查询是吧match query对吧等等等等那咱这儿呢这个地方我们应该用term query因为咱前面在搭建环境的时候给大家说过这个内幕这个字段我们是不是进行分词了是不是用ik分词记分词了所以我们这儿呢就进行这个term query就是词条查询就行了
[12:17] 那我要查询的字段这个名字就叫什么呀内幕值呢值不就是DTO对象里边取出来这个值吗是吧这个代码就这么写啊大家瞅一眼啊那如果这个内幕的值不为空就证明客户想按这个进行查询那我就应该把它封装成条件这个条件是什么样呢就是我要根据内幕字段来进行什么查询啊term啊就是词条查询那么值呢是这个值
[12:48] 然后呢就封装到这个宽儿标的这个对象里面那咱接下来再加点条件吧这个田你自己看看家啊呃我在这再给你挑个那个什么呀挑个那个然后你挑一个咱将来肯定能用到的一个字段就这个字段你找一找就是这个字段这个字段不知道大家有没有印象他是什么意思啊就是借款的期限
[13:22] 就是你是借一年借两年或者借多少个月这是期限所以说我们接下来准备呢把它当成一个条件也用一用那这个条件大家想一想它应该就是一个范围的一个查询对不对比如说12个月到24个月的对不对或者12个月到36个月是不是大家现在看到这个值360啊它的单位是天它在存储数据的时候呢是换算成天数了
[13:50] 360天不就是12个月吗总之啊这个查询的话一定是根据一个什么范围就是多少个月到多少个月这个来进行搜索我们把这个功能给它架上就这个条件给它架上就是范围的一个查询那这个我们首先是不是也要进行非空校验那需要校验哪几个值呢咱去DTO对象里边瞅一瞅吧DTO对象里边它应该有两个属性的值吧你看这一个是star一个是ind对吧
[14:22] 那比如说就是比如我借款借60天到360天是不是这就是一个范围一个查询那我们现在是不是这两个值都要进行盘了对不对那调他的给他放那就行那就是一副什么呀对一副还是从DQ对象里边取吗get star他对不对那我是怎么判断他违不违空呢刚才你也看到了他是自补串吗你看这
[14:53] 不是自然他已经可以给是吧那我这应该怎么判断不等于闹就行是不是这就不为空那如果不为空的话我是不是应该把它做条件封装到curbuda里边对吧这个代码怎么写那就是curbuda.还是什么呀must然后这里边我们做的就不是term query而是一个范围查询就是认记query那应该怎么写就是curry builder不是他curry builders.rang query
[15:26] 这是一个范围的一个查询那我们查询的这个字段名就叫刚才我们说了叫啥名我们给它粘过来吧不是这个名字啊我们应该对照这儿看这边P I O D这个名字啊P I O D这个名字这是我们要查哪个字段那条件是啥呢是大于呢还是什么呀小于呢对不对无非就是这两种或者大于等于小于等于都可以对不对
[16:00] 那我们这儿我们这个地方应该是用大于还是小于还是大于等于小于等于呢大家看我们这儿是star是不是其实的那个那个天数对不对那其实的天数我们应该是用大于或者说大于等于没错吧所以我们接下来继续调用它的方法调用哪个方法呢我们调用这个谁啊GTE了这个GTE应该是大于等于值是哪个值呢那还是从DTO对象里边取出来这个值就
[16:32] 行了这个值这就是我们又封装进去是不是一个条件对吧那接下来这个结束的这个值是不是跟他一样我们粘过来这改一改呗这要调用给他in的点get in那下面这些地方的话我们也要改一改那这我们不用动了啊然后呢这是不是也得改一改是不是
[17:12] 方法换一下其他的应该就不用管哎这还得改这就不能是什么呀大于等于了应该是什么呀小于等于小于等于是LLTLT这是几个条件啊三个条件了对不对那还加不加了不加了吧因为这个DTO里边的属性太多了你想加的话你下去可以参考这个咱现在的这个代码自己加一些自己测测测也是可以的咱这呢就暂时先不加了
[17:46] 这是我们现在把什么把条件这一块全部封装好那咱一会接着要封装什么排序分页还要完成封装执行搜索咱一会单独再编写一下这些代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Elasticsearch 的 RestHighLevelClient 构建项目搜索功能，包括配置、构建查询条件、分页和结果封装。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`@Autowired private RestHighLevelClient restHighLevelClient; @Value("${wanxingzp.es.index}") private String projectIndex; public PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortby, String order) { //1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 2：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`public class ProjectIndexServiceImpl implements ProjectIndexService { }`

画面 3：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`import cn.itcast.wanxingzp.api.search.model.ProjectQueryParamsDTO; import cn.itcast.wanxingzp.api.transaction.model.ProjectDTO; import org.springframework.stereotype.Service; @Service public class ProjectIndexServiceImpl implements ProjectIndexService { }`

画面 4：
- 展示了 Apollo 配置中心的界面。
- 配置项：`micro_service.spring-boot-es` 的 `wanxingzp.es.host` 值为 `127.0.0.1:9200`，`wanxingzp.es.index` 值为 `wanxingzp_project`。

画面 5：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`@Autowired private RestHighLevelClient restHighLevelClient; @Value("${wanxingzp.es.index}") private String projectIndex; public PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortby, String order) { //1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 6：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`//1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 7：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`private RestHighLevelClient restHighLevelClient; @Value("${wanxingzp.es.index}") private String projectIndex; public PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortby, String order) { //1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 8：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`private RestHighLevelClient restHighLevelClient; @Value("${wanxingzp.es.index}") private String projectIndex; public PageVO<ProjectDTO> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortby, String order) { //1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 9：
- 展示了 Elasticsearch 的 Head 界面。
- 显示了索引 `wanxingzp_project`，状态为 `green`，文档数量为 418。

画面 10：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectQueryParamsDTO.java` 文件。
- 代码内容：`@ApiModelProperty("标的名称(分词匹配)") private String name; @ApiModelProperty("标的描述(分词匹配)") private String description; @ApiModelProperty("起止标的期限(单位:天)") private Integer startPeriod; @ApiModelProperty("起止标的期限(单位:天)") private Integer endPeriod; @ApiModelProperty("起止年化利率(投资人视图)") private BigDecimal startAnnualRate; @ApiModelProperty("起止年化利率(投资人视图)") private BigDecimal endAnnualRate; @ApiModelProperty("标的的状态") private String status;`

画面 11：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`//1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 12：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`//1.创建搜索请求对象 SearchRequest searchRequest = new SearchRequest(projectIndex); //2.1.搜索条件 BoolQueryBuilder queryBuilder = QueryBuilders.boolQuery(); //2.2.非空判断并设置条件 if (StringUtils.isNotBlank(projectQueryParamsDTO.getname())) { queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getname())); } if (projectQueryParamsDTO.getStartPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod())); } if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } }`

画面 13：
- 展示了 IDE 中的项目结构，当前选中的是 `ProjectIndexServiceImpl.java` 文件。
- 代码内容：`if (projectQueryParamsDTO.getPeriod() != null) { queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getPeriod())); } //3.创建SearchSourceBuilder对象——封装对象 SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder(); //3.1.设置查询条件 searchSourceBuilder.query(queryBuilder); //3.2.设置分页参数 searchSourceBuilder.from(pageNo).size(pageSize); //3.3.

