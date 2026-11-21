# 26_用户行为功能_控制器编写及业务层代码思路分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\26_用户行为功能_控制器编写及业务层代码思路分析【海量资源尽在 666java.com】.mp4
- 时长 7分19秒（音频 439s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好目前的话咱们已经把这个接口给定义出来了下面咱们就来定一个控制器来实现当前这个接口咱们还是在当前的这种行为的微服务下边去创建一个控制器它的控制器叫behaviour是吧Controller好让它去实现刚才定义的接口implementbehaviourcontrollerapi是吧control i然后在上面去加一个什么加什么路线叫restcontroller好吧
[00:34] 然后下面是有一个requestmyping请求映射咱们这个咋呢跟之前是差不多的叫api开头的然后是给个给一个半个号v1然后再去就是满模块就是behind好那这样的话咱们就设置完了啊在这里边主要是干啥事呢这个控制器里边控制器里边的主要呢就是咱们要去做保存是吧咱们这啊也在这也给他给一个这东西啊那这个咱们叫啥呢
[01:05] 我们的save我们的behaviour那这个咱们里边刚说了咱们需要去需要去设置保存就可以所以说咱们在这去创建一个serviceprivate然后是什么来着pp是吧是请名字叫behaviourvior Service行咱们需要注入一下虽然没有关系我们可以把它给创建出来
[01:41] 创建一个 interface找到当前的Service包下面这个接口就算是创建创建出来了然后咱们再回到当前的方法里边它只需要去调用一个方法就可以了直接去调用当前的保存操作就可以了保存的话咱们的参数就是BTO没问题然后最终咱们要去把这个方法给创建出来
[02:13] 创建出来之后呢,这只是接口是吧,咱们需要用实现类来去实现所以说咱们在这再去创建一个类这个类是app-show-dehiver然后是Service-app-show-dehiver,没有问题,点OK然后这时候让它去实现当前的接口app-show-Service
[02:43] 那这儿咱们还要再加个助理叫什么叫serviceOK那这里边呢这里边咱们需要去做哪些事呢需要做哪些事啊大家来想一想之前咱们的步骤是分析过的是吧首先要干嘛呢你看我们再来看一下首先是获取用户信息获取设备IDOK那这个设备ID咱们已经可以拿到用户信息怎么获取来说一下获取用户信息
[03:15] 而获取了吗获取设备ID那用户信息怎么拿我们之前在讲那个Article的时候是不是讲过说用户信息是不是可以通过一个工具类在SlideLocal中去可以获取到用户信息啊OK没问题啊然后第二步要干嘛呢再来看一下啊要去查询根据当前的设备ID和用户信息去查询行为实体根据当前的用户信息获
[03:46] 或您要注意啊或设备ID查询行为肢体行为肢体咱们都知道啊行为肢体就是保存什么东西看一下就是保存了当前用户的ID和用户的设备ID设备ID就是手机的编号信息刚才咱们说了啊当前用户用户登录之后呢是保存了用户的ID
[04:13] 如果说用户没有登录咱们保存的是手机的编号ID那这个ID呢就是咱们也可以通过这个ID进行推荐没问题好吧然后呢咱们来看第三步啊是获取啥呢获取前台传递过来的什么文章列表文章列表好那这是第三步那第四步呢看一看啊第四步的话呢咱们就要去
[04:48] 根据当前的文章ID类表和设备ID查询APP文章展现行为表那这是啥意思呢好来看一下啊咱们还是要打开当前这个表那这个表里边啊它说的是查询当前这个表根据什么查呢根据当前的一个叫什么一个叫做设备ID另外一个呢另外也是要根据当前的一个文章的ID文章的ID最终的是查询当前的这个类表信息
[05:17] 好那咱们来写一下啊据什么设备ID那这个设备ID跟当前这个设备ID不是一个ID大家一定要注意啊这个设备ID是行为实体的ID行为实体ID然后和什么呢和文章列表ID查询APP什么行为表行为表啊这是实体是行为表这个表对应的是谁啊
[05:55] 就是AP哪个就是AP数台湾这边对应谁啊这边对应的是当前的这个实体链好大家注意听啊这个很容易乱这一块啊行拿到他之后要干嘛呢我们要去做过滤数据的过滤那过滤啥呢通点过滤OK那你看之前呢已经拿到了文章列表的ID然后这里边呢他通过查询的之后呢咱们还可以再去拿到另外一个
[06:32] 对吧那个ID呢就是还可以查到文章的ID那该怎么过滤呢就是说啊咱们需要需要干嘛呢需要删除什么东西需要删除已经删除表中已经存在的ID就是文章ID文章ID也就是说从这个里边去过滤从前台里边去过滤这个里边找有没有有就删除没有的话
[07:06] 咱们就存下来最终存下来的数据要干嘛呢要进行保存操作好那这个呢咱们就把这个步骤给写了一下一会儿咱们再来去实现这个步骤好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何为“用户点击文章行为”功能开发对应的控制器和业务服务层代码，并配合数据库表结构设计。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了接口定义文件 BehaviorControllerApi.java，其中定义了 saveShowBehavior 方法，接收 ShowBehaviorDto 参数并返回 ResponseResult。
画面2: 展示了控制器实现类 BehaviorController.java 的开头，正在导入 Spring MVC 相关的注解。
画面3: 展示了 BehaviorController.java 中的 saveShowBehavior 方法，方法体为空，仅返回 null。
画面4: 展示了 BehaviorController.java 中添加了 @RestController 和 @RequestMapping 注解，并定义了 saveShowBehavior 方法。
画面5: 展示了在 IntelliJ IDEA 中弹出的“选择目标包”对话框，用户正在将类移动到 com.heima.behavior.Controller.v1 包下。
画面6: 展示了 BehaviorController.java 中添加了私有成员变量 appShowBehaviorService，并在 saveShowBehavior 方法中调用它。
画面7: 展示了右键菜单中选择“新建”并创建 AppShowBehaviorService 接口。
画面8: 展示了 AppShowBehaviorService.java 文件，定义了 saveShowBehavior 方法。
画面9: 展示了 AppShowBehaviorService.java 文件，定义了 saveShowBehavior 方法。
画面10: 展示了 PPT 页面，标题为“7.3.4 行为相关功能开发”，其中包含“ShowBehaviorDto”类的定义和行为逻辑的“思路分析”流程图。
画面11: 展示了 PPT 页面，标题为“行为实体”，内容为“主要是保存了用户id或设备的id（手机的编号信息）”，并附有流程图。
画面12: 展示了 AppShowBehaviorServiceImpl.java 文件，方法体为空，仅返回 null。
画面13: 展示了 Navicat for MySQL 中的 SQL 语句，用于创建表 ap_show_behavior。
画面14: 展示了 AppShowBehaviorServiceImpl.java 文件，方法体中添加了注释，说明了获取用户信息、获取文章列表等操作。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1:
```java
package com.heima.article.apis;

import com.heima.model.behavior.dto.ShowBehaviorDto;
import com.heima.model.common.dto.ResponseResult;

public interface BehaviorControllerApi {
    /**
     * 用户点击文章的行为
     */
    ResponseResult saveShowBehavior(ShowBehaviorDto dto);
}
```

画面2:
```java
package com.heima.behavior.Controller.v1;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.bind.annotation.GetMapping;
import org

