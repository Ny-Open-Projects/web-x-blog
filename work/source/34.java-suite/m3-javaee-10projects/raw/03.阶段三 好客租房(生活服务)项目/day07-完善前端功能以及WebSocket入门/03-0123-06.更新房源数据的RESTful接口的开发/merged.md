# 06.更新房源数据的RESTful接口的开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\06.更新房源数据的RESTful接口的开发【海量资源尽在 ubkz.com】.mp4
- 时长 5分45秒（音频 345s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现房源数据更新的这样的功能其实我们去做这个功能呢无非就是想让我们的整个网站的这个功能呢相对会完整一些啊因为呢前面呢我们已经对房源的数据做了一些展现
[00:19] 那么有些时候呢我们需要可能去做一些数据的一些修改然后呢我们来看一下它是否有一些这个变更啊所以说我们需要对房源的数据的一个更新啊做一个这样功能的一个开发啊哎OK那么对于这个房源数据的一个开发这个功能啊其实整体来讲呢应该就是有两个部分啊第一个部分呢就是我们只要在我们的后端
[00:46] 也就是我们的这个rest API这一段啊就是我们这个这个工程下面对吧在这给他去写一个什么呢写一个我们的一个更新的一个接口然后呢我们在页面中的去写我们的一些页面的一些逻辑然后呢去把一些更新后的数据提交到我们的接口就可以完成一个更新啊所以这个功能它的难点或者说它的难度并不是特别大那么
[01:12] 可能对我们后端工程师而言可能它的难度就在于前端的一个页面的一些交互一些修改OK那么在前面我们是没有给出修改页面的所以我们需要去自己去写一个这样的修改页面那我们来看一下它应该怎么去写那么首先我们先来去去把这个更新的这个接口就是我们前面所说的这个rest4
[01:40] 这个接口我们先把它先做出来然后呢我们后面再去做这个页面啊OK那么先把这个接口我们先给它写出来那么我们就参考这个讲义吧因为这个它里面的一些这个逻辑并不复杂对吧我们也没有太多需要去分析的所以呢我们就先把参考这个讲义先把这个功能我们先做好好那么我们首先第一个我们要修改的是一个Controller然后呢在我们的这个来找一下吧
[02:09] 是在下面我们 Controller下面有一个house resource下面 Controller中我们之前有了新增有了查询我们再来给它添加一个叫做update把这个call过来那么要注意的是update我们在这个位置所使用的put请求ok那么我们前面学过rest4应该都知道clud数据clud对应的是不是就是
[02:35] get post put和delete对吧更新我们往往用的都是put作为一个这样的一个请求那么咱们把这个注释这个也拷过来来往这一拷好这个拷过来之后呢这个就修改房源那么我们这个Service里面是不是还没有去实现这个更新这个方法那么我们给他来实现一下那么在这个Service的下面我们来看一下他是怎么实现呢是不是在这个下面Service对吧那么我们把这个直接调用这个
[03:05] 注入的这个Service这个是double的一个服务直接去调用它就可以了但是呢在我们这个double这个服务中啊它是不是也没有去定义这个方法那么OK我们也给它定义出来好那么咱们加一个入室这个叫什么呢更新更新房源更新房源数据好那么现在这个是不是就搞定了这个就搞定了然后呢我们去看它的一个实现类啊我们来找一下
[03:35] 在这个server下面我们找到这个下面的server然后呢我们去找到这个下面的一个实现类实现类呢是在这个下面肯定会报错了对吧因为我们新增了一个方法那么我们把这个方法去给他去做一个实现那么这个里面怎么做呢他呢又要去调入我们的业务的Service去做一个更新把它丢过来然后呢我们在这个业务的这个Service中呢我们再去给他
[04:03] 再去给他去生成这样的一个方法创建一个这个方法OK好那么创建这个方法那么这个创建好这个方法之后它只是一个接口对吧那我们还需要去修改它的一个实现类这个就是更新这个房源更新房源数据那我们来找一下它的一个实现类在这儿那它肯定也会报错然后呢我们去实现它的一个方法把这个更新房源这个方法来实现那么这个里面怎么去做呢
[04:35] 是不是我们就直接去调用我们的super下面的update直接做一个更新就可以了看它的修改的数据条度是不是等于1如果等于1就返回q那就代表的数据修改成功了如果修改的数量就是影响的行数不是等于1那就说明我们修改失败了所以它返回就false那么这就是我们的一个修改的逻辑当然了在这个super下面的update里面它会更新我们的一个update这样的一个
[05:05] 这样的一个字段把这个值会更新成我们当前的一个时间OK好那么这个更新的他是通过这个ID是不是做更新的也就是说我们从前端我们去传递数据到我们的接口的时候一定要有ID才能够去做更新OK好那么这个的话那么我们关于这个服务是不是就
[05:26] REST4这个服务是不是就搞定了那么下面我们需要把我们的double的一个服务重启以及我们的API的服务做重启OK好那么关于我们的更新房源列表的一个REST4的一个接口的一个编写我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现房源数据的更新功能，包括修改Controller、Service及Dubbo服务层的代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT目录，当前章节为“4. 实现更新房源数据”，子章节“4.1.1、修改Controller”，并预览了三个项目文件夹。
画面2：PPT页面显示“4.1.1、修改Controller”，下方展示代码注释“修改房源 @param houseResources json数据 @return”。
画面3：IDE中展示HouseResourcesController类的save方法，包含@PostMapping注解和try-catch异常处理。
画面4：IDE中展示HouseResourcesController类的list方法，包含@GetMapping注解和@RequestParam参数。
画面5：IDE中展示HouseResourcesController类的update方法，包含@PutMapping注解和try-catch异常处理。
画面6：PPT页面显示“4.1.2、修改Service”和“4.1.3、修改dubbo服务”，并展示修改接口和实现类的代码结构。
画面7：PPT页面展示修改接口ApiHouseResourcesService和实现类ApiHouseResourcesServiceImpl的代码结构。
画面8：IDE中展示Dubbo服务端的ApiHouseResourcesServiceImpl类，包含saveHouseResources、queryHouseResourcesList和queryHouseResourcesById方法。
画面9：PPT页面展示修改接口ApiHouseResourcesService和实现类ApiHouseResourcesServiceImpl的代码结构。
画面10：IDE中展示HouseResourcesService接口和实现类的代码结构，包含saveHouseResources、queryHouseResourcesList、queryHouseResourcesById和updateHouseResources方法。
画面11：PPT页面展示修改实现类ApiHouseResourcesServiceImpl的代码，其中update方法调用houseResourcesService的update方法。
画面12：PPT页面展示“4.2、编写EditResource.js”，并展示React代码“import React from 'React'”。
画面13：IDE中展示BaseServiceImpl类，包含update和deleteById方法。
画面14：PPT页面显示“4.1.1、修改Controller”，并展示代码注释“修改房源 @param houseResources json数据 @return”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
@PostMapping
@ResponseBody
public ResponseEntity<Void> save(@RequestBody HouseResources houseResources) {
    try {
        boolean bool = this.houseResourcesService.save(houseResources);
        if (bool) {
            return ResponseEntity.status(HttpStatus.CREATED).build();
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面4：
```java
@GetMapping
@ResponseBody
public ResponseEntity<TableResult> list(HouseResources houseResources,
        @RequestParam(name = "currentPage", defaultValue = "1") Integer currentPage,
        @RequestParam(name = "pageSize", defaultValue = "10") Integer pageSize) {
    return ResponseEntity.ok(this.houseResourcesService.queryList(houseResources, currentPage, pageSize));
}
```

画面5：
```java
@PutMapping
@ResponseBody
public ResponseEntity<Void> update(@RequestBody HouseResources houseResources) {
    try {
        boolean bool = this.houseResourcesService.update(houseResources);
        if (bool) {
            return ResponseEntity.status(HttpStatus.NO_CONTENT).build();
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
}
```

画面6：
```java
public boolean update(HouseResources houseResources) {
    return this.apiHouseResourcesService.updateHouseResources(houseResources);
}
```

画面7：
```java
/**
 * 修改房源
 * @param houseResources
 * @return
 */
boolean updateHouseResources(HouseResources houseResources);
```

画面8：
```java
@Service(version = "1.0.0")
public class ApiHouseResourcesServiceImpl implements ApiHouseResourcesService {

    @Autowired
    private HouseResourcesService houseResourcesService;

    @Override
    public int saveHouseResources(HouseResources houseResources) {
        return this.houseResourcesService.saveHouseResources(houseResources);
    }

    @Override
    public PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize) {
        return this.houseResourcesService.queryHouseResourcesList(page, pageSize);
    }

    @Override
    public HouseResources queryHouseResourcesById(Long id) {
        return this.houseResourcesService.queryHouseResourcesById(id);
    }
}
```

画面10：
```java
int saveHouseResources(HouseResources houseResources);
PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize);
HouseResources queryHouseResourcesById(Long id);
boolean updateHouseResources(HouseResources houseResources);
```

画面11：
```java
@Override
public boolean updateHouseResources(HouseResources houseResources) {
    return this.houseResourcesService.updateHouseResources(houseResources);
}
```

画面12：
```javascript
import React from 'React';
```

画面13：
```java
/**
 * 更新数据
 * @param record
 * @return
 */
public Integer update(T record) {
    record.setUpdated(new Date());
    return this.Mapper.updateById(record);
}

/**
 * 根据id删除数据
 * @param id
 * @return
 */
public Integer deleteById(Long id) { return this.Mapper.deleteById(id); }
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“4. 实现更新房源数据”，子标题“4.1.1、修改Controller”。
画面2：PPT标题“4.1.1、修改Controller”，下方代码注释“修改房源 @param houseResources json数据 @return”。
画面6：PPT标题“4.1.2、修改Service”和“4.1.3、修改dubbo服务”，下方展示修改接口和实现类的代码结构。
画面7：PPT标题“修改接口 ApiHouseResourcesService”和“修改实现类 ApiHouseResourcesServiceImpl”和“修改业务Service : HouseResourcesServiceImpl”。
画面12：PPT标题“4.2、编写EditResource.js”，下方展示React代码“import React from 'React'”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

