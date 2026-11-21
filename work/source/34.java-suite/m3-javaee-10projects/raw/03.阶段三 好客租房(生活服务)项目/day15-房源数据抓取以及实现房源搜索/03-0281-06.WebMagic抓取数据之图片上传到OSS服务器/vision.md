# 画面线理解：06.WebMagic抓取数据之图片上传到OSS服务器

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\06.WebMagic抓取数据之图片上传到OSS服务器【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:06, 00:21, 00:27, 00:37, 00:46, 00:51, 00:56, 01:45, 01:58, 02:04, 02:06, 02:17, 02:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:03:47

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码将从网页抓取的房屋图片数据批量上传至阿里云 OSS 对象存储服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中“1.5. 将图片上传到 OSS”章节的开头，列出上传的图片数据示例（JSON 格式），并显示代码文件夹结构。
画面2：PDF 文档中“1.5. 将图片上传到 OSS”章节，展示 Java 代码的 package 声明和导入语句。
画面3：展示一个房屋租赁网页（链家），鼠标右键点击图片，弹出“在新标签页中打开图片”等选项，暗示图片可被抓取。
画面4：展示 Windows 资源管理器，路径为“F:\开发\好课等等\day15\视频”，包含多个 WebMagic 相关的视频文件。
画面5：展示 Windows 资源管理器，路径为“F:\开发\好课等等\day15\images”，显示大量抓取的房屋图片。
画面6：展示阿里云 OSS 控制台，显示名为“itcast-haoke”的存储桶，其中已上传多个图片文件。
画面7：PDF 文档中“1.5. 将图片上传到 OSS”章节，展示 Java 代码的测试类 TestOSSTest 的开头部分，包含 OSS 客户端初始化的配置。
画面8：PDF 文档中“1.5. 将图片上传到 OSS”章节，展示 Java 代码的 for 循环部分，用于读取 JSON 文件并上传图片。
画面9：PDF 文档中“1.5. 将图片上传到 OSS”章节，展示 Java 代码的 for 循环部分，其中 `ossClient.putObject(...)` 方法被高亮。
画面10：展示阿里云 OSS 控制台，显示“itcast-haoke”存储桶中已上传的图片列表。
画面11：展示阿里云 OSS 控制台，选中一个图片文件后，点击“预览”按钮，右侧弹出预览窗口。
画面12：展示阿里云 OSS 控制台，预览窗口中显示“加载中...”。
画面13：展示阿里云 OSS 控制台，预览窗口中成功加载并显示图片，下方显示文件名、URL 和“复制成功”提示。
画面14：PDF 文档中“1.5. 将图片上传到 OSS”章节，展示已上传的图片列表，与 OSS 控制台内容对应。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
{
  "image": "SH2136963681764769792.jpg", "orientation": "40m", "houseType": "1室1厅1卫", "rentMethod": "整租", "time": "需搬进预约", "title": "整租，精装，可租两室的一房，2楼采光好安静卫生，居家舒适", "rent": "4800", "floor": "6层", "url": "https://sh.Tianjia.com/zufang/SH2136963681764769792.html"
}
{
  "image": "SH2118607017555279872.jpg", "orientation": "68m", "houseType": "2室1厅1卫", "rentMethod": "整租", "time": "需搬进预约", "title": "整租，长暮新两 2层 7300", "rent": "7300", "floor": "6层", "url": "https://sh.Tianjia.com/zufang/SH2118607017555279872.html"
}

画面2：
package cn.itcast.es;
import com.aliyun.oss.OSSClient;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.io.FileUtils;
import org.junit.Test;
import java.io.File;
import java.util.List;

画面7：
package cn.itcast.es;
import com.aliyun.oss.OSSClient;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.io.FileUtils;
import org.junit.Test;
import java.io.File;
import java.util.List;

public class TestOSSTest {
@Test
public void testoss() throws Exception{
ObjectMapper mapper = new ObjectMapper();
String endpoint = "http://oss-cn-qingdao.aliyuncs.com";
String accessKeyId = "L1aIFC7UsPj7Rfq";
String accessKeySecret = "c2vo3qlAmivty8lxnFscFko2c2hick";
String bucketName = "itcast-haoke";
String urlPrefix = "http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/";
OSSClient ossClient = new OSSClient(endpoint, accessKeyId, accessKeySecret);
}

画面8：
List<String> lines = FileUtils.readLines(new File("F:\\code\\data.json"), "UTF-8");
for (String line : lines) {
JsonNode jsonNode = mapper.readTree(line);
String image = jsonNode.get("image").asText();
ossClient.putObject(bucketName, "image", new File("F:\\code\\images\\"+image));
System.out.println(image);
}

画面9：
List<String> lines = FileUtils.readLines(new File("F:\\code\\data.json"), "UTF-8");
for (String line : lines) {
JsonNode jsonNode = mapper.readTree(line);
String image = jsonNode.get("image").asText();
ossClient.putObject(bucketName, "image", new File("F:\\code\\images\\"+image));
System.out.println(image);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
