# 08.后台系统开发之新增房源的自动完成功能的讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\08.后台系统开发之新增房源的自动完成功能的讲解【海量资源尽在 ubkz.com】.mp4
- 时长 9分19秒（音频 559s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下自动完成这个功能那么什么是自动完成呢那么它用在哪里呢我们来一起来看一下首先我们先来看一下我们最终实现的一个效果那么其实呢是在上面这个位置啊帮我们去新增一个房源的时候那么这个房源是不是一定有所属的一个楼盘呢
[00:21] 因为楼盘你不能随便写对吧它一定是在我们系统中啊所存在的一个楼盘所以呢我们需要在这个位置呢去做一个搜索啊比方说来一个来一个来一个什么的上海啊上海那么你看当我去输入这个上海两个字的时候是不是它就会出现有下面这两个选项对吧那么比方说我选择这个上海康城然后我点击它一点击那么它就自动会在下面这个楼盘地址这个位置是不是去给我去直接输入这个值
[00:51] 对吧叫上海市闽杭区新松路958弄啊这样的一个地址OK好那么这个就是我们最终做完的一个效果对吧那么这个效果怎么做出来的呢需要给大家去讲解一下那我们来找到找到我们的这个文档啊找到文档这个呢是官方的一个自动完成这个文档那么其实呢实在是在这个位置啊那我们来看一下这个输入框的自动完成
[01:19] 那么自动完成它有很多种演示大家可以看一下比如说像AA随便写AA等等是不是有一些提示对吧写这样的一个提示对吧像这种效果我相信大家在网上是不是很多位置都见到过自动完成补全后面这个邮箱这样的一个效果然后还有像这样的效果对吧比如说你看这个怎么样比如说输入一个币怎么样的OK然后比如说这个位置输入一个币是不是有这样的一个效果等等OK
[01:48] 那么它的一些 API就在下面那么我们来看一下我们具体在使用它的时候怎么样去做我们找到我们的自动完成的位置那么也就是说我们在这在这个位置是不是引入了一个自动完成这样的一个组件
[02:05] 然后在这个里面要注意的是我们给它设置了一个data source那么这个data source等于谁呢等于this.state是不是我们将这个data source的数据给它放在我们的当前的组件状态中然后我们来找一下当前状态值在哪里来看一下那么显然是不是在这个位置不是在这找错了然后再往上面点一下应该下面这个点一下那么我们可以看到
[02:35] 在这个位置是不是我们一个构造函数在构造函数中我们设置了我们这个叫楼盘的数据Data Source它是一个空相当于做一个初始化就是一个空的一个数组好那么继续往下面看那么一开始是不是就会有一个相当于是一个空的数组什么都没有对不对那么我们什么时候给它去填充这个数据呢让它去显示出这个什么的比如说上海填充这两个数据上海康城和上海这个阳城
[03:06] 那么OK那么来看一下怎么做那么在这个里面呢其实我们有一个叫做什么的unsearch这个方法那我们来看一下官方这个文档对他这个描述什么叫unsearch呢说一下是不是就是在搜索补全项的时候需要调用对吧那么当我们去去这个需要他补全的时候去调用这个unsearch这个方法那我们就用this.handset
[03:30] 那找一下listing and search是不是在这个位置那么这个里面呢我们实现了一个小的一个逻辑啊什么逻辑呢就是就是呢我们去这个里面你看拿到我们的一个value只注意这个value就是我们所输入这个字比如说我输入的是一个上上这个字啊这个value拿到就这个上这个字那么这个字呢判断一下如果大于0就说明我输入内容了那么继续去找没有的话那就直接设置为它啊就就OK了
[03:59] 那么在这个里面我们做了一个小逻辑什么逻辑呢有一个E-State Map就是我们这个房源数据有一个Map定义在这那么看到这大家就明白了原来我们是把这个数据写死到我们的页面了对不对但是好像这样做似乎是有点不合理的为什么呢因为我们刚刚讲过在我们的楼盘数据的时候是不是已经有一个后台的一个数据数据表是不是去存储这个数据
[04:24] 对不对那么这个位置怎么把它写死了呢OK那么简单的解释一下就是由于我们现在呢是做这个新增房源的这样的功能那么我们先把这个位置呢先写死啊那么我们只要把它能写死然后实现这个功能那么我们后期把它改成能够去后台加载数据是不是也是很容易的事情啊这个并不难啊所以呢我们先把它写死那么也就是说
[04:47] 在这个位置我是不是已经有相当于我这个楼盘数据对吧有五条这个数据那么五条数据呢我在这个位置呢给它去做一个EFH循环然后呢我去判断一下判断什么呢判断我这个key注意key是不是就是我这个楼盘的名称对吧key是楼盘的名称啊然后呢我判断key是不是以我以我输入的这个关键字开始如果要是的话那就把它push到我这个数据中
[05:14] 那么如果不是的话那就不把它push进去然后最后我们是不是要用这次点setState去更新我们的状态的数据更新状态数据中这个叫eState然后DataSource更新它是一个这样的一个数组那么是不是就可以看到当我们去输入上这个字的时候那么它是不是去做一个便利便利我们在集合中是不是就会有两个一个是上海康城一个就是上海的阳城对吧ok找到这两个数据
[05:44] 然后给他去做一个填充这样的一个效果OK好那么这个我们就知道了通过这种方式就可以去做一个数据的填充那么当我们去选中他的时候他是又如何去修改下面的数据来看一下比如说我选择上海阳城那么就改成了闽杭区的罗景路OK那么他是如何去做到这样的一个效果的我们来看一下那么依然还是找到我们的找到我们自动完成这个位置
[06:13] 在知道完成这个位置呢它有一个属性叫做unselect就是选择的时候啊那我们来搜索一下看一下这个选择unselect官方的一个解释是什么呢是被选中时调用然后呢参数中为选中项的value的值哎呀ok那我们就知道了那么这个value是不是就是我们选中的那个值那么我是不是就可以通过这个值去到我前面这个map中是不是找到我的这个数据找到这个v
[06:42] 然后我去更新这个值要注意的是那么我的楼盘的数据它的值怎么显示来看一下在我的楼盘数据这个位置是不是我有一个input并且我把它标记为sigridonly的就是一个纸炉的这样的一个标签这个里面的数据你是修改不了的对吧你是修改不了的修改不了的
[07:04] 然后我们可以看到它的一个default value就是默认值就是拿到this.state中的e state中的address是不是这样的一个属性对吧拿到这样的属性那么通过这个属性是不是就显示它的值那么我们想要去给这个表单去设置值那我们只需要去修改这个state中的这个属性值是不是就可以了所以我在这个位置是不是就去拿到我这个v
[07:31] 拿到我这个V拿到我的这个值然后做一个sub-stream是不是做一个这个字符算的一个截取那么为什么要去做字符算截取呢我们来看一下它的一个数据结构那么在这个数据结构中我们发现它的一个value是以一个数杠做一个分割的对不对那么前面这个就是我们楼盘的ID后面这个是不是就是我们楼盘的一个具体的一个地址所以我们需要去分割这个数杠那么根据数杠的前面就是ID后面是不是就是它的一个
[07:59] 后面显示的是不是一个具体地址所以我们需要给他设置的是他的一个地址就是截取从这个速杠的下一个字符开始去截取然后一直截取到最后那么这个他的具体地址那么当我们去set state的时候去更新的时候是不是他就会去自动去更新了这个位置所以我们可以看到这样的效果对吧比如说我选择上海我选择康城
[08:21] 他就改回到这个地址了OK就这样的一个效果那么也能说老师下面这个Estate ID是什么意思呢这个是楼盘的ID那么这个拿这个有什么用我们并没有展现出来对不对并没有显示出来那么我们拿到它有什么意义呢意义是不是就是当我们表单提交的时候我们是有必要去提交这个楼盘数据的因为我们最终我们的数据中是不是有一个楼盘数据这个ID这个大家能够理解吗OK好
[08:48] 然后呢我们看到啊在最后我们提交的时候是不是就需要拿到这个楼盘这个ID给他去做一个提交哎OK好嘞那么那么这样的话我们是不是就已经完成了一个这个自动完成了这样的一个代码对吧OK这样的效果呢就实现了
[09:06] OK那么也希望通过这个讲解大家参考官方的文档那么就可以去实现自己想要的一些功能OK好那么关于这个自动完成我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Ant Design 的 AutoComplete 组件中实现房源地址的自动补全功能，并在前端代码中集成该组件。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 Ant Design 官网 AutoComplete 组件的“基本用法”示例，包含一个输入框和一个数据源数组。
画面 2: 展示 AutoComplete 组件的 API 文档，包含 `allowClear`、`autoFocus`、`backfill`、`children`、`dataSource` 等参数及其说明。
画面 3: 展示前端代码中 `handleSearch` 函数的实现，用于根据输入值筛选房源地址数据。
画面 4: 展示 AutoComplete 组件的 API 文档，与画面 2 内容相同。
画面 5: 展示前端代码中 `handleSearch` 函数的实现，与画面 3 内容相同。
画面 6: 展示前端代码中 `estateMap` 的定义和 `@connect` 高阶组件的使用。
画面 7: 展示房源管理系统的前端页面，用户正在填写房源信息，地址字段已自动补全。
画面 8: 展示前端代码中处理表单字段的逻辑，包括 `facilities`、`floor_1`、`floor_2` 等字段的处理。
画面 9: 展示前端代码中 `handleSearch` 函数的实现，与画面 3 内容相同。
画面 10: 展示前端代码中 `Form.Item` 和 `Input` 组件的配置，包括 `style`、`placeholder`、`rules` 等属性。
画面 11: 展示前端代码中 `FormItemLayout` 和 `submitFormLayout` 的配置，用于定义表单布局。
画面 12: 展示前端代码中 `AutoComplete` 组件的完整实现，包括 `style`、`dataSource`、`onSelect`、`onSearch`、`filterOption` 等属性。
画面 13: 展示前端代码中 `handleSearch` 函数的实现，与画面 3 内容相同。
画面 14: 展示房源管理系统的前端页面，用户正在填写房源信息，地址字段已自动补全。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```jsx
const dataSource = ['12345', '23456', '34567'];
<AutoComplete dataSource={dataSource} />
```

