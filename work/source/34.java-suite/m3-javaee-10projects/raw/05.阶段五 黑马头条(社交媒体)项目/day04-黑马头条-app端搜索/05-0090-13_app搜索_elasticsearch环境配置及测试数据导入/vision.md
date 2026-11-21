# 画面线理解：13_app搜索_elasticsearch环境配置及测试数据导入

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day04-黑马头条-app端搜索
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day04-黑马头条-app端搜索\13_app搜索_elasticsearch环境配置及测试数据导入【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:48, 01:39, 02:28, 03:11, 04:07, 04:34, 05:12, 05:57, 07:11, 08:05, 08:24, 09:11, 10:58, 11:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:35:38

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
    <groupId>org.elasticsearch</groupId>
    <artifactId>elasticsearch</artifactId>
    <version>7.2.0</version>
</dependency>

画面3：
spring.elasticsearch.jest.url=http://localhost:9200
spring.elasticsearch.jest.read-timeout=20000
spring.elasticsearch.jest.connection-timeout=20000

画面4：
@Configuration
@ConfigurationProperties(prefix = "spring.elasticsearch.jest")
@PropertySource("classpath:elasticsearch.properties")
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
@ComponentScan({"com.heima.elasticsearch"})
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
