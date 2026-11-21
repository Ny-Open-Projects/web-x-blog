# 画面线理解：09.整合前后端进行图片上传开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\09.整合前后端进行图片上传开发【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:59, 01:19, 01:52, 02:27, 03:02, 03:37, 04:28, 05:17, 06:04, 07:22, 08:43, 09:07, 09:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:54:22

1) 这一组画面整体在讲什么（一句话）：
演示一个房产资源管理系统的前端图片上传功能实现，包括前端代码编写、后端接口测试、数据库记录同步等环节。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：前端代码文件 ShowPics.js 中定义了图片展示按钮，包含 disabled 属性和 icon 属性，文件导出为 default。
画面2：前端代码文件 AddResource.js 中导入了 PicturesWall 组件，并定义了 FormItem、Option、RangePicker、TextArea、Search、InputGroup、CheckboxGroup 等常量，以及 estateMap 映射表，包含多个房产地址信息。
画面3：前端代码文件 PicturesWall.js 中定义了上传组件，包含 action、listType、fileList、onPreview、onChange 等属性，以及一个 Modal 弹窗用于预览图片。
画面4：配置文件 config.js 中定义了主题、外部依赖、代理目标地址（http://127.0.0.1:18080）、忽略时区、Less 加载选项、JavaScript 启用、CSS 加载选项、模块配置和本地资源路径处理逻辑。
画面5：使用 Advanced REST Client 工具向 http://127.0.0.1:18080/pic/upload 发送 POST 请求，上传文件 4.jpg，返回状态码 200。
画面6：在浏览器中访问 http://localhost:8000/house/addResource 页面，显示上传图片的界面，网络面板显示上传请求成功。
画面7：在浏览器中访问 http://localhost:8000/house/addResource 页面，显示上传图片的界面，网络面板显示上传请求成功，响应数据包含图片 URL。
画面8：前端代码文件 PicturesWall.js 中定义了 handleCancel、handlePreview、handleChange 方法，以及 render 函数，用于处理上传和预览逻辑。
画面9：前端代码文件 AddResource.js 中定义了组件构造函数，初始化 state 包含 estateDataSource、estateAddress、estateId、pics 等属性。
画面10：在 Navicat Premium 中查看 tb_house_resources 表，显示房产资源数据，包含 title、estate_id、building_num、building_floor_num、rent、payment_method、house_type、covered_area 等字段。
画面11：在浏览器中访问 http://localhost:8000/house/addResource 页面，填写房产信息，包括楼盘名称、楼盘地址、房源标题等。
画面12：在 Navicat Premium 中查看 tb_house_resources 表，显示房产资源数据，包含 building_unit、building_floor_num、rent、payment_method、house_type、covered_area、use_area、floor、orientation、decorate 等字段。
画面13：在 PDF 文档中查看“4.2. 修改AddResource.js”章节，描述了修改图片上传完成后的变更方法，包括使用 Set 集合存储图片名称。
画面14：在浏览器中访问 http://localhost:8000/house/addResource 页面，填写房产信息，包括楼层、租金、支付方式、户型、建筑面积等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```javascript
<Button disabled={this.state.btnDisabled} icon="picture" shape="c"
</div>
export default ShowPics;
```

画面2：
```javascript
import PicturesWall from '../Utils/PicturesWall';

const FormItem = Form.Item;
const { Option } = Select;
const { RangePicker } = DatePicker;
const TextArea = Input.Search;
const InputGroup = Input.Group;
const CheckboxGroup = Input.Group;

const estateMap = new Map([
  ['中远两湾城', '1001|上海市,上海市,普陀区,景凌路97弄'],
  ['上海绿城', '1002|上海市,上海市,闵行区,莘松路958弄'],
  ['保利西子湾', '1003|上海市,上海市,松江区,广富林路1188弄'],
  ['万科城市花园', '1004|上海市,上海市,闵行区,七莘路3333弄2区-15区'],
  ['上海阳城', '1005|上海市,上海市,闵行区,罗韵路888弄']
]);

