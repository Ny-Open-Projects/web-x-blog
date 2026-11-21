# 13_app搜索_elasticsearch环境配置及测试数据导入

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\13_app搜索_elasticsearch环境配置及测试数据导入【海量资源尽在 666java.com】.mp4
- 时长 11分23秒（音频 684s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来完成文章搜索接口这是最后一个接口啊但是接口之前呢在说这个接口之前呢咱们还要再去说一个问题就是当前的有一个ES就是Elasticsearch那这个东西呢咱们需要先去准备好当前的环境才能用首先呢你要在你的电脑上或是说说在你这个开发的环境里边呢去安装当前的什么一个是ES另外一个是Keybinder
[00:28] 这两个当然可以不安装没有问题但这个东西你必须安装好吧那这个安装的过程我就不再去讲了不得去讲了因为咱们之前的课上都已经讲过了然后下面咱们就直接去说当前的在本项目中集成的过程好了那这个环境你要先启动起来比如说你看我这已经启动了当前的ES跟当前的Keybanner好了然后下面咱们就在项目中该怎么去用其实咱们用的一个是JS的Client
[00:58] 然后用它呢去连接咱们的ES的索引库好吧那首先呢你要把这个包啊给包倒进去啊倒进去倒进去之后呢那这个目前呢给你们发的环境里边其实这个两个包已经倒进去了你不用管咱们主要是去集成其他技术技术的时候咱们说了都要在common中模块中去设置好那咱们下面呢就来一步一步去把它给设置设置一下首先呢你要去创建一个以lastic设置的proportis文件在哪啊
[01:28] 在当前的comment,就都把它关掉在当前的comment包下边这有一个resource,当前文件然后你把当前的连接伺服券放进去这个券其实大家需要改的地址就这一处如果说你安装到本地的话那就是localhost它默认是9200我这个是安装到本地所以说我就用这个地址如果说你安装到了什么
[01:57] 比如说你按照那讯息或者说某一台服务器上那就把这个地址给改一改就可以了好吧行那这个加完之后咱们下面还有一个配置类需要去设置这个配置类咱们也会再去在哪在哪设在comment包下边是写错了咱们就在comment包下边去创建一个Elasticsearch来去找到当前的comment然后在这去创建一个comment下面的什么呢这么一个配置类吧
[02:35] 好那这样的话就算是创建了一个类那这类呢其实是一个配置类所以说呢这个代码咱们就直接考过来简单说一说啊考一下然后呢还有上面的一些配置咱们要考一下啊这个咱们之前都写过了一次代码啊好首先呢这是一个date这是longbook的date是吧然后它是一个配置类然后呢它是这个前缀哪个前缀呢就是当前配置文件这个前缀其实就是就是它啊就是它啊因为对前缀是不是都是都是这东西啊是吧
[03:11] 然后呢然后是去设置了三个URL三个属性吧这三个属性应该都是从这去读的啊然后最终呢咱们是创建了一个DISTCLANT那这个CLANT呢就可以去连接咱们的ES可以连接ES啊在这里边需要去有些参数这个参数的话呢都是从这去读的这是URL还有连接的超市市场多取到超市市场咱们都可以去设置啊
[03:37] 行那这个还加了一个艾特并那这样的话就是当服务启动的时候把当前配置类给加进来之后呢就能在死位容器中找到当前那个JS是吧那这样的话咱们就可以去连接咱们的ES的随意库了啊行那这个加完之后啊嗯还没有完啊最终最终的咱们这个comment是通用的在哪个工程下边想去用的话呢你需要在哪个工程下边去把它给干嘛呢
[04:05] 说实话了说实话的过程其实很简单就是说你在每一个每一个config里边去创建一个esconfig去加载就可以了比如说咱们article里边需要那就在这去加就可以了比如说打开这config esconfig我这有你看它就是这么简单的一句话就这么简单的一句话这样的话就只要是把这个包给扫描到了就可以了好吧
[04:32] 那行那这个咱们讲完之后呢你再去使用的时候你直接去注入当前这个JS Client就可以了好吧行那这个环境啊咱们就说到这啊那环境说完之后呢下面还有一些东西咱们还要再去说一说啊首先呢这是有一个KeybannerKeybanner一个索引库还有映射的创建那这个呢你只要是去创建启动了当前的这种ES库和Keybanner之后呢你就可以用打开这啊打开Keybanner稍等
[05:03] 你打开它之后呢你就可以去创建你的索引你看我这已经创建索引了创建索引之后呢并且是设置了一些映射你直接考过来用一下就可以了但这个这里边的词呢我简单说一说简单说一说你看比如说channel id是吧content还有id还有一些发布时间还有一些查询相关的东西但还有一些什么状态和tag状态和tag还有啥呢还有title
[05:30] 就是文章的信息然后最终还有user id其实这个呢都是一些文章相关的东西因为咱们目前的话创建缩影只有一个缩影库这个缩影库呢就是当前的ap info article就是文章相关的一些信息咱们会放到缩影库供查询的时候去能够返回结果就那么多作用啊但这个数据的话呢还要再去说一说这个数据啊你需要去准备好我先走啊然后你创建完缩影之后呢这时候呢缩影库有了你需要去准备你的
[05:59] 这种数据准备数据准备数据之前咱们这边还有一个配置咱们再说一说配置咱们实际咱们再去放进来所以的时候是扔了三块所以但是目前的话只用到了一块我简单说一说为了方便后期扩展性更强所以说咱们可以在这去设置比如说我们现在是文章所以叫APP info article用户是叫user作者是叫author是吧
[06:26] 当然你要是去设置的时候呢你也可以按照比如我下去这三库都三个户都查咱们就查这个定义的长量啊但是我要去定义的某一个户的话那你就是查这个东西但第一个呢第一个是文章的类型目前的话都有默认的就可以了因为这个气上的这个类型的已经不再去使用了啊所以说咱们用默认值杠Doc就可以了好吧行那咱们下面就可以把当前的这个长量啊给定义一下啊这长量的也是在哪定义啊
[06:56] 也是在constance这里边去定义所以说咱们在这直接去拷贝一下拷贝到common下面这你直接考到这就可以了common下面有个constance考到这这样的话咱们查量就算是设置完了下面刚才说了就需要你去准备数据准备数据其实非常简单的就无非你就是去查先去查文章从白色文章去查查完之后你再去重新插入到哪
[07:34] 插入到你的当前的索引库就完了那我这块这个代码我已经写完了啊这个代码啊嗯这里边大家可以去拷贝过去去用一用就可以了但这个呢只是今天测试会用一下后期的话咱们去审核文章的时候呢还会再去自动的去往索引库中去添加啊自动啊咱们也可以看一下这个代码啊那个代码呢首先呢这会去封装了一个叫es index entity
[08:02] 那这样也行咱们先看下弹板也行这个弹板的话其实就在当前的article里边我这删了是吧在测试里边打开ES test打开其实就是这个弹板就是我已经到考了笔记上了这无所谓首先你看首先这是有一个注入了三个东西注入了三个东西哪三个东西第一个是JAS client是连接ES的还有是
[08:32] AAP article Mapper这是为了查询文章的这是查询文章内容的好了啊然后再往下看啊最终呢咱们是去要首先呢要去把文章的信息给查出来这个咱们之前的方法是写过的啊所以说我是设置两个参数目前只插入了50条数据OK啊这个查出来之后呢它并没有文章内容所以说呢我又通过data id呢去查了一个文章的内容最终是又去创建了一个对象这个对象呢是不断的去
[09:01] 往当前这个里面去放这里面放这个对象呢其实就是去干嘛呢就是去我可以去创建对象创建所以应该是创建所以啊行那这个对象啊这个对象的话就是又去新创建了一个这种es index entity这个对象那这个对象呢可以看看啊他就是门用来去插入所有的一个这样又重新封装了一个对象啊比如id啊content什么channel id是吧publish time
[09:31] 还有什么cdc title user id和tag好吧大家呢可以拷贝过来然后是方便测试就可以但是这些词呢大家也能够看明白啊比如说content是吧就不用说了content就是内容channel id就是频道id这个是发布时间这是状态这是标题这是运行id这个tag呢我要简单说一说这个tag的话就能区分当前文章到底是文章还是呃其实这样这个tag是这样啊
[09:58] 不是说文章因为都是文章目前的这个是来区分到底是从你的爬床爬过来的文章还是我的自媒体发布的文章这个是咱们用来做标识用的我这块目前的话没有标识就只是写了一个article只是写了article行那这个咱们后期去爬文章的时候或者再去发布章的时候咱们再去设置目前的话其实你设置的这些东西就已经够用了
[10:26] 好吧最终的这有一个JS client然后去执行一下index对index你需要去创建出来啊就是你的当前的什么就是你的当前的什么indexbuild index然后是你可以去设置当前的什么所以设置当前的什么当前的一个叫做类型啊文章类型这样的就可以了啊但是这个builder里边呢builder里边啊已经装入了当前的一个所以库啊就是当前的文档啊不知道所以库叫文档好吧
[10:56] 这一共是插入了50条好吧行那这个插完之后呢插入完之后啊你就可以去在这你可以去在这去查询一下目前我这里边是有50条文章啊50条文章为了咱们能够更好的更方便的去测试啊所以说我只插入了50条文章啊行那目前的话这个环境啊咱们都该说完的都说完了啊没问题了然后下面呢咱们就来完成当前文章搜索接口的开发好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中配置并使用 Elasticsearch，包括添加依赖、配置文件、创建配置类和编写测试代码。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程文档目录，当前章节为“4.6 文章搜索接口”，子章节“4.6.1 ES配置使用”，内容包括安装配置 Elasticsearch 和 Kibana 环境，以及在 common 项目中添加依赖。
画面2：在 IDEA 中右键点击项目，准备新建文件或目录。
画面3：展示在 resources 目录下创建 elasticSearch.properties 配置文件，内容包括连接地址和超时设置。
画面4：展示 ElasticSearchConfig.java 文件，其中使用 @ConfigurationProperties 注解绑定配置文件，并定义了 getJestClient 方法。
画面5：展示 ElasticSearchConfig.java 文件，代码中定义了 url、readTimeout、connectionTimeout 字段，并在 getJestClient 方法中配置了 HttpClient。
画面6：展示在 heima-leadnews-article 项目中创建 EsConfig.java 文件，内容为 @Configuration 和 @ComponentScan 注解。
画面7：展示使用 Kibana 创建索引的 PUT 请求，内容为 app_info_article 索引的 mapping 定义。
画面8：展示 EIndexConstants 类，定义了默认文档和索引名称常量，并说明了 ES 类型默认为 _doc。
画面9：展示在 article 项目中创建 EsConfig.java 文件，内容为 @Configuration 和 @ComponentScan 注解。
画面10：展示在 common 项目中打开 EIndexConstants.java 文件，内容为定义索引常量。
画面11：展示 EsTest.java 文件，定义了测试类和测试方法 testSave。
画面12：展示 testSave 方法中，创建 EsIndexEntity 对象并设置属性，然后使用 Index.Builder 构建索引并执行。
画面13：展示 testSave 方法中，如果执行失败则抛出异常。
画面14：展示课程文档目录，当前章节为“4.6.1 接口定义”，内容包括接口规范和请求路径。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
<dependency>
    <groupId>io.searchbox</groupId>
    <artifactId>jest</artifactId>
    <version>6.1.3</version>
