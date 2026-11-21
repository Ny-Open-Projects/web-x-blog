# 15-POI文件导入：需求说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\15-POI文件导入：需求说明_【海量资源尽在 ubkz.com】.mp4
- 时长 7分58秒（音频 479s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们完成了PUI的基本入门操作之后呢其实对于使用PUI操作一个cell它的一个大致情况各位都已经掌握了那接下来呢就是将PUI应用到我们这个系统当中去完成这些功能那首先嘛完成一个功能呢就是一个PUI报表的一个导入那收到这个导入呢我们先对这个我们的需求做一个简单的分析的一个过程是这样的在我们这个系统这边各位会发现
[00:32] 对于员工管理而言呢其中有一个点呢可能会比较麻烦在哪呢就是说对于我们的人事的一些人员需要把用需要把我们的员工信息录入到我们这个系统当中那这边呢我们之前写过一个新增员工的这么一个操作把这些内容全部都录入进去那录入进去之后呢再去点击保存那如果说一个公司里面可能有上百人他要录入起来就太麻烦了那我们可以怎么做呢咱们可以给他来一个批量导入的一个功能
[01:02] 好了这边有一个导入的一个按钮那这个导入按钮呢你可以去下载我们给他提供好的这么一个模板注意这个模板呢给他提供好也就是说你如果想要使用这个功能就必须按照模板里面的这些内容去填写OK好了那下载好了模板之后按照模板内容添加好然后你点击上传Excel那上传好一个Excel之后呢在我们的服务端解析Excel文件并且把数据给我批量的注册到数据库当中
[01:33] 这个呢就是我们的一个需求那这边说到了有一个模板文件那这个模板文件呢在今天的课程资料当中也给各位准备好了好了这边有一个导入数据的一个模板各位可以简单的来看一下当然了我这个写的是比较简单的其实还数据还是比较多的可能还有很多的其他的字段但是都是大同小异我们就以这几个举例来说明问题其实就可以了
[01:58] 好了我们这个模板是这样的首先呢有用户名手机号公号聘用形式入职时间还有部门编码那对于这个部门编码呢我简单的做一个说明注意我们之前呢这边写自己代码的时候添加一个员工这边呢我们是不是可以给他添加这个部门的一个选择你可以选择是哪个部门的是研发部啊还是我们的开发部等等那这边呢对于每一个部门来说各位找到部门
[02:28] 对于某一个部门来说呢咱们之前呢玩过它都有一个这个部门编码这个部门编码不是部门ID也不是部门的名称那这个部门编码是一个比较简单易记的这么一个字符划所以呢对于我们而言要做的事情前几个比较简单就是把它保存到我们的用户表里面就可以了那最后这个是不是要根据部门编码去查询完整的部门信息接着给它转化成部门的ID和部门的名称
[02:58] 再保存到收益库里所以这个就是我们简单的做了一下我们这个批量导入员工的这个功能的一个分析以及我们要做的事情OK那我们接下来呢就把这个员工导入的这个需求给他实现出来那对于我们要在系统当中
[03:21] 要去实现这个员工导入的这个功能首先呢第一件事是就应该把我们py相应的这个依赖添加到我们的工程当中这是第一件事那接着第二件事呢就是说啊对我们导入来说这个员工这个导入的这个功能应该写到哪个模块下那我们这边的代码呢这个模块呢有很多各位有我们的系统微服务啊用用系统微服务有我们的员工微服务还有我们的企业微服务那我们这边要用到用户注册
[03:50] 这个一个功能也就是把用户注册到我们的这个BS user表这个当中那对于我们来说呢是不是应该把它写到系统微服务当中更加合适因为是用户的我们写到user Controller当中是不是就可以了好了这个我们基本上都做好了之后呢接下来咱们就开始第一件事把箱的坐标给他拿过来那这个坐标呢我们刚才写过很多的简单的这个demo案例从里面直接把py箱的坐标control c给他copy到我们这边
[04:20] 好了我就靠到复工程模块下了哎靠到下边写点点注释PWA的好了那坐标引入进来之后接下来呢就是说我在user Controller这边咱们就可以填写一个我们导入Excel添加用户的这么一个功能OK那对于这个功能呢咱们可以简单的打开页面来试一下
[04:51] 打开F12这边看一下我们的请求地址请求路径究竟是什么OK点击一个随便来一个我就随便来一上传了好了各位来看import好了各位来看API这个是我们不管它的我们关注的是sys user import是不是就是后面这一部分的这么一个请求地址所以对于我们而言这边找到我们的这个工程副路径sys好了那接下来我们这边可以填写我们的一个Controller at request
[05:22] 叫做 mappingrequest mapping那我这个 request mapping里面写的内容呢就相对来说比较简单value等于我们直接从这边call过来即可user importok 那我们的请求方式呢显而易见method postok 好了那我们这个方法呢随便给它来一个就可以了注意注意好了result返回值那对于我们这边的方法名称呢随便给它来一个吧import就叫 import
[05:56] OK好了这边呢为了不抱错啊咱们直接呢就把它返回来new一个result好了里面resultcode.succeed那接着呢我想跟各位来声明的有一个问题是这样的就是说呢我们批量的上传到一个excel过来那这边呢就涉及到一个文件上传的这么一个细节问题就是文件上传那对于文件上传呢在我们的Spring Boot程序当中
[06:33] 如何表述这是上传的一个文件呢各位那如何描述这边是一个文件其实比较简单其实也不难那我们应该如何去体现它需要和各位做一个简单的说明那我们这边请求过来各位看请求request那request的这一大堆这一大堆其实说明了我这边呢multipartmultipartformdate这代表的是我有一个文件上传过来
[07:02] 那并且呢我这边底下有我请求的内容这个文件的名称叫做failname等于fail不是failname啊是这个name等于fail指的是我当前的这个文件的名称那接着呢就是说了对于我这边咱们就可以使用Spring Boot里面借助Spring给我们提供的一个叫做martpartfail这么一个对象来代替好了这边呢我就随便来了代表的是一个fail对象
[07:34] 好了这边我们可以使用ata request permokata request perm那我们传递的这个属性呢其实就是它的名称呢就是fail我们刚才看过名称fail那这样一来它会把上传过来的这个文件直接给我拼装到这个fail对象当中ok

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过前端上传 Excel 文件，后端使用 Apache POI 解析数据并批量导入员工信息。

