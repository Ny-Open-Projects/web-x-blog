# 画面线理解：17_自媒体文章管理_发布文章业务层代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day05-黑马头条-自媒体文章发布与管理
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day05-黑马头条-自媒体文章发布与管理\17_自媒体文章管理_发布文章业务层代码编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:49, 01:28, 01:59, 02:17, 03:37, 04:25, 04:56, 05:42, 06:34, 07:11, 07:54, 08:31, 09:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:53:27

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中定义接口、实现类、控制器，并通过数据库操作实现新闻稿件的增删改查功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 IDEA 中的项目结构，当前选中的是 `AdChannelServiceImpl` 类。
- 代码内容：`public interface AdChannelService { List<AdChannel> selectAll(); }`。
- 画面左侧导航栏显示当前章节为“5.1.4 代码实现”。

画面 2：
- 展示了 `AdChannelService` 接口的定义，位于 `com.heima.media.service` 包下。
- 代码内容：`public interface AdChannelService { List<AdChannel> selectAll(); }`。
- 项目结构中显示了 `AdChannelServiceImpl` 的实现类。

画面 3：
- 展示了 `AdChannelServiceImpl` 类的代码，位于 `com.heima.media.service.impl` 包下。
- 代码内容：`import com.heima.media.service.AdChannelService; import com.heima.model.admin.po.AdChannel; import org.springframework.stereotype.Service; import java.util.List; @Service public class AdChannelServiceImpl implements AdChannelService { @Override public List<AdChannel> selectAll() { return null; } }`。

画面 4：
- 展示了项目结构，当前选中的是 `heima-leadnews-media` 模块。
- 项目结构中包含 `src/main/java`、`src/main/resources` 等目录。

画面 5：
- 展示了在 `heima-leadnews-apis` 模块中创建新类的对话框。
- 对话框中 `Name` 字段为空，`Kind` 选择为 `Interface`。

画面 6：
- 展示了 `NewsControllerApi` 接口的代码，位于 `com.heima.media.apis` 包下。
- 代码内容：`public interface NewsControllerApi { public ResponseResult submitNews(NewsDto dto); public ResponseResult saveDraftNews(NewsDto dto); }`。

画面 7：
- 展示了项目结构，当前选中的是 `heima-leadnews-apis` 模块。
- 项目结构中包含 `src/main/java`、`src/main/resources` 等目录。

画面 8：
- 展示了 `NewsController` 类的代码，位于 `com.heima.media.controller` 包下。
- 代码内容：`import com.heima.media.apis.NewsControllerApi; import com.heima.model.common.dto.ResponseResult; import com.heima.model.media.dto.NewsDto; import org.springframework.web.bind.annotation.RestController; @RestController public class NewsController implements NewsControllerApi { }`。

画面 9：
- 展示了 `NewsController` 类的代码，位于 `com.heima.media.controller` 包下。
- 代码内容：`import com.heima.model.common.dto.ResponseResult; import com.heima.model.media.dto.NewsDto; import org.springframework.web.bind.annotation.RestController; @RestController public class NewsController implements NewsControllerApi { @Autowired private NewsService newsService; @Override public ResponseResult submitNews(NewsDto dto) { return newsService.saveNews(dto); } @Override public ResponseResult saveDraftNews(NewsDto dto) { return null; } }`。

画面 10：
- 展示了 Navicat for MySQL 的界面，显示了 `wm_news` 数据库中的 `channel` 表。
- 表中包含 `channel_id`、`labels`、`created_time`、`submitted_time`、`status`、`publish_time`、`reason`、`article_id`、`images`、`enable` 等字段。

画面 11：
- 展示了 `NewsController` 类的代码，位于 `com.heima.media.controller` 包下。
- 代码内容：`import com.heima.model.common.dto.ResponseResult; import com.heima.model.media.dto.NewsDto; import org.springframework.web.bind.annotation.RestController; @RestController public class NewsController implements NewsControllerApi { @Autowired private NewsService newsService; @Override public ResponseResult submitNews(NewsDto dto) { return newsService.saveNews(dto); } @Override public ResponseResult saveDraftNews(NewsDto dto) { return newsService.saveDraftNews(dto, WM_NEWS_DRAFT_STATUS); } }`。

画面 12：
- 展示了 `AdChannelControllerApi` 接口的代码，位于 `com.heima.media.controller` 包下。
- 代码内容：`import com.heima.media.apis.AdChannelControllerApi; import com.heima.model.common.dto.ResponseResult; import org.springframework.web.bind.annotation.RestController; @RestController public class AdChannelController implements AdChannelControllerApi { }`。

画面 13：
- 展示了 `AdChannelController` 类的代码，位于 `com.heima.media.controller` 包下。
- 代码内容：`import com.heima.media.apis.AdChannelControllerApi; import com.heima.media.service.AdChannelService; import com.heima.model.common.dto.ResponseResult; import org.springframework.web.bind.annotation.RestController; @RestController public class AdChannelController implements AdChannelControllerApi { @Autowired private AdChannelService adChannelService; @Override public ResponseResult selectAll() { return null; } }`。

画面 14：
- 展示了 `AdChannelController` 类的代码，位于 `com.heima.media.controller` 包下。
- 代码内容：`import com.heima.media.apis.AdChannelControllerApi; import com.heima.media.service.AdChannelService; import com.heima.model.common.dto.ResponseResult; import org.springframework.web.bind.annotation.RestController; @RestController public class AdChannelController implements AdChannelControllerApi { @Autowired private AdChannelService adChannelService; @Override public ResponseResult selectAll() { return ResponseResult.okResult(adChannelService.selectAll()); } }`。
