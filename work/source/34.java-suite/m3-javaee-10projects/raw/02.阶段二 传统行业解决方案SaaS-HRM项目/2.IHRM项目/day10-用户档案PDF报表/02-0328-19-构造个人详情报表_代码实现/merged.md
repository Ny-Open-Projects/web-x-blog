# 19-构造个人详情报表：代码实现

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\19-构造个人详情报表：代码实现_【海量资源尽在 ubkz.com】.mp4
- 时长 7分47秒（音频 468s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那基本的这个工程目录结构我们都已经写好了环境也搭建的差不多了但是各位别忘了由于我们现在使用的是Studio这种工具去创建的模板它对中文的支持呢可能还是有些问题的所以接下来我们要做的事情呢还有一步就是要对中文进行一个处理那中文处理其实步骤都是一模一样的咱们直接把之前写好的这几个配置也拿过来其实就可以了
[00:28] Strong以及这边Jasper Report它自己扩展的我们自己的配置文件Ctrl C全部放到Resource这个目录下OK已经搞定了接下来我们这回整个的搭建环境工程其实才已经结束这些我们都已经搞定了接下来我们关注的就是构造数据也就是我们数据来源最重要的部分对于这个部分来说我们要根据ID查询用户的详情和岗位信息
[00:57] 那这些内容其实在我们这个微服当中都已经准备好了就是借助user Service和user company job Service进行查询那我们构造的用户数据呢可以分成这么两个部分第一个部分呢就是用户详情的数据好了第二个部分呢就是我们用户岗位信息的数据以及我们第三部分数据就是用户的头像信息
[01:25] 没错吧各位好了这些都给各位准备的差不多了之后这些我们都分析好了之后接下来可以把这个数据先给他查询出来首先第一个借助user servicepersonal serviceuser companypersonal Service打点find by id这个id参数抱歉刚才没写他pass variable死菌类型的id拿过来OK把id传入进去好了personal我就叫personal了
[01:58] 好了接着再来一个岗位信息user company job Service打点也是find by id把id传过去这样一来呢得到岗位信息当然还有一个用户头像死菌类型的叫做那我们这个模板叫什么名字啊ok就是就是他吧control c拿过来打大括号去掉ok那对于这个头像信息我们应该如何去写呢
[02:34] 其实对于头像信息呢它可以接收一个UIL地址那么的UIL地址之前已经把所有的这些用户头像上传到青牛云里那我只需要拿到网络的这个地址给它传入进来其实就可以了那我们的青牛云相信各位还记着要想访问用户头像的时候我们有一个访问的规则那前面呢就是我们的域名域名那加上后面的我们的ID还有印象吧我们唯一标志是不是用户的ID啊
[03:04] 那我们的域名呢可以打开我们数据库来关注一下这个域名部分呢之前上传过很多次了就是这一段Ctrl C把它拷过来那后边加上IDID已经传递过来了那这样一来用户头像也构造好了那用户头像构造好了之后剩下的事情就是把这些数据封装到我们的Parameter Map集合里OK Parameter打点一个一个的put进去即可
[03:33] 那首先呢我们有用户头像好了那除了用户头像之外抱歉put那除了用户头像之外那这些又应该如何去做呢那注意这个是对象这是一个一个的对象那我们要做的事情是不是parametersputpersonal.getputjob.get等等啊那这个其实有点麻烦了那根据我之前的这个做法是这样的首先第一件事我这边用到的所有自定义的这些参数
[04:06] 可以找到这个parameters这里面所有我自定义的这些参数和实体类当中的属性名是一模一样的是一模一样的那我就可以这样去做我可以把每一个对象转化成map那转化成map之后把每一个map里面的key和value存到这个parameters里面那这样一来咱们做起来就比较简单了那我之前写过一个工具类叫做binmap utils打点它有一个方法
[04:36] 叫做bin2map直接接收一个对象通过对象的形式转化成一个map集合那第一个我构造了好了第二个打点bin2mapdrops那这样一来得到第二个map集合好了那接下来呢两个map都已经有了那接下来把map1和map2里所有数据放到parameters里面那这个也比较简单打点putallmap1parameters打点putall
[05:09] 这边map2那这样一来所有的内容就已经都准备好了好了各位那我们这个代码呢其实都已经写好了但是这边呢还有一个小小的问题是这样的就是说呢我这边现在写的是不是还是这个模板的这个内容啊这个还是模板相关的信息那这个还是写的有问题我们是不是应该把这个模板编译好的这个内容进行读取啊那我们需要这边打开studio对这个
[05:39] 进行一个模板编译好了编译好了之后Ctrl Ccall到Tamalysia好了掏过来之后呢我这边呢抄一下他的名称Ctrl C拿过来OK那好了重启一下员工微服务好了这边员工微服务再重启那接下来呢我们打开浏览器打开浏览器刷新一把注意注意在这个页面部分呢其实这个页面今天也给各位准备好了这边这个页面呢有一句话
[06:18] 大家加上其实就可以这句话在上面我加了一个按钮这么一个打印的按钮那这个打印按钮呢其实触发一个事件那触发这个事件呢就是让我当前页面进行一个跳转跳转到我们员工微服务刚才的这个链接上那这个ID是我们的用户ID就是构造我们请求的地址让页面进行跳转好了那我们跳转我们回到页面回到页面之后点击这个下载按钮走
[06:48] 各位发现现在呢其实已经进入到了当前的这个界面那该有的数据呢其实也都有了只是这个头像呢现在还没有显出来好了我们这边多刷新两次OK已经没有问题了这个图像也能正常显示出来了OK好了那到目前为止呢咱们今天的这些内容呢就跟各位都讲过了其实对于我们今天的主要目的就是和各位简单的来看一下
[07:19] 如何去通过Studio这个工具去创建模板当然了我们一起来看了一下数据填充分组报表chart报表还有我们父子报表这些形式当然了最后呢还有一个没有难度的这么一个用户档案那个下载那对于这个用户档案下载来说呢着重是让各位看一下或者回顾一下我们之前构造一个报表的那三个步骤首先呢制作模板接下来呢填充数据构造数据其实就可以了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过控制器调用服务层数据，填充 Jasper 报表模板并导出 PDF 文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 EmployeeController.java 中，展示 pdf 方法的代码，用于读取 jasper 文件并导出 PDF。
画面 2: 在项目结构中，展示 templates 目录下的 profile.jrxml 文件，以及 application.yml 配置文件。
画面 3: 展示一个 Word 文档，内容为“员工的个人信息：下载员工的pdf详情资料”，并列出“1.模板”、“2.数据来源”、“3.填充数据”、“4.导出到map集合参数”等步骤。
画面 4: 在 EmployeeController.java 中，展示 pdf 方法的代码，注释中提到“用户岗位信息模板”。
画面 5: 在 EmployeeController.java 中，展示 pdf 方法的代码，通过 @Autowired 注入 ArchiveService，并弹出 UserCompanyPersonalService 的方法列表。
画面 6: 在 EmployeeController.java 中，展示 pdf 方法的代码，弹出 UserCompanyJobsService 的方法列表。
画面 7: 在数据库管理工具中，展示一个 Blob 字段的插入对话框，URL 为 http://pkbivgrm.bkt.cloudn.com/1063705989962275601rt=1645785077443。
画面 8: 在 EmployeeController.java 中，展示 pdf 方法的代码，使用 Map.putAll() 方法将数据合并到 params 中。
画面 9: 在 EmployeeController.java 中，展示 pdf 方法的代码，将用户个人数据和岗位信息填充到 params 中。
画面 10: 在 EmployeeController.java 中，展示 pdf 方法的代码，使用 BeanMapUtils 将对象转换为 Map 并合并到 params 中。
画面 11: 在项目结构中，展示 templates 目录下的 profile.jrxml 文件，以及 application.yml 配置文件。
画面 12: 在 HRM 系统的个人详情页面，显示用户名为 “aj123” 的用户信息。
画面 13: 在 HRM 系统的个人详情页面，鼠标悬停在“更新”按钮上。
画面 14: 在浏览器中，显示生成的 PDF 文件内容，标题为“岗位信息”，包含“岗位：文员”、“职级：null”、“招聘渠道：番头”、“转正评价：null”等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 打印员工pdf报表
 */
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 2:
```yaml
# application.yml
```

