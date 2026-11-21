# 画面线理解：08.后台系统开发之新增房源的自动完成功能的讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\08.后台系统开发之新增房源的自动完成功能的讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:51, 02:27, 02:50, 03:38, 04:07, 04:37, 05:05, 06:08, 06:51, 07:39, 08:24, 08:56, 09:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:30:24

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