画面 2:
```jsx
const dataSource = ['12345', '23456', '34567'];
<AutoComplete dataSource={dataSource} />
```

画面 3:
```jsx
handleSearch = (value) => {
  let arr = new Array();
  if(value.length > 0) {
    estateMap.forEach((v, k) => {
      if(k.startsWith(value)) {
        arr.push(k);
      }
    });
  }
  this.setState({
    estateDataSource: arr
  });
};
```

画面 4:
```jsx
const dataSource = ['12345', '23456', '34567'];
<AutoComplete dataSource={dataSource} />
```

画面 5:
```jsx
handleSearch = (value) => {
  let arr = new Array();
  if(value.length > 0) {
    estateMap.forEach((v, k) => {
      if(k.startsWith(value)) {
        arr.push(k);
      }
    });
  }
  this.setState({
    estateDataSource: arr
  });
};
```

画面 6:
```jsx
const estateMap = new Map([
  ['1001', '上海市,上海市,普陀区,远景路97弄'],
  ['1002', '上海市,上海市,闵行区,莘松路958弄'],
  ['1003', '上海市,上海市,松江区,广富林路1188弄'],
  ['1004', '上海市,上海市,闵行区,七莘路3333弄2区-15区'],
  ['1005', '上海市,上海市,闵行区,罗南路888弄']
]);
@connect(({ loading }) => {
  submitting: loading.effects['form/submitRegularForm'],
})
```

