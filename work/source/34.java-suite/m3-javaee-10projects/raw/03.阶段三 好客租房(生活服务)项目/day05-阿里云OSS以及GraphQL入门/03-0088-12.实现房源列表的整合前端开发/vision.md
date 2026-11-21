# 画面线理解：12.实现房源列表的整合前端开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\12.实现房源列表的整合前端开发【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:50, 01:57, 02:41, 03:37, 04:48, 05:36, 06:07, 06:37, 07:44, 08:26, 09:11, 09:43, 10:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:56:23

1) 这一组画面整体在讲如何在前端项目中整合并修改房源列表的展示与数据结构，包括使用 Ant Design 组件、实现图片轮播、修改数据请求地址和字段结构。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中“5.5.1、修改请求数据地址”章节，目录结构中高亮显示 `houseResource.js` 文件。
画面2：在 IntelliJ IDEA 中查看 `src/models/houseResource.js` 文件，代码中导入 `queryResource` 并导出默认模块，定义了 `state` 和 `effects`。
画面3：浏览器地址栏显示 `localhost:8000`，页面为 Google 搜索首页。
画面4：在 IntelliJ IDEA 中查看 `src/pages/haoke/Resource.js` 文件，代码中定义了表格列配置，包括“房源编号”、“房源信息”、“图”、“楼栋”、“支付方式”等。
画面5：在 Navicat Premium 中查看数据库表 `tb_house_resources`，显示了房源数据记录。
画面6：PDF 文档中展示 `columns = [ ... ]` 的代码片段，定义了表格列标题和数据索引。
画面7：浏览器中显示房源管理页面，列出了房源信息，包括房源编号、房源信息、图、楼栋、支付方式、户型、面积、楼层、操作等。
画面8：在 Ant Design 官网查看 Carousel 组件的属性和方法文档。
画面9：在 Ant Design 官网查看 Modal 组件的弹窗示例，弹窗中显示“这是通知消息”。
画面10：在 Ant Design 官网查看 Modal 组件的自定义弹窗示例，包含确认和取消按钮。
画面11：在 IntelliJ IDEA 中查看 `src/pages/haoke/ShowPics.js` 文件，代码中使用 `Modal.info` 和 `Carousel` 组件展示图片。
画面12：在 IntelliJ IDEA 中查看 `src/pages/haoke/ShowPics.js` 文件，代码中定义了 `constructor` 方法，初始化 `state`。
画面13：PDF 文档中展示 `columns = [ ... ]` 的代码片段，定义了表格列标题和数据索引。
画面14：PDF 文档中展示 `houseResource.js` 文件的目录结构，并显示了 `queryResource` 函数的代码，请求地址为 `/haoke/house/resources`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```javascript
import { queryResource } from '@/services/houseResource';
export default 'house_resource',
namespace: {
  data: {
    list: [],
    pagination: {},
  },
},
effects: {
  fetch({ payload }, { call, put }) {
    const response = yield call(queryResource, payload);
    yield put({
      type: 'save',
      payload: response,
    });
  },
},
reducers: {
```

画面4：
```javascript
title: '房源编号',
dataIndex: 'id',
},
{
  title: '房源信息',
  dataIndex: 'title',
},
{
  title: '图',
  dataIndex: 'pic',
  render: (text, record, index) => {
    return <ShowPics pics={text}/>
  },
},
{
  title: '楼栋',
  render: (text, record, index) => {
    return record.buildingFloorNum + "栋" + record.buildingNum + "单元" + record.buildingUnit + "号"
  },
},
{
  title: '支付方式',
```

画面5：
```sql
tb_house_resources (haoke)
```

画面11：
```javascript
class ShowPics extends React.Component{
  info () -> {
    Modal.info({
      title: '',
      iconType: 'false',
      width: '800px',
      okText: "ok",
      content: (
        <div style={{width:650, height: 400, lineHeight:400, textAlign:"center"}}>
          <Carousel autoplay={true}>
            {this.props.pics.split(',').map((value, index) => {
              return <div><img style={{ maxWidth:600, maxHeight:400, margin:"0 auto" }} src={value}/></div>
            })}
          </Carousel>
        </div>
      ),
      onOk() {},
    });
  },
```

画面12：
```javascript
constructor(props){
  super(props);
  this.state = {
    btnDisabled: this.props.pics? false: true
  }
}
```

画面14：
```javascript
import request from '@/utils/request';
import { stringify } from 'qs';
export async function queryResource([param] {
  return request(`/haoke/house/resources?${stringify(params)}`);
})
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：PDF 文档标题为“5.5.1、修改请求数据地址”。
画面6：PDF 文档中展示 `columns = [ ... ]` 的代码片段。
画面13：PDF 文档中展示 `columns = [ ... ]` 的代码片段。
画面14：PDF 文档中展示 `houseResource.js` 文件的目录结构，并显示了 `queryResource` 函数的代码。

5) 无。
