# 21-部署流程：代码编写

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\21-部署流程：代码编写_【海量资源尽在 ubkz.com】.mp4
- 时长 13分12秒（音频 792s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那我们现在已经把这个数据源相应的部分呢咱们已经搞定了那我们回到讲义一起来看一下接下来我们就要完成比较重要的一块内容就是要做一个流程的部署对于这个流程的部署呢其实很简单了就是我们把刚才已经自己制作好的这个请假的文件上传到我们的服务器当中
[00:29] 那说的直白一点上传到我们的这个工程上那接下来呢通过它内置的一些接口那把这个工程的文件呢解析好接着把数据传入到数据库当中当然这些呢都是activity它暴露的一些接口直接对象打点调方法就自动执行了那所以这个上传的逻辑还是比较简单的那我们来看一下这些应该怎么去做
[00:59] 首先呢回到我们这边的ID工程当中那相应的位置呢咱们就开始配置代码那首先呢配置一个包我们叫做Controller c1 t r o l 1 e rcontroller那在Controller当中配置对应的一个叫什么名字呢注意咱们就叫process Controller了p o c e s scontroller c1 t r o l 1 e rcontrollerOK
[01:32] 那注意这个里面呢全部都写的是我们的流程流程控制的Controller啥意思呢就是说啊咱流程是不是对应的就是工作流activity里面那个表啊所以对里面的一些上传部署它里面还可以进行删除查看列表等等等等我就放到这个里面了业务的审批咱们一会儿再去配置一个Controller去完成业务相关的代码配置两个OK啊抱歉这个包哎选错了
[02:06] 拿过来那接下来呢咱们这个上面呢可以去配置相应的一些注解了好了来cross好了这个代表的是我们解决跨域问题好了接着来request Controller那接下来add request mapping那对于这个request mapping我们就开始了value等于配置一个我们刚才说过了请求所有都是user开头的那对于这里面呢我们还可以配置process
[02:35] 这个对应的全部都是我们流程处理所涉及到的一些接口方法OK好了那接下来我们在底下开始完成第一个就是我们的部署新流程而那对于这个部署新流程当然了这里面也可以自动的进行流程更新我就写就是部署流程了那对于这个里面呢咱们需要各位注意的这个部署流程指的是前端将我们
[03:08] 绘制好的流程模型图我们虽然知道它叫流程模型图但是其实直白一点就是我们的文件就是BPMN文件没错了就是把我们这个BPMN文件上传到我们的方法当中所以我们这个方法写起来就很简单了
[03:41] 我们配置一个方法这个方法呢必然要接触参数而这个参数是不是就是一个文件啊好了所以这边的我们有参数参数代表的就是我上传的文件那在Spring这个boot当中我们上传的文件全部都是使用multipartfill来完成的multipart
[04:08] multiple fill 来完成的ok 好了那接下来咱们开始把这个方法呢给它定义出来at request mapping我们的请求路径哎咱们就叫做 deploy部署 deployok 配置一个方法public result 公共的接口返回值resultok 那配置这个方法名呢就叫做 deploy process好了把这个名称 control c 靠过来 control v
[04:41] OK为了不报错呢我先把返回值给它写出来return new一个result那我们之前定义过如果是一个成功的result我们这边就可以result code.success这个代表的是返回成功那接下来中间我们的代码以及我们的参数都需要给它补充完整好了at request request paramrequest param好了这边定义一下我这边呢需要传递过来一个参数叫做fill
[05:13] 好了代表的是一个money part fill我们来选一下当然了这边说一下如果这个文件名称注意这边这个对象的参数名称是不是叫fill那这个fill其实跟上面前面这个fill是一致的什么意思是这样的就是你传递这个文件的时候文件名称必须叫fill如果你这个fill名称保持一致其实这玩意可以删掉当然了我这边就不写了
[05:43] 好了那文件上传过来之后我们这个流程应该交给谁处理呢很简单我们可以自己写一个Service通过Service把这个文件部署到我们的activity当中好了那我们配置一个serviceat all to whereprivate这个Service呢还没写我先把它定义出来p o c e s s s e r v i c e这个还没写OK那接下来这边呢我们去配置一个Service
[06:16] SERVSE放到这个包下new创建一个class好了那接下来在这边呢我们就可以通过抱歉上面那个来注解ata Service别抱错那接下来我们就可以通过Service打点同样是deploy把这玩意上传过去就可以了那我们都知道这个流程呢可能啊不同的公司它这个流程是不一致的
[06:48] 那这个文件呢可能也是不同的公司要上传不同的文件没错吧那这边呢我们可以给它传递一个company id传过去当然了我这company id我自己先给它定一个这个我先随便写比如说就叫传制播客其实这个应该代表是一个id名称啊我这边先随便写我们先来测试一下最后看一下效果OK那接下来呢这边思维当中补充一个新的方法那这个方法咱们就是用来进行流程部署的
[07:21] 流程部署那流程部署呢两个参数第一个就是我们上传的ppmn文件好了接着第二个改下名字company id好了company id代表的是企业idok那接下来咱们就开始完成这个上传或者我们流程部署的这块代码的编写
[07:55] 那这个流程部署的这个代码编写呢其实没有各位想象的那么难一共关注的注意啊一共关注的其实就三件事情首先呢第一件事情是这样的好了我获取一下上传的这个文件名称因为这个文件名称最终会保存到数据库里这是第一件事好那接着第二件事第二件事呢我们就开始借助或者通过
[08:24] Repository ServiceORYVICE进行这个流程部署很简单那接下来呢第三件事呢我们其实可以打印打印我们的部署结果OK这个都比较简单那我们说过了咱们刚刚工程当中是不是要进行流程部署那流程部署要借助这个Service那我们可以把这个Service at auto where注进来那这边呢再来解释一下
[08:57] Repository这个Service不是我们自己写的是Activity工作流它给我们暴露或者给我们提供好的这么一个工具方法直接通过里面的方法完成我们的EO部署其实就可以了好了注入进来private不要选错包Activity的OK注入进来之后我们一会就能完成操作了好了接下来咱们把步骤里面的涉及到这些代码给它补充完整第一个获取上传的文件名称
[09:29] Skyn来一个叫做fill name等于好了你上传的fill里面其实包含了你的名称.getoriginal fill name这样一来文件名称获取到了那获取到了之后我们就开始进行流程部署流程部署需要用到Reposit Service好了那接下来你要想进行流程部署首先第一件事.create一个
[10:01] Deployment好了那这样一来呢咱们就能够得到对应的这么一个对象这么一个Deployment Builder好了这个是我们的部署的一个构建者部署的一个构建器那通过这个构建器继续打点好了继续打点呢我们就可以End Bytes那这个代表的什么意思呢这个就是部署部署我们的流程那注意这个里面呢需要设计到的
[10:39] 有两个参数第一个参数就是我们的流程名就第一个参数就是我们的这个文件名称好那接着第二个参数代表的就是我们文件的诶注意文件的bytes数组诶所以我们只需要把这个fill name传递过来那接着这个bytes数组在我们的上传文件当中轻轻松松就能获取到点get bytes好了这边呢会有一个小小的
[11:12] 异常啊我们来处理一下OK没问题了那注意啊那这个只是上传了一个文件但是我们说你上传的文件是不同的企业是不是都不一样啊所以我们这边呢继续呢也可以添加一个对应的租户ID比如说传职博客可以有传职博客的流程那比如说IT黑马可以有IT黑马的流程那对于这个activity也支持这种多租户的方式那怎么做很简单builder点
[11:42] 这边呢Tentance ID指的是你要设置的诶 组户ID那我们的组户ID就是company ID传递过来其实就可以了当然了我们这个代码呢写的还是不太符合人家的这种开发的一个要求那其实呢这些代码呢我们注视掉它可以通过这种这种编程方式也能够实现就是一行打点create deployment点add
[12:16] by词这就有一点点像流逝编程就是一行往下写点好了我们的组户ID放进去这种方式也可以那最终得到那最终得到的其实也是这么一个deploy builder那注意啊现在而言还没有部署那没有部署那怎么办呢就可以通过这个builder点好了deploy进行真真正正的部署
[12:51] 那部署之后会有一个返回值就是deployment那我们可以一起最终打印一下这个部署结果deploymentOK好了那这样一来咱们这个流程上传流程部署的这个工作呢咱已经把它写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过控制器接收上传的 BPMN 文件，并调用 RepositoryService 创建流程定义。

