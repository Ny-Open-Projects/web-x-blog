# 22-统一异常处理

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\22-统一异常处理_【海量资源尽在 ubkz.com】.mp4
- 时长 14分12秒（音频 853s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 我们已经完成了基本企业微服务的一个增删改查的一个操作但是呢还有一个环节我们也需要考虑到我们的工程可能出现不同程度的问题也就是异常为了让我们的代码或者让我们的工程更加友好我们有必要对可能出现的问题做一个处理那这边我们就需要借助Sprint提供的Controller Advice进行异常的一个处理了
[00:30] 那接下来这个公共异常处理应该怎么做呢其实也比较简单把这个异常借助Sprint的ControllerAdvice和ExceptionHandle两个注解配置到类上配置到方法上自动的就会把所有的异常给你解决掉那接下来我们来看一下如何进行处理好了在这边呢我找到我们的idea
[00:58] 那这个异常处理呢其实是应该是很多的工程当中都要有那针对这些我们就把公共的内容放到common这个包下了那在这个common包下我去创建一个我们异常处理的这么一个类好了又见创建一个class当然了我把它放到一个包下吧handhandle
[01:20] 好了这个叫什么名字呢我们看一下讲义我就跟讲义上它的名字保持一致了比如说就叫做base exception handlerbase exception handlerOK好了呢对于这个是我们自定义的公共异常处理类处理器吧那怎么去做这个异常处理器那这边我们需要做这么两件事
[01:50] 那这两件事首先第一件事我们要声明它它是一个异常处理器你只有声明了死不仁才知道死不仁才能用它对我们的异常进行处理那接下来那如果抛出异常的时候我们应该对这个异常做什么样的处理这是我们要完成的第二件事所以我们的两件事都比较明确第一个声明异常处理器好了第二个是对异常进行统一的处理
[02:21] 那一个一来看声明异常处理器我们借助的是一个注解这个注解叫做ata controlleradvice那对异常统一处理那应该怎么去处理呢我们需要去写一个方法那这个方法呢随便可以定义一个public will id当然了这个是一个返回值那对于我们来说出现的返回值都用result来做来代表返回值
[02:51] 那这个方法叫什么名字其实无所谓我叫做arrow那这个arrow当中我们可以接收很多的参数比如说可以接收http servlet request比如说可以接收http servlet response比如说还可以接收你当前的异常究竟是啥OK那我为了不报错我个人习惯先写一纳好了这个就是我们干的第二件事就是对异常统一处理
[03:22] 那对异常统一处理你怎么知道出现了异常就能执行这个error方法呢你怎么知道执行error方法要返回是一个resource呢而不是其他的内容那怎么做我们需要指定指定这个是我们出现异常的一个处理器指定它是一个出现异常的处理机制我们这边用的是一个注解这个注解叫做exception handler那exception handler当中我们可以配置
[03:52] 你对哪样的异常进行处理比如说value等于exception.class我处理的是全局的exception异常当然如果说你有其他的异常你就写其他异常我直接处理最大的好了接下来我们的返回是result但是我们需要将result是不是封装成我们的自封装成我们的json对象响应给前端这样就更加友好了
[04:23] 所以在这边我们需要把返回值进行处理,at response body,它自动的把你处理拦截到的异常的内容封装成对象,或者封装成我们的JSON字幕串并进行响应。
[04:36] 好了,这些我们都做过了之后,接着就是里面的一些代码的一个处理,对里面代码处理其实比较简单,比较简单,那如果出现了异常,它就会执行error方法,那在error方法当中,我们不会是简单粗暴的抛出,
[04:53] 我们要干什么直接封装 result 对象即可等于 new 一个 result那么 new result 的时候呢可以传递 result 我们的返回编码 code这回不叫 success点比如说server arrow 代表是服务器出错了那底下直接 return即可那这样一来那这样一来我当前的这个 controlleradvice就已经配置好了
[05:26] 一旦出现异常一旦出现异常它就会进入到error方法进行处理那error方法简单粗暴的就返回一个error的这么一个说明里面false9999抱歉系统出错了OK并且以JSON字符创的形式响应给我们的请求好了这个代码呢我们已经写好了那写好了之后需要各位注意那注意的点在哪呢就是说呢我现在已经放到了
[05:55] common这个保险common这个保险叫handler那我现在要想去在company当中使用的话我先去打开启动类在启动类里面我们要扫描那扫描的注解注意它现在扫描的是company它扫描不到common所以我这边要做一个简单的修改就是说你去给我扫描com.ihm那这样一来我这个处理器不也就能扫描到了吗
[06:24] OK好了这个我们搞好了之后接下来呢我们就可以构造一个异常随便搞一个异常出来比如说呢我在里面Find就Find All吧我里面出现一问题int i等于1除以0哎出错了那出错了之后我把我这个服务重新启动一下这个启动过程相对来说有一点点慢啊各位耐心等待Find All那好了接着我打开Postman
[06:59] company我们的请求地址get方式代表查询全部代表查询全部现在里面出现了一个错误那一旦出错了它会进入到我们定义好的公共的异常处理器里面进入到异常处理器里面进入执行它的error方法把你的异常转化为一个resolve对象接着以json组串给我返回过来那这个错误里面是什么系统方法等等
[07:28] 我们接着一起来执行一下看下效果走这回效果就有了你后台虽然抛出了一个错误但是并不影响我前端使用而且是一个比较友好的这么一种处理方式OK那有的朋友会说你系统的这个异常能够处理那如果说我自己定义的异常能不能够统一处理呢当然也可以
[07:59] 那接下来我们来看一下如何自己定义一个异常并且处理那我们这边呢要做的事情呢其实一共就两件事第一件事呢我们可以自己定义一个异常累出来那接下来在我们刚才的公共异常处理器里面把我们自己定的这个异常给它捕获到并做专门的处理即可所以接下来呢我们就围绕着这两个方向来做首先第一个添加一个自定义的异常
[08:28] 好了在这边呢自定义常我就写到common包下来一class把它放到exce exce ptln exception这个包下比如说呢我就叫做跟他这边一样了common exceptionok好了这个自定义常的时候呢这个叫做自定义常那自定义常我们需要继承flag exception
[09:02] 那继承复类之后里面可以自己定义你自己需要的一些参数或者一些数据那我这边呢为了保持和我的代码的统一我这里面定义一个属性就是result code比如就叫做r result code了OK那接下来result code好了接下来呢我可以提供一个构造方法如果你想要用我这个一长的话你需要提供一个构造方法传递一个result code进来
[09:49] 那这个result code当中呢其中有很多的属性有它的是否成功失败它的标志它的字它的这个编码还有它的说明OK好了那接下来接下来由于我其他地方可能要用get这个result code所以我在上面来一个get方法OK那这样一来我这个基本的setter方法其实咱们就已经都写好了已经都写好了那写好了之后注意写好了之后
[10:23] 自定义义常搞定了第一步我们第二步就关注的是我们的义义常处理器那在义义常处理器当中由于我拦截的其实是负类其实是负类那接着我可以在里面做一个分门别类的处理ifexceptione.getClass如果你得到的这个类的类名呢它跟我们自定义的义义常getClass一模一样如果一模一样
[10:58] 那这个是不是就是我们自己定义的异常如果不是的话是不是去返回我们自己构造的叫做ServiceError就是6个9OK那接着我们关注一下中间如何处理那其实中间的处理也比较简单ResultR-E-S-U-L-T等于New一个R-E-S-U-L-TResult那注意了接着Return
[11:29] 那接着我想说你当前得到的这个异常我们可以对它进行一个转化类型转化转型嘛相向啊转型OK那把我们这个异常的转化成CE等于就是来一个类型强力转化那好了我这个common exception当中是不是恰巧有这个result扣开啊所以我这边可以借助CE
[12:03] 打点get result code直接构造result并且返回不就可以了OK好了那这样一来呢我这个异常处理器咱们就已经写好了并且是使用自定义异常的形式来做的那同时我再去构造一个错误比如说呢就是find by idfind by id呢我直接在这边来一个throwthnew一个我们叫做common
[12:43] common exception当然这个common exception throw啊抱歉 throwcommon exception需要一个参数那这个参数就是我们的result coderesult code打点比如说我这result code有很多比如说我告诉你权限不足比如我告诉你权限不足OK好了这边呢会对异常做一个简单的处理OK底下这些我就都先不要了都先不要了
[13:20] 那我一定要用Find by ID它就会帮我抛出异常抛出的是我写的是一个权限不足当然你可以自己定义自己的枚举自己定义自己的枚举按照格式来自己定义就可以了好了这些我们都写好了之后来重新启动一下我们这个服务注意来看我们的Controller代码如果查询全部是一个通用的异常那如果说是根据ID查那是不是抛出我们自己的权限不足那好了我们再来测试一下
[13:51] get全部走系统异常好了同样是get根据ID查询1走全线不足那这样一来我们就已经做到了统一的全线处理并且可以对自定义的异常也做不同的处理OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过自定义异常类和全局异常处理器来统一处理控制器层的异常，并展示其在实际接口调用中的响应效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了课程目录结构，当前位于“4.1 创建项目的说明”。
- 代码编辑器中显示了自定义异常类 `CommonException` 的定义，继承自 `RuntimeException`，包含 `ResultCode` 字段和构造方法。
- 代码内容：
  ```java
  package com.ihrm.common.entity;
  import com.ihrm.common.entity.ResultCode;
  import lombok.Getter;
  @Getter
  public class CommonException extends RuntimeException {
      private static final long serialVersionUID = 1L;
      private ResultCode code = ResultCode.SERVER_ERROR;
      public CommonException() {
      }
      public CommonException(ResultCode resultCode) {
          super(resultcode.message());
          this.code = resultCode;
      }
  }
  ```

