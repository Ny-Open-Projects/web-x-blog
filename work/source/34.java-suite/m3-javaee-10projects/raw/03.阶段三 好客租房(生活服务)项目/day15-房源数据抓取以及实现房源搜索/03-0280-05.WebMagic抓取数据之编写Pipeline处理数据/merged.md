# 05.WebMagic抓取数据之编写Pipeline处理数据

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day15-房源数据抓取以及实现房源搜索
- 源文件：03.阶段三 好客租房(生活服务)项目\day15-房源数据抓取以及实现房源搜索\05.WebMagic抓取数据之编写Pipeline处理数据【海量资源尽在 ubkz.com】.mp4
- 时长 8分40秒（音频 521s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来写一个paypal就是去处理我们拿到的一个结果那么前面呢我们是不是把这个我们的数据是不是都丢到这个page里面来对吧然后呢我们来看一下怎么样去处理它呢那么下面我们在这个位置去写一个类啊就叫比如说叫mypaypal然后呢就去paypal啊就是管道是吧line呢就一行一行就一行一行去处理我们这个数据那么点击这个ok它呢需要去实现一个接口
[00:29] 就叫什么呢PayPal然后呢是然后呢我们去实现这个里面的一个方法那么在这个方法中呢我们就可以去拿到的ResultItems那么这个ResultItems呢我们可以把它先做一个打印先做一个打印那么这样我们在这个地方打一个断点然后我们来做一个测试那么我们写完这个MyPayPal之后怎么去用呢我们就可以在这个里面就是我们刚刚写的这个卖方法这个位置
[00:58] 把这个代码格式我们简单的调整一下那么到这然后呢去加一个它点按的一个pay plannew一个刚刚我们写的my pay plan那么这样的话呢我们就把我们写这个pay planpay plan呢就加到这个里面来了然后呢我们就可以去debug启动启动它然后呢我们断点这个就通过然后呢我们要处理的呢就是在这个里面来来看一下
[01:22] 那么要注意的是在我们前面的代码中我们是不是有一个跳过来看一下那么如果我们配置中去设置了一个跳过的话它就不再进入我们PayPal来做处理这一点要注意好的我们来进入我们的PayPal来看一下那么咱们就在日志这个位置然后往下面一行走
[01:42] 打印那么可以看到在这个里面是不是就把我们刚刚所看到的信息是不是就拿到了那么在这个里面拿到信息我们是不是就可以去存文件呢存数据库呢等等那么都可以去做一些这个处理了OK那么怎么样处理呢我们来看一下我们的讲义那我们把一些相关代码我们拷贝过来那么这个就不重复了那么我们把这个挪过来然后呢去拷贝一下然后呢到这个里面来OK
[02:09] 好然后呢下面还有一些这个代码没考完那么继续拷贝一下那么我们来考完之后我们来做一个讲解看他到底在做什么事情啊呃那么还缺一些东西吧缺一个这个下载就是我们要去下载图片啊下载图片呃然后呢来看一下啊这个还是不是还缺一些东西啊我们来看一下那么这个是这个是不是一些制服的问题啊那我们先把这个格式先处理一下好那么我们把这个放大化看一下啊
[02:44] 他应该是代码格式的稍微有一点点问题那么把相关的间这个包先导入进来把这个费用这个包导入进来这个matter呢是在前面的我们需要做一个定义啊那么我把这个map拿过来这个map呢就是我们要去把我们的数据的序列化成一个json去做一个这样的一个记录到文件中所以需要一个json里面这样的一个包在那个类这个没有吗有把它导入进来哎OK
[03:13] 好那么这样的话我们来看下还有什么问题吗这个哦刚才我们是不是这个位置这个下载的这个这个方法这个拷贝的位置有问题应该丢到下面来方法在外面OK这样的话就没有问题了好那么我们来读一下这个代码这个代码应该是比较好读的那么首先我们定义了一个我们的一个map做一个这个data最终的我们需要把这个map做一个序列化也就是最终的我们需要保存到文件的时候那么保存到文件在这
[03:43] 那么需要通过这个file.tils去write写一个文件那么写到这个下面然后这个是它的一些内容最终我们需要对内容做一个做一个json的一个序列化那么我们接着继续往下面看然后下面的这一堆这个内容都是去做具体的数据的一个解析那么可以看到这个是url这个是标题这个是租金然后下面就需要做一些处理了拿到这个
[04:10] 拿到type去做需要做一些分割然后拿到的临时租赁方式怎么户型朝向然后它下面这个是info信息那么info信息就比较多了刚刚我们看到了一长串就是它的页面中的我们来找一下页面中的这个位置
[04:27] 页面中的就是这个位置这个很多这个信息那么从中要去截取出我们需要的一些信息我们通过一个空格去做一个分割然后去循环找到我们所需要的一个数据就可以了然后下面这个是获取我们的图片获取到的图片的地址然后我们去因为我们需要把这个图片下载到我们的本地
[04:54] 但有同学可能会有点不太理解就说我们不是已经拿到他的一个图片的一个链接了吗那么我们拿这个链接我们直接去用不就可以了吗干嘛我们要下载到我们本地呢是这样的这个呢我们做个测试就是说这个链接网呢他对这个URL就图片URL的一个
[05:11] 请求做了一些限制就说如果你这个链接加到你的项目中直接去访问的话是访问不了的但是你通过浏览器访问是直接是可以访问的所以说我们现在看到是可以但是如果把这个链接用到我们项目中是用不了的所以我们需要去做一个图片的一个下载然后我们给他去起一个新的名字最终的这个是以什么是以我们请求的这个URL来看一下
[05:36] 那么这个就是我们所请求的URL中它有一个这个ID其实就是这个房源这个ID那么我们以它去做了一个截取去做以这个ID就是房源这个ID作为我们的图片的一个图片名给它加一个jpg这样的一个意思然后去做一个download下载download是我们自己写的这样的一个方法去做一个下载通过httpclient去做一个下载然后下载完成之后
[06:01] 我们会把这个图片去写到我们的一个本地的磁盘的目录下面然后我们去会把这个就是我们的一个new name就是文件的一个名字再丢到我们这个data中然后去做一个序列化去得到这样的一个数据然后把这个内容再写到我们这个jsonjson这个文件中那么下面我们来看一下找一下我这个F盘下面的一个code那么F盘找一下F盘下面的一个
[06:30] 扣了下面的有一个叫做images那么这个是不是就是已经抓取过这个图片那么这样我把这个我把这个内容吧把我把这个内容全部都删掉删掉之后呢我回到头来也把这个内容的也给他删掉OK那么下面我们来去启动一下做一个测试看他会不会把数据写到这个文件中并且把这个图片的去下载到我们的本地
[06:57] 然后我就直接运行直接运行看得运行前面这个直接运行来看效果走那么看一下它会怎么样那么等待它的一个执行我们来看一下这个里面的内容有没有去下载下来目前还没有是不是现在已经有图片来了对吧有图片来了然后我们来把这个我们把这个去打开就这个文件打开我们来看一下效果把它丢到这来然后会发现是不是已经有数据了
[07:28] 那么这个数据我们随便考一条出来然后丢到我们的有一个叫Jasonville里面来找一个我们工具叫Jasonville找一个Jasonville然后我们去做这样的一个解析来看一下那么这个就是我们最终的一个抓到的一个数据对吧有图片有这个就是面积就是房屋的面积然后它户型租赁方式它的看房的时间
[07:57] 标题价格等等一些信息都拿到了并且它所对应的图片你看这个图片是肯定在我们目录中它是有对吧来看一下一个目录里面是不是有对应这个图片那么你这个Path就会不断的去运行然后就会不断的去抓取数据下来那么我们其实想要的数据是不是就是这两个数据一个就是我们JSON这样的数据另外一个是不是就是图片的数据
[08:22] OK好那么这个图片数据是不是就已经搞定了对吧包括这个文本的数据呢也就搞定了可以看到现在已经抓了有30条数据了那么其实你可以等他一会儿等他跑一会儿那么这样的一个数据呢我们就能够抓到手了OK好那么关于这个爬城的一个编写那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 WebMagic 框架编写爬虫程序，从链家网抓取房源信息并保存为 JSON 文件和图片。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 `LianjiaPageProcessor.java` 中的 `process` 方法，用于从 HTML 页面中提取标题、租金、户型、朝向、图片等信息，并调用 `page.putField` 存储。
画面 2: 展示了 `MyPipeline.java` 中的 `process` 方法，用于处理抓取到的数据，创建 `Map<String, Object> data` 并进行字段赋值。
画面 3: 在 `LianjiaPageProcessor.java` 中，添加了判断逻辑：如果提取到的标题为空，则调用 `page.setSkip(true)` 跳过当前页面。
画面 4: 在 `MyPipeline.java` 中，对 `info` 字段进行解析，提取“看房”和“楼层”信息，并分别存入 `time` 和 `floor` 字段。
画面 5: 在 `MyPipeline.java` 中，继续处理 `info` 字段，提取“看房”和“楼层”信息。
画面 6: 在 `MyPipeline.java` 中，添加了下载图片的逻辑，使用 `this.downloadFile` 下载图片并保存到指定路径，同时将图片信息存入 `data`。
画面 7: 在 `MyPipeline.java` 中，将 `data` 转换为 JSON 字符串，并写入 `F:\code\data.json` 文件。
画面 8: 展示了链家网房源详情页的网页截图，包含房屋基本信息和配套设施。
画面 9: 在 `MyPipeline.java` 中，对 `image` 字段进行处理，提取图片 URL。
画面 10: 在 `MyPipeline.java` 中，对 `image` 字段进行处理，提取图片 URL。
画面 11: 展示了下载图片的进度条，显示已下载 48%。
画面 12: 展示了下载完成后的 `images` 文件夹，其中包含两张图片文件。
画面 13: 展示了 `data.json` 文件在 JSON Viewer 中的结构，包含 `image`、`orientation`、`houseType`、`rentMethod`、`title`、`url` 等字段。
画面 14: 展示了 `data.json` 文件在 EditPlus 编辑器中的内容，包含多个房源的 JSON 数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public void process(Page page) {
    Html html = page.getHtml();
    // 房源详情页
    List<String> list = html.css(selector: ".content_list-item-title a").links().all();
    page.addTargetRequests(list);
    String title = html.xpath("//div[@class='content clear w150']/p/text()").toString();
    page.putField(key: "title", title);
    page.putField(key: "rent", html.xpath("//p[@class='content_aside-title']/span/text()").toString());
    page.putField(key: "type", html.xpath("//p[@class='content_article_table']/allText()").toString());
    page.putField(key: "info", html.xpath("//div[@class='content_article_slide_item']/img").toString());
}
```

画面 2:
```java
import us.codecraft.webmagic.ResultItems;
import us.codecraft.webmagic.Task;
import us.codecraft.webmagic.pipeline.Pipeline;

