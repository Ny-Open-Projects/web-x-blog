# 画面线理解：04_自媒体文章自动审核_aliyunAI_文本内容审核测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\04_自媒体文章自动审核_aliyunAI_文本内容审核测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:25, 00:47, 01:14, 01:49, 02:56, 03:29, 04:14, 04:46, 05:50, 06:26, 07:16, 07:40, 08:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:17:16

1) 这一组画面整体在讲如何使用阿里云的文本内容审核服务（TextScanRequest）进行文本检测，并在 Spring Boot 项目中集成和测试该功能。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示了在 IntelliJ IDEA 中编写 Java 代码，实现阿里云文本审核的请求逻辑。
- 代码片段：
  ```java
  private String secret;
  public String textScanRequest(String content) throws Exception {
      IClientProfile profile = DefaultProfile.getProfile("cn-shanghai", accessKey, secret);
      TextScanRequest textScanRequest = new TextScanRequest();
      textScanRequest.setAcceptFormat(FormatType.JSON);
      textScanRequest.setMethod(com.aliyuncs.http.MethodType.POST);
      textScanRequest.setEncoding("UTF-8");
      textScanRequest.setRegionId("cn-shanghai");
      List<Map<String, Object>> tasks = new ArrayList<Map<String, Object>>();
      Map<String, Object> task1 = new LinkedHashMap<String, Object>();
      task1.put("dataId", UUID.randomUUID().toString());
      // 待检测的文本，长度不能超过10000个字符
      task1.put("content", content);
      tasks.add(task1);
      JSONObject data = new JSONObject();
      // 侦测场景，文本垃圾检测场景：antispan
      data.put("scenes", Arrays.asList("antispan"));
      System.out.println(JSON.toJSONString(data, true));
      textScanRequest.setHttpContent(data.toJSONString().getBytes("UTF-8"), "UTF-8");
  }
  ```

画面2：
- 展示了阿里云官网的文本审核服务文档页面，列出了支持的区域和检测场景。
- 文档内容：
  ```
  文本审核服务
  - cn-beijing
  - cn-shenzhen
  - cn-hangzhou
  - cn-qingdao
  - cn-shanghai
  检测场景（scene）
  - normal: 正常文本
  - opus: 合法性检测
  - ad: 广告
  - politics: 政治
  - terrorism: 恐怖
  - abuse: 恶意
  - porn: 色情
  - flood: 洪水
  - contraband: 禁物
  - meaningless: 无意义
  - customised: 自定义（根据命中文本关键词）
  ```

画面3：
- 展示了 IntelliJ IDEA 中的项目结构，当前选中的是 `heima-leadnews-common` 模块。
- 项目结构：
  ```
  heima-leadnews
  ├── heima-leadnews-admin
  ├── heima-leadnews-apis
  ├── heima-leadnews-article
  ├── heima-leadnews-behavior
  └── heima-leadnews-common
      ├── src
      │   └── main
      │       └── java
      │           └── com.heima.common
      │               └── aliyun
      │                   └── TextScanRequest.java
      └── resources
          └── aliyun.properties
  ```

画面4：
- 展示了测试类代码，用于测试阿里云文本审核服务。
- 代码片段：
  ```java
  @Autowired
  private AliyunTextScanRequest aliyunTextScanRequest;

  @Test
  public void testTextScanRequest() throws Exception {
      String message = "阿里云，阿里巴巴集团旗下的云计算品牌奇点，全球卓越的云计算技术和服务器提供商，成立于2009年，在杭州、北京、硅谷等地设有研发和运营中心。";
      String response = aliyunTextScanRequest.textScanRequest(message);
      System.out.println(response);
  }
  ```

