# 画面线理解：11_app文章详情_文章内容接口_使用mockmvc文章内容接口测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\11_app文章详情_文章内容接口_使用mockmvc文章内容接口测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:40, 02:41, 03:55, 05:02, 06:00, 06:46, 07:44, 08:17, 08:51, 09:53, 10:41, 11:21, 12:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:12:33

1) 这一组画面整体在讲如何为 Spring Boot 项目中的 ArticleInfoController 编写并执行单元测试，重点演示了使用 MockMvc 模拟 HTTP 请求并验证服务层逻辑。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 ArticleInfoController.java 中的 @PostMapping("/load_article_info") 方法，用于加载文章信息。
画面 2: 展示 ArticleInfoControllerTest.java 的测试类，使用 @SpringBootTest(classes = ArticleJarApplication.class) 和 @RunWith(SpringRunner.class) 注解。
画面 3: 展示测试类中使用 @AutoConfigureMockMvc 注解，用于配置 MockMvc。
画面 4: 展示测试类中导入 MockMvc 和 MockMvcRequestBuilder 等类。
画面 5: 展示测试方法 testLoadArticleInfo() 中创建 ArticleInfoDto 对象并设置 articleId。
画面 6: 展示测试方法中使用 MockMvcRequestBuilders.post() 构建 POST 请求。
画面 7: 展示测试方法中使用 .content(mapper.writeValueAsBytes(dto)) 设置请求体。
画面 8: 展示测试方法中使用 mvc.perform(builder) 执行请求。
画面 9: 展示调试器中 ArticleInfoController 的方法执行过程，参数 dto 和 appArticleInfoService 被赋值。
画面 10: 展示测试执行后的控制台日志，包含 Hibernate 初始化信息。
画面 11: 展示测试执行成功后的控制台输出，显示响应状态码 200 和响应体。
画面 12: 展示 AppArticleInfoService.java 中的逻辑，根据 articleId 查询配置信息。
画面 13: 展示测试执行后的控制台日志，包含 Hibernate 初始化信息。
画面 14: 展示测试方法中设置请求体的代码，使用 .content(mapper.writeValueAsBytes(dto))。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
@RestController
@RequestMapping("/api/v1/article")
public class ArticleInfoController implements ArticleInfoControllerApi {

    @Autowired
    private AppArticleInfoService appArticleInfoService;

    @PostMapping("/load_article_info")
    public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
        return appArticleInfoService.getArticleInfo(dto.getArticleId());
    }
}
```

画面 2:
```java
package com.heima.article.controller.v1;

import com.heima.article.ArticleJarApplication;
import org.springframework.boot.test.context.SpringBootTest;
@RunWith(SpringRunner.class)
@SpringBootTest(classes = ArticleJarApplication.class)
public class ArticleInfoControllerTest {

}
```

画面 3:
```java
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

@RunWith(SpringRunner.class)
@SpringBootTest(classes = ArticleJarApplication.class)
@AutoConfigureMockMvc
public class ArticleInfoControllerTest {

}
```

画面 4:
```java
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
```

画面 5:
```java
public void testLoadArticleInfo() {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

画面 6:
```java
public void testLoadArticleInfo() {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

画面 7:
```java
public void testLoadArticleInfo() throws Exception {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

画面 8:
```java
public void testLoadArticleInfo() throws Exception {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

画面 9:
```java
public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
    return appArticleInfoService.getArticleInfo(dto.getArticleId());
}
```

画面 10:
```java
2019-09-19 19:23:37,833 | INFO  | main | org.hibernate.jpa.internal.util.LogHelper | logPersistenceUnitInformation | HHH000224: Processing PersistenceUnitInformation
name: default
```

画面 11:
```java
Attributes - null
MockHttpServletResponse:
Status - 200
Error message - null
Headers - {Content-Type=[application/json;charset=UTF-8]}
Body - {"host":"null","code":"0","errorMessage":"操作成功","data":{"id":1,"articleId":1,"isComment":true,"isForward":true,"isDown":false}}
Redirected URL - null
Cookies - []
```

画面 12:
```java
//根据文章id查询配置信息
ArticleConfig apArticleConfig = apArticleConfigMapper.selectByArticleId(articleId);
if (apArticleConfig == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
} else if (apArticleConfig.getDelete()) {
    ArticleContent apArticleContent = apArticleContentMapper.selectByArticleId(articleId);
    String content = ZipUtils.gunzip(apArticleContent.getContent());
    data.put("config", apArticleConfig);
    data.put("content", content);
    return ResponseResult.okResult(data);
}
```

画面 13:
```java
2019-09-19 19:25:49,814 | INFO  | main | org.hibernate.Version | logVersion | HHH000012: Hibernate Core (3.3.10.Final)
```

画面 14:
```java
public void testLoadArticleInfo() throws Exception {
    ArticleInfoDto dto = new ArticleInfoDto();
    dto.setArticleId(1);
    MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
            .contentType(MediaType.APPLICATION_JSON_VALUE).content(
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
