# 12-工程搭建：搭建子工程之搭建环境构造返回实体类

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\12-工程搭建：搭建子工程之搭建环境构造返回实体类_【海量资源尽在 ubkz.com】.mp4
- 时长 9分56秒（音频 596s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 复工程我们已经搭建好了那么接下来呢我们去搭建第一个子模块就是一些工具类的一些公共的模块好了这个模块当中呢我们首先第一件事呢就是构建先把它构建出来那构建出来接下来因为我们进行交互的时候可能会有一些交互过程的一些实体类比如说呢返回码比如说交互过程的对象那这些内容呢就要创建出来那创建出来那接下来
[00:32] 我们在一个微服务的这么一个架构体系下可能会用到一些微服务架构下的一些ID生成器所以这个ID生成器也需要把它引入到我当前的这个公共子模块里面所以对于我这个子模块来说首先第一件事构建那构建好了之后把相应的这些涉及到交互的这些实体类创建出来哎涉及到了比如说返回值实体类给它创建出来那还有我们搞一个
[01:02] 分布是ID生成器那么好我们一个一个的来看首先先把这个公共子模块创建出来它叫做IHM common好了在这边呢打开我的idea在parent也就是复工程上边右键new创建一个模块同样是mayman工程点击nextgrab ID不用改了artifact ID我们叫做IHRM下滑信按commoncommon
[01:32] Next点击Finish那子模块现在呢已经创建出来了那接下来接下来我们要做的第二件事打开讲义我们来看一下有公共的实体类还有公共的返回值定义返回码的这些定义那对于这些内容都比较简单都比较简单咱们就不废话了在这边打开Java右键创建一个包右键创建一个包
[02:04] com.ihim.com.intity那包创建好了之后里面的这个抱歉这个intity写错了好了这个包创建好了之后接下来如果各位有兴趣的话一个升起来一个升起来的你去往里填那这些代码由于比较简单我已经在今天的代码资料当中通用代码common给各位准备好了
[02:35] 那把这三个实体类Ctrl C直接call到entity包下即可那call过来之后呢简单的对这些代码做一个说明其中resource code这个resource code代表的是我们公共的返回码那各位来看这个公共的返回码其实是一个枚举其实是一个枚举里面定义了三条信息其中四个size代表你当前操作是否成功code
[03:08] 代表返回码message代表消息那这玩意儿其实不陌生咱们刚才介绍API的时候做过一个说明因为我们这边操作响应的时候有code有flag有message嘛所以一个枚局里面定义了很多的内容有三部分处代表是否成功code返回码操作成功的标志它的一些说明好了那我们想跟各位来声明的是
[03:36] 声明的是其中有一个叫做返回码code那返回码code我们做一个统一的定义比如说成功我就叫一万那接下来如果是一个统一的失败我叫一万零一那剩下呢更加详细的说明比如说未登录那未登录的话我叫一万零二比如说没有权限未授权授权
[04:13] 那未授权的话我叫做1003如果说抛出异常当然了我们会对这个异常做处理那抛出异常的话我叫59那除了这些返回码之外还有一些返回码比如说呢有用户操作的用户操作可能操作失败了比如说有企业操作的可能操作失败了权限其他操作极其可能都有操作失败的可能那针对这些操作失败的可能底下都有预留要写的内容
[04:42] 比如说用户操作的返回码我们叫做二某某某某企业操作的我们叫做三某某某某好了以此类推OK那这个返回码做了一个简单的说明那接下来就是对于我们请求之后要有响应那请求之后要有响应我封装了一个数据响应对象那这个数据响应对象里面success datasuccess code message
[05:16] 那这三个这三个是我们数据响应里面的code flag message那除了这个玩意之外比如说我们要查询企业列表那查询企业列表的时候这边底下是我们的响应code flag message没问题那还有就是我们的数据部分那数据部分给它封装到一个data属性里所以各位来看真正的数据响应对象
[05:45] 我们其中包含的第一个叫做Success第二个叫做Code第三个叫做MessageOK当然了还有第四个第四个呢叫做Data那Success代表是否成功Code代表返回码好了Message代表我们的消息说明返回消息返回信息好了还有一个叫做返回数据那经过我们这样一处理
[06:28] 那经过这样一处理那我们返回的数据是什么格式呢其实就是一个大括号返回的是一个json数据嘛大括号那这个返回的data部分它其实又是一个json数据OK我写到上面吧OK那这样一来我们就能构造这么一个结构那其实有的朋友就有点不明白了你写了一个result干嘛还写一个result code呀
[07:02] 是因为我们如果自己去写这个result有点麻烦你要传递一个数据一条信息两条信息三条信息四条信息那太麻烦了我要写好多次get set的方法那我就可以直接传递过来一个每举对象那拿到每举对象的每一个值复制到这个result里面那这样一来我一会写代码可能就更加方便一点如果说你不构造result code其实也可以你自己一个一个的new一个result一个一个的set进来其实就可以了
[07:32] 那好了那reset result这个返回响应对象那我们已经响应抱歉这个单词这个字写错了返回响应对象这个响应对象已经跟各位做过一个交代那还有一个叫做配置对照那这个配置对照它又是什么含义呢注意注意那我们可能在进行数据响应的时候可能带有分页的一个处理
[08:00] 那对于分译的处理我要构造的数据格式其实跟刚才大致是一模一样的首先它有SUCCESS比如说这边代表成功那除了SUCCESS之外还有CODECODE我们说过了1万代表成功那还有MESSAGE那MESSAGE比如说就是查询成功了比如说我这边就叫OK了那别忘了我想的数据还有一个叫做DATA
[08:34] 那这个data里面如何能够描述出分页数据呢那所以注意如果涉及到分页的话我们要构造一个page result把这个page result放到data部分即可所以这一回放了我们的page result之后那我们这一回响应的数据格式它就变了变成了第一个有total好了第二个叫做肉丝
[09:06] 那这个total代表的是我们的总条数还有一个肉丝代表的就是记住数据列表OK那这样一来就跟各位都说清楚了我们返回的数据全部封装到result里面如果是一个对象直接data比如说是一个企业对象直接把企业放到data部分他就能给我进行解析如果是一道分页
[09:39] 我们用的是配置result那配置result total代表总条数肉丝里面所有都是我们的数据列表把这个result再配置到我们的data部分那这样一来让它帮我们自动构造数据其实就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
构建一个用于 SAAS-HRM 系统的公共子模块（ihrm-common），并定义统一的返回结果实体类（Result）和分页结果类（PageResult）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程目录结构，当前位于“4.4.1 构建公共子模块ihrm-common”章节，IDEA 中选中了“ihrm_common”模块，右侧显示其在项目结构中的位置，并标注“公共子模块”。
画面 2：与画面 1 几乎相同，强调“4.4.1 构建公共子模块ihrm-common”和“ihrm_common”模块。
画面 3：在 IDEA 中右键点击“ihrm_common”模块，弹出菜单，显示“Build Module 'ihrm_common'”等选项，右侧显示模块的 pom.xml 内容。
画面 4：在 Windows 资源管理器中，显示项目路径“ihrm\day1”，选中了“pom.txt”文件。
画面 5：在 IDEA 中打开“ResultCode.java”文件，显示 ResultCode 枚举类的定义，包含 SUCCESS、FAIL、UNAUTHENTICATED、UNAUTHORIZED、SERVER_ERROR 等常量。
画面 6：在 Swagger UI 界面中，展示“Company”模块的 API 文档，包含 POST、GET、PUT、DELETE 等操作。
画面 7：在 IDEA 中，ResultCode.java 文件中，注释部分显示“公共的返回码”和“返回码：code”。
画面 8：在 IDEA 中，ResultCode.java 文件中，注释部分显示“返回码：code”和“失败码：10001”。
画面 9：在 Swagger UI 界面中，展示“GET /company”接口的响应示例，返回 JSON 格式的数据。
画面 10：在 IDEA 中，打开“Result.java”文件，显示 Result 类的定义，包含 @Data、@NoArgsConstructor、@AllArgsConstructor 注解。
画面 11：在 IDEA 中，Result.java 文件中，注释部分显示“数据相应对象”和“success、code、message、data”。
画面 12：在 IDEA 中，Result.java 文件中，注释部分显示“数据相应对象”和“success、code、message、data”。
画面 13：在 IDEA 中，打开“PageResult.java”文件，显示 PageResult 类的定义，包含 total 和 rows 字段。
画面 14：在 IDEA 中，Result.java 文件中，显示 Result 类的静态方法 SUCCESS()。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 的 pom.xml 内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>ihrm_parent</artifactId>
        <groupId>com.ihrm</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>ihrm_common</artifactId>