画面5：
- 展示了 `AliyunTextScanRequest.java` 代码，其中设置了请求参数。
- 代码片段：
  ```java
  public String textScanRequest(String content) throws Exception {
      IClientProfile profile = DefaultProfile.getProfile("cn-shanghai", accessKey, secret);
      TextScanRequest textScanRequest = new TextScanRequest();
      textScanRequest.setAcceptFormat(FormatType.JSON);
      textScanRequest.setMethod(com.aliyuncs.http.MethodType.POST);
      textScanRequest.setEncoding("UTF-8");
      textScanRequest.setRegionId("cn-shanghai");
      List<Map<String, Object>> tasks = new ArrayList<Map<String, Object>>();
      Map<String, Object> task1 = new LinkedHashMap<String, Object>();
      task1.put("dataId", UUID.randomUUID().toString());
      // 待检测的文本，长度不能超过10000个字符
      task1.put("content", content);
      tasks.add(task1);
      JSONObject data = new JSONObject();
      // 侦测场景，文本垃圾检测场景：antispan
      data.put("scenes", Arrays.asList("antispan"));
      System.out.println(JSON.toJSONString(data, true));
      textScanRequest.setHttpContent(data.toJSONString().getBytes("UTF-8"), "UTF-8");
  }
  ```

画面6：
- 展示了 `AliyunTextScanRequest.java` 代码，其中使用了 `@ConfigurationProperties` 注解加载配置。
- 代码片段：
  ```java
  @Configuration
  @ConfigurationProperties(prefix = "aliyun")
  @PropertySource("classpath:aliyun.properties")
  public class AliyunTextScanRequest {
      private String accessKey;
      private String secret;
  }
  ```

画面7：
- 展示了项目结构，当前选中的是 `heima-leadnews-common` 模块。
- 项目结构：
  ```
  heima-leadnews
  ├── heima-leadnews-admin
  ├── heima-leadnews-apis
  ├── heima-leadnews-article
  ├── heima-leadnews-behavior
  └── heima-leadnews-common
      ├── src
      │   └── main
      │       └── java
      │           └── com.heima.common
      │               └── aliyun
      │                   └── TextScanRequest.java
      └── resources
          └── aliyun.properties
  ```

画面8：
- 展示了 `AllTest.java` 文件，其中包含了测试类的导入和注解。
- 代码片段：
  ```java
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.context.annotation.PropertySource;
  import org.springframework.test.context.ContextConfiguration;
  import org.springframework.test.context.junit4.SpringRunner;
  import org.springframework.test.context.support.AnnotationConfigContextLoader;
  ```

画面9：
- 展示了 `AllTest.java` 文件，其中包含了测试类的导入和注解。
- 代码片段：
  ```java
  import org.junit.runner.RunWith;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.boot.test.context.SpringBootTest;
  import org.springframework.test.context.junit4.SpringRunner;
  ```

画面10：
- 展示了 `AllTest.java` 文件，其中包含了测试类的导入和注解。
- 代码片段：
  ```java
  @RunWith(SpringRunner.class)
  @SpringBootTest
  public class AllTest {
      @Autowired
      private AliyunTextScanRequest aliyunTextScanRequest;
  }
  ```

画面11：
- 展示了 `AllTest.java` 文件，其中包含了测试类的导入和注解。
- 代码片段：
  ```java
  @RunWith(SpringRunner.class)
  @SpringBootTest
  public class AllTest {
      @Autowired
      private AliyunTextScanRequest aliyunTextScanRequest;
  }
  ```

画面12：
- 展示了 `AllTest.java` 文件，其中包含了测试类的导入和注解。
- 代码片段：
  ```java
  @RunWith(SpringRunner.class)
  @SpringBootTest
  public class AllTest {
      @Autowired
      private AliyunTextScanRequest aliyunTextScanRequest;
  }
  ```

画面13：
- 展示了阿里云官网的文本审核服务文档页面，列出了支持的区域和检测场景。
- 文档内容：
  ```
  文本审核服务
  - cn-beijing
  - cn-shenzhen
  - cn-hangzhou
  - cn-qingdao
  - cn-shanghai
  检测场景（scene）
  - normal: 正常文本
  - opus: 合法性检测
  - ad: 广告
  - politics: 政治
  - terrorism: 恐怖
  - abuse: 恶意
  - porn: 色情
  - flood: 洪水
  - contraband: 禁物
  - meaningless: 无意义
  - customised: 自定义（根据命中文本关键词）
  ```

画面14：
- 展示了阿里云官网的文本审核服务文档页面，列出了支持的区域和检测场景。
- 文档内容：
  ```
  文本审核服务
  - cn-beijing
  - cn-shenzhen
  - cn-hangzhou
  - cn-qingdao
  - cn-shanghai
  检测场景（scene）
  - normal: 正常文本
  - opus: 合法性检测
  - ad: 广告
