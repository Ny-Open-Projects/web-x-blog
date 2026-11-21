# 04_自媒体文章自动审核_aliyunAI_文本内容审核测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\04_自媒体文章自动审核_aliyunAI_文本内容审核测试【海量资源尽在 666java.com】.mp4
- 时长 8分12秒（音频 492s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续下面咱们就来去做一些例子首先做的第一个例子就是文本内容的这种审核这个其实你可以参考谁参考刚才说了你可以参考他的SDK里边提供了一些例子往上翻往上翻这有一个SDK找到Java然后下面是有一个文本反垃圾是吧这时候你就可以参考当前的Java代码其实我这个其实我今天给大家去提供了一个例子就是他
[00:28] 咱们可以直接拷贝一下比如再去说好咱们拷到哪呢拷到了当前的哪啊拷到当前的这个地儿在这去创建一个包这个包呢叫阿里云好吧阿里云啊OK然后呢咱们可以把当前的类啊直接拷进去拷进去之后啊咱们再去说一说啊比如说咱们可以把这个包先倒一下啊倒完啊下面还有些啊下面还有些我们来去倒一下我这样已经是在本项目中已经跑入了
[01:03] 阿里云的一些SDK所以说他都能去找到啊都能找到同时呢你要这里边因为他用到了一个这两个码这两个码的话是你申请的这两个东西啊这两个东西啊他俩他两个这时候呢你需要呢是在你这个里边在这啊去设置一个阿里云的跑跑历史内容的话其实就跟他一样啊就他跟他一样啊这个自己填写就可以好吧然后你在这读
[01:31] 因为这里边你去发请求的时候他就会去调用这两个东西去做验证好吧行这个你要去设置一下这里边其实大部分东西咱们不用去设置大部分东西不用设置因为这里边所有的参数咱们都已经设置好了其实你可以用我的我只是我的我的也是参考的当前的他然后稍微去改造了一下改造的内容其实不多改造内容其实只有一个哪个呢在这设了一个反位值
[01:59] 是吧同时呢在这儿是有一个contentcontent你需要传过来比如说你要审核的文本你要传过来然后呢他就会给你一些返回值返回值的话呢咱们就主要呢是拿到当前的这东西拿到当前的他我最终返回的时候也是他因为他呢就是咱们真正要返回的一些值比如说pass还有block还有review看得出来还有review啊
[02:31] review是人工审核就是三个值拿到pass之后就是干嘛呢就是说咱们干嘛要直接就通过了是吧review就是人工审核block就是命中垃圾这时候咱们需要去你这个文本审核就不通过了明白这意思吧好了行这个咱们再可以简单说一说上面还有些东西比如说这块内容就是你当前get和set然后是有一个它是一个配置类
[03:02] 然后还有啥呢他去读取了当前配置文件就是他就这块就这块然后就设了一个潜队叫阿里云然后最终我是把这两个码读进来读进来之后这时候就可以了好吧咱们可以去测一下但是测试怎么测试你可以在这测可以在咱们的 admin 上面去测因为 admin 上有时候要用到他你可以在这要测试的话首先你要先把当前配置给加进来怎么加
[03:29] 在这咱们再去创建一个配置类叫什么叫阿里好吧放一个我在这上面写的时候就非常简单了叫第一个是configuration然后第二个呢是compenscan你扫描当下就可以了比如说我是pump.黑马common什么阿里云是这个包吧没问题下面呢咱们就可以干嘛呢就可以去在这去写一个测试在这写啊
[04:02] 比如说com.hema.admin我们叫aliyun.test我们叫ali.test写ok之后呢咱们在这儿去写sprintboot.test还有什么runwithsprintrunner.class然后呢你这时候你就可以去注入进来比如说把谁注进来呢当前的这个类类叫啥呢叫aliyun.test
[04:32] request 是AutoVir加进来之后咱们就可以去写一些测试列public void test然后在这就加一个test下面就可以去调用了阿里有一个叫做这个你又可以去设置一些文本
[05:11] content 绑鱼咱们就在笔记中把它们给拷过来比如content是它然后最终它会返回这个是需要拋一长是吧那就拋出来拋出来然后咱们它这有个返回值返回值的话就是response咱们可以打印一下responseresponse然后咱们去加个东西省的太多咱们区分一下后边加个这东西好吧
[05:48] 那这个就算是设置完了设置完之后啊我们可以在笔记中这个内容给它考过来啊咱们去审核的时候啊这个内容啊是一个正常的内容它不会报任何问题这时候它就会去返回一个好这个里边你看它并没有任何违规的内容啊好这时候咱们可以去测试啊你测试的时候你要注意啊你的电脑一定要干嘛呢一定要连上网啊因为它需要调用阿里的接口好点稍等
[06:26] 好正在加载稍等啊好你看现在是绿色是吧通过了啊你看你打打印的是不是一个pass是吧这里边其实还有级别级别的话是当前的这东西啊是没有任何东西啊就是这个文章这个文本内容是可以的当然你要在下面去加个东西比如说嗯比如说咱们在这加一个啊比如说英乌买卖
[06:58] 这个内容其实又涉及到一些违禁品是吧你再去审核的时候他应该会告诉我你这个内容是有问题的好咱们可以来试一下走看一下这个效果好稍等正在加载好你看当前你看这是block刚才说了block什么意思是不是有违禁的一些东西是不是审核问审核文本的时候这个没有通过呀咱们也可以打开这个技术再去查查看一眼
[07:41] 比如说你往上看往上看API参考里边有一个什么叫文本文本里边有一个内容检测内容检测里边它是有一个block这个block刚才说了block就是没有通过但是它什么属于什么级别你也可以在这往上去翻往上翻的话就是它它对应的是谁你可以看一下对应的是是不是它是不是伪金品的没问题OK那咱们这个文本的选核咱们测试咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

