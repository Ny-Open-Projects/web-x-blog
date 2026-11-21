# 画面线理解：10.圈子推荐之发送、接收消息的测试

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\10.圈子推荐之发送、接收消息的测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:33, 01:03, 01:37, 01:56, 02:18, 02:37, 03:01, 03:21, 03:46, 04:11, 05:09, 05:39, 06:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:57:15

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
