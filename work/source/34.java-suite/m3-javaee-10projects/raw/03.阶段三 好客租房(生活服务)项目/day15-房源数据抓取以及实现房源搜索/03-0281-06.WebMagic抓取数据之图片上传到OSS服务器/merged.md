# 06.WebMagic抓取数据之图片上传到OSS服务器

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\06.WebMagic抓取数据之图片上传到OSS服务器【海量资源尽在 ubkz.com】.mp4
- 时长 2分24秒（音频 144s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续前面呢我们已经就把数据呢是不是就已经抓取完成了那么抓取完成之后呢我们还有件事情需要去做就是我们需要呢把我们这个图片呢上传到我们的OSS中那么为什么要去做一个上传呢前面我们说过我们不能直接使用链家的这个URL地址就是我们看到的啊这样的URL地址因为在项目中呢是不可用的所以我们去必须把它下载到本地那么刚刚呢我们也下载到了本地对吧
[00:29] 来看一下那么刚刚我们已经下载到是在code在这个里面那么我们下载到这个里面来了那么但是大家想一下最终我们访问是不是要通过我们URL的形式去做一个访问所以说我们现在有必要把它上传到我们的OSS中那么下面我们来看一下代码那么代码就是我们前面去讲我们上传的时候代码基本上是一样的那么我们去调用
[00:58] 这个阿里的OSS的客户端client然后呢去new一个这样的一个客户端把这些相关的信息呢给他传入进来ok得到一个client然后呢得到这client之后那么我们就要去干嘛呢就要去做一个这个上传那么上传的逻辑呢是在这儿这边有个put object然后呢上传到所有这个链接这个下面来然后呢读取到我们本地的读取到我们本地的这样的一个文件去做这个上传
[01:27] 那么在这个位置呢是不是我们读取到我们的抓取完的一个这样的一个文件然后呢每一行每一行中的这个AIMER是不是就是我们图片数据然后再读取到我们这个图片文件下所对应的这张图片然后做一个上传就可以了OK那么最终的这个代码呢我就不去运行了那么这个代码大家去拿到手应该直接运行就可以了当然了这个内容要填充你自己的一些信息啊自己信息这个呢是我的信息
[01:54] 好嘞那么我们来看一下在这个里面我们还是我现在已经就上传成功了我们可以看一下那比如说看一下这个图片就是我们上传好这样的一张图片可以看到那么我们是不是通过这个URL是不是就能够去做一个访问了对吧来看一下走是不是就可以做一个访问了那么这个链接我们就丢到我们项目中去使用是不是就OK了好那么这个就是关于我们图片的一个上传到OSS先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
ObjectMapper Mapper = new ObjectMapper();
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
JsonNode jsonNode = Mapper.readTree(line);
String image = jsonNode.get("image").asText();
ossClient.putObject(bucketName, "image", new File("F:\\code\\images\\"+image));
System.out.println(image);
}

画面9：
List<String> lines = FileUtils.readLines(new File("F:\\code\\data.json"), "UTF-8");
for (String line : lines) {
JsonNode jsonNode = Mapper.readTree(line);
String image = jsonNode.get("image").asText();
ossClient.putObject(bucketName, "image", new File("F:\\code\\images\\"+image));
System.out.println(image);
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

