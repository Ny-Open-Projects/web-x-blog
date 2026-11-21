# 画面线理解：03_自媒体文章自动审核_aliyun服务介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day07-黑马头条-自媒体文章审核
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day07-黑马头条-自媒体文章审核\03_自媒体文章自动审核_aliyun服务介绍【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:58, 02:28, 03:00, 03:13, 03:51, 04:22, 05:30, 06:02, 06:45, 07:03, 07:32, 07:57, 08:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:16:18

1) 这一组画面整体在讲如何使用阿里云内容安全服务进行文本垃圾内容检测，并展示相关的开发文档和代码示例。

2) 按时间顺序列出每张画面的要点：
画面1：展示Markdown文档，内容为“2.1 阿里云服务介绍”下的“2.1.1 文本垃圾内容检测”章节，其中包含“安装sdk”的Maven依赖配置。
画面2：在百度搜索框中输入“ba”，搜索结果包含“阿里云”相关链接。
画面3：在阿里云官网“内容安全”页面，鼠标悬停在“图片审核”选项卡上。
画面4：在阿里云内容安全控制台的“文本垃圾内容检测”统计页面，展示柱状图和饼图。
画面5：在阿里云帮助文档页面，搜索框中输入“ah”。
画面6：在阿里云帮助文档页面，展示“关于scene与label参数”的表格，包含scene和label的定义。
画面7：在阿里云帮助文档页面，展示“表2 result”的部分，包含“scene”、“label”、“suggestion”、“rate”等字段的描述。
画面8：在Markdown文档中，鼠标悬停在“2.1.1 文本垃圾内容检测”下的“文本垃圾内容检测说明”链接上。
画面9：在Markdown文档中，展示“2.1.1 文本垃圾内容检测”章节，包含“安装sdk”的Maven依赖配置。
画面10：在阿里云帮助文档页面，展示“文本内容检测”的Java代码示例，包含“DefaultClient”、“TextScanRequest”等类的使用。
画面11：在阿里云帮助文档页面，鼠标悬停在“人像审核”选项卡上。
画面12：在阿里云帮助文档页面，展示“表2 result”的部分，包含“scene”、“label”、“suggestion”、“rate”等字段的描述。
画面13：在阿里云帮助文档页面，展示“表2 result”的部分，包含“scene”、“label”、“suggestion”、“rate”等字段的描述。
画面14：在阿里云帮助文档页面，展示“表2 result”的部分，包含“scene”、“label”、“suggestion”、“rate”等字段的描述。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面1：
```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>3.4.1</version>
</dependency>

<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-green</artifactId>
    <version>3.4.1</version>
</dependency>
```

画面10：
```java
import com.aliyun.DefaultClient;
import com.aliyun.TextClient;
import com.aliyun.exceptions.ServerException;
import com.aliyun.http.FormType;
import com.aliyun.http.HttpResponse;
import com.aliyun.profile.DefaultProfile;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", "yourAccessKeyId", "yourAccessKeySecret");
        TextClient client = new TextClient(profile);
        TextScanRequest textScanRequest = new TextScanRequest();
        textScanRequest.setMethod(com.aliyun.http.MethodType.POST);
        textScanRequest.setEncoding("UTF-8");
        textScanRequest.setBody("待检测的文本，长度不超过10000个字符");
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面6：
| 功能 | 描述 | scene | label |
|------|------|-------|-------|
| 文本垃圾检测 | 结合行为、内容、采用多维度、多模型、多标签手段，识别文本中的垃圾内容、广告、谩骂、涉政、色情等高危风险。 | antispam | normal: 正常文本<br>spam: 垃圾信息<br>ad: 广告<br>politics: 政治<br>terrorism: 恐怖<br>violence: 暴力<br>sex: 色情<br>hate: 嫉妒<br>contradiction: 逻辑错误<br>copyright: 版权<br>other: 其他 |

画面12：
| 名称 | 类型 | 是否必填 | 描述 |
|------|------|----------|------|
| scene | 字符串 | 是 | 图片检测场景，和请求中的场景（scenes）对应。 |
| label | 字符串 | 是 | 检测场景的分类，与具体的scene对应，取值范围见scene label映射。 |
| suggestion | 字符串 | 是 | 建议执行的操作，取值范围：<br>pass：图片正常，无需进行处理；或者未识别出目标对象<br>review：需要人工审核<br>block：图片违规，建议执行此操作（如屏蔽或删除）处理。 |
| rate | 浮点数 | 是 | 结果与该分类的概率，取值范围[0.00-100.00]，越高，表示越有可能属于该分类。 |

5) 不要评价画面美观，不要输出与课程无关的内容。
