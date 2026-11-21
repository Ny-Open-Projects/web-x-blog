# 05_数据保存准备_爬虫文章图文附加信息_需求分析及mapper定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\05_数据保存准备_爬虫文章图文附加信息_需求分析及mapper定义【海量资源尽在 666java.com】.mp4
- 时长 5分17秒（音频 318s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们再去说第二个啊就是爬虫文章的图文附加信息啊这是附加信息附加信息然后这块内容呢咱们看一下需求啊这个需求的话说爬虫文章的附加信息比如文章的点赞转发评论等然后呢它是方便的后期追踪数据反向爬与数据啊这句话什么意思呢你看咱们都知道啊咱们目前的话是在APP端是展示文章在这个文章的来源呢咱们之前讲过一个呢
[00:31] 就是自媒体是吧第二个呢就是爬虫那爬虫的文章如果说当你比如说你要是从sysdn上去爬了某一篇文章这个文章呢它的点赞量可能会越来越高比如说今天是100到明天的时候可能在sysdn上面已经是200了那那咱们的系统里边是不是应该去更新当前的点赞数呢需要啊需要更新这个点赞数啊所以说呢咱们还需要二次爬去也就是反向爬去
[00:58] 咱们只需要去爬取当前文章的点赞转发评论然后同时更新到咱们的数据库里边就可以了好吧这个呢就是它附加信息的一个存在的一个必要好吧呃行那这个表啊这个表呢其实对应的就是当前的CL News啊Digital啊Digital啊那就它呢你看这里边字段啊呃字段的话有个通关地是吧有原文地址你看到了吧阅读量还有点赞
[01:29] 评论是吧转发不喜欢收藏等等还有创建时间是吧更新次数咱们要更新吗还有就是更新时间下次更新时间咱们都会去设置OK那这个啊这个的话咱们这个表啊也比较好利益也是一个单表啊它对应的类呢对应的这种实体类啊就是这个就是刚刚咱们说的那所有的字段好吧然后下面咱们就来去定义当前的MIPRO接口这个MIPRO接口来看一下啊
[01:58] 首先你看也是咱们比较通用的一些东西比如说删除是吧新增还有是也是个新增还有什么查询根据主见修改修改两个还有下面这个是按条件查询还有按按什么获取需要更新的数据那这个是根据时间刚才说了这里边有两个时间是吧更新次数更新时间还有下次更新时间这是咱们的可以做个定时是吧那但是后期可以做定时
[02:28] 比如说下一次更新的时候它会自动去更新它的条件就是根据当前的时间你看这块就是根据当前某一个时间去更新数据OK行这个的话咱们就算是说完了说完之后咱们可以把它给考一下考到当前的model中把这个也测完了然后找到modelmypro是吧colors
[03:05] 然后直接就可以了可不完之后可以看一下把这个包倒下那考完之后下面是不是还得学干嘛是不是还得需要当前一个麦普文件呢我可以回来还是当前的resource下面有一个callers在这去直接去创建一个文件然后你就可以把这些内容铁拷过来之后你要去检查一下到底有没有报错有报错就改一改好吧
[03:39] 还是挺多的是吧好,看完啊回来之后你看这块有可能会出错是吧来看一看啊那目前的话来看呢是出错的也有一处啊就这啊这个这个可能是有问题可以按一下两压shift按它真正的地址是谁它是吧右键然后是拷贝它的地址然后把这个给替换了就可以了啊那这个就算是设置完了啊这个我也把它
[04:11] 笔记上更新一下最后一个更新完之后这份内容咱们就算是设置完了设置完之后你可以再简单看一眼这个里边就是对应的咱们Maple文件里边所有的这种方法是吧行这个我就不再去说了然后如果说我再去强调一个事就光是现在还是后边咱们拷贝的时候如果说字段说不全的话不全的话你首先得以稀微准
[04:44] 首先呢你得以表为准得以表为准如果这里边有的话如果说你的这个属性没有是吧你要学会去更新学会去更新啊以当前的表为准OK那行那再往下看啊那里边有slack的是吧还有什么根据需要去更新根据需要去更新啊还有就是根据组件是吧OK没啥问题啊这个呢还是相对来说不难啊也比较简单啊这有咱们就不再去细讲了
[05:13] 好了那咱们下面呢就来去定义Service好吧把这个先断一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个新闻爬虫项目中，如何定义实体类、Mapper接口、Service接口及对应的MyBatis XML映射文件，实现对新闻附加信息的增删改查功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了项目结构目录，当前选中的是“day01/数据持久化与文章支持分析”下的“1.2 额外文章信息”章节。
- 代码编辑器中显示了实体类 CINewsAdditional 的定义，包含多个私有字段如 id、newsId、url、readCount、likes、comment、forward、unlikes、collection、createdTime、count、updatedTime、nextUpdateTime、updateNum。

