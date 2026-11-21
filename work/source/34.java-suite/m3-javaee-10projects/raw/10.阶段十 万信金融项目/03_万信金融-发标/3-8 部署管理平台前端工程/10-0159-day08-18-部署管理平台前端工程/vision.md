# 画面线理解：day08-18-部署管理平台前端工程

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-8 部署管理平台前端工程
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-8 部署管理平台前端工程\day08-18-部署管理平台前端工程_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 02:01, 03:16, 04:00, 04:51, 05:48, 06:39, 07:32, 08:23, 09:16, 09:59, 10:26, 11:31, 11:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:56:12

1) 这一组画面整体在讲如何部署和运行万信金融管理平台的前端工程，包括环境搭建、服务启动和登录验证。

2) 按时间顺序列出每张画面的要点：
画面1: 展示前端页面“资料审核中”状态，同时浏览器开发者工具的Network面板显示XHR请求状态为“(Paused)”。
画面2: PPT标题为“3.3.1 打开前端工程”，内容说明前端工程位于资料文件夹中的p2pManager，使用vue-element-admin集成方案，技术栈为vue [2.6.10] + element-ui [2.7.0] + axios。
画面3: 文件资源管理器显示路径为“wanxin2p > day06 > 资料”，其中包含“安装 Apollo配置.txt”等文件。
画面4: PPT标题为“3.3.2 搭建运行环境”，展示系统架构图：用户前端（wanxin2p_front）和管理平台前端（p2pManager）均指向网关，网关指向服务端（wanxin2p-discover-server, wanxin2p-account-service, wanxin2p-consumer-service, wanxin2p-uaa-service...），Apollo指向网关。
画面5: 展示前端页面“资料审核中”状态，同时浏览器开发者工具的Network面板显示XHR请求状态为“(Paused)”。
画面6: HBuilder X编辑器打开项目“p2pManager”，显示项目目录结构，包括“.editorconfig”、“.env.development”、“.env.production”、“.eslintrc.js”、“babel.config.js”、“package.json”、“postcss.config.js”等文件。
画面7: PPT内容说明“内置终端”功能，可在菜单视图中呼出，用于执行npm install等命令。
画面8: HBuilder X的控制台显示npm安装过程中的警告信息，包括“npm WARN deprecated circular-json@0.3.3:”等。
画面9: PPT内容说明前端工程运行在“http://localhost:8079/”，并提示需要启动Apollo及多个后端服务才能成功登录。
画面10: 浏览器显示万信金融登录页面，输入账号“admin”和密码，点击“登录”按钮。
画面11: HBuilder X中右键点击项目“p2pManager”，弹出菜单，包含“新建(N)”、“在新窗体中打开(K)”、“打开文件所在目录(I)”、“使用命令行窗口打开目录所在目录(U)”等选项。
画面12: IDE中打开“ConsumerService.java”文件，代码中包含“SecurityUtil.getMobile()”方法调用，下方控制台显示“ConfigClusterResolver.java:4”等日志信息。
画面13: 浏览器地址栏显示“localhost:8079/#/login?redirect=%2Fdashboard”，页面为万信金融登录页面。
画面14: PPT标题为“3.3 部署万信金融管理前端”，内容说明P2P公司管理员需要登录万信金融管理平台进行审核，该功能同放在Wanxin2p-transaction-service工程中实现，需要一个独立的前端（管理平台）作为审核的入口。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面6: 项目目录结构：
```
p2pManager
├── build
├── dist
├── mock
├── node_modules
├── public
├── src
├── tests
├── .editorconfig
├── .env.development
├── .env.production
├── .eslintrc.js
├── .gitignore
├── .travis.yml
├── babel.config.js
├── demo.png
├── LICENSE
├── package.json
├── package-lock.json
└── postcss.config.js
```
画面7: 文本内容：
```
内置终端
内置的命令行终端，可在菜单视图中呼出
```
画面9: 文本内容：
```
App running at:
- Local: http://localhost:8079/
- Network: http://192.168.25.128:8079/

Note that the development build is not optimized.
To create a production build, run npm run build.

6. 在浏览器中访问登录页面，账号和密码都是admin。要想登录成功，需要启动Apollo以及wanxin2p-discover-server, wanxin2p-account-service, wanxin2p-consumer-service, wanxin2p-gateway-server, wanxin2p-uaa-service等服务。
```
画面12: 代码片段：
```java
private ConfigService configService;

@Override
public ProjectDTO createProject(ProjectDTO projectDTO) {
    RestResponse<ConsumerDTO> restResponse = consumerApiAgent.getConsumerSecurityUtil.getMobile());
    projectDTO.setConsumerId(restResponse.getResult().getConsumerId());
    projectDTO.setProjectNo(projectDTO.getNo(CodePrefixCode.COD_PROJECT_PREFIX));
    // 根据天数生成
    return projectDTO;
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面4: 架构图结构：
- 用户前端（wanxin2p_front） → 网关
- 管理平台前端（p2pManager） → 网关
- 网关 → 服务端（wanxin2p-discover-server, wanxin2p-account-service, wanxin2p-consumer-service, wanxin2p-uaa-service...）
- Apollo → 网关

画面9: 表格数据（无表格，仅文字说明）：
- App running at: Local: http://localhost:8079/
- Network: http://192.168.25.128:8079/
- Note that the development build is not optimized.
- To create a production build, run npm run build.
- 6. 在浏览器中访问登录页面，账号和密码都是admin。要想登录成功，需要启动Apollo以及wanxin2p-discover-server, wanxin2p-account-service, wanxin2p-consumer-service, wanxin2p-gateway-server, wanxin2p-uaa-service等服务。

画面14: 表格数据（无表格，仅文字说明）：
- 交易中心保存完好的信息后，P2P公司管理员就需要登录万信金融管理平台对该标的进行审核，该功能同样放在Wanxin2p-transaction-service工程中实现，但是该功能需要一个独立的前端（管理平台）作为审核的入口。

5) 无。
