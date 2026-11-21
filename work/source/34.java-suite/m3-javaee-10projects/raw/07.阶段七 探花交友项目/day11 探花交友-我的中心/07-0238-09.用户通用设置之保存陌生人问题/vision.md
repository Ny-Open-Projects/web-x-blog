# 画面线理解：09.用户通用设置之保存陌生人问题

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\09.用户通用设置之保存陌生人问题_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 00:52, 01:37, 02:53, 03:28, 04:24, 04:49, 05:21, 05:41, 07:46, 08:16, 09:12, 09:41, 10:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:42:20

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现用户保存问题功能，包括 Controller、Service 层代码编写、数据库操作以及相关配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Typora 文档中 UsersController 的 saveQuestions 方法，用于接收前端 POST 请求并调用 UserService。
画面 2: 展示 Mock 服务接口文档，用于测试保存问题功能，包含请求头和请求体参数。
画面 3: 展示 IntelliJ IDEA 中 UserService.java 文件，代码中包含用户点赞通知等逻辑。
画面 4: 展示 QuestionService.java 文件，代码中包含查询问题的逻辑。
画面 5: 展示 QuestionService.java 文件，代码中包含保存问题的逻辑，判断问题是否存在。
画面 6: 展示 QuestionService.java 文件，代码中对问题对象进行 set 操作。
画面 7: 展示 QuestionService.java 文件，代码中对问题对象进行 set 操作，选中了 setId 方法。
画面 8: 展示 IntelliJ IDEA 中右键菜单，选择“Replace in Path...”进行全局替换。
画面 9: 展示 MyMetaObjectHandler.java 文件，代码中实现 insertFill 方法，为 created 和 updated 字段赋值。
画面 10: 展示 MyMetaObjectHandler.java 文件，代码中实现 insertFill 方法，为 created 和 updated 字段赋值。
画面 11: 展示手机端应用界面，用于演示功能。
画面 12: 展示 Navicat 数据库管理工具，显示 tb_question 表中的数据。
画面 13: 展示 Typora 文档中 UsersService 和 QuestionService 的代码。
画面 14: 展示 Typora 文档中黑名单表结构的 SQL 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 设置陌生人问题
 */
@GetMapping("/questions")
public ResponseEntity<Void> saveQuestions(@RequestBody Map<String, String> param) {
    try {
        String content = param.get("content");
        this.userService.saveQuestions(content);
        return ResponseEntity.ok(null);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面 3:
```java
User user = UserThreadLocal.get();
this.questionService.save(user.getId(), content);
```

画面 4:
```java
@Service
public class QuestionService {
    @Autowired
    private QuestionMapper questionMapper;
    ...
}
```

画面 5:
```java
public void save(Long userId, String content) {
    //判断问题是否存在，如果存在，进行修改，如果不存在，就新增操作
    Question question = this.queryQuestion(userId);
    if(null != question) {
        question.setTxt(content);
        this.questionMapper.updateById(question);
    }else{
        question = new Question();
        question.setUserId(userId);
        question.setTxt(content);
        this.questionMapper.insert(question);
    }
}
```

画面 9:
```java
@Component
public class MyMetaObjectHandler implements MetaObjectHandler {

    @Override
    public void insertFill(MetaObject metaObject) {
        Object created = getFieldValueByName("created", metaObject);
        if(null == created) {
            //字段为空，可以进行赋值
            setFieldValueByName("created", new Date(), metaObject);
        }
        Object updated = getFieldValueByName("updated", metaObject);
        if(null == updated) {
            //字段为空，可以进行赋值
            setFieldValueByName("updated", new Date(), metaObject);
        }
    }
}
```

画面 14:
```sql
CREATE TABLE `tb_black_list` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) DEFAULT NULL,
  `black_user_id` bigint(20) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='黑名单';
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
