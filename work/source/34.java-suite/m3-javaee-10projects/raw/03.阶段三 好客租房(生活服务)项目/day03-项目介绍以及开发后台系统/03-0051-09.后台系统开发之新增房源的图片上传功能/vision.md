# 画面线理解：09.后台系统开发之新增房源的图片上传功能

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\09.后台系统开发之新增房源的图片上传功能【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:31, 01:08, 01:36, 02:01, 02:23, 02:51, 05:22, 05:41, 06:17, 07:15, 07:41, 08:15, 09:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:31:17

1) 这一组画面整体在讲什么（一句话）：
讲解房屋信息发布页面中图片上传功能的实现，包括前端页面交互、Ant Design 组件使用、以及父组件与子组件间数据传递的机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程大纲，当前位于“2.2.2.4 图片上传”章节，页面中显示了图片上传的前端界面，包含“上传内容”区域和“Upload”按钮。
画面 2: 展示前端页面，用户通过文件选择器选择图片文件（如 1.jpg, 2.jpg 等），并点击“Upload”按钮上传。
画面 3: 展示上传成功后，图片显示在页面上，下方是表单字段，包括“联系人”、“手机号”、“看房时间”、“物业费”等，部分字段有红色提示“此项为必填项”。
画面 4: 展示前端页面代码，是 AddResource.js 文件中关于表单字段的 JSX 代码，包括联系人、手机号、看房时间、物业费等字段的定义，以及一个下拉选择框用于选择“看房时间”。
画面 5: 展示前端代码，是 PicturesWall.js 文件，定义了上传组件的 React 类，包含 state、handleCancel、handlePreview、handleChange 等方法，以及 render 方法中定义的上传按钮。
画面 6: 展示前端页面代码，是 AddResource.js 文件中关于“图片信息”部分的代码，包含“房源描述”文本域和“上传室内图”图片上传组件。
画面 7: 展示前端代码，是 PicturesWall.js 文件，高亮显示了 state 中的 previewVisible、previewImage、fileList 等属性。
画面 8: 展示前端页面代码，是 AddResource.js 文件中关于“图片信息”部分的代码，包含“房源描述”文本域和“上传室内图”图片上传组件。
画面 9: 展示前端页面代码，是 AddResource.js 文件中关于“配置设施”部分的代码，包含一个 CheckBoxGroup 组件，用于选择房屋的设施，如“水”、“暖气/天然气”、“有线电视”等。
画面 10: 展示前端页面代码，是 AddResource.js 文件中关于“图片信息”部分的代码，包含“房源描述”文本域和“上传室内图”图片上传组件。
画面 11: 展示前端页面代码，是 AddResource.js 文件中关于表单布局的代码，定义了 formItemLayout 和 submitFormLayout，用于控制表单字段的栅格布局。
画面 12: 展示前端页面，是房屋信息发布页面，显示了上传的图片和表单字段，包括“联系人”、“手机号”、“看房时间”、“物业费”等，部分字段有红色提示“此项为必填项”。
画面 13: 展示课程讲义，讲解父组件如何获取子组件中的数据，通过 this.props 传递数据，以及在子组件中通过 this.props.handleFileList(this.state.fileList) 传递数据。
画面 14: 展示课程讲义，讲解父组件如何获取子组件中的数据，通过 this.props 传递数据，以及在子组件中通过 this.props.handleFileList(this.state.fileList) 传递数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4 代码：
```jsx
<Card bordered={false} title="出借信息">
  <FormItem {...formItemLayout} label="联系人">
    {getFieldDecorator('contact', {
      rules: [{ required: true, message: '此项为必填项' }]
    })(
      <Input placeholder="请输入" />
    )}
  </FormItem>
  <FormItem {...formItemLayout} label="手机号">
    {getFieldDecorator('mobile', {
      rules: [{ required: true, maxLength: 11, message: '此项为必填项' }]
    })(
      <Input placeholder="请输入" maxLength="11" />
    )}
  </FormItem>
  <FormItem {...formItemLayout} label="看房时间">
    {getFieldDecorator('time', {
      initialValue: '1',
      rules: [{ required: true, message: '此项为必填项' }]
    })(
      <Select style={{ width: '20%' }}>
        <Option value="1">上午</Option>
        <Option value="2">中午</Option>
        <Option value="3">下午</Option>
      </Select>
    )}
  </FormItem>
</Card>
```

