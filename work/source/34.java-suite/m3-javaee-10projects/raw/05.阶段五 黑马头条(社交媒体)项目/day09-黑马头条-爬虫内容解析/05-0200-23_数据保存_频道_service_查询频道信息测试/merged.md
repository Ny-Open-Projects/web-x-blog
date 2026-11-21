# 23_数据保存_频道_service_查询频道信息测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\23_数据保存_频道_service_查询频道信息测试【海量资源尽在 666java.com】.mp4
- 时长 2分36秒（音频 157s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去测试一下刚刚写这个方法在这咱们再去定一个方法叫public然后是Void这个方法名你最好是跟这个能够保持一致咱们稍微改一改稍微规范一些好吧这个是加上get这个其实也是一样咱们是通过前的一个他要test是拼上一个这东西像这个方法好在这去加一个test
[00:38] 然后你就可以直接去调用当前这个方法了而当前的getAdKinoByLiveIds你可以传执比如传一个1传一个2最终它只会返回一个1对吧因为咱们只需要去默认第一个就可以了而inJD当前的Ids可以了行这个咱们可以直接执行一下看看有没有包错就可以了好吧
[01:05] 看看最终的结果能不能拿到应该是拿到当前的一个1因为这里边你可以看这个呢这个level1呢对应的是1对应的是1啊没问题咱们可以看一下当前的结果到底是不是1就可以了稍等稍微有点慢啊到后期会越来越慢啊好这个没有问题啊你可以看一下当下有没有打印呢打印是1是吧没问题啊当然如果说你要想不信的话呢你可以在这给他改点东西啊就1122啊
[01:47] 我说你再去干嘛呢你再去执行一下啊看看拿到的是不是1122因为现在啊这个label1对应的就是1122是吧好稍等一下啊再来去等再等一会儿马上结束了稍等啊好结束了你看这是不是1122啊没问题啊好我把这个给恢复过来啊这个开始改成1好吧行那这个啊这个咱们就算是讲完了啊完了
[02:23] 然后今天内容呢其实咱们也讲差不多了这个爱不在理迟啊这个暂时不讲了我会把这个笔记呢是挪到下一天挪到下一天去讲好吧行那这个今天内容啊咱们就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过单元测试验证标签服务（AdLabelService）根据频道ID获取标签ID的功能，并展示相关的数据库表结构和操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示测试类AdLabelServiceTest中的测试方法test1()，调用adlabelService的getLabels方法传入参数"java, Docker, 8888xxxx"，并打印返回值。测试通过。
画面2：在测试类中，将测试方法重命名为testGetAdChannelByLabelsId()，准备测试根据频道ID获取标签ID的功能。
画面3：在测试方法中，将参数从"java, Docker, 8888xxxx"修改为"1,2"，准备测试根据频道ID获取标签ID的功能。
画面4：在测试方法中，将参数从"1,2"修改为"1,2"，并显示了IDEA的代码补全建议列表。
画面5：在Navicat中查看数据库表ad_channel_label的数据，显示了多条记录，其中id为1108的记录被选中。
画面6：在IDEA中运行测试，控制台输出了测试通过的信息，日志显示Spring Boot应用启动并初始化了Hikari连接池。
画面7：在IDEA中运行测试，控制台输出了测试通过的信息，日志显示Spring Boot应用启动并初始化了Hikari连接池。
画面8：在IDEA中运行测试，控制台输出了测试通过的信息，日志显示Spring Boot应用启动并初始化了Hikari连接池。
画面9：在Navicat中查看数据库表ad_channel_label的数据，显示了多条记录，其中id为1108的记录被选中。
画面10：在Navicat中，将选中的记录的channel_id从1修改为1122。
画面11：在IDEA中运行测试，控制台输出了测试通过的信息，日志显示Spring Boot应用启动并初始化了Hikari连接池。
画面12：在IDEA中运行测试，控制台输出了测试通过的信息，日志显示Spring Boot应用启动并初始化了Hikari连接池。
画面13：在IDEA中运行测试，控制台输出了测试通过的信息，日志显示Spring Boot应用启动并初始化了Hikari连接池。
画面14：在PDF文档中，展示了测试类AdLabelServiceTest的代码，其中包含测试方法testGetAdChannelByLabelsId()，用于测试根据频道ID获取标签ID的功能。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public class AdLabelServiceTest {
    @Autowired
    private AdLabelService adlabelService;

    @Test
    public void test1() {
        String labelIds = adlabelService.getLabels("java, Docker, 8888xxxx");
        System.out.println(labelIds);
    }
}
```

画面2：
```java
public class AdLabelServiceTest {
    @Autowired
    private AdLabelService adlabelService;

    @Test
    public void test1() {
        String labelIds = adlabelService.getLabels("java, Docker, 8888xxxx");
        System.out.println(labelIds);
    }

    public void
```

画面3：
```java
public class AdLabelServiceTest {
    @Autowired
    private AdLabelService adlabelService;

    @Test
    public void test1() {
        String labelIds = adlabelService.getLabels("java, Docker, 8888xxxx");
        System.out.println(labelIds);
    }

    @Test
    public void testGetAdChannelByLabelsId() {
    }
}
```

画面4：
```java
public class AdLabelServiceTest {
    @Autowired
    private AdLabelService adlabelService;

    @Test
    public void test1() {
        String labelIds = adlabelService.getLabels("java, Docker, 8888xxxx");
        System.out.println(labelIds);
    }

    @Test
    public void testGetAdChannelByLabelsId() {
        String labelIds = adlabelService.getAdChannelByLabelsId("1,2");
        System.out.println(labelIds);
    }
}
```

画面6：
```java
2019-10-22 21:38:38,301 [INFO] main [org.springframework.cloud.context.scope.GenericScope] [setSerializationId] [BeanFactory] [id=80336c62-6c4d-3937-943e-819582b3563d]
2019-10-22 21:38:38,313 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,325 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,341 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,353 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,365 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,377 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,389 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,401 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,413 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,425 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,437 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,449 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,461 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,473 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,485 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,497 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,509 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,521 [INFO] main [org.springframework.context.support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker] [postProcessAfterInitialization] [BeanFactoryPostProcessor]
2019-10-22 21:38:38,533 [INFO]

