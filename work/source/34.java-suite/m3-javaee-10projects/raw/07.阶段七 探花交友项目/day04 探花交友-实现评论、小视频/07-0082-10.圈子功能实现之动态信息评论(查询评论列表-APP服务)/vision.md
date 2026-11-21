# 画面线理解：10.圈子功能实现之动态信息评论（查询评论列表-APP服务）

- 阶段：07.阶段七 探花交友项目
- 章节：day04 探花交友-实现评论、小视频
- 源文件：07.阶段七 探花交友项目\day04 探花交友-实现评论、小视频\10.圈子功能实现之动态信息评论（查询评论列表-APP服务）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 02:19, 03:56, 05:11, 06:38, 08:21, 09:26, 10:30, 11:59, 13:16, 14:40, 15:44, 16:41, 18:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:54:44

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Mock 服务中定义一个评论列表接口，并在后端 Java 代码中实现该接口的 Controller 和 Service 层逻辑，包括参数绑定、分页、用户信息关联和数据格式化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Mock 服务界面中，查看接口基本信息，接口路径为 /comments，请求方式为 GET，Mock 地址为 https://mock.boxuegu.com/mock/164/comments，请求头包含 Content-Type: application/json 和 Authorization: Bearer 令牌。
画面 2: 在 Mock 服务界面中，点击“评论列表”后，弹出一个包含多个开发环境截图的预览窗口，展示代码和界面。
画面 3: 在 IntelliJ IDEA 中，打开 CommentsController.java 文件，显示了 @RequestMapping 和 @RequestParam 注解的使用。
画面 4: 在 IntelliJ IDEA 中，展示 CommentsController.java 文件中 queryCommentsList 方法的完整代码，包括 @GetMapping 注解和参数绑定。
画面 5: 在 IntelliJ IDEA 中，打开 CommentsService.java 文件，显示了 @Service 注解和 @Autowired 注解的使用。
画面 6: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的开始部分，包括 PageResult 的声明和初始化。
画面 7: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 quanZiApi 的调用和 PageResult 的赋值。
画面 8: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 QueryWrapper 的创建和 userInfoService 的调用。
画面 9: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 PageResult 的声明和初始化。
画面 10: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setCreateDate 的代码和日期格式化。
画面 11: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setLikeCount 和 comments.setHasLiked 的代码。
画面 12: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setLikeCount 和 comments.setHasLiked 的代码。
画面 13: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setCreateDate 的代码和日期格式化。
画面 14: 在 IntelliJ IDEA 中，展示 CommentsService.java 文件中 queryCommentsList 方法的中间部分，包括 comments.setCreateDate 的代码和日期格式化。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("comments")
public class CommentsController {

    @Autowired
    private CommentsService commentsService;

    @GetMapping
    public PageResult queryCommentsList(@RequestParam("movementId") String publishId,
                                        @RequestParam(value = "page", defaultValue = "1") Integer page,
                                        @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
        PageResult_pageResult this.commentsService.queryCommentsList(publishId, page, pageSize);
    }
}
```

画面 4:
```java
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("comments")
public class CommentsController {

    @Autowired
    private CommentsService commentsService;

    @GetMapping
    public PageResult queryCommentsList(@RequestParam("movementId") String publishId,
                                        @RequestParam(value = "page", defaultValue = "1") Integer page,
                                        @RequestParam(value = "pagesize", defaultValue = "10") Integer pageSize) {
        PageResult_pageResult this.commentsService.queryCommentsList(publishId, page, pageSize);
    }
}
```

画面 5:
```java
package com.tanhua.server.service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Autowired
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 6:
```java
package com.tanhua.server.service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 7:
```java
package com.tanhua.server.service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 8:
```java
package com.tanhua.server.service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 9:
```java
package com.tanhua.server.service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 10:
```java
package com.tanhua.server.service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 11:
```java
package com.tanhua.server.service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList<>();
        if (CollectionUtils.isEmpty(records)) {
            return null;
        }
        return pageResult;
    }
}
```

画面 12:
```java
package com.tanhua.server.service;

import com.tanhua.dubbo.server.api.QuanZiApi;
import com.tanhua.server.vo.PageResult;
import org.springframework.stereotype.Service;

@Service
public class CommentsService {

    @Reference(version = "1.0.0")
    private QuanZiApi quanZiApi;

    public PageResult queryCommentsList(String publishId, Integer page, Integer pageSize) {
        PageResult pageResult = new PageResult();
        PageInfo<Comment> pageInfo = new PageInfo<>();
        List<Comment> records = new ArrayList