public class MyPipeline implements Pipeline {
    @Override
    public void process(ResultItems resultItems, Task task) {
        StackOverflowError (java.lang)
        StringIndexOutOfBoundsException (java.lang)
        GithubRepoPageProcessor (cn.itcast.es.wm)
        LianjiaPageProcessor (cn.itcast.es.wm)
        sout
        Prints a string to System.out
        soutp
        Prints a formatted string to System.out
        soutp
        Prints method parameter names and values to System.out
        soutv
        Prints a value to System.out
    }
}
```

画面 3:
```java
if (page.getResultItems().get("title") == null) {
    page.setSkip(true);
}
```

画面 4:
```java
data.put("title", resultItems.get("title")); //标题
data.put("rent", resultItems.get("rent")); //租金
String[] types = StringUtils.split(resultItems.get("type"), ' '); //户型
data.put("rentMethod", types[0]); //租赁方式
data.put("houseType", types[1]); //户型，如：2室1厅1卫
data.put("orientation", types[2]); //朝向
String[] infos = StringUtils.split(resultItems.get("info"), separatorChar: ' ');
for (String info : infos) {
    if (StringUtils.startsWith(info, prefix: "看房：")) {
        data.put("time", StringUtils.split(info, separatorChar: ':')[1]);
    } else if (StringUtils.startsWith(info, prefix: "楼层：")) {
        data.put("floor", StringUtils.split(info, separatorChar: ':')[1]);
    }
}
```

画面 5:
```java
String image = StringUtils.split(resultItems.get("img"), separatorChar: '"')[3];
String newName = StringUtils.substringBefore(StringUtils.substringAfterLast(resultItems.getRequest().getUrl(), separator: "/"), separator: ".");
```

画面 6:
```java
try {
    this.downloadFile(imageUrl, new File(pathname: "F:\code\images\\" + newName));
    data.put("image", newName);
    String json = MAPPER.writeValueAsString(data);
    FileUtils.write(new File(pathname: "F:\code\data.json"), data: json + "\n", encoding: "UTF-8", append: true);
} catch (Exception e) {
    e.printStackTrace();
}
```

画面 7:
```java
String json = MAPPER.writeValueAsString(data);
FileUtils.write(new File(pathname: "F:\code\data.json"), data: json + "\n", encoding: "UTF-8", append: true);
```

画面 8: 无代码。

画面 9:
```java
String image = StringUtils.split(resultItems.get("img"), separatorChar: '"')[3];
String newName = StringUtils.substringBefore(StringUtils.substringAfterLast(resultItems.getRequest().getUrl(), separator: "/"), separator: ".");
```

画面 10:
```java
String image = StringUtils.split(resultItems.get("img"), separatorChar: '"')[3];
String newName = StringUtils.substringBefore(StringUtils.substringAfterLast(resultItems.getRequest().getUrl(), separator: "/"), separator: ".");
```

画面 11: 无代码。

画面 12: 无代码。

画面 13:
```json
{
    "image": "SH210919638597144832.jpg",
    "orientation": "10m",
    "houseType": "2室1厅1卫",
    "rentMethod": "整租",
    "title": "整租",
    "url": "https://sh.lianjia.com/zu/SH210919638597144832.html"
}
```

画面 14:
```json
{
    "image": "SH213046324401363916.jpg",
    "orientation": "33m",
    "houseType": "1室1厅1卫",
    "rentMethod": "整租",
    "title": "整租",
    "url": "https://sh.lianjia.com/zu/SH213046324401363916.html"
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

