# day08-22-查询标的信息-前后端集成测试

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-9 实现查询标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-9 实现查询标的信息\day08-22-查询标的信息-前后端集成测试_【海量资源尽在 666java.com】.mp4
- 时长 4分59秒（音频 300s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才我们把业务层的代码这都全部编写完了编完之后咱接下来需要再完善一块代码还是哪对还是Controller咱之前Controller是一个空实现现在我们要把它给完善一下跟之前一样就是调用一下什么样业务层的方法把这些数据传给业务层业务层处理完之后是不是反而给我们一个配置view对象然后我们封装到rest response边给前端就OK了这个代码大家都比较熟悉了
[00:32] 我们找到我们的control软就这儿是吧这个格式吧你现在自己给吧好大概这样就OK了呃那这个代码咱就算完善了啊这个完善完之后呢咱们整个什么呀标的信息这个查询的这个功能我们就搞定了那咱接下来就要进行测试那咱这个测试的话还是直接就进行这个前后端集中测试因为这个功能本身就比较简单只是一个查询而已那咱看看吧咱都需要启动啥呀
[01:06] Apollo我已经启动过了是不是然后前端工程哎这个前端工程你一定要注意了这个前端工程可不是咱以前那个consumer那个用户那个前端工程是咱最近刚给大家介绍的p2p平台的这个什么呀前端管理平台的前端这个我们需要给他启动一下是不是怎么启动啊点右键然后呢命令是吧执行npm run dv然后呢这个后端的微服我们都需要启动啥后端微服你看吧
[01:38] 我们也要登录嘛所以说跟登录有关的consumer对吧这个ua啊account都要启动注册中心不用说了网关也得启动我们是前后端集成测试嘛那还有这个transaction对不对这个存款代理我们现在用不着大概这些微服务吧你都得启动我这也都启动过了那我们就等着这个前端启动吧前端启动完之后呢这个前端没反应吗哎这是咋的事我再点一下再点一下啊
[02:13] 那是不是那个那个那个视图我我是不小心的关了呀是哪个空来还是中端中端吗在这已经走过了是吧8079是吧我啥没有自动给咱打开这个页面呢好我们接下来输一下密码admin登录登录完之后你看这数据已经查出来了是不是你看这我们这样我们把这个
[02:45] 开发者工具给他打开给他调出来调出来之后我们也看看他发了请求这边这些报的这些错误你不用管因为这里边好多功能咱都没开发了我们正常应该是点这点这这就是用来查询我们刚才说的什么标题信息的你可以点一下你观察下控制台你看你看这是不是发请求了是不是你看这我们看看他完整的请求他是往transaction发的对不对projectsq
[03:15] 你找找咱刚才这个Controller是不是projectsq对不对然后你看后边传过来的数据你看pose的请求是不是咱这也是什么pose的请求然后后边有什么第一页一页显示实行这怎么传两遍这个钱的代码可能有点问题不过不影响效果对吧好什么状态是零好这个是标底的状态collection它是表示目击中相当于是新标了基本上
[03:45] 这前端吧他他写的这个代码咱也不用管啊只要不报错咱也不用管然后呢由于我们表里边是不是就一行数据吧是不是咱以前发标就用这个白的女士发了一次标嘛对不对所以这只能查出来一条数据啊就这么讲但这个功能是咱的确实现那么下边的话就是这样啊因为前端这个代码我们是直接提问大家你知道你要想很灵活的对咱刚才这个代码进行测试的话你还是要去postman里
[04:13] 在普罗内曼里边呢你这些值你就随便改当然呢咱这个现在毕竟是表里边数据有限的就一条吧你看看你也可以回头拿着那个那个什么呀发标那个你可以多发几次标嘛发个一二十次的对不对这样呢就可以测出来这个什么呀分页的这个效果所以这呢咱这个数据比较少我就不再过多给大家测试了这个下去大家自己测啊就是第一个你要多发几次标让这个数据多一些最起码你能查发两页吧是不是
[04:43] 第二个呢就是你要测什么测这些条件你给不同的条件是不是看看他这个查询出来的结果有啥变化没有这个大家下去自己测一下就行这是目前吧咱们把这个标底信息查询这个功能也测出过了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在万信金融项目中，通过前后端联调，实现分页查询项目数据的完整流程，包括后端 Controller 代码编写、前端页面开发与网络请求调试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 IDE 中的项目结构和代码编辑器。
- 代码内容：在 TransactionController 中定义了 @PostMapping("/projects/q") 方法，接收 ProjectQueryDTO 参数，调用 projectService.queryProjectsByQueryDTO 方法，并返回 RestResponse.success(projects)。
- 画面标题：4. 完善TransactionController类中的代码。
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 2:
- 展示了 IDE 中的代码编辑器，显示了项目分页查询的业务逻辑代码。
- 代码内容：在 private List<ProjectDTO> convertProjectEntityListToDTOList(List<Project> projectList) 方法中，对项目实体列表进行转换，创建 ProjectDTO 对象并添加到 dtolist 中。
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 3:
- 展示了 IDE 中的代码编辑器，显示了 TransactionController 中的 queryProjects 方法。
- 代码内容：@PostMapping("/projects/q") public RestResponse<PageVO<ProjectDTO>> queryProjects(@RequestBody ProjectQueryDTO projectQueryDTO, String order, Integer pageNo, Integer pageSize, String sortBy) { PageVO<ProjectDTO> projects = projectService.queryProjectsByQueryDTO(projectQueryDTO, order, pageNo, pageSize, sortBy); return RestResponse.success(projects); }
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 4:
- 展示了 IDE 中的代码编辑器，显示了 TransactionController 中的 queryProjects 方法。
- 代码内容：@PostMapping("/projects/q") public RestResponse<PageVO<ProjectDTO>> queryProjects(@RequestBody ProjectQueryDTO projectQueryDTO, String order, Integer pageNo, Integer pageSize, String sortBy) { PageVO<ProjectDTO> projects = projectService.queryProjectsByQueryDTO(projectQueryDTO, order, pageNo, pageSize, sortBy); return RestResponse.success(projects); }
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 5:
- 展示了 HBuilder X 的项目结构，显示了 p2pManager 项目的文件夹结构。
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 6:
- 展示了 IDE 中的代码编辑器，显示了 TransactionController 中的 queryProjects 方法。
- 代码内容：@PostMapping("/projects/q") public RestResponse<PageVO<ProjectDTO>> queryProjects(@RequestBody ProjectQueryDTO projectQueryDTO, String order, Integer pageNo, Integer pageSize, String sortBy) { PageVO<ProjectDTO> projects = projectService.queryProjectsByQueryDTO(projectQueryDTO, order, pageNo, pageSize, sortBy); return RestResponse.success(projects); }
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 7:
- 展示了 IDE 中的代码编辑器，显示了 TransactionController 中的 queryProjects 方法。
- 代码内容：@PostMapping("/projects/q") public RestResponse<PageVO<ProjectDTO>> queryProjects(@RequestBody ProjectQueryDTO projectQueryDTO, String order, Integer pageNo, Integer pageSize, String sortBy) { PageVO<ProjectDTO> projects = projectService.queryProjectsByQueryDTO(projectQueryDTO, order, pageNo, pageSize, sortBy); return RestResponse.success(projects); }
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 8:
- 展示了 HBuilder X 的项目结构，显示了 p2pManager 项目的文件夹结构。
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 9:
- 展示了浏览器中的登录页面，显示了万信金融的登录界面。
- 登录信息：用户名为 "admin"，密码为空。
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 10:
- 展示了浏览器中的贷款管理页面，显示了贷款信息。
- 页面内容：贷款名称为“白瑞女士第12次借款”，金额为 10000 元，创建时间为 2019-08-23，期限为 12 个月，状态为“募集中”，年化利率为 15%。
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 11:
- 展示了浏览器中的网络请求面板，显示了请求的详细信息。
- 请求信息：Request URL: http://127.0.0.1:13908/transaction/projects/q?pageNo=1&pageSize=10&sortStatus=COLLECTING，Request Method: POST，Status Code: 200。
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 12:
- 展示了 IDE 中的代码编辑器，显示了 TransactionController 中的 queryProjects 方法。
- 代码内容：@PostMapping("/projects/q") public RestResponse<PageVO<ProjectDTO>> queryProjects(@RequestBody ProjectQueryDTO projectQueryDTO, String order, Integer pageNo, Integer pageSize, String sortBy) { PageVO<ProjectDTO> projects = projectService.queryProjectsByQueryDTO(projectQueryDTO, order, pageNo, pageSize, sortBy); return RestResponse.success(projects); }
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 13:
- 展示了浏览器中的网络请求面板，显示了请求的详细信息。
- 请求信息：Request URL: http://127.0.0.1:13908/transaction/projects/q?pageNo=1&pageSize=10&sortStatus=COLLECTING，Request Method: POST，Status Code: 200。
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

画面 14:
- 展示了浏览器中的网络请求面板，显示了请求的详细信息。
- 请求信息：Request URL: http://127.0.0.1:13908/transaction/projects/q?pageNo=1&pageSize=10&sortStatus=COLLECTING，Request Method: POST，Status Code: 200。
- 画面中显示的 PPT 标题：3.4.3 前后端集成测试。