2) 按时间顺序列出每张画面的要点：
画面1：展示 HRM 系统员工列表页面，包含员工姓名、手机号、工号、聘用形式、部门等字段，右侧有“导入”、“设置”等操作按钮。
画面2：在 HRM 系统“员工导入”页面，弹出“打开”文件对话框，准备选择 Excel 文件。
画面3：展示 Excel 文件内容，包含“用户名”、“手机号”、“工号”、“聘用形式”、“入职时间”、“部门编码”等列，数据示例为 test001、13800000001、2001、1、2018/1/1、DEPT-DEV。
画面4：与画面3相同，Excel 文件内容未变化。
画面5：展示课程 PPT 页面，标题为“4.1 需求分析”，内容为“实现批量导入员工功能，页面端上传excel表格，服务端解析表格获取数据，批量新增用户”，并列出子章节“4.2 员工导入”及“4.2.1 搭建环境”。
画面6：在 IntelliJ IDEA 中打开 `pom.xml` 文件，展示 Maven 依赖配置，其中包含 `org.apache.poi` 的依赖。
画面7：在 IntelliJ IDEA 中打开 `UserController.java` 文件，展示 `assignRoles` 方法，用于分配角色。
画面8：在浏览器中打开 HRM 系统的“员工导入”页面，显示“点击上传”按钮和“将文件拖到此处”区域。
画面9：在 IntelliJ IDEA 中打开 `UserController.java` 文件，展示 `testFeign` 方法，用于测试 Feign 服务。
画面10：在 IntelliJ IDEA 中打开 `UserController.java` 文件，展示 `testFeign` 方法，用于测试 Feign 服务。
画面11：在 IntelliJ IDEA 中打开 `UserController.java` 文件，展示 `importUser` 方法，用于导入用户。
画面12：在浏览器中打开 HRM 系统的“员工导入”页面，使用开发者工具查看网络请求，显示上传文件的请求头和请求体。
画面13：在 IntelliJ IDEA 中打开 `UserController.java` 文件，展示 `importUser` 方法，用于导入用户。
画面14：在 IntelliJ IDEA 中打开 `UserController.java` 文件，展示 `importUser` 方法，用于导入用户。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面6 `pom.xml` 依赖配置：
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>4.0.1</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml-schemas</artifactId>
    <version>4.0.1</version>
</dependency>
```

画面5 PPT 文本：
“4.1 需求分析
实现批量导入员工功能，页面端上传excel表格，服务端解析表格获取数据，批量新增用户
4.2 员工导入
4.2.1 搭建环境
父模块pom文件添加依赖
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>”

画面13 `UserController.java` 方法：
```java
@RequestMapping(value = "/user/import", method = RequestMethod.POST)
public Result importUser(@RequestParam(name = "file") MultipartFile file) {
    return new Result(ResultCode.SUCCESS);
}
```

画面14 `UserController.java` 方法：
```java
@RequestMapping(value = "/user/import", method = RequestMethod.POST)
public Result importUser(@RequestParam(name = "file") MultipartFile file) {
    return new Result(ResultCode.SUCCESS);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面5 PPT 标题：
“4.1 需求分析”
“4.2 员工导入”
“4.2.1 搭建环境”

画面5 PPT 表格数据：
“父模块pom文件添加依赖”
“<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.0.1</version>
</dependency>”

5) 无。