画面 2:
- 展示了项目结构，当前选中 `BaseExceptionHandler.java`。
- 代码编辑器中显示了 `BaseExceptionHandler` 类的注解和导入语句，准备定义公共异常处理器。
- 代码内容：
  ```java
  package com.ihrm.common.handler;
  import org.springframework.web.bind.annotation.*;
  ```

画面 3:
- 展示了 `BaseExceptionHandler` 类的 `@ControllerAdvice` 注解和 `@ExceptionHandler` 注解。
- 代码内容：
  ```java
  @ControllerAdvice
  public class BaseExceptionHandler {
      public Result error(HttpServletRequest request, HttpServletResponse response, Exception e) {
          return null;
      }
  }
  ```

画面 4:
- 展示了 `BaseExceptionHandler` 类中 `error` 方法的实现，使用了 `@ExceptionHandler` 注解。
- 代码内容：
  ```java
  @ExceptionHandler(value = Exception.class)
  public Result error(HttpServletRequest request, HttpServletResponse response, Exception e) {
      return null;
  }
  ```

画面 5:
- 展示了 `BaseExceptionHandler` 类中 `error` 方法的实现，返回一个 `Result` 对象。
- 代码内容：
  ```java
  @ExceptionHandler(value = Exception.class)
  @ResponseBody
  public Result error(HttpServletRequest request, HttpServletResponse response, Exception e) {
      Result result = new Result(ResultCode.SERVER_ERROR);
      return result;
  }
  ```

