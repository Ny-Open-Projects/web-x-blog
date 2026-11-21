# 25-网站流量日志分析-数据的可视化-案例分析结果可视化

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\25-网站流量日志分析-数据的可视化-案例分析结果可视化【海量资源尽在 ubkz.com】.mp4
- 时长 14分0秒（音频 841s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在学习完一掐死的入门之后接下来我们的任务是将这个数据库中的两张表的数据那么这两张表呢分别是一个每天的页面平均访问量还有个是一周内每个页面访问参数的一个值把这两张表的数据呢通过一掐死展示到页面上那么要做这件事情呢我们还是得去实现一个外部编程来打开我们的ID
[00:29] 在这里呢我已经把这个所有的资源和代码给大家提供好了那首先呢我们要实现这么一个案例的话呢我们有些页面资源我已经在这里复制过了这个里边比如说有CSS样式有它用到的一些图片Image还有JS文件以及呢这里边还提供了一些页面OK提供了一些页面都是我们需要的一些资源好在这个index.jsp里边呢
[00:59] 这里边我已经把一掐四中我们要用的一些界面模板已经放在这里了好那接下来我们怎么做呢我们需要使用三大框架将我们数据库中的数据呢读取到页面上来我们来看在加尔瓦的下面呢我建了一个包CNIDCAS Weblog好在这里呢我们呢我建了一个三层架构一个Control层控制层一个呢Service层业务层
[01:28] 一个Mapper一个持久层OK那么接下来我们先看第一个Control层OK点开在这个Control里边呢我们做了一件事情来这个先不用看看这个这个呢有一个注解叫Request Mapping这个是一个请求用色为什么写这么一个东西呢我们来看一下我们的eChast的主页面在哪里呢
[01:55] 在我们webinfo下面jsp有个index.jsp在这里的话呢有一个地方我们来找一下就是这个地方像应该是我看一下我们有两张两个图一个是一个是这个我来看这个一个是avgpvnumberaction我们来看是不是它这个地方呢拿到我们这个代码里边avgpvnumberaction就是它
[02:31] 好那么这个地方呢它其实是一个阿贾克斯请求阿贾克斯请求这个阿贾克斯请求里边呢你看一下它的请求的URL呢是AVG PV number action就是平均的配积V数量那么当我去请求这个路径的时候呢那这个时候呢我们的服务器给我们返回一个json哎返回json之后呢注意这个data就是返回的一个json串拿到这个json串之后呢我在这里
[03:01] 我调了一个叫set options那这个set options不就是咱在看那个一掐死的模板的时候调了这个方法也就是我只要调了这个方法我就可以把这里的数据展示到我们的页面上那么在展示的时候呢它需要一些数据这个数据呢来自data也就是来自服务器给我返回的这个对象这个对象中有两个参数一个是x种这个地方是data的datas
[03:31] 一个是呢一个是SERV是它携带的数据data.data也就是说我只要让服务器给我返回这两个数据那么它就能够正确展示这两个数据来自哪里呢最终其实来自是我们的数据库哪个数据库呢应该是这个来自这个数据库你可以认为呢我们这里边两个参数一个是data分别对应这个列而一个是data呢
[04:01] 它应该是对应这个列OK所以说这两列分别对应这两个参数那么我们的任务是干嘛呢我们的任务是用三层架构将数据库中的数据呢变成json返回给这个页面就可以了好那我们来看当他请求这个路径的时候呢在这个Controller里边呢他会去找到这个他去利用这个请求用上然后呢会执行这个方法好那么执行这个方法的时候呢
[04:30] 我们这个方法干了什么事呢我们来看一下这个方法的话呢他首先呢去调Service那么调完Service之后呢他返回了一个对象这个对象是什么呢我们进去看一下这个对象里边包含了两个集合为什么是两个集合呢是因为呢我们页面呢要数据的时候呢要的其实是一个数组那么我最终给他的是一个JSON我们的集合是不是刚好可以转成数组所以说呢
[05:00] 这个地方它是一个集合我们来看这个地方它是一个集合好那回到我们刚才的代码那么返回的数据刚好满足页面的需求好那这个地方它转成对象之后我们加了这个注解它就会把这个对象转成Jason好这是我们的Control那么Control调Service我们去看Service好Service这是一个接口我们来找它的实现类这个是它的实现类AVG Number Service MPL
[05:31] 这个实现类干了什么事情呢看这句话这个实现类呢调MAPR也就是持久层它调了一个方法通过这个方法呢你认为它可以去获取这个表中的所有数据这个表中的所有数据OK这个表中的所有数据呢放在这个集合中这有一个类这个类是什么呢这个类看一下这个类有三列三个成员变量而你这个表是不是有三列它们俩之间刚好对
[06:02] 也就是说我们去调用数据库查询数据库的时候我们得到的是一个集合那么得到一个集合之后呢这个full循环是将这个集合的值变例变例完之后呢添加到这两个集合里面去OK那么拿到这两个集合之后呢我们还需要将这两个集合添加到这个对象里面去因为我们上层呢要的是对象所以说呢这个其实就是从数据库中
[06:31] 查询那个表的数据并且把这个数据呢封装到这个对象好封装完之后呢这个地方咱再看一下这个mypar也就是我们的持久层这个mypar呢是用mybattis写的来我们来看一下这mypar这个里边呢mypar是一个方是一个接口在这个位置在resource里边mypar里边有个有一个配置文件avg在这里呢我们用mybattis呢来去执行一条搜索指令
[07:00] OK这是他一个套路好那么有了这个之后呢我们再回到contra的层好经过下层的调用呢我们得到了这么一个对象而这个对象中呢有两个集合这两个集合呢分别对应我们这个数据库中这两列的数据拿到这个集合之后呢我们回到刚才这个地方拿到这个集合嗯稍等拿到这个集合之后呢而这个对象呢会把
[07:30] 里边的成员变成杰森返回给我们的页面好页面收到数据之后呢我们再回到页面回到这个页面页面收到数据之后呢就会在这个位置和这个位置使用集合的值然后使用集合的值之后呢它就会在这个地方形成一个数组那么就会把这个数组的内容呢展现到我们的页面上来这样我们把这个呢也给大家启动一下好我们把这个代码呢也给跑一下
[08:00] 热补数一下稍等我们的访问路径呢是什么呢看下control我们的访问路径是这个AVPGNUMBER ACTION我来访问好在这里我们访问试一下走回车稍等我们来访问那个页面好这个地方呢是不是访问地址写错了我们得到的是一个JSON哦这个地方写错了我们应该先访问这个这个呢它就会给我们返回
[08:36] 这个里边webinfo.jsp下面的一个index.jsp我们要的页面其实是一个index.jsp然后这个index.jsp呢会发出阿加克斯请求然后呢向这个页面呢重新再发出这个请求所以说我们应该先访问index.action我们来做一下在后面呢给一个index.action走来访问它的首页来我们来看一下你会发现这个地方呢出现了一个
[09:06] 最近7天的日均访问量那这个呢其实就是我们刚才啊刚才呢从数据库读出来的数据你看20130919这是日期吧每个日期呢访问量13.4017.60OK这就出来了这就是注装图好那么接下来呢我们还有一个什么呢我们还有一张表这个表呢是这个flow number这个是一周呢
[09:36] 各个参数的一个访问量那这个呢怎么去显示到我们这个图里面呢那么这个地方呢我们可以使用折线图来做那我们来做一下首先呢在这个页面中呢我们先找到在这个页面中我们来在这个index.gzb中我们来找另外一个地方这个地方应该是我来看一下那是近一周访客的变化趋势就这个
[10:05] 这个的话又是一个e-charts的一个独立的一个一个显示的页面我们来看一下就在这个位置那这个地方呢他也会发出呢阿贾克斯请求你看在这里边他的访问的路径呢访问的请求方式是flow number directionOK这里边需要三个参数一个是Datas一个是Datas一个是独立访客一个是新独立访客这三个参数呢
[10:34] 应该是对应我们数据库中的三列第一个是什么呢第一个是Data 4Data 4应该是这个地方应该是PV Number而这个地方还有一个叫什么呢还有一个我们来看一下还有一个呢是这个UVS这个UVS是谁呢应该是这个地方的UVS应该是这个UV Number还有一个叫新的UVS应该是New UV Number
[11:03] 也就是这三列应该是对应我们这个地方的三个数组这是三个数组那我们需要做什么事情呢我们需要从数据库中查出来数据把数据转成json然后这个地方它就会给你显示这个地方显示的应该是一个折线图应该是显示一个折线图好了那接下来我们就做这个事情怎么做呢我们回到ID在这里的话呢我这个代码已经给大家写好了首先我们来看控制层
[11:33] 在这个里边呢我们这个地方有个叫flow number direction就是刚才阿贾克斯请求的路径好那在这里的话呢我们在这里我们来调Service层Service层有个get all flow number来我们来找Service层的实现类这个flow number Service mpr而找了之后呢这段代码应该是干什么事情呢它应该是调用我们的持久层持久层呢通过mybattles去
[12:01] 数据库中查询数据把数据的查询出来的所有数据封装到这个集合这个类呢其实是描述我们一张表的一个一个实体类那么这个实体类已经有数据之后呢我通过这个便利把我们这个实体类中的数据呢我们提取出来放到这三个集合为什么要三个集合呢因为我的页面中呢需要三个数组OK然后再把这三个集合的数据呢
[12:31] 给我放到这个对象里边去我们最终返回的应该是这个对象好那我们再看这个Mapper进到这个Mapper里边flow number Mapper好这是一个接口在这个地方有一个flow number Mapper的插面好我们去靠这么一个命令就可以查到查到数据库中对应的表的数据好查到之后呢我们最终的把数据呢返回到这个位置然后呢通过这个注解把它转成json
[13:02] 那最终呢返回一个页面页面呢就能呈现出来一个折线图来我们来看一下我们来热部署一下在这里稍等部署完之后呢我们回到这个页面我们来刷新一下其实你已经看到了这就是所谓的折线图稍等一下那就这个图这个图呢就是从数据库中取出来的你看下面是时间这个地方呢是它对应的一个一个访客你看独立访客
[13:36] OK独立访客还有呢新独立访客等等这些是他对应的数据好那么这个呢其实就是我们如何将呃关系型数据互动的临时结果呢通过呃通过图形化的方式展现出来哎我们这里用的是一架子OK那么关于呢我们的数据的一个展示呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 ECharts 在 Web 应用中动态展示数据图表，涉及前端 JavaScript 代码、后端 Java 控制器与服务层、以及数据映射层的实现。

