# 画面线理解：07.更新房源的交互页面实现讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\07.更新房源的交互页面实现讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 02:02, 03:06, 03:41, 05:55, 06:37, 07:49, 08:45, 09:33, 10:37, 11:37, 12:36, 13:44, 15:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:22:33

1) 这一组画面整体在讲如何在 React 项目中实现房源信息的编辑功能，包括前端界面、状态管理、表单验证和图片上传处理。

2) 按时间顺序列出每张画面的要点：
画面1：展示房源管理页面，包含房源列表和编辑、删除操作按钮。
画面2：在 IntelliJ IDEA 中打开 EditResource.js 文件，正在编写组件的 render 方法。
画面3：在 Resource.js 文件中，定义了 handleFormReset 函数，用于重置表单状态并触发数据获取。
画面4：在 Resource.js 文件中，定义了列的渲染函数，包括“面积”、“楼层”和“操作”列。
画面5：在 Adobe Reader 中查看 PDF 文档，内容涉及 React 表单和装饰器的使用。
画面6：在 EditResource.js 文件中，编写了 showModal 函数和 Modal 组件的结构。
画面7：在 EditResource.js 文件中，定义了组件的 state 和 showModal 函数。
画面8：在浏览器开发者工具中，显示了 ReferenceError: getFieldDecorator is not defined 的错误信息。
画面9：在 EditResource.js 文件中，定义了 FormItem 组件的属性，包括 label 和 rules。
画面10：在浏览器中，显示了房源编辑弹窗，包含房源标题、租金、建筑面积和图片上传区域。
画面11：在 EditResource.js 文件中，编写了 handleFileList 函数，用于处理上传的图片。
画面12：在 PicturesWall.js 文件中，定义了 handleCancel、handlePreview 和 handleChange 函数。
画面13：在 EditResource.js 文件中，编写了 handleSave 函数，用于保存表单数据。
画面14：在 Adobe Reader 中查看 PDF 文档，内容涉及 EditResource.js 文件中的 state 和函数定义。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```javascript
import React from 'react';
class EditResource extends React.Component{
  render() {
    return (
      <div>
        <a onClick={() => this.props.reload()}>刷新</a>
      </div>
    );
  }
}
```

画面3：
```javascript
type: 'rule/fetch',
payload: params,
});
handleFormReset () => {
  const { form, dispatch } = this.props;
  form.resetFields();
  this.setState({
    formValues: {},
  });
  dispatch({
    type: 'rule/fetch',
    payload: [],
  });
};
```

画面4：
```javascript
title: '面积',
dataIndex: 'useArea',
render: (text, record, index) => {
  return text + "平方"
},
title: '楼层',
dataIndex: 'floor'
,
title: '操作',
render: (text, record) => (
  <Fragment>
    <a onClick={() => {}}>查看</a>
    <Divider type="vertical" />
    <a href="">删除</a>
  </Fragment>
);
```

画面5：
```javascript
<React.Fragment>
  <a onClick={() => { this.showModal() }}>编辑</a>
  <Modal
    title="编辑"
    width={640}
    visible={this.state.visible}
    onOk={() => this.handleSave()}
    onCancel={() => this.handleCancel()}
    destroyOnClose={true}
  >
    <div style={{ overflowY: 'auto' }}>
      <Form hideRequiredMark style={{ marginTop: 8 }}>
        <FormItem {...formItemLayout} label="房源标题">
          {getFieldDecorator('title', {
            initialValue: record.title,
            rules: [{
              required: true,
              message: '房源标题为必填项'
            }]
          })(<Input style={{ width: '100%' }} />)}
        </FormItem>
        <FormItem {...formItemLayout} label="租金">
          {getFieldDecorator('rent', {
            initialValue: record.rent,
            rules: [{
              required: true,
              message: '租金为必填项'
            }]
          })(<InputNumber style={{ width: '100%' }} />)}
        </FormItem>
      </Form>
    </div>
  </Modal>
</React.Fragment>
```

