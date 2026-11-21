# 画面线理解：07.后台系统开发之form表单组件以及表单提交的讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\07.后台系统开发之form表单组件以及表单提交的讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:32, 02:56, 04:06, 05:00, 06:39, 08:04, 08:55, 09:44, 10:24, 11:18, 12:17, 13:10, 13:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:29:35

1) 这一组画面整体在讲什么（一句话）：
讲解 Ant Design 的 Form 组件在 React 项目中的使用，包括表单域的结构、验证状态、自定义表单以及与 Redux 的集成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Ant Design 官网的 Form 组件文档，介绍表单的两种排列方式（水平排列、垂直排列、行内排列）和表单域的组成。
画面 2: 展示 Form 组件的验证状态示例，包括成功、警告、失败和错误状态，以及日期选择器的验证。
画面 3: 展示 Form.create() 包装组件后提供的 API，包括 getFieldDecorator、getFieldError、getFieldValue、isFieldsTouched、isFieldValidating 等方法。
画面 4: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中使用了 Form.Item 和 Input 组件，并通过 getFieldDecorator 进行表单字段的装饰。
画面 5: 展示 Form.create() 的 API 文档，包括 mapPropsToFields、validatMessages、onFieldsChange、onValuesChange 等方法。
画面 6: 展示 Typora 中的 markdown 文档，内容是关于 getFieldDecorator 的使用说明，包括其特性、注意事项和相关 GitHub 链接。
画面 7: 浏览器地址栏显示正在访问 GitHub 上的 async-validator-type 仓库。
画面 8: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中使用了 Select 组件和 getFieldDecorator 进行表单字段的装饰。
画面 9: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中定义了 formItemLayout 和 submitFormLayout 的样式配置。
画面 10: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中定义了 handleSearch 函数，用于处理搜索逻辑。
画面 11: 展示 Word 文档中的表格，列出了房源信息的字段，包括 id、name、province、city、area、address、year、type、propertyCost、propertyCompany、developers、created、updated。
画面 12: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中处理了 facilities 和 floor 字段的值，并在提交前进行拼接和清理。
画面 13: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中处理了 houseType 字段的值，并在提交前进行拼接和清理。
画面 14: 在 IntelliJ IDEA 中展示 AddResource.js 文件，代码中处理了 houseType 字段的值，并在提交前进行拼接和清理。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```jsx
<Form.Item {...props}>
  {children}
</Form.Item>
```

画面 2:
```jsx
Validating: I'm the content is being validated!
Success: I'm the content
Warning: Warning
Fail: unavailable codes
Should be combination of numbers & alphabets
Success: 请选择日期
Warning: 请选择时间
Error: Option 1
Validating: The information is being validated...
Success: 请选择日期
```

画面 3:
```jsx
const EnhancedForm = Form.create()(CustomizedForm);
this.form // => The instance of CustomizedForm
```

画面 4:
```jsx
this.setState({
  estateAddress: v.substring(v.indexOf('') + 1),
  estateId: v.substring(0, v.indexOf(''))
})
onSearch={(this.handleSearch)
filterOption=(inputValue, option) => option.props.children.to
<Form.Item {...formItemLayout} label="楼盘地址">
  <Input
    prefix={<Icon type="environment" style={{ color: 'rgba(0,0,0,25%)' }} />}
    value={this.state.estateAddress}
    defaultValue={this.state.estateAddress}
  />
</Form.Item>
<Form.Item {...formItemLayout} label="楼栋">
  <InputGroup>
    {getFieldDecorator('buildingNum', {rules: [{ required: true, message: '楼栋号必填' }]})(
      <Input />
    )}
    {getFieldDecorator('buildingFloorNum', {rules: [{ required: true, message: '楼层号必填' }]})(
      <Input />
    )}
  </InputGroup>
</Form.Item>
<Form.Item {...formItemLayout} label="租金">
  <Form.Item compact>
    {getFieldDecorator('rent', {rules: [{ required: true, message: '此项为必填项' }]})(
      <Input />
    )}
  </Form.Item>
</Form.Item>
<Form.Item {...formItemLayout} label="支付方式">
  {getFieldDecorator('paymentMethod', {initialValue: '1', rules: [{ required: true, message: '此项为必填项' }]})(
    <Select style={{ width: '100%' }}>
      <Option value="1">付一押一</Option>
      <Option value="2">付三押一</Option>
      <Option value="3">付六押一</Option>
      <Option value="4">年付押一</Option>
      <Option value="5">其它</Option>
    </Select>
  )}
</Form.Item>
```

