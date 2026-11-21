# 17.地图找房功能实现之改造静态数据为动态加载（GraphQL服务实现）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\17.地图找房功能实现之改造静态数据为动态加载（GraphQL服务实现）【海量资源尽在 ubkz.com】.mp4
- 时长 11分38秒（音频 699s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就把他前面的静态的数据的这个逻辑我们改造一下改造成我们去呃加载我们后台的一个这种方式啊去做一个这样的一个改造那么呃我们先来去呃开发我们后台数据的一个接口那么我们依然呢通过这个GrabQL这样的方式去做一个加载那么我们先写后台的接口然后再去改造前端的这样的一个逻辑啊那我们先来看一下我们的
[00:29] 这个接口那么首先我们还是需要进入到我们后台系统然后在我们的这个里面就是API Server这个下面我们找到它下面有一个GrabQr的一个这样的一个文件就它然后我们需要给它添加一个查询我们来看一下这个跟我们讲义就保持一致我们添加一个叫MapHost然后Data然后它的类型是叫做MapHost
[00:58] 然后DataResult这样的一种类型那么把它加到这来那么下面我们是不是就需要做这样的一个定义加一个type这样的一个定义OK然后在它下面其实有一个定义我们来看一下定义什么样的数据结构其实我们要定义的是一个list为什么是个list那么又要回到我们前端系统所要求的一个结构那么在我们前端系统中
[01:27] 他所要求的一个结构就是这样的一个宿主这个结构对不对所以说我们在我们的后端这个位置给他定义的时候呢我们是一个list那么list它是一个什么样的类型呢我们又要去给他定义一个对象那么我们定义一个叫mapmaphost x y那么也就是他的一个坐标那么为什么定义他呢还是要去看前台在前端这个系统是不是要求到我们的需要的数据是xy就是我们的一个
[01:57] 这个房源数据它的一个精纬度的这样的一个坐标那么用XY做一个表示好那么我们把它的这个后面的一个定义我们拿过来然后呢是在下面这个位置呢有一个叫做map host XY坐标这样的一个定义那么它有两个啊一个是X一个是Y它的所对应的类型呢都是float啊这种类型那么就是我们的一个小数啊这样的一个类型
[02:24] 好嘞那么这个我们是不是就搞定了那么接下来呢我们就需要进入到我们的这个查询这个里面GrabQR下面有一个有一个这个DataFetcher是不是需要它那么我们需要再去写一个它那么怎么样去写呢我们先考下这个类的名字吧我们需要去写一个它那么先把它呢先拿过来好那么我们先去实现一个先写一个它
[02:54] 然后呢他们要去实现我们自己写的这个接口对吧那么我们让他去实现一个接口叫mydatafetcher然后呢我们需要实现有两个方法对吧OK那么然后呢我们需要给他先添加一个注解添加一个注解那就叫什么呢component是不是加到我们的spin的容器就可以了那么fill的name就是我们查询的名字
[03:22] 那么查询的名字呢刚刚我们是不是给他已经定义好了那就是上面对应的对应的他对吧哎把他靠过来呃然后呢放到这然后下面这个就是做我们数据的一个查询那么我们的数据最终所返回的一个类型是叫就叫这个map host data result所以我们需要给他定义啊这两个的一个类型那我们来看一下我们的讲义中的这两个呃对象的一个定义
[03:51] 那么我们需要在这儿在VO这个下面给他创建一个包就叫map这个包那么在map包这个下面我们需要创建两个对象那么第一个是这个result这个对象把它就call过来了然后往这一callok然后这个就搞定但是他还缺一个对象那么XY这个对象把这个XY这个对象也call过来往这一call好这样的话是不是就OK了
[04:21] 好那么我们现在已经参考我们刚刚的这个GrabQL文件中的一个定义我们已经定义好了这两个这个对象那么现在呢我们只需要在我们这个Data Feature这个里面去实现我们的这个查询是不是就可以了当然我们是不是这个里面的这个数据可以先按照我们前端的这个数据呢去做一个这个返回因为我们先把它改成通过加载的方式去做一个这样的一个
[04:51] 加载ok好嘞那么我们来看一下这个里面应该怎么去写我们是不是应该这么去写那么最终返回的其实是我们拗一个叫做map resultmap host然后result这个对象然后传递一个listlist是谁我们就需要定一个list他的所需要存放的是map host然后 xy list
[05:19] 等于new一个reve list好那么把这个list传递给他传递给他ok那么下面我们只需要给他去构造数据就可以了那么我们找到我们的讲义我们把这个给他去拷贝一下这个我们就不写了这个数据这个数据跟我们前端数据是一模一样的只是说我们把它改造成后端的形式去做一个数据的返回那么ok
[05:46] 好那么到这里呢我们是不是已经提供了这样的一个服务啊那么我们把这个服务呢做一个重启那我们接下来来测试一下这个服务是否是OK呢好那么现在呢我们这个服务呢就重新启动起来了那么启动起来呢我们就来测试一下啊打开我们的这个测试工具我们来测一下啊那么我们就新建一个吧新建一个这个测试那么我们的一个这个测试应该怎么去写呢我们来看一下
[06:13] 那么我们去参考我们这样的一个查询对吧那么应该怎么写呢是不是我们应该这样来写那么在这个位置呢我们给他添加一个是不是就是括号然后呢我们要查询的内容呢就是我们这个里面所定义的他对吧然后呢拷贝一下然后我们要查询的他里面的什么呢是不是就是这个下面的list那么list里面的什么内容呢是不是就是x和y
[06:42] 是不是就这样去写啊好那么我们来执行一下走好那么现在我们是不是就已经查到数据了那就说明到目前为止的我们是不是在我们的服务端给他返回的一个数据就搞定了那么接下来呢我们就需要在我们的前端这个系统把这个测试数据啊给他改造成我们去查询的方式那么怎么样查询呢我们依然是参考我们的讲义啊那么在讲义中呢我们还是去
[07:10] 引入我们这个Apollo这样的一个API对吧去做一个查询那么把它拷过来拷到这个位置先导入进来导入进来之后呢我们先给它定义我们的一个client客户端就是Apollo client那么它这个地址是不是指向的就是我们这个GrabQL这个地址然后呢下面的我们还是需要给它去定义一个这个query查询这个query来定义过来
[07:41] 定义到这OK那么这个呢就是我们的一个这个查询那么下面呢我们就需要去修改一下我们这个代码逻辑那么怎么样查询呢我们来看一下啊查询呢我们就需要这么来玩那么我们把这个代码拷过来这个这个拷贝到哪里呢拷贝到这定义完成我们这个map就是我们那个摆入地图之后啊然后呢我们在这个位置
[08:10] 去给他去做这样的一个设置那么这个是不是就是我们数据加载完要去执行的一个逻辑对吧到这就是我们的数据加载加载完成加载完成了去走这个位置走这个位置那么走这个怎么玩呢就是我们这个XY其实是已经是这个就不需要了对吧然后我们把下面这个代码把下面这个代码那么我们都减7然后给它移到这个位置来
[08:40] 移到这个位置那么移到这个位置之后我们就可以去编写它这里面的内容那么在我们代码中它所需要的是一个 x y就是我们的一个数组我们给它定义一个这个叫 x y s它等于我们这个 result点什么来看一下dateresult下面是不是有一个date下面有一个叫map host date点list
[09:10] 那么点list拿到了是不是就是一个数组那么其实就是我们这个XYS这个数组那么咱们把它去调一下XYSXYSXYSOK这样的话对它做一个循环便利那么我们在这呢把这几个变量给它去去调整一下最好不要使用这个Y对吧改成这个letOK然后呢我们来看一下这个也设置成这个letY
[09:41] 这个是地图上面的一个这个覆盖物然后呢我们给它去做一个这个调整一个设置然后呢我们来看一下在这个里面呢我们需要调整一个值呢是这个值啊这个把它调整50就是这个值什么意思呢就是我们那个覆盖物它所对应的那个一个那个叫小格的一个大小把它调大一点我们就是把地图放大的时候可以看到更多的那个覆盖物啊是这样的一个意思
[10:10] 好的我们来测试一下吧看他能不能够去按照我们的期望啊就是在我们页面加载完成之后呢去加载我们这个数据那么去不要使用这种静态的数据啊就实现这样的一个效果啊那么还是呢回到我们前端的这个页面中我们来刷新一下看效果啊然后呢点击这个地图导房走OK那么是不是可以看到哎有这样的一个效果啊那么我们来看他有没有去查询我们的数据呢来看一下你看
[10:41] 数据是不是已经查到了对吧查到我们这个数据虽然数据都是一样的但是它已经改成从我们后端是不是去做一个数据的一个加载那么我们把这个放大一点那你可以看到放大之后是不是就会有更多的这个圆圈的这个效果刚刚没有这个效果因为它最开始所设置的这个
[11:00] 这个小格子通过我们把这个小格就是它所划分的小格调大之后它就可以更多的显示这样的一个圆圈的一个效果就是聚合物这样的一个效果那么OK可以看到这样的一个效果了好那么现在我们其实已经就走出了第一步
[11:20] 就是已经把静态数据是不是已经改成我们去后台去加载这样的一个这种效果对吧那么后面呢我们只需要去去加载我们真实的一些这种数据是不是就OK了好嘞那么我们关于我们这个改造我们的一个静态数据的一个加载我们就讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 GraphQL 查询动态数据，并在前端 React 页面上使用百度地图 API 展示这些数据点，同时使用 MarkerClusterer 实现地图上点的聚合效果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中“5.2.1、修改数据的加载逻辑”章节，图示目录结构中高亮显示 `maphouse.js` 文件，文字说明“可以看到，目前的数据是静态的，需要改成加载后台数据的方式”。
画面2：展示 PDF 文档中定义的 TypeScript 接口 `type HaookeQuery` 和 `type HouseResources`。
画面3：展示 PDF 文档中定义的 TypeScript 接口 `type IndexAdResult`、`type IndexAdResultData` 和 `type MapHouseXY`。
画面4：展示 PDF 文档中定义的 Java 类 `MapHouseDataFetcher` 的部分代码，包含 `@Override` 注解和 `dataFetcher` 方法。
画面5：展示 IntelliJ IDEA 中的项目结构和 GraphQL 查询文件 `HouseResourcesDataFetcher.java`，其中包含 `type TableResult`、`type Pagination`、`type IndexAdResult` 和 `type IndexAdResultData` 的定义。
画面6：展示 IntelliJ IDEA 中的项目结构和 `maphouse.js` 文件，其中包含 `import React from 'React';`、`import { Icon } from 'semantic-ui-React';`、`import ApolloClient from 'apollo-boost';` 和 `import gql from 'GraphQL';` 的导入语句。
画面7：展示 IntelliJ IDEA 中的 `MapHouseDataFetcher` 类代码，包含 `@Override` 注解和 `dataFetcher` 方法。
画面8：展示 Altair GraphQL Client 界面，URL 为 `http://127.0.0.1:8000/GraphQL`，提示“Welcome to Altair GraphQL Client”。
画面9：展示 IntelliJ IDEA 中的 `maphouse.js` 文件，包含 `import React from 'React';`、`import { Icon } from 'semantic-ui-React';`、`import ApolloClient from 'apollo-boost';` 和 `import gql from 'GraphQL';` 的导入语句。
画面10：展示 PDF 文档中 `maphouse.js` 文件的代码，包含 `client.query(query: GET_MAP_HOUSE).then(result => {`、`var markers = [];`、`var pt = null;` 和 `for (var i in xys) {` 等语句。
画面11：展示 IntelliJ IDEA 中的 `maphouse.js` 文件，包含 `let pt = null;`、`for (let i in xys) {`、`pt = new BMap.Point(xys[i].x, xys[i].y);` 和 `markers.push(new BMap.Marker(pt));` 等语句。
画面12：展示 IntelliJ IDEA 中的 `maphouse.js` 文件，包含 `let pt = null;`、`for (let i in xys) {`、`pt = new BMap.Point(xys[i].x, xys[i].y);` 和 `markers.push(new BMap.Marker(pt));` 等语句。
画面13：展示浏览器中百度地图页面，显示“地图找房”，地图上有两个绿色圆圈标记，右侧是 Chrome 开发者工具的 Network 标签页，显示请求 URL 为 `http://127.0.0.1:8000/GraphQL`。
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
```GraphQL
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
import React from 'React';
import { Icon } from 'semantic-ui-React';
import ApolloClient from 'apollo-boost';
import gql from 'GraphQL';
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
import React from 'React';
import { Icon } from 'semantic-ui-React';
import ApolloClient from 'apollo-boost';
import gql from 'GraphQL';

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