@connect({ loading } -> {
  submitting: loading.effects['form/submitRegularForm'],
})
```

画面3：
```javascript
const { previewVisible, previewImage, fileList } - this.state;
const uploadButton = (
  <div>
    <Icon type="plus" />
    <div className="ant-upload-text">Upload</div>
  </div>
);
return (
  <Upload
    action="/haoke/pic/upload"
    listType="picture-card"
    fileList={fileList}
    onPreview={this.handlePreview}
    onChange={this.handleChange}
  >
    {fileList.length >= 5 ? null : uploadButton}
  </Upload>
  <Modal visible={previewVisible} footer={null} onCancel={this.handleCancel}>
    <img alt="example" style={{ width: '100%' }} src={previewImage} />
  </Modal>
</div>
```

画面4：
```javascript
theme: {
  'primary-color': defaultSettings.primaryColor,
},
externals: {
  '@antv/data-set': 'DataSet',
},
proxy: {
  '/haoke': {
    'target': 'http://127.0.0.1:18080',
    'changeOrigin': true,
    'pathRewrite': {'^/haoke': ''}
  }
},
ignoreMomentLocale: true,
lessLoaderOptions: {
  javascriptEnabled: true,
},
disableRedirectHoist: true,
cssLoaderOptions: {
  modules: true,
  getLocalIdent: (context, localIdentName, localName) => {
    if (context.resourcePath.includes('node_modules')) ||
    ...
  }
}
```

画面5：
```http
POST http://127.0.0.1:18080/pic/upload
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrCesTK
```

画面6：
```javascript
// 网络面板显示
upload
200 OK
```

画面7：
```javascript
// 网络面板显示
upload
200 OK
```

画面8：
```javascript
handleCancel - () -> this.setState({ previewVisible: false })
handlePreview - (file) -> {
  this.setState({
    previewImage: file.url || file.thumbUrl,
    previewVisible: true,
  });
}
handleChange = ({ fileList }) => {
  this.setState({ fileList });
  this.props.handleFileList(this.state.fileList);
}
render() {
  const { previewVisible, previewImage, fileList } - this.state;
  const uploadButton = (
    <div>
      <Icon type="plus" />
      <div className="ant-upload-text">Upload</div>
    </div>
  );
  return (
    <Upload
      action="/haoke/pic/upload"
      listType="picture-card"
      fileList={fileList}
      onPreview={this.handlePreview}
      onChange={this.handleChange}
    >
      {fileList.length >= 5 ? null : uploadButton}
    </Upload>
    <Modal visible={previewVisible} footer={null} onCancel={this.handleCancel}>
      <img alt="example" style={{ width: '100%' }} src={previewImage} />
    </Modal>
  </div>
}
```

画面9：
```javascript
constructor(props) {
  super(props);
  this.state = {
    estateDataSource: [],
    estateAddress: '',
    estateId: '',
    pics: []
  }
}
render() {
  const { submitting } - this.props;
  const {
    getFieldDecorator, getFieldValue
  } = this.props;
  const formItemLayout = {
    labelCol: {
      xs: { span: 24 },
    },
  };
}
```

画面10：
```sql
SELECT * FROM `tb_house_resources` LIMIT 0, 100
```

画面11：
```sql
// 网络面板显示
upload
200 OK
```

画面12：
```sql
SELECT * FROM `tb_house_resources` LIMIT 0, 100
```

画面13：
```javascript
action: '/haoke/pic/upload'
listType='picture-card'
fileList={fileList}
onPreview={this.handlePreview}
onChange={this.handleChange}
<Modal visible={previewVisible} footer={null} onCancel={this.handleCancel}>
  <img alt="example" style={{ width: '100%' }} src={previewImage} />
</Modal>
```

画面14：
```javascript
// 网络面板显示
upload
200 OK
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13：PDF 文档中显示“4.2. 修改AddResource.js”章节，描述了修改图片上传完成后的变更方法，包括使用 Set 集合存储图片名称。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
