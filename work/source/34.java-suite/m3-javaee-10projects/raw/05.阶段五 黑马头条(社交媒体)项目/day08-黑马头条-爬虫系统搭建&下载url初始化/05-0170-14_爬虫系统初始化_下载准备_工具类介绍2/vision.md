# 画面线理解：14_爬虫系统初始化_下载准备_工具类介绍2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\14_爬虫系统初始化_下载准备_工具类介绍2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:30, 01:36, 02:52, 04:25, 04:42, 05:21, 06:42, 07:18, 07:53, 08:30, 09:59, 10:41, 11:40, 12:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:37:43

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Selenium 的网页爬虫客户端的代码结构、核心功能实现及测试流程，重点讲解延迟工具类、代理设置、Cookie管理及测试用例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 IDE 中的 `DelayedUtils.java` 文件，其中包含 `delayed` 和 `delayed` 方法。
- 代码内容：
  ```java
  public class DelayedUtils {
      public static void delayed(long delayedTime) {
          try {
              Thread.sleep(delayedTime);
          } catch (InterruptedException e) {
              e.printStackTrace();
          }
      }

      /**
       * 延时方法
       * @param callback
       */
      public static Object delayed(DelayedCallback callback) {
          boolean flag = false;
          long sleepTime = callback.sleepTime();
          long timeout = callback.timeout();
          long currentTime = System.currentTimeMillis();
          Object obj = null;
          try {
              Thread.sleep(sleepTime);
          }
  ```

画面 2：
- 继续展示 `DelayedUtils.java` 文件，显示 `delayed` 方法的后续代码。
- 代码内容：
  ```java
  long duration = System.currentTimeMillis() - currentTime;
  boolean isExist = callback.isExist();
  if (isExist) {
      flag = true;
  } else if (duration > timeout) {
      flag = true;
  }
  if (flag) {
      break;
  }
  ```

画面 3：
- 展示了 `ConcurrentEntity` 类的定义，用于管理并发状态。
- 代码内容：
  ```java
  static class ConcurrentEntity {
      /**
       * 当前时间
       */
      private long currentTime = System.currentTimeMillis();
      /**
       * 时间区间
       */
      private long timeInterval = 10000;
      /**
       * 是否可用
       */
      private boolean available = true;
  }
  ```

画面 4：
- 展示了 `SeleniumClient` 类中用于初始化 ChromeDriver 的部分代码。
- 代码内容：
  ```java
  private static final long SLEEP_TIME = 1000;
  /**
   * 读取crawler.properties 配置文件
   */
  private static final ResourceBundle resourceBundle = ResourceBundle.getBundle("crawler");
  /**
   * java源码的xpath 表达式
   */
  public static final String SELENIUM_JSON_DATA_PATH = "//pre/text()";
  ```

画面 5：
- 展示了 `SeleniumClient` 类中 `isExist` 和 `sleepTime` 方法的实现。
- 代码内容：
  ```java
  @Override
  public boolean isExist() {
      Set<Cookie> cookieSet = driver.manage().getCookies();
      return isExistCookieName(cookieSet, cookieName);
  }

  /**
   * 防止一直获取cpu资源浪费的太多，默认1秒重复获取一次
   */
  public long sleepTime() {
      return sleepTime;
  }

  /**
   * 设置的超时时间，防止页面没有找到cookie一直重试，没有超出
   * 当达到超时时间自动退出，将需要的页面抓取返回
   */
  public long timeout() {
      return timeout;
  }
  ```

画面 6：
- 展示了项目结构和测试类 `SeleniumClientTest` 的代码。
- 代码内容：
  ```java
  package com.heima.crawler.test;

  @SpringBootTest
  @RunWith(SpringRunner.class)
  public class SeleniumClientTest {
      @Autowired
      private SeleniumClient seleniumClient;

      @Test
      public void test() {
          CrawlerHtml crawlerHtml = seleniumClient.getCrawlerHtml("http://www.baidu.com".null.mill
          System.out.println(crawlerHtml.getHtml());
      }
  }
  ```

画面 7：
- 展示了测试类 `SeleniumClientTest` 的调试日志，显示 Spring Boot 启动时的配置加载信息。
- 日志内容：
  ```
  2019-10-15 14:38:30.326 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) No URLs will be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323 [WARN] main [com.netflix.config.sources.URLConfigurationSource] (init) To enable URLs to be polled as dynamic configuration sources.
  2019-10-15 14:38:30.323
