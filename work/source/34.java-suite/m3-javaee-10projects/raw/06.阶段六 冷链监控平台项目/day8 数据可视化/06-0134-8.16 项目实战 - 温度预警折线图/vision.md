# 画面线理解：8.16 项目实战 - 温度预警折线图

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day8 数据可视化
- 源文件：06.阶段六 冷链监控平台项目\day8 数据可视化\8.16 项目实战 - 温度预警折线图_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:44, 01:05, 01:14, 02:46, 03:32, 03:36, 03:42, 04:09, 04:25, 04:46, 04:59, 05:20, 05:27, 05:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 18:01:04

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Superset 中创建仓库温度预警折线图，并将其嵌入前端 Vue 应用中。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程文档，当前章节为“9.2.1 需求分析”，内容为“冷链设备监控平台需要按仓库维度每小时预警数量”，需求包括“1. 仓库维度”、“2. 每小时”、“3. 预警分析”。
画面 2: 在 Superset 中创建新图表，选择数据源为“all_device_message”，可视化类型选择“Table”。
画面 3: Superset 页面加载中，显示空白。
画面 4: Superset 中配置查询，筛选条件为“timestamp > 0”，分组为“housecode”，排序为“Sort Descending”，行限制为“50000”。
画面 5: 在 IntelliJ IDEA 中打开 Vue 项目，查看 `dashboard/index.vue` 文件，其中包含 `<div class="disFlex">` 和 `<div class="content">` 等结构。
画面 6: Superset 中配置图表，数据源为“all_device_message”，可视化类型为“Line Chart”，时间粒度为“1 hour”，并显示“仓库 温度 预警折线图”。
画面 7: 前端应用页面，显示“冰眼”系统首页，包含地图和设备图标。
画面 8: 在终端运行 `npm` 命令，显示构建进度。
画面 9: 前端应用页面，显示“仓库 温度 预警折线图”，图表数据已加载。
画面 10: Superset 中配置图表，数据源为“all_device_message”，可视化类型为“Line Chart”，时间粒度为“1 hour”，并显示“仓库 温度 预警折线图”。
画面 11: Superset 中配置图表，数据源为“all_device_message”，可视化类型为“Line Chart”，时间粒度为“1 hour”，并显示“仓库 温度 预警折线图”，点击“Save”按钮。
画面 12: 在 IntelliJ IDEA 中打开 `dashboard/index.vue` 文件，查看 `<iframe>` 标签的代码，其中 `src` 属性包含 Superset 的 URL。
画面 13: 在终端运行 `npm` 命令，显示构建进度。
画面 14: 前端应用页面，显示“仓库 温度 预警折线图”链接，页面空白。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```html
<div class="content" style="height: 200px;">
  <BaiduMap v-if="mapData" :data="mapData"></BaiduMap>
</div>
<div class="disFlex">
  <div class="cont" style="height:450px;">
    <div class="title">故障设备状态图</div>
    <div class="content">
    </div>
  </div>
</div>
```
画面 12:
```html
<iframe
  width="1000"
  height="400"
  seamless
  frameBorder="0"
  scrolling="no"
  src="http://172.17.0.143:8088/superset/explore/?form_data=%7B%22datasource%22%3A%22all_device_message%22%2C%22viz_type%22%3A%22line%22%7D"
>
</iframe>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