2) 按时间顺序列出每张画面的要点：
画面 1:
要点：展示 ECharts 初始化代码，配置了标题、工具提示、图例、X 轴、Y 轴和数据系列，数据为数组 [5, 20, 36, 10, 26]，对应类别为 ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]。

画面 2:
要点：展示后端 Java 控制器 IndexController 中的 @RequestMapping("/avgPvNum.action") 方法，用于返回 AvgReturnPojo 对象。

画面 3:
要点：展示前端 JavaScript 代码，用于在数据加载完成后调用 myChart.hideLoading() 方法隐藏加载动画。

画面 4:
要点：展示前端 JavaScript 代码，使用 $.ajax() 发送请求到 "/avgPvNum.action"，并在 success 回调中设置 ECharts 图表的选项，数据源为 data.data 和 data.dates。

画面 5:
要点：展示前端 JavaScript 代码，使用 $.ajax() 发送请求到 "/avgPvNum.action"，并在 success 回调中设置 ECharts 图表的选项，数据源为 data.dates 和 data.data。

画面 6:
要点：展示后端 Java 实体类 AvgPvNumPojo，包含 id、dateStr、avgPvNum 三个私有属性及其对应的 getter 和 setter 方法。

画面 7:
要点：展示后端 Java 返回对象 AvgReturnPojo，包含 dates 和 data 两个 List<String> 类型的私有属性及其对应的 getter 和 setter 方法。

