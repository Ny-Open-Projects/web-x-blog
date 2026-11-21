# 09.更新房源窗口销毁问题的演示以及说明

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\09.更新房源窗口销毁问题的演示以及说明【海量资源尽在 ubkz.com】.mp4
- 时长 3分20秒（音频 200s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么下面呢,我们来演示一下前面我们所说到的这个销毁的这个问题啊刚刚呢,只是我去口述了一下啊那么可能呢,大家也不一定能够去理解到底为什么要把它设置为true因为呢,我在做这个功能的时候啊也掉到这个坑里面了然后呢,去网上一搜呢,也会发现
[00:22] 有很多人也掉到这个坑里面去了所以我们有必要把这给大家演示一下因为我们现在功能都已经OK了对吧那我们就可以给大家来做个演示就如果我把它设置为False因为它默认是False对不对那我们看一下会发生什么会出现什么情况那我们来刷新一下这个页面那么给大家来演示一下它的一个问题那么我们依然的点击这个编辑点击这个编辑然后把这个数据注意改的是最新的一条数据把它设置为44
[00:52] 走那么可以看一下没有任何问题我们点击他也是44没有问题那么点击下面的这个是不是也是最新的修改房源三没有任何问题但是要注意了那么如果我现在修改的不是第一条数据而是修改的第二条或者说其他数据那么我就以这个第二条数据为例我点击这个第二条这个编辑没有问题对吧我把它改成这个4要注意观察我点击一个确定走那么要注意的是我是不是已经修改成功了
[01:22] 那么是不是这个表格的数据是不是也进行了重新的一个刷新但是如果我点击在这个位置我点击第二条数据44用ID为8的这条数据当我点击这个编辑的时候来看一下会发生什么点击它的时候你会发现第二条数据依然是什么之前的那个数据看明白了吗依然是之前那条数据
[01:47] 原因是你之前所生成的弹出框的对象并没有被销毁所以依然保留的是第二个位置的数据并没有被销毁ok所以会出现这样的一个问题那么所以我们就需要把它设置为什么去
[02:05] 那么当我们去关闭这个窗口的时候然后需要把这个窗口的内容给它全部都销毁掉然后重新再做一个生成OK这样的话就没有问题了我们再来做个测试看一下效果那么我们来看一下我修改最新的这个数据把它修改成5我们来测一下来看一下当我点击它看有没有问题是不是没有问题然后我修改的是第二条这个数据我把44改成555
[02:35] 然后点击这个提交走那么当我再点击我的第二行数据你看这个55是已经跑到最前面去了对吧当我点击这个第二行这个数据它会怎么样呢走是不是就会显示第二条这个数据而不会显示前面的55哎OK这个就是我前面所说的这个窗口这个销毁的这个问题那么这个呢大家也可以动手的去测试一下它会有这样的一个问题那个网上也有不少人掉到这个坑里面去了哎呦OK
[03:04] 那么希望把这个问题呢给大家去讲出来然后大家能够去理解然后在做项目的时候呢一定要避开这个坑呢哎OK好那么关于这样的一个销毁的一个问题的一个演示呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 React 的房源管理系统的编辑弹窗功能，包括前端界面交互和对应的 React 组件代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档目录结构，其中包含“4. 实现新增房源弹窗”、“4.1. 修改 Controller”、“4.2. 修改 Service”等条目，同时显示了 React 组件代码片段，包含 Modal 和 FormItem 的配置。
画面 2: 在 IntelliJ IDEA 中展示 EditResource.js 文件的代码，包含 Modal 组件的配置和 FormItem 的结构，其中 FormItem 的 label 为“房源标题”。
画面 3: 浏览器中显示空白页面，地址栏为 localhost:8000/house/resource。
画面 4: 展示房源管理页面的编辑弹窗，弹窗内包含房源标题、租金、建筑面积和上传室内图等字段。
画面 5: 展示房源管理页面的列表，包含房源编号、房源信息、图片、支付方式、户型、面积、操作等列。
画面 6: 展示房源管理页面的列表，鼠标悬停在第 3 条房源记录上。
画面 7: 展示房源管理页面的编辑弹窗，弹窗内包含房源标题、租金、建筑面积和上传室内图等字段，上传室内图已显示两张图片。
画面 8: 展示房源管理页面的编辑弹窗，弹窗内包含房源标题、租金、建筑面积和上传室内图等字段，上传室内图已显示两张图片。
画面 9: 在 IntelliJ IDEA 中展示 EditResource.js 文件的代码，高亮显示了 this.refs、this.render()、this.componentWillReceiveProps 等方法。
画面 10: 浏览器中显示空白页面，地址栏为 localhost:8000/house/resource。
画面 11: 展示房源管理页面的编辑弹窗，弹窗顶部显示“提交成功”提示，底部有“取消”和“确定”按钮。
画面 12: 展示房源管理页面的编辑弹窗，弹窗内包含房源标题、租金、建筑面积和上传室内图等字段，房源标题已输入“555”。
画面 13: 展示房源管理页面的编辑弹窗，弹窗内包含房源标题、租金、建筑面积和上传室内图等字段，上传室内图已显示两张图片。
画面 14: 在 IntelliJ IDEA 中展示 EditResource.js 文件的代码，包含 Modal 组件的配置和 FormItem 的结构，其中 FormItem 的 label 为“租金”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
return (
  <React.Fragment>
    <a onClick={() => this.showModal()}>编辑</a>
    <Modal
      title='编辑'
      width={640}
      visible={this.state.visible}
      onOk={() => this.handleSave()}
      onCancel={() => this.handleCancel()}
      destroyOnClose={true}
    >
      <div style={{ overflowY: 'auto' }}>
        <FormItem {...formItemLayout} label='房源标题'>
          {getFieldDecorator('title', {
            initialValue: record.title,
            rules: [{ required: true, message: '请输入房源标题' }]
          })(<Input />)}
        </FormItem>
      </div>
    </Modal>
  </React.Fragment>
)
```
画面 2:
```javascript
form: { getFieldDecorator }
- this.props;
return (
  <React.Fragment>
    <a onClick={() => this.showModal()}>编辑</a>
    <Modal
      title='编辑'
      width={640}
      visible={this.state.visible}
      onOk={() => this.handleSave()}
      onCancel={() => this.handleCancel()}
      destroyOnClose={true}
    >
      <div style={{ overflowY: 'auto' }}>
        <FormItem {...formItemLayout} label='房源标题'>
          {getFieldDecorator('title', {
            initialValue: record.title,
            rules: [{ required: true, message: '请输入房源标题' }]
          })(<Input />)}
        </FormItem>
      </div>
    </Modal>
  </React.Fragment>
)
```
画面 9:
```javascript
this.refs (React.Component)
this.render() (EditResource)
this.componentWillReceiveProps (nextProps: Readonly<P>, nextContext: any)
void
this.UNSAFE_componentWillReceiveProps (nextProps: Readonly<P>, nextContext: any)
void
EditResource(props) (EditResource)
```
画面 14:
```javascript
<Modal
  title="编辑"
  width={640}
  visible={this.state.visible}
  onOk={() => this.handleSave()}
  onCancel={() => this.handleCancel()}
  destroyOnClose={true}
>
  <div style={{ overflowY: 'auto' }}>
    <FormItem {...formItemLayout} label="房源标题">
      {getFieldDecorator('title', {
        initialValue: record.title,
        rules: [{ required: true, message: '请输入房源标题' }]
      })(<Input />)}
    </FormItem>
    <FormItem {...formItemLayout} label="租金">
      <InputGroup compact>
        {getFieldDecorator('rent', {
          initialValue: record.rent,
          rules: [{ required: true, message: '请输入租金' }]
        })(<Input />)}
      </InputGroup>
    </FormItem>
    <FormItem {...formItemLayout} label="建筑面积">
      {getFieldDecorator('area', {
        initialValue: record.area,
        rules: [{ required: true, message: '请输入建筑面积' }]
      })(<Input />)}
    </FormItem>
  </div>
</Modal>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

