# 画面线理解：02-热门学科排名-业务报表系统字段分析

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\02-热门学科排名-业务报表系统字段分析_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 00:58, 03:11, 03:20, 03:23, 04:13, 04:30, 04:33, 04:45, 05:11, 05:34, 05:43, 05:48, 05:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:11:14

1) 这一组画面整体在讲什么（一句话）：
展示一个热门学科排名Web前端页面的实时数据统计与后端API交互过程，包括数据模型、查询分析和前端展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：前端页面显示热门学科排名图表和数据表格，右侧浏览器开发者工具的Network面板显示对“/statistics”接口的GET请求，响应数据为JSON格式，包含多个学科的销售金额、销售量、学生人数等字段。
画面2：PPT页面，标题为“3.2 数据模型”，子标题“3.2.1 数据结构分析”，表格列出数据字段：subjectName（学科名，string）、amountPercent（销售额增幅，float）、saleAmount（销售额，int）、saleNum（销售量，int）、salePercent（销售量增幅，float）、userNum（学生人数，int）、userPercent（学生人数增幅，float），并给出数据示例。
画面3：PPT页面，标题为“3.2.2 数据查询分析”，表格分为“周查询前端请求”和“月查询前端请求”两部分，分别说明以周或月为单位查询时的前端参数（如datePickerSel=2019-39&type=week）和响应数据格式（如{subjectName: "Java", saleNum: 49687, salePercent: 0.44, userNum: 52198,...}）。
画面4：与画面1内容相同，前端页面显示热门学科排名图表和数据表格，右侧浏览器开发者工具的Network面板显示对“/statistics”接口的GET请求，响应数据为JSON格式，包含多个学科的销售金额、销售量、学生人数等字段。
画面5：与画面1内容相同，前端页面显示热门学科排名图表和数据表格，右侧浏览器开发者工具的Network面板显示对“/statistics”接口的GET请求，响应数据为JSON格式，包含多个学科的销售金额、销售量、学生人数等字段。
画面6：前端页面切换至“用户统计”页面，显示按周或月的统计数据表格，右侧浏览器开发者工具的Network面板显示对“/statistics”接口的GET请求，响应数据为JSON格式，包含多个学科的销售金额、销售量、学生人数等字段。
画面7：PPT页面，标题为“3.2.2 数据查询分析”，表格分为“周查询前端请求”和“月查询前端请求”两部分，分别说明以周或月为单位查询时的前端参数（如datePickerSel=2019-39&type=week）和响应数据格式（如{subjectName: "Java", saleNum: 49687, salePercent: 0.44, userNum: 52198,...}）。
画面8：PPT页面，标题为“3.2.2 数据查询分析”，表格分为“周查询前端请求”和“月查询前端请求”两部分，分别说明以周或月为单位查询时的前端参数（如datePickerSel=2019-39&type=week）和响应数据格式（如{subjectName: "Java", saleNum: 49687, salePercent: 0.44, userNum: 52198,...}）。
画面9：PPT页面，标题为“3.2 数据模型”，子标题“3.2.1 数据结构分析”，表格列出数据字段：subjectName（学科名，string）、amountPercent（销售额增幅，float）、saleAmount（销售额，int）、saleNum（销售量，int）、salePercent（销售量增幅，float）、userNum（学生人数，int）、userPercent（学生人数增幅，float），并给出数据示例。
画面10：PPT页面，标题为“3.3 数据采集”，子标题“3.3.1 ODS层数据结构-用户选课”，说明销售数据来源为课程购买，学生数据来源为用户选课（MySQL），并提及可采用NIFI生产的方式。
画面11：PPT页面，标题为“3.2.2 数据查询分析”，表格分为“周查询前端请求”和“月查询前端请求”两部分，分别说明以周或月为单位查询时的前端参数（如datePickerSel=2019-39&type=week）和响应数据格式（如{subjectName: "Java", saleNum: 49687, salePercent: 0.44, userNum: 52198,...}）。
画面12：PPT页面，标题为“3.2.2 数据查询分析”，表格分为“周查询前端请求”和“月查询前端请求”两部分，分别说明以周或月为单位查询时的前端参数（如datePickerSel=2019-39&type=week）和响应数据格式（如{subjectName: "Java", saleNum: 49687, salePercent: 0.44, userNum: 52198,...}）。
画面13：PPT页面，标题为“3.2.2 数据查询分析”，表格分为“周查询前端请求”和“月查询前端请求”两部分，分别说明以周或月为单位查询时的前端参数（如datePickerSel=2019-39&type=week）和响应数据格式（如{subjectName: "Java", saleNum: 49687, salePercent: 0.44, userNum: 52198,...}）。
画面14：PPT页面，标题为“3.2.2 数据查询分析”，表格分为“周查询前端请求”和“月查询前端请求”两部分，分别说明以周或月为单位查询时的前端参数（如datePickerSel=2019-39&type=week）和响应数据格式（如{subjectName: "Java", saleNum: 49687, salePercent: 0.44, userNum: 52198,...}）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1、4、5、6、7、8、11、12、13、14：
```json
{
  "code": 200,
  "msg": "voluptate est ut dolore",
  "result": [
    {
      "subjectName": "Fugiat",
      "saleNum": 94953,
      "salePercent": 62.5,
      "saleAmount": 5079,
      "userNum": 44524,
      "userPercent": 87.6
    },
    {
      "subjectName": "Ipsum est",
      "saleNum": 50956,
      "salePercent": 38.7,
      "saleAmount": 3202,
      "userNum": 81649,
      "userPercent": 83.9
    },
    {
      "subjectName": "ex incididunt am",
      "saleNum": 10480,
      "salePercent": 61.2,
      "saleAmount": 2627,
      "userNum": 41305,
      "userPercent": 11.9
    },
    {
      "subjectName": "ut",
      "saleNum": 56048,
      "salePercent": 61.9,
      "saleAmount": 5821,
      "userNum": 84885,
      "userPercent": 19.4
    },
    {
      "subjectName": "tempor minim",
      "saleNum": 51696,
      "salePercent": 69.0,
      "saleAmount": 2004,
      "userNum": 76232,
      "userPercent": 22.5
    },
    {
      "subjectName": "es",
      "saleNum": 749,
      "salePercent": 93.8,
      "saleAmount": 2626,
      "userNum": 56889,
      "userPercent": 5.4
    },
    {
      "subjectName": "consequat ea",
      "saleNum": 32625,
      "salePercent": 74.1,
      "saleAmount": 7984,
      "userNum": 30184,
      "userPercent": 29.9
    },
    {
      "subjectName": "exercitation qui voluptate oc",
      "saleNum": 25174,
      "salePercent": 91.8,
      "saleAmount": 4410,
      "userNum": 78410,
      "userPercent": 7.9
    }
  ]
}
```

画面5：
```json
{
  "code": 200,
  "msg": "tempor dolor",
  "result": []
}
```

画面6：
```json
{
  "code