画面 5 代码：
```jsx
import { Upload, Icon, Modal } from 'antd';

class PictureWall extends React.Component {
  state = {
    previewVisible: false,
    previewImage: '',
    fileList: [],
  };

  handleCancel = () => this.setState({ previewVisible: false });

  handlePreview = (file) => {
    this.setState({
      previewImage: file.url || file.thumbUrl,
      previewVisible: true,
    });
  };

  handleChange = (fileList) => {
    this.setState({ fileList });
    this.props.handleFileList(this.state.fileList);
  };

  render() {
    const { previewVisible, previewImage, fileList } = this.state;
    const uploadButton = (
      <div>
        <Icon type="plus" />
        <div className="ant-upload-text">Upload</div>
      </div>
    );
    return (
      <div>
        {previewVisible && (
          <Modal
            visible={previewVisible}
            footer={null}
            onCancel={this.handleCancel}
          >
            <img alt="example" style={{ width: '100%' }} src={previewImage} />
          </Modal>
        )}
        <Upload
          action="/upload.do"
          listType="picture-card"
          fileList={fileList}
          onChange={this.handleChange}
          onPreview={this.handlePreview}
        >
          {fileList.length < 1 && !previewVisible && uploadButton}
        </Upload>
      </div>
    );
  }
}
```

画面 6 代码：
```jsx
<Card bordered={false} title="图片信息">
  <FormItem {...formItemLayout} label="房源描述">
    {getFieldDecorator('desc', {
      rules: [{ required: true, message: '此项为必填项' }]
    })(
      <TextArea placeholder="请输入备注信息" autosize={{ minRows: 4, maxRows: 10 }} />
    )}
  </FormItem>
  <FormItem {...formItemLayout} label="上传室内图">
    <PictureWall handleFileList={this.handleFileList.bind(this)} />
  </FormItem>
</Card>
```

画面 7 代码：
```jsx
import { Upload, Icon, Modal } from 'antd';

class PictureWall extends React.Component {
  state = {
    previewVisible: false,
    previewImage: '',
    fileList: [],
  };

  handleCancel = () => this.setState({ previewVisible: false });

  handlePreview = (file) => {
    this.setState({
      previewImage: file.url || file.thumbUrl,
      previewVisible: true,
    });
  };

  handleChange = (fileList) => {
    this.setState({ fileList });
    this.props.handleFileList(this.state.fileList);
  };

  render() {
    const { previewVisible, previewImage, fileList } = this.state;
    const uploadButton = (
      <div>
        <Icon type="plus" />
        <div className="ant-upload-text">Upload</div>
      </div>
    );
    return (
      <div>
        {previewVisible && (
          <Modal
            visible={previewVisible}
            footer={null}
            onCancel={this.handleCancel}
          >
            <img alt="example" style={{ width: '100%' }} src={previewImage} />
          </Modal>
        )}
        <Upload
          action="/upload.do"
          listType="picture-card"
          fileList={fileList}
          onChange={this.handleChange}
          onPreview={this.handlePreview}
        >
          {fileList.length < 1 && !previewVisible && uploadButton}
        </Upload>
      </div>
    );
  }
}
```

画面 9 代码：
```jsx
<FormItem {...formItemLayout} label="配置设施">
  {getFieldDecorator('facilities', {
    initialValue: ['1', '2', '3'],
    rules: [{ required: true, message: '此项为必填项' }]
  })(
    <CheckboxGroup options={[
      { label: '水', value: '1' },
      { label: '暖气/天然气', value: '2' },
      { label: '暖气', value: '3' },
      { label: '有线电视', value: '4' },
      { label: '宽带', value: '5' },
      { label: '电梯', value: '6' },
      { label: '车位/车库', value: '7' },
      { label: '地下室/储藏室', value: '8' },
      { label: '地下室/储藏室', value: '9' },
    ]}/>
  )}
</FormItem>
```

画面 10 代码：
```jsx
<Card bordered={false} title="图片信息">
  <FormItem {...formItemLayout} label="房源描述">
    {getFieldDecorator('desc', {
