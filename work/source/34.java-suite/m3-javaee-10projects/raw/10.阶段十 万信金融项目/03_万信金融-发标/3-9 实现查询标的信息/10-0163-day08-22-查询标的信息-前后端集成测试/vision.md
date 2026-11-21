# 画面线理解：day08-22-查询标的信息-前后端集成测试

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-9 实现查询标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-9 实现查询标的信息\day08-22-查询标的信息-前后端集成测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:06, 00:13, 00:56, 01:31, 01:56, 02:01, 02:21, 02:31, 02:50, 03:11, 03:23, 03:52, 04:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:59:16

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
