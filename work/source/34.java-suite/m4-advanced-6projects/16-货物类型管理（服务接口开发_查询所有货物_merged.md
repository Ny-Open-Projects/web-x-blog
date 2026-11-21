# 16-货物类型管理（服务接口开发_查询所有货物 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是已经实现了我们根据ID查询货物类型这个服务接口。

接下来呢,我们下一个,来看下一个,下一个的话是查询所有货物类型。

但是在这呢,我们需要注意啊,所谓所有货物类型,其实也并不是说我们所有的这个货物类型表中所有的记录都要查出来。

是因为什么呢?我们还记得吧,在咱们这个货物类型啊,这个实体里边,是不是定义的有这么一个,来找一下,货物类型,PT,对吧?

在这个货物类型实体类里边呢,我们其实定义了这么一个属性叫做status,对吧?

status,它代表的是状态,是否是禁用的,对吧?

那么我们查询所有货物类型了,其实只是查什么呢?

只是查它这个状态是1的,也就是正常的这种。

对于状态是0的这种呢,我们其实也不需要查出来。

所以说呢,这个地方我们需要注意啊,就是所有货物类型其实并不是真正的所有记录,而是状态是正常的,对吧?

所以我们需要通过status去查,那个状态位去查。

然后还有一点呢,就是什么呢?

我们这个地方呢,查询货物类型的时候呢,就不再去查询关联的那个什么呢?

像我们刚才根据ID查询的时候,是不是还要查询关联的信息,对吧?

关联的车辆类型ID。

这个地方呢,我们就不再去查询关联的那个什么呢?

就不需要查了,只是查货物类型基本信息。

所以相对来说呢,其实反而会更简单一点。

那接下来呢,我们就来创建这个方法。

这个方法名呢,就叫findall就可以了,跟我们的讲义保持一致,就是这个。

好,那么接下来我们来创建一下这个方法。

public,然后返回值呢,肯定是一个例子的集合,对吧?

然后呢,这个还是我们的DTO对象,就是goost type DTO对象。

然后方法名叫做findall。

因为是查询所有啊。

所以说就不需要传参数了。

包括那个status也不用传过来。

因为我们已经指定死了,对吧?

0就表示禁用,1表示正常使用。

所以说呢,并不需要通过参数传过来。

然后呢,同样还是这儿先return一个null,保证它不报错。

然后呢,在这儿呢,来加一个getmyping,对吧?

然后呢,看一下我们这个接口是怎么定义的啊。

就叫all,对吧?

然后呢,再别忘了加一个api operation吧。

然后呢,来一个value。

等于什么呢?

这个是查询所有啊。

查询所有货物类型。

咱们现在写的呢,都是一些基本的增生改查啊。

主要是给我们这个前端来使用的。

当然了,我们前面也提到过啊,前端呢,不会直接调我们这个PDBase。

而是直接调到什么呢?

我们这个PDWeb这里边,对吧?

然后呢,通过PDWeb,然后呢,再调我们这个PDBase。

所以我们这个PDBase呢,它其实是在后端的,对吧?

那么一层一层调过来。

那么这儿呢,我们都是一些基础的增生改查的方法。

这个就是查询所有货物类型。

把这注释加一下。

然后呢,我们在这儿呢,肯定就要调service了,对吧?

调service。

来看一下我们这个service还是这个,对吧?

这个service,点。

咱们就叫final吧,final。

当然了,现在我们这个service里面还没有这个方法,对吧?

对吧?

所以我们需要去干什么呢?

去这个扩展一下。

然后返回值呢,我们先来指定一下。

返回值的话呢,它这个地方肯定是这个PDGooseType吧。

货物类型。

是这么一个粒子的集合。

因为我们这儿呢,它直接面对的,后边是面对的数据库啊。

所以我们最终查出来的呢,其实是这么一个实体对象。

它是跟我们这个表是不是有映射关系的。

只不过呢,我们查完之后呢,需要把这个粒子的集合重新处理一下。

然后呢,封装成这种DTO对象,对吧?

而我们真正传输,传输的是DTO对象。

基本上全都是这种套路啊。

好,那接下来呢,我们需要先把这个方法是不是来扩展一下。