2) 按时间顺序列出每张画面的要点：
画面1: 在 IntelliJ IDEA 中，右键点击 `AuditTest.java` 文件，弹出菜单，选择“Close Others”关闭其他标签页，当前只保留 `AuditTest.java` 和 `AuditTest.testActivity` 两个标签页。
画面2: 点击“Close Others”后，IDEA 主界面显示空的项目结构，提示“Search Everywhere Double Shift”等快捷操作。
画面3: 在项目结构中，选中 `com.ihrm.audit` 包，展开其下的 `src/main/java` 目录，显示 `Controller`、`dao`、`entity` 等子包。
画面4: 在 `ProcessController.java` 文件中，光标位于 `@RestController` 注解后，显示代码补全建议，包括 `@CrossOrigin`、`@RequestMapping` 等。
画面5: 在 `ProcessController.java` 文件中，光标位于 `@RequestMapping` 注解后，显示代码补全建议，包括 `@CrossOrigin`、`@RestController` 等。
画面6: 在 `ProcessController.java` 文件中，光标位于 `@RequestMapping` 注解后，显示代码补全建议，包括 `@CrossOrigin`、`@RestController` 等。
画面7: 在 `ProcessController.java` 文件中，光标位于 `@RequestMapping` 注解后，显示代码补全建议，包括 `@CrossOrigin`、`@RestController` 等。
画面8: 在 `ProcessController.java` 文件中，光标位于 `@RequestMapping` 注解后，显示代码补全建议，包括 `@CrossOrigin`、`@RestController` 等。
画面9: 在 `ProcessController.java` 文件中，光标位于 `@RequestMapping` 注解后，显示代码补全建议，包括 `@CrossOrigin`、`@RestController` 等。
画面10: 在 `ProcessService.java` 文件中，光标位于 `@Service` 注解后，显示代码补全建议，包括 `@Service`、`@Autowired` 等。
画面11: 在 `ProcessService.java` 文件中，光标位于 `@Autowired` 注解后，显示代码补全建议，包括 `@Autowired`、`@Service` 等。
画面12: 在 `ProcessService.java` 文件中，光标位于 `@Autowired` 注解后，显示代码补全建议，包括 `@Autowired`、`@Service` 等。
画面13: 在 `ProcessService.java` 文件中，光标位于 `@Autowired` 注解后，显示代码补全建议，包括 `@Autowired`、`@Service` 等。
画面14: 在 `ProcessService.java` 文件中，光标位于 `@Autowired` 注解后，显示代码补全建议，包括 `@Autowired`、`@Service` 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4:
```java
package com.ihrm.audit.Controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// 程序控制的Controller
@RestController
@RequestMapping(value = "/user/process")
public class ProcessController {

}
```

