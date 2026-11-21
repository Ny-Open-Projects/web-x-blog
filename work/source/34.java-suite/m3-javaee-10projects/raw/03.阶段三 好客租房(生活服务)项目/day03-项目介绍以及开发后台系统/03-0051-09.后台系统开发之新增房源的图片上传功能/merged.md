# 09.后台系统开发之新增房源的图片上传功能

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\09.后台系统开发之新增房源的图片上传功能【海量资源尽在 ubkz.com】.mp4
- 时长 9分42秒（音频 582s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下图片的上传首先呢我们先来看一下这个实现的功能效果啊那么在我们新增房源的这个位置有一个叫做上传视力图然后呢我们点击这个upload来看一下点击它然后呢呃在我们那个资料中啊给大家去有几张这张图片啊大家可以具体去使用一下啊那么你比如说我上传这个我这张图片点击它
[00:26] 那么是不是可以看到这个有一个小的一个缩略图我可以再去点一下对吧再去点一下4啊我再去我随便点一些那么看一下效果3好发现是不是后面那个添加按钮是不是没有了哎OK那么这个是我们做了一个限制啊就最多五张图啊做这样的一个限制那么我们可以点击在这个位置有两个操作一个是预览文件啊就是预览我们这个图片
[00:56] 另外一个就是把这个删除掉那我们先来看一下第一个这个预览点击它预览那么就可以去查看我们这个大图片那么我再点击这个查看可以查看这样的一个图片那么我如果要把它删掉就点击这个删除的这个按钮一点击的话那么就删掉了那么同样这个上传的这个upload的这个组件它也能够再次的显示出来那OK这个就是我们实践的一个效果
[01:22] 那么关键的我们需要来看一下它在页面中是如何实现的那我们来找一下这个under resource这个页面那么在页面的下面呢我们找到图片上传那么往下面拉找到是在在这个位置在这个位置那么所以我们可以看到是不是这有一个叫pictures view然后呢这个组件去做一个上传我们来点击一下它那么我们可以看到这个pictures view呢其实它是我们的一个
[01:53] 自定义的一个组件啊自定义的组件那么我们来看一下这个组件在哪里呢点一下它那么可以发现这个组件呢其实是在我们这个有tels这个下面啊有tels这个下面那么这个呢是一个图片的一个自定义组件那么我们来看一下在这个图片的自定义组件中它是通过什么样的组件来完成的呢我们可以看到是不是通过这个upload这个组件来完成的对吧哎OK好那么
[02:21] 现在我们是不是就可以看到是在我们的这个form表单中是不是引入了一个我们的自定义的一个图片的上传的组件然后呢在我们这个图片的上传组件中呢去上传图片上传完成之后呢最后我们是不是提交这个表单对不对OK那么提交这个表单大家想象一下那么我们的图片上传来看一下图片上传呢它是将我们的数据
[02:48] 是会保存在图片的这个组件中对吧这个stage中保存这个里面那么我们外面的这个这个form的一个页面那么这个页面呢它呢是引用了是不是图片上传的这个组件那么也就是说有一个负值组件的概念啊就是这样的一个意思我们来画个图那比如说我们这个框它呢就是我们的谁呢就是我们的这个就是我们外面的这个叫什么
[03:18] 按着resource啊这就是我们这个页面啊这就是我们这个页面然后呢我们在它的内部啊在它内部呢我们又有一个图片上传那个按钮咱们就放到这啊图片上传那么这个框呢我们认为它就是图片上传那个组件那么就是我们看到的它啊就是它它呢就是这个组件啊这个组件那么也就是说我们这个图片上传它呢是其实是我们外面这个组件的一个什么
[03:47] 直组件也就他他是什么呢他是副组件对不对副组件那么里面这个呢是属于叫直组件啊有他们的副组关系啊有这样的副组关系那么我们可以来看一下那么这个时候就会存在一个问题了那么我们的这个提交的这个按钮对吧提交按钮我解个OK啊OK那么提交按钮当我点击提交按钮的时候呢我这个副组件的一个form啊formform
[04:17] 那么form会做一个提交对不对像我们服务端是不是做一个提交那么问题就是在我们这个副组件中它又该如何去获取我们子组件中数据呢这是不是一个疑问对吧怎么样去获取这样的一个获取它这样的一个数据呢OK为什么这么说原因是你的这个子组件中上传完成之后你的上传成功的一些图片的数据是不是保存在这个里面有这样的数据
[04:47] 这样的数据这样的数据那么这些数据我副组件怎么拿到这就是我们的一个疑问或者说这是我们需要解决的一个问题那么大家还有印象吗就是我们在前面讲这个reactgest的时候那么我们讲过副组件如何去引用子组件或者说如何引用自定义的组件那么在引用自定义组件的时候又如何去传递这个数据或者说传值
[05:17] 那么我们前面说过是不是可以通过什么呢通过这种属性传输的方式让我们来看一下当我们副组件中引用我们这个图片上传这个组件的时候呢我们通过一个属性叫做hander failed list这样的一个属性去传递了一个什么呢传递了一个什么的函数注意传递了一个函数我们把这个函数呢给它传递过去给它传递过去找一下它啊找一下
[05:46] 在哪呢在这啊那我们通过这个通过属性的方式是不是给他传递过去把这个函数传递过去那么要注意的是在这个位置我们给他做了一个棒的然后类似的那么通过这个棒的这个函数我们去改变他的一个类似的指向也就是说那么在我们这个直组电中那么去调用我们这个函数的时候
[06:12] 调用我们这个函数的时候那么它的这个this所指向的就指向到我们副组件中的一个this而不是直组件中的this那么我们来看一下通过这个属性是不是将我们这函数传递到直组件中那么也就意味着在我们的直组件中可以去通过一个this.professor.handle field list是不是就可以调用了我们刚才传入的一个函数通过我们执行
[06:40] 副组件传入的一个函数那么我们是不是就可以传递一些参数给它那么来请注意那么你可以看到在这个位置这个 race.state它是不是属于我们子组件中的一个这个数据对不对然后呢它呢通过这样的一个调用通过调用那么去调用我们副组件中的一个函数也就意味着是不是可以把子组件中的这个数据是不是就传递到了我们副组件中
[07:09] 是不是通过这种方式去做一个传递啊哎OK那么所以说在我们的这个副组件中的一个这个函数中我们就可以拿到一个object啊obj那么这个obj呢就是直组件中去传入的一个fail list
[07:25] 在那里有list那么我们传入进去之后那么在副组件中就可以拿到数据了那么拿到数据我们是不是就可以把这个数据放到我们这个表单中然后跟着我们表单是不是一起做一个提交那么也是不是也就实现了我们在这个页面中是不是可以拿到我们子组件中的一个图片的数据然后做一个表单的提交好的我们接下来一起来看一下我们的讲义
[07:50] 那么在讲义中呢也做了这样的一个讲解就是说图片上传呢通过自定义的picturesville这样的一个组件来完成当然了在这个picturesville中呢需要调用什么呢upload这个组件来完成这个upload这个组件呢它其实就是谁呢就是我们的这个按照底端中的一个上传的一个组件啊OK好那么效果就这样的效果那么刚刚是不是我们也提到这个问题了就是说我们需要解决的问题是
[08:19] 副主件如何去获取子组件中的数据那么解决的思路就是副组件通过属性的方式进行引用子组件那么在棒的方法中改变Zs的一个引用作为一个副组件那么在子组件中通过Zs.prop去获取传入的一个函数进行调用就可以把数据传入到我们的
[08:42] 副主件中那么可以看到在副主件中通过这个属性是不是去传递一个函数给他然后呢在子组件中呢通过调用this.proposy.hand什么fail list通过它是不是就可以去执行去传入的这样的一个函数那么在我们的副组件中是不是拿到子组件中所传入这个数据是object那么也就是说最终我们是不是就拿到这样的数据了
[09:09] 那么其实呢在我们做图片上传的时候那么需要给大家讲的就是我们如何在副组件中去拿到子组件的这样的一个数据那么就通过什么呢属性的这种方式传递函数是不是就可以获取到啊哎OK那么这个就是给大家去讲这个图片上传
[09:27] OK好那么后面的我们也会基于这个图片上传的组件呢来去做它真实功能的一个实践会把这个图片上传的真实存储到我们的服务器上面啊OK好那么关于这个图片上传呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

