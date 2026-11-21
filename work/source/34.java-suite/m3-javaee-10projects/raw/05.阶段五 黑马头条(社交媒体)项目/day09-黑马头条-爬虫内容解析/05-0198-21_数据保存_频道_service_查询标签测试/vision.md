# 画面线理解：21_数据保存_频道_service_查询标签测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\21_数据保存_频道_service_查询标签测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:36, 01:14, 02:11, 02:30, 03:11, 03:53, 04:28, 04:51, 05:19, 06:06, 06:37, 07:21, 07:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:57:35

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中编写并调试一个用于过滤标签的 Service 层方法，并通过单元测试验证其功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示了 IntelliJ IDEA 中的项目结构，当前打开的文件是 `AdLabelServiceImp.java`。
- 代码内容：在 `addLabel` 方法中，创建了一个 `AdLabel` 对象，设置其属性（name, type, createTime），并调用 `adLabelMapper.insert(adlabel)` 插入数据库。
- 代码片段：
```java
private AdLabel addLabel(String label) {
    AdLabel adlabel = new AdLabel();
    adlabel.setName(label);
    adlabel.setType(true);
    adlabel.setCreateTime(new Date());
    adlabelMapper.insert(adlabel);
    return adlabel;
}
```

画面 2：
- 显示了测试类 `AdLabelServiceTest.java` 的开头部分。
- 代码内容：导入了 `@SpringBootTest` 和 `@RunWith(SpringRunner.class)` 注解，定义了测试类 `AdLabelServiceTest`。
- 代码片段：
```java
package com.heima.crawler.service;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
@RunWith(SpringRunner.class)
public class AdLabelServiceTest {
```

画面 3：
- 显示了在测试类中编写测试方法 `test1()` 的过程。
- 代码内容：在方法中调用 `adLabelService.getLabelIds(labels: "java, docker, 8888xxxx")` 并打印结果。
- 代码片段：
```java
@Test
public void test1() {
    String labelIds = adLabelService.getLabelIds(labels: "java, docker, 8888xxxx");
    System.out.println(labelIds);
}
```

画面 4：
- 显示了测试方法 `test1()` 的执行结果。
- 控制台输出：`rationSHEnhancer:SpringOCLIB$18eda9fc1 is not eligible for getting processed by all BeanPostProcessors (for example; not eligible for auto-proxying)`。
- 说明：测试执行成功，但有 Spring 的警告信息。

画面 5：
- 显示了测试执行时的日志输出。
- 日志内容：显示了线程池关闭、HikariCP 数据库连接池关闭等信息。
- 日志片段：
```
2019-10-22 21:02:47,500 [DEBUG] Thread-5 log.springframework.scheduling.concurrent.ThreadPoolTaskExecutor: Shutdown (shutting down ExecutorService)
2019-10-22 21:02:47,500 [DEBUG] Thread-5 log.springframework.scheduling.concurrent.ThreadPoolTaskExecutor: Shutdown (destroying PA EntityManagerFactory)
2019-10-22 21:02:47,500 [DEBUG] Thread-5 log.zaxxer.hikari.pool.HikariPool-1: close [HikariPool-1] - Shutdown completed.
```

画面 6：
- 显示了测试类 `AdLabelServiceTest` 的完整代码。
- 代码内容：测试类中包含 `@Autowired` 注入的 `AdLabelService` 和 `@Test` 方法 `test1()`。
- 代码片段：
```java
@Autowired
private AdLabelService adlabelService;

@Test
public void test1() {
    String labelIds = adLabelService.getLabelIds(labels: "java, docker, 8888xxxx");
    System.out.println(labelIds);
}
```

画面 7：
- 显示了 `AdLabelServiceImpl.java` 中的 `addLabelList` 方法。
- 代码内容：方法用于过滤模板标签列表，移除与已存在标签重复的标签。
- 代码片段：
```java
private List<AdLabel> addLabelList(List<String> tmplLabels, List<AdLabel> adlabelList) {
    if (tmplLabels != null && !tmplLabels.isEmpty()) {
        for (int i = 0; tmplLabels.size(); i++) {
            for (AdLabel adlabel : adlabelList) {
                if (tmplLabels.get(i).contains(adlabel.getName())) {
                    tmplLabels.remove(i);
                }
            }
        }
    }
}
```

画面 8：
- 显示了调试模式下 `addLabelList` 方法的执行过程。
- 调试信息：`tmplLabels` 初始大小为 3，`adlabelList` 初始大小为 2。
- 调试信息：
```
tmplLabels = (ArrayList) size = 3
0 = Collecting data
1 = Collecting data
2 = Collecting data
```

画面 9：
- 显示了调试模式下 `addLabelList` 方法的执行过程。
- 调试信息：`tmplLabels` 大小变为 2，`adlabelList` 大小仍为 2。
- 调试信息：
```
tmplLabels = (ArrayList) size = 2
0 = Collecting data
1 = Collecting data
```

画面 10：
- 显示了调试模式下 `addLabelList` 方法的执行过程。
- 调试信息：`tmplLabels` 大小为 2，`adlabelList` 大小为 2。
- 调试信息：
```
tmplLabels = (ArrayList) size = 2
adlabelList = (ArrayList) size = 2
```

画面 11：
- 显示了 `addLabelList` 方法的完整代码。
- 代码内容：在过滤标签后，如果 `tmplLabels` 不为空，则将其添加到 `adlabelList` 中。
- 代码片段：
```java
if (tmplLabels != null && !tmplLabels.isEmpty()) {
    adlabelList.addAll(addLabelList(tmplLabels));
}
```

画面 12：
- 显示了调试模式下 `addLabelList` 方法的执行过程。
- 调试信息：`adlabelList` 大小变为 1。
- 调试信息：
```
adlabelList = (ArrayList) size = 1
```

画面 13：
- 显示了 `addLabelList` 方法的完整代码。
- 代码内容：方法最后返回 `adlabelList`。
- 代码片段：
```java
return adlabelList;
```

画面 14：
- 显示了测试类 `AdLabelServiceTest` 的测试方法 `test1()` 的执行结果。
- 控制台输出：`Tests passed`，表示测试通过。
- 代码片段：
```java
@Test
public void test1() {
    String labelIds = adLabelService.getLabelIds(labels: "java, docker, 8888xxxx");
    System.out.println(labelIds);
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文各画面的代码片段。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