画面5:
```java
package com.ihrm.audit.Controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// 程序控制的Controller
@RestController
@RequestMapping(value = "/user/process")
public class ProcessController {

}
```

画面6:
```java
package com.ihrm.audit.Controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// 程序控制的Controller
@RestController
@RequestMapping(value = "/user/process")
public class ProcessController {

}
```

画面7:
```java
package com.ihrm.audit.Controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// 程序控制的Controller
@RestController
@RequestMapping(value = "/user/process")
public class ProcessController {

}
```

画面8:
```java
package com.ihrm.audit.Controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// 程序控制的Controller
@RestController
@RequestMapping(value = "/user/process")
public class ProcessController {

}
```

画面9:
```java
package com.ihrm.audit.Controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// 程序控制的Controller
@RestController
@RequestMapping(value = "/user/process")
public class ProcessController {

}
```

画面10:
```java
package com.ihrm.audit.Service;

import org.springframework.stereotype.Service;

@Service
public class ProcessService {

}
```

画面11:
```java
package com.ihrm.audit.Service;

import org.springframework.stereotype.Service;

@Service
public class ProcessService {

}
```

画面12:
```java
package com.ihrm.audit.Service;

import org.springframework.stereotype.Service;

@Service
public class ProcessService {

}
```

画面13:
```java
package com.ihrm.audit.Service;

import org.springframework.stereotype.Service;

@Service
public class ProcessService {

}
```

画面14:
```java
package com.ihrm.audit.Service;

import org.springframework.stereotype.Service;

@Service
public class ProcessService {

}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