</dependency>
<dependency>
    <groupId>org.Elasticsearch</groupId>
    <artifactId>Elasticsearch</artifactId>
    <version>7.2.0</version>
</dependency>

画面3：
spring.Elasticsearch.jest.url=http://localhost:9200
spring.Elasticsearch.jest.read-timeout=20000
spring.Elasticsearch.jest.connection-timeout=20000

画面4：
@Configuration
@ConfigurationProperties(prefix = "spring.Elasticsearch.jest")
@PropertySource("classpath:Elasticsearch.properties")
public class ElasticsearchConfig {
    private String url;
    private Integer readTimeout;
    private Integer connectionTimeout;

    @Bean
    public JestClient getJestClient() {
        JestClientFactory factory = new JestClientFactory();
        factory.setHttpClientConfig(new HttpClientConfig
                .Builder(this.url)
                .multiThreaded(true)
                .connTimeout(this.connectionTimeout)
                .readTimeout(this.readTimeout)
                .build();
        return factory.getObject();
    }
}

画面6：
@Configuration
@ComponentScan({"com.heima.Elasticsearch"})
public class EsConfig {

画面8：
public class EIndexConstants {
    public static final String DEFAULT_DOC = "_doc";
    public static final String ALL_INDEX = "app_info_";
    public static final String ARTICLE_INDEX = "app_info_article";
    public static final String USER_INDEX = "app_info_user";
    public static final String AUTHOR_INDEX = "app_info_author";
}

画面11：
@Test
public void testSave() throws IOException {
    ArticleDmDto dto = new ArticleDmDto();
    dto.setPageSize(50);
    dto.setTags("_all_");
    List<Article> aparticles = aparticleMapper.loadArticleListByLocation(dto, type: null);
    for (Article aparticle : aparticles) {
        ApArticleContent aparticleContent = apArticleContentMapper.selectByArticleId(aparticle.getArticleId());
        EsIndexEntity esIndexEntity = new EsIndexEntity();
        esIndexEntity.setChannelId(new Long(aparticle.getChannelId()));
        esIndexEntity.setArticleId(aparticle.getArticleId());
        esIndexEntity.setContent(UrlUtils.gzip(aparticleContent.getContent()));
        esIndexEntity.setPublishTime(aparticle.getPublishTime());
        esIndexEntity.setStatus(new Long(value: 1));
        esIndexEntity.setTag("article");
        Index.Builder builder = new Index.Builder(esIndexEntity);
        builder.id(aparticle.getArticleId().toString());
        Index index = builder.index(EsIndexConstants.ARTICLE_INDEX).type(EsIndexConstants.DEFAULT_DOC).build();
        JestResult result = jestClient.execute(index);
        if (result != null && !result.isSucceeded()) {
            throw new RuntimeException(result.getErrorMessage() + "插入更新索引失败！");
        }
    }
}

画面14：
接口规范：
请求地址：/api/v1/article/search/article_search
请求参数：com.heima.model.article.dtos.UserSearchDto

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT标题为“4.6 文章搜索接口”，子标题“4.6.1 ES配置使用”。
画面6：PPT标题为“使用Elasticsearch”，内容为“按需项目使用模块按需加载，我们使用ES只读数据库common配置ES目录”。
画面8：PPT标题为“EIndexConstants”，内容为“定义了默认文档和索引名称常量”。
画面14：PPT标题为“4.6.1 接口定义”，内容为“接口规范”和“请求地址”。

5) 不评价画面美观，不输出与课程无关的内容。

