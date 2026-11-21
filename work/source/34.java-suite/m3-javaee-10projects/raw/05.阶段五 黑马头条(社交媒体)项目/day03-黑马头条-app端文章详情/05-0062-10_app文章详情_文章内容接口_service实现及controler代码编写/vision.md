# 画面线理解：10_app文章详情_文章内容接口_service实现及controler代码编写

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\10_app文章详情_文章内容接口_service实现及controler代码编写【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:48, 01:21, 01:44, 02:16, 02:52, 03:27, 03:58, 04:20, 04:47, 05:46, 06:14, 06:52, 07:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:11:46

1) 这一组画面整体在讲如何在 Spring Boot 项目中实现文章信息的查询服务，包括服务层的参数校验、配置与内容映射，以及控制器层的接口定义与调用。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 AppArticleInfoServiceImpl.java 中，对 articleId 参数进行初步校验，若为空或小于1则返回错误结果。
画面 2: 在 AppArticleInfoServiceImpl.java 中，添加了 articleId 的非空和小于1的校验逻辑。
画面 3: 在 AppArticleInfoServiceImpl.java 中，引入了 @Autowired 注解，并声明了 apArticleConfigMapper 和 apArticleContentMapper 两个私有成员变量。
画面 4: 在 AppArticleInfoServiceImpl.java 中，为两个 Mapper 接口变量添加了 @Autowired 注解。
画面 5: 在 AppArticleInfoServiceImpl.java 中，为 apArticleConfigMapper 变量添加了 @Autowired 注解。
画面 6: 在 AppArticleInfoServiceImpl.java 中，为 apArticleContentMapper 变量添加了 @Autowired 注解。
画面 7: 在 AppArticleInfoServiceImpl.java 中，声明了一个 Map<String, Object> 类型的 data 变量，并开始编写业务逻辑。
画面 8: 在 AppArticleInfoServiceImpl.java 中，完成对 apArticleConfigMapper 的赋值和校验逻辑。
画面 9: 在 AppArticleInfoServiceImpl.java 中，完成对 apArticleContentMapper 的赋值和校验逻辑。
画面 10: 在 IDEA 中，右键点击 com.heima.article 包，选择“Create New Class”创建新类。
画面 11: 在 IDEA 中，右键点击 com.heima.article.controller.v1 包，选择“New” -> “Interface” 创建接口。
画面 12: 在 ArticleInfoControllerApi.java 中，定义了接口方法 loadArticleInfo。
画面 13: 在 ArticleInfoControllerApi.java 中，为 loadArticleInfo 方法添加了 @RequestMapping 注解。
画面 14: 在 ArticleInfoController.java 中，为 loadArticleInfo 方法添加了 @RequestMapping 注解，并调用 service 层方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.heima.article.service.impl;
import com.heima.article.service.AppArticleInfoService;
import com.heima.model.common.dtos.ResponseResult;
import org.springframework.stereotype.Service;

@Service
public class AppArticleInfoServiceImpl implements AppArticleInfoService {
    @Override
    public ResponseResult getArticleInfo(Integer articleId) {
        //根据文章id查询config的信息
        //判断当前文章是否删除
        return null;
    }
}
```

画面 2:
```java
if(articleId == null || articleId < 1) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 3:
```java
@Autowired
private ApArticleConfigMapper apArticleConfigMapper;
@Autowired
private ApArticleContentMapper apArticleContentMapper;
```

画面 4:
```java
@Autowired
private ApArticleConfigMapper apArticleConfigMapper;
@Autowired
private ApArticleContentMapper apArticleContentMapper;
```

画面 5:
```java
@Autowired
private ApArticleConfigMapper apArticleConfigMapper;
```

画面 6:
```java
@Autowired
private ApArticleContentMapper apArticleContentMapper;
```

画面 7:
```java
Map<String, Object> data = new HashMap<>();
```

画面 8:
```java
if(apArticleConfig == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 9:
```java
else if(!apArticleConfig.getIsDelete()) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID);
}
```

画面 10:
```java
// Create New Class
Name: 
Kind: Interface
```

画面 11:
```java
public interface ArticleInfoControllerApi {
    public ResponseResult loadArticleInfo(ArticleInfoDto dto);
}
```

画面 12:
```java
public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
    return null;
}
```

画面 13:
```java
@RequestMapping("/api/v1/article")
public class ArticleInfoController implements ArticleInfoControllerApi {
    @Autowired
    private AppArticleInfoService appArticleInfoService;
    @Override
    public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
        return appArticleInfoService.getArticleInfo(dto.getArticleId());
    }
}
```

画面 14:
```java
@RequestMapping("/api/v1/article")
public class ArticleInfoController implements ArticleInfoControllerApi {
    @Autowired
    private AppArticleInfoService appArticleInfoService;
    @Override
    public ResponseResult loadArticleInfo(ArticleInfoDto dto) {
        return appArticleInfoService.getArticleInfo(dto.getArticleId());
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