画面 8:
要点：展示后端 Java 控制器 IndexController 中的 @RequestMapping("/avgPvNum.action") 方法，用于返回 AvgReturnPojo 对象。

画面 9:
要点：展示前端页面，显示 ECharts 图表，标题为“ECharts 入门示例”，图表类型为柱状图，数据为 [5, 20, 36, 10, 26]。

画面 10:
要点：展示前端 JavaScript 代码，配置 ECharts 图表的标题、工具提示、图例、数据视图、魔法类型等选项。

画面 11:
要点：展示前端 JavaScript 代码，使用 $.ajax() 发送请求到 "/flowNum.action"，并在 success 回调中设置 ECharts 图表的选项，数据源为 data.dates 和 data.uvs。

画面 12:
要点：展示前端 JavaScript 代码，用于在数据加载完成后调用 myChart4.hideLoading() 方法隐藏加载动画。

画面 13:
要点：展示后端 Java 接口 FlowNumMapper，定义了方法 getAllFlowNum()。

画面 14:
要点：展示后端 Java 控制器 IndexController 中的 @RequestMapping("/flowNum.action") 方法，用于返回 FlowReturnPojo 对象。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```javascript
var mychart = echarts.init(document.getElementById('main'));
var option = {
    title: {
        text: 'ECharts 入门示例'
    },
    tooltip: {},
    legend: {
        data: ['销量']
    },
    xAxis: {
        data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 26]
    }]
};
```

