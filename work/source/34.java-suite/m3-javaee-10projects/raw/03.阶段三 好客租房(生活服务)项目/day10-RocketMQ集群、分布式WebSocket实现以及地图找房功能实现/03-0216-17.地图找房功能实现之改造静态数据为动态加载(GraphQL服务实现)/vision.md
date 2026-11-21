# 画面线理解：17.地图找房功能实现之改造静态数据为动态加载（GraphQL服务实现）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\17.地图找房功能实现之改造静态数据为动态加载（GraphQL服务实现）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:50, 01:40, 02:43, 03:30, 04:15, 05:19, 06:19, 07:19, 07:53, 08:43, 09:45, 10:37, 11:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:21:59

1) 这一组画面整体在讲如何通过 GraphQL 查询动态数据，并在前端 React 页面上使用百度地图 API 展示这些数据点，同时使用 MarkerClusterer 实现地图上点的聚合效果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中“5.2.1、修改数据的加载逻辑”章节，图示目录结构中高亮显示 `maphouse.js` 文件，文字说明“可以看到，目前的数据是静态的，需要改成加载后台数据的方式”。
画面2：展示 PDF 文档中定义的 TypeScript 接口 `type HaookeQuery` 和 `type HouseResources`。
画面3：展示 PDF 文档中定义的 TypeScript 接口 `type IndexAdResult`、`type IndexAdResultData` 和 `type MapHouseXY`。
画面4：展示 PDF 文档中定义的 Java 类 `MapHouseDataFetcher` 的部分代码，包含 `@Override` 注解和 `dataFetcher` 方法。
画面5：展示 IntelliJ IDEA 中的项目结构和 GraphQL 查询文件 `HouseResourcesDataFetcher.java`，其中包含 `type TableResult`、`type Pagination`、`type IndexAdResult` 和 `type IndexAdResultData` 的定义。
画面6：展示 IntelliJ IDEA 中的项目结构和 `maphouse.js` 文件，其中包含 `import React from 'react';`、`import { Icon } from 'semantic-ui-react';`、`import ApolloClient from 'apollo-boost';` 和 `import gql from 'graphql';` 的导入语句。
画面7：展示 IntelliJ IDEA 中的 `MapHouseDataFetcher` 类代码，包含 `@Override` 注解和 `dataFetcher` 方法。
画面8：展示 Altair GraphQL Client 界面，URL 为 `http://127.0.0.1:8000/graphql`，提示“Welcome to Altair GraphQL Client”。
画面9：展示 IntelliJ IDEA 中的 `maphouse.js` 文件，包含 `import React from 'react';`、`import { Icon } from 'semantic-ui-react';`、`import ApolloClient from 'apollo-boost';` 和 `import gql from 'graphql';` 的导入语句。
画面10：展示 PDF 文档中 `maphouse.js` 文件的代码，包含 `client.query(query: GET_MAP_HOUSE).then(result => {`、`var markers = [];`、`var pt = null;` 和 `for (var i in xys) {` 等语句。
画面11：展示 IntelliJ IDEA 中的 `maphouse.js` 文件，包含 `let pt = null;`、`for (let i in xys) {`、`pt = new BMap.Point(xys[i].x, xys[i].y);` 和 `markers.push(new BMap.Marker(pt));` 等语句。
画面12：展示 IntelliJ IDEA 中的 `maphouse.js` 文件，包含 `let pt = null;`、`for (let i in xys) {`、`pt = new BMap.Point(xys[i].x, xys[i].y);` 和 `markers.push(new BMap.Marker(pt));` 等语句。
画面13：展示浏览器中百度地图页面，显示“地图找房”，地图上有两个绿色圆圈标记，右侧是 Chrome 开发者工具的 Network 标签页，显示请求 URL 为 `http://127.0.0.1:8000/graphql`。
画面14：展示 PDF 文档中 `maphouse.js` 文件的代码，包含 `client.query(query: GET_MAP_HOUSE).then(result => {`、`var markers = [];`、`var pt = null;` 和 `for (var i in xys) {` 等语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```
home
├── calc.js
├── home.css
├── home.js
├── list.js
├── maphouse.js
└── searchbar.js
```
画面2：
```typescript
type HaookeQuery {
  HouseResources: HouseResources
  HouseResourcesList(page: Int, pageSize: Int): TableResult
  IndexAdList: IndexAdResult
  MapHouseData: MapHouseDataResult
}

type HouseResources {
  id: Long!
  estateId: Long
  buildingNum: String
  buildingInit: String
  buildingFloorNum: Number
  rent: Int
}
```
画面3：
```typescript
type IndexAdResult {
  list: [IndexAdResultData]
}

type IndexAdResultData {
  original: String
}

type MapHouseXY {
  x: Float
  y: Float
}
```
画面4：
```java
package cn.itcast.haoke.dubbo.api.vo.map;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
```
画面5：
```graphql
type TableResult(
  list: [HouseResources]
  pagination: Pagination
)

type Pagination(
  current: Int
  pageSize: Int
  total: Int
)

type IndexAdResult(
  list: [IndexAdResultData]
)

type IndexAdResultData(
  original: String
)
```
画面6：
```javascript
import React from 'react';
import { Icon } from 'semantic-ui-react';
import ApolloClient from 'apollo-boost';
import gql from 'graphql';
```
画面7：
```java
public class MapHouseDataFetcher implements MyDataFetcher {

  @Override
  public String fieldName() {
    return "MapHouseData";
  }

  @Override
  public Object dataFetcher(DataFetchingEnvironment environment) {
    List<MapHouseXY> list = null;
    return list;
  }
}
```
画面9：
```javascript
import React from 'react';
import { Icon } from 'semantic-ui-react';
import ApolloClient from 'apollo-boost';
import gql from 'graphql';

class MapHouse extends React.Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    // 百度地图API函数
    var BMap = window.BMap;
    var BMapLib = window.BMapLib;
    // 创建地图实例
    var map = new BMap.Map("allmap");
    // 初始化地图，设置中心点坐标和级别
    map.centerAndZoom(new BMap.Point(116.43244, 39.929986), 12);
    // 添加地图控件
    map.addControl(new BMap.MapTypeControl());
    // 设置地图缩放级别
    map.addControl(new BMap.ScaleControl({
      anchor: window.BMAP_NAVIGATION_CONTROL_ZOOM
    }));
  }
}
```
画面10：
```javascript
client.query(query: GET_MAP_HOUSE).then(result => {
  var xys = result.data.MapHouseData.list;
  var markers = [];
  var pt = null;
  for (var i in xys) {
    pt = new BMap.Point(xys[i].x, xys[i].y);
    markers.push(new BMap.Marker(pt));
  }
  // 地图上覆盖物的聚合效果
  var markerClusterer = new BMapLib.MarkerClusterer(map, {
    markers: markers,
    gridSize: 100,
    styles: [
      {
        background: 'rgba(12,181,106,0.9)',
        size: new BMap.Size(92, 92),
        textSize: '16',
        textColor: '#fff',
        borderRadius: 'true'
      }
    ]
  });
  markerClusterer.setMaxZoom(50);
  markerClusterer.setGridSize(50);
});
```
画面11：
```javascript
let pt = null;
for (let i in xys) {
  pt = new BMap.Point(xys[i].x, xys[i].y);
  markers.push(new BMap.Marker(pt));
}
// 地图上覆盖物的聚合效果
var markerClusterer = new BMapLib.MarkerClusterer(map, {
  markers: markers,
  gridSize: 100,
  styles: [
    {
      background: 'rgba(12,181,106,0.9)',
      size: new BMap.Size(92, 92),
      textSize: '16',
      textColor: '#fff',
      borderRadius: 'true'
    }
  ]
});
markerClusterer.setMaxZoom(50);
markerClusterer.setGridSize(10);
```
画面12：
```javascript
let pt = null;
for (let i in xys) {
  pt = new BMap.Point(xys[i].x, xys[i].y);
  markers.push(new BMap.Marker(pt));
}
// 地图上覆盖物的聚合效果
var markerClusterer = new BMapLib.MarkerClusterer(map, {
  markers: markers,
  gridSize: 100,
  styles: [
    {
      background: 'rgba(12,181,106,0.9)',
      size: new BMap.Size(92, 92),
      textSize: '16',
      textColor: '#fff',
      borderRadius: 'true'
    }
  ]
});
markerClusterer.setMaxZoom(50);
markerClusterer.setGridSize(10);
```
画面14：
```javascript
client.query(query: GET_MAP_HOUSE).then(result =>
