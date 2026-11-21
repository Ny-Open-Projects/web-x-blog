# 09.整合前后端进行图片上传开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\09.整合前后端进行图片上传开发【海量资源尽在 ubkz.com】.mp4
- 时长 9分51秒（音频 591s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着内容继续啊那么下面呢我们就需要去整合我们的前端的去实现这个图片的上传那么现在呢我们相当于是已经把后端的服务呢是不是已经搭建好了那么现在我们只要需要去前后端去整合去做一个实现那么这个图片上传功能就做完整了对吧好那么这样的我们先把我们的服务端的这个实现呢我们先给他
[00:24] 切回到什么呢先切回到我们的这个阿里云的这个实现啊OK那么把它拿掉把这个呢拿掉把下面这个给它住掉啊把这个也住掉好这样的话是我们就切回到我们阿里云的这个OSS服务的一个实现好把它启动起来那么在它启动过程中呢我们就来看一下我们的讲义啊那么对于我们前后端的整合呢其实我们要去修改的是不是就是我们图片上传那个页面那么图片上传那个页面我们大家还有没有印象啊是在
[00:53] 我们的这个Pages下面有一个叫做浩克对吧然后呢我们有一个Android Source新增房源这个位置然后呢往下面找找到我们的有一个叫做上传图片的这个位置是不是它引入了一个自定义的那个组件对吧我们点击它那么就会进入到这个自定义这个组件里面在这个组件中呢我们下面就有个Upload这个组件这个组件所使用的就是按着Design它提供的一个组件
[01:20] 那么在这个组件中呢它需要提供的是一个accent就是你提交的一个路径那么我们需要把这个路径是不是写成我们自己的这个路径要注意的是我们自己的这个路径是不是这样的路径啊118080然后呢PIC后面一个upload对不对这样的路径但是呢这个里面是不是会存在一个跨域的问题对吧所以呢我们在前面配置了一个呃配置了一个找一下啊
[01:47] 配置了一个代理这个还有印象吗是不是在这个位置是不是配置了这样的一个代理对吧那么我们就可以去以这个浩克开头的一个请求会议转发到我们本机的一个这个18080这个端口然后呢并且把这个前面这个浩克给它替换掉替换掉好然后呢我们再进入刚刚的我们这个页面所以呢在这个页面中我们只需要把这个action地址写成这个样子是不是就ok了就是在前面这个地址
[02:15] 前面加一个浩克就好了哎好那么第一个这个操作是不是就搞定了第二个这个操作呢是我们需要去在我们上传完成之后那么我们在提交我们这个表单页面的时候就我们在提交把这个我们都关掉啊在我们提交点击提交的时候那么我们是不是要去拿到他上传之后的一个这个结果然后呢把它丢到我们这个表单里面是不是一起做一个提交对吧哎OK
[02:45] 好那么我们先来测试一下这个上传这个逻辑它OK不OK先保证这个是OK的对吧然后我们再来看一下它怎么处理它这个数据好那么点击这个upload我们来去点击一个这个图片上传中可以看到这个是不是已经上传成功了那我们来看一下那么它是返回的一个数据是不是已经返回的是这个阿里云的这个地址那么并且这个图片的预览是不是也可以正常做一个预览那我们尝试的去反问一下
[03:15] 这个图片能不能够去成功的去访问到哎OK不行我们前面是不是做过一个这个限制啊所以呢我们要把这个限制给他打开不需要做一个源头保护了保存好这样就OK了然后我们刷新一下好这样的话是不是就没有任何问题啊可以访问到了好那么我们是不是先保证我们能够上传到我们的这个服务器上面然后呢我们接着继续往下面看
[03:44] 在我们的新增图片的这个新增房源的这个里面呢我们前面说过是不是有个叫做hunter fill list这样的一个方法那我们来做一个搜索找一下这个方法找一下这个方法然后呢去找找找在上面呢有一个这样的方法那么他会传递一个obj给我们那么这个obj obj是谁呢其实就是在我们前面的这个图片上传这个里面是不是在这个位置对吧
[04:15] 通过我们的publish中的这个handle fill list这个方法将这个state中的fill list传递给我们那么这个file state fill list就是我们回传到回传给这个upload组件的一个图片的一个列表所以呢我们在这个里面就能够拿到我们这个图片的一个列表拿到一个它由于我们传入的这个数据啊它会有些重复所以呢我们需要在这个位置定一个set集合
[04:44] 然后我们不断的去将我们这个图片的内幕其实就是我们回传到回传给我们这个URL对不对就这个URL你看是不是这个内幕对吧将这个URL就填到我们这个set的这个集合中那么是不是就可以做一个重复的一个去重的一个动作对吧然后我们接下来将我们这个图片这个集合我们给它丢到我们的state中状态中
[05:08] 那么在我们前面做初始化的时候啊那么我们也给他做了一个set集合的一个哎找一下在前面找到一个初始化在这对吧他这个里面是不是有一个pics是不是一个初始化的一个是一个空的一个数组然后呢我们在做表单提交的时候那么在这个位置呢我们将这个pics是不是保存到我们这个values中是不是作为表单一起做一个提交啊
[05:35] 在这个位置有一个小的一个技巧大家可以来看一下就是呢我们这个PICS是不是就是一个set击合它是它如何去转成一种什么结构呢这样的一种结构我们来看一下找到那个我们的这个NavKit找到NavKit来看一下我们的一个数据结构大家这个还有印象吗我们来看一下要把我这个里面找到这个浩克然后呢我们找到我们这个房源
[06:03] 在这个里面呢我们其实要求我们这个数据啊那么存储到我们这个PIC这个字段里面的话那么我们可以发现是不是它是用这个逗号是不是去做一个分割的对吧做一个逗号的一个分割那么我们这个如何去将我们的一个这个set集合去转成这样的一个结构呢对吧转成这样一个正方形结构用逗号分割的一个结构那么在这个位置用了一个小的一个技巧啊就是
[06:32] 由于我们的宿主它本身是不是有个join这个方法就可以把宿主的元素用这个逗号是不是把它连接起来那么我们只要想办法去把它这个url是不是转成一个宿主就可以了对吧所以呢我们就在前面有个宿主那么怎么样把一个set击和快速转成一个宿主呢我们通过一个展开这个表达式还记得吗就是我们三个点这个操作
[06:58] 将我们的set的集合给它展开然后就形成一个新的一个素组然后做一个join操作就可以得到我们的一个字符创OK就这样的一个效果那么接下来我们来测试一下它是否能够去实现这样的一个效果那么我们来上传几张图片比如说就两张两张这个图好嘞那么我们来看一下这个楼盘的数据比如说我们写一个上海上海然后呢房源的标题那就随便写一个吧就是康城
[07:28] 康城的精品房源然后呢这个123随便写数据了租金1000元然后呢付一押一整租然后呢一室一厅一卫一厨一阳台然后呢建筑面积呢50平方使用面积呢40平方然后呢楼层呢是在三层然后总高呢20层随便写啊这个随便填那么房源描述就是精品房源随便写点东西
[07:58] 然后图片我们是不是已经上传了两张了对吧联系人李四然后手机号18888写这么多然后物业费一块钱一个月点击提交注意观察在提交的一个内容走那么提交那么我们房源数据是不是提交成功了对吧那我们来看一下提交的数据长什么样那么在提交这个数据中我们来看一下表单的一个数据重点关注的是不是这个PIC这个数据那么可以看到这个数据是不是有两个这个URL
[08:27] 那么并且已经用逗号是不是做了分割那么我们来尝试去访问一下第二个这个URL看它是不是能够访问到我们刚刚所上传的一张图片呢走那么可以看到是不是这张是不是就是我们刚刚上传的一张图片啊OK好那我们来看一下有没有把数据保存到我们的这个数据库呢来刷新看一下那么在这个里面是不是有一个叫康城精品房源是不是已经就上传到我们的保存到我们数据库了对吧那么来看一下这个图片哎OK是不是没有任何问题啊好嘞
[08:56] 好那么这样的话我们是不是就已经实现了图片的一个上传OK那么来看一下我们的讲义那么首先第一个是修改我们图片上传组件中的提交的地址然后在我们新增房源这个页面中我们就去给它修改一下我们处理逻辑然后我们去把图片的一个拼接字幕创是不是放到PIC这个里面
[09:22] 这个位置是对于set击合做了一个处理这是也是一个小技巧希望大家能够从这个点去学习这样的一个小技巧然后进行做一个测试那么最后数据是不是就保存到我们的数据库了没有任何问题那么这样的话我们是不是整合了前后端实现了图片上层这个功能那么到此为止我们新增房源这个功能是不是就算是比较完整的实现了OK好那么关于前后端整合开发我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