这个是查询所有货物类型。

好,把这个方法扩展好。

然后呢,先回到咱们controller,回到controller这边,对吧?

那这样的话,比如说我们现在这个list呢,已经查好了。

对吧?

这个就是我们的。

goose type list。

这个list已经查好了。

那么查好了之后呢,接下来需要做什么事呢?

咱们是不是需要把它处理一下?

因为我们现在最终要返回的是不是DTO对象啊?

把它封装成集合。

所以说呢,我们需要把这个list呢,进行一个处理。

还是啊,先来判断一下。

if什么呢,goose type list不等于空。

同时什么呢,goose type list.size。

.size。

好。

大于0,对吧?

这个时候呢,我们就可以进一步处理了。

怎么处理呢?其实非常简单。

还是使用我们这个stream流。

点stream,对吧?

然后呢,点map。

好。

然后呢,每一个呢,其实就是一个goose type。

对象。

就是这么一个对象。

这儿怎么处理呢?

咱们是不是需要把它怎么做?

把它是不是给它封装成我们的这个DTO对象啊?

其实你仔细看的话,

我们这个DTO对象这里边的属性啊,其实跟我们这块实体类这些属性呢,都是一一对应的。

对吧?

都是一一对应的。

所以我们在这个地方呢,直接通过一个属性拷贝是不是就可以。

当然我们先把这个DTO对象呢,先NU出来啊。

先把DTO对象NU出来。

goose type DTO,NU一个。

goose type DTO。

先把它NU出来,然后呢,使用bin utils,对吧?

然后呢,把它来copy一下。

然后呢,goose type,应该是我们这个goose type,对吧?

这是原。

目标呢,就是这个DTO。

是不是给它拷好。

拷好之后呢,别忘了return啊。

return我们这个goose type DTO。

把它返回。

然后呢,注意还没完啊,咱们刚才写的这一堆代码,其实只是这一块。

它是一个整体的吧。

整个我选中的这一块呢,这就是我们这个这个Lambda表达式。

然后呢,弄好之后呢,需要给它collect一下。

收集为我们的集合。

集合,对吧?

collectors.toList。

这样的话呢,就能得到我们想要的这个集合了。

这就是我们这个goose type DTO,封装好的这么一个集合。

这个list。

然后呢,把它返回就可以了。

goose type。

OK。

那么到这儿的话呢,咱们control了这个方法呢,其实就已经这个写好了。

对吧?就已经写好了。

那么接下来呢,我们要做的呢,是不是就是需要把咱们这个findout,

这个方法呢,给它实现了。

对吧?把这个方法实现了。

因为我们现在呢,只是在这个接口里边扩展了这个方法。

所以接下来呢,我们需要找到它的实现类。

你看它这边是不是又报错了。

我们需要去实现这个findout这个方法。

那这个实现起来呢,其实也是比较简单的。

我们就使用一个简单的Lambda query对象,是不是就可以封装这个参数。

因为我们刚才提到,我们这个地方呢,要查询是所有的,对吧?

查询所有的。

对吧?

我们要的这个查询所有货物类型。

货物类型。

其实呢,我们需要给它加一个条件,就是那个Status。

对吧?所以我们在这儿呢,需要来封装一下。

我们封装成一个叫做query,querywrapper。

好,就这个,对吧?querywrapper。

然后呢,这个范型的话,需要来指定一下。

这个范型的话呢,其实就是我们这个PDGhostType,对吧?

好,然后querywrapper等于new一个,直接new就可以了。

好,把它new出来。

new出来之后呢,我们来添加一个条件。

添加过滤条件,对吧?

添加条件。

根据什么呢?

根据我们的这个Status,对吧?

Status来查询。

好,那么我们在这儿呢,就可以直接通过wrapper,querywrapper点什么呢?

这个也是个等值的,对吧?

所以也是个equal,一个查询。

第一个呢,是我们的这个参数,condition。

那么在这儿我们就可以写Status,对吧?

然后呢,

我们在后边写个1。

1,我们是不是已经定死了?

因为我们在这里边已经定死了。

1代表的是正常,0代表的是禁用。

所以我们直接写1就可以了。

好,这样我们这个条件就已经封存好了。

