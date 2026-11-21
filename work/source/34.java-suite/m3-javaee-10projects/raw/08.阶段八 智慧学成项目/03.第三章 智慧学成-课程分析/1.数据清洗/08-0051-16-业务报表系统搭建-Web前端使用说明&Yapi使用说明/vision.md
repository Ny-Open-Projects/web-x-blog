# 画面线理解：16-业务报表系统搭建-Web前端使用说明&Yapi使用说明

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/1.数据清洗
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\1.数据清洗\16-业务报表系统搭建-Web前端使用说明&Yapi使用说明_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:25, 02:36, 03:05, 03:22, 04:09, 04:38, 04:58, 05:48, 06:15, 06:46, 07:22, 07:53, 08:47, 09:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:58:10

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Yapi 平台进行 API 接口管理，包括环境配置、项目创建、接口导入和前端服务部署。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Nifi 流程，包含“1. 数据采集”、“2. 数据清洗”和“3. 同步到业务库”三个步骤，用于数据处理。
画面 2: 显示了 Yapi 平台的文档，内容为“1. 源码”和“2. docker-compose.yml 配置”，并提示源码需解压到指定位置。
画面 3: 展示了 Yapi 平台的前端界面，包含数据统计图表和服务器信息，如“xc-online-yapi”服务。
画面 4: 显示了 Yapi 平台的“docker-compose.yml 配置”部分，包含服务定义和端口映射。
画面 5: 展示了 Yapi 平台的登录界面，用户名为“admin@admin.com”，密码已输入。
画面 6: 显示了文件选择对话框，用于上传文件到 Yapi 平台。
画面 7: 展示了 Yapi 平台的“数据导入”页面，提示用户点击上传接口文件。
画面 8: 展示了 Xshell 终端界面，用于远程连接服务器。
画面 9: 展示了 WinSCP 文件传输界面，显示了“docker-compose.yml”等文件。
画面 10: 显示了 Sublime Text 编辑器中的“yapi.config.js”文件，包含代理配置。
画面 11: 展示了 Yapi 平台的项目设置页面，包含项目名称、所属空间和 MOCK 地址。
画面 12: 展示了 Xshell 终端界面，用于执行命令。
画面 13: 展示了 Xshell 终端界面，显示了 Vue CLI 服务启动成功，应用运行在 http://localhost:8080。
画面 14: 展示了 Yapi 平台的前端界面，包含数据统计图表和服务器信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
源码位置：
  _ 接收资料
    _ 第3层：课程分析
      _ code
        _ yapi.zip
```
画面 4:
```
xc-online-yapi:
  container_name: xc-online-yapi
  image: yapi/1.10.0
  ports:
    - "3000:3000"
  environment:
    - NODE_ENV=production
    - PORT=3000
    - YAPI_DB_HOST=127.0.0.1
    - YAPI_DB_PORT=3306
    - YAPI_DB_USER=root
    - YAPI_DB_PASS=123456
    - YAPI_DB_NAME=yapi
  volumes:
    - ./yapi:/opt/yapi
    - ./yapi/logs:/opt/yapi/logs
    - ./yapi/config:/opt/yapi/config
  restart: always
```
画面 10:
```
open: true,
port: 8080,
host: "0.0.0.0",
proxy: {
  "xuecheng": {
    // 原型环境
    // target: "https://mock.boxegeu.com/mock/143",
    // docker: yapi 原型环境
    // target: "http://xc-online-yapi:3000/mock/11",
    // 开发环境，通过一系列清洗最终落地到业务库
    target: "http://xc-online:8080",
    changeOrigin: true,
    pathRewrite: {
      "^/xuecheng": ""
    }
  }
}
```
画面 11:
```
MOCK地址：http://xc-online:3000/mock/14
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“Yapi平台”，内容包括“1. 源码”和“2. docker-compose.yml 配置”。
画面 4: PPT 标题为“docker-compose.yml 配置”，内容包括服务定义和端口映射。
画面 11: PPT 标题为“项目设置”，内容包括项目名称、所属空间和 MOCK 地址。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