画面 4:
```java
/**
 * 打印员工pdf报表
 */
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //6.用户岗位信息模板
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 5:
```java
@Autowired
private ArchiveService archiveService;

// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //6.用户岗位信息模板
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 6:
```java
// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //6.用户岗位信息模板
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 7:
```sql
-- 插入 Blob 字段的 URL
http://pkbivgrm.bkt.cloudn.com/1063705989962275601rt=1645785077443
```

画面 8:
```java
// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    //6.用户岗位信息模板
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    ServletOutputStream os = response.getOutputStream();
    try {
        JasperPrint print = JasperFillManager.fillReport(fis, params, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面 9:
```java
// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf(@PathVariable String id) throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    UserCompanyPersonal personal = userCompanyPersonalService.findById(id);
    UserCompanyJobs jobs = userCompanyJobsService.findById(id);
    //3.用户头像
    String staffPhoto = "http://pkbivgrm.bkt.cloudn.com/" + id;
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    params.put(key, "staffPhoto", staffPhoto);
}
```

画面 10:
```java
// 打印员工pdf报表
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf(@PathVariable String id) throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/profile.jrxml");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.构造数据
    UserCompanyPersonal personal = userCompanyPersonalService.findById(id);
    UserCompanyJobs jobs = userCompanyJobsService.findById(id);
    //3.用户头像
    String staffPhoto = "http://pkbivgrm.bkt.cloudn.com/" + id;
    //3.填充pdf模板数据，并输出pdf
    Map params = new HashMap();
    params.put(key, "staffPhoto", staffPhoto);
    Map<String, Object> map1 = BeanMapUtils.beanToMap(personal);
    Map<String, Object> map2 = BeanMapUtils.beanToMap(jobs);
    params.putAll(map1);
    params.putAll(map2);
}
```

画面 11:
```yaml
# application.yml
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 文档内容为“员工的个人信息：下载员工的pdf详情资料”，并列出“1.模板”、“2.数据来源”