画面6：
```javascript
import React from 'react';
class EditResource extends React.Component{
  showModal = () => {
    this.setState({
      visible: true
    });
  };
  render() {
    return (
      <React.Fragment>
        <a onClick={() => this.showModal()}>编辑</a>
        <Modal
          title="编辑"
          width={640}
          visible={this.state.visible}
          onOk={() => this.handleSave()}
          onCancel={() => this.handleCancel()}
          destroyOnClose={true}
        >
          <div style={{ overflowY: 'auto' }}>
```

画面7：
```javascript
super(props);
this.state = {
  visible: false,
  pics: new Set()
};
showModal = () => {
  this.setState({
    visible: true
  });
};
render() {
  return (
    <React.Fragment>
      <a onClick={() => this.showModal()}>编辑</a>
      <Modal
        title="编辑"
        width={640}
        visible={this.state.visible}
        onOk={() => this.handleSave()}
        onCancel={() => this.handleCancel()}
        destroyOnClose={true}
      >
        <div style={{ overflowY: 'auto' }}>
```

画面8：
```javascript
ReferenceError: getFieldDecorator is not defined
```

画面9：
```javascript
<FormItem {...formItemLayout} label="房源标题">
  {getFieldDecorator('title', {
    initialValue: record.title,
    rules: [{
      required: true,
      message: '房源标题为必填项'
    }]
  })(<Input style={{ width: '100%' }} />)}
</FormItem>
<FormItem {...formItemLayout} label="租金">
  {getFieldDecorator('rent', {
    initialValue: record.rent,
    rules: [{
      required: true,
      message: '租金为必填项'
    }]
  })(<InputNumber style={{ width: '100%' }} />)}
</FormItem>
```

画面10：
```html
房源标题：最新修改房源
租金：1000 元/月
建筑面积：100 平米
上传室内图：
[图片预览]
[上传按钮]
```

画面11：
```javascript
handleFileList = (obj) => {
  let pics = new Set();
  obj.forEach((v, k) => {
    if (v.response) {
      pics.add(v.response.name);
    }
    if (v.url) {
      pics.add(v.url);
    }
  });
  this.setState({
    pics: pics
  });
};
```

画面12：
```javascript
this.state = {
  previewVisible: false,
  previewImage: '',
  fileList: filelist
};
handleCancel = (file) => {
  this.setState({
    previewImage: file.url || file.thumbUrl,
    previewVisible: true,
  });
};
handleChange = (fileList) => {
```

画面13：
```javascript
handleSave = () => {
  const { dispatch, form, record } = this.props;
  form.validateFieldsAndScroll((err, values) => {
    if (err) {
      if (this.state.pics.size > 0) {
        values.pic = [...this.state.pics].join(',');
      }
      values.id = record.id;
      dispatch({
        type: 'house/updateHouseForm',
        payload: values,
      });
      setTimeout(() => {
        this.handleCancel();
      }, 500);
    }
  });
};
```

画面14：
```javascript
pics: new Set()
showModal = () => {
  this.setState({
    visible: true
  });
};
handleCancel = () => {
  this.setState({
    visible: false,
  });
};
handleSave = () => {
  const { dispatch, form, record } = this.props;
  form.validateFieldsAndScroll((err, values) => {
    if (err) {
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面5：
PPT标题：React 表单和装饰器的使用
表格数据：
- 2.1. 表单中传递参数
- 2.2. 设置参数
- 2.3. 设置默认值
- 2.4. 测试
- 3. 公共类装饰器
- 3.1. 修饰器的使用
- 3.2. 修饰器的使用
- 3.3. 测试
- 4. 实现数据存储
- 4.1. 新增接口（REST）
- 4.2. 修改接口
- 4.3. 删除接口
- 4.4. 修改接口
- 4.5. 修改接口
- 5. 为接口添加请求方法
- 5.1. 使用 Decorator
- 5.2. 使用 Axios
- 5.3. 使用 Axios
- 5.4. 导入数据
- 5.5. 导入数据

画面14：
PPT标题：EditResource.js 文件中的 state 和函数定义
表格数据：
- 1. state: { visible: false, pics: new Set() }
- 2. showModal = () => { this.setState({ visible: true }) }
- 3. handleCancel = () => { this.setState({ visible: false }) }
- 4