画面 5:
```jsx
mapPropsToFields
validatMessages
onFieldsChange
onValuesChange
```

画面 6:
```jsx
{getFieldDecorator('paymentMethod', {initialValue: '1', rules: [{ required: true, message: '此项为必填项' }]})(
  <Select style={{ width: '100%' }}>
    <Option value="1">付一押一</Option>
    <Option value="2">付三押一</Option>
    <Option value="3">付六押一</Option>
    <Option value="4">年付押一</Option>
    <Option value="5">其它</Option>
  </Select>
)}
```

画面 8:
```jsx
<Select style={{ width: '100%' }}>
  <Option value="1">付一押一</Option>
  <Option value="2">付三押一</Option>
  <Option value="3">付六押一</Option>
  <Option value="4">年付押一</Option>
  <Option value="5">其它</Option>
</Select>
```

画面 9:
```jsx
const formItemLayout = {
  labelCol: {
    xs: { span: 24 },
    sm: { span: 7 },
  },
  wrapperCol: {
    xs: { span: 24 },
    sm: { span: 12 },
    md: { span: 10 },
  },
};
const submitFormLayout = {
  wrapperCol: {
    xs: { span: 24, offset: 0 },
    sm: { span: 10, offset: 7 },
  },
};
```

画面 10:
```jsx
dispatch({
  type: 'form/submitRegularForm',
  payload: values,
});
handleSearch = (value) => {
  let arr = new Array();
  if(value.length > 0) {
    estateList.forEach((y, k) => {
      if(y.startsWith(value)) {
        arr.push(k);
      }
    });
  }
};
```

画面 11:
```markdown
| id | Long | 楼盘id |
| --- | --- | --- |
| name | String | 楼盘名称 |
| province | String | 所在省 |
| city | String | 所在市 |
| area | String | 所在区 |
| address | String | 具体地址 |
| year | String | 建筑年代 |
| type | String | 建筑类型 |
| propertyCost | String | 物业费 |
| propertyCompany | String | 物业公司 |
| developers | String | 开发商 |
| created | datetime | 创建时间 |
| updated | datetime | 更新时间 |
```

画面 12:
```jsx
e.preventDefault();
console.log(this.state.fileList);
form.validateFieldsAndScroll((err, values) => {
  if (err) {
    if (values.facilities) {
      values.facilities = values.facilities.join(",");
    }
    if (values.floor_1 && values.floor_2) {
      values.floor = values.floor_1 + "/" + values.floor_2;
    }
  }
  values.houseType = values.houseType_3 + "室" + values.houseType_2 + "厅" + values.houseType_4 + "阳台";
  delete values.floor_1;
  delete values.floor_2;
  delete values.houseType_1;
  delete values.houseType_2;
  delete values.houseType_3;
  delete values.houseType_4;
  delete values.houseType_5;
  dispatch({
    type: 'form/submitRegularForm',
    payload: values,
  });
});
```

画面 13:
```jsx
values.houseType = values.houseType_3 + "室" + values.houseType_2 + "厅" + values.houseType_4 + "阳台";
delete values.floor_1;
delete values.floor_2;
delete values.houseType_1;
delete values.houseType_2;
delete values.houseType_3;
delete values.houseType_4;
delete values.houseType_5;
```

画面 14