画面2：
- 展示了Mapper接口定义，接口名为 CINewsAdditionalMapper，位于包 com.heima.model.mappers.crawlers 下。
- 接口定义了三个方法：deleteByPrimaryKey(Integer id)、insert(CINewsAdditional record)、insertSelective(CINewsAdditional record)。

画面3：
- 展示了测试类 CrawlerIpPoolServiceTest 的代码，用于测试 IP 池服务。
- 代码中使用了 @SpringBootTest 和 @Autowired 注解，测试方法 testSaveCrawlerIpPool() 中创建了 CrawlerIpPool 对象并调用 saveCrawlerIpPool() 方法。

画面4：
- 展示了项目结构目录，当前选中的是 test 目录下的 CrawlerIpPoolServiceTest。
- 项目结构中显示了多个模块，如 admin、article、behavior、common、crawler、media、mess、quartz.dos、user、WebSocket.dos。

画面5：
- 展示了项目结构目录，当前选中的是 com.heima.model 包下的 CINewsAdditionalMapper.xml 文件。
- 项目结构中显示了多个模块，如 admin、article、behavior、common、crawler、media、mess、quartz.dos、user、WebSocket.dos。

画面6：
- 展示了 CINewsAdditionalMapper.xml 文件的内容，其中定义了两个 SQL 查询语句：selectList() 和 selectListByNeedUpdate()。
- XML 文件中定义了 namespace、resultMap 和 sql 标签，用于映射数据库字段到 Java 对象属性。

画面7：
- 展示了 CINewsAdditionalMapper.xml 文件的内容，与画面6相同。
- XML 文件中定义了 namespace、resultMap 和 sql 标签，用于映射数据库字段到 Java 对象属性。

画面8：
- 展示了 Service 接口 CrawlerNewsAdditionalService 的定义，位于包 com.heima.crawler.Service 下。
- 接口定义了两个方法：saveAdditional(CINewsAdditional cNewsAdditional) 和 queryListByNeedUpdate(Date currentDate)。

画面9：
- 展示了 CINewsAdditionalMapper.xml 文件的内容，其中定义了 resultMap 和 sql 标签。
- resultMap 标签中定义了 id、url、read_count、likes、comment、forward、unlikes、collection、created_time、count、updated_time、update_num、next_update_time 等字段映射。

画面10：
- 展示了 CINewsAdditionalMapper.xml 文件的内容，与画面8相同。
- XML 文件中定义了 namespace、resultMap 和 sql 标签，用于映射数据库字段到 Java 对象属性。

画面11：
- 展示了 CINewsAdditionalMapper.xml 文件的内容，其中定义了 update 标签。
- update 标签中定义了 set 子句，用于更新 CINewsAdditional 对象的各个字段。

画面12：
- 展示了 CINewsAdditionalMapper.xml 文件的内容，其中定义了 sql 标签。
- sql 标签中定义了多个 if 条件，用于根据传入的参数值动态生成 SQL 查询条件。

画面13：
- 展示了 CINewsAdditionalMapper.xml 文件的内容，其中定义了 sql 标签。
- sql 标签中定义了多个 if 条件，用于根据传入的参数值动态生成 SQL 查询条件。

画面14：
- 展示了 CINewsAdditionalMapper.xml 文件的内容，其中定义了 select、delete、insert 标签。
- select 标签中使用了 include refid="Base_Column_list" 来引用基础列。
- delete 标签中定义了 deleteById 的 SQL 语句。
- insert 标签中定义了插入数据的 SQL 语句，包括 keyProperty 和 useGeneratedKeys 属性。