封存好之后呢,直接return什么呢?

basewrapper点什么呢?

select list。

然后呢,把我们这个querywrapper对象,条件对象传进去就可以了。

只有这么一个条件。

所以整个代码写起来呢,其实还是比较简单的。

这是根据,这是查询所有货物类型。

好,那么一会儿呢,我们来测试一下就可以了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达达TMS”的Java Spring Boot项目中，实现“货物类型”数据增删改查功能的教学演示。讲师通过IntelliJ IDEA开发环境，逐步讲解了如何在Controller层调用Service层，以及如何在Service层使用MyBatis-Plus的`QueryWrapper`进行数据库查询。核心内容包括：
- **功能目标**：实现“查询所有货物类型”和“新增货物类型”两个接口。
- **技术栈**：Spring Boot + MyBatis-Plus + Java 8 Stream API。
- **核心操作**：
  1. 在`GoodsTypeController`中定义`@GetMapping("/all")`方法。
  2. 在`IPdGoodsTypeService`接口中声明`findAll()`方法。
  3. 在`PdGoodsTypeServiceImpl`中实现`findAll()`方法，使用`QueryWrapper`构建查询条件。
  4. 在`GoodsTypeController`中，通过`Stream` API将数据库查询结果转换为DTO对象列表。
  5. 在`saveGoodsType`方法中，演示了如何使用`idGenerator`生成主键并保存实体。
- **关键点**：讲师强调了`@ApiModelProperty`注解用于API文档，以及`BeanUtils.copyProperties`用于对象属性复制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：视频开场，展示项目结构和当前正在编辑的`GoodsTypeController.java`文件，讲师介绍本节将实现“查询所有货物类型”功能。
*   **00:05 - 00:15**：讲师在`GoodsTypeController`中编写`@GetMapping("/all")`方法的框架，并注释说明其功能。
*   **00:15 - 00:25**：讲师在`GoodsTypeController`中编写`findAll()`方法的主体，调用`goodsTypeService.findAll()`。
*   **00:25 - 00:35**：讲师在`GoodsTypeController`中添加`if`判断，检查`goodsTypeList`是否非空，若为空则返回`null`。
*   **00:35 - 00:45**：讲师在`GoodsTypeController`中使用`Stream` API对`goodsTypeList`进行转换，创建`GoodsTypeDto`对象并调用`BeanUtils.copyProperties`进行属性复制。
*   **00:45 - 00:55**：讲师在`GoodsTypeController`中调用`Collectors.toList()`将流转换为列表，并返回。
*   **00:55 - 01:05**：讲师切换到`PdGoodsTypeServiceImpl.java`文件，演示如何实现`findAll()`方法。
*   **01:05 - 01:15**：讲师在`PdGoodsTypeServiceImpl.java`中创建`QueryWrapper`对象，并设置查询条件`eq("status", 1)`。
*   **01:15 - 01:25**：讲师在`PdGoodsTypeServiceImpl.java`中调用`baseMapper.selectList(wrapper)`执行查询。
*   **01:25 - 01:35**：讲师切换到`GoodsTypeController.java`，演示如何在`saveGoodsType`方法中使用`idGenerator`生成主键。
*   **01:35 - 01:45**：讲师在`GoodsTypeController.java`中演示如何将`truckTypeIds`列表中的ID赋值给`goodsTypeDto`对象。
*   **01:45 - 01:55**：讲师在`GoodsTypeController.java`中完成`saveGoodsType`方法的编写，包括保存货物类型和关联的车辆类型。
*   **01:55 - 02:05**：讲师在`GoodsTypeController.java`中完成`findAll()`方法的编写，包括`Stream`转换和`BeanUtils.copyProperties`调用。
*   **02:05 - 02:15**：讲师在`GoodsTypeController.java`中完成`findAll()`方法的编写，包括`Collectors.toList()`调用和返回。
*   **02:15 - 02:25**：讲师在`GoodsTypeController.java`中完成`findAll()`方法的编写，包括`return null;`语句。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**：
    *   无明确的PPT或图表展示，主要通过IDE界面和代码高亮进行教学。
*   **公式**：
    *   无数学公式。
