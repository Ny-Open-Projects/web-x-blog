# 画面线理解：06.后台系统开发之楼盘、房源数据结构

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\06.后台系统开发之楼盘、房源数据结构【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:45, 01:10, 01:41, 02:17, 02:36, 02:51, 03:03, 03:15, 03:30, 03:52, 04:22, 04:54, 05:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:28:40

1) 这一组画面整体在讲一个房屋租赁管理系统的前端页面开发与后端数据结构设计，包括房源列表、新增房源表单、数据模型文档以及部分接口实现。

2) 按时间顺序列出每张画面的要点：
画面1：展示“好客租房-管理系统”的房源管理页面，包含房源列表、搜索和筛选功能。
画面2：展示“新增房源”的表单页面，包含楼盘名称、地址、租金、支付方式、户型、面积等输入项。
画面3：展示“楼盘数据 (estate)”和“房源数据 (houseResources)”的数据库字段定义，包括字段名、类型和备注。
画面4：继续展示“楼盘数据 (estate)”的字段定义，聚焦在“propertyCompany”字段。
画面5：继续展示“房源数据 (houseResources)”的字段定义，聚焦在“coveredArea”、“floor”、“orientation”等字段。
画面6：展示“编写页面”的说明，包含页面效果预览图，显示了左侧导航菜单和右侧表单区域。
画面7：展示前端代码，定义了estateMap对象，包含多个楼盘的名称和地址映射，并实现了handleSubmit方法。
画面8：展示前端代码，实现“楼盘名称”下拉选择框的onSelect事件，用于获取楼盘ID。
画面9：展示前端代码，实现“租金”和“支付方式”下拉选择框的代码。
画面10：展示前端代码，实现“看房时间”和“物业费”输入框的代码。
画面11：展示“好客租房后台V1.0.0 - Azure RP 8 Enterprise Edition”的合同管理页面，包含合同列表和搜索条件。
画面12：展示Google搜索页面，无具体内容。
画面13：展示“房源数据 (houseResources)”的字段定义，聚焦在“rentMethod”、“paymentMethod”、“houseType”等字段。
画面14：展示一个房屋租赁网站的房源详情页，包含价格、楼盘信息、联系人和在线咨询按钮。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面7：
```javascript
const estateMap = new Map([
  ['中远两湾城', '1001|上海市,上海市,普陀区,远景路97弄'],
  ['上海新城', '1002|上海市,上海市,闵行区,莘松路358弄'],
  ['保利西海岸', '1003|上海市,上海市,松江区,广富林路1188弄'],
  ['万科城花园', '1004|上海市,上海市,闵行区,七莘路3333弄2区-15区'],
  ['上海阳城', '1005|上海市,上海市,闵行区,罗锦路888弄']
]);

@connect(({ loading }) => ({
  submitting: loading.effects['form/submitRegularForm'],
}))
class AddResource extends PureComponent {
  handleSubmit = (dispatch, form) => this.props;
  e.preventDefault();
  form.validateFieldsAndScroll((err, values) => {
    if (err) {
      values.facilities = values.facilities.join(",");
    }
    if (values.floor_1 && values.floor_2) {
    }
  });
```

画面8：
```jsx
<Form onSubmit={this.handleSubmit} hideRequiredMark style={{ margin: '20px 0' }}>
  <FormItem {...formItemLayout} label="楼盘名称">
    <AutoComplete
      style={{ width: '100%' }}
      dataSource={this.state.estateDataSource}
      onSelect={(value, option) => {
        let v = estateMap.get(value);
        this.setState({
          estateAddress: v.substring(v.indexOf('|') + 1),
          estateId: v.substring(0, v.indexOf('|'))
        });
      }}
    />
  </FormItem>
  <FormItem {...formItemLayout} label="楼盘地址">
    <Input
      prefix={<Icon type="environment" style={{ color: 'red' }} />}
      value={this.state.estateAddress}
      defaultValue={this.state.estateAddress}
    />
  </FormItem>
</Form>
```

画面9：
```jsx
<Select style={{ width: '50%' }}>
  <Option value="1">一押</Option>
  <Option value="2">二押</Option>
  <Option value="3">三押</Option>
  <Option value="4">四押</Option>
  <Option value="5">其它</Option>
</Select>

<Select style={{ width: '50%' }}>
  <Option value="1">整租</Option>
  <Option value="2">合租</Option>
</Select>
```

画面10：
```jsx
<Select style={{ width: '20%' }}>
  <Option value="1">上午</Option>
  <Option value="2">中午</Option>
  <Option value="3">下午</Option>
  <Option value="4">晚上</Option>
  <Option value="5">全天</Option>
</Select>

<InputGroup compact>
  <Input style={{ width: '30%' }} addonAfter="元/平" />
</InputGroup>
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面3、4、5、13：展示“楼盘数据 (estate)”和“房源数据 (houseResources)”的字段定义表格，包含字段名、类型和备注。
画面6：展示“编写页面”的说明，包含页面效果预览图，显示了左侧导航菜单和右侧表单区域。
画面11：展示“合同管理”的页面，包含合同列表和搜索条件。

5) 无。
