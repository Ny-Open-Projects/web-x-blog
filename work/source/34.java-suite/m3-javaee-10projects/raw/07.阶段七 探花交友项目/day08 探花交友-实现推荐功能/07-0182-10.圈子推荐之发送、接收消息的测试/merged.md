# 10.圈子推荐之发送、接收消息的测试

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\10.圈子推荐之发送、接收消息的测试_【海量资源尽在 666java.com】.mp4
- 时长 6分56秒（音频 415s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么接下来呢我们就来测试一下这个消息的发送啊以及消息的一个接收处理那么接下来呢我们把我们的服务呢都跑起来啊一个是double服务SSO还有server还有recmend然后呢我们首先呢找到我们的server啊然后呢我们去打断点那么找到Controller然后在我们的这个moments里面去打一个断点
[00:25] 然后呢我们再进入到我们的recommend中去打断点就是就message啊这个里面来然后呢我们在上面这个位置啊来打个断点好那么接下来呢我们就来测试一下啊那么首先呢我们先来去做登录啊先来去做一个登录然后呢走去做一个发送验证码发送成功了那么接下来呢我们就来去去登录一下啊走
[00:54] 它应该能够去登录成功了好登录成功之后那么这个就是这个我们所需要的这个token然后呢拿到之后那么接下来呢我们就去做一个上传那么我们找到找到我们的这个往下面走吧对着啊哎哎错了那么就是在下面这个位置那么之前这个呢测试过然后呢我们就直接来看一下
[01:21] 那么这个就是这个就是我们这个token然后呢下面呢就是我们的这个内容啊这个内容然后呢这个是我们的这个写的一些内容然后呢我们会传一个文件啊那么文件名是什么呢我们可以来找一下我们这个Controller那么这个Controller中呢来看一下这个这个是query对吧我们找到我们的这个新增来找一下啊那么新增的是在这然后呢文件名就是
[01:49] 这个image contact好那我们就传一个图片上来然后我们就随便来一个就可以了比如说就这个然后当然你可以多个那么我们再来写一个比如说写一个他随便选两个然后点击send发送好那么这个时候可以看到请求是不是进入我们的Controller然后我们继续往下面走那么这个断点我们就要去掉了然后我们就直接往下面走吧走走走走
[02:19] 然后我们走走走这个是处理图片对吧做一个图片上传我们有两张这个图片那我们跟一下它的一个支线的流程两张图片OK没有问题塞进去然后通过我们的圈子API做一个save保存保存的mongoDB那么可以看到现在是不是已经就返回了这个ID了对吧然后我们判断一下不为空那么就OK了然后走到这个位置就去发送我们的消息
[02:48] 那么调用了这个方法中呢然后去调用this.send a message然后去做一个发送那么我们去查询啊这个是查询public对象那么显然这个时候肯定是能够去查询到啊查询到这个数据然后呢我们接着继续往下面看走走走去做一个数据的一个分装然后呢去做一个消息的一个发送那么走到这里呢哎他已经来了啊这个是我们消息接收了啊那我们先回到这个里面来
[03:17] 那么先通过那么看一下我们这个请求是不是就是200OK没有问题好那么回到我们的这个Recommend中消息是不是就接收到了对吧我们来看一下走去做一个我们的一个解析然后拿到type然后拿到这个publish id来看一下那么这个就是publish id没有问题往下面走然后拿到date拿到usid拿到pid
[03:45] 然后呢往下面走走走啊走走然后呢去做一个space操作然后呢再去查询用publish对象查到之后呢看它的长度啊那么这个长度是7那么符合第一个这个条件那么得分的是1然后呢我们的图片有两个对吧那么最后得分应该是3看一下对不对啊哎3没有问题然后呢继续往下面走set到这个score中然后呢去做一个保存
[04:14] OK那么这样的话就保存成功了好那么接下来呢我们来看一下我们的MangoDB中有没有数据来刷新一下那么我们来找一下找一下数据呢是在这儿然后呢来看这个应该是错了应该是这个这条数据那么这个是我们刚刚所保存的一条数据来看一下那么也就是说我们呢目前有一个这个用户用户ID唯一的这个用户对一个圈子做了一个对圈子动态做一个操作圈子动态呢是4
[04:44] 然后得分的是一个三分这样的一个操作时间是这样的一个时间OK好那么显然可以看到我们这个流程是不是基本上OK的对吧那么这个是保存是OK的那么接下来我们就来测试一下测试一下什么我们先来找到我们的这条数据就是我们的PID为4的这条数据来找一下那么就是在这条
[05:11] 是这个啊那么他的ID呢就是这样的一个ID那么接下来呢我们就对他做一些这个点赞呢还有些喜欢呢啊这样的一些操作啊那么往下面走那我们来找一下啊比如说呢我们就去做一个点赞啊其他的都非常的类似了啊那么ID呢就是我们把这个ID拷贝到这个里面来作为get请求走那么哎消息又来了直接通过吧好那我们来看一下我们刚刚的这个
[05:39] 就是我们的这个数据啊来刷新一下显然是不是有两条数据了对吧那么可以看到这个操作呢是用户ID唯一的这个用户对public ID为4的这个动态的做一个得分为5的这样的一个操作那么当然了我们还可以去做一个dislike那么就是做一个取消啊取消这个点赞那么通过
[06:02] 好那么我们再来刷新一下看一下这个效果啊那么基本一样又来一条对吧然后呢这个是-5这个操作那么就相当于把前面这个底消掉了呃然后呢我们也可以去做一些什么呢比如说浪就是做这个喜欢啊这个操作走好那么这个呢肯定他也就成功了啊来看一下那是不是又来一条啊就是这个8ok那么到这呢基本上呢我们就能够去呃看到这样的效果就可以
[06:30] 只要用户呢对我们这个动态的这个消息数据啊那么做各种各样的操作呢我们都会去记录到我们当前这张表里面来然后呢我们后面其实只要通过这张表的数据我们去做一个计算做一个推荐啊是不是就OK了对吧好那么关于我们这个消息的一个发送啊以及这个处理的一个这样的一个测试呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的推荐系统如何通过消息队列（MQ）接收用户动态并将其数据持久化到 MongoDB 数据库的过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了推荐服务的启动类 RecommendApplication，其中调用 SpringApplication.run() 启动应用。
画面 2: 展示了消息消费者 QuanzIMsgConsumer 中的 switch-case 语句，根据消息类型设置推荐分数。
画面 3: 使用 Advanced REST Client 发送一个 JSON 格式的消息，请求路径为 /imovements，响应状态码为 200。
画面 4: 展示了 MovementsController 中的 @GetMapping 注解方法，用于根据 ID 查询动态信息，并在查询后调用 quanziMQService 发送消息。
画面 5: 在 Advanced REST Client 中选择上传图片文件，准备发送包含图片的请求。
画面 6: 展示了 MovementsService 中处理图片上传的代码，创建 Publish 对象并设置用户信息、位置和图片 URL。
画面 7: 展示了 MovementsController 中的 saveMovements 方法，接收请求参数并调用 quanziMQService 发送保存消息。
画面 8: 展示了 QuanziMQService 中的 sendMag 方法，用于发送消息。
画面 9: 使用 Advanced REST Client 发送包含多个图片文件的 multipart/form-data 请求，响应状态码为 200。
画面 10: 展示了 QuanzIMsgConsumer 中的 onMessage 方法，解析接收到的 JSON 消息并创建 RecommendQuanzi 对象。
画面 11: 展示了 QuanzIMsgConsumer 中的 save 方法，将 RecommendQuanzi 对象保存到 MongoDB 的 recommend_quanzi 集合中。
画面 12: 在 Robo 3T 数据库客户端中，执行 db.getCollection('recommend_quanzi').find() 查询推荐集合。
画面 13: 在 Robo 3T 中，执行 db.getCollection('recommend_quanzi').find() 查询并显示了推荐集合中的文档内容。
画面 14: 在 Robo 3T 中，显示了查询到的推荐集合中包含的多个文档，其中包含用户 ID、发布 ID、分数和日期等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class RecommendApplication {
    public static void main(String[] args) {
        SpringApplication.run(RecommendApplication.class, args);
    }
}
```

画面 2:
```java
case 6: {
    recommendQuanzi.setScore(-5d);
    break;
}
case 7: {
    recommendQuanzi.setScore(-8d);
    break;
}
default: {
    recommendQuanzi.setScore(0d);
    break;
}
```

画面 3:
```json
{
    "pcode": "1982020981",
    "writeCode": "112368"
}
```

画面 4:
```java
@GetMapping("{id}")
    ResponseEntity<Movements> queryMovementsById(@PathVariable("id") String id) {
        try {
            Movements movements = this.movementsService.queryMovementsById(id);
            if (null != movements) {
                //发送消息
                this.quanziMQService.sendQueryPublishMsg(publishId);
                return ResponseEntity.ok(movements);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
    }
```

画面 6:
```java
String longitude, latitude = "11.11", "22.22";
MultipartFile[] multipartFile) {
    User user = UserThreadLocal.get();
    publish = new Publish();
    publish.setUserId(user.getId());
    publish.setMobile(user.getMobile());
    publish.setLatitude(latitude);
    publish.setLongitude(longitude);
    publish.setText(content);
    publish.setLocationName(location);
    publish.setPublishId(publishId);
    publish.setPublishTime(new Date());

    //图片上传
    List<String> imageUrls = new ArrayList<>();
    for (MultipartFile file : multipartFile) {
```

画面 7:
```java
try {
    String publishId = this.movementsService.saveMovements(
            @RequestParam("location") String location,
            @RequestParam("latitude") String latitude,
            @RequestParam("longitude") String longitude,
            @RequestParam("textContent") String textContent,
            @RequestParam("imageUrls") List<String> imageUrls
    );
    if (StringUtils.isNotEmpty(publishId)) {
        this.quanziMQService.sendSavePublishMsg(publishId);
        return ResponseEntity.ok(null);
    }
} catch (Exception e) {
    e.printStackTrace();
}
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
```

画面 8:
```java
private void sendMag(Integer type, String publishId) {
    publish = new Publish();
    publish.setType(type);
    publish.setPublishId(publishId);
    publish.setPublishTime(new Date());
    publish.setUserId(user.getId());
    publish.setMobile(user.getMobile());
    publish.setLocationName(location);
    publish.setLatitude(latitude);
    publish.setLongitude(longitude);
    publish.setText(content);
    publish.setImageUrls(imageUrls);
    publish.setPublishTime(new Date());
}
```

画面 10:
```java
@Override
public void onMessage(String msg) {
    try {
        JsonNode jsonNode = MAPPER.readTree(msg);
        int type = jsonNode.get("type").asInt();
        String publishId = jsonNode.get("publishId").asText();
        Long date = jsonNode.get("date").asLong();
        Long userId = jsonNode.get("userId").asLong();
        String pid = jsonNode.get("pid").asText();
        RecommendQuanzi recommendQuanzi = new RecommendQuanzi();
        recommendQuanzi.setPublishId(publishId);
        recommendQuanzi.setUserId(userId);
        recommendQuanzi.setScore(3.0);
        recommendQuanzi.setDate(date);
        recommendQuanzi.setClass(pid);
        recommendQuanzi.setPublishTime(new Date());
        recommendQuanzi.setPublishId(publishId);
        recommendQuanzi.setUserId(userId);
        recommendQuanzi.setScore(3.0);
        recommendQuanzi.setDate(date);
        recommendQuanzi.setClass(pid);
        recommendQuanzi.setPublishTime(new Date());
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

画面 11:
```java
// 将数据写入到MongoDB
String collectName = "recommend quanzi" + new DateTime().toString();
this.mongoTemplate.save(recommendQuanzi, collectName);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