画面 7: 无代码。

画面 8:
```jsx
if(values.facilities) {
  values.facilities = values.facilities.join(",");
}
if(values.floor_1 && values.floor_2) {
  values.floor = values.floor_1 + "室" + values.floor_2 + "厅" + values.houseType_1 + "卫" + values.houseType_2 + "阳台";
  delete values.floor_1;
  delete values.floor_2;
  delete values.houseType_1;
  delete values.houseType_2;
  delete values.houseType_3;
  delete values.houseType_4;
  delete values.houseType_5;
}
dispatch({
  type: 'form/submitRegularForm',
  payload: values,
});
```

画面 9:
```jsx
handleSearch = (value) => {
  let arr = new Array();
  if(value.length > 0) {
    estateMap.forEach((v, k) => {
      if(k.startsWith(value)) {
        arr.push(k);
      }
    });
  }
  this.setState({
    estateDataSource: arr
  });
};
```

画面 10:
```jsx
style={{ width: '100%' }}
dataSource={this.state.estateDataSource}
placeholder="搜索楼盘"
onSelect={(value, option) => {
  let v = estateMap.get(value);
  estateAddress = v.substring(v.indexOf('!') + 1, v.indexOf('!'));
  this.setState({
    estateAddress: v.substring(0, v.indexOf('!'))
  });
}}
onSearch={this.handleSearch}
filterOption={(inputValue, option) => option.props.children.toUpperCase().indexOf(inputValue) > -1}
```

画面 11:
```jsx
const FormItemLayout = {
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

画面 12:
```jsx
return (
  <PageReaderWrapper>
    <Form onSubmit={this.handleSubmit} hideRequiredMark style={{ marginTop: 0 }}>
      <FormItem {...FormItemLayout} label="楼盘名称">
        <AutoComplete
          style={{ width: '100%' }}
          dataSource={this.state.estateDataSource}
          placeholder="搜索楼盘"
          onSelect={(value, option) => {
            let v = estateMap.get(value);
            estateAddress = v.substring(v.indexOf('!') + 1, v.indexOf('!'));
            this.setState({
              estateAddress: v.substring(0, v.indexOf('!'))
            });
          }}
          onSearch={this.handleSearch}
          filterOption={(inputValue, option) => option.props.children.toUpperCase().indexOf(inputValue) > -1}
        />
      </FormItem>
      <FormItem {...FormItemLayout} label="楼盘地址">
        <Input
          prefix={<Icon type="environment" style={{ color: 'rgba(0,0,0,25)' }} />}
          value={this.state.estateAddress}
          readOnly
        />
      </FormItem>
      <FormItem {...FormItemLayout} label="楼栋">
        <InputGroup compact>
          <Input />
        </InputGroup>
      </FormItem>
    </Form>
  </PageReaderWrapper>
);
```

画面 13:
```jsx
handleSearch = (value) => {
  let arr = new Array();
  if(value.length > 0) {
    estateMap.forEach((v, k) => {
      if(k.startsWith(value)) {
        arr.push(k);
      }
    });
  }
  this.setState({
    estateDataSource: arr
  });
};
```

画面 14: 无代码。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