画面 6:
- 展示了 `CompanyController` 类中的 `findAll` 方法，用于查询所有公司信息。
- 代码内容：
  ```java
  List<Company> list = companyService.findAll();
  Result result = new Result(ResultCode.SUCCESS);
  result.setData(list);
  return result;
  ```

画面 7:
- 展示了 `ResultCode` 类中的常量定义，包含系统错误码和业务错误码。
- 代码内容：
  ```java
  SUCCESS(true,10000,"操作成功"),
  FAIL(false,10001,"操作失败"),
  UNAUTHORIZED(false,10002,"您还未登录"),
  SERVER_ERROR(false,99999,"抱歉,系统繁忙,请稍后重试");
  ```

画面 8:
- 展示了在 `ResultCode` 类中定义 `SUCCESS` 常量的代码。
- 代码内容：
  ```java
  public static final ResultCode SUCCESS = new ResultCode(true, 10000, "操作成功");
  ```

画面 9:
- 展示了 `ResultCode` 类中的 `SUCCESS` 常量定义。
- 代码内容：
  ```java
  public static final ResultCode SUCCESS = new ResultCode(true, 10000, "操作成功");
  ```

画面 10:
- 展示了 `BaseExceptionHandler` 类中 `error` 方法的实现，判断异常类型并返回相应结果。
- 代码内容：
  ```java
  @ExceptionHandler(value = Exception.class)
  @ResponseBody
  public Result error(HttpServletRequest request, HttpServletResponse response, Exception e) {
      if (e.getClass() == CommonException.class) {
          return new Result(ResultCode.SUCCESS);
      }
      return new Result(ResultCode.SERVER_ERROR);
  }
  ```

画面 11:
- 展示了 `CompanyController` 类中的 `findById` 方法，用于根据 ID 查询公司信息。
- 代码内容：
  ```java
  @RequestMapping(value = "/{id}", method = RequestMethod.GET)
  public Result findById(@PathVariable("id") String id) {
      return new Result(companyService.findById(id));
  }
  ```

画面 12:
- 展示了 `CompanyController` 类中的 `findALL` 方法，用于查询所有公司信息。
- 代码内容：
  ```java
  @RequestMapping(value = "", method = RequestMethod.GET)
  public Result findAll() {
      int i = 1/0;
      List<Company> list = companyService.findAll();
      Result result = new Result(ResultCode.SUCCESS);
      result.setData(list);
      return result;
  }
  ```

画面 13:
- 展示了 `ResultCode` 类中的常量定义，包含系统错误码和业务错误码。
- 代码内容：
  ```java
  public enum ResultCode {
      SUCCESS(true,10000,"操作成功"),
      FAIL(false,10001,"操作失败"),
      UNAUTHORIZED(false,10002,"您还未登录"),
      SERVER_ERROR(false,99999,"抱歉,系统繁忙,请稍后重试");
  }
  ```

画面 14:
- 展示了 Postman 中发送 GET 请求到 `http://localhost:9001/company` 的响应结果。
- 响应内容：
  ```json
  {"success":false,"code":99999,"message":"抱歉,系统繁忙,请稍后重试","data":null}
  ```

