# 画面线理解：07_后端通用封装-类图关系说明

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\07_后端通用封装-类图关系说明【海量资源尽在 666java.com】.mp4
- 抽帧：8 帧 @ 00:13, 00:14, 00:30, 00:36, 00:41, 00:42, 03:43, 03:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:01:48

1) 这一组画面整体在讲什么（一句话）：
讲解通用封装后端开发中各核心类（如 CommonWhereDto、CommonDto、CommonDao 等）的职责与类图关系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了“4 通用封装-后端开发”章节下的“4.1 类图说明”PPT页面。
- 页面中央是一个类图，包含多个类节点（如 CommonWhereDto、CommonTableEnum、CommonDto、CommonDao、Service、CommonService、CommonController）及其继承/依赖关系。
- 页面下方列出了各类的说明：
  - CommonTableEnum: 用于定义哪些数据表可支持通用操作，及其开发的CRUD功能
  - CommonWhereDto: 用于接收前端传入的修改字段或查询条件参数
  - CommonDto: 用于接收前端传入的接口参数（包括CRUD接口的参数）
  - CommonDao: 持久层动态SQL拼接实现
  - CommonServiceImpl: 用于实现CRUD的通用逻辑处理
  - CommonController: 实现通用接口的控制层定义
- 右下角显示了“按住空格键选择区域”的提示框，尺寸为 1280 x 720。
- 左侧是文档大纲，当前选中“4.1 类图说明”。

画面2：
- 画面内容与画面1基本一致，但鼠标光标位于左侧边栏，显示“拖动以调整选区”提示。
- 右下角的提示框尺寸变为 800 x 450。
- 左侧大纲仍选中“4.1 类图说明”。

画面3：
- 画面内容与画面1基本一致，鼠标光标位于页面中央。
- 右下角无提示框。
- 左侧大纲仍选中“4.1 类图说明”。

画面4：
- 画面内容与画面1基本一致，鼠标光标位于页面中央。
- 右下角无提示框。
- 左侧大纲仍选中“4.1 类图说明”。

画面5：
- 画面内容与画面1基本一致，鼠标光标位于页面右上角。
- 右下角显示“按住空格键选择区域”的提示框，尺寸为 1280 x 720。
- 左侧大纲仍选中“4.1 类图说明”。

画面6：
- 画面内容与画面1基本一致，鼠标光标位于左侧边栏，显示“拖动以调整选区”提示。
- 右下角的提示框尺寸变为 800 x 450。
- 左侧大纲仍选中“4.1 类图说明”。

画面7：
- 画面内容与画面1基本一致，鼠标光标位于页面中央。
- 右下角无提示框。
- 左侧大纲仍选中“4.1 类图说明”。

画面8：
- 画面内容与画面1基本一致，鼠标光标位于页面中央。
- 右下角无提示框。
- 左侧大纲仍选中“4.1 类图说明”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
PPT标题：
- 4 通用封装-后端开发
- 4.1 类图说明

架构图/流程图结构：
- 类图包含以下节点：
  - CommonWhereDto
  - CommonTableEnum
  - CommonDto
  - CommonDao
  - Service
  - CommonService
  - CommonController
  - BaseCommonFilter
- 连接关系（箭头方向）：
  - CommonWhereDto → CommonDto
  - CommonTableEnum → CommonDto
  - CommonDto → CommonDao
  - CommonDao → Service
  - CommonService → CommonController
  - BaseCommonFilter → CommonDao
  - BaseCommonFilter → CommonService
  - BaseCommonFilter → CommonController

表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