*   **代码**：
    *   **`GoodsTypeController.java` - `findAll()` 方法**：
        ```java
        @GetMapping("/all")
        @ApiOperation(value = "查询所有货物类型")
        public List<GoodsTypeDto> findAll() {
            List<PdGoodsType> goodsTypeList = goodsTypeService.findAll();
            if (goodsTypeList != null && goodsTypeList.size() > 0) {
                return goodsTypeList.stream().map(goodsType -> {
                    GoodsTypeDto goodsTypeDto = new GoodsTypeDto();
                    BeanUtils.copyProperties(goodsType, goodsTypeDto);
                    return goodsTypeDto;
                }).collect(Collectors.toList());
            }
            return null;
        }
        ```
    *   **`GoodsTypeController.java` - `saveGoodsType()` 方法**：
        ```java
        @PostMapping("/add")
        @ApiOperation(value = "添加货物类型")
        public GoodsTypeDto saveGoodsType(@RequestBody PdGoodsTypeDto pdGoodsTypeDto) {
            PdGoodsType pdGoodsType = new PdGoodsType();
            BeanUtils.copyProperties(pdGoodsTypeDto, pdGoodsType);
            pdGoodsTypeService.saveGoodsType(pdGoodsType);
            String goodsTypeId = pdGoodsType.getId();
            List<String> truckTypeIds = pdGoodsType.getTruckTypeIds();
            // 保存车辆类型关联
            if (truckTypeIds != null && truckTypeIds.size() > 0) {
                for (String truckTypeId : truckTypeIds) {
                    PdTruckTypeGoodsType pdTruckTypeGoodsType = new PdTruckTypeGoodsType();
                    pdTruckTypeGoodsType.setGoodsTypeId(goodsTypeId);
                    pdTruckTypeGoodsType.setTruckTypeId(truckTypeId);
                    pdTruckTypeGoodsTypeService.save(pdTruckTypeGoodsType);
                }
            }
            return pdGoodsTypeDto;
        }
        ```
    *   **`PdGoodsTypeServiceImpl.java` - `findAll()` 方法**：
        ```java
        @Override
        public List<PdGoodsType> findAll() {
            QueryWrapper<PdGoodsType> wrapper = new QueryWrapper<>();
            wrapper.eq("status", 1);
            return baseMapper.selectList(wrapper);
        }
        ```
    *   **`PdGoodsTypeServiceImpl.java` - `saveGoodsType()` 方法**：
        ```java
        @Override
        public PdGoodsType saveGoodsType(PdGoodsType pdGoodsType) {
            pdGoodsType.setId(idGenerator.nextId(pdGoodsType) + "");
            baseMapper.insert(pdGoodsType);
            return pdGoodsType;
        }
        ```
    *   **`GoodsTypeDto.java` 类**：
        ```java
        @Data
        public class GoodsTypeDto implements Serializable {
            private static final long serialVersionUID = -6890776123674482761L;
            @ApiModelProperty("主键")
            private String id;
            @ApiModelProperty("物品类型名称")
            private String name;
            @ApiModelProperty("默认重量，单位：千克")
            private Double weight;
        }
        ```
    *   **`PdGoodsType.java` 类**：
        ```java
        @TableName("pd_goods_type")
        public class PdGoodsType implements Serializable {
            private static final long serialVersionUID = 1L;
            @TableId(value = "id", type = IdType.INPUT)
            private String id;
            @TableField("name")
            private String name;
            @TableField("weight")
            private Double weight;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建查询接口**
    *   **描述**：讲师在`GoodsTypeController`中创建`@GetMapping("/all")`方法，并使用`@ApiOperation`注解描述其功能。
*   **场景二：调用Service层**
    *   **描述**：讲师在`GoodsTypeController`中编写`findAll()`方法，通过`goodsTypeService.findAll()`调用Service层进行数据查询。
*   **场景三：处理查询结果**
    *   **描述**：讲师在`GoodsTypeController`中添加`if`判断，检查查询结果是否为空，若为空则返回`null`。
*   **场景四：使用Stream API转换数据**
    *   **描述**：讲师在`GoodsTypeController`中使用`Stream` API对查询结果进行转换，创建`GoodsTypeDto`对象并调用`BeanUtils.copyProperties`