画面 2:
```java
@Controller
public class IndexController {
    @Autowired
    private AvgNumService avgNumService;

    @RequestMapping("/index.action")
    public String skipIndex() { return "index"; }

    @RequestMapping("/avgPvNum.action")
    @ResponseBody
    public AvgReturnPojo getAvgPvNum() {
        AvgReturnPojo returnPojo = avgNumService.getAvgReturnJson();
        return returnPojo;
    }
}
```

画面 3:
```javascript
// 数据加载完成后再调用 hideLoading 方法隐藏加载动画
myChart.hideLoading();
```

画面 4:
```javascript
$.ajax({
    type: "post",
    url: "<%=basePath%>/avgPvNum.action",
    dataType: "json",
    success: function(data) {
        myChart.setOption({
            xAxis: {
                data: data.dates
            },
            series: [{
                // 根据名字对应到相应的系列
                name: 'PV',
                data: data.data
            }]
        });
        // 数据加载完成后再调用 hideLoading 方法隐藏加载动画
        myChart.hideLoading();
    }
});
```

画面 5:
```javascript
$.ajax({
    type: "post",
    url: "<%=basePath%>/avgPvNum.action",
    dataType: "json",
    success: function(data) {
        myChart.setOption({
            xAxis: {
                data: data.dates
            },
            series: [{
                // 根据名字对应到相应的系列
                name: 'PV',
                data: data.data
            }]
        });
    }
});
```

画面 6:
```java
package cn.itcast.weblog.pojo;

public class AvgPvNumPojo {
    private Integer id;
    private String dateStr;
    private String avgPvNum;

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    public String getDateStr() { return dateStr; }
    public void setDateStr(String dateStr) { this.dateStr = dateStr; }
    public String getAvgPvNum() { return avgPvNum; }
    public void setAvgPvNum(String avgPvNum) { this.avgPvNum = avgPvNum; }

    @Override
    public String toString() {
        return "AvgPvNumPojo{" +
                "id=" + id +
                ", dateStr='" + dateStr + '\'' +
                ", avgPvNum='" + avgPvNum + '\'' +
                '}';
    }
}
```

画面 7:
```java
package cn.itcast.weblog.pojo;

import java.util.List;

public class AvgReturnPojo {
    private List<String> dates;
    private List<String> data;

    public List<String> getDates() { return dates; }
    public void setDates(List<String> dates) { this.dates = dates; }
    public List<String> getData() { return data; }
    public void setData(List<String> data) { this.data = data; }

    @Override
    public String toString() {
        return "AvgReturnPojo{" +
                "dates=" + dates +
                ", data=" + data +
                '}';
    }
}
```

画面 8:
```java
@Controller
public class IndexController {
    @Autowired
    private AvgNumService avgNumService;

    @RequestMapping("/index.action")
    public String skipIndex() { return "index"; }

    @RequestMapping("/avgPvNum.action")
    @ResponseBody
    public AvgReturnPojo getAvgPvNum() {
        AvgReturnPojo returnPojo = avgNumService.getAvgReturnJson();
        return returnPojo;
    }
}
```

画面 9:
```html
ECharts 入门示例
```

画面 10:
```javascript
title: {
    text: '近一周访客数量变化趋势',
    subtext: '动态数据'
},
tooltip: {
    trigger: 'axis'
},
legend: {
    data: ['独立访客', '新独立访客']
},
toolbox: {
    show: true,
    feature: {
        mark: {
            show: true
        },
        dataView: {
            show: true,
            readOnly: false
        },
        magicType: {
            show: true
        }
    }
},
```

画面 11:
```javascript
$.ajax({
    type: "post",
    url: "<%=basePath%>/flowNum.action",
    dataType: "json",
    success: function(data) {
        myChart4.setOption({
            xAxis: {
                data: data.dates
            },
            series: [{
                name: '独立访客',
                data: data.uvs
            }, {
                name: '新独立访客',
                data: data.new_uvs
            }]
        });
        myChart4.hideLoading();
    }
});
```

画面 12:
```javascript
// 数据加载完成后再调用 hideLoading 方法隐藏加载动画
myChart4.hideLoading();
```

画面 13:
```java
package cn.itcast.weblog.Mapper;

import java.util.List;

public interface FlowNumMapper {
    List<FlowNumPojo> getAllFlowNum();
}
```

画面 14:
```java
@Controller
public class IndexController {
    @Autowired
    private FlowNumService flowNumService;

    @RequestMapping("/index.action")
    public String skipIndex() { return "index"; }

    @RequestMapping("/avgPvNum.action")
    @ResponseBody
    public AvgReturnPojo getAvgPvNum() {
        AvgReturnPojo returnPojo = avgNumService.getAvgReturnJson();
        return returnPojo;
    }