</project>
```

画面 5 的 ResultCode.java 内容：
```java
package com.ihrm.common.entity;

public enum ResultCode {
    SUCCESS(true,10000,"操作成功！"),
    FAIL(false,10001,"操作失败！"),
    UNAUTHENTICATED(false,10002,"您还未登录！"),
    UNAUTHORIZED(false,10003,"权限不足！"),
    SERVER_ERROR(false,99999,"抱歉，系统繁忙，请稍后重试！");
    //---用户操作返回码---
    //---企业操作返回码---
    //---权限操作返回码---
    //---其他操作返回码---

    //操作是否成功
    boolean success;
    //操作代码
    int code;
    //提示信息
    String message;

    ResultCode(boolean success,int code, String message){
        this.success = success;
        this.code = code;
        this.message = message;
    }
}
```

画面 10 的 Result.java 内容：
```java
package com.ihrm.common.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

public class Result {
    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public class Result {
        private boolean success;//是否成功
        private Integer code;//返回码
        private String message;//返回信息
        private Object data;//返回数据

        public Result(ResultCode code) {
            this.success = code.success;
            this.code = code.code;
            this.message = code.message;
        }

        public Result(ResultCode code, Object data) {
            this.success = code.success;
            this.code = code.code;
            this.message = code.message;
            this.data = data;
        }

        public Result(Integer code, String message, boolean success) {
            this.code = code;
            this.message = message;
            this.success = success;
        }
    }
}
```

画面 13 的 PageResult.java 内容：
```java
package com.ihrm.common.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

public class PageResult<T> {
    private Long total;
    private List<T> rows;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

