# 笔试题库 · Spring（知识点 110 条）

**Qspring-1000（单选·正向·作用域）** 关于「IoC」的说法，正确的是？
- A. Spring 单例是 JVM 全局唯一
- B. Spring Bean 默认作用域是 singleton 单例容器内唯一
- C. 默认作用域是 prototype
- D. singleton 与 GoF 单例模式相同
**答案：B**
**解析：** Spring Bean 默认作用域是 singleton 单例容器内唯一。原因：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）。
**来源：** SP-001 · IoC（Spring 文档）

**Qspring-1001（判断·作用域）** Spring Bean 默认作用域是 singleton 单例容器内唯一
**答案：对。** 解析：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）

**Qspring-1002（判断·作用域）** Spring 单例是 JVM 全局唯一
**答案：错。** 正确表述：Spring Bean 默认作用域是 singleton 单例容器内唯一。原因：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）

**Qspring-1003（判断·作用域）** 默认作用域是 prototype
**答案：错。** 正确表述：Spring Bean 默认作用域是 singleton 单例容器内唯一。原因：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）

**Qspring-1004（判断·作用域）** singleton 与 GoF 单例模式相同
**答案：错。** 正确表述：Spring Bean 默认作用域是 singleton 单例容器内唯一。原因：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）

**Qspring-1005（场景单选·作用域）** 在工程实践中关于「singleton」，下列做法符合推荐实践的是？
- A. singleton 与 GoF 单例模式相同
- B. 默认作用域是 prototype
- C. Spring 单例是 JVM 全局唯一
- D. 回答作用域题先说默认值
**答案：D**
**解析：** 推荐实践：回答作用域题先说默认值。事实依据：Spring Bean 默认作用域是 singleton 单例容器内唯一。

**Qspring-1006（场景判断·作用域）** 推荐实践：回答作用域题先说默认值
**答案：对。** 解析：Spring Bean 默认作用域是 singleton 单例容器内唯一。原因：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）

**Qspring-1007（填空·作用域）** Spring Bean 默认作用域是 ______ 单例容器内唯一
**答案：singleton**。解析：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）

**Qspring-1008（简答·作用域）** 请说明「IoC」中singleton的机制与使用要点。
**要点（标准答案）**：① Spring Bean 默认作用域是 singleton 单例容器内唯一；② 原理：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）；③ 使用要点：回答作用域题先说默认值。版本锚点：Spring 文档。

**Qspring-1009（单选·正向·流程）** 关于「Bean 生命周期」的说法，正确的是？
- A. Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁
- B. Aware 回调在属性填充之前
- C. 实例化与初始化是同一件事
- D. 销毁回调在容器刷新时执行
**答案：A**
**解析：** Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁。原因：实例化（构造）与初始化（init 回调）是两个阶段，属性填充在两者之间，记住主线再展开细节。
**来源：** SP-002 · Bean 生命周期（Spring 源码 doCreateBean）

**Qspring-1010（判断·流程）** Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁
**答案：对。** 解析：实例化（构造）与初始化（init 回调）是两个阶段，属性填充在两者之间，记住主线再展开细节

**Qspring-1011（判断·流程）** 实例化与初始化是同一件事
**答案：错。** 正确表述：Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁。原因：实例化（构造）与初始化（init 回调）是两个阶段，属性填充在两者之间，记住主线再展开细节

**Qspring-1012（判断·流程）** Aware 回调在属性填充之前
**答案：错。** 正确表述：Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁。原因：实例化（构造）与初始化（init 回调）是两个阶段，属性填充在两者之间，记住主线再展开细节

**Qspring-1013（判断·流程）** 销毁回调在容器刷新时执行
**答案：错。** 正确表述：Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁。原因：实例化（构造）与初始化（init 回调）是两个阶段，属性填充在两者之间，记住主线再展开细节

**Qspring-1014（场景单选·流程）** 在工程实践中关于「属性填充」，下列做法符合推荐实践的是？
- A. Aware 回调在属性填充之前
- B. 销毁回调在容器刷新时执行
- C. 背生命周期按七步主线
- D. 实例化与初始化是同一件事
**答案：C**
**解析：** 推荐实践：背生命周期按七步主线。事实依据：Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁。

**Qspring-1015（场景判断·流程）** 推荐实践：背生命周期按七步主线
**答案：对。** 解析：Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁。原因：实例化（构造）与初始化（init 回调）是两个阶段，属性填充在两者之间，记住主线再展开细节

**Qspring-1016（填空·流程）** Bean 生命周期主线：实例化、______、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁
**答案：属性填充**。解析：实例化（构造）与初始化（init 回调）是两个阶段，属性填充在两者之间，记住主线再展开细节

**Qspring-1017（简答·流程）** 请说明「Bean 生命周期」中属性填充的机制与使用要点。
**要点（标准答案）**：① Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁；② 原理：实例化（构造）与初始化（init 回调）是两个阶段，属性填充在两者之间，记住主线再展开细节；③ 使用要点：背生命周期按七步主线。版本锚点：Spring 源码 doCreateBean。

**Qspring-1018（单选·正向·扩展点）** 关于「Bean 生命周期」的说法，正确的是？
- A. BeanPostProcessor 在初始化前后对每个 Bean 加工
- B. BeanPostProcessor 只处理一次
- C. BPP 不能修改 Bean
- D. BPP 前后处理都在初始化之后
**答案：A**
**解析：** BeanPostProcessor 在初始化前后对每个 Bean 加工。原因：postProcessBeforeInitialization 在 init 回调前、After 在之后，AOP 代理、@Autowired 填充、@PostConstruct 全靠它实现。
**来源：** SP-003 · Bean 生命周期（Spring 源码）

**Qspring-1019（判断·扩展点）** BeanPostProcessor 在初始化前后对每个 Bean 加工
**答案：对。** 解析：postProcessBeforeInitialization 在 init 回调前、After 在之后，AOP 代理、@Autowired 填充、@PostConstruct 全靠它实现

**Qspring-1020（判断·扩展点）** BeanPostProcessor 只处理一次
**答案：错。** 正确表述：BeanPostProcessor 在初始化前后对每个 Bean 加工。原因：postProcessBeforeInitialization 在 init 回调前、After 在之后，AOP 代理、@Autowired 填充、@PostConstruct 全靠它实现

**Qspring-1021（判断·扩展点）** BPP 前后处理都在初始化之后
**答案：错。** 正确表述：BeanPostProcessor 在初始化前后对每个 Bean 加工。原因：postProcessBeforeInitialization 在 init 回调前、After 在之后，AOP 代理、@Autowired 填充、@PostConstruct 全靠它实现

**Qspring-1022（判断·扩展点）** BPP 不能修改 Bean
**答案：错。** 正确表述：BeanPostProcessor 在初始化前后对每个 Bean 加工。原因：postProcessBeforeInitialization 在 init 回调前、After 在之后，AOP 代理、@Autowired 填充、@PostConstruct 全靠它实现

**Qspring-1023（场景单选·扩展点）** 在工程实践中关于「BeanPostProcessor」，下列做法符合推荐实践的是？
- A. BPP 前后处理都在初始化之后
- B. BeanPostProcessor 只处理一次
- C. Spring 扩展机制核心，插件体系的基石
- D. BPP 不能修改 Bean
**答案：C**
**解析：** 推荐实践：Spring 扩展机制核心，插件体系的基石。事实依据：BeanPostProcessor 在初始化前后对每个 Bean 加工。

**Qspring-1024（场景判断·扩展点）** 推荐实践：Spring 扩展机制核心，插件体系的基石
**答案：对。** 解析：BeanPostProcessor 在初始化前后对每个 Bean 加工。原因：postProcessBeforeInitialization 在 init 回调前、After 在之后，AOP 代理、@Autowired 填充、@PostConstruct 全靠它实现

**Qspring-1025（填空·扩展点）** ______ 在初始化前后对每个 Bean 加工
**答案：BeanPostProcessor**。解析：postProcessBeforeInitialization 在 init 回调前、After 在之后，AOP 代理、@Autowired 填充、@PostConstruct 全靠它实现

**Qspring-1026（简答·扩展点）** 请说明「Bean 生命周期」中BeanPostProcessor的机制与使用要点。
**要点（标准答案）**：① BeanPostProcessor 在初始化前后对每个 Bean 加工；② 原理：postProcessBeforeInitialization 在 init 回调前、After 在之后，AOP 代理、@Autowired 填充、@PostConstruct 全靠它实现；③ 使用要点：Spring 扩展机制核心，插件体系的基石。版本锚点：Spring 源码。

**Qspring-1027（单选·正向·时机）** 关于「AOP」的说法，正确的是？
- A. AOP 代理在 postProcessBeforeInitialization 创建
- B. 代理在属性填充阶段创建
- C. AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建
- D. 代理在实例化阶段创建
**答案：C**
**解析：** AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建。原因：AbstractAutoProxyCreator.wrapIfNecessary 在 After 阶段判断切点匹配生成代理（本项目源码级核对结论），代理创建晚于 init 回调。
**来源：** SP-004 · AOP（AbstractAutoProxyCreator）

**Qspring-1028（判断·时机）** AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建
**答案：对。** 解析：AbstractAutoProxyCreator.wrapIfNecessary 在 After 阶段判断切点匹配生成代理（本项目源码级核对结论），代理创建晚于 init 回调

**Qspring-1029（判断·时机）** AOP 代理在 postProcessBeforeInitialization 创建
**答案：错。** 正确表述：AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建。原因：AbstractAutoProxyCreator.wrapIfNecessary 在 After 阶段判断切点匹配生成代理（本项目源码级核对结论），代理创建晚于 init 回调

**Qspring-1030（判断·时机）** 代理在实例化阶段创建
**答案：错。** 正确表述：AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建。原因：AbstractAutoProxyCreator.wrapIfNecessary 在 After 阶段判断切点匹配生成代理（本项目源码级核对结论），代理创建晚于 init 回调

**Qspring-1031（判断·时机）** 代理在属性填充阶段创建
**答案：错。** 正确表述：AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建。原因：AbstractAutoProxyCreator.wrapIfNecessary 在 After 阶段判断切点匹配生成代理（本项目源码级核对结论），代理创建晚于 init 回调

**Qspring-1032（场景单选·时机）** 在工程实践中关于「wrapIfNecessary」，下列做法符合推荐实践的是？
- A. 代理在实例化阶段创建
- B. 代理在属性填充阶段创建
- C. 回答"AOP 代理何时创建"的精确版本
- D. AOP 代理在 postProcessBeforeInitialization 创建
**答案：C**
**解析：** 推荐实践：回答"AOP 代理何时创建"的精确版本。事实依据：AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建。

**Qspring-1033（场景判断·时机）** 推荐实践：回答"AOP 代理何时创建"的精确版本
**答案：对。** 解析：AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建。原因：AbstractAutoProxyCreator.wrapIfNecessary 在 After 阶段判断切点匹配生成代理（本项目源码级核对结论），代理创建晚于 init 回调

**Qspring-1034（简答·时机）** 请说明「AOP」中wrapIfNecessary的机制与使用要点。
**要点（标准答案）**：① AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建；② 原理：AbstractAutoProxyCreator.wrapIfNecessary 在 After 阶段判断切点匹配生成代理（本项目源码级核对结论），代理创建晚于 init 回调；③ 使用要点：回答"AOP 代理何时创建"的精确版本。版本锚点：AbstractAutoProxyCreator。

**Qspring-1035（单选·正向·顺序）** 关于「Bean 生命周期」的说法，正确的是？
- A. init-method 先于 afterPropertiesSet
- B. @PostConstruct 在初始化之后执行
- C. 三个回调互斥只能选一个
- D. 初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method
**答案：D**
**解析：** 初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method。原因：注解最早（由 BPP 调用）、接口次之、XML/bean 方法最后，三者可同时存在按序执行。
**来源：** SP-005 · Bean 生命周期（Spring 文档）

**Qspring-1036（判断·顺序）** 初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method
**答案：对。** 解析：注解最早（由 BPP 调用）、接口次之、XML/bean 方法最后，三者可同时存在按序执行

**Qspring-1037（判断·顺序）** init-method 先于 afterPropertiesSet
**答案：错。** 正确表述：初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method。原因：注解最早（由 BPP 调用）、接口次之、XML/bean 方法最后，三者可同时存在按序执行

**Qspring-1038（判断·顺序）** @PostConstruct 在初始化之后执行
**答案：错。** 正确表述：初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method。原因：注解最早（由 BPP 调用）、接口次之、XML/bean 方法最后，三者可同时存在按序执行

**Qspring-1039（判断·顺序）** 三个回调互斥只能选一个
**答案：错。** 正确表述：初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method。原因：注解最早（由 BPP 调用）、接口次之、XML/bean 方法最后，三者可同时存在按序执行

**Qspring-1040（场景单选·顺序）** 在工程实践中关于「afterPropertiesSet」，下列做法符合推荐实践的是？
- A. @PostConstruct 在初始化之后执行
- B. 三个回调互斥只能选一个
- C. init-method 先于 afterPropertiesSet
- D. 初始化逻辑拆层时按此顺序安排
**答案：D**
**解析：** 推荐实践：初始化逻辑拆层时按此顺序安排。事实依据：初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method。

**Qspring-1041（场景判断·顺序）** 推荐实践：初始化逻辑拆层时按此顺序安排
**答案：对。** 解析：初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method。原因：注解最早（由 BPP 调用）、接口次之、XML/bean 方法最后，三者可同时存在按序执行

**Qspring-1042（填空·顺序）** 初始化回调顺序：@PostConstruct、InitializingBean.______、init-method
**答案：afterPropertiesSet**。解析：注解最早（由 BPP 调用）、接口次之、XML/bean 方法最后，三者可同时存在按序执行

**Qspring-1043（简答·顺序）** 请说明「Bean 生命周期」中afterPropertiesSet的机制与使用要点。
**要点（标准答案）**：① 初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method；② 原理：注解最早（由 BPP 调用）、接口次之、XML/bean 方法最后，三者可同时存在按序执行；③ 使用要点：初始化逻辑拆层时按此顺序安排。版本锚点：Spring 文档。

**Qspring-1044（单选·正向·注解）** 关于「Bean 生命周期」的说法，正确的是？
- A. @PostConstruct 在依赖注入前执行
- B. @PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用
- C. @PostConstruct 可以带参数
- D. @PostConstruct 由反射直接调用与 BPP 无关
**答案：B**
**解析：** @PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用。原因：JSR-250 注解，Spring 用 BPP 桥接实现，依赖注入完成后才执行。
**来源：** SP-006 · Bean 生命周期（JSR-250）

**Qspring-1045（判断·注解）** @PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用
**答案：对。** 解析：JSR-250 注解，Spring 用 BPP 桥接实现，依赖注入完成后才执行

**Qspring-1046（判断·注解）** @PostConstruct 在依赖注入前执行
**答案：错。** 正确表述：@PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用。原因：JSR-250 注解，Spring 用 BPP 桥接实现，依赖注入完成后才执行

**Qspring-1047（判断·注解）** @PostConstruct 由反射直接调用与 BPP 无关
**答案：错。** 正确表述：@PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用。原因：JSR-250 注解，Spring 用 BPP 桥接实现，依赖注入完成后才执行

**Qspring-1048（判断·注解）** @PostConstruct 可以带参数
**答案：错。** 正确表述：@PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用。原因：JSR-250 注解，Spring 用 BPP 桥接实现，依赖注入完成后才执行

**Qspring-1049（场景单选·注解）** 在工程实践中关于「@PostConstruct」，下列做法符合推荐实践的是？
- A. @PostConstruct 在依赖注入前执行
- B. @PostConstruct 可以带参数
- C. 初始化钩子首选注解方式
- D. @PostConstruct 由反射直接调用与 BPP 无关
**答案：C**
**解析：** 推荐实践：初始化钩子首选注解方式。事实依据：@PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用。

**Qspring-1050（场景判断·注解）** 推荐实践：初始化钩子首选注解方式
**答案：对。** 解析：@PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用。原因：JSR-250 注解，Spring 用 BPP 桥接实现，依赖注入完成后才执行

**Qspring-1051（填空·注解）** ______ 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用
**答案：@PostConstruct**。解析：JSR-250 注解，Spring 用 BPP 桥接实现，依赖注入完成后才执行

**Qspring-1052（简答·注解）** 请说明「Bean 生命周期」中@PostConstruct的机制与使用要点。
**要点（标准答案）**：① @PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用；② 原理：JSR-250 注解，Spring 用 BPP 桥接实现，依赖注入完成后才执行；③ 使用要点：初始化钩子首选注解方式。版本锚点：JSR-250。

**Qspring-1053（单选·正向·三级缓存）** 关于「循环依赖」的说法，正确的是？
- A. 三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂
- B. 三级缓存顺序是工厂、早期、成品
- C. 三级缓存都是存 Bean 实例的
- D. 一级缓存存 ObjectFactory
**答案：A**
**解析：** 三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。原因：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory。
**来源：** SP-007 · 循环依赖（Spring 源码）

**Qspring-1054（判断·三级缓存）** 三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂
**答案：对。** 解析：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory

**Qspring-1055（判断·三级缓存）** 三级缓存都是存 Bean 实例的
**答案：错。** 正确表述：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。原因：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory

**Qspring-1056（判断·三级缓存）** 三级缓存顺序是工厂、早期、成品
**答案：错。** 正确表述：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。原因：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory

**Qspring-1057（判断·三级缓存）** 一级缓存存 ObjectFactory
**答案：错。** 正确表述：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。原因：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory

**Qspring-1058（场景单选·三级缓存）** 在工程实践中关于「singletonObjects」，下列做法符合推荐实践的是？
- A. 三级缓存都是存 Bean 实例的
- B. 背三级缓存必背各级名称与职责
- C. 一级缓存存 ObjectFactory
- D. 三级缓存顺序是工厂、早期、成品
**答案：B**
**解析：** 推荐实践：背三级缓存必背各级名称与职责。事实依据：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。

**Qspring-1059（场景判断·三级缓存）** 推荐实践：背三级缓存必背各级名称与职责
**答案：对。** 解析：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。原因：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory

**Qspring-1060（填空·三级缓存）** 三级缓存：______ 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂
**答案：singletonObjects**。解析：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory

**Qspring-1061（简答·三级缓存）** 请说明「循环依赖」中singletonObjects的机制与使用要点。
**要点（标准答案）**：① 三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂；② 原理：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory；③ 使用要点：背三级缓存必背各级名称与职责。版本锚点：Spring 源码。

**Qspring-1062（单选·正向·原理）** 关于「循环依赖」的说法，正确的是？
- A. AOP 循环依赖靠二级缓存就够
- B. 三级缓存存在的意义是让 AOP 场景能提前拿到代理引用
- C. 三级缓存是为了性能优化
- D. 只有构造器注入才需要三级缓存
**答案：B**
**解析：** 三级缓存存在的意义是让 AOP 场景能提前拿到代理引用。原因：如果只有二级缓存，AOP 代理只能等初始化后创建，循环依赖时另一方拿到的是原始对象导致不一致；三级工厂通过 getEarlyBeanReference 提前生成代理。
**来源：** SP-008 · 循环依赖（Spring 源码）

**Qspring-1063（判断·原理）** 三级缓存存在的意义是让 AOP 场景能提前拿到代理引用
**答案：对。** 解析：如果只有二级缓存，AOP 代理只能等初始化后创建，循环依赖时另一方拿到的是原始对象导致不一致；三级工厂通过 getEarlyBeanReference 提前生成代理

**Qspring-1064（判断·原理）** AOP 循环依赖靠二级缓存就够
**答案：错。** 正确表述：三级缓存存在的意义是让 AOP 场景能提前拿到代理引用。原因：如果只有二级缓存，AOP 代理只能等初始化后创建，循环依赖时另一方拿到的是原始对象导致不一致；三级工厂通过 getEarlyBeanReference 提前生成代理

**Qspring-1065（判断·原理）** 三级缓存是为了性能优化
**答案：错。** 正确表述：三级缓存存在的意义是让 AOP 场景能提前拿到代理引用。原因：如果只有二级缓存，AOP 代理只能等初始化后创建，循环依赖时另一方拿到的是原始对象导致不一致；三级工厂通过 getEarlyBeanReference 提前生成代理

**Qspring-1066（判断·原理）** 只有构造器注入才需要三级缓存
**答案：错。** 正确表述：三级缓存存在的意义是让 AOP 场景能提前拿到代理引用。原因：如果只有二级缓存，AOP 代理只能等初始化后创建，循环依赖时另一方拿到的是原始对象导致不一致；三级工厂通过 getEarlyBeanReference 提前生成代理

**Qspring-1067（场景单选·原理）** 在工程实践中关于「getEarlyBeanReference」，下列做法符合推荐实践的是？
- A. AOP 循环依赖靠二级缓存就够
- B. 只有构造器注入才需要三级缓存
- C. 解释"为什么是三级不是二级"的标准答案
- D. 三级缓存是为了性能优化
**答案：C**
**解析：** 推荐实践：解释"为什么是三级不是二级"的标准答案。事实依据：三级缓存存在的意义是让 AOP 场景能提前拿到代理引用。

**Qspring-1068（场景判断·原理）** 推荐实践：解释"为什么是三级不是二级"的标准答案
**答案：对。** 解析：三级缓存存在的意义是让 AOP 场景能提前拿到代理引用。原因：如果只有二级缓存，AOP 代理只能等初始化后创建，循环依赖时另一方拿到的是原始对象导致不一致；三级工厂通过 getEarlyBeanReference 提前生成代理

**Qspring-1069（简答·原理）** 请说明「循环依赖」中getEarlyBeanReference的机制与使用要点。
**要点（标准答案）**：① 三级缓存存在的意义是让 AOP 场景能提前拿到代理引用；② 原理：如果只有二级缓存，AOP 代理只能等初始化后创建，循环依赖时另一方拿到的是原始对象导致不一致；三级工厂通过 getEarlyBeanReference 提前生成代理；③ 使用要点：解释"为什么是三级不是二级"的标准答案。版本锚点：Spring 源码。

**Qspring-1070（单选·正向·限制）** 关于「循环依赖」的说法，正确的是？
- A. 构造器注入循环依赖可以解决
- B. setter 注入循环依赖在 Boot 2.6+ 默认仍可注入
- C. 构造器注入的循环依赖 Spring 无法解决
- D. @Lazy 不能解决循环依赖
**答案：C**
**解析：** 构造器注入的循环依赖 Spring 无法解决。原因：实例化前就需要依赖方，提前曝光机制尚未生效（对象还没 new 出来），Spring Boot 2.6 起默认禁止一切循环依赖并要求重构。
**来源：** SP-009 · 循环依赖（Boot 2.6 release note）

**Qspring-1071（判断·限制）** 构造器注入的循环依赖 Spring 无法解决
**答案：对。** 解析：实例化前就需要依赖方，提前曝光机制尚未生效（对象还没 new 出来），Spring Boot 2.6 起默认禁止一切循环依赖并要求重构

**Qspring-1072（判断·限制）** 构造器注入循环依赖可以解决
**答案：错。** 正确表述：构造器注入的循环依赖 Spring 无法解决。原因：实例化前就需要依赖方，提前曝光机制尚未生效（对象还没 new 出来），Spring Boot 2.6 起默认禁止一切循环依赖并要求重构

**Qspring-1073（判断·限制）** setter 注入循环依赖在 Boot 2.6+ 默认仍可注入
**答案：错。** 正确表述：构造器注入的循环依赖 Spring 无法解决。原因：实例化前就需要依赖方，提前曝光机制尚未生效（对象还没 new 出来），Spring Boot 2.6 起默认禁止一切循环依赖并要求重构

**Qspring-1074（判断·限制）** @Lazy 不能解决循环依赖
**答案：错。** 正确表述：构造器注入的循环依赖 Spring 无法解决。原因：实例化前就需要依赖方，提前曝光机制尚未生效（对象还没 new 出来），Spring Boot 2.6 起默认禁止一切循环依赖并要求重构

**Qspring-1075（场景单选·限制）** 在工程实践中关于「构造器注入」，下列做法符合推荐实践的是？
- A. 构造器注入循环依赖可以解决
- B. setter 注入循环依赖在 Boot 2.6+ 默认仍可注入
- C. 用 @Lazy 或重构消除依赖链
- D. @Lazy 不能解决循环依赖
**答案：C**
**解析：** 推荐实践：用 @Lazy 或重构消除依赖链。事实依据：构造器注入的循环依赖 Spring 无法解决。

**Qspring-1076（场景判断·限制）** 推荐实践：用 @Lazy 或重构消除依赖链
**答案：对。** 解析：构造器注入的循环依赖 Spring 无法解决。原因：实例化前就需要依赖方，提前曝光机制尚未生效（对象还没 new 出来），Spring Boot 2.6 起默认禁止一切循环依赖并要求重构

**Qspring-1077（填空·限制）** ______的循环依赖 Spring 无法解决
**答案：构造器注入**。解析：实例化前就需要依赖方，提前曝光机制尚未生效（对象还没 new 出来），Spring Boot 2.6 起默认禁止一切循环依赖并要求重构

**Qspring-1078（简答·限制）** 请说明「循环依赖」中构造器注入的机制与使用要点。
**要点（标准答案）**：① 构造器注入的循环依赖 Spring 无法解决；② 原理：实例化前就需要依赖方，提前曝光机制尚未生效（对象还没 new 出来），Spring Boot 2.6 起默认禁止一切循环依赖并要求重构；③ 使用要点：用 @Lazy 或重构消除依赖链。版本锚点：Boot 2.6 release note。

**Qspring-1079（单选·正向·限制）** 关于「循环依赖」的说法，正确的是？
- A. prototype 作用域的循环依赖无法解决
- B. prototype 报错发生在启动阶段
- C. prototype 循环依赖也能三级缓存解决
- D. 只有 singleton 才会循环依赖报错
**答案：A**
**解析：** prototype 作用域的循环依赖无法解决。原因：prototype 每次获取都新建，没有缓存可提前曝光，Spring 启动或首次获取时报 BeanCurrentlyInCreationException。
**来源：** SP-010 · 循环依赖（Spring 文档）

**Qspring-1080（判断·限制）** prototype 作用域的循环依赖无法解决
**答案：对。** 解析：prototype 每次获取都新建，没有缓存可提前曝光，Spring 启动或首次获取时报 BeanCurrentlyInCreationException

**Qspring-1081（判断·限制）** prototype 循环依赖也能三级缓存解决
**答案：错。** 正确表述：prototype 作用域的循环依赖无法解决。原因：prototype 每次获取都新建，没有缓存可提前曝光，Spring 启动或首次获取时报 BeanCurrentlyInCreationException

**Qspring-1082（判断·限制）** 只有 singleton 才会循环依赖报错
**答案：错。** 正确表述：prototype 作用域的循环依赖无法解决。原因：prototype 每次获取都新建，没有缓存可提前曝光，Spring 启动或首次获取时报 BeanCurrentlyInCreationException

**Qspring-1083（判断·限制）** prototype 报错发生在启动阶段
**答案：错。** 正确表述：prototype 作用域的循环依赖无法解决。原因：prototype 每次获取都新建，没有缓存可提前曝光，Spring 启动或首次获取时报 BeanCurrentlyInCreationException

**Qspring-1084（场景单选·限制）** 在工程实践中关于「prototype」，下列做法符合推荐实践的是？
- A. 有状态对象用 prototype 时避免环
- B. prototype 循环依赖也能三级缓存解决
- C. 只有 singleton 才会循环依赖报错
- D. prototype 报错发生在启动阶段
**答案：A**
**解析：** 推荐实践：有状态对象用 prototype 时避免环。事实依据：prototype 作用域的循环依赖无法解决。

**Qspring-1085（场景判断·限制）** 推荐实践：有状态对象用 prototype 时避免环
**答案：对。** 解析：prototype 作用域的循环依赖无法解决。原因：prototype 每次获取都新建，没有缓存可提前曝光，Spring 启动或首次获取时报 BeanCurrentlyInCreationException

**Qspring-1086（填空·限制）** ______ 作用域的循环依赖无法解决
**答案：prototype**。解析：prototype 每次获取都新建，没有缓存可提前曝光，Spring 启动或首次获取时报 BeanCurrentlyInCreationException

**Qspring-1087（简答·限制）** 请说明「循环依赖」中prototype的机制与使用要点。
**要点（标准答案）**：① prototype 作用域的循环依赖无法解决；② 原理：prototype 每次获取都新建，没有缓存可提前曝光，Spring 启动或首次获取时报 BeanCurrentlyInCreationException；③ 使用要点：有状态对象用 prototype 时避免环。版本锚点：Spring 文档。

**Qspring-1088（单选·正向·Boot 2.6）** 关于「循环依赖」的说法，正确的是？
- A. 该开关影响 prototype 注入
- B. 开启开关后构造器注入循环依赖也能用
- C. Boot 2.6 后循环依赖完全不能用
- D. Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启
**答案：D**
**解析：** Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启。原因：官方认为循环依赖是设计坏味道，禁止它把问题暴露在启动期而不是运行期。
**来源：** SP-011 · 循环依赖（Boot 2.6）

**Qspring-1089（判断·Boot 2.6）** Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启
**答案：对。** 解析：官方认为循环依赖是设计坏味道，禁止它把问题暴露在启动期而不是运行期

**Qspring-1090（判断·Boot 2.6）** Boot 2.6 后循环依赖完全不能用
**答案：错。** 正确表述：Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启。原因：官方认为循环依赖是设计坏味道，禁止它把问题暴露在启动期而不是运行期

**Qspring-1091（判断·Boot 2.6）** 开启开关后构造器注入循环依赖也能用
**答案：错。** 正确表述：Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启。原因：官方认为循环依赖是设计坏味道，禁止它把问题暴露在启动期而不是运行期

**Qspring-1092（判断·Boot 2.6）** 该开关影响 prototype 注入
**答案：错。** 正确表述：Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启。原因：官方认为循环依赖是设计坏味道，禁止它把问题暴露在启动期而不是运行期

**Qspring-1093（场景单选·Boot 2.6）** 在工程实践中关于「allow-circular-references」，下列做法符合推荐实践的是？
- A. 升级 Boot 2.6 前先解环再加开关
- B. 开启开关后构造器注入循环依赖也能用
- C. Boot 2.6 后循环依赖完全不能用
- D. 该开关影响 prototype 注入
**答案：A**
**解析：** 推荐实践：升级 Boot 2.6 前先解环再加开关。事实依据：Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启。

**Qspring-1094（场景判断·Boot 2.6）** 推荐实践：升级 Boot 2.6 前先解环再加开关
**答案：对。** 解析：Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启。原因：官方认为循环依赖是设计坏味道，禁止它把问题暴露在启动期而不是运行期

**Qspring-1095（填空·Boot 2.6）** Spring Boot 2.6 起默认禁止循环依赖需显式 ______=true 开启
**答案：allow-circular-references**。解析：官方认为循环依赖是设计坏味道，禁止它把问题暴露在启动期而不是运行期

**Qspring-1096（简答·Boot 2.6）** 请说明「循环依赖」中allow-circular-references的机制与使用要点。
**要点（标准答案）**：① Spring Boot 2.6 起默认禁止循环依赖需显式 allow-circular-references=true 开启；② 原理：官方认为循环依赖是设计坏味道，禁止它把问题暴露在启动期而不是运行期；③ 使用要点：升级 Boot 2.6 前先解环再加开关。版本锚点：Boot 2.6。

**Qspring-1097（单选·正向·作用域）** 关于「IoC」的说法，正确的是？
- A. request 作用域在非 Web 环境也能用
- B. 注入 request Bean 不需要任何处理
- C. Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理
- D. session 作用域线程安全无需代理
**答案：C**
**解析：** Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理。原因：singleton Bean 引用 request 作用域 Bean 时 Spring 生成 ScopedProxyFactoryBean 代理转发到当前请求。
**来源：** SP-012 · IoC（Spring 文档）

**Qspring-1098（判断·作用域）** Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理
**答案：对。** 解析：singleton Bean 引用 request 作用域 Bean 时 Spring 生成 ScopedProxyFactoryBean 代理转发到当前请求

**Qspring-1099（判断·作用域）** request 作用域在非 Web 环境也能用
**答案：错。** 正确表述：Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理。原因：singleton Bean 引用 request 作用域 Bean 时 Spring 生成 ScopedProxyFactoryBean 代理转发到当前请求

**Qspring-1100（判断·作用域）** 注入 request Bean 不需要任何处理
**答案：错。** 正确表述：Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理。原因：singleton Bean 引用 request 作用域 Bean 时 Spring 生成 ScopedProxyFactoryBean 代理转发到当前请求

**Qspring-1101（判断·作用域）** session 作用域线程安全无需代理
**答案：错。** 正确表述：Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理。原因：singleton Bean 引用 request 作用域 Bean 时 Spring 生成 ScopedProxyFactoryBean 代理转发到当前请求

**Qspring-1102（场景单选·作用域）** 在工程实践中关于「request」，下列做法符合推荐实践的是？
- A. 每请求状态对象的标准做法
- B. session 作用域线程安全无需代理
- C. 注入 request Bean 不需要任何处理
- D. request 作用域在非 Web 环境也能用
**答案：A**
**解析：** 推荐实践：每请求状态对象的标准做法。事实依据：Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理。

**Qspring-1103（场景判断·作用域）** 推荐实践：每请求状态对象的标准做法
**答案：对。** 解析：Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理。原因：singleton Bean 引用 request 作用域 Bean 时 Spring 生成 ScopedProxyFactoryBean 代理转发到当前请求

**Qspring-1104（填空·作用域）** Web 作用域 ______/session/application 依赖 Web 环境且注入 singleton 时需代理
**答案：request**。解析：singleton Bean 引用 request 作用域 Bean 时 Spring 生成 ScopedProxyFactoryBean 代理转发到当前请求

**Qspring-1105（简答·作用域）** 请说明「IoC」中request的机制与使用要点。
**要点（标准答案）**：① Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理；② 原理：singleton Bean 引用 request 作用域 Bean 时 Spring 生成 ScopedProxyFactoryBean 代理转发到当前请求；③ 使用要点：每请求状态对象的标准做法。版本锚点：Spring 文档。

**Qspring-1106（单选·正向·误用）** 关于「IoC」的说法，正确的是？
- A. Spring 会自动按需创建新 prototype
- B. 注入后每次调用返回新实例
- C. 加 @Lazy 后每次都是新实例
- D. singleton 中注入 prototype Bean 只注入一次失去多例语义
**答案：D**
**解析：** singleton 中注入 prototype Bean 只注入一次失去多例语义。原因：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取。
**来源：** SP-013 · IoC（经典陷阱）

**Qspring-1107（判断·误用）** singleton 中注入 prototype Bean 只注入一次失去多例语义
**答案：对。** 解析：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取

**Qspring-1108（判断·误用）** Spring 会自动按需创建新 prototype
**答案：错。** 正确表述：singleton 中注入 prototype Bean 只注入一次失去多例语义。原因：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取

**Qspring-1109（判断·误用）** 注入后每次调用返回新实例
**答案：错。** 正确表述：singleton 中注入 prototype Bean 只注入一次失去多例语义。原因：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取

**Qspring-1110（判断·误用）** 加 @Lazy 后每次都是新实例
**答案：错。** 正确表述：singleton 中注入 prototype Bean 只注入一次失去多例语义。原因：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取

**Qspring-1111（场景单选·误用）** 在工程实践中关于「prototype 注入」，下列做法符合推荐实践的是？
- A. Spring 会自动按需创建新 prototype
- B. 每次需要新实例用 ObjectProvider.getBean
- C. 加 @Lazy 后每次都是新实例
- D. 注入后每次调用返回新实例
**答案：B**
**解析：** 推荐实践：每次需要新实例用 ObjectProvider.getBean。事实依据：singleton 中注入 prototype Bean 只注入一次失去多例语义。

**Qspring-1112（场景判断·误用）** 推荐实践：每次需要新实例用 ObjectProvider.getBean
**答案：对。** 解析：singleton 中注入 prototype Bean 只注入一次失去多例语义。原因：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取

**Qspring-1113（简答·误用）** 请说明「IoC」中prototype 注入的机制与使用要点。
**要点（标准答案）**：① singleton 中注入 prototype Bean 只注入一次失去多例语义；② 原理：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取；③ 使用要点：每次需要新实例用 ObjectProvider.getBean。版本锚点：经典陷阱。

**Qspring-1114（单选·正向·API）** 关于「IoC」的说法，正确的是？
- A. getIfAvailable 找不到会抛异常
- B. ObjectProvider 在启动时立刻解析依赖
- C. 它是 @Autowired 的废弃替代
- D. ObjectProvider 提供延迟与可选的依赖获取
**答案：D**
**解析：** ObjectProvider 提供延迟与可选的依赖获取。原因：getIfAvailable、getIfUnique、getObject，解决"依赖可能不存在"与"每次要新实例"两类问题。
**来源：** SP-014 · IoC（Spring 文档）

**Qspring-1115（判断·API）** ObjectProvider 提供延迟与可选的依赖获取
**答案：对。** 解析：getIfAvailable、getIfUnique、getObject，解决"依赖可能不存在"与"每次要新实例"两类问题

**Qspring-1116（判断·API）** ObjectProvider 在启动时立刻解析依赖
**答案：错。** 正确表述：ObjectProvider 提供延迟与可选的依赖获取。原因：getIfAvailable、getIfUnique、getObject，解决"依赖可能不存在"与"每次要新实例"两类问题

**Qspring-1117（判断·API）** 它是 @Autowired 的废弃替代
**答案：错。** 正确表述：ObjectProvider 提供延迟与可选的依赖获取。原因：getIfAvailable、getIfUnique、getObject，解决"依赖可能不存在"与"每次要新实例"两类问题

**Qspring-1118（判断·API）** getIfAvailable 找不到会抛异常
**答案：错。** 正确表述：ObjectProvider 提供延迟与可选的依赖获取。原因：getIfAvailable、getIfUnique、getObject，解决"依赖可能不存在"与"每次要新实例"两类问题

**Qspring-1119（场景单选·API）** 在工程实践中关于「ObjectProvider」，下列做法符合推荐实践的是？
- A. ObjectProvider 在启动时立刻解析依赖
- B. 框架开发与可选依赖场景
- C. getIfAvailable 找不到会抛异常
- D. 它是 @Autowired 的废弃替代
**答案：B**
**解析：** 推荐实践：框架开发与可选依赖场景。事实依据：ObjectProvider 提供延迟与可选的依赖获取。

**Qspring-1120（场景判断·API）** 推荐实践：框架开发与可选依赖场景
**答案：对。** 解析：ObjectProvider 提供延迟与可选的依赖获取。原因：getIfAvailable、getIfUnique、getObject，解决"依赖可能不存在"与"每次要新实例"两类问题

**Qspring-1121（填空·API）** ______ 提供延迟与可选的依赖获取
**答案：ObjectProvider**。解析：getIfAvailable、getIfUnique、getObject，解决"依赖可能不存在"与"每次要新实例"两类问题

**Qspring-1122（简答·API）** 请说明「IoC」中ObjectProvider的机制与使用要点。
**要点（标准答案）**：① ObjectProvider 提供延迟与可选的依赖获取；② 原理：getIfAvailable、getIfUnique、getObject，解决"依赖可能不存在"与"每次要新实例"两类问题；③ 使用要点：框架开发与可选依赖场景。版本锚点：Spring 文档。

**Qspring-1123（单选·正向·FactoryBean）** 关于「IoC」的说法，正确的是？
- A. getBean 直接返回 FactoryBean 实例
- B. FactoryBean 与 BeanFactory 是一回事
- C. FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物
- D. & 前缀是可选语法
**答案：C**
**解析：** FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物。原因：取 FactoryBean 本身要在名字前加 &（getBean("&xxx")），MyBatis Mapper、Spring AOP 代理、Feign 客户端都由 FactoryBean 产出。
**来源：** SP-015 · IoC（Spring 文档）

**Qspring-1124（判断·FactoryBean）** FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物
**答案：对。** 解析：取 FactoryBean 本身要在名字前加 &（getBean("&xxx")），MyBatis Mapper、Spring AOP 代理、Feign 客户端都由 FactoryBean 产出

**Qspring-1125（判断·FactoryBean）** FactoryBean 与 BeanFactory 是一回事
**答案：错。** 正确表述：FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物。原因：取 FactoryBean 本身要在名字前加 &（getBean("&xxx")），MyBatis Mapper、Spring AOP 代理、Feign 客户端都由 FactoryBean 产出

**Qspring-1126（判断·FactoryBean）** getBean 直接返回 FactoryBean 实例
**答案：错。** 正确表述：FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物。原因：取 FactoryBean 本身要在名字前加 &（getBean("&xxx")），MyBatis Mapper、Spring AOP 代理、Feign 客户端都由 FactoryBean 产出

**Qspring-1127（判断·FactoryBean）** & 前缀是可选语法
**答案：错。** 正确表述：FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物。原因：取 FactoryBean 本身要在名字前加 &（getBean("&xxx")），MyBatis Mapper、Spring AOP 代理、Feign 客户端都由 FactoryBean 产出

**Qspring-1128（场景单选·FactoryBean）** 在工程实践中关于「getObject」，下列做法符合推荐实践的是？
- A. MyBatis MapperProxy 的注册原理
- B. getBean 直接返回 FactoryBean 实例
- C. FactoryBean 与 BeanFactory 是一回事
- D. & 前缀是可选语法
**答案：A**
**解析：** 推荐实践：MyBatis MapperProxy 的注册原理。事实依据：FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物。

**Qspring-1129（场景判断·FactoryBean）** 推荐实践：MyBatis MapperProxy 的注册原理
**答案：对。** 解析：FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物。原因：取 FactoryBean 本身要在名字前加 &（getBean("&xxx")），MyBatis Mapper、Spring AOP 代理、Feign 客户端都由 FactoryBean 产出

**Qspring-1130（填空·FactoryBean）** FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 ______ 的产物
**答案：getObject**。解析：取 FactoryBean 本身要在名字前加 &（getBean("&xxx")），MyBatis Mapper、Spring AOP 代理、Feign 客户端都由 FactoryBean 产出

**Qspring-1131（简答·FactoryBean）** 请说明「IoC」中getObject的机制与使用要点。
**要点（标准答案）**：① FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物；② 原理：取 FactoryBean 本身要在名字前加 &（getBean("&xxx")），MyBatis Mapper、Spring AOP 代理、Feign 客户端都由 FactoryBean 产出；③ 使用要点：MyBatis MapperProxy 的注册原理。版本锚点：Spring 文档。

**Qspring-1132（单选·正向·懒加载）** 关于「IoC」的说法，正确的是？
- A. @Lazy 延迟到首次使用时才初始化 Bean
- B. @Lazy 提前初始化
- C. @Lazy 影响 AOP 代理创建
- D. @Lazy 对 singleton 全局生效（只对标注处）
**答案：A**
**解析：** @Lazy 延迟到首次使用时才初始化 Bean。原因：启动提速与打破循环依赖（注入代理占位），@Lazy 加在循环依赖字段上用代理打破死锁。
**来源：** SP-016 · IoC（Spring 文档）

**Qspring-1133（判断·懒加载）** @Lazy 延迟到首次使用时才初始化 Bean
**答案：对。** 解析：启动提速与打破循环依赖（注入代理占位），@Lazy 加在循环依赖字段上用代理打破死锁

**Qspring-1134（判断·懒加载）** @Lazy 提前初始化
**答案：错。** 正确表述：@Lazy 延迟到首次使用时才初始化 Bean。原因：启动提速与打破循环依赖（注入代理占位），@Lazy 加在循环依赖字段上用代理打破死锁

**Qspring-1135（判断·懒加载）** @Lazy 对 singleton 全局生效（只对标注处）
**答案：错。** 正确表述：@Lazy 延迟到首次使用时才初始化 Bean。原因：启动提速与打破循环依赖（注入代理占位），@Lazy 加在循环依赖字段上用代理打破死锁

**Qspring-1136（判断·懒加载）** @Lazy 影响 AOP 代理创建
**答案：错。** 正确表述：@Lazy 延迟到首次使用时才初始化 Bean。原因：启动提速与打破循环依赖（注入代理占位），@Lazy 加在循环依赖字段上用代理打破死锁

**Qspring-1137（场景单选·懒加载）** 在工程实践中关于「@Lazy」，下列做法符合推荐实践的是？
- A. @Lazy 影响 AOP 代理创建
- B. @Lazy 提前初始化
- C. @Lazy 对 singleton 全局生效（只对标注处）
- D. 启动慢与循环依赖的两个用途
**答案：D**
**解析：** 推荐实践：启动慢与循环依赖的两个用途。事实依据：@Lazy 延迟到首次使用时才初始化 Bean。

**Qspring-1138（场景判断·懒加载）** 推荐实践：启动慢与循环依赖的两个用途
**答案：对。** 解析：@Lazy 延迟到首次使用时才初始化 Bean。原因：启动提速与打破循环依赖（注入代理占位），@Lazy 加在循环依赖字段上用代理打破死锁

**Qspring-1139（填空·懒加载）** ______ 延迟到首次使用时才初始化 Bean
**答案：@Lazy**。解析：启动提速与打破循环依赖（注入代理占位），@Lazy 加在循环依赖字段上用代理打破死锁

**Qspring-1140（简答·懒加载）** 请说明「IoC」中@Lazy的机制与使用要点。
**要点（标准答案）**：① @Lazy 延迟到首次使用时才初始化 Bean；② 原理：启动提速与打破循环依赖（注入代理占位），@Lazy 加在循环依赖字段上用代理打破死锁；③ 使用要点：启动慢与循环依赖的两个用途。版本锚点：Spring 文档。

**Qspring-1141（单选·正向·对比）** 关于「容器」的说法，正确的是？
- A. ApplicationContext 与 BeanFactory 无关
- B. ApplicationContext 不支持懒加载
- C. BeanFactory 是 ApplicationContext 的子接口
- D. ApplicationContext 是 BeanFactory 的超集增强版
**答案：D**
**解析：** ApplicationContext 是 BeanFactory 的超集增强版。原因：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton。
**来源：** SP-017 · 容器（Spring 文档）

**Qspring-1142（判断·对比）** ApplicationContext 是 BeanFactory 的超集增强版
**答案：对。** 解析：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton

**Qspring-1143（判断·对比）** ApplicationContext 与 BeanFactory 无关
**答案：错。** 正确表述：ApplicationContext 是 BeanFactory 的超集增强版。原因：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton

**Qspring-1144（判断·对比）** ApplicationContext 不支持懒加载
**答案：错。** 正确表述：ApplicationContext 是 BeanFactory 的超集增强版。原因：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton

**Qspring-1145（判断·对比）** BeanFactory 是 ApplicationContext 的子接口
**答案：错。** 正确表述：ApplicationContext 是 BeanFactory 的超集增强版。原因：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton

**Qspring-1146（场景单选·对比）** 在工程实践中关于「ApplicationContext」，下列做法符合推荐实践的是？
- A. BeanFactory 是 ApplicationContext 的子接口
- B. ApplicationContext 与 BeanFactory 无关
- C. 回答容器体系对比题
- D. ApplicationContext 不支持懒加载
**答案：C**
**解析：** 推荐实践：回答容器体系对比题。事实依据：ApplicationContext 是 BeanFactory 的超集增强版。

**Qspring-1147（场景判断·对比）** 推荐实践：回答容器体系对比题
**答案：对。** 解析：ApplicationContext 是 BeanFactory 的超集增强版。原因：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton

**Qspring-1148（填空·对比）** ______ 是 BeanFactory 的超集增强版
**答案：ApplicationContext**。解析：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton

**Qspring-1149（简答·对比）** 请说明「容器」中ApplicationContext的机制与使用要点。
**要点（标准答案）**：① ApplicationContext 是 BeanFactory 的超集增强版；② 原理：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton；③ 使用要点：回答容器体系对比题。版本锚点：Spring 文档。

**Qspring-1150（单选·正向·启动）** 关于「容器」的说法，正确的是？
- A. 容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板
- B. refresh 每次都会重新创建所有 Bean
- C. refresh 只在 XML 容器存在
- D. 内嵌 Tomcat 在实例化 Bean 之后启动
**答案：A**
**解析：** 容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板。原因：步骤包括 BeanFactory 准备、BPP 注册与执行、国际化、事件广播器、onRefresh（内嵌容器启动）、finishBeanFactoryInitialization（预实例化）。
**来源：** SP-018 · 容器（Spring 源码）

**Qspring-1151（判断·启动）** 容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板
**答案：对。** 解析：步骤包括 BeanFactory 准备、BPP 注册与执行、国际化、事件广播器、onRefresh（内嵌容器启动）、finishBeanFactoryInitialization（预实例化）

**Qspring-1152（判断·启动）** refresh 每次都会重新创建所有 Bean
**答案：错。** 正确表述：容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板。原因：步骤包括 BeanFactory 准备、BPP 注册与执行、国际化、事件广播器、onRefresh（内嵌容器启动）、finishBeanFactoryInitialization（预实例化）

**Qspring-1153（判断·启动）** 内嵌 Tomcat 在实例化 Bean 之后启动
**答案：错。** 正确表述：容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板。原因：步骤包括 BeanFactory 准备、BPP 注册与执行、国际化、事件广播器、onRefresh（内嵌容器启动）、finishBeanFactoryInitialization（预实例化）

**Qspring-1154（判断·启动）** refresh 只在 XML 容器存在
**答案：错。** 正确表述：容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板。原因：步骤包括 BeanFactory 准备、BPP 注册与执行、国际化、事件广播器、onRefresh（内嵌容器启动）、finishBeanFactoryInitialization（预实例化）

**Qspring-1155（场景单选·启动）** 在工程实践中关于「refresh」，下列做法符合推荐实践的是？
- A. refresh 只在 XML 容器存在
- B. refresh 每次都会重新创建所有 Bean
- C. 内嵌 Tomcat 在实例化 Bean 之后启动
- D. Spring Boot 启动慢分析从 refresh 分步计时入手
**答案：D**
**解析：** 推荐实践：Spring Boot 启动慢分析从 refresh 分步计时入手。事实依据：容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板。

**Qspring-1156（场景判断·启动）** 推荐实践：Spring Boot 启动慢分析从 refresh 分步计时入手
**答案：对。** 解析：容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板。原因：步骤包括 BeanFactory 准备、BPP 注册与执行、国际化、事件广播器、onRefresh（内嵌容器启动）、finishBeanFactoryInitialization（预实例化）

**Qspring-1157（填空·启动）** 容器启动核心是 AbstractApplicationContext.______ 的 12 步模板
**答案：refresh**。解析：步骤包括 BeanFactory 准备、BPP 注册与执行、国际化、事件广播器、onRefresh（内嵌容器启动）、finishBeanFactoryInitialization（预实例化）

**Qspring-1158（简答·启动）** 请说明「容器」中refresh的机制与使用要点。
**要点（标准答案）**：① 容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板；② 原理：步骤包括 BeanFactory 准备、BPP 注册与执行、国际化、事件广播器、onRefresh（内嵌容器启动）、finishBeanFactoryInitialization（预实例化）；③ 使用要点：Spring Boot 启动慢分析从 refresh 分步计时入手。版本锚点：Spring 源码。

**Qspring-1159（单选·正向·BFPP）** 关于「扩展点」的说法，正确的是？
- A. BFPP 与 BPP 没有区别
- B. BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition
- C. BFPP 在 Bean 创建后执行
- D. BFPP 可以修改 Bean 实例属性
**答案：B**
**解析：** BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition。原因：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP。
**来源：** SP-019 · 扩展点（Spring 源码）

**Qspring-1160（判断·BFPP）** BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition
**答案：对。** 解析：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP

**Qspring-1161（判断·BFPP）** BFPP 在 Bean 创建后执行
**答案：错。** 正确表述：BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition。原因：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP

**Qspring-1162（判断·BFPP）** BFPP 与 BPP 没有区别
**答案：错。** 正确表述：BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition。原因：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP

**Qspring-1163（判断·BFPP）** BFPP 可以修改 Bean 实例属性
**答案：错。** 正确表述：BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition。原因：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP

**Qspring-1164（场景单选·BFPP）** 在工程实践中关于「BeanFactoryPostProcessor」，下列做法符合推荐实践的是？
- A. BFPP 可以修改 Bean 实例属性
- B. BFPP 在 Bean 创建后执行
- C. 配置占位符、动态注册 BeanDefinition 的入口
- D. BFPP 与 BPP 没有区别
**答案：C**
**解析：** 推荐实践：配置占位符、动态注册 BeanDefinition 的入口。事实依据：BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition。

**Qspring-1165（场景判断·BFPP）** 推荐实践：配置占位符、动态注册 BeanDefinition 的入口
**答案：对。** 解析：BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition。原因：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP

**Qspring-1166（填空·BFPP）** ______ 在 Bean 实例化前修改 BeanDefinition
**答案：BeanFactoryPostProcessor**。解析：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP

**Qspring-1167（简答·BFPP）** 请说明「扩展点」中BeanFactoryPostProcessor的机制与使用要点。
**要点（标准答案）**：① BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition；② 原理：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP；③ 使用要点：配置占位符、动态注册 BeanDefinition 的入口。版本锚点：Spring 源码。

**Qspring-1168（单选·正向·BDRPP）** 关于「扩展点」的说法，正确的是？
- A. BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition
- B. 它比普通 BFPP 执行更晚
- C. 它不能注册新 BeanDefinition
- D. @MapperScan 用 BeanPostProcessor 实现
**答案：A**
**解析：** BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition。原因：MyBatis @MapperScan 动态注册 Mapper BeanDefinition 就是该扩展点（MapperScannerRegistrar→BDRPP），比静态 @Bean 更早介入。
**来源：** SP-020 · 扩展点（Spring 源码）

**Qspring-1169（判断·BDRPP）** BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition
**答案：对。** 解析：MyBatis @MapperScan 动态注册 Mapper BeanDefinition 就是该扩展点（MapperScannerRegistrar→BDRPP），比静态 @Bean 更早介入

**Qspring-1170（判断·BDRPP）** 它比普通 BFPP 执行更晚
**答案：错。** 正确表述：BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition。原因：MyBatis @MapperScan 动态注册 Mapper BeanDefinition 就是该扩展点（MapperScannerRegistrar→BDRPP），比静态 @Bean 更早介入

**Qspring-1171（判断·BDRPP）** 它不能注册新 BeanDefinition
**答案：错。** 正确表述：BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition。原因：MyBatis @MapperScan 动态注册 Mapper BeanDefinition 就是该扩展点（MapperScannerRegistrar→BDRPP），比静态 @Bean 更早介入

**Qspring-1172（判断·BDRPP）** @MapperScan 用 BeanPostProcessor 实现
**答案：错。** 正确表述：BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition。原因：MyBatis @MapperScan 动态注册 Mapper BeanDefinition 就是该扩展点（MapperScannerRegistrar→BDRPP），比静态 @Bean 更早介入

**Qspring-1173（场景单选·BDRPP）** 在工程实践中关于「BeanDefinitionRegistryPostProcessor」，下列做法符合推荐实践的是？
- A. 动态注册 Bean 的标准扩展点
- B. 它不能注册新 BeanDefinition
- C. @MapperScan 用 BeanPostProcessor 实现
- D. 它比普通 BFPP 执行更晚
**答案：A**
**解析：** 推荐实践：动态注册 Bean 的标准扩展点。事实依据：BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition。

**Qspring-1174（场景判断·BDRPP）** 推荐实践：动态注册 Bean 的标准扩展点
**答案：对。** 解析：BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition。原因：MyBatis @MapperScan 动态注册 Mapper BeanDefinition 就是该扩展点（MapperScannerRegistrar→BDRPP），比静态 @Bean 更早介入

**Qspring-1175（填空·BDRPP）** ______ 在普通 BFPP 之前执行可动态注册 BeanDefinition
**答案：BeanDefinitionRegistryPostProcessor**。解析：MyBatis @MapperScan 动态注册 Mapper BeanDefinition 就是该扩展点（MapperScannerRegistrar→BDRPP），比静态 @Bean 更早介入

**Qspring-1176（简答·BDRPP）** 请说明「扩展点」中BeanDefinitionRegistryPostProcessor的机制与使用要点。
**要点（标准答案）**：① BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition；② 原理：MyBatis @MapperScan 动态注册 Mapper BeanDefinition 就是该扩展点（MapperScannerRegistrar→BDRPP），比静态 @Bean 更早介入；③ 使用要点：动态注册 Bean 的标准扩展点。版本锚点：Spring 源码。

**Qspring-1177（单选·正向·Aware）** 关于「扩展点」的说法，正确的是？
- A. 所有 Aware 同时回调
- B. Aware 回调可以手动触发
- C. Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理
- D. ApplicationContextAware 最先回调
**答案：C**
**解析：** Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理。原因：Aware 是容器向 Bean 注入基础设施引用的通道，不同 Aware 由不同组件调用时机略异。
**来源：** SP-021 · 扩展点（Spring 源码）

**Qspring-1178（判断·Aware）** Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理
**答案：对。** 解析：Aware 是容器向 Bean 注入基础设施引用的通道，不同 Aware 由不同组件调用时机略异

**Qspring-1179（判断·Aware）** 所有 Aware 同时回调
**答案：错。** 正确表述：Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理。原因：Aware 是容器向 Bean 注入基础设施引用的通道，不同 Aware 由不同组件调用时机略异

**Qspring-1180（判断·Aware）** ApplicationContextAware 最先回调
**答案：错。** 正确表述：Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理。原因：Aware 是容器向 Bean 注入基础设施引用的通道，不同 Aware 由不同组件调用时机略异

**Qspring-1181（判断·Aware）** Aware 回调可以手动触发
**答案：错。** 正确表述：Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理。原因：Aware 是容器向 Bean 注入基础设施引用的通道，不同 Aware 由不同组件调用时机略异

**Qspring-1182（场景单选·Aware）** 在工程实践中关于「Aware 接口」，下列做法符合推荐实践的是？
- A. 所有 Aware 同时回调
- B. ApplicationContextAware 最先回调
- C. 需要容器能力时实现对应 Aware
- D. Aware 回调可以手动触发
**答案：C**
**解析：** 推荐实践：需要容器能力时实现对应 Aware。事实依据：Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理。

**Qspring-1183（场景判断·Aware）** 推荐实践：需要容器能力时实现对应 Aware
**答案：对。** 解析：Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理。原因：Aware 是容器向 Bean 注入基础设施引用的通道，不同 Aware 由不同组件调用时机略异

**Qspring-1184（简答·Aware）** 请说明「扩展点」中Aware 接口的机制与使用要点。
**要点（标准答案）**：① Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理；② 原理：Aware 是容器向 Bean 注入基础设施引用的通道，不同 Aware 由不同组件调用时机略异；③ 使用要点：需要容器能力时实现对应 Aware。版本锚点：Spring 源码。

**Qspring-1185（单选·正向·销毁）** 关于「Bean 生命周期」的说法，正确的是？
- A. @PreDestroy 最后执行
- B. 销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method
- C. 销毁回调在 JVM 退出时自动调用
- D. prototype Bean 也有销毁回调（容器不管理 prototype 销毁）
**答案：B**
**解析：** 销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method。原因：与初始化三回调镜像对称，容器关闭（context.close 或 Boot 优雅停机）时执行。
**来源：** SP-022 · Bean 生命周期（Spring 文档）

**Qspring-1186（判断·销毁）** 销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method
**答案：对。** 解析：与初始化三回调镜像对称，容器关闭（context.close 或 Boot 优雅停机）时执行

**Qspring-1187（判断·销毁）** 销毁回调在 JVM 退出时自动调用
**答案：错。** 正确表述：销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method。原因：与初始化三回调镜像对称，容器关闭（context.close 或 Boot 优雅停机）时执行

**Qspring-1188（判断·销毁）** @PreDestroy 最后执行
**答案：错。** 正确表述：销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method。原因：与初始化三回调镜像对称，容器关闭（context.close 或 Boot 优雅停机）时执行

**Qspring-1189（判断·销毁）** prototype Bean 也有销毁回调（容器不管理 prototype 销毁）
**答案：错。** 正确表述：销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method。原因：与初始化三回调镜像对称，容器关闭（context.close 或 Boot 优雅停机）时执行

**Qspring-1190（场景单选·销毁）** 在工程实践中关于「@PreDestroy」，下列做法符合推荐实践的是？
- A. 释放连接与线程池的正确位置
- B. 销毁回调在 JVM 退出时自动调用
- C. @PreDestroy 最后执行
- D. prototype Bean 也有销毁回调（容器不管理 prototype 销毁）
**答案：A**
**解析：** 推荐实践：释放连接与线程池的正确位置。事实依据：销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method。

**Qspring-1191（场景判断·销毁）** 推荐实践：释放连接与线程池的正确位置
**答案：对。** 解析：销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method。原因：与初始化三回调镜像对称，容器关闭（context.close 或 Boot 优雅停机）时执行

**Qspring-1192（填空·销毁）** 销毁回调顺序：______、DisposableBean.destroy、destroy-method
**答案：@PreDestroy**。解析：与初始化三回调镜像对称，容器关闭（context.close 或 Boot 优雅停机）时执行

**Qspring-1193（简答·销毁）** 请说明「Bean 生命周期」中@PreDestroy的机制与使用要点。
**要点（标准答案）**：① 销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method；② 原理：与初始化三回调镜像对称，容器关闭（context.close 或 Boot 优雅停机）时执行；③ 使用要点：释放连接与线程池的正确位置。版本锚点：Spring 文档。

**Qspring-1194（单选·正向·注入）** 关于「IoC」的说法，正确的是？
- A. 构造器注入是官方推荐的注入方式
- B. 构造器注入无法解决循环依赖（是特性不是缺陷，暴露设计问题）
- C. 字段注入是最佳实践
- D. 构造器注入参数多时应该换字段注入
**答案：A**
**解析：** 构造器注入是官方推荐的注入方式。原因：依赖不可变（final 字段）、完整初始化、便于测试，阿里手册也明确推荐构造器注入。
**来源：** SP-023 · IoC（官方文档）

**Qspring-1195（判断·注入）** 构造器注入是官方推荐的注入方式
**答案：对。** 解析：依赖不可变（final 字段）、完整初始化、便于测试，阿里手册也明确推荐构造器注入

**Qspring-1196（判断·注入）** 字段注入是最佳实践
**答案：错。** 正确表述：构造器注入是官方推荐的注入方式。原因：依赖不可变（final 字段）、完整初始化、便于测试，阿里手册也明确推荐构造器注入

**Qspring-1197（判断·注入）** 构造器注入参数多时应该换字段注入
**答案：错。** 正确表述：构造器注入是官方推荐的注入方式。原因：依赖不可变（final 字段）、完整初始化、便于测试，阿里手册也明确推荐构造器注入

**Qspring-1198（判断·注入）** 构造器注入无法解决循环依赖（是特性不是缺陷，暴露设计问题）
**答案：错。** 正确表述：构造器注入是官方推荐的注入方式。原因：依赖不可变（final 字段）、完整初始化、便于测试，阿里手册也明确推荐构造器注入

**Qspring-1199（场景单选·注入）** 在工程实践中关于「构造器注入」，下列做法符合推荐实践的是？
- A. 字段注入是最佳实践
- B. 构造器注入参数多时应该换字段注入
- C. 新代码一律构造器注入
- D. 构造器注入无法解决循环依赖（是特性不是缺陷，暴露设计问题）
**答案：C**
**解析：** 推荐实践：新代码一律构造器注入。事实依据：构造器注入是官方推荐的注入方式。

**Qspring-1200（场景判断·注入）** 推荐实践：新代码一律构造器注入
**答案：对。** 解析：构造器注入是官方推荐的注入方式。原因：依赖不可变（final 字段）、完整初始化、便于测试，阿里手册也明确推荐构造器注入

**Qspring-1201（填空·注入）** ______是官方推荐的注入方式
**答案：构造器注入**。解析：依赖不可变（final 字段）、完整初始化、便于测试，阿里手册也明确推荐构造器注入

**Qspring-1202（简答·注入）** 请说明「IoC」中构造器注入的机制与使用要点。
**要点（标准答案）**：① 构造器注入是官方推荐的注入方式；② 原理：依赖不可变（final 字段）、完整初始化、便于测试，阿里手册也明确推荐构造器注入；③ 使用要点：新代码一律构造器注入。版本锚点：官方文档。

**Qspring-1203（单选·正向·注入）** 关于「IoC」的说法，正确的是？
- A. @Qualifier 按类型过滤（它按名称限定）
- B. @Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧
- C. @Autowired 找不到直接跳过
- D. @Autowired 默认按名称注入
**答案：B**
**解析：** @Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧。原因：按类型找到多个候选先看 @Primary 再按字段名匹配，都不确定抛 NoUniqueBeanDefinitionException。
**来源：** SP-024 · IoC（Spring 文档）

**Qspring-1204（判断·注入）** @Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧
**答案：对。** 解析：按类型找到多个候选先看 @Primary 再按字段名匹配，都不确定抛 NoUniqueBeanDefinitionException

**Qspring-1205（判断·注入）** @Autowired 默认按名称注入
**答案：错。** 正确表述：@Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧。原因：按类型找到多个候选先看 @Primary 再按字段名匹配，都不确定抛 NoUniqueBeanDefinitionException

**Qspring-1206（判断·注入）** @Autowired 找不到直接跳过
**答案：错。** 正确表述：@Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧。原因：按类型找到多个候选先看 @Primary 再按字段名匹配，都不确定抛 NoUniqueBeanDefinitionException

**Qspring-1207（判断·注入）** @Qualifier 按类型过滤（它按名称限定）
**答案：错。** 正确表述：@Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧。原因：按类型找到多个候选先看 @Primary 再按字段名匹配，都不确定抛 NoUniqueBeanDefinitionException

**Qspring-1208（场景单选·注入）** 在工程实践中关于「@Autowired」，下列做法符合推荐实践的是？
- A. @Qualifier 按类型过滤（它按名称限定）
- B. @Autowired 找不到直接跳过
- C. @Autowired 默认按名称注入
- D. 多实现接口注入的标准解法
**答案：D**
**解析：** 推荐实践：多实现接口注入的标准解法。事实依据：@Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧。

**Qspring-1209（场景判断·注入）** 推荐实践：多实现接口注入的标准解法
**答案：对。** 解析：@Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧。原因：按类型找到多个候选先看 @Primary 再按字段名匹配，都不确定抛 NoUniqueBeanDefinitionException

**Qspring-1210（填空·注入）** ______ 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧
**答案：@Autowired**。解析：按类型找到多个候选先看 @Primary 再按字段名匹配，都不确定抛 NoUniqueBeanDefinitionException

**Qspring-1211（简答·注入）** 请说明「IoC」中@Autowired的机制与使用要点。
**要点（标准答案）**：① @Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧；② 原理：按类型找到多个候选先看 @Primary 再按字段名匹配，都不确定抛 NoUniqueBeanDefinitionException；③ 使用要点：多实现接口注入的标准解法。版本锚点：Spring 文档。

**Qspring-1212（单选·正向·注入）** 关于「IoC」的说法，正确的是？
- A. @Resource 是 JSR-250 标准默认按名称注入
- B. 两者行为完全一致
- C. @Resource 是 Spring 的注解
- D. @Resource 默认按类型注入
**答案：A**
**解析：** @Resource 是 JSR-250 标准默认按名称注入。原因：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同。
**来源：** SP-025 · IoC（JSR-250）

**Qspring-1213（判断·注入）** @Resource 是 JSR-250 标准默认按名称注入
**答案：对。** 解析：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同

**Qspring-1214（判断·注入）** @Resource 默认按类型注入
**答案：错。** 正确表述：@Resource 是 JSR-250 标准默认按名称注入。原因：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同

**Qspring-1215（判断·注入）** @Resource 是 Spring 的注解
**答案：错。** 正确表述：@Resource 是 JSR-250 标准默认按名称注入。原因：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同

**Qspring-1216（判断·注入）** 两者行为完全一致
**答案：错。** 正确表述：@Resource 是 JSR-250 标准默认按名称注入。原因：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同

**Qspring-1217（场景单选·注入）** 在工程实践中关于「@Resource」，下列做法符合推荐实践的是？
- A. 两者行为完全一致
- B. @Resource 默认按类型注入
- C. JDK17+ 移除 javax.annotation 后 Boot 3 需显式依赖 jakarta.annotation
- D. @Resource 是 Spring 的注解
**答案：C**
**解析：** 推荐实践：JDK17+ 移除 javax.annotation 后 Boot 3 需显式依赖 jakarta.annotation。事实依据：@Resource 是 JSR-250 标准默认按名称注入。

**Qspring-1218（场景判断·注入）** 推荐实践：JDK17+ 移除 javax.annotation 后 Boot 3 需显式依赖 jakarta.annotation
**答案：对。** 解析：@Resource 是 JSR-250 标准默认按名称注入。原因：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同

**Qspring-1219（填空·注入）** ______ 是 JSR-250 标准默认按名称注入
**答案：@Resource**。解析：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同

**Qspring-1220（简答·注入）** 请说明「IoC」中@Resource的机制与使用要点。
**要点（标准答案）**：① @Resource 是 JSR-250 标准默认按名称注入；② 原理：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同；③ 使用要点：JDK17+ 移除 javax.annotation 后 Boot 3 需显式依赖 jakarta.annotation。版本锚点：JSR-250。

**Qspring-1221（单选·正向·注入）** 关于「IoC」的说法，正确的是？
- A. 注入 List/Map 类型会收集容器内所有匹配类型的 Bean
- B. 无法控制顺序
- C. 集合注入不支持泛型匹配
- D. 集合注入只会注入一个 Bean
**答案：A**
**解析：** 注入 List/Map 类型会收集容器内所有匹配类型的 Bean。原因：策略模式的 Spring 实现：注入 List<Handler> 或 Map<String,Handler>（key 为 Bean 名），配合 @Order 排序。
**来源：** SP-026 · IoC（Spring 文档）

**Qspring-1222（判断·注入）** 注入 List/Map 类型会收集容器内所有匹配类型的 Bean
**答案：对。** 解析：策略模式的 Spring 实现：注入 List<Handler> 或 Map<String,Handler>（key 为 Bean 名），配合 @Order 排序

**Qspring-1223（判断·注入）** 集合注入只会注入一个 Bean
**答案：错。** 正确表述：注入 List/Map 类型会收集容器内所有匹配类型的 Bean。原因：策略模式的 Spring 实现：注入 List<Handler> 或 Map<String,Handler>（key 为 Bean 名），配合 @Order 排序

**Qspring-1224（判断·注入）** 集合注入不支持泛型匹配
**答案：错。** 正确表述：注入 List/Map 类型会收集容器内所有匹配类型的 Bean。原因：策略模式的 Spring 实现：注入 List<Handler> 或 Map<String,Handler>（key 为 Bean 名），配合 @Order 排序

**Qspring-1225（判断·注入）** 无法控制顺序
**答案：错。** 正确表述：注入 List/Map 类型会收集容器内所有匹配类型的 Bean。原因：策略模式的 Spring 实现：注入 List<Handler> 或 Map<String,Handler>（key 为 Bean 名），配合 @Order 排序

**Qspring-1226（场景单选·注入）** 在工程实践中关于「集合注入」，下列做法符合推荐实践的是？
- A. 集合注入只会注入一个 Bean
- B. 集合注入不支持泛型匹配
- C. 策略模式落地标准写法
- D. 无法控制顺序
**答案：C**
**解析：** 推荐实践：策略模式落地标准写法。事实依据：注入 List/Map 类型会收集容器内所有匹配类型的 Bean。

**Qspring-1227（场景判断·注入）** 推荐实践：策略模式落地标准写法
**答案：对。** 解析：注入 List/Map 类型会收集容器内所有匹配类型的 Bean。原因：策略模式的 Spring 实现：注入 List<Handler> 或 Map<String,Handler>（key 为 Bean 名），配合 @Order 排序

**Qspring-1228（简答·注入）** 请说明「IoC」中集合注入的机制与使用要点。
**要点（标准答案）**：① 注入 List/Map 类型会收集容器内所有匹配类型的 Bean；② 原理：策略模式的 Spring 实现：注入 List<Handler> 或 Map<String,Handler>（key 为 Bean 名），配合 @Order 排序；③ 使用要点：策略模式落地标准写法。版本锚点：Spring 文档。

**Qspring-1229（单选·正向·配置）** 关于「IoC」的说法，正确的是？
- A. 占位符缺失默认返回空串
- B. SpEL 与占位符互斥
- C. @Value 只支持 ${} 语法
- D. @Value 支持 ${} 占位符与 #{} SpEL 表达式
**答案：D**
**解析：** @Value 支持 ${} 占位符与 #{} SpEL 表达式。原因：${db.url} 从 Environment 取值，#{systemProperties['x']} 是 SpEL，二者可嵌套，占位符找不到启动即报错（可给默认值 ${a:default}）。
**来源：** SP-027 · IoC（Spring 文档）

**Qspring-1230（判断·配置）** @Value 支持 ${} 占位符与 #{} SpEL 表达式
**答案：对。** 解析：${db.url} 从 Environment 取值，#{systemProperties['x']} 是 SpEL，二者可嵌套，占位符找不到启动即报错（可给默认值 ${a:default}）

**Qspring-1231（判断·配置）** @Value 只支持 ${} 语法
**答案：错。** 正确表述：@Value 支持 ${} 占位符与 #{} SpEL 表达式。原因：${db.url} 从 Environment 取值，#{systemProperties['x']} 是 SpEL，二者可嵌套，占位符找不到启动即报错（可给默认值 ${a:default}）

**Qspring-1232（判断·配置）** SpEL 与占位符互斥
**答案：错。** 正确表述：@Value 支持 ${} 占位符与 #{} SpEL 表达式。原因：${db.url} 从 Environment 取值，#{systemProperties['x']} 是 SpEL，二者可嵌套，占位符找不到启动即报错（可给默认值 ${a:default}）

**Qspring-1233（判断·配置）** 占位符缺失默认返回空串
**答案：错。** 正确表述：@Value 支持 ${} 占位符与 #{} SpEL 表达式。原因：${db.url} 从 Environment 取值，#{systemProperties['x']} 是 SpEL，二者可嵌套，占位符找不到启动即报错（可给默认值 ${a:default}）

**Qspring-1234（场景单选·配置）** 在工程实践中关于「@Value」，下列做法符合推荐实践的是？
- A. 配置注入推荐 @ConfigurationProperties 优先
- B. SpEL 与占位符互斥
- C. @Value 只支持 ${} 语法
- D. 占位符缺失默认返回空串
**答案：A**
**解析：** 推荐实践：配置注入推荐 @ConfigurationProperties 优先。事实依据：@Value 支持 ${} 占位符与 #{} SpEL 表达式。

**Qspring-1235（场景判断·配置）** 推荐实践：配置注入推荐 @ConfigurationProperties 优先
**答案：对。** 解析：@Value 支持 ${} 占位符与 #{} SpEL 表达式。原因：${db.url} 从 Environment 取值，#{systemProperties['x']} 是 SpEL，二者可嵌套，占位符找不到启动即报错（可给默认值 ${a:default}）

**Qspring-1236（填空·配置）** ______ 支持 ${} 占位符与 #{} SpEL 表达式
**答案：@Value**。解析：${db.url} 从 Environment 取值，#{systemProperties['x']} 是 SpEL，二者可嵌套，占位符找不到启动即报错（可给默认值 ${a:default}）

**Qspring-1237（简答·配置）** 请说明「IoC」中@Value的机制与使用要点。
**要点（标准答案）**：① @Value 支持 ${} 占位符与 #{} SpEL 表达式；② 原理：${db.url} 从 Environment 取值，#{systemProperties['x']} 是 SpEL，二者可嵌套，占位符找不到启动即报错（可给默认值 ${a:default}）；③ 使用要点：配置注入推荐 @ConfigurationProperties 优先。版本锚点：Spring 文档。

**Qspring-1238（单选·正向·配置绑定）** 关于「Boot」的说法，正确的是？
- A. 它需要手动调用 bind 方法
- B. @ConfigurationProperties 只能绑定 String
- C. relaxed binding 会模糊匹配任意拼写
- D. @ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据
**答案：D**
**解析：** @ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据。原因：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value。
**来源：** SP-028 · Boot（Boot 文档）

**Qspring-1239（判断·配置绑定）** @ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据
**答案：对。** 解析：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value

**Qspring-1240（判断·配置绑定）** @ConfigurationProperties 只能绑定 String
**答案：错。** 正确表述：@ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据。原因：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value

**Qspring-1241（判断·配置绑定）** 它需要手动调用 bind 方法
**答案：错。** 正确表述：@ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据。原因：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value

**Qspring-1242（判断·配置绑定）** relaxed binding 会模糊匹配任意拼写
**答案：错。** 正确表述：@ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据。原因：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value

**Qspring-1243（场景单选·配置绑定）** 在工程实践中关于「@ConfigurationProperties」，下列做法符合推荐实践的是？
- A. 它需要手动调用 bind 方法
- B. 配置项超过 3 个就建绑定类
- C. relaxed binding 会模糊匹配任意拼写
- D. @ConfigurationProperties 只能绑定 String
**答案：B**
**解析：** 推荐实践：配置项超过 3 个就建绑定类。事实依据：@ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据。

**Qspring-1244（场景判断·配置绑定）** 推荐实践：配置项超过 3 个就建绑定类
**答案：对。** 解析：@ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据。原因：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value

**Qspring-1245（填空·配置绑定）** ______ 批量绑定前缀下的属性并支持校验与元数据
**答案：@ConfigurationProperties**。解析：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value

**Qspring-1246（简答·配置绑定）** 请说明「Boot」中@ConfigurationProperties的机制与使用要点。
**要点（标准答案）**：① @ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据；② 原理：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value；③ 使用要点：配置项超过 3 个就建绑定类。版本锚点：Boot 文档。

**Qspring-1247（单选·正向·配置）** 关于「Boot」的说法，正确的是？
- A. 配置优先级：命令行参数 > 环境变量 > application-{profile} > application
- B. 命令行参数默认被忽略
- C. profile 文件优先级低于主文件
- D. application 文件优先级高于环境变量
**答案：A**
**解析：** 配置优先级：命令行参数 > 环境变量 > application-{profile} > application。原因：SpringApplication.setAddCommandLineProperties 默认开，K8s 部署靠环境变量覆盖文件配置。
**来源：** SP-029 · Boot（Boot 文档）

**Qspring-1248（判断·配置）** 配置优先级：命令行参数 > 环境变量 > application-{profile} > application
**答案：对。** 解析：SpringApplication.setAddCommandLineProperties 默认开，K8s 部署靠环境变量覆盖文件配置

**Qspring-1249（判断·配置）** application 文件优先级高于环境变量
**答案：错。** 正确表述：配置优先级：命令行参数 > 环境变量 > application-{profile} > application。原因：SpringApplication.setAddCommandLineProperties 默认开，K8s 部署靠环境变量覆盖文件配置

**Qspring-1250（判断·配置）** profile 文件优先级低于主文件
**答案：错。** 正确表述：配置优先级：命令行参数 > 环境变量 > application-{profile} > application。原因：SpringApplication.setAddCommandLineProperties 默认开，K8s 部署靠环境变量覆盖文件配置

**Qspring-1251（判断·配置）** 命令行参数默认被忽略
**答案：错。** 正确表述：配置优先级：命令行参数 > 环境变量 > application-{profile} > application。原因：SpringApplication.setAddCommandLineProperties 默认开，K8s 部署靠环境变量覆盖文件配置

**Qspring-1252（场景单选·配置）** 在工程实践中关于「优先级」，下列做法符合推荐实践的是？
- A. 命令行参数默认被忽略
- B. profile 文件优先级低于主文件
- C. 容器化配置注入的依据
- D. application 文件优先级高于环境变量
**答案：C**
**解析：** 推荐实践：容器化配置注入的依据。事实依据：配置优先级：命令行参数 > 环境变量 > application-{profile} > application。

**Qspring-1253（场景判断·配置）** 推荐实践：容器化配置注入的依据
**答案：对。** 解析：配置优先级：命令行参数 > 环境变量 > application-{profile} > application。原因：SpringApplication.setAddCommandLineProperties 默认开，K8s 部署靠环境变量覆盖文件配置

**Qspring-1254（填空·配置）** 配置______：命令行参数 > 环境变量 > application-{profile} > application
**答案：优先级**。解析：SpringApplication.setAddCommandLineProperties 默认开，K8s 部署靠环境变量覆盖文件配置

**Qspring-1255（简答·配置）** 请说明「Boot」中优先级的机制与使用要点。
**要点（标准答案）**：① 配置优先级：命令行参数 > 环境变量 > application-{profile} > application；② 原理：SpringApplication.setAddCommandLineProperties 默认开，K8s 部署靠环境变量覆盖文件配置；③ 使用要点：容器化配置注入的依据。版本锚点：Boot 文档。

**Qspring-1256（单选·正向·环境）** 关于「Boot」的说法，正确的是？
- A. 多个 profile 不能同时激活
- B. @Profile 与 @Conditional 无关
- C. @Profile 是运行时动态切换
- D. @Profile 按激活的 profile 决定 Bean 是否装配
**答案：D**
**解析：** @Profile 按激活的 profile 决定 Bean 是否装配。原因：@SpringBootTest 可设 profile，dev/test/prod 隔离数据源与中间件地址，spring.profiles.active 指定。
**来源：** SP-030 · Boot（Boot 文档）

**Qspring-1257（判断·环境）** @Profile 按激活的 profile 决定 Bean 是否装配
**答案：对。** 解析：@SpringBootTest 可设 profile，dev/test/prod 隔离数据源与中间件地址，spring.profiles.active 指定

**Qspring-1258（判断·环境）** @Profile 是运行时动态切换
**答案：错。** 正确表述：@Profile 按激活的 profile 决定 Bean 是否装配。原因：@SpringBootTest 可设 profile，dev/test/prod 隔离数据源与中间件地址，spring.profiles.active 指定

**Qspring-1259（判断·环境）** 多个 profile 不能同时激活
**答案：错。** 正确表述：@Profile 按激活的 profile 决定 Bean 是否装配。原因：@SpringBootTest 可设 profile，dev/test/prod 隔离数据源与中间件地址，spring.profiles.active 指定

**Qspring-1260（判断·环境）** @Profile 与 @Conditional 无关
**答案：错。** 正确表述：@Profile 按激活的 profile 决定 Bean 是否装配。原因：@SpringBootTest 可设 profile，dev/test/prod 隔离数据源与中间件地址，spring.profiles.active 指定

**Qspring-1261（场景单选·环境）** 在工程实践中关于「@Profile」，下列做法符合推荐实践的是？
- A. 多个 profile 不能同时激活
- B. @Profile 与 @Conditional 无关
- C. @Profile 是运行时动态切换
- D. 环境隔离标准方案
**答案：D**
**解析：** 推荐实践：环境隔离标准方案。事实依据：@Profile 按激活的 profile 决定 Bean 是否装配。

**Qspring-1262（场景判断·环境）** 推荐实践：环境隔离标准方案
**答案：对。** 解析：@Profile 按激活的 profile 决定 Bean 是否装配。原因：@SpringBootTest 可设 profile，dev/test/prod 隔离数据源与中间件地址，spring.profiles.active 指定

**Qspring-1263（填空·环境）** ______ 按激活的 profile 决定 Bean 是否装配
**答案：@Profile**。解析：@SpringBootTest 可设 profile，dev/test/prod 隔离数据源与中间件地址，spring.profiles.active 指定

**Qspring-1264（简答·环境）** 请说明「Boot」中@Profile的机制与使用要点。
**要点（标准答案）**：① @Profile 按激活的 profile 决定 Bean 是否装配；② 原理：@SpringBootTest 可设 profile，dev/test/prod 隔离数据源与中间件地址，spring.profiles.active 指定；③ 使用要点：环境隔离标准方案。版本锚点：Boot 文档。

**Qspring-1265（单选·正向·条件装配）** 关于「Boot」的说法，正确的是？
- A. OnMissingBean 与加载顺序无关
- B. @Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）
- C. @Conditional 在 Bean 创建后求值
- D. 条件注解可以加在方法体内部
**答案：B**
**解析：** @Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）。原因：Spring Boot 自动配置的全部开关逻辑基于条件装配，@ConditionalOnMissingBean 让用户定义优先于默认配置。
**来源：** SP-031 · Boot（Boot 文档）

**Qspring-1266（判断·条件装配）** @Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）
**答案：对。** 解析：Spring Boot 自动配置的全部开关逻辑基于条件装配，@ConditionalOnMissingBean 让用户定义优先于默认配置

**Qspring-1267（判断·条件装配）** @Conditional 在 Bean 创建后求值
**答案：错。** 正确表述：@Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）。原因：Spring Boot 自动配置的全部开关逻辑基于条件装配，@ConditionalOnMissingBean 让用户定义优先于默认配置

**Qspring-1268（判断·条件装配）** 条件注解可以加在方法体内部
**答案：错。** 正确表述：@Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）。原因：Spring Boot 自动配置的全部开关逻辑基于条件装配，@ConditionalOnMissingBean 让用户定义优先于默认配置

**Qspring-1269（判断·条件装配）** OnMissingBean 与加载顺序无关
**答案：错。** 正确表述：@Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）。原因：Spring Boot 自动配置的全部开关逻辑基于条件装配，@ConditionalOnMissingBean 让用户定义优先于默认配置

**Qspring-1270（场景单选·条件装配）** 在工程实践中关于「@Conditional」，下列做法符合推荐实践的是？
- A. 条件注解可以加在方法体内部
- B. 自定义 starter 的核心机制
- C. @Conditional 在 Bean 创建后求值
- D. OnMissingBean 与加载顺序无关
**答案：B**
**解析：** 推荐实践：自定义 starter 的核心机制。事实依据：@Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）。

**Qspring-1271（场景判断·条件装配）** 推荐实践：自定义 starter 的核心机制
**答案：对。** 解析：@Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）。原因：Spring Boot 自动配置的全部开关逻辑基于条件装配，@ConditionalOnMissingBean 让用户定义优先于默认配置

**Qspring-1272（填空·条件装配）** ______ 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）
**答案：@Conditional**。解析：Spring Boot 自动配置的全部开关逻辑基于条件装配，@ConditionalOnMissingBean 让用户定义优先于默认配置

**Qspring-1273（简答·条件装配）** 请说明「Boot」中@Conditional的机制与使用要点。
**要点（标准答案）**：① @Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）；② 原理：Spring Boot 自动配置的全部开关逻辑基于条件装配，@ConditionalOnMissingBean 让用户定义优先于默认配置；③ 使用要点：自定义 starter 的核心机制。版本锚点：Boot 文档。

**Qspring-1274（单选·正向·机制）** 关于「自动配置」的说法，正确的是？
- A. 自动配置在用户 Bean 之后加载
- B. AutoConfiguration.imports 是注解扫描结果
- C. spring.factories 至今仍是自动配置入口
- D. Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports
**答案：D**
**解析：** Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports。原因：Boot 3.0 彻底移除旧机制，自定义 starter 必须用新文件，老 starter 升级 Boot 3 前必须迁移。
**来源：** SP-032 · 自动配置（Boot 2.7/3.0）

**Qspring-1275（判断·机制）** Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports
**答案：对。** 解析：Boot 3.0 彻底移除旧机制，自定义 starter 必须用新文件，老 starter 升级 Boot 3 前必须迁移

**Qspring-1276（判断·机制）** spring.factories 至今仍是自动配置入口
**答案：错。** 正确表述：Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports。原因：Boot 3.0 彻底移除旧机制，自定义 starter 必须用新文件，老 starter 升级 Boot 3 前必须迁移

**Qspring-1277（判断·机制）** 自动配置在用户 Bean 之后加载
**答案：错。** 正确表述：Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports。原因：Boot 3.0 彻底移除旧机制，自定义 starter 必须用新文件，老 starter 升级 Boot 3 前必须迁移

**Qspring-1278（判断·机制）** AutoConfiguration.imports 是注解扫描结果
**答案：错。** 正确表述：Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports。原因：Boot 3.0 彻底移除旧机制，自定义 starter 必须用新文件，老 starter 升级 Boot 3 前必须迁移

**Qspring-1279（场景单选·机制）** 在工程实践中关于「AutoConfiguration.imports」，下列做法符合推荐实践的是？
- A. Boot 3 迁移必查项
- B. spring.factories 至今仍是自动配置入口
- C. AutoConfiguration.imports 是注解扫描结果
- D. 自动配置在用户 Bean 之后加载
**答案：A**
**解析：** 推荐实践：Boot 3 迁移必查项。事实依据：Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports。

**Qspring-1280（场景判断·机制）** 推荐实践：Boot 3 迁移必查项
**答案：对。** 解析：Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports。原因：Boot 3.0 彻底移除旧机制，自定义 starter 必须用新文件，老 starter 升级 Boot 3 前必须迁移

**Qspring-1281（填空·机制）** Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.______
**答案：AutoConfiguration.imports**。解析：Boot 3.0 彻底移除旧机制，自定义 starter 必须用新文件，老 starter 升级 Boot 3 前必须迁移

**Qspring-1282（简答·机制）** 请说明「自动配置」中AutoConfiguration.imports的机制与使用要点。
**要点（标准答案）**：① Boot 2.7+ 自动配置清单从 META-INF/spring.factories 迁移到 spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports；② 原理：Boot 3.0 彻底移除旧机制，自定义 starter 必须用新文件，老 starter 升级 Boot 3 前必须迁移；③ 使用要点：Boot 3 迁移必查项。版本锚点：Boot 2.7/3.0。

**Qspring-1283（单选·正向·启动）** 关于「Boot」的说法，正确的是？
- A. 组合注解不可拆开单独使用
- B. @SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合
- C. 它会扫描整个 classpath
- D. 扫描范围默认是主类同包之外
**答案：B**
**解析：** @SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合。原因：默认扫描主类所在包及子包，排包错位导致 Bean 扫不到是常见启动失败根因。
**来源：** SP-033 · Boot（Boot 文档）

**Qspring-1284（判断·启动）** @SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合
**答案：对。** 解析：默认扫描主类所在包及子包，排包错位导致 Bean 扫不到是常见启动失败根因

**Qspring-1285（判断·启动）** 它会扫描整个 classpath
**答案：错。** 正确表述：@SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合。原因：默认扫描主类所在包及子包，排包错位导致 Bean 扫不到是常见启动失败根因

**Qspring-1286（判断·启动）** 组合注解不可拆开单独使用
**答案：错。** 正确表述：@SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合。原因：默认扫描主类所在包及子包，排包错位导致 Bean 扫不到是常见启动失败根因

**Qspring-1287（判断·启动）** 扫描范围默认是主类同包之外
**答案：错。** 正确表述：@SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合。原因：默认扫描主类所在包及子包，排包错位导致 Bean 扫不到是常见启动失败根因

**Qspring-1288（场景单选·启动）** 在工程实践中关于「@SpringBootApplication」，下列做法符合推荐实践的是？
- A. 它会扫描整个 classpath
- B. 组合注解不可拆开单独使用
- C. 主类放包根（com.example.app 的顶层）
- D. 扫描范围默认是主类同包之外
**答案：C**
**解析：** 推荐实践：主类放包根（com.example.app 的顶层）。事实依据：@SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合。

**Qspring-1289（场景判断·启动）** 推荐实践：主类放包根（com.example.app 的顶层）
**答案：对。** 解析：@SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合。原因：默认扫描主类所在包及子包，排包错位导致 Bean 扫不到是常见启动失败根因

**Qspring-1290（填空·启动）** ______ 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合
**答案：@SpringBootApplication**。解析：默认扫描主类所在包及子包，排包错位导致 Bean 扫不到是常见启动失败根因

**Qspring-1291（简答·启动）** 请说明「Boot」中@SpringBootApplication的机制与使用要点。
**要点（标准答案）**：① @SpringBootApplication 是 @Configuration+@EnableAutoConfiguration+@ComponentScan 组合；② 原理：默认扫描主类所在包及子包，排包错位导致 Bean 扫不到是常见启动失败根因；③ 使用要点：主类放包根（com.example.app 的顶层）。版本锚点：Boot 文档。

**Qspring-1292（单选·正向·步骤）** 关于「自定义 starter」的说法，正确的是？
- A. starter 里要写业务逻辑
- B. 自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports
- C. 自定义 starter 必须用 @ComponentScan
- D. starter 命名随意
**答案：B**
**解析：** 自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports。原因：命名规范官方 x-spring-boot-starter 自家 spring-boot-starter-x，提供 spring-configuration-metadata.json 让 IDE 补全。
**来源：** SP-034 · 自定义 starter（Boot 文档）

**Qspring-1293（判断·步骤）** 自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports
**答案：对。** 解析：命名规范官方 x-spring-boot-starter 自家 spring-boot-starter-x，提供 spring-configuration-metadata.json 让 IDE 补全

**Qspring-1294（判断·步骤）** starter 里要写业务逻辑
**答案：错。** 正确表述：自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports。原因：命名规范官方 x-spring-boot-starter 自家 spring-boot-starter-x，提供 spring-configuration-metadata.json 让 IDE 补全

**Qspring-1295（判断·步骤）** 自定义 starter 必须用 @ComponentScan
**答案：错。** 正确表述：自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports。原因：命名规范官方 x-spring-boot-starter 自家 spring-boot-starter-x，提供 spring-configuration-metadata.json 让 IDE 补全

**Qspring-1296（判断·步骤）** starter 命名随意
**答案：错。** 正确表述：自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports。原因：命名规范官方 x-spring-boot-starter 自家 spring-boot-starter-x，提供 spring-configuration-metadata.json 让 IDE 补全

**Qspring-1297（场景单选·步骤）** 在工程实践中关于「starter」，下列做法符合推荐实践的是？
- A. 自定义 starter 必须用 @ComponentScan
- B. starter 命名随意
- C. starter 里要写业务逻辑
- D. 公共组件 SDK 化标准方案
**答案：D**
**解析：** 推荐实践：公共组件 SDK 化标准方案。事实依据：自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports。

**Qspring-1298（场景判断·步骤）** 推荐实践：公共组件 SDK 化标准方案
**答案：对。** 解析：自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports。原因：命名规范官方 x-spring-boot-starter 自家 spring-boot-starter-x，提供 spring-configuration-metadata.json 让 IDE 补全

**Qspring-1299（填空·步骤）** 自定义 ______：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports
**答案：starter**。解析：命名规范官方 x-spring-boot-starter 自家 spring-boot-starter-x，提供 spring-configuration-metadata.json 让 IDE 补全

**Qspring-1300（简答·步骤）** 请说明「自定义 starter」中starter的机制与使用要点。
**要点（标准答案）**：① 自定义 starter：写自动配置类+条件注解+配置绑定+注册到 AutoConfiguration.imports；② 原理：命名规范官方 x-spring-boot-starter 自家 spring-boot-starter-x，提供 spring-configuration-metadata.json 让 IDE 补全；③ 使用要点：公共组件 SDK 化标准方案。版本锚点：Boot 文档。

**Qspring-1301（单选·正向·proxyBeanMethods）** 关于「配置类」的说法，正确的是？
- A. lite 模式下 @Bean 互调仍返回单例
- B. @Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理
- C. @Bean 互调与代理无关
- D. proxyBeanMethods 默认是 false
**答案：B**
**解析：** @Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。原因：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）。
**来源：** SP-035 · 配置类（Boot 文档）

**Qspring-1302（判断·proxyBeanMethods）** @Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理
**答案：对。** 解析：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）

**Qspring-1303（判断·proxyBeanMethods）** lite 模式下 @Bean 互调仍返回单例
**答案：错。** 正确表述：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。原因：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）

**Qspring-1304（判断·proxyBeanMethods）** proxyBeanMethods 默认是 false
**答案：错。** 正确表述：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。原因：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）

**Qspring-1305（判断·proxyBeanMethods）** @Bean 互调与代理无关
**答案：错。** 正确表述：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。原因：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）

**Qspring-1306（场景单选·proxyBeanMethods）** 在工程实践中关于「lite mode」，下列做法符合推荐实践的是？
- A. 性能敏感的启动优化点
- B. @Bean 互调与代理无关
- C. proxyBeanMethods 默认是 false
- D. lite 模式下 @Bean 互调仍返回单例
**答案：A**
**解析：** 推荐实践：性能敏感的启动优化点。事实依据：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。

**Qspring-1307（场景判断·proxyBeanMethods）** 推荐实践：性能敏感的启动优化点
**答案：对。** 解析：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。原因：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）

**Qspring-1308（简答·proxyBeanMethods）** 请说明「配置类」中lite mode的机制与使用要点。
**要点（标准答案）**：① @Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理；② 原理：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）；③ 使用要点：性能敏感的启动优化点。版本锚点：Boot 文档。

**Qspring-1309（单选·正向·陷阱）** 关于「配置类」的说法，正确的是？
- A. full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例
- B. lite 与 full 模式行为相同
- C. 配置类不用 CGLIB 增强
- D. @Bean 方法互调会创建两个实例
**答案：A**
**解析：** full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例。原因：配置类被 CGLIB 子类化拦截方法调用，保证语义等价于容器查找，这就是 proxyBeanMethods 区分 full/lite 的原因。
**来源：** SP-036 · 配置类（Spring 源码）

**Qspring-1310（判断·陷阱）** full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例
**答案：对。** 解析：配置类被 CGLIB 子类化拦截方法调用，保证语义等价于容器查找，这就是 proxyBeanMethods 区分 full/lite 的原因

**Qspring-1311（判断·陷阱）** @Bean 方法互调会创建两个实例
**答案：错。** 正确表述：full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例。原因：配置类被 CGLIB 子类化拦截方法调用，保证语义等价于容器查找，这就是 proxyBeanMethods 区分 full/lite 的原因

**Qspring-1312（判断·陷阱）** 配置类不用 CGLIB 增强
**答案：错。** 正确表述：full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例。原因：配置类被 CGLIB 子类化拦截方法调用，保证语义等价于容器查找，这就是 proxyBeanMethods 区分 full/lite 的原因

**Qspring-1313（判断·陷阱）** lite 与 full 模式行为相同
**答案：错。** 正确表述：full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例。原因：配置类被 CGLIB 子类化拦截方法调用，保证语义等价于容器查找，这就是 proxyBeanMethods 区分 full/lite 的原因

**Qspring-1314（场景单选·陷阱）** 在工程实践中关于「@Bean 互调」，下列做法符合推荐实践的是？
- A. 配置类不用 CGLIB 增强
- B. lite 与 full 模式行为相同
- C. 理解配置类原理的经典题
- D. @Bean 方法互调会创建两个实例
**答案：C**
**解析：** 推荐实践：理解配置类原理的经典题。事实依据：full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例。

**Qspring-1315（场景判断·陷阱）** 推荐实践：理解配置类原理的经典题
**答案：对。** 解析：full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例。原因：配置类被 CGLIB 子类化拦截方法调用，保证语义等价于容器查找，这就是 proxyBeanMethods 区分 full/lite 的原因

**Qspring-1316（简答·陷阱）** 请说明「配置类」中@Bean 互调的机制与使用要点。
**要点（标准答案）**：① full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例；② 原理：配置类被 CGLIB 子类化拦截方法调用，保证语义等价于容器查找，这就是 proxyBeanMethods 区分 full/lite 的原因；③ 使用要点：理解配置类原理的经典题。版本锚点：Spring 源码。

**Qspring-1317（单选·正向·代理）** 关于「AOP」的说法，正确的是？
- A. 有接口时 CGLIB 不能用
- B. JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求
- C. CGLIB 可以代理 final 类
- D. JDK 代理性能永远更差
**答案：B**
**解析：** JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求。原因：JDK 代理实现 Proxy+InvocationHandler，CGLIB 用 ASM 生成子类覆写方法，final 类与 final/private 方法无法被 CGLIB 增强且 final 方法不进入代理。
**来源：** SP-037 · AOP（Spring 文档）

**Qspring-1318（判断·代理）** JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求
**答案：对。** 解析：JDK 代理实现 Proxy+InvocationHandler，CGLIB 用 ASM 生成子类覆写方法，final 类与 final/private 方法无法被 CGLIB 增强且 final 方法不进入代理

**Qspring-1319（判断·代理）** JDK 代理性能永远更差
**答案：错。** 正确表述：JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求。原因：JDK 代理实现 Proxy+InvocationHandler，CGLIB 用 ASM 生成子类覆写方法，final 类与 final/private 方法无法被 CGLIB 增强且 final 方法不进入代理

**Qspring-1320（判断·代理）** CGLIB 可以代理 final 类
**答案：错。** 正确表述：JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求。原因：JDK 代理实现 Proxy+InvocationHandler，CGLIB 用 ASM 生成子类覆写方法，final 类与 final/private 方法无法被 CGLIB 增强且 final 方法不进入代理

**Qspring-1321（判断·代理）** 有接口时 CGLIB 不能用
**答案：错。** 正确表述：JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求。原因：JDK 代理实现 Proxy+InvocationHandler，CGLIB 用 ASM 生成子类覆写方法，final 类与 final/private 方法无法被 CGLIB 增强且 final 方法不进入代理

**Qspring-1322（场景单选·代理）** 在工程实践中关于「JDK vs CGLIB」，下列做法符合推荐实践的是？
- A. JDK 代理性能永远更差
- B. 回答 AOP 代理选型
- C. 有接口时 CGLIB 不能用
- D. CGLIB 可以代理 final 类
**答案：B**
**解析：** 推荐实践：回答 AOP 代理选型。事实依据：JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求。

**Qspring-1323（场景判断·代理）** 推荐实践：回答 AOP 代理选型
**答案：对。** 解析：JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求。原因：JDK 代理实现 Proxy+InvocationHandler，CGLIB 用 ASM 生成子类覆写方法，final 类与 final/private 方法无法被 CGLIB 增强且 final 方法不进入代理

**Qspring-1324（简答·代理）** 请说明「AOP」中JDK vs CGLIB的机制与使用要点。
**要点（标准答案）**：① JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求；② 原理：JDK 代理实现 Proxy+InvocationHandler，CGLIB 用 ASM 生成子类覆写方法，final 类与 final/private 方法无法被 CGLIB 增强且 final 方法不进入代理；③ 使用要点：回答 AOP 代理选型。版本锚点：Spring 文档。

**Qspring-1325（单选·正向·默认）** 关于「AOP」的说法，正确的是？
- A. Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）
- B. proxy-target-class 默认 false
- C. 切换 JDK 代理是性能优化
- D. Boot 默认 JDK 代理
**答案：A**
**解析：** Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）。原因：统一代理避免"有接口用 JDK 无接口用 CGLIB"的类型不一致问题，注入时按具体类型而非接口。
**来源：** SP-038 · AOP（Boot 2.0）

**Qspring-1326（判断·默认）** Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）
**答案：对。** 解析：统一代理避免"有接口用 JDK 无接口用 CGLIB"的类型不一致问题，注入时按具体类型而非接口

**Qspring-1327（判断·默认）** Boot 默认 JDK 代理
**答案：错。** 正确表述：Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）。原因：统一代理避免"有接口用 JDK 无接口用 CGLIB"的类型不一致问题，注入时按具体类型而非接口

**Qspring-1328（判断·默认）** proxy-target-class 默认 false
**答案：错。** 正确表述：Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）。原因：统一代理避免"有接口用 JDK 无接口用 CGLIB"的类型不一致问题，注入时按具体类型而非接口

**Qspring-1329（判断·默认）** 切换 JDK 代理是性能优化
**答案：错。** 正确表述：Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）。原因：统一代理避免"有接口用 JDK 无接口用 CGLIB"的类型不一致问题，注入时按具体类型而非接口

**Qspring-1330（场景单选·默认）** 在工程实践中关于「proxy-target-class」，下列做法符合推荐实践的是？
- A. 切换 JDK 代理是性能优化
- B. Boot 默认 JDK 代理
- C. proxy-target-class 默认 false
- D. Boot 2 迁移说明
**答案：D**
**解析：** 推荐实践：Boot 2 迁移说明。事实依据：Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）。

**Qspring-1331（场景判断·默认）** 推荐实践：Boot 2 迁移说明
**答案：对。** 解析：Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）。原因：统一代理避免"有接口用 JDK 无接口用 CGLIB"的类型不一致问题，注入时按具体类型而非接口

**Qspring-1332（填空·默认）** Spring Boot 2.0 起 AOP 默认强制 CGLIB（______=true）
**答案：proxy-target-class**。解析：统一代理避免"有接口用 JDK 无接口用 CGLIB"的类型不一致问题，注入时按具体类型而非接口

**Qspring-1333（简答·默认）** 请说明「AOP」中proxy-target-class的机制与使用要点。
**要点（标准答案）**：① Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）；② 原理：统一代理避免"有接口用 JDK 无接口用 CGLIB"的类型不一致问题，注入时按具体类型而非接口；③ 使用要点：Boot 2 迁移说明。版本锚点：Boot 2.0。

**Qspring-1334（单选·正向·通知）** 关于「AOP」的说法，正确的是？
- A. AfterReturning 先于 After 执行
- B. Around 会跳过 After
- C. 通知顺序由方法名决定
- D. 同一切面内通知顺序：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing
**答案：D**
**解析：** 同一切面内通知顺序：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing。原因：Spring 5.2.7 之前 @After 与 @AfterReturning 顺序在不同版本不稳定，5.2.7 统一为上述顺序（面试背当前版本语义）。
**来源：** SP-039 · AOP（Spring 5.2.7）

**Qspring-1335（判断·通知）** 同一切面内通知顺序：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing
**答案：对。** 解析：Spring 5.2.7 之前 @After 与 @AfterReturning 顺序在不同版本不稳定，5.2.7 统一为上述顺序（面试背当前版本语义）

**Qspring-1336（判断·通知）** AfterReturning 先于 After 执行
**答案：错。** 正确表述：同一切面内通知顺序：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing。原因：Spring 5.2.7 之前 @After 与 @AfterReturning 顺序在不同版本不稳定，5.2.7 统一为上述顺序（面试背当前版本语义）

**Qspring-1337（判断·通知）** Around 会跳过 After
**答案：错。** 正确表述：同一切面内通知顺序：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing。原因：Spring 5.2.7 之前 @After 与 @AfterReturning 顺序在不同版本不稳定，5.2.7 统一为上述顺序（面试背当前版本语义）

**Qspring-1338（判断·通知）** 通知顺序由方法名决定
**答案：错。** 正确表述：同一切面内通知顺序：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing。原因：Spring 5.2.7 之前 @After 与 @AfterReturning 顺序在不同版本不稳定，5.2.7 统一为上述顺序（面试背当前版本语义）

**Qspring-1339（场景单选·通知）** 在工程实践中关于「顺序」，下列做法符合推荐实践的是？
- A. AOP 日志/审计切面正确性依赖此序
- B. 通知顺序由方法名决定
- C. Around 会跳过 After
- D. AfterReturning 先于 After 执行
**答案：A**
**解析：** 推荐实践：AOP 日志/审计切面正确性依赖此序。事实依据：同一切面内通知顺序：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing。

**Qspring-1340（场景判断·通知）** 推荐实践：AOP 日志/审计切面正确性依赖此序
**答案：对。** 解析：同一切面内通知顺序：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing。原因：Spring 5.2.7 之前 @After 与 @AfterReturning 顺序在不同版本不稳定，5.2.7 统一为上述顺序（面试背当前版本语义）

**Qspring-1341（填空·通知）** 同一切面内通知______：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing
**答案：顺序**。解析：Spring 5.2.7 之前 @After 与 @AfterReturning 顺序在不同版本不稳定，5.2.7 统一为上述顺序（面试背当前版本语义）

**Qspring-1342（简答·通知）** 请说明「AOP」中顺序的机制与使用要点。
**要点（标准答案）**：① 同一切面内通知顺序：Around 前段、Before、目标方法、Around 后段、After、AfterReturning/AfterThrowing；② 原理：Spring 5.2.7 之前 @After 与 @AfterReturning 顺序在不同版本不稳定，5.2.7 统一为上述顺序（面试背当前版本语义）；③ 使用要点：AOP 日志/审计切面正确性依赖此序。版本锚点：Spring 5.2.7。

**Qspring-1343（单选·正向·排序）** 关于「AOP」的说法，正确的是？
- A. 未标注 @Order 的切面先执行
- B. @Order 数字越大优先级越高
- C. @Order 可以加在方法参数上
- D. 多个切面的执行顺序由 @Order 值决定数字越小优先级越高
**答案：D**
**解析：** 多个切面的执行顺序由 @Order 值决定数字越小优先级越高。原因：事务切面 Order 默认 Ordered.LOWEST_PRECEDENCE，自定义切面想包在事务外需要更小值（先进入后退出）。
**来源：** SP-040 · AOP（Spring 文档）

**Qspring-1344（判断·排序）** 多个切面的执行顺序由 @Order 值决定数字越小优先级越高
**答案：对。** 解析：事务切面 Order 默认 Ordered.LOWEST_PRECEDENCE，自定义切面想包在事务外需要更小值（先进入后退出）

**Qspring-1345（判断·排序）** @Order 数字越大优先级越高
**答案：错。** 正确表述：多个切面的执行顺序由 @Order 值决定数字越小优先级越高。原因：事务切面 Order 默认 Ordered.LOWEST_PRECEDENCE，自定义切面想包在事务外需要更小值（先进入后退出）

**Qspring-1346（判断·排序）** 未标注 @Order 的切面先执行
**答案：错。** 正确表述：多个切面的执行顺序由 @Order 值决定数字越小优先级越高。原因：事务切面 Order 默认 Ordered.LOWEST_PRECEDENCE，自定义切面想包在事务外需要更小值（先进入后退出）

**Qspring-1347（判断·排序）** @Order 可以加在方法参数上
**答案：错。** 正确表述：多个切面的执行顺序由 @Order 值决定数字越小优先级越高。原因：事务切面 Order 默认 Ordered.LOWEST_PRECEDENCE，自定义切面想包在事务外需要更小值（先进入后退出）

**Qspring-1348（场景单选·排序）** 在工程实践中关于「@Order」，下列做法符合推荐实践的是？
- A. @Order 可以加在方法参数上
- B. 未标注 @Order 的切面先执行
- C. @Order 数字越大优先级越高
- D. 切面叠加时的执行矩阵
**答案：D**
**解析：** 推荐实践：切面叠加时的执行矩阵。事实依据：多个切面的执行顺序由 @Order 值决定数字越小优先级越高。

**Qspring-1349（场景判断·排序）** 推荐实践：切面叠加时的执行矩阵
**答案：对。** 解析：多个切面的执行顺序由 @Order 值决定数字越小优先级越高。原因：事务切面 Order 默认 Ordered.LOWEST_PRECEDENCE，自定义切面想包在事务外需要更小值（先进入后退出）

**Qspring-1350（填空·排序）** 多个切面的执行顺序由 ______ 值决定数字越小优先级越高
**答案：@Order**。解析：事务切面 Order 默认 Ordered.LOWEST_PRECEDENCE，自定义切面想包在事务外需要更小值（先进入后退出）

**Qspring-1351（简答·排序）** 请说明「AOP」中@Order的机制与使用要点。
**要点（标准答案）**：① 多个切面的执行顺序由 @Order 值决定数字越小优先级越高；② 原理：事务切面 Order 默认 Ordered.LOWEST_PRECEDENCE，自定义切面想包在事务外需要更小值（先进入后退出）；③ 使用要点：切面叠加时的执行矩阵。版本锚点：Spring 文档。

**Qspring-1352（单选·正向·失效）** 关于「AOP」的说法，正确的是？
- A. 把方法改 public 就能解决自调用
- B. 自调用 AOP 依然生效
- C. 只有 @Transactional 受影响
- D. 同类内 this 调用注解方法 AOP 失效（事务/异步/缓存）
**答案：D**
**解析：** 同类内 this 调用注解方法 AOP 失效（事务/异步/缓存）。原因：this 指向原始对象而非代理，绕过代理拦截，解法：注入自身代理、AopContext.currentProxy（需 exposeProxy）、拆类。
**来源：** SP-041 · AOP（实战共识）

**Qspring-1353（判断·失效）** 同类内 this 调用注解方法 AOP 失效（事务/异步/缓存）
**答案：对。** 解析：this 指向原始对象而非代理，绕过代理拦截，解法：注入自身代理、AopContext.currentProxy（需 exposeProxy）、拆类

**Qspring-1354（判断·失效）** 自调用 AOP 依然生效
**答案：错。** 正确表述：同类内 this 调用注解方法 AOP 失效（事务/异步/缓存）。原因：this 指向原始对象而非代理，绕过代理拦截，解法：注入自身代理、AopContext.currentProxy（需 exposeProxy）、拆类

**Qspring-1355（判断·失效）** 只有 @Transactional 受影响
**答案：错。** 正确表述：同类内 this 调用注解方法 AOP 失效（事务/异步/缓存）。原因：this 指向原始对象而非代理，绕过代理拦截，解法：注入自身代理、AopContext.currentProxy（需 exposeProxy）、拆类

**Qspring-1356（判断·失效）** 把方法改 public 就能解决自调用
**答案：错。** 正确表述：同类内 this 调用注解方法 AOP 失效（事务/异步/缓存）。原因：this 指向原始对象而非代理，绕过代理拦截，解法：注入自身代理、AopContext.currentProxy（需 exposeProxy）、拆类

**Qspring-1357（场景单选·失效）** 在工程实践中关于「自调用」，下列做法符合推荐实践的是？
- A. 事务/异步注解失效第一原因
- B. 只有 @Transactional 受影响
- C. 自调用 AOP 依然生效
- D. 把方法改 public 就能解决自调用
**答案：A**
**解析：** 推荐实践：事务/异步注解失效第一原因。事实依据：同类内 this 调用注解方法 AOP 失效（事务/异步/缓存）。

**Qspring-1358（场景判断·失效）** 推荐实践：事务/异步注解失效第一原因
**答案：对。** 解析：同类内 this 调用注解方法 AOP 失效（事务/异步/缓存）。原因：this 指向原始对象而非代理，绕过代理拦截，解法：注入自身代理、AopContext.currentProxy（需 exposeProxy）、拆类

**Qspring-1359（简答·失效）** 请说明「AOP」中自调用的机制与使用要点。
**要点（标准答案）**：① 同类内 this 调用注解方法 AOP 失效（事务/异步/缓存）；② 原理：this 指向原始对象而非代理，绕过代理拦截，解法：注入自身代理、AopContext.currentProxy（需 exposeProxy）、拆类；③ 使用要点：事务/异步注解失效第一原因。版本锚点：实战共识。

**Qspring-1360（单选·正向·失效）** 关于「AOP」的说法，正确的是？
- A. final 方法切面正常工作
- B. CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效
- C. static 方法可以被切面增强
- D. CGLIB 能代理 private 方法
**答案：B**
**解析：** CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效。原因：代理通过子类覆写实现增强，final/private 方法不可覆写导致绕过代理。
**来源：** SP-042 · AOP（CGLIB 限制）

**Qspring-1361（判断·失效）** CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效
**答案：对。** 解析：代理通过子类覆写实现增强，final/private 方法不可覆写导致绕过代理

**Qspring-1362（判断·失效）** CGLIB 能代理 private 方法
**答案：错。** 正确表述：CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效。原因：代理通过子类覆写实现增强，final/private 方法不可覆写导致绕过代理

**Qspring-1363（判断·失效）** final 方法切面正常工作
**答案：错。** 正确表述：CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效。原因：代理通过子类覆写实现增强，final/private 方法不可覆写导致绕过代理

**Qspring-1364（判断·失效）** static 方法可以被切面增强
**答案：错。** 正确表述：CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效。原因：代理通过子类覆写实现增强，final/private 方法不可覆写导致绕过代理

**Qspring-1365（场景单选·失效）** 在工程实践中关于「final 方法」，下列做法符合推荐实践的是？
- A. 注解方法避免 private/final/static
- B. static 方法可以被切面增强
- C. final 方法切面正常工作
- D. CGLIB 能代理 private 方法
**答案：A**
**解析：** 推荐实践：注解方法避免 private/final/static。事实依据：CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效。

**Qspring-1366（场景判断·失效）** 推荐实践：注解方法避免 private/final/static
**答案：对。** 解析：CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效。原因：代理通过子类覆写实现增强，final/private 方法不可覆写导致绕过代理

**Qspring-1367（简答·失效）** 请说明「AOP」中final 方法的机制与使用要点。
**要点（标准答案）**：① CGLIB 无法覆写 final 与 private 方法这些方法上的切面失效；② 原理：代理通过子类覆写实现增强，final/private 方法不可覆写导致绕过代理；③ 使用要点：注解方法避免 private/final/static。版本锚点：CGLIB 限制。

**Qspring-1368（单选·正向·表达式）** 关于「AOP」的说法，正确的是？
- A. execution 表达式：修饰符 返回类型 包.类.方法(参数) throws
- B. (..) 与 (*) 语义相同
- C. execution 只能匹配 public 方法
- D. 表达式大小写敏感无所谓
**答案：A**
**解析：** execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。原因：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配。
**来源：** SP-043 · AOP（AspectJ 语法）

**Qspring-1369（判断·表达式）** execution 表达式：修饰符 返回类型 包.类.方法(参数) throws
**答案：对。** 解析：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配

**Qspring-1370（判断·表达式）** execution 只能匹配 public 方法
**答案：错。** 正确表述：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。原因：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配

**Qspring-1371（判断·表达式）** (..) 与 (*) 语义相同
**答案：错。** 正确表述：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。原因：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配

**Qspring-1372（判断·表达式）** 表达式大小写敏感无所谓
**答案：错。** 正确表述：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。原因：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配

**Qspring-1373（场景单选·表达式）** 在工程实践中关于「execution」，下列做法符合推荐实践的是？
- A. 表达式大小写敏感无所谓
- B. execution 只能匹配 public 方法
- C. 写切点前先明确匹配范围
- D. (..) 与 (*) 语义相同
**答案：C**
**解析：** 推荐实践：写切点前先明确匹配范围。事实依据：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。

**Qspring-1374（场景判断·表达式）** 推荐实践：写切点前先明确匹配范围
**答案：对。** 解析：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。原因：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配

**Qspring-1375（填空·表达式）** ______ 表达式：修饰符 返回类型 包.类.方法(参数) throws
**答案：execution**。解析：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配

**Qspring-1376（简答·表达式）** 请说明「AOP」中execution的机制与使用要点。
**要点（标准答案）**：① execution 表达式：修饰符 返回类型 包.类.方法(参数) throws；② 原理：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配；③ 使用要点：写切点前先明确匹配范围。版本锚点：AspectJ 语法。

**Qspring-1377（单选·正向·织入）** 关于「AOP」的说法，正确的是？
- A. Spring AOP 支持 LTW
- B. AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP
- C. AspectJ 是运行时代理
- D. LTW 无法拦截构造器
**答案：B**
**解析：** AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP。原因：可增强 private/final/构造器/字段，需要 -javaagent 加载织入器，全链路监控 agent 就是 LTW 实现。
**来源：** SP-044 · AOP（AspectJ 文档）

**Qspring-1378（判断·织入）** AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP
**答案：对。** 解析：可增强 private/final/构造器/字段，需要 -javaagent 加载织入器，全链路监控 agent 就是 LTW 实现

**Qspring-1379（判断·织入）** Spring AOP 支持 LTW
**答案：错。** 正确表述：AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP。原因：可增强 private/final/构造器/字段，需要 -javaagent 加载织入器，全链路监控 agent 就是 LTW 实现

**Qspring-1380（判断·织入）** LTW 无法拦截构造器
**答案：错。** 正确表述：AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP。原因：可增强 private/final/构造器/字段，需要 -javaagent 加载织入器，全链路监控 agent 就是 LTW 实现

**Qspring-1381（判断·织入）** AspectJ 是运行时代理
**答案：错。** 正确表述：AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP。原因：可增强 private/final/构造器/字段，需要 -javaagent 加载织入器，全链路监控 agent 就是 LTW 实现

**Qspring-1382（场景单选·织入）** 在工程实践中关于「LTW」，下列做法符合推荐实践的是？
- A. Spring AOP 支持 LTW
- B. AspectJ 是运行时代理
- C. LTW 无法拦截构造器
- D. 需要跨方法深度增强时用 AspectJ
**答案：D**
**解析：** 推荐实践：需要跨方法深度增强时用 AspectJ。事实依据：AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP。

**Qspring-1383（场景判断·织入）** 推荐实践：需要跨方法深度增强时用 AspectJ
**答案：对。** 解析：AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP。原因：可增强 private/final/构造器/字段，需要 -javaagent 加载织入器，全链路监控 agent 就是 LTW 实现

**Qspring-1384（填空·织入）** AspectJ 支持编译期与类加载期织入（______）能力强于 Spring AOP
**答案：LTW**。解析：可增强 private/final/构造器/字段，需要 -javaagent 加载织入器，全链路监控 agent 就是 LTW 实现

**Qspring-1385（简答·织入）** 请说明「AOP」中LTW的机制与使用要点。
**要点（标准答案）**：① AspectJ 支持编译期与类加载期织入（LTW）能力强于 Spring AOP；② 原理：可增强 private/final/构造器/字段，需要 -javaagent 加载织入器，全链路监控 agent 就是 LTW 实现；③ 使用要点：需要跨方法深度增强时用 AspectJ。版本锚点：AspectJ 文档。

**Qspring-1386（单选·正向·实践）** 关于「AOP」的说法，正确的是？
- A. 它是推荐的解自调用方式
- B. exposeProxy 默认开启
- C. currentProxy 无需任何开关
- D. AopContext.currentProxy 需要开启 exposeProxy=true 才能用
**答案：D**
**解析：** AopContext.currentProxy 需要开启 exposeProxy=true 才能用。原因：代理内部保存当前代理引用暴露到 ThreadLocal，自调用场景通过它再走一遍代理，代码侵入大，首选拆类或注入自身。
**来源：** SP-045 · AOP（Spring 文档）

**Qspring-1387（判断·实践）** AopContext.currentProxy 需要开启 exposeProxy=true 才能用
**答案：对。** 解析：代理内部保存当前代理引用暴露到 ThreadLocal，自调用场景通过它再走一遍代理，代码侵入大，首选拆类或注入自身

**Qspring-1388（判断·实践）** exposeProxy 默认开启
**答案：错。** 正确表述：AopContext.currentProxy 需要开启 exposeProxy=true 才能用。原因：代理内部保存当前代理引用暴露到 ThreadLocal，自调用场景通过它再走一遍代理，代码侵入大，首选拆类或注入自身

**Qspring-1389（判断·实践）** currentProxy 无需任何开关
**答案：错。** 正确表述：AopContext.currentProxy 需要开启 exposeProxy=true 才能用。原因：代理内部保存当前代理引用暴露到 ThreadLocal，自调用场景通过它再走一遍代理，代码侵入大，首选拆类或注入自身

**Qspring-1390（判断·实践）** 它是推荐的解自调用方式
**答案：错。** 正确表述：AopContext.currentProxy 需要开启 exposeProxy=true 才能用。原因：代理内部保存当前代理引用暴露到 ThreadLocal，自调用场景通过它再走一遍代理，代码侵入大，首选拆类或注入自身

**Qspring-1391（场景单选·实践）** 在工程实践中关于「exposeProxy」，下列做法符合推荐实践的是？
- A. exposeProxy 默认开启
- B. currentProxy 无需任何开关
- C. 它是推荐的解自调用方式
- D. 理解自调用问题的备选解
**答案：D**
**解析：** 推荐实践：理解自调用问题的备选解。事实依据：AopContext.currentProxy 需要开启 exposeProxy=true 才能用。

**Qspring-1392（场景判断·实践）** 推荐实践：理解自调用问题的备选解
**答案：对。** 解析：AopContext.currentProxy 需要开启 exposeProxy=true 才能用。原因：代理内部保存当前代理引用暴露到 ThreadLocal，自调用场景通过它再走一遍代理，代码侵入大，首选拆类或注入自身

**Qspring-1393（填空·实践）** AopContext.currentProxy 需要开启 ______=true 才能用
**答案：exposeProxy**。解析：代理内部保存当前代理引用暴露到 ThreadLocal，自调用场景通过它再走一遍代理，代码侵入大，首选拆类或注入自身

**Qspring-1394（简答·实践）** 请说明「AOP」中exposeProxy的机制与使用要点。
**要点（标准答案）**：① AopContext.currentProxy 需要开启 exposeProxy=true 才能用；② 原理：代理内部保存当前代理引用暴露到 ThreadLocal，自调用场景通过它再走一遍代理，代码侵入大，首选拆类或注入自身；③ 使用要点：理解自调用问题的备选解。版本锚点：Spring 文档。

**Qspring-1395（单选·正向·原理）** 关于「事务」的说法，正确的是？
- A. @Transactional 基于 AOP 代理由 TransactionInterceptor 实现
- B. 开启事务会立即提交一次
- C. 事务与 AOP 无关
- D. @Transactional 是 JDBC 驱动实现
**答案：A**
**解析：** @Transactional 基于 AOP 代理由 TransactionInterceptor 实现。原因：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析。
**来源：** SP-046 · 事务（Spring 源码）

**Qspring-1396（判断·原理）** @Transactional 基于 AOP 代理由 TransactionInterceptor 实现
**答案：对。** 解析：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析

**Qspring-1397（判断·原理）** @Transactional 是 JDBC 驱动实现
**答案：错。** 正确表述：@Transactional 基于 AOP 代理由 TransactionInterceptor 实现。原因：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析

**Qspring-1398（判断·原理）** 事务与 AOP 无关
**答案：错。** 正确表述：@Transactional 基于 AOP 代理由 TransactionInterceptor 实现。原因：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析

**Qspring-1399（判断·原理）** 开启事务会立即提交一次
**答案：错。** 正确表述：@Transactional 基于 AOP 代理由 TransactionInterceptor 实现。原因：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析

**Qspring-1400（场景单选·原理）** 在工程实践中关于「TransactionInterceptor」，下列做法符合推荐实践的是？
- A. 事务与 AOP 无关
- B. 开启事务会立即提交一次
- C. @Transactional 是 JDBC 驱动实现
- D. 事务原理是 AOP 应用的最佳案例
**答案：D**
**解析：** 推荐实践：事务原理是 AOP 应用的最佳案例。事实依据：@Transactional 基于 AOP 代理由 TransactionInterceptor 实现。

**Qspring-1401（场景判断·原理）** 推荐实践：事务原理是 AOP 应用的最佳案例
**答案：对。** 解析：@Transactional 基于 AOP 代理由 TransactionInterceptor 实现。原因：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析

**Qspring-1402（填空·原理）** @Transactional 基于 AOP 代理由 ______ 实现
**答案：TransactionInterceptor**。解析：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析

**Qspring-1403（简答·原理）** 请说明「事务」中TransactionInterceptor的机制与使用要点。
**要点（标准答案）**：① @Transactional 基于 AOP 代理由 TransactionInterceptor 实现；② 原理：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析；③ 使用要点：事务原理是 AOP 应用的最佳案例。版本锚点：Spring 源码。

**Qspring-1404（单选·正向·失效）** 关于「事务」的说法，正确的是？
- A. 自调用时事务仍生效
- B. 把方法改 private 能修复
- C. @Transactional 自调用失效是最高频事务坑
- D. 事务失效只有传播行为一种原因
**答案：C**
**解析：** @Transactional 自调用失效是最高频事务坑。原因：同类 this 调用不走代理事务拦截器不介入，与 AOP 失效同源，表现：内层注解方法无事务。
**来源：** SP-047 · 事务（实战共识）

**Qspring-1405（判断·失效）** @Transactional 自调用失效是最高频事务坑
**答案：对。** 解析：同类 this 调用不走代理事务拦截器不介入，与 AOP 失效同源，表现：内层注解方法无事务

**Qspring-1406（判断·失效）** 自调用时事务仍生效
**答案：错。** 正确表述：@Transactional 自调用失效是最高频事务坑。原因：同类 this 调用不走代理事务拦截器不介入，与 AOP 失效同源，表现：内层注解方法无事务

**Qspring-1407（判断·失效）** 把方法改 private 能修复
**答案：错。** 正确表述：@Transactional 自调用失效是最高频事务坑。原因：同类 this 调用不走代理事务拦截器不介入，与 AOP 失效同源，表现：内层注解方法无事务

**Qspring-1408（判断·失效）** 事务失效只有传播行为一种原因
**答案：错。** 正确表述：@Transactional 自调用失效是最高频事务坑。原因：同类 this 调用不走代理事务拦截器不介入，与 AOP 失效同源，表现：内层注解方法无事务

**Qspring-1409（场景单选·失效）** 在工程实践中关于「自调用」，下列做法符合推荐实践的是？
- A. 事务失效八股的第一条
- B. 自调用时事务仍生效
- C. 事务失效只有传播行为一种原因
- D. 把方法改 private 能修复
**答案：A**
**解析：** 推荐实践：事务失效八股的第一条。事实依据：@Transactional 自调用失效是最高频事务坑。

**Qspring-1410（场景判断·失效）** 推荐实践：事务失效八股的第一条
**答案：对。** 解析：@Transactional 自调用失效是最高频事务坑。原因：同类 this 调用不走代理事务拦截器不介入，与 AOP 失效同源，表现：内层注解方法无事务

**Qspring-1411（填空·失效）** @Transactional ______失效是最高频事务坑
**答案：自调用**。解析：同类 this 调用不走代理事务拦截器不介入，与 AOP 失效同源，表现：内层注解方法无事务

**Qspring-1412（简答·失效）** 请说明「事务」中自调用的机制与使用要点。
**要点（标准答案）**：① @Transactional 自调用失效是最高频事务坑；② 原理：同类 this 调用不走代理事务拦截器不介入，与 AOP 失效同源，表现：内层注解方法无事务；③ 使用要点：事务失效八股的第一条。版本锚点：实战共识。

**Qspring-1413（单选·正向·失效）** 关于「事务」的说法，正确的是？
- A. protected 方法事务在所有版本生效
- B. Spring 6.0 之前 @Transactional 只对 public 方法生效
- C. 接口默认方法的事务一定生效
- D. 非 public 加注解会启动报错
**答案：B**
**解析：** Spring 6.0 之前 @Transactional 只对 public 方法生效。原因：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效。
**来源：** SP-048 · 事务（Spring 6.0 release note）

**Qspring-1414（判断·失效）** Spring 6.0 之前 @Transactional 只对 public 方法生效
**答案：对。** 解析：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效

**Qspring-1415（判断·失效）** protected 方法事务在所有版本生效
**答案：错。** 正确表述：Spring 6.0 之前 @Transactional 只对 public 方法生效。原因：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效

**Qspring-1416（判断·失效）** 非 public 加注解会启动报错
**答案：错。** 正确表述：Spring 6.0 之前 @Transactional 只对 public 方法生效。原因：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效

**Qspring-1417（判断·失效）** 接口默认方法的事务一定生效
**答案：错。** 正确表述：Spring 6.0 之前 @Transactional 只对 public 方法生效。原因：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效

**Qspring-1418（场景单选·失效）** 在工程实践中关于「public」，下列做法符合推荐实践的是？
- A. 非 public 加注解会启动报错
- B. protected 方法事务在所有版本生效
- C. 升级 Spring 6 才有非 public 事务支持
- D. 接口默认方法的事务一定生效
**答案：C**
**解析：** 推荐实践：升级 Spring 6 才有非 public 事务支持。事实依据：Spring 6.0 之前 @Transactional 只对 public 方法生效。

**Qspring-1419（场景判断·失效）** 推荐实践：升级 Spring 6 才有非 public 事务支持
**答案：对。** 解析：Spring 6.0 之前 @Transactional 只对 public 方法生效。原因：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效

**Qspring-1420（填空·失效）** Spring 6.0 之前 @Transactional 只对 ______ 方法生效
**答案：public**。解析：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效

**Qspring-1421（简答·失效）** 请说明「事务」中public的机制与使用要点。
**要点（标准答案）**：① Spring 6.0 之前 @Transactional 只对 public 方法生效；② 原理：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效；③ 使用要点：升级 Spring 6 才有非 public 事务支持。版本锚点：Spring 6.0 release note。

**Qspring-1422（单选·正向·回滚）** 关于「事务」的说法，正确的是？
- A. @Transactional 默认只回滚 RuntimeException 与 Error
- B. Error 不触发回滚
- C. 默认回滚所有异常
- D. 默认回滚受检异常
**答案：A**
**解析：** @Transactional 默认只回滚 RuntimeException 与 Error。原因：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款。
**来源：** SP-049 · 事务（阿里手册）

**Qspring-1423（判断·回滚）** @Transactional 默认只回滚 RuntimeException 与 Error
**答案：对。** 解析：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款

**Qspring-1424（判断·回滚）** 默认回滚所有异常
**答案：错。** 正确表述：@Transactional 默认只回滚 RuntimeException 与 Error。原因：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款

**Qspring-1425（判断·回滚）** 默认回滚受检异常
**答案：错。** 正确表述：@Transactional 默认只回滚 RuntimeException 与 Error。原因：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款

**Qspring-1426（判断·回滚）** Error 不触发回滚
**答案：错。** 正确表述：@Transactional 默认只回滚 RuntimeException 与 Error。原因：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款

**Qspring-1427（场景单选·回滚）** 在工程实践中关于「rollbackFor」，下列做法符合推荐实践的是？
- A. Error 不触发回滚
- B. 事务注解一律显式 rollbackFor
- C. 默认回滚所有异常
- D. 默认回滚受检异常
**答案：B**
**解析：** 推荐实践：事务注解一律显式 rollbackFor。事实依据：@Transactional 默认只回滚 RuntimeException 与 Error。

**Qspring-1428（场景判断·回滚）** 推荐实践：事务注解一律显式 rollbackFor
**答案：对。** 解析：@Transactional 默认只回滚 RuntimeException 与 Error。原因：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款

**Qspring-1429（简答·回滚）** 请说明「事务」中rollbackFor的机制与使用要点。
**要点（标准答案）**：① @Transactional 默认只回滚 RuntimeException 与 Error；② 原理：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款；③ 使用要点：事务注解一律显式 rollbackFor。版本锚点：阿里手册。

**Qspring-1430（单选·正向·失效）** 关于「事务」的说法，正确的是？
- A. setRollbackOnly 会抛异常
- B. 吞异常是推荐的容错方式
- C. 事务方法内异常被 try-catch 吞掉后事务照常提交
- D. catch 后事务自动回滚
**答案：C**
**解析：** 事务方法内异常被 try-catch 吞掉后事务照常提交。原因：拦截器感知不到被吞的异常，回滚决策失效，需要 catch 后 throw 或用 TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()。
**来源：** SP-050 · 事务（实战共识）

**Qspring-1431（判断·失效）** 事务方法内异常被 try-catch 吞掉后事务照常提交
**答案：对。** 解析：拦截器感知不到被吞的异常，回滚决策失效，需要 catch 后 throw 或用 TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()

**Qspring-1432（判断·失效）** catch 后事务自动回滚
**答案：错。** 正确表述：事务方法内异常被 try-catch 吞掉后事务照常提交。原因：拦截器感知不到被吞的异常，回滚决策失效，需要 catch 后 throw 或用 TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()

**Qspring-1433（判断·失效）** setRollbackOnly 会抛异常
**答案：错。** 正确表述：事务方法内异常被 try-catch 吞掉后事务照常提交。原因：拦截器感知不到被吞的异常，回滚决策失效，需要 catch 后 throw 或用 TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()

**Qspring-1434（判断·失效）** 吞异常是推荐的容错方式
**答案：错。** 正确表述：事务方法内异常被 try-catch 吞掉后事务照常提交。原因：拦截器感知不到被吞的异常，回滚决策失效，需要 catch 后 throw 或用 TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()

**Qspring-1435（场景单选·失效）** 在工程实践中关于「catch」，下列做法符合推荐实践的是？
- A. setRollbackOnly 会抛异常
- B. 吞异常是推荐的容错方式
- C. catch 后事务自动回滚
- D. 代码 review 必查事务内 catch
**答案：D**
**解析：** 推荐实践：代码 review 必查事务内 catch。事实依据：事务方法内异常被 try-catch 吞掉后事务照常提交。

**Qspring-1436（场景判断·失效）** 推荐实践：代码 review 必查事务内 catch
**答案：对。** 解析：事务方法内异常被 try-catch 吞掉后事务照常提交。原因：拦截器感知不到被吞的异常，回滚决策失效，需要 catch 后 throw 或用 TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()

**Qspring-1437（填空·失效）** 事务方法内异常被 try-______ 吞掉后事务照常提交
**答案：catch**。解析：拦截器感知不到被吞的异常，回滚决策失效，需要 catch 后 throw 或用 TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()

**Qspring-1438（简答·失效）** 请说明「事务」中catch的机制与使用要点。
**要点（标准答案）**：① 事务方法内异常被 try-catch 吞掉后事务照常提交；② 原理：拦截器感知不到被吞的异常，回滚决策失效，需要 catch 后 throw 或用 TransactionAspectSupport.currentTransactionStatus().setRollbackOnly()；③ 使用要点：代码 review 必查事务内 catch。版本锚点：实战共识。

**Qspring-1439（单选·正向·传播）** 关于「事务」的说法，正确的是？
- A. REQUIRED 是默认传播行为：有事务加入无事务新建
- B. 它与非事务调用组合必然回滚
- C. REQUIRED 总是新建事务
- D. 默认传播是 REQUIRES_NEW
**答案：A**
**解析：** REQUIRED 是默认传播行为：有事务加入无事务新建。原因：7 种传播行为的核心，大多数业务场景用它，理解其余 6 种都从它出发。
**来源：** SP-051 · 事务（Spring 文档）

**Qspring-1440（判断·传播）** REQUIRED 是默认传播行为：有事务加入无事务新建
**答案：对。** 解析：7 种传播行为的核心，大多数业务场景用它，理解其余 6 种都从它出发

**Qspring-1441（判断·传播）** 默认传播是 REQUIRES_NEW
**答案：错。** 正确表述：REQUIRED 是默认传播行为：有事务加入无事务新建。原因：7 种传播行为的核心，大多数业务场景用它，理解其余 6 种都从它出发

**Qspring-1442（判断·传播）** REQUIRED 总是新建事务
**答案：错。** 正确表述：REQUIRED 是默认传播行为：有事务加入无事务新建。原因：7 种传播行为的核心，大多数业务场景用它，理解其余 6 种都从它出发

**Qspring-1443（判断·传播）** 它与非事务调用组合必然回滚
**答案：错。** 正确表述：REQUIRED 是默认传播行为：有事务加入无事务新建。原因：7 种传播行为的核心，大多数业务场景用它，理解其余 6 种都从它出发

**Qspring-1444（场景单选·传播）** 在工程实践中关于「REQUIRED」，下列做法符合推荐实践的是？
- A. 默认传播是 REQUIRES_NEW
- B. 它与非事务调用组合必然回滚
- C. 传播行为题的基准点
- D. REQUIRED 总是新建事务
**答案：C**
**解析：** 推荐实践：传播行为题的基准点。事实依据：REQUIRED 是默认传播行为：有事务加入无事务新建。

**Qspring-1445（场景判断·传播）** 推荐实践：传播行为题的基准点
**答案：对。** 解析：REQUIRED 是默认传播行为：有事务加入无事务新建。原因：7 种传播行为的核心，大多数业务场景用它，理解其余 6 种都从它出发

**Qspring-1446（填空·传播）** ______ 是默认传播行为：有事务加入无事务新建
**答案：REQUIRED**。解析：7 种传播行为的核心，大多数业务场景用它，理解其余 6 种都从它出发

**Qspring-1447（简答·传播）** 请说明「事务」中REQUIRED的机制与使用要点。
**要点（标准答案）**：① REQUIRED 是默认传播行为：有事务加入无事务新建；② 原理：7 种传播行为的核心，大多数业务场景用它，理解其余 6 种都从它出发；③ 使用要点：传播行为题的基准点。版本锚点：Spring 文档。

**Qspring-1448（单选·正向·传播）** 关于「事务」的说法，正确的是？
- A. 它不会挂起当前事务
- B. 内层回滚外层必然回滚
- C. REQUIRES_NEW 加入外层事务
- D. REQUIRES_NEW 挂起当前事务开独立新事务互不影响
**答案：D**
**解析：** REQUIRES_NEW 挂起当前事务开独立新事务互不影响。原因：内层回滚外层可 catch 继续提交（日志表场景），外层回滚不影响已提交的内层，代价是连接占用翻倍与死锁风险升高。
**来源：** SP-052 · 事务（Spring 文档）

**Qspring-1449（判断·传播）** REQUIRES_NEW 挂起当前事务开独立新事务互不影响
**答案：对。** 解析：内层回滚外层可 catch 继续提交（日志表场景），外层回滚不影响已提交的内层，代价是连接占用翻倍与死锁风险升高

**Qspring-1450（判断·传播）** REQUIRES_NEW 加入外层事务
**答案：错。** 正确表述：REQUIRES_NEW 挂起当前事务开独立新事务互不影响。原因：内层回滚外层可 catch 继续提交（日志表场景），外层回滚不影响已提交的内层，代价是连接占用翻倍与死锁风险升高

**Qspring-1451（判断·传播）** 内层回滚外层必然回滚
**答案：错。** 正确表述：REQUIRES_NEW 挂起当前事务开独立新事务互不影响。原因：内层回滚外层可 catch 继续提交（日志表场景），外层回滚不影响已提交的内层，代价是连接占用翻倍与死锁风险升高

**Qspring-1452（判断·传播）** 它不会挂起当前事务
**答案：错。** 正确表述：REQUIRES_NEW 挂起当前事务开独立新事务互不影响。原因：内层回滚外层可 catch 继续提交（日志表场景），外层回滚不影响已提交的内层，代价是连接占用翻倍与死锁风险升高

**Qspring-1453（场景单选·传播）** 在工程实践中关于「REQUIRES_NEW」，下列做法符合推荐实践的是？
- A. REQUIRES_NEW 加入外层事务
- B. 内层回滚外层必然回滚
- C. 它不会挂起当前事务
- D. 操作日志/审计与主业务解耦
**答案：D**
**解析：** 推荐实践：操作日志/审计与主业务解耦。事实依据：REQUIRES_NEW 挂起当前事务开独立新事务互不影响。

**Qspring-1454（场景判断·传播）** 推荐实践：操作日志/审计与主业务解耦
**答案：对。** 解析：REQUIRES_NEW 挂起当前事务开独立新事务互不影响。原因：内层回滚外层可 catch 继续提交（日志表场景），外层回滚不影响已提交的内层，代价是连接占用翻倍与死锁风险升高

**Qspring-1455（填空·传播）** ______ 挂起当前事务开独立新事务互不影响
**答案：REQUIRES_NEW**。解析：内层回滚外层可 catch 继续提交（日志表场景），外层回滚不影响已提交的内层，代价是连接占用翻倍与死锁风险升高

**Qspring-1456（简答·传播）** 请说明「事务」中REQUIRES_NEW的机制与使用要点。
**要点（标准答案）**：① REQUIRES_NEW 挂起当前事务开独立新事务互不影响；② 原理：内层回滚外层可 catch 继续提交（日志表场景），外层回滚不影响已提交的内层，代价是连接占用翻倍与死锁风险升高；③ 使用要点：操作日志/审计与主业务解耦。版本锚点：Spring 文档。

**Qspring-1457（单选·正向·传播）** 关于「事务」的说法，正确的是？
- A. NESTED 与 REQUIRES_NEW 等价
- B. NESTED 开新物理事务
- C. 保存点是 MySQL 不支持的
- D. NESTED 在当前事务内建立保存点（savepoint）可部分回滚
**答案：D**
**解析：** NESTED 在当前事务内建立保存点（savepoint）可部分回滚。原因：内层回滚只回滚到保存点外层继续，外层回滚内层必回滚，与 REQUIRES_NEW 的本质区别是同一物理事务。
**来源：** SP-053 · 事务（Spring 文档）

**Qspring-1458（判断·传播）** NESTED 在当前事务内建立保存点（savepoint）可部分回滚
**答案：对。** 解析：内层回滚只回滚到保存点外层继续，外层回滚内层必回滚，与 REQUIRES_NEW 的本质区别是同一物理事务

**Qspring-1459（判断·传播）** NESTED 开新物理事务
**答案：错。** 正确表述：NESTED 在当前事务内建立保存点（savepoint）可部分回滚。原因：内层回滚只回滚到保存点外层继续，外层回滚内层必回滚，与 REQUIRES_NEW 的本质区别是同一物理事务

**Qspring-1460（判断·传播）** NESTED 与 REQUIRES_NEW 等价
**答案：错。** 正确表述：NESTED 在当前事务内建立保存点（savepoint）可部分回滚。原因：内层回滚只回滚到保存点外层继续，外层回滚内层必回滚，与 REQUIRES_NEW 的本质区别是同一物理事务

**Qspring-1461（判断·传播）** 保存点是 MySQL 不支持的
**答案：错。** 正确表述：NESTED 在当前事务内建立保存点（savepoint）可部分回滚。原因：内层回滚只回滚到保存点外层继续，外层回滚内层必回滚，与 REQUIRES_NEW 的本质区别是同一物理事务

**Qspring-1462（场景单选·传播）** 在工程实践中关于「NESTED」，下列做法符合推荐实践的是？
- A. NESTED 与 REQUIRES_NEW 等价
- B. 嵌套业务步骤部分失败继续执行
- C. 保存点是 MySQL 不支持的
- D. NESTED 开新物理事务
**答案：B**
**解析：** 推荐实践：嵌套业务步骤部分失败继续执行。事实依据：NESTED 在当前事务内建立保存点（savepoint）可部分回滚。

**Qspring-1463（场景判断·传播）** 推荐实践：嵌套业务步骤部分失败继续执行
**答案：对。** 解析：NESTED 在当前事务内建立保存点（savepoint）可部分回滚。原因：内层回滚只回滚到保存点外层继续，外层回滚内层必回滚，与 REQUIRES_NEW 的本质区别是同一物理事务

**Qspring-1464（填空·传播）** ______ 在当前事务内建立保存点（savepoint）可部分回滚
**答案：NESTED**。解析：内层回滚只回滚到保存点外层继续，外层回滚内层必回滚，与 REQUIRES_NEW 的本质区别是同一物理事务

**Qspring-1465（简答·传播）** 请说明「事务」中NESTED的机制与使用要点。
**要点（标准答案）**：① NESTED 在当前事务内建立保存点（savepoint）可部分回滚；② 原理：内层回滚只回滚到保存点外层继续，外层回滚内层必回滚，与 REQUIRES_NEW 的本质区别是同一物理事务；③ 使用要点：嵌套业务步骤部分失败继续执行。版本锚点：Spring 文档。

**Qspring-1466（单选·正向·传播）** 关于「事务」的说法，正确的是？
- A. MANDATORY 强制要求已有事务、NEVER 禁止事务、SUPPORTS 有则用无则非事务、NOT_SUPPORTED 挂起以非事务执行
- B. NOT_SUPPORTED 与 SUPPORTS 等价
- C. NEVER 表示需要新事务
- D. SUPPORTS 会新建事务
**答案：A**
**解析：** MANDATORY 强制要求已有事务、NEVER 禁止事务、SUPPORTS 有则用无则非事务、NOT_SUPPORTED 挂起以非事务执行。原因：四种边界型传播用于约束调用契约（如查询方法 MANDATORY 保证必须被事务包裹）。
**来源：** SP-054 · 事务（Spring 文档）

**Qspring-1467（判断·传播）** MANDATORY 强制要求已有事务、NEVER 禁止事务、SUPPORTS 有则用无则非事务、NOT_SUPPORTED 挂起以非事务执行
**答案：对。** 解析：四种边界型传播用于约束调用契约（如查询方法 MANDATORY 保证必须被事务包裹）

**Qspring-1468（判断·传播）** SUPPORTS 会新建事务
**答案：错。** 正确表述：MANDATORY 强制要求已有事务、NEVER 禁止事务、SUPPORTS 有则用无则非事务、NOT_SUPPORTED 挂起以非事务执行。原因：四种边界型传播用于约束调用契约（如查询方法 MANDATORY 保证必须被事务包裹）

**Qspring-1469（判断·传播）** NEVER 表示需要新事务
**答案：错。** 正确表述：MANDATORY 强制要求已有事务、NEVER 禁止事务、SUPPORTS 有则用无则非事务、NOT_SUPPORTED 挂起以非事务执行。原因：四种边界型传播用于约束调用契约（如查询方法 MANDATORY 保证必须被事务包裹）

**Qspring-1470（判断·传播）** NOT_SUPPORTED 与 SUPPORTS 等价
**答案：错。** 正确表述：MANDATORY 强制要求已有事务、NEVER 禁止事务、SUPPORTS 有则用无则非事务、NOT_SUPPORTED 挂起以非事务执行。原因：四种边界型传播用于约束调用契约（如查询方法 MANDATORY 保证必须被事务包裹）

**Qspring-1471（场景单选·传播）** 在工程实践中关于「其他」，下列做法符合推荐实践的是？
- A. NEVER 表示需要新事务
- B. NOT_SUPPORTED 与 SUPPORTS 等价
- C. SUPPORTS 会新建事务
- D. 契约型方法设计
**答案：D**
**解析：** 推荐实践：契约型方法设计。事实依据：MANDATORY 强制要求已有事务、NEVER 禁止事务、SUPPORTS 有则用无则非事务、NOT_SUPPORTED 挂起以非事务执行。

**Qspring-1472（场景判断·传播）** 推荐实践：契约型方法设计
**答案：对。** 解析：MANDATORY 强制要求已有事务、NEVER 禁止事务、SUPPORTS 有则用无则非事务、NOT_SUPPORTED 挂起以非事务执行。原因：四种边界型传播用于约束调用契约（如查询方法 MANDATORY 保证必须被事务包裹）

**Qspring-1473（简答·传播）** 请说明「事务」中其他的机制与使用要点。
**要点（标准答案）**：① MANDATORY 强制要求已有事务、NEVER 禁止事务、SUPPORTS 有则用无则非事务、NOT_SUPPORTED 挂起以非事务执行；② 原理：四种边界型传播用于约束调用契约（如查询方法 MANDATORY 保证必须被事务包裹）；③ 使用要点：契约型方法设计。版本锚点：Spring 文档。

**Qspring-1474（单选·正向·属性）** 关于「事务」的说法，正确的是？
- A. 超时后立即中断正在执行的 SQL
- B. timeout 默认 60 秒
- C. @Transactional(timeout=5) 限定事务从开始到提交的最长时间
- D. timeout 是连接池参数
**答案：C**
**解析：** @Transactional(timeout=5) 限定事务从开始到提交的最长时间。原因：超时回滚防止长事务拖垮连接池，超时检查在实际 SQL 执行时触发，MySQL 端还有 innodb_lock_wait_timeout 控制锁等待。
**来源：** SP-055 · 事务（Spring 文档）

**Qspring-1475（判断·属性）** @Transactional(timeout=5) 限定事务从开始到提交的最长时间
**答案：对。** 解析：超时回滚防止长事务拖垮连接池，超时检查在实际 SQL 执行时触发，MySQL 端还有 innodb_lock_wait_timeout 控制锁等待

**Qspring-1476（判断·属性）** timeout 默认 60 秒
**答案：错。** 正确表述：@Transactional(timeout=5) 限定事务从开始到提交的最长时间。原因：超时回滚防止长事务拖垮连接池，超时检查在实际 SQL 执行时触发，MySQL 端还有 innodb_lock_wait_timeout 控制锁等待

**Qspring-1477（判断·属性）** 超时后立即中断正在执行的 SQL
**答案：错。** 正确表述：@Transactional(timeout=5) 限定事务从开始到提交的最长时间。原因：超时回滚防止长事务拖垮连接池，超时检查在实际 SQL 执行时触发，MySQL 端还有 innodb_lock_wait_timeout 控制锁等待

**Qspring-1478（判断·属性）** timeout 是连接池参数
**答案：错。** 正确表述：@Transactional(timeout=5) 限定事务从开始到提交的最长时间。原因：超时回滚防止长事务拖垮连接池，超时检查在实际 SQL 执行时触发，MySQL 端还有 innodb_lock_wait_timeout 控制锁等待

**Qspring-1479（场景单选·属性）** 在工程实践中关于「timeout」，下列做法符合推荐实践的是？
- A. 超时后立即中断正在执行的 SQL
- B. timeout 默认 60 秒
- C. 防大事务的标准配置
- D. timeout 是连接池参数
**答案：C**
**解析：** 推荐实践：防大事务的标准配置。事实依据：@Transactional(timeout=5) 限定事务从开始到提交的最长时间。

**Qspring-1480（场景判断·属性）** 推荐实践：防大事务的标准配置
**答案：对。** 解析：@Transactional(timeout=5) 限定事务从开始到提交的最长时间。原因：超时回滚防止长事务拖垮连接池，超时检查在实际 SQL 执行时触发，MySQL 端还有 innodb_lock_wait_timeout 控制锁等待

**Qspring-1481（填空·属性）** @Transactional(______=5) 限定事务从开始到提交的最长时间
**答案：timeout**。解析：超时回滚防止长事务拖垮连接池，超时检查在实际 SQL 执行时触发，MySQL 端还有 innodb_lock_wait_timeout 控制锁等待

**Qspring-1482（简答·属性）** 请说明「事务」中timeout的机制与使用要点。
**要点（标准答案）**：① @Transactional(timeout=5) 限定事务从开始到提交的最长时间；② 原理：超时回滚防止长事务拖垮连接池，超时检查在实际 SQL 执行时触发，MySQL 端还有 innodb_lock_wait_timeout 控制锁等待；③ 使用要点：防大事务的标准配置。版本锚点：Spring 文档。

**Qspring-1483（单选·正向·属性）** 关于「事务」的说法，正确的是？
- A. readOnly 只对 JPA 生效
- B. readOnly=true 是只读优化提示非强制约束
- C. readOnly 能强制只读
- D. readOnly 对性能无影响
**答案：B**
**解析：** readOnly=true 是只读优化提示非强制约束。原因：驱动与框架可据此优化（跳过脏检查、路由到从库），readOnly 事务中写操作在 MySQL 下报错取决于具体配置。
**来源：** SP-056 · 事务（Spring 文档）

**Qspring-1484（判断·属性）** readOnly=true 是只读优化提示非强制约束
**答案：对。** 解析：驱动与框架可据此优化（跳过脏检查、路由到从库），readOnly 事务中写操作在 MySQL 下报错取决于具体配置

**Qspring-1485（判断·属性）** readOnly 能强制只读
**答案：错。** 正确表述：readOnly=true 是只读优化提示非强制约束。原因：驱动与框架可据此优化（跳过脏检查、路由到从库），readOnly 事务中写操作在 MySQL 下报错取决于具体配置

**Qspring-1486（判断·属性）** readOnly 对性能无影响
**答案：错。** 正确表述：readOnly=true 是只读优化提示非强制约束。原因：驱动与框架可据此优化（跳过脏检查、路由到从库），readOnly 事务中写操作在 MySQL 下报错取决于具体配置

**Qspring-1487（判断·属性）** readOnly 只对 JPA 生效
**答案：错。** 正确表述：readOnly=true 是只读优化提示非强制约束。原因：驱动与框架可据此优化（跳过脏检查、路由到从库），readOnly 事务中写操作在 MySQL 下报错取决于具体配置

**Qspring-1488（场景单选·属性）** 在工程实践中关于「readOnly」，下列做法符合推荐实践的是？
- A. readOnly 能强制只读
- B. readOnly 只对 JPA 生效
- C. readOnly 对性能无影响
- D. 查询类事务标注 readOnly
**答案：D**
**解析：** 推荐实践：查询类事务标注 readOnly。事实依据：readOnly=true 是只读优化提示非强制约束。

**Qspring-1489（场景判断·属性）** 推荐实践：查询类事务标注 readOnly
**答案：对。** 解析：readOnly=true 是只读优化提示非强制约束。原因：驱动与框架可据此优化（跳过脏检查、路由到从库），readOnly 事务中写操作在 MySQL 下报错取决于具体配置

**Qspring-1490（填空·属性）** ______=true 是只读优化提示非强制约束
**答案：readOnly**。解析：驱动与框架可据此优化（跳过脏检查、路由到从库），readOnly 事务中写操作在 MySQL 下报错取决于具体配置

**Qspring-1491（简答·属性）** 请说明「事务」中readOnly的机制与使用要点。
**要点（标准答案）**：① readOnly=true 是只读优化提示非强制约束；② 原理：驱动与框架可据此优化（跳过脏检查、路由到从库），readOnly 事务中写操作在 MySQL 下报错取决于具体配置；③ 使用要点：查询类事务标注 readOnly。版本锚点：Spring 文档。

**Qspring-1492（单选·正向·大事务）** 关于「事务」的说法，正确的是？
- A. 大事务只影响性能不影响可用性
- B. 事务内发 MQ 能保证原子性
- C. 事务越大越安全
- D. 大事务治理：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围
**答案：D**
**解析：** 大事务治理：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围。原因：大事务持有连接与行锁时间长，拖垮连接池与并发度，把 RPC/MQ 移到事务外（事务提交后发消息）。
**来源：** SP-057 · 事务（实战方法论）

**Qspring-1493（判断·大事务）** 大事务治理：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围
**答案：对。** 解析：大事务持有连接与行锁时间长，拖垮连接池与并发度，把 RPC/MQ 移到事务外（事务提交后发消息）

**Qspring-1494（判断·大事务）** 事务越大越安全
**答案：错。** 正确表述：大事务治理：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围。原因：大事务持有连接与行锁时间长，拖垮连接池与并发度，把 RPC/MQ 移到事务外（事务提交后发消息）

**Qspring-1495（判断·大事务）** 事务内发 MQ 能保证原子性
**答案：错。** 正确表述：大事务治理：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围。原因：大事务持有连接与行锁时间长，拖垮连接池与并发度，把 RPC/MQ 移到事务外（事务提交后发消息）

**Qspring-1496（判断·大事务）** 大事务只影响性能不影响可用性
**答案：错。** 正确表述：大事务治理：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围。原因：大事务持有连接与行锁时间长，拖垮连接池与并发度，把 RPC/MQ 移到事务外（事务提交后发消息）

**Qspring-1497（场景单选·大事务）** 在工程实践中关于「治理」，下列做法符合推荐实践的是？
- A. 事务内发 MQ 能保证原子性
- B. 大事务只影响性能不影响可用性
- C. review 大事务的标准检查单
- D. 事务越大越安全
**答案：C**
**解析：** 推荐实践：review 大事务的标准检查单。事实依据：大事务治理：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围。

**Qspring-1498（场景判断·大事务）** 推荐实践：review 大事务的标准检查单
**答案：对。** 解析：大事务治理：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围。原因：大事务持有连接与行锁时间长，拖垮连接池与并发度，把 RPC/MQ 移到事务外（事务提交后发消息）

**Qspring-1499（填空·大事务）** 大事务______：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围
**答案：治理**。解析：大事务持有连接与行锁时间长，拖垮连接池与并发度，把 RPC/MQ 移到事务外（事务提交后发消息）

**Qspring-1500（简答·大事务）** 请说明「事务」中治理的机制与使用要点。
**要点（标准答案）**：① 大事务治理：拆分事务边界、事务内禁远程调用与 MQ 发送、编程式 TransactionTemplate 控制范围；② 原理：大事务持有连接与行锁时间长，拖垮连接池与并发度，把 RPC/MQ 移到事务外（事务提交后发消息）；③ 使用要点：review 大事务的标准检查单。版本锚点：实战方法论。

**Qspring-1501（单选·正向·事件）** 关于「事务」的说法，正确的是？
- A. @TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）
- B. 事务回滚后默认仍会执行
- C. 它默认异步执行
- D. 默认在事务提交前执行
**答案：A**
**解析：** @TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）。原因：默认 phase=AFTER_COMMIT 保证"事务成功后才发后续动作"，failingExecution 表示事务回滚时的行为，BEFORE_COMMIT/AFTER_ROLLBACK/ AFTER_COMPLETION 可选。
**来源：** SP-058 · 事务（Spring 文档核对）

**Qspring-1502（判断·事件）** @TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）
**答案：对。** 解析：默认 phase=AFTER_COMMIT 保证"事务成功后才发后续动作"，failingExecution 表示事务回滚时的行为，BEFORE_COMMIT/AFTER_ROLLBACK/ AFTER_COMPLETION 可选

**Qspring-1503（判断·事件）** 默认在事务提交前执行
**答案：错。** 正确表述：@TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）。原因：默认 phase=AFTER_COMMIT 保证"事务成功后才发后续动作"，failingExecution 表示事务回滚时的行为，BEFORE_COMMIT/AFTER_ROLLBACK/ AFTER_COMPLETION 可选

**Qspring-1504（判断·事件）** 它默认异步执行
**答案：错。** 正确表述：@TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）。原因：默认 phase=AFTER_COMMIT 保证"事务成功后才发后续动作"，failingExecution 表示事务回滚时的行为，BEFORE_COMMIT/AFTER_ROLLBACK/ AFTER_COMPLETION 可选

**Qspring-1505（判断·事件）** 事务回滚后默认仍会执行
**答案：错。** 正确表述：@TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）。原因：默认 phase=AFTER_COMMIT 保证"事务成功后才发后续动作"，failingExecution 表示事务回滚时的行为，BEFORE_COMMIT/AFTER_ROLLBACK/ AFTER_COMPLETION 可选

**Qspring-1506（场景单选·事件）** 在工程实践中关于「@TransactionalEventListener」，下列做法符合推荐实践的是？
- A. 它默认异步执行
- B. 事务回滚后默认仍会执行
- C. 默认在事务提交前执行
- D. 提交后发 MQ/清缓存的标准姿势
**答案：D**
**解析：** 推荐实践：提交后发 MQ/清缓存的标准姿势。事实依据：@TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）。

**Qspring-1507（场景判断·事件）** 推荐实践：提交后发 MQ/清缓存的标准姿势
**答案：对。** 解析：@TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）。原因：默认 phase=AFTER_COMMIT 保证"事务成功后才发后续动作"，failingExecution 表示事务回滚时的行为，BEFORE_COMMIT/AFTER_ROLLBACK/ AFTER_COMPLETION 可选

**Qspring-1508（填空·事件）** ______ 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）
**答案：@TransactionalEventListener**。解析：默认 phase=AFTER_COMMIT 保证"事务成功后才发后续动作"，failingExecution 表示事务回滚时的行为，BEFORE_COMMIT/AFTER_ROLLBACK/ AFTER_COMPLETION 可选

**Qspring-1509（简答·事件）** 请说明「事务」中@TransactionalEventListener的机制与使用要点。
**要点（标准答案）**：① @TransactionalEventListener 默认在 AFTER_COMMIT 阶段执行（本项目已核对文档）；② 原理：默认 phase=AFTER_COMMIT 保证"事务成功后才发后续动作"，failingExecution 表示事务回滚时的行为，BEFORE_COMMIT/AFTER_ROLLBACK/ AFTER_COMPLETION 可选；③ 使用要点：提交后发 MQ/清缓存的标准姿势。版本锚点：Spring 文档核对。

**Qspring-1510（单选·正向·事件）** 关于「事务」的说法，正确的是？
- A. 提交后写库自动有事务
- B. 该阶段不可能写库
- C. 监听器继承原事务上下文
- D. AFTER_COMMIT 监听器里再写数据库不会自动开新事务
**答案：D**
**解析：** AFTER_COMMIT 监听器里再写数据库不会自动开新事务。原因：此时事务资源已提交完成，写操作可能以 autoCommit 游离执行，需要 @Transactional(propagation=REQUIRES_NEW) 显式开新事务。
**来源：** SP-059 · 事务（实战教训）

**Qspring-1511（判断·事件）** AFTER_COMMIT 监听器里再写数据库不会自动开新事务
**答案：对。** 解析：此时事务资源已提交完成，写操作可能以 autoCommit 游离执行，需要 @Transactional(propagation=REQUIRES_NEW) 显式开新事务

**Qspring-1512（判断·事件）** 提交后写库自动有事务
**答案：错。** 正确表述：AFTER_COMMIT 监听器里再写数据库不会自动开新事务。原因：此时事务资源已提交完成，写操作可能以 autoCommit 游离执行，需要 @Transactional(propagation=REQUIRES_NEW) 显式开新事务

**Qspring-1513（判断·事件）** 监听器继承原事务上下文
**答案：错。** 正确表述：AFTER_COMMIT 监听器里再写数据库不会自动开新事务。原因：此时事务资源已提交完成，写操作可能以 autoCommit 游离执行，需要 @Transactional(propagation=REQUIRES_NEW) 显式开新事务

**Qspring-1514（判断·事件）** 该阶段不可能写库
**答案：错。** 正确表述：AFTER_COMMIT 监听器里再写数据库不会自动开新事务。原因：此时事务资源已提交完成，写操作可能以 autoCommit 游离执行，需要 @Transactional(propagation=REQUIRES_NEW) 显式开新事务

**Qspring-1515（场景单选·事件）** 在工程实践中关于「坑」，下列做法符合推荐实践的是？
- A. 提交后写库自动有事务
- B. 提交后补偿写库必须显式开新事务
- C. 该阶段不可能写库
- D. 监听器继承原事务上下文
**答案：B**
**解析：** 推荐实践：提交后补偿写库必须显式开新事务。事实依据：AFTER_COMMIT 监听器里再写数据库不会自动开新事务。

**Qspring-1516（场景判断·事件）** 推荐实践：提交后补偿写库必须显式开新事务
**答案：对。** 解析：AFTER_COMMIT 监听器里再写数据库不会自动开新事务。原因：此时事务资源已提交完成，写操作可能以 autoCommit 游离执行，需要 @Transactional(propagation=REQUIRES_NEW) 显式开新事务

**Qspring-1517（简答·事件）** 请说明「事务」中坑的机制与使用要点。
**要点（标准答案）**：① AFTER_COMMIT 监听器里再写数据库不会自动开新事务；② 原理：此时事务资源已提交完成，写操作可能以 autoCommit 游离执行，需要 @Transactional(propagation=REQUIRES_NEW) 显式开新事务；③ 使用要点：提交后补偿写库必须显式开新事务。版本锚点：实战教训。

**Qspring-1518（单选·正向·机制）** 关于「事件」的说法，正确的是？
- A. Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行
- B. 事件默认异步执行
- C. 事件监听异常不影响发布方
- D. 事件是跨进程通信
**答案：A**
**解析：** Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行。原因：监听器在发布线程内执行（同调用方法一样），异常会传播回发布者，解耦发布方与消费方。
**来源：** SP-060 · 事件（Spring 文档）

**Qspring-1519（判断·机制）** Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行
**答案：对。** 解析：监听器在发布线程内执行（同调用方法一样），异常会传播回发布者，解耦发布方与消费方

**Qspring-1520（判断·机制）** 事件默认异步执行
**答案：错。** 正确表述：Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行。原因：监听器在发布线程内执行（同调用方法一样），异常会传播回发布者，解耦发布方与消费方

**Qspring-1521（判断·机制）** 事件监听异常不影响发布方
**答案：错。** 正确表述：Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行。原因：监听器在发布线程内执行（同调用方法一样），异常会传播回发布者，解耦发布方与消费方

**Qspring-1522（判断·机制）** 事件是跨进程通信
**答案：错。** 正确表述：Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行。原因：监听器在发布线程内执行（同调用方法一样），异常会传播回发布者，解耦发布方与消费方

**Qspring-1523（场景单选·机制）** 在工程实践中关于「ApplicationEvent」，下列做法符合推荐实践的是？
- A. 事件监听异常不影响发布方
- B. 事件默认异步执行
- C. 进程内解耦（业务完成后的扩展动作）
- D. 事件是跨进程通信
**答案：C**
**解析：** 推荐实践：进程内解耦（业务完成后的扩展动作）。事实依据：Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行。

**Qspring-1524（场景判断·机制）** 推荐实践：进程内解耦（业务完成后的扩展动作）
**答案：对。** 解析：Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行。原因：监听器在发布线程内执行（同调用方法一样），异常会传播回发布者，解耦发布方与消费方

**Qspring-1525（填空·机制）** Spring 事件机制：______Publisher 发布、@EventListener 监听默认同步执行
**答案：ApplicationEvent**。解析：监听器在发布线程内执行（同调用方法一样），异常会传播回发布者，解耦发布方与消费方

**Qspring-1526（简答·机制）** 请说明「事件」中ApplicationEvent的机制与使用要点。
**要点（标准答案）**：① Spring 事件机制：ApplicationEventPublisher 发布、@EventListener 监听默认同步执行；② 原理：监听器在发布线程内执行（同调用方法一样），异常会传播回发布者，解耦发布方与消费方；③ 使用要点：进程内解耦（业务完成后的扩展动作）。版本锚点：Spring 文档。

**Qspring-1527（单选·正向·异步）** 关于「事件」的说法，正确的是？
- A. @EventListener 天然异步
- B. 不需要线程池配置
- C. 事件异步化：监听器加 @Async 且启用 @EnableAsync
- D. 异步监听异常会传回发布者
**答案：C**
**解析：** 事件异步化：监听器加 @Async 且启用 @EnableAsync。原因：发布线程立即返回监听在线程池执行，异步监听异常由 AsyncUncaughtExceptionHandler 处理。
**来源：** SP-061 · 事件（Spring 文档）

**Qspring-1528（判断·异步）** 事件异步化：监听器加 @Async 且启用 @EnableAsync
**答案：对。** 解析：发布线程立即返回监听在线程池执行，异步监听异常由 AsyncUncaughtExceptionHandler 处理

**Qspring-1529（判断·异步）** @EventListener 天然异步
**答案：错。** 正确表述：事件异步化：监听器加 @Async 且启用 @EnableAsync。原因：发布线程立即返回监听在线程池执行，异步监听异常由 AsyncUncaughtExceptionHandler 处理

**Qspring-1530（判断·异步）** 异步监听异常会传回发布者
**答案：错。** 正确表述：事件异步化：监听器加 @Async 且启用 @EnableAsync。原因：发布线程立即返回监听在线程池执行，异步监听异常由 AsyncUncaughtExceptionHandler 处理

**Qspring-1531（判断·异步）** 不需要线程池配置
**答案：错。** 正确表述：事件异步化：监听器加 @Async 且启用 @EnableAsync。原因：发布线程立即返回监听在线程池执行，异步监听异常由 AsyncUncaughtExceptionHandler 处理

**Qspring-1532（场景单选·异步）** 在工程实践中关于「@Async+@EventListener」，下列做法符合推荐实践的是？
- A. 发布方不被下游拖慢
- B. 不需要线程池配置
- C. 异步监听异常会传回发布者
- D. @EventListener 天然异步
**答案：A**
**解析：** 推荐实践：发布方不被下游拖慢。事实依据：事件异步化：监听器加 @Async 且启用 @EnableAsync。

**Qspring-1533（场景判断·异步）** 推荐实践：发布方不被下游拖慢
**答案：对。** 解析：事件异步化：监听器加 @Async 且启用 @EnableAsync。原因：发布线程立即返回监听在线程池执行，异步监听异常由 AsyncUncaughtExceptionHandler 处理

**Qspring-1534（简答·异步）** 请说明「事件」中@Async+@EventListener的机制与使用要点。
**要点（标准答案）**：① 事件异步化：监听器加 @Async 且启用 @EnableAsync；② 原理：发布线程立即返回监听在线程池执行，异步监听异常由 AsyncUncaughtExceptionHandler 处理；③ 使用要点：发布方不被下游拖慢。版本锚点：Spring 文档。

**Qspring-1535（单选·正向·@Async）** 关于「异步」的说法，正确的是？
- A. 默认池是 FixedThreadPool
- B. @Async 默认池有界队列
- C. @Async 默认线程池的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor
- D. Boot 各版本默认池一致
**答案：C**
**解析：** @Async 默认线程池的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor。原因：纯 Spring 无 Boot 时回退 SimpleAsyncTaskExecutor（每任务新线程），@Async 必须显式配线程池防 OOM 与线程爆炸（本项目核对的版本结论）。
**来源：** SP-062 · 异步（Boot 版本核对）

**Qspring-1536（判断·@Async）** @Async 默认线程池的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor
**答案：对。** 解析：纯 Spring 无 Boot 时回退 SimpleAsyncTaskExecutor（每任务新线程），@Async 必须显式配线程池防 OOM 与线程爆炸（本项目核对的版本结论）

**Qspring-1537（判断·@Async）** @Async 默认池有界队列
**答案：错。** 正确表述：@Async 默认线程池的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor。原因：纯 Spring 无 Boot 时回退 SimpleAsyncTaskExecutor（每任务新线程），@Async 必须显式配线程池防 OOM 与线程爆炸（本项目核对的版本结论）

**Qspring-1538（判断·@Async）** 默认池是 FixedThreadPool
**答案：错。** 正确表述：@Async 默认线程池的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor。原因：纯 Spring 无 Boot 时回退 SimpleAsyncTaskExecutor（每任务新线程），@Async 必须显式配线程池防 OOM 与线程爆炸（本项目核对的版本结论）

**Qspring-1539（判断·@Async）** Boot 各版本默认池一致
**答案：错。** 正确表述：@Async 默认线程池的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor。原因：纯 Spring 无 Boot 时回退 SimpleAsyncTaskExecutor（每任务新线程），@Async 必须显式配线程池防 OOM 与线程爆炸（本项目核对的版本结论）

**Qspring-1540（场景单选·@Async）** 在工程实践中关于「线程池」，下列做法符合推荐实践的是？
- A. @Async 上线前必配自定义 Executor
- B. 默认池是 FixedThreadPool
- C. @Async 默认池有界队列
- D. Boot 各版本默认池一致
**答案：A**
**解析：** 推荐实践：@Async 上线前必配自定义 Executor。事实依据：@Async 默认线程池的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor。

**Qspring-1541（场景判断·@Async）** 推荐实践：@Async 上线前必配自定义 Executor
**答案：对。** 解析：@Async 默认线程池的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor。原因：纯 Spring 无 Boot 时回退 SimpleAsyncTaskExecutor（每任务新线程），@Async 必须显式配线程池防 OOM 与线程爆炸（本项目核对的版本结论）

**Qspring-1542（填空·@Async）** @Async 默认______的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor
**答案：线程池**。解析：纯 Spring 无 Boot 时回退 SimpleAsyncTaskExecutor（每任务新线程），@Async 必须显式配线程池防 OOM 与线程爆炸（本项目核对的版本结论）

**Qspring-1543（简答·@Async）** 请说明「异步」中线程池的机制与使用要点。
**要点（标准答案）**：① @Async 默认线程池的版本演进：Boot 2.1+ 自动配置 applicationTaskExecutor（core 8 队列无界 OOM 风险），Boot 3.2 开虚拟线程后是 SimpleAsyncTaskExecutor；② 原理：纯 Spring 无 Boot 时回退 SimpleAsyncTaskExecutor（每任务新线程），@Async 必须显式配线程池防 OOM 与线程爆炸（本项目核对的版本结论）；③ 使用要点：@Async 上线前必配自定义 Executor。版本锚点：Boot 版本核对。

**Qspring-1544（单选·正向·@Async）** 关于「异步」的说法，正确的是？
- A. @Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public
- B. @Async 默认启用无需 @EnableAsync
- C. 自调用异步生效
- D. void 方法异常自动打印全栈（默认走 handler 打日志但不会传播）
**答案：A**
**解析：** @Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。原因：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里。
**来源：** SP-063 · 异步（实战共识）

**Qspring-1545（判断·@Async）** @Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public
**答案：对。** 解析：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里

**Qspring-1546（判断·@Async）** @Async 默认启用无需 @EnableAsync
**答案：错。** 正确表述：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。原因：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里

**Qspring-1547（判断·@Async）** 自调用异步生效
**答案：错。** 正确表述：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。原因：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里

**Qspring-1548（判断·@Async）** void 方法异常自动打印全栈（默认走 handler 打日志但不会传播）
**答案：错。** 正确表述：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。原因：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里

**Qspring-1549（场景单选·@Async）** 在工程实践中关于「失效」，下列做法符合推荐实践的是？
- A. 异步任务失效排查三板斧
- B. void 方法异常自动打印全栈（默认走 handler 打日志但不会传播）
- C. @Async 默认启用无需 @EnableAsync
- D. 自调用异步生效
**答案：A**
**解析：** 推荐实践：异步任务失效排查三板斧。事实依据：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。

**Qspring-1550（场景判断·@Async）** 推荐实践：异步任务失效排查三板斧
**答案：对。** 解析：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。原因：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里

**Qspring-1551（填空·@Async）** @Async ______场景：同类自调用、未加 @EnableAsync、方法非 public
**答案：失效**。解析：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里

**Qspring-1552（简答·@Async）** 请说明「异步」中失效的机制与使用要点。
**要点（标准答案）**：① @Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public；② 原理：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里；③ 使用要点：异步任务失效排查三板斧。版本锚点：实战共识。

**Qspring-1553（单选·正向·web）** 关于「Boot」的说法，正确的是？
- A. 视图解析在 HandlerMapping 之前
- B. 请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应
- C. 每个请求先到 Controller
- D. HandlerAdapter 负责路由匹配
**答案：B**
**解析：** 请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应。原因：所有请求入口统一是 DispatcherServlet（前端控制器模式），理解流程后拦截器/异常/参数解析各就各位。
**来源：** SP-064 · Boot（Spring MVC 文档）

**Qspring-1554（判断·web）** 请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应
**答案：对。** 解析：所有请求入口统一是 DispatcherServlet（前端控制器模式），理解流程后拦截器/异常/参数解析各就各位

**Qspring-1555（判断·web）** 每个请求先到 Controller
**答案：错。** 正确表述：请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应。原因：所有请求入口统一是 DispatcherServlet（前端控制器模式），理解流程后拦截器/异常/参数解析各就各位

**Qspring-1556（判断·web）** HandlerAdapter 负责路由匹配
**答案：错。** 正确表述：请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应。原因：所有请求入口统一是 DispatcherServlet（前端控制器模式），理解流程后拦截器/异常/参数解析各就各位

**Qspring-1557（判断·web）** 视图解析在 HandlerMapping 之前
**答案：错。** 正确表述：请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应。原因：所有请求入口统一是 DispatcherServlet（前端控制器模式），理解流程后拦截器/异常/参数解析各就各位

**Qspring-1558（场景单选·web）** 在工程实践中关于「DispatcherServlet」，下列做法符合推荐实践的是？
- A. 视图解析在 HandlerMapping 之前
- B. 每个请求先到 Controller
- C. HandlerAdapter 负责路由匹配
- D. Spring MVC 八股主线
**答案：D**
**解析：** 推荐实践：Spring MVC 八股主线。事实依据：请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应。

**Qspring-1559（场景判断·web）** 推荐实践：Spring MVC 八股主线
**答案：对。** 解析：请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应。原因：所有请求入口统一是 DispatcherServlet（前端控制器模式），理解流程后拦截器/异常/参数解析各就各位

**Qspring-1560（填空·web）** 请求处理主线：______ 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应
**答案：DispatcherServlet**。解析：所有请求入口统一是 DispatcherServlet（前端控制器模式），理解流程后拦截器/异常/参数解析各就各位

**Qspring-1561（简答·web）** 请说明「Boot」中DispatcherServlet的机制与使用要点。
**要点（标准答案）**：① 请求处理主线：DispatcherServlet 收到请求→HandlerMapping 找处理器→HandlerAdapter 执行→ViewResolver/HttpMessageConverter→响应；② 原理：所有请求入口统一是 DispatcherServlet（前端控制器模式），理解流程后拦截器/异常/参数解析各就各位；③ 使用要点：Spring MVC 八股主线。版本锚点：Spring MVC 文档。

**Qspring-1562（单选·正向·web）** 关于「Boot」的说法，正确的是？
- A. @RequestBody 由反射解析
- B. Long 转 String 没有必要（前端 JS Number 超过 2^53 会丢精度所以必要）
- C. @RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换
- D. Jackson 不可定制
**答案：C**
**解析：** @RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换。原因：默认 Jackson，配置 ObjectMapper 定制（时间格式、null 处理、Long 转字符串防前端精度丢失）。
**来源：** SP-065 · Boot（Spring MVC 文档）

**Qspring-1563（判断·web）** @RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换
**答案：对。** 解析：默认 Jackson，配置 ObjectMapper 定制（时间格式、null 处理、Long 转字符串防前端精度丢失）

**Qspring-1564（判断·web）** @RequestBody 由反射解析
**答案：错。** 正确表述：@RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换。原因：默认 Jackson，配置 ObjectMapper 定制（时间格式、null 处理、Long 转字符串防前端精度丢失）

**Qspring-1565（判断·web）** Jackson 不可定制
**答案：错。** 正确表述：@RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换。原因：默认 Jackson，配置 ObjectMapper 定制（时间格式、null 处理、Long 转字符串防前端精度丢失）

**Qspring-1566（判断·web）** Long 转 String 没有必要（前端 JS Number 超过 2^53 会丢精度所以必要）
**答案：错。** 正确表述：@RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换。原因：默认 Jackson，配置 ObjectMapper 定制（时间格式、null 处理、Long 转字符串防前端精度丢失）

**Qspring-1567（场景单选·web）** 在工程实践中关于「HttpMessageConverter」，下列做法符合推荐实践的是？
- A. 统一响应与序列化定制
- B. Long 转 String 没有必要（前端 JS Number 超过 2^53 会丢精度所以必要）
- C. Jackson 不可定制
- D. @RequestBody 由反射解析
**答案：A**
**解析：** 推荐实践：统一响应与序列化定制。事实依据：@RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换。

**Qspring-1568（场景判断·web）** 推荐实践：统一响应与序列化定制
**答案：对。** 解析：@RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换。原因：默认 Jackson，配置 ObjectMapper 定制（时间格式、null 处理、Long 转字符串防前端精度丢失）

**Qspring-1569（填空·web）** @RequestBody/@ResponseBody 由 ______ 完成 JSON 与对象转换
**答案：HttpMessageConverter**。解析：默认 Jackson，配置 ObjectMapper 定制（时间格式、null 处理、Long 转字符串防前端精度丢失）

**Qspring-1570（简答·web）** 请说明「Boot」中HttpMessageConverter的机制与使用要点。
**要点（标准答案）**：① @RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换；② 原理：默认 Jackson，配置 ObjectMapper 定制（时间格式、null 处理、Long 转字符串防前端精度丢失）；③ 使用要点：统一响应与序列化定制。版本锚点：Spring MVC 文档。

**Qspring-1571（单选·正向·web）** 关于「Boot」的说法，正确的是？
- A. 拦截器比 Filter 更早执行
- B. Filter 能访问 HandlerMethod
- C. 拦截器是 Servlet 规范一部分
- D. HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理
**答案：D**
**解析：** HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。原因：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）。
**来源：** SP-066 · Boot（Spring MVC 文档）

**Qspring-1572（判断·web）** HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理
**答案：对。** 解析：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）

**Qspring-1573（判断·web）** 拦截器比 Filter 更早执行
**答案：错。** 正确表述：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。原因：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）

**Qspring-1574（判断·web）** Filter 能访问 HandlerMethod
**答案：错。** 正确表述：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。原因：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）

**Qspring-1575（判断·web）** 拦截器是 Servlet 规范一部分
**答案：错。** 正确表述：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。原因：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）

**Qspring-1576（场景单选·web）** 在工程实践中关于「拦截器」，下列做法符合推荐实践的是？
- A. Filter 能访问 HandlerMethod
- B. 登录态/幂等/审计用拦截器，编码/全链路 header 用 Filter
- C. 拦截器比 Filter 更早执行
- D. 拦截器是 Servlet 规范一部分
**答案：B**
**解析：** 推荐实践：登录态/幂等/审计用拦截器，编码/全链路 header 用 Filter。事实依据：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。

**Qspring-1577（场景判断·web）** 推荐实践：登录态/幂等/审计用拦截器，编码/全链路 header 用 Filter
**答案：对。** 解析：HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理。原因：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）

**Qspring-1578（简答·web）** 请说明「Boot」中拦截器的机制与使用要点。
**要点（标准答案）**：① HandlerInterceptor 在 Controller 前后执行（preHandle/postHandle/afterCompletion），Bean 由 Spring 容器管理；② 原理：Filter 是 Servlet 规范在 DispatcherServlet 之前，拦截器能拿 Handler 信息与容器 Bean，afterCompletion 在视图渲染后必执行（适合清理）；③ 使用要点：登录态/幂等/审计用拦截器，编码/全链路 header 用 Filter。版本锚点：Spring MVC 文档。

**Qspring-1579（单选·正向·web）** 关于「Boot」的说法，正确的是？
- A. 全局异常处理器只能处理一个异常类型
- B. 兜底 handler 会覆盖精确匹配
- C. @RestControllerAdvice+@ExceptionHandler 全局异常映射
- D. @ExceptionHandler 在 Controller 内注册才生效
**答案：C**
**解析：** @RestControllerAdvice+@ExceptionHandler 全局异常映射。原因：统一异常响应体（code/message/traceId），按异常类型精确匹配优先级高于父类，兜底 Exception.class 兜住未预期异常。
**来源：** SP-067 · Boot（Spring MVC 文档）

**Qspring-1580（判断·web）** @RestControllerAdvice+@ExceptionHandler 全局异常映射
**答案：对。** 解析：统一异常响应体（code/message/traceId），按异常类型精确匹配优先级高于父类，兜底 Exception.class 兜住未预期异常

**Qspring-1581（判断·web）** @ExceptionHandler 在 Controller 内注册才生效
**答案：错。** 正确表述：@RestControllerAdvice+@ExceptionHandler 全局异常映射。原因：统一异常响应体（code/message/traceId），按异常类型精确匹配优先级高于父类，兜底 Exception.class 兜住未预期异常

**Qspring-1582（判断·web）** 全局异常处理器只能处理一个异常类型
**答案：错。** 正确表述：@RestControllerAdvice+@ExceptionHandler 全局异常映射。原因：统一异常响应体（code/message/traceId），按异常类型精确匹配优先级高于父类，兜底 Exception.class 兜住未预期异常

**Qspring-1583（判断·web）** 兜底 handler 会覆盖精确匹配
**答案：错。** 正确表述：@RestControllerAdvice+@ExceptionHandler 全局异常映射。原因：统一异常响应体（code/message/traceId），按异常类型精确匹配优先级高于父类，兜底 Exception.class 兜住未预期异常

**Qspring-1584（场景单选·web）** 在工程实践中关于「异常」，下列做法符合推荐实践的是？
- A. 异常体系的统一出口
- B. 兜底 handler 会覆盖精确匹配
- C. @ExceptionHandler 在 Controller 内注册才生效
- D. 全局异常处理器只能处理一个异常类型
**答案：A**
**解析：** 推荐实践：异常体系的统一出口。事实依据：@RestControllerAdvice+@ExceptionHandler 全局异常映射。

**Qspring-1585（场景判断·web）** 推荐实践：异常体系的统一出口
**答案：对。** 解析：@RestControllerAdvice+@ExceptionHandler 全局异常映射。原因：统一异常响应体（code/message/traceId），按异常类型精确匹配优先级高于父类，兜底 Exception.class 兜住未预期异常

**Qspring-1586（填空·web）** @RestControllerAdvice+@ExceptionHandler 全局______映射
**答案：异常**。解析：统一异常响应体（code/message/traceId），按异常类型精确匹配优先级高于父类，兜底 Exception.class 兜住未预期异常

**Qspring-1587（简答·web）** 请说明「Boot」中异常的机制与使用要点。
**要点（标准答案）**：① @RestControllerAdvice+@ExceptionHandler 全局异常映射；② 原理：统一异常响应体（code/message/traceId），按异常类型精确匹配优先级高于父类，兜底 Exception.class 兜住未预期异常；③ 使用要点：异常体系的统一出口。版本锚点：Spring MVC 文档。

**Qspring-1588（单选·正向·web）** 关于「Boot」的说法，正确的是？
- A. 校验在参数绑定前执行
- B. 字段上不加注解默认必填
- C. @Valid 支持@Validated 的分组
- D. @Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）
**答案：D**
**解析：** @Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。原因：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理。
**来源：** SP-068 · Boot（JSR-380）

**Qspring-1589（判断·web）** @Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）
**答案：对。** 解析：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理

**Qspring-1590（判断·web）** @Valid 支持@Validated 的分组
**答案：错。** 正确表述：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。原因：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理

**Qspring-1591（判断·web）** 校验在参数绑定前执行
**答案：错。** 正确表述：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。原因：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理

**Qspring-1592（判断·web）** 字段上不加注解默认必填
**答案：错。** 正确表述：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。原因：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理

**Qspring-1593（场景单选·web）** 在工程实践中关于「校验」，下列做法符合推荐实践的是？
- A. 字段上不加注解默认必填
- B. @Valid 支持@Validated 的分组
- C. 校验在参数绑定前执行
- D. DTO 校验注解+全局异常三件套
**答案：D**
**解析：** 推荐实践：DTO 校验注解+全局异常三件套。事实依据：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。

**Qspring-1594（场景判断·web）** 推荐实践：DTO 校验注解+全局异常三件套
**答案：对。** 解析：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。原因：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理

**Qspring-1595（填空·web）** @Validated/@Valid 触发 JSR-303 ______（Hibernate Validator 实现）
**答案：校验**。解析：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理

**Qspring-1596（简答·web）** 请说明「Boot」中校验的机制与使用要点。
**要点（标准答案）**：① @Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）；② 原理：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理；③ 使用要点：DTO 校验注解+全局异常三件套。版本锚点：JSR-380。

**Qspring-1597（单选·正向·web）** 关于「Boot」的说法，正确的是？
- A. Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端
- B. RestClient 替代了 WebClient
- C. RestTemplate 是 Boot 3 首选
- D. RestClient 是异步的
**答案：A**
**解析：** Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端。原因：RestTemplate 处于维护模式，RestClient 流式 API（get().uri().retrieve().body()），WebClient 仍是响应式场景首选。
**来源：** SP-069 · Boot（Boot 3.2）

**Qspring-1598（判断·web）** Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端
**答案：对。** 解析：RestTemplate 处于维护模式，RestClient 流式 API（get().uri().retrieve().body()），WebClient 仍是响应式场景首选

**Qspring-1599（判断·web）** RestTemplate 是 Boot 3 首选
**答案：错。** 正确表述：Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端。原因：RestTemplate 处于维护模式，RestClient 流式 API（get().uri().retrieve().body()），WebClient 仍是响应式场景首选

**Qspring-1600（判断·web）** RestClient 是异步的
**答案：错。** 正确表述：Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端。原因：RestTemplate 处于维护模式，RestClient 流式 API（get().uri().retrieve().body()），WebClient 仍是响应式场景首选

**Qspring-1601（判断·web）** RestClient 替代了 WebClient
**答案：错。** 正确表述：Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端。原因：RestTemplate 处于维护模式，RestClient 流式 API（get().uri().retrieve().body()），WebClient 仍是响应式场景首选

**Qspring-1602（场景单选·web）** 在工程实践中关于「RestClient」，下列做法符合推荐实践的是？
- A. RestClient 是异步的
- B. RestClient 替代了 WebClient
- C. RestTemplate 是 Boot 3 首选
- D. 新项目 HTTP 客户端选型
**答案：D**
**解析：** 推荐实践：新项目 HTTP 客户端选型。事实依据：Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端。

**Qspring-1603（场景判断·web）** 推荐实践：新项目 HTTP 客户端选型
**答案：对。** 解析：Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端。原因：RestTemplate 处于维护模式，RestClient 流式 API（get().uri().retrieve().body()），WebClient 仍是响应式场景首选

**Qspring-1604（填空·web）** Spring Boot 3.2 引入 ______ 同步 API 风格化 HTTP 客户端
**答案：RestClient**。解析：RestTemplate 处于维护模式，RestClient 流式 API（get().uri().retrieve().body()），WebClient 仍是响应式场景首选

**Qspring-1605（简答·web）** 请说明「Boot」中RestClient的机制与使用要点。
**要点（标准答案）**：① Spring Boot 3.2 引入 RestClient 同步 API 风格化 HTTP 客户端；② 原理：RestTemplate 处于维护模式，RestClient 流式 API（get().uri().retrieve().body()），WebClient 仍是响应式场景首选；③ 使用要点：新项目 HTTP 客户端选型。版本锚点：Boot 3.2。

**Qspring-1606（单选·正向·运维）** 关于「Boot」的说法，正确的是？
- A. Actuator 提供 /actuator/health、metrics、env 等运维端点
- B. health 端点默认关闭
- C. Actuator 是监控面板替代品
- D. Actuator 默认暴露全部端点
**答案：A**
**解析：** Actuator 提供 /actuator/health、metrics、env 等运维端点。原因：生产暴露 health+info+prometheus 其余关闭（management.endpoints.web.exposure.include），health 可聚合 DB/Redis/MQ 健康度供 K8s 探针。
**来源：** SP-070 · Boot（Boot 文档）

**Qspring-1607（判断·运维）** Actuator 提供 /actuator/health、metrics、env 等运维端点
**答案：对。** 解析：生产暴露 health+info+prometheus 其余关闭（management.endpoints.web.exposure.include），health 可聚合 DB/Redis/MQ 健康度供 K8s 探针

**Qspring-1608（判断·运维）** Actuator 默认暴露全部端点
**答案：错。** 正确表述：Actuator 提供 /actuator/health、metrics、env 等运维端点。原因：生产暴露 health+info+prometheus 其余关闭（management.endpoints.web.exposure.include），health 可聚合 DB/Redis/MQ 健康度供 K8s 探针

**Qspring-1609（判断·运维）** health 端点默认关闭
**答案：错。** 正确表述：Actuator 提供 /actuator/health、metrics、env 等运维端点。原因：生产暴露 health+info+prometheus 其余关闭（management.endpoints.web.exposure.include），health 可聚合 DB/Redis/MQ 健康度供 K8s 探针

**Qspring-1610（判断·运维）** Actuator 是监控面板替代品
**答案：错。** 正确表述：Actuator 提供 /actuator/health、metrics、env 等运维端点。原因：生产暴露 health+info+prometheus 其余关闭（management.endpoints.web.exposure.include），health 可聚合 DB/Redis/MQ 健康度供 K8s 探针

**Qspring-1611（场景单选·运维）** 在工程实践中关于「Actuator」，下列做法符合推荐实践的是？
- A. K8s liveness/readiness 探针数据源
- B. Actuator 是监控面板替代品
- C. Actuator 默认暴露全部端点
- D. health 端点默认关闭
**答案：A**
**解析：** 推荐实践：K8s liveness/readiness 探针数据源。事实依据：Actuator 提供 /actuator/health、metrics、env 等运维端点。

**Qspring-1612（场景判断·运维）** 推荐实践：K8s liveness/readiness 探针数据源
**答案：对。** 解析：Actuator 提供 /actuator/health、metrics、env 等运维端点。原因：生产暴露 health+info+prometheus 其余关闭（management.endpoints.web.exposure.include），health 可聚合 DB/Redis/MQ 健康度供 K8s 探针

**Qspring-1613（填空·运维）** ______ 提供 /actuator/health、metrics、env 等运维端点
**答案：Actuator**。解析：生产暴露 health+info+prometheus 其余关闭（management.endpoints.web.exposure.include），health 可聚合 DB/Redis/MQ 健康度供 K8s 探针

**Qspring-1614（简答·运维）** 请说明「Boot」中Actuator的机制与使用要点。
**要点（标准答案）**：① Actuator 提供 /actuator/health、metrics、env 等运维端点；② 原理：生产暴露 health+info+prometheus 其余关闭（management.endpoints.web.exposure.include），health 可聚合 DB/Redis/MQ 健康度供 K8s 探针；③ 使用要点：K8s liveness/readiness 探针数据源。版本锚点：Boot 文档。

**Qspring-1615（单选·正向·可执行 jar）** 关于「Boot」的说法，正确的是？
- A. Boot jar 与普通 jar 结构相同
- B. Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载
- C. BOOT-INF 是可选目录
- D. 外部容器部署与可执行 jar 类加载一致
**答案：B**
**解析：** Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载。原因：依赖打进 BOOT-INF/lib 内部 jar，启动类 JarLauncher 引导，解法解决了"fat jar 在容器内 classpath 问题"，代价是类加载稍慢。
**来源：** SP-071 · Boot（Boot 文档）

**Qspring-1616（判断·可执行 jar）** Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载
**答案：对。** 解析：依赖打进 BOOT-INF/lib 内部 jar，启动类 JarLauncher 引导，解法解决了"fat jar 在容器内 classpath 问题"，代价是类加载稍慢

**Qspring-1617（判断·可执行 jar）** Boot jar 与普通 jar 结构相同
**答案：错。** 正确表述：Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载。原因：依赖打进 BOOT-INF/lib 内部 jar，启动类 JarLauncher 引导，解法解决了"fat jar 在容器内 classpath 问题"，代价是类加载稍慢

**Qspring-1618（判断·可执行 jar）** 外部容器部署与可执行 jar 类加载一致
**答案：错。** 正确表述：Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载。原因：依赖打进 BOOT-INF/lib 内部 jar，启动类 JarLauncher 引导，解法解决了"fat jar 在容器内 classpath 问题"，代价是类加载稍慢

**Qspring-1619（判断·可执行 jar）** BOOT-INF 是可选目录
**答案：错。** 正确表述：Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载。原因：依赖打进 BOOT-INF/lib 内部 jar，启动类 JarLauncher 引导，解法解决了"fat jar 在容器内 classpath 问题"，代价是类加载稍慢

**Qspring-1620（场景单选·可执行 jar）** 在工程实践中关于「nested jar」，下列做法符合推荐实践的是？
- A. 外部容器部署与可执行 jar 类加载一致
- B. 理解 fat jar 加载原理
- C. Boot jar 与普通 jar 结构相同
- D. BOOT-INF 是可选目录
**答案：B**
**解析：** 推荐实践：理解 fat jar 加载原理。事实依据：Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载。

**Qspring-1621（场景判断·可执行 jar）** 推荐实践：理解 fat jar 加载原理
**答案：对。** 解析：Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载。原因：依赖打进 BOOT-INF/lib 内部 jar，启动类 JarLauncher 引导，解法解决了"fat jar 在容器内 classpath 问题"，代价是类加载稍慢

**Qspring-1622（简答·可执行 jar）** 请说明「Boot」中nested jar的机制与使用要点。
**要点（标准答案）**：① Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载；② 原理：依赖打进 BOOT-INF/lib 内部 jar，启动类 JarLauncher 引导，解法解决了"fat jar 在容器内 classpath 问题"，代价是类加载稍慢；③ 使用要点：理解 fat jar 加载原理。版本锚点：Boot 文档。

**Qspring-1623（单选·正向·测试）** 关于「Boot」的说法，正确的是？
- A. @SpringBootTest 是所有测试首选
- B. 切片测试加载全部 Bean
- C. @MockBean 会永久替换 Bean
- D. @SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest 切片测试
**答案：D**
**解析：** @SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest 切片测试。原因：切片只装配相关组件启动快，MockMvc 测 Controller，@MockBean 替换容器 Bean，集成测试慢时优先切片。
**来源：** SP-072 · Boot（Boot 测试文档）

**Qspring-1624（判断·测试）** @SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest 切片测试
**答案：对。** 解析：切片只装配相关组件启动快，MockMvc 测 Controller，@MockBean 替换容器 Bean，集成测试慢时优先切片

**Qspring-1625（判断·测试）** @SpringBootTest 是所有测试首选
**答案：错。** 正确表述：@SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest 切片测试。原因：切片只装配相关组件启动快，MockMvc 测 Controller，@MockBean 替换容器 Bean，集成测试慢时优先切片

**Qspring-1626（判断·测试）** 切片测试加载全部 Bean
**答案：错。** 正确表述：@SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest 切片测试。原因：切片只装配相关组件启动快，MockMvc 测 Controller，@MockBean 替换容器 Bean，集成测试慢时优先切片

**Qspring-1627（判断·测试）** @MockBean 会永久替换 Bean
**答案：错。** 正确表述：@SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest 切片测试。原因：切片只装配相关组件启动快，MockMvc 测 Controller，@MockBean 替换容器 Bean，集成测试慢时优先切片

**Qspring-1628（场景单选·测试）** 在工程实践中关于「切片」，下列做法符合推荐实践的是？
- A. 切片测试加载全部 Bean
- B. @SpringBootTest 是所有测试首选
- C. 测试金字塔分层落地
- D. @MockBean 会永久替换 Bean
**答案：C**
**解析：** 推荐实践：测试金字塔分层落地。事实依据：@SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest 切片测试。

**Qspring-1629（场景判断·测试）** 推荐实践：测试金字塔分层落地
**答案：对。** 解析：@SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest 切片测试。原因：切片只装配相关组件启动快，MockMvc 测 Controller，@MockBean 替换容器 Bean，集成测试慢时优先切片

**Qspring-1630（填空·测试）** @SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest ______测试
**答案：切片**。解析：切片只装配相关组件启动快，MockMvc 测 Controller，@MockBean 替换容器 Bean，集成测试慢时优先切片

**Qspring-1631（简答·测试）** 请说明「Boot」中切片的机制与使用要点。
**要点（标准答案）**：① @SpringBootTest 全上下文 vs @DataJpaTest/@WebMvcTest 切片测试；② 原理：切片只装配相关组件启动快，MockMvc 测 Controller，@MockBean 替换容器 Bean，集成测试慢时优先切片；③ 使用要点：测试金字塔分层落地。版本锚点：Boot 测试文档。

**Qspring-1632（单选·正向·版本）** 关于「Boot」的说法，正确的是？
- A. Boot 3 支持 JDK8
- B. Spring Boot 3.x 要求 JDK17+ 且 javax.* 迁移到 jakarta.*
- C. jakarta 只是改了包名无 API 变化（签名等价但二进制不兼容需重新编译）
- D. 可以渐进式混用 javax 与 jakarta
**答案：B**
**解析：** Spring Boot 3.x 要求 JDK17+ 且 javax.* 迁移到 jakarta.*。原因：Servlet 规范jakarta EE 9+ 命名空间迁移，第三方依赖（如老 MyBatis 老版本）不兼容 jakarta 时升级受阻，需升依赖版本。
**来源：** SP-073 · Boot（Boot 3.0）

**Qspring-1633（判断·版本）** Spring Boot 3.x 要求 JDK17+ 且 javax.* 迁移到 jakarta.*
**答案：对。** 解析：Servlet 规范jakarta EE 9+ 命名空间迁移，第三方依赖（如老 MyBatis 老版本）不兼容 jakarta 时升级受阻，需升依赖版本

**Qspring-1634（判断·版本）** Boot 3 支持 JDK8
**答案：错。** 正确表述：Spring Boot 3.x 要求 JDK17+ 且 javax.* 迁移到 jakarta.*。原因：Servlet 规范jakarta EE 9+ 命名空间迁移，第三方依赖（如老 MyBatis 老版本）不兼容 jakarta 时升级受阻，需升依赖版本

**Qspring-1635（判断·版本）** jakarta 只是改了包名无 API 变化（签名等价但二进制不兼容需重新编译）
**答案：错。** 正确表述：Spring Boot 3.x 要求 JDK17+ 且 javax.* 迁移到 jakarta.*。原因：Servlet 规范jakarta EE 9+ 命名空间迁移，第三方依赖（如老 MyBatis 老版本）不兼容 jakarta 时升级受阻，需升依赖版本

**Qspring-1636（判断·版本）** 可以渐进式混用 javax 与 jakarta
**答案：错。** 正确表述：Spring Boot 3.x 要求 JDK17+ 且 javax.* 迁移到 jakarta.*。原因：Servlet 规范jakarta EE 9+ 命名空间迁移，第三方依赖（如老 MyBatis 老版本）不兼容 jakarta 时升级受阻，需升依赖版本

**Qspring-1637（场景单选·版本）** 在工程实践中关于「3.x」，下列做法符合推荐实践的是？
- A. Boot 3 支持 JDK8
- B. 可以渐进式混用 javax 与 jakarta
- C. jakarta 只是改了包名无 API 变化（签名等价但二进制不兼容需重新编译）
- D. Boot 3 升级评估清单
**答案：D**
**解析：** 推荐实践：Boot 3 升级评估清单。事实依据：Spring Boot 3.x 要求 JDK17+ 且 javax.* 迁移到 jakarta.*。

**Qspring-1638（场景判断·版本）** 推荐实践：Boot 3 升级评估清单
**答案：对。** 解析：Spring Boot 3.x 要求 JDK17+ 且 javax.* 迁移到 jakarta.*。原因：Servlet 规范jakarta EE 9+ 命名空间迁移，第三方依赖（如老 MyBatis 老版本）不兼容 jakarta 时升级受阻，需升依赖版本

**Qspring-1639（填空·版本）** Spring Boot ______ 要求 JDK17+ 且 javax.* 迁移到 jakarta.*
**答案：3.x**。解析：Servlet 规范jakarta EE 9+ 命名空间迁移，第三方依赖（如老 MyBatis 老版本）不兼容 jakarta 时升级受阻，需升依赖版本

**Qspring-1640（简答·版本）** 请说明「Boot」中3.x的机制与使用要点。
**要点（标准答案）**：① Spring Boot 3.x 要求 JDK17+ 且 javax.* 迁移到 jakarta.*；② 原理：Servlet 规范jakarta EE 9+ 命名空间迁移，第三方依赖（如老 MyBatis 老版本）不兼容 jakarta 时升级受阻，需升依赖版本；③ 使用要点：Boot 3 升级评估清单。版本锚点：Boot 3.0。

**Qspring-1641（单选·正向·web）** 关于「Boot」的说法，正确的是？
- A. 内嵌容器不可更换
- B. 内嵌容器默认 Tomcat 可切 Undertow/Jetty
- C. Undertow 是默认容器
- D. 切换容器需要改代码
**答案：B**
**解析：** 内嵌容器默认 Tomcat 可切 Undertow/Jetty。原因：Undertow 高并发下吞吐与内存表现更优（案例），切换依赖 spring-boot-starter-undertow 并排除默认 starter。
**来源：** SP-074 · Boot（Boot 文档）

**Qspring-1642（判断·web）** 内嵌容器默认 Tomcat 可切 Undertow/Jetty
**答案：对。** 解析：Undertow 高并发下吞吐与内存表现更优（案例），切换依赖 spring-boot-starter-undertow 并排除默认 starter

**Qspring-1643（判断·web）** 内嵌容器不可更换
**答案：错。** 正确表述：内嵌容器默认 Tomcat 可切 Undertow/Jetty。原因：Undertow 高并发下吞吐与内存表现更优（案例），切换依赖 spring-boot-starter-undertow 并排除默认 starter

**Qspring-1644（判断·web）** Undertow 是默认容器
**答案：错。** 正确表述：内嵌容器默认 Tomcat 可切 Undertow/Jetty。原因：Undertow 高并发下吞吐与内存表现更优（案例），切换依赖 spring-boot-starter-undertow 并排除默认 starter

**Qspring-1645（判断·web）** 切换容器需要改代码
**答案：错。** 正确表述：内嵌容器默认 Tomcat 可切 Undertow/Jetty。原因：Undertow 高并发下吞吐与内存表现更优（案例），切换依赖 spring-boot-starter-undertow 并排除默认 starter

**Qspring-1646（场景单选·web）** 在工程实践中关于「容器」，下列做法符合推荐实践的是？
- A. 高并发网关型服务的容器选型
- B. 切换容器需要改代码
- C. 内嵌容器不可更换
- D. Undertow 是默认容器
**答案：A**
**解析：** 推荐实践：高并发网关型服务的容器选型。事实依据：内嵌容器默认 Tomcat 可切 Undertow/Jetty。

**Qspring-1647（场景判断·web）** 推荐实践：高并发网关型服务的容器选型
**答案：对。** 解析：内嵌容器默认 Tomcat 可切 Undertow/Jetty。原因：Undertow 高并发下吞吐与内存表现更优（案例），切换依赖 spring-boot-starter-undertow 并排除默认 starter

**Qspring-1648（填空·web）** 内嵌______默认 Tomcat 可切 Undertow/Jetty
**答案：容器**。解析：Undertow 高并发下吞吐与内存表现更优（案例），切换依赖 spring-boot-starter-undertow 并排除默认 starter

**Qspring-1649（简答·web）** 请说明「Boot」中容器的机制与使用要点。
**要点（标准答案）**：① 内嵌容器默认 Tomcat 可切 Undertow/Jetty；② 原理：Undertow 高并发下吞吐与内存表现更优（案例），切换依赖 spring-boot-starter-undertow 并排除默认 starter；③ 使用要点：高并发网关型服务的容器选型。版本锚点：Boot 文档。

**Qspring-1650（单选·正向·启动）** 关于「Boot」的说法，正确的是？
- A. 启动优化：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志
- B. @Lazy 全局开启没有副作用
- C. 启动优化只有加内存一条路
- D. 自动配置排除会破坏功能
**答案：A**
**解析：** 启动优化：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志。原因：大应用冷启动秒级→可测，K8s 弹性扩容场景启动时间直接影响就绪探针延迟。
**来源：** SP-075 · Boot（实战方法论）

**Qspring-1651（判断·启动）** 启动优化：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志
**答案：对。** 解析：大应用冷启动秒级→可测，K8s 弹性扩容场景启动时间直接影响就绪探针延迟

**Qspring-1652（判断·启动）** 启动优化只有加内存一条路
**答案：错。** 正确表述：启动优化：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志。原因：大应用冷启动秒级→可测，K8s 弹性扩容场景启动时间直接影响就绪探针延迟

**Qspring-1653（判断·启动）** @Lazy 全局开启没有副作用
**答案：错。** 正确表述：启动优化：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志。原因：大应用冷启动秒级→可测，K8s 弹性扩容场景启动时间直接影响就绪探针延迟

**Qspring-1654（判断·启动）** 自动配置排除会破坏功能
**答案：错。** 正确表述：启动优化：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志。原因：大应用冷启动秒级→可测，K8s 弹性扩容场景启动时间直接影响就绪探针延迟

**Qspring-1655（场景单选·启动）** 在工程实践中关于「优化」，下列做法符合推荐实践的是？
- A. 自动配置排除会破坏功能
- B. 启动优化只有加内存一条路
- C. @Lazy 全局开启没有副作用
- D. 启动 profiling（Boot 3 的 ApplicationStartup）定位
**答案：D**
**解析：** 推荐实践：启动 profiling（Boot 3 的 ApplicationStartup）定位。事实依据：启动优化：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志。

**Qspring-1656（场景判断·启动）** 推荐实践：启动 profiling（Boot 3 的 ApplicationStartup）定位
**答案：对。** 解析：启动优化：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志。原因：大应用冷启动秒级→可测，K8s 弹性扩容场景启动时间直接影响就绪探针延迟

**Qspring-1657（填空·启动）** 启动______：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志
**答案：优化**。解析：大应用冷启动秒级→可测，K8s 弹性扩容场景启动时间直接影响就绪探针延迟

**Qspring-1658（简答·启动）** 请说明「Boot」中优化的机制与使用要点。
**要点（标准答案）**：① 启动优化：@Lazy 延迟、排除不需要的自动配置、AppCDS、虚拟线程（3.2）、关闭不必要日志；② 原理：大应用冷启动秒级→可测，K8s 弹性扩容场景启动时间直接影响就绪探针延迟；③ 使用要点：启动 profiling（Boot 3 的 ApplicationStartup）定位。版本锚点：实战方法论。

**Qspring-1659（单选·正向·集成）** 关于「MyBatis」的说法，正确的是？
- A. Mapper 接口由 JDK 反射直接调用
- B. @MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean
- C. Mapper 接口需要写实现类
- D. @MapperScan 是 BeanPostProcessor 实现
**答案：B**
**解析：** @MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。原因：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理。
**来源：** SP-076 · MyBatis（MyBatis-Spring）

**Qspring-1660（判断·集成）** @MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean
**答案：对。** 解析：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理

**Qspring-1661（判断·集成）** Mapper 接口由 JDK 反射直接调用
**答案：错。** 正确表述：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。原因：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理

**Qspring-1662（判断·集成）** @MapperScan 是 BeanPostProcessor 实现
**答案：错。** 正确表述：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。原因：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理

**Qspring-1663（判断·集成）** Mapper 接口需要写实现类
**答案：错。** 正确表述：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。原因：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理

**Qspring-1664（场景单选·集成）** 在工程实践中关于「@MapperScan」，下列做法符合推荐实践的是？
- A. @MapperScan 是 BeanPostProcessor 实现
- B. Mapper 接口由 JDK 反射直接调用
- C. 框架集成扩展点实战案例
- D. Mapper 接口需要写实现类
**答案：C**
**解析：** 推荐实践：框架集成扩展点实战案例。事实依据：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。

**Qspring-1665（场景判断·集成）** 推荐实践：框架集成扩展点实战案例
**答案：对。** 解析：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。原因：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理

**Qspring-1666（填空·集成）** ______ 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean
**答案：@MapperScan**。解析：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理

**Qspring-1667（简答·集成）** 请说明「MyBatis」中@MapperScan的机制与使用要点。
**要点（标准答案）**：① @MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean；② 原理：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理；③ 使用要点：框架集成扩展点实战案例。版本锚点：MyBatis-Spring。

**Qspring-1668（单选·正向·缓存）** 关于「MyBatis」的说法，正确的是？
- A. 一级缓存每个方法都有效
- B. 事务内一级缓存会读到旧数据
- C. MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）
- D. 一级缓存是全局共享的
**答案：C**
**解析：** MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）。原因：MyBatis-Spring 的 SqlSessionTemplate 精确语义（本项目核对源码的结论），事务内同一 SqlSession 复用所以一级缓存命中。
**来源：** SP-077 · MyBatis（MyBatis-Spring 源码核对）

**Qspring-1669（判断·缓存）** MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）
**答案：对。** 解析：MyBatis-Spring 的 SqlSessionTemplate 精确语义（本项目核对源码的结论），事务内同一 SqlSession 复用所以一级缓存命中

**Qspring-1670（判断·缓存）** 一级缓存每个方法都有效
**答案：错。** 正确表述：MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）。原因：MyBatis-Spring 的 SqlSessionTemplate 精确语义（本项目核对源码的结论），事务内同一 SqlSession 复用所以一级缓存命中

**Qspring-1671（判断·缓存）** 一级缓存是全局共享的
**答案：错。** 正确表述：MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）。原因：MyBatis-Spring 的 SqlSessionTemplate 精确语义（本项目核对源码的结论），事务内同一 SqlSession 复用所以一级缓存命中

**Qspring-1672（判断·缓存）** 事务内一级缓存会读到旧数据
**答案：错。** 正确表述：MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）。原因：MyBatis-Spring 的 SqlSessionTemplate 精确语义（本项目核对源码的结论），事务内同一 SqlSession 复用所以一级缓存命中

**Qspring-1673（场景单选·缓存）** 在工程实践中关于「一级缓存」，下列做法符合推荐实践的是？
- A. 一级缓存的边界条件比"作用域是 session"更重要
- B. 一级缓存每个方法都有效
- C. 事务内一级缓存会读到旧数据
- D. 一级缓存是全局共享的
**答案：A**
**解析：** 推荐实践：一级缓存的边界条件比"作用域是 session"更重要。事实依据：MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）。

**Qspring-1674（场景判断·缓存）** 推荐实践：一级缓存的边界条件比"作用域是 session"更重要
**答案：对。** 解析：MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）。原因：MyBatis-Spring 的 SqlSessionTemplate 精确语义（本项目核对源码的结论），事务内同一 SqlSession 复用所以一级缓存命中

**Qspring-1675（填空·缓存）** MyBatis ______ SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）
**答案：一级缓存**。解析：MyBatis-Spring 的 SqlSessionTemplate 精确语义（本项目核对源码的结论），事务内同一 SqlSession 复用所以一级缓存命中

**Qspring-1676（简答·缓存）** 请说明「MyBatis」中一级缓存的机制与使用要点。
**要点（标准答案）**：① MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）；② 原理：MyBatis-Spring 的 SqlSessionTemplate 精确语义（本项目核对源码的结论），事务内同一 SqlSession 复用所以一级缓存命中；③ 使用要点：一级缓存的边界条件比"作用域是 session"更重要。版本锚点：MyBatis-Spring 源码核对。

**Qspring-1677（单选·正向·缓存）** 关于「MyBatis」的说法，正确的是？
- A. 二级缓存默认开启
- B. MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用
- C. 二级缓存比 Redis 缓存更可靠
- D. 二级缓存集群自动同步
**答案：B**
**解析：** MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用。原因：跨 namespace 不可见（关联查询更新不失效）、序列化开销、集群下各节点独立（除非第三方实现），生产多用 Redis 缓存替代。
**来源：** SP-078 · MyBatis（MyBatis 文档）

**Qspring-1678（判断·缓存）** MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用
**答案：对。** 解析：跨 namespace 不可见（关联查询更新不失效）、序列化开销、集群下各节点独立（除非第三方实现），生产多用 Redis 缓存替代

**Qspring-1679（判断·缓存）** 二级缓存集群自动同步
**答案：错。** 正确表述：MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用。原因：跨 namespace 不可见（关联查询更新不失效）、序列化开销、集群下各节点独立（除非第三方实现），生产多用 Redis 缓存替代

**Qspring-1680（判断·缓存）** 二级缓存默认开启
**答案：错。** 正确表述：MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用。原因：跨 namespace 不可见（关联查询更新不失效）、序列化开销、集群下各节点独立（除非第三方实现），生产多用 Redis 缓存替代

**Qspring-1681（判断·缓存）** 二级缓存比 Redis 缓存更可靠
**答案：错。** 正确表述：MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用。原因：跨 namespace 不可见（关联查询更新不失效）、序列化开销、集群下各节点独立（除非第三方实现），生产多用 Redis 缓存替代

**Qspring-1682（场景单选·缓存）** 在工程实践中关于「二级缓存」，下列做法符合推荐实践的是？
- A. 二级缓存默认开启
- B. 二级缓存集群自动同步
- C. 缓存注解失效排查时知道二级缓存边界
- D. 二级缓存比 Redis 缓存更可靠
**答案：C**
**解析：** 推荐实践：缓存注解失效排查时知道二级缓存边界。事实依据：MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用。

**Qspring-1683（场景判断·缓存）** 推荐实践：缓存注解失效排查时知道二级缓存边界
**答案：对。** 解析：MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用。原因：跨 namespace 不可见（关联查询更新不失效）、序列化开销、集群下各节点独立（除非第三方实现），生产多用 Redis 缓存替代

**Qspring-1684（填空·缓存）** MyBatis ______ namespace 级多 SqlSession 共享但生产慎用
**答案：二级缓存**。解析：跨 namespace 不可见（关联查询更新不失效）、序列化开销、集群下各节点独立（除非第三方实现），生产多用 Redis 缓存替代

**Qspring-1685（简答·缓存）** 请说明「MyBatis」中二级缓存的机制与使用要点。
**要点（标准答案）**：① MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用；② 原理：跨 namespace 不可见（关联查询更新不失效）、序列化开销、集群下各节点独立（除非第三方实现），生产多用 Redis 缓存替代；③ 使用要点：缓存注解失效排查时知道二级缓存边界。版本锚点：MyBatis 文档。

**Qspring-1686（单选·正向·抽象）** 关于「缓存」的说法，正确的是？
- A. 缓存注解在类内部自调用生效
- B. Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合
- C. 缓存 key 默认是方法所有参数
- D. @CachePut 也先查缓存
**答案：B**
**解析：** Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合。原因：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）。
**来源：** SP-079 · 缓存（Spring 文档）

**Qspring-1687（判断·抽象）** Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合
**答案：对。** 解析：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）

**Qspring-1688（判断·抽象）** @CachePut 也先查缓存
**答案：错。** 正确表述：Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合。原因：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）

**Qspring-1689（判断·抽象）** 缓存注解在类内部自调用生效
**答案：错。** 正确表述：Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合。原因：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）

**Qspring-1690（判断·抽象）** 缓存 key 默认是方法所有参数
**答案：错。** 正确表述：Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合。原因：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）

**Qspring-1691（场景单选·抽象）** 在工程实践中关于「@Cacheable」，下列做法符合推荐实践的是？
- A. 声明式缓存落地
- B. 缓存注解在类内部自调用生效
- C. 缓存 key 默认是方法所有参数
- D. @CachePut 也先查缓存
**答案：A**
**解析：** 推荐实践：声明式缓存落地。事实依据：Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合。

**Qspring-1692（场景判断·抽象）** 推荐实践：声明式缓存落地
**答案：对。** 解析：Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合。原因：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）

**Qspring-1693（填空·抽象）** Spring Cache 抽象：______/@CachePut/@CacheEvict/@Caching 组合
**答案：@Cacheable**。解析：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）

**Qspring-1694（简答·抽象）** 请说明「缓存」中@Cacheable的机制与使用要点。
**要点（标准答案）**：① Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合；② 原理：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）；③ 使用要点：声明式缓存落地。版本锚点：Spring 文档。

**Qspring-1695（单选·正向·陷阱）** 关于「缓存」的说法，正确的是？
- A. null 缓存与穿透无关
- B. allowNullValues 是默认 true
- C. @Cacheable 默认缓存 null
- D. @Cacheable 默认不缓存 null 返回值（可配 allowNullValues）
**答案：D**
**解析：** @Cacheable 默认不缓存 null 返回值（可配 allowNullValues）。原因：穿透防护要么允许 null 加短 TTL，要么代码层缓存空对象，配合缓存穿透治理。
**来源：** SP-080 · 缓存（Spring 文档）

**Qspring-1696（判断·陷阱）** @Cacheable 默认不缓存 null 返回值（可配 allowNullValues）
**答案：对。** 解析：穿透防护要么允许 null 加短 TTL，要么代码层缓存空对象，配合缓存穿透治理

**Qspring-1697（判断·陷阱）** @Cacheable 默认缓存 null
**答案：错。** 正确表述：@Cacheable 默认不缓存 null 返回值（可配 allowNullValues）。原因：穿透防护要么允许 null 加短 TTL，要么代码层缓存空对象，配合缓存穿透治理

**Qspring-1698（判断·陷阱）** null 缓存与穿透无关
**答案：错。** 正确表述：@Cacheable 默认不缓存 null 返回值（可配 allowNullValues）。原因：穿透防护要么允许 null 加短 TTL，要么代码层缓存空对象，配合缓存穿透治理

**Qspring-1699（判断·陷阱）** allowNullValues 是默认 true
**答案：错。** 正确表述：@Cacheable 默认不缓存 null 返回值（可配 allowNullValues）。原因：穿透防护要么允许 null 加短 TTL，要么代码层缓存空对象，配合缓存穿透治理

**Qspring-1700（场景单选·陷阱）** 在工程实践中关于「null」，下列做法符合推荐实践的是？
- A. 缓存穿透方案选型
- B. null 缓存与穿透无关
- C. @Cacheable 默认缓存 null
- D. allowNullValues 是默认 true
**答案：A**
**解析：** 推荐实践：缓存穿透方案选型。事实依据：@Cacheable 默认不缓存 null 返回值（可配 allowNullValues）。

**Qspring-1701（场景判断·陷阱）** 推荐实践：缓存穿透方案选型
**答案：对。** 解析：@Cacheable 默认不缓存 null 返回值（可配 allowNullValues）。原因：穿透防护要么允许 null 加短 TTL，要么代码层缓存空对象，配合缓存穿透治理

**Qspring-1702（填空·陷阱）** @Cacheable 默认不缓存 ______ 返回值（可配 allowNullValues）
**答案：null**。解析：穿透防护要么允许 null 加短 TTL，要么代码层缓存空对象，配合缓存穿透治理

**Qspring-1703（简答·陷阱）** 请说明「缓存」中null的机制与使用要点。
**要点（标准答案）**：① @Cacheable 默认不缓存 null 返回值（可配 allowNullValues）；② 原理：穿透防护要么允许 null 加短 TTL，要么代码层缓存空对象，配合缓存穿透治理；③ 使用要点：缓存穿透方案选型。版本锚点：Spring 文档。

**Qspring-1704（单选·正向·陷阱）** 关于「缓存」的说法，正确的是？
- A. 缓存注解同样受自调用失效影响
- B. 缓存注解不受自调用影响
- C. Caffeine 缓存注解例外
- D. 把注解加在被调方法上即可
**答案：A**
**解析：** 缓存注解同样受自调用失效影响。原因：与事务/AOP 同源，同类方法互调不走代理缓存不生效。
**来源：** SP-081 · 缓存（实战共识）

**Qspring-1705（判断·陷阱）** 缓存注解同样受自调用失效影响
**答案：对。** 解析：与事务/AOP 同源，同类方法互调不走代理缓存不生效

**Qspring-1706（判断·陷阱）** 缓存注解不受自调用影响
**答案：错。** 正确表述：缓存注解同样受自调用失效影响。原因：与事务/AOP 同源，同类方法互调不走代理缓存不生效

**Qspring-1707（判断·陷阱）** Caffeine 缓存注解例外
**答案：错。** 正确表述：缓存注解同样受自调用失效影响。原因：与事务/AOP 同源，同类方法互调不走代理缓存不生效

**Qspring-1708（判断·陷阱）** 把注解加在被调方法上即可
**答案：错。** 正确表述：缓存注解同样受自调用失效影响。原因：与事务/AOP 同源，同类方法互调不走代理缓存不生效

**Qspring-1709（场景单选·陷阱）** 在工程实践中关于「自调用」，下列做法符合推荐实践的是？
- A. 把注解加在被调方法上即可
- B. 缓存失效排查第三板斧
- C. 缓存注解不受自调用影响
- D. Caffeine 缓存注解例外
**答案：B**
**解析：** 推荐实践：缓存失效排查第三板斧。事实依据：缓存注解同样受自调用失效影响。

**Qspring-1710（场景判断·陷阱）** 推荐实践：缓存失效排查第三板斧
**答案：对。** 解析：缓存注解同样受自调用失效影响。原因：与事务/AOP 同源，同类方法互调不走代理缓存不生效

**Qspring-1711（填空·陷阱）** 缓存注解同样受______失效影响
**答案：自调用**。解析：与事务/AOP 同源，同类方法互调不走代理缓存不生效

**Qspring-1712（简答·陷阱）** 请说明「缓存」中自调用的机制与使用要点。
**要点（标准答案）**：① 缓存注解同样受自调用失效影响；② 原理：与事务/AOP 同源，同类方法互调不走代理缓存不生效；③ 使用要点：缓存失效排查第三板斧。版本锚点：实战共识。

**Qspring-1713（单选·正向·对比）** 关于「WebFlux」的说法，正确的是？
- A. 响应式无需学习成本
- B. WebFlux 是响应式非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高
- C. WebFlux 吞吐一定高于 MVC
- D. WebFlux 让接口延迟更低
**答案：B**
**解析：** WebFlux 是响应式非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高。原因：少量线程处理大量连接（Netty），回溯调试难、生态（JDBC 阻塞）受限，R2DBC 弥补数据库层，选型看团队与场景。
**来源：** SP-082 · WebFlux（Spring WebFlux 文档）

**Qspring-1714（判断·对比）** WebFlux 是响应式非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高
**答案：对。** 解析：少量线程处理大量连接（Netty），回溯调试难、生态（JDBC 阻塞）受限，R2DBC 弥补数据库层，选型看团队与场景

**Qspring-1715（判断·对比）** WebFlux 吞吐一定高于 MVC
**答案：错。** 正确表述：WebFlux 是响应式非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高。原因：少量线程处理大量连接（Netty），回溯调试难、生态（JDBC 阻塞）受限，R2DBC 弥补数据库层，选型看团队与场景

**Qspring-1716（判断·对比）** WebFlux 让接口延迟更低
**答案：错。** 正确表述：WebFlux 是响应式非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高。原因：少量线程处理大量连接（Netty），回溯调试难、生态（JDBC 阻塞）受限，R2DBC 弥补数据库层，选型看团队与场景

**Qspring-1717（判断·对比）** 响应式无需学习成本
**答案：错。** 正确表述：WebFlux 是响应式非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高。原因：少量线程处理大量连接（Netty），回溯调试难、生态（JDBC 阻塞）受限，R2DBC 弥补数据库层，选型看团队与场景

**Qspring-1718（场景单选·对比）** 在工程实践中关于「响应式」，下列做法符合推荐实践的是？
- A. WebFlux 吞吐一定高于 MVC
- B. 响应式无需学习成本
- C. IO 密集高并发网关场景
- D. WebFlux 让接口延迟更低
**答案：C**
**解析：** 推荐实践：IO 密集高并发网关场景。事实依据：WebFlux 是响应式非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高。

**Qspring-1719（场景判断·对比）** 推荐实践：IO 密集高并发网关场景
**答案：对。** 解析：WebFlux 是响应式非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高。原因：少量线程处理大量连接（Netty），回溯调试难、生态（JDBC 阻塞）受限，R2DBC 弥补数据库层，选型看团队与场景

**Qspring-1720（填空·对比）** WebFlux 是______非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高
**答案：响应式**。解析：少量线程处理大量连接（Netty），回溯调试难、生态（JDBC 阻塞）受限，R2DBC 弥补数据库层，选型看团队与场景

**Qspring-1721（简答·对比）** 请说明「WebFlux」中响应式的机制与使用要点。
**要点（标准答案）**：① WebFlux 是响应式非阻塞栈（Reactor）吞吐高于阻塞栈但心智与调试成本高；② 原理：少量线程处理大量连接（Netty），回溯调试难、生态（JDBC 阻塞）受限，R2DBC 弥补数据库层，选型看团队与场景；③ 使用要点：IO 密集高并发网关场景。版本锚点：Spring WebFlux 文档。

**Qspring-1722（单选·正向·虚拟线程）** 关于「Boot」的说法，正确的是？
- A. 虚拟线程改变编程模型需要重写
- B. Spring Boot 3.2 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程
- C. 虚拟线程与 @Async 不兼容
- D. 开启后 CPU 密集也加速
**答案：B**
**解析：** Spring Boot 3.2 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程。原因：IO 密集服务吞吐显著提升（阻塞时让出载体线程），synchronized pin 载体的问题在 JDK24 修复，代码零改动升级。
**来源：** SP-083 · Boot（Boot 3.2）

**Qspring-1723（判断·虚拟线程）** Spring Boot 3.2 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程
**答案：对。** 解析：IO 密集服务吞吐显著提升（阻塞时让出载体线程），synchronized pin 载体的问题在 JDK24 修复，代码零改动升级

**Qspring-1724（判断·虚拟线程）** 虚拟线程改变编程模型需要重写
**答案：错。** 正确表述：Spring Boot 3.2 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程。原因：IO 密集服务吞吐显著提升（阻塞时让出载体线程），synchronized pin 载体的问题在 JDK24 修复，代码零改动升级

**Qspring-1725（判断·虚拟线程）** 开启后 CPU 密集也加速
**答案：错。** 正确表述：Spring Boot 3.2 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程。原因：IO 密集服务吞吐显著提升（阻塞时让出载体线程），synchronized pin 载体的问题在 JDK24 修复，代码零改动升级

**Qspring-1726（判断·虚拟线程）** 虚拟线程与 @Async 不兼容
**答案：错。** 正确表述：Spring Boot 3.2 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程。原因：IO 密集服务吞吐显著提升（阻塞时让出载体线程），synchronized pin 载体的问题在 JDK24 修复，代码零改动升级

**Qspring-1727（场景单选·虚拟线程）** 在工程实践中关于「3.2」，下列做法符合推荐实践的是？
- A. 开启后 CPU 密集也加速
- B. 虚拟线程与 @Async 不兼容
- C. 虚拟线程改变编程模型需要重写
- D. IO 密集服务低成本扩容
**答案：D**
**解析：** 推荐实践：IO 密集服务低成本扩容。事实依据：Spring Boot 3.2 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程。

**Qspring-1728（场景判断·虚拟线程）** 推荐实践：IO 密集服务低成本扩容
**答案：对。** 解析：Spring Boot 3.2 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程。原因：IO 密集服务吞吐显著提升（阻塞时让出载体线程），synchronized pin 载体的问题在 JDK24 修复，代码零改动升级

**Qspring-1729（填空·虚拟线程）** Spring Boot ______ 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程
**答案：3.2**。解析：IO 密集服务吞吐显著提升（阻塞时让出载体线程），synchronized pin 载体的问题在 JDK24 修复，代码零改动升级

**Qspring-1730（简答·虚拟线程）** 请说明「Boot」中3.2的机制与使用要点。
**要点（标准答案）**：① Spring Boot 3.2 开 spring.threads.virtual.enabled=true 让 Tomcat/@Async 走虚拟线程；② 原理：IO 密集服务吞吐显著提升（阻塞时让出载体线程），synchronized pin 载体的问题在 JDK24 修复，代码零改动升级；③ 使用要点：IO 密集服务低成本扩容。版本锚点：Boot 3.2。

**Qspring-1731（单选·正向·事务）** 关于「测试」的说法，正确的是？
- A. 测试事务会真实提交
- B. 所有集成测试都应加 @Transactional
- C. 回滚机制影响被测代码语义
- D. 测试类 @Transactional 默认每测试方法后回滚不污染库
**答案：D**
**解析：** 测试类 @Transactional 默认每测试方法后回滚不污染库。原因：由测试框架管理（非生产代理语义），需要真实提交的集成步骤用 @Commit 或编程式事务。
**来源：** SP-084 · 测试（Spring Test 文档）

**Qspring-1732（判断·事务）** 测试类 @Transactional 默认每测试方法后回滚不污染库
**答案：对。** 解析：由测试框架管理（非生产代理语义），需要真实提交的集成步骤用 @Commit 或编程式事务

**Qspring-1733（判断·事务）** 测试事务会真实提交
**答案：错。** 正确表述：测试类 @Transactional 默认每测试方法后回滚不污染库。原因：由测试框架管理（非生产代理语义），需要真实提交的集成步骤用 @Commit 或编程式事务

**Qspring-1734（判断·事务）** 回滚机制影响被测代码语义
**答案：错。** 正确表述：测试类 @Transactional 默认每测试方法后回滚不污染库。原因：由测试框架管理（非生产代理语义），需要真实提交的集成步骤用 @Commit 或编程式事务

**Qspring-1735（判断·事务）** 所有集成测试都应加 @Transactional
**答案：错。** 正确表述：测试类 @Transactional 默认每测试方法后回滚不污染库。原因：由测试框架管理（非生产代理语义），需要真实提交的集成步骤用 @Commit 或编程式事务

**Qspring-1736（场景单选·事务）** 在工程实践中关于「@Transactional 回滚」，下列做法符合推荐实践的是？
- A. 集成测试的标准姿势
- B. 回滚机制影响被测代码语义
- C. 所有集成测试都应加 @Transactional
- D. 测试事务会真实提交
**答案：A**
**解析：** 推荐实践：集成测试的标准姿势。事实依据：测试类 @Transactional 默认每测试方法后回滚不污染库。

**Qspring-1737（场景判断·事务）** 推荐实践：集成测试的标准姿势
**答案：对。** 解析：测试类 @Transactional 默认每测试方法后回滚不污染库。原因：由测试框架管理（非生产代理语义），需要真实提交的集成步骤用 @Commit 或编程式事务

**Qspring-1738（简答·事务）** 请说明「测试」中@Transactional 回滚的机制与使用要点。
**要点（标准答案）**：① 测试类 @Transactional 默认每测试方法后回滚不污染库；② 原理：由测试框架管理（非生产代理语义），需要真实提交的集成步骤用 @Commit 或编程式事务；③ 使用要点：集成测试的标准姿势。版本锚点：Spring Test 文档。

**Qspring-1739（单选·正向·扩展）** 关于「容器」的说法，正确的是？
- A. @PostConstruct 时所有 Bean 已就绪
- B. 该事件在每个 Bean 初始化时发布
- C. ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化
- D. ApplicationRunner 与该事件同时触发
**答案：C**
**解析：** ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化。原因：此时所有 Bean 就绪（含非懒加载），对比 @PostConstruct（自身就绪）与 ApplicationRunner（Boot 专属）的时机差异。
**来源：** SP-085 · 容器（Spring 文档）

**Qspring-1740（判断·扩展）** ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化
**答案：对。** 解析：此时所有 Bean 就绪（含非懒加载），对比 @PostConstruct（自身就绪）与 ApplicationRunner（Boot 专属）的时机差异

**Qspring-1741（判断·扩展）** 该事件在每个 Bean 初始化时发布
**答案：错。** 正确表述：ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化。原因：此时所有 Bean 就绪（含非懒加载），对比 @PostConstruct（自身就绪）与 ApplicationRunner（Boot 专属）的时机差异

**Qspring-1742（判断·扩展）** @PostConstruct 时所有 Bean 已就绪
**答案：错。** 正确表述：ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化。原因：此时所有 Bean 就绪（含非懒加载），对比 @PostConstruct（自身就绪）与 ApplicationRunner（Boot 专属）的时机差异

**Qspring-1743（判断·扩展）** ApplicationRunner 与该事件同时触发
**答案：错。** 正确表述：ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化。原因：此时所有 Bean 就绪（含非懒加载），对比 @PostConstruct（自身就绪）与 ApplicationRunner（Boot 专属）的时机差异

**Qspring-1744（场景单选·扩展）** 在工程实践中关于「ContextRefreshedEvent」，下列做法符合推荐实践的是？
- A. ApplicationRunner 与该事件同时触发
- B. @PostConstruct 时所有 Bean 已就绪
- C. 全量就绪后的预热/校验任务
- D. 该事件在每个 Bean 初始化时发布
**答案：C**
**解析：** 推荐实践：全量就绪后的预热/校验任务。事实依据：ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化。

**Qspring-1745（场景判断·扩展）** 推荐实践：全量就绪后的预热/校验任务
**答案：对。** 解析：ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化。原因：此时所有 Bean 就绪（含非懒加载），对比 @PostConstruct（自身就绪）与 ApplicationRunner（Boot 专属）的时机差异

**Qspring-1746（填空·扩展）** ______ 在容器刷新完成后发布适合做启动后初始化
**答案：ContextRefreshedEvent**。解析：此时所有 Bean 就绪（含非懒加载），对比 @PostConstruct（自身就绪）与 ApplicationRunner（Boot 专属）的时机差异

**Qspring-1747（简答·扩展）** 请说明「容器」中ContextRefreshedEvent的机制与使用要点。
**要点（标准答案）**：① ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化；② 原理：此时所有 Bean 就绪（含非懒加载），对比 @PostConstruct（自身就绪）与 ApplicationRunner（Boot 专属）的时机差异；③ 使用要点：全量就绪后的预热/校验任务。版本锚点：Spring 文档。

**Qspring-1748（单选·正向·扩展）** 关于「容器」的说法，正确的是？
- A. @Import 只能导入配置类
- B. 三种用法行为相同
- C. @Import 会覆盖已有 Bean
- D. @Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar
**答案：D**
**解析：** @Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar。原因：Selector 按条件批量导入（@EnableAutoConfiguration 原理），Registrar 完全自定义注册（@MapperScan 原理），是框架级扩展的入口。
**来源：** SP-086 · 容器（Spring 文档）

**Qspring-1749（判断·扩展）** @Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar
**答案：对。** 解析：Selector 按条件批量导入（@EnableAutoConfiguration 原理），Registrar 完全自定义注册（@MapperScan 原理），是框架级扩展的入口

**Qspring-1750（判断·扩展）** @Import 只能导入配置类
**答案：错。** 正确表述：@Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar。原因：Selector 按条件批量导入（@EnableAutoConfiguration 原理），Registrar 完全自定义注册（@MapperScan 原理），是框架级扩展的入口

**Qspring-1751（判断·扩展）** 三种用法行为相同
**答案：错。** 正确表述：@Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar。原因：Selector 按条件批量导入（@EnableAutoConfiguration 原理），Registrar 完全自定义注册（@MapperScan 原理），是框架级扩展的入口

**Qspring-1752（判断·扩展）** @Import 会覆盖已有 Bean
**答案：错。** 正确表述：@Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar。原因：Selector 按条件批量导入（@EnableAutoConfiguration 原理），Registrar 完全自定义注册（@MapperScan 原理），是框架级扩展的入口

**Qspring-1753（场景单选·扩展）** 在工程实践中关于「Import」，下列做法符合推荐实践的是？
- A. @Import 会覆盖已有 Bean
- B. @Import 只能导入配置类
- C. 读框架源码的钥匙
- D. 三种用法行为相同
**答案：C**
**解析：** 推荐实践：读框架源码的钥匙。事实依据：@Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar。

**Qspring-1754（场景判断·扩展）** 推荐实践：读框架源码的钥匙
**答案：对。** 解析：@Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar。原因：Selector 按条件批量导入（@EnableAutoConfiguration 原理），Registrar 完全自定义注册（@MapperScan 原理），是框架级扩展的入口

**Qspring-1755（填空·扩展）** @______ 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar
**答案：Import**。解析：Selector 按条件批量导入（@EnableAutoConfiguration 原理），Registrar 完全自定义注册（@MapperScan 原理），是框架级扩展的入口

**Qspring-1756（简答·扩展）** 请说明「容器」中Import的机制与使用要点。
**要点（标准答案）**：① @Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar；② 原理：Selector 按条件批量导入（@EnableAutoConfiguration 原理），Registrar 完全自定义注册（@MapperScan 原理），是框架级扩展的入口；③ 使用要点：读框架源码的钥匙。版本锚点：Spring 文档。

**Qspring-1757（单选·正向·配置）** 关于「Boot」的说法，正确的是？
- A. 配置文件优先级最高
- B. 外部化配置必须重启进程才生效（Boot 支持部分热刷新）
- C. 环境变量不能覆盖文件配置
- D. 配置外部化顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件
**答案：D**
**解析：** 配置外部化顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件。原因：12 因子应用原则，同一镜像跨环境部署只换环境变量，K8s ConfigMap/Secret 注入环境变量。
**来源：** SP-087 · Boot（Boot 文档）

**Qspring-1758（判断·配置）** 配置外部化顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件
**答案：对。** 解析：12 因子应用原则，同一镜像跨环境部署只换环境变量，K8s ConfigMap/Secret 注入环境变量

**Qspring-1759（判断·配置）** 配置文件优先级最高
**答案：错。** 正确表述：配置外部化顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件。原因：12 因子应用原则，同一镜像跨环境部署只换环境变量，K8s ConfigMap/Secret 注入环境变量

**Qspring-1760（判断·配置）** 环境变量不能覆盖文件配置
**答案：错。** 正确表述：配置外部化顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件。原因：12 因子应用原则，同一镜像跨环境部署只换环境变量，K8s ConfigMap/Secret 注入环境变量

**Qspring-1761（判断·配置）** 外部化配置必须重启进程才生效（Boot 支持部分热刷新）
**答案：错。** 正确表述：配置外部化顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件。原因：12 因子应用原则，同一镜像跨环境部署只换环境变量，K8s ConfigMap/Secret 注入环境变量

**Qspring-1762（场景单选·配置）** 在工程实践中关于「外部化」，下列做法符合推荐实践的是？
- A. 配置文件优先级最高
- B. 环境变量不能覆盖文件配置
- C. 外部化配置必须重启进程才生效（Boot 支持部分热刷新）
- D. 云原生部署基本功
**答案：D**
**解析：** 推荐实践：云原生部署基本功。事实依据：配置外部化顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件。

**Qspring-1763（场景判断·配置）** 推荐实践：云原生部署基本功
**答案：对。** 解析：配置外部化顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件。原因：12 因子应用原则，同一镜像跨环境部署只换环境变量，K8s ConfigMap/Secret 注入环境变量

**Qspring-1764（填空·配置）** 配置______顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件
**答案：外部化**。解析：12 因子应用原则，同一镜像跨环境部署只换环境变量，K8s ConfigMap/Secret 注入环境变量

**Qspring-1765（简答·配置）** 请说明「Boot」中外部化的机制与使用要点。
**要点（标准答案）**：① 配置外部化顺序：命令行 > SPRING_APPLICATION_JSON > 环境变量 > 配置文件；② 原理：12 因子应用原则，同一镜像跨环境部署只换环境变量，K8s ConfigMap/Secret 注入环境变量；③ 使用要点：云原生部署基本功。版本锚点：Boot 文档。

**Qspring-1766（单选·正向·Spring Security）** 关于「安全」的说法，正确的是？
- A. Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）
- B. FilterChainProxy 只有一个过滤器
- C. Spring Security 是拦截器实现
- D. 安全配置在 Controller 层
**答案：A**
**解析：** Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）。原因：认证（AuthenticationManager）、授权（AuthorizationManager）、CSRF、会话管理各是一环，与业务拦截器（HandlerInterceptor）职责分层。
**来源：** SP-088 · 安全（Spring Security 文档）

**Qspring-1767（判断·Spring Security）** Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）
**答案：对。** 解析：认证（AuthenticationManager）、授权（AuthorizationManager）、CSRF、会话管理各是一环，与业务拦截器（HandlerInterceptor）职责分层

**Qspring-1768（判断·Spring Security）** Spring Security 是拦截器实现
**答案：错。** 正确表述：Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）。原因：认证（AuthenticationManager）、授权（AuthorizationManager）、CSRF、会话管理各是一环，与业务拦截器（HandlerInterceptor）职责分层

**Qspring-1769（判断·Spring Security）** FilterChainProxy 只有一个过滤器
**答案：错。** 正确表述：Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）。原因：认证（AuthenticationManager）、授权（AuthorizationManager）、CSRF、会话管理各是一环，与业务拦截器（HandlerInterceptor）职责分层

**Qspring-1770（判断·Spring Security）** 安全配置在 Controller 层
**答案：错。** 正确表述：Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）。原因：认证（AuthenticationManager）、授权（AuthorizationManager）、CSRF、会话管理各是一环，与业务拦截器（HandlerInterceptor）职责分层

**Qspring-1771（场景单选·Spring Security）** 在工程实践中关于「过滤器链」，下列做法符合推荐实践的是？
- A. 安全配置在 Controller 层
- B. 认证授权体系的主干
- C. Spring Security 是拦截器实现
- D. FilterChainProxy 只有一个过滤器
**答案：B**
**解析：** 推荐实践：认证授权体系的主干。事实依据：Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）。

**Qspring-1772（场景判断·Spring Security）** 推荐实践：认证授权体系的主干
**答案：对。** 解析：Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）。原因：认证（AuthenticationManager）、授权（AuthorizationManager）、CSRF、会话管理各是一环，与业务拦截器（HandlerInterceptor）职责分层

**Qspring-1773（简答·Spring Security）** 请说明「安全」中过滤器链的机制与使用要点。
**要点（标准答案）**：① Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）；② 原理：认证（AuthenticationManager）、授权（AuthorizationManager）、CSRF、会话管理各是一环，与业务拦截器（HandlerInterceptor）职责分层；③ 使用要点：认证授权体系的主干。版本锚点：Spring Security 文档。

**Qspring-1774（单选·正向·认证）** 关于「安全」的说法，正确的是？
- A. JWT 载荷加密不可读
- B. JWT 无状态认证：签发→携带→过滤链校验签名
- C. JWT 服务端需存储 token
- D. JWT 天然防重放
**答案：B**
**解析：** JWT 无状态认证：签发→携带→过滤链校验签名。原因：服务端不存会话水平扩展友好，缺点：无法主动失效（需黑名单）、payload 明文（不放敏感信息、HS256/RSA 签名）。
**来源：** SP-089 · 安全（实战共识）

**Qspring-1775（判断·认证）** JWT 无状态认证：签发→携带→过滤链校验签名
**答案：对。** 解析：服务端不存会话水平扩展友好，缺点：无法主动失效（需黑名单）、payload 明文（不放敏感信息、HS256/RSA 签名）

**Qspring-1776（判断·认证）** JWT 服务端需存储 token
**答案：错。** 正确表述：JWT 无状态认证：签发→携带→过滤链校验签名。原因：服务端不存会话水平扩展友好，缺点：无法主动失效（需黑名单）、payload 明文（不放敏感信息、HS256/RSA 签名）

**Qspring-1777（判断·认证）** JWT 载荷加密不可读
**答案：错。** 正确表述：JWT 无状态认证：签发→携带→过滤链校验签名。原因：服务端不存会话水平扩展友好，缺点：无法主动失效（需黑名单）、payload 明文（不放敏感信息、HS256/RSA 签名）

**Qspring-1778（判断·认证）** JWT 天然防重放
**答案：错。** 正确表述：JWT 无状态认证：签发→携带→过滤链校验签名。原因：服务端不存会话水平扩展友好，缺点：无法主动失效（需黑名单）、payload 明文（不放敏感信息、HS256/RSA 签名）

**Qspring-1779（场景单选·认证）** 在工程实践中关于「JWT」，下列做法符合推荐实践的是？
- A. JWT 天然防重放
- B. JWT 载荷加密不可读
- C. 分布式会话方案对比
- D. JWT 服务端需存储 token
**答案：C**
**解析：** 推荐实践：分布式会话方案对比。事实依据：JWT 无状态认证：签发→携带→过滤链校验签名。

**Qspring-1780（场景判断·认证）** 推荐实践：分布式会话方案对比
**答案：对。** 解析：JWT 无状态认证：签发→携带→过滤链校验签名。原因：服务端不存会话水平扩展友好，缺点：无法主动失效（需黑名单）、payload 明文（不放敏感信息、HS256/RSA 签名）

**Qspring-1781（填空·认证）** ______ 无状态认证：签发→携带→过滤链校验签名
**答案：JWT**。解析：服务端不存会话水平扩展友好，缺点：无法主动失效（需黑名单）、payload 明文（不放敏感信息、HS256/RSA 签名）

**Qspring-1782（简答·认证）** 请说明「安全」中JWT的机制与使用要点。
**要点（标准答案）**：① JWT 无状态认证：签发→携带→过滤链校验签名；② 原理：服务端不存会话水平扩展友好，缺点：无法主动失效（需黑名单）、payload 明文（不放敏感信息、HS256/RSA 签名）；③ 使用要点：分布式会话方案对比。版本锚点：实战共识。

**Qspring-1783（单选·正向·认证）** 关于「安全」的说法，正确的是？
- A. Session 方案无法水平扩展
- B. 分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含
- C. 两方案性能差距是主因
- D. JWT 无任何中心依赖（刷新仍需存储）
**答案：B**
**解析：** 分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含。原因：集中式可随时踢人（运维可控），JWT 免中心存储但撤销难，混合方案：短 JWT+refresh token。
**来源：** SP-090 · 安全（实战共识）

**Qspring-1784（判断·认证）** 分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含
**答案：对。** 解析：集中式可随时踢人（运维可控），JWT 免中心存储但撤销难，混合方案：短 JWT+refresh token

**Qspring-1785（判断·认证）** Session 方案无法水平扩展
**答案：错。** 正确表述：分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含。原因：集中式可随时踢人（运维可控），JWT 免中心存储但撤销难，混合方案：短 JWT+refresh token

**Qspring-1786（判断·认证）** JWT 无任何中心依赖（刷新仍需存储）
**答案：错。** 正确表述：分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含。原因：集中式可随时踢人（运维可控），JWT 免中心存储但撤销难，混合方案：短 JWT+refresh token

**Qspring-1787（判断·认证）** 两方案性能差距是主因
**答案：错。** 正确表述：分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含。原因：集中式可随时踢人（运维可控），JWT 免中心存储但撤销难，混合方案：短 JWT+refresh token

**Qspring-1788（场景单选·认证）** 在工程实践中关于「Session vs JWT」，下列做法符合推荐实践的是？
- A. 按业务需求选型（可撤销性）
- B. 两方案性能差距是主因
- C. Session 方案无法水平扩展
- D. JWT 无任何中心依赖（刷新仍需存储）
**答案：A**
**解析：** 推荐实践：按业务需求选型（可撤销性）。事实依据：分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含。

**Qspring-1789（场景判断·认证）** 推荐实践：按业务需求选型（可撤销性）
**答案：对。** 解析：分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含。原因：集中式可随时踢人（运维可控），JWT 免中心存储但撤销难，混合方案：短 JWT+refresh token

**Qspring-1790（简答·认证）** 请说明「安全」中Session vs JWT的机制与使用要点。
**要点（标准答案）**：① 分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含；② 原理：集中式可随时踢人（运维可控），JWT 免中心存储但撤销难，混合方案：短 JWT+refresh token；③ 使用要点：按业务需求选型（可撤销性）。版本锚点：实战共识。

**Qspring-1791（单选·正向·监控）** 关于「Boot」的说法，正确的是？
- A. 指标采集有显著性能开销
- B. 业务指标不能自定义
- C. Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana
- D. Micrometer 是监控系统
**答案：C**
**解析：** Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana。原因：自动暴露 JVM（内存/GC/线程）、HTTP（QPS/P99）、连接池指标，自定义 @Timed/MeterRegistry 埋业务指标。
**来源：** SP-091 · Boot（Boot 文档）

**Qspring-1792（判断·监控）** Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana
**答案：对。** 解析：自动暴露 JVM（内存/GC/线程）、HTTP（QPS/P99）、连接池指标，自定义 @Timed/MeterRegistry 埋业务指标

**Qspring-1793（判断·监控）** Micrometer 是监控系统
**答案：错。** 正确表述：Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana。原因：自动暴露 JVM（内存/GC/线程）、HTTP（QPS/P99）、连接池指标，自定义 @Timed/MeterRegistry 埋业务指标

**Qspring-1794（判断·监控）** 指标采集有显著性能开销
**答案：错。** 正确表述：Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana。原因：自动暴露 JVM（内存/GC/线程）、HTTP（QPS/P99）、连接池指标，自定义 @Timed/MeterRegistry 埋业务指标

**Qspring-1795（判断·监控）** 业务指标不能自定义
**答案：错。** 正确表述：Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana。原因：自动暴露 JVM（内存/GC/线程）、HTTP（QPS/P99）、连接池指标，自定义 @Timed/MeterRegistry 埋业务指标

**Qspring-1796（场景单选·监控）** 在工程实践中关于「metrics」，下列做法符合推荐实践的是？
- A. 业务指标不能自定义
- B. 可观测性三支柱之一（metrics）
- C. 指标采集有显著性能开销
- D. Micrometer 是监控系统
**答案：B**
**解析：** 推荐实践：可观测性三支柱之一（metrics）。事实依据：Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana。

**Qspring-1797（场景判断·监控）** 推荐实践：可观测性三支柱之一（metrics）
**答案：对。** 解析：Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana。原因：自动暴露 JVM（内存/GC/线程）、HTTP（QPS/P99）、连接池指标，自定义 @Timed/MeterRegistry 埋业务指标

**Qspring-1798（简答·监控）** 请说明「Boot」中metrics的机制与使用要点。
**要点（标准答案）**：① Micrometer 是 Boot 的指标门面对接 Prometheus/Grafana；② 原理：自动暴露 JVM（内存/GC/线程）、HTTP（QPS/P99）、连接池指标，自定义 @Timed/MeterRegistry 埋业务指标；③ 使用要点：可观测性三支柱之一（metrics）。版本锚点：Boot 文档。

**Qspring-1799（单选·正向·tracing）** 关于「可观测」的说法，正确的是？
- A. 每服务重新生成 traceId
- B. traceId 由业务代码手动生成
- C. 全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递
- D. 跨 MQ 传递自动完成
**答案：C**
**解析：** 全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递。原因：通过 HTTP header（W3C traceparent）与 MQ 属性传递，日志 MDC 打 traceId 串起单请求全部日志。
**来源：** SP-092 · 可观测（实战共识）

**Qspring-1800（判断·tracing）** 全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递
**答案：对。** 解析：通过 HTTP header（W3C traceparent）与 MQ 属性传递，日志 MDC 打 traceId 串起单请求全部日志

**Qspring-1801（判断·tracing）** traceId 由业务代码手动生成
**答案：错。** 正确表述：全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递。原因：通过 HTTP header（W3C traceparent）与 MQ 属性传递，日志 MDC 打 traceId 串起单请求全部日志

**Qspring-1802（判断·tracing）** 跨 MQ 传递自动完成
**答案：错。** 正确表述：全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递。原因：通过 HTTP header（W3C traceparent）与 MQ 属性传递，日志 MDC 打 traceId 串起单请求全部日志

**Qspring-1803（判断·tracing）** 每服务重新生成 traceId
**答案：错。** 正确表述：全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递。原因：通过 HTTP header（W3C traceparent）与 MQ 属性传递，日志 MDC 打 traceId 串起单请求全部日志

**Qspring-1804（场景单选·tracing）** 在工程实践中关于「traceId」，下列做法符合推荐实践的是？
- A. 可观测性第二支柱（tracing）
- B. traceId 由业务代码手动生成
- C. 每服务重新生成 traceId
- D. 跨 MQ 传递自动完成
**答案：A**
**解析：** 推荐实践：可观测性第二支柱（tracing）。事实依据：全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递。

**Qspring-1805（场景判断·tracing）** 推荐实践：可观测性第二支柱（tracing）
**答案：对。** 解析：全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递。原因：通过 HTTP header（W3C traceparent）与 MQ 属性传递，日志 MDC 打 traceId 串起单请求全部日志

**Qspring-1806（填空·tracing）** 全链路追踪：Micrometer Tracing/OpenTelemetry 生成 ______ 跨服务传递
**答案：traceId**。解析：通过 HTTP header（W3C traceparent）与 MQ 属性传递，日志 MDC 打 traceId 串起单请求全部日志

**Qspring-1807（简答·tracing）** 请说明「可观测」中traceId的机制与使用要点。
**要点（标准答案）**：① 全链路追踪：Micrometer Tracing/OpenTelemetry 生成 traceId 跨服务传递；② 原理：通过 HTTP header（W3C traceparent）与 MQ 属性传递，日志 MDC 打 traceId 串起单请求全部日志；③ 使用要点：可观测性第二支柱（tracing）。版本锚点：实战共识。

**Qspring-1808（单选·正向·多数据源）** 关于「事务」的说法，正确的是？
- A. 多数据源事务只有 JTA 一种解
- B. @Transactional 自动跨数据源
- C. 加 @Transactional 即可跨库
- D. @Transactional 不支持跨数据源（本地事务仅单连接）
**答案：D**
**解析：** @Transactional 不支持跨数据源（本地事务仅单连接）。原因：多库写需要 JTA（Atomikos）/Seata/最终一致性，最实用是业务侧拆分（各自事务+补偿）。
**来源：** SP-093 · 事务（实战共识）

**Qspring-1809（判断·多数据源）** @Transactional 不支持跨数据源（本地事务仅单连接）
**答案：对。** 解析：多库写需要 JTA（Atomikos）/Seata/最终一致性，最实用是业务侧拆分（各自事务+补偿）

**Qspring-1810（判断·多数据源）** @Transactional 自动跨数据源
**答案：错。** 正确表述：@Transactional 不支持跨数据源（本地事务仅单连接）。原因：多库写需要 JTA（Atomikos）/Seata/最终一致性，最实用是业务侧拆分（各自事务+补偿）

**Qspring-1811（判断·多数据源）** 加 @Transactional 即可跨库
**答案：错。** 正确表述：@Transactional 不支持跨数据源（本地事务仅单连接）。原因：多库写需要 JTA（Atomikos）/Seata/最终一致性，最实用是业务侧拆分（各自事务+补偿）

**Qspring-1812（判断·多数据源）** 多数据源事务只有 JTA 一种解
**答案：错。** 正确表述：@Transactional 不支持跨数据源（本地事务仅单连接）。原因：多库写需要 JTA（Atomikos）/Seata/最终一致性，最实用是业务侧拆分（各自事务+补偿）

**Qspring-1813（场景单选·多数据源）** 在工程实践中关于「不跨库」，下列做法符合推荐实践的是？
- A. @Transactional 自动跨数据源
- B. 多库写一致性选型
- C. 多数据源事务只有 JTA 一种解
- D. 加 @Transactional 即可跨库
**答案：B**
**解析：** 推荐实践：多库写一致性选型。事实依据：@Transactional 不支持跨数据源（本地事务仅单连接）。

**Qspring-1814（场景判断·多数据源）** 推荐实践：多库写一致性选型
**答案：对。** 解析：@Transactional 不支持跨数据源（本地事务仅单连接）。原因：多库写需要 JTA（Atomikos）/Seata/最终一致性，最实用是业务侧拆分（各自事务+补偿）

**Qspring-1815（简答·多数据源）** 请说明「事务」中不跨库的机制与使用要点。
**要点（标准答案）**：① @Transactional 不支持跨数据源（本地事务仅单连接）；② 原理：多库写需要 JTA（Atomikos）/Seata/最终一致性，最实用是业务侧拆分（各自事务+补偿）；③ 使用要点：多库写一致性选型。版本锚点：实战共识。

**Qspring-1816（单选·正向·连接）** 关于「事务」的说法，正确的是？
- A. afterCommit 中事务仍可回滚
- B. TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）
- C. 同步回调默认异步执行
- D. 注册回调必须手动开新事务才能写库（提交后阶段）
**答案：B**
**解析：** TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）。原因：编程式钩子：afterCommit 发 MQ、afterCompletion 清资源，与 @TransactionalEventListener 等价但更底层灵活。
**来源：** SP-094 · 事务（Spring 源码）

**Qspring-1817（判断·连接）** TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）
**答案：对。** 解析：编程式钩子：afterCommit 发 MQ、afterCompletion 清资源，与 @TransactionalEventListener 等价但更底层灵活

**Qspring-1818（判断·连接）** 同步回调默认异步执行
**答案：错。** 正确表述：TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）。原因：编程式钩子：afterCommit 发 MQ、afterCompletion 清资源，与 @TransactionalEventListener 等价但更底层灵活

**Qspring-1819（判断·连接）** afterCommit 中事务仍可回滚
**答案：错。** 正确表述：TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）。原因：编程式钩子：afterCommit 发 MQ、afterCompletion 清资源，与 @TransactionalEventListener 等价但更底层灵活

**Qspring-1820（判断·连接）** 注册回调必须手动开新事务才能写库（提交后阶段）
**答案：错。** 正确表述：TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）。原因：编程式钩子：afterCommit 发 MQ、afterCompletion 清资源，与 @TransactionalEventListener 等价但更底层灵活

**Qspring-1821（场景单选·连接）** 在工程实践中关于「TransactionSynchronization」，下列做法符合推荐实践的是？
- A. 精确控制事务生命周期
- B. 同步回调默认异步执行
- C. 注册回调必须手动开新事务才能写库（提交后阶段）
- D. afterCommit 中事务仍可回滚
**答案：A**
**解析：** 推荐实践：精确控制事务生命周期。事实依据：TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）。

**Qspring-1822（场景判断·连接）** 推荐实践：精确控制事务生命周期
**答案：对。** 解析：TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）。原因：编程式钩子：afterCommit 发 MQ、afterCompletion 清资源，与 @TransactionalEventListener 等价但更底层灵活

**Qspring-1823（填空·连接）** ______Manager 注册事务同步回调（提交前/后/回滚后）
**答案：TransactionSynchronization**。解析：编程式钩子：afterCommit 发 MQ、afterCompletion 清资源，与 @TransactionalEventListener 等价但更底层灵活

**Qspring-1824（简答·连接）** 请说明「事务」中TransactionSynchronization的机制与使用要点。
**要点（标准答案）**：① TransactionSynchronizationManager 注册事务同步回调（提交前/后/回滚后）；② 原理：编程式钩子：afterCommit 发 MQ、afterCompletion 清资源，与 @TransactionalEventListener 等价但更底层灵活；③ 使用要点：精确控制事务生命周期。版本锚点：Spring 源码。

**Qspring-1825（单选·正向·覆盖）** 关于「Bean」的说法，正确的是？
- A. Boot 默认允许覆盖
- B. 覆盖是配置便利性设计
- C. Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）
- D. 开关只对 @Bean 生效
**答案：C**
**解析：** Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）。原因：覆盖引发的隐性 Bug 难排查，显式开启（spring.main.allow-bean-definition-overriding=true）才允许，团队规范建议重名直接报错。
**来源：** SP-095 · Bean（Boot 2.1）

**Qspring-1826（判断·覆盖）** Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）
**答案：对。** 解析：覆盖引发的隐性 Bug 难排查，显式开启（spring.main.allow-bean-definition-overriding=true）才允许，团队规范建议重名直接报错

**Qspring-1827（判断·覆盖）** Boot 默认允许覆盖
**答案：错。** 正确表述：Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）。原因：覆盖引发的隐性 Bug 难排查，显式开启（spring.main.allow-bean-definition-overriding=true）才允许，团队规范建议重名直接报错

**Qspring-1828（判断·覆盖）** 覆盖是配置便利性设计
**答案：错。** 正确表述：Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）。原因：覆盖引发的隐性 Bug 难排查，显式开启（spring.main.allow-bean-definition-overriding=true）才允许，团队规范建议重名直接报错

**Qspring-1829（判断·覆盖）** 开关只对 @Bean 生效
**答案：错。** 正确表述：Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）。原因：覆盖引发的隐性 Bug 难排查，显式开启（spring.main.allow-bean-definition-overriding=true）才允许，团队规范建议重名直接报错

**Qspring-1830（场景单选·覆盖）** 在工程实践中关于「allow-bean-definition-overriding」，下列做法符合推荐实践的是？
- A. Boot 默认允许覆盖
- B. 覆盖是配置便利性设计
- C. 升级 Boot 2.1 常见启动报错
- D. 开关只对 @Bean 生效
**答案：C**
**解析：** 推荐实践：升级 Boot 2.1 常见启动报错。事实依据：Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）。

**Qspring-1831（场景判断·覆盖）** 推荐实践：升级 Boot 2.1 常见启动报错
**答案：对。** 解析：Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）。原因：覆盖引发的隐性 Bug 难排查，显式开启（spring.main.allow-bean-definition-overriding=true）才允许，团队规范建议重名直接报错

**Qspring-1832（简答·覆盖）** 请说明「Bean」中allow-bean-definition-overriding的机制与使用要点。
**要点（标准答案）**：① Boot 2.1 起默认禁止 Bean 覆盖（重名即启动失败）；② 原理：覆盖引发的隐性 Bug 难排查，显式开启（spring.main.allow-bean-definition-overriding=true）才允许，团队规范建议重名直接报错；③ 使用要点：升级 Boot 2.1 常见启动报错。版本锚点：Boot 2.1。

**Qspring-1833（单选·正向·顺序）** 关于「IoC」的说法，正确的是？
- A. @Order 保证 Bean 完全初始化顺序
- B. @Order 只对 @Bean 方法生效
- C. @Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）
- D. @Order 数字大先执行
**答案：C**
**解析：** @Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）。原因：依赖关系应靠 @DependsOn 或显式注入表达而非顺序猜测，@Order 是提示不是保证。
**来源：** SP-096 · IoC（Spring 文档）

**Qspring-1834（判断·顺序）** @Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）
**答案：对。** 解析：依赖关系应靠 @DependsOn 或显式注入表达而非顺序猜测，@Order 是提示不是保证

**Qspring-1835（判断·顺序）** @Order 保证 Bean 完全初始化顺序
**答案：错。** 正确表述：@Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）。原因：依赖关系应靠 @DependsOn 或显式注入表达而非顺序猜测，@Order 是提示不是保证

**Qspring-1836（判断·顺序）** @Order 数字大先执行
**答案：错。** 正确表述：@Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）。原因：依赖关系应靠 @DependsOn 或显式注入表达而非顺序猜测，@Order 是提示不是保证

**Qspring-1837（判断·顺序）** @Order 只对 @Bean 方法生效
**答案：错。** 正确表述：@Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）。原因：依赖关系应靠 @DependsOn 或显式注入表达而非顺序猜测，@Order 是提示不是保证

**Qspring-1838（场景单选·顺序）** 在工程实践中关于「@Order 注入」，下列做法符合推荐实践的是？
- A. 顺序敏感场景用 @DependsOn 显式声明
- B. @Order 保证 Bean 完全初始化顺序
- C. @Order 只对 @Bean 方法生效
- D. @Order 数字大先执行
**答案：A**
**解析：** 推荐实践：顺序敏感场景用 @DependsOn 显式声明。事实依据：@Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）。

**Qspring-1839（场景判断·顺序）** 推荐实践：顺序敏感场景用 @DependsOn 显式声明
**答案：对。** 解析：@Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）。原因：依赖关系应靠 @DependsOn 或显式注入表达而非顺序猜测，@Order 是提示不是保证

**Qspring-1840（简答·顺序）** 请说明「IoC」中@Order 注入的机制与使用要点。
**要点（标准答案）**：① @Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）；② 原理：依赖关系应靠 @DependsOn 或显式注入表达而非顺序猜测，@Order 是提示不是保证；③ 使用要点：顺序敏感场景用 @DependsOn 显式声明。版本锚点：Spring 文档。

**Qspring-1841（单选·正向·顺序）** 关于「IoC」的说法，正确的是？
- A. @DependsOn 显式声明初始化依赖顺序
- B. 不需要它 Spring 会自动分析依赖
- C. 它只影响注入不影响初始化
- D. @DependsOn 与 @Order 等价
**答案：A**
**解析：** @DependsOn 显式声明初始化依赖顺序。原因：初始化缓存 Bean 与使用 Bean 的关系、静态资源准备，比 @Order 强（保证创建完成顺序）。
**来源：** SP-097 · IoC（Spring 文档）

**Qspring-1842（判断·顺序）** @DependsOn 显式声明初始化依赖顺序
**答案：对。** 解析：初始化缓存 Bean 与使用 Bean 的关系、静态资源准备，比 @Order 强（保证创建完成顺序）

**Qspring-1843（判断·顺序）** @DependsOn 与 @Order 等价
**答案：错。** 正确表述：@DependsOn 显式声明初始化依赖顺序。原因：初始化缓存 Bean 与使用 Bean 的关系、静态资源准备，比 @Order 强（保证创建完成顺序）

**Qspring-1844（判断·顺序）** 它只影响注入不影响初始化
**答案：错。** 正确表述：@DependsOn 显式声明初始化依赖顺序。原因：初始化缓存 Bean 与使用 Bean 的关系、静态资源准备，比 @Order 强（保证创建完成顺序）

**Qspring-1845（判断·顺序）** 不需要它 Spring 会自动分析依赖
**答案：错。** 正确表述：@DependsOn 显式声明初始化依赖顺序。原因：初始化缓存 Bean 与使用 Bean 的关系、静态资源准备，比 @Order 强（保证创建完成顺序）

**Qspring-1846（场景单选·顺序）** 在工程实践中关于「@DependsOn」，下列做法符合推荐实践的是？
- A. @DependsOn 与 @Order 等价
- B. 显式依赖的标准工具
- C. 它只影响注入不影响初始化
- D. 不需要它 Spring 会自动分析依赖
**答案：B**
**解析：** 推荐实践：显式依赖的标准工具。事实依据：@DependsOn 显式声明初始化依赖顺序。

**Qspring-1847（场景判断·顺序）** 推荐实践：显式依赖的标准工具
**答案：对。** 解析：@DependsOn 显式声明初始化依赖顺序。原因：初始化缓存 Bean 与使用 Bean 的关系、静态资源准备，比 @Order 强（保证创建完成顺序）

**Qspring-1848（填空·顺序）** ______ 显式声明初始化依赖顺序
**答案：@DependsOn**。解析：初始化缓存 Bean 与使用 Bean 的关系、静态资源准备，比 @Order 强（保证创建完成顺序）

**Qspring-1849（简答·顺序）** 请说明「IoC」中@DependsOn的机制与使用要点。
**要点（标准答案）**：① @DependsOn 显式声明初始化依赖顺序；② 原理：初始化缓存 Bean 与使用 Bean 的关系、静态资源准备，比 @Order 强（保证创建完成顺序）；③ 使用要点：显式依赖的标准工具。版本锚点：Spring 文档。

**Qspring-1850（单选·正向·关闭）** 关于「容器」的说法，正确的是？
- A. Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器
- B. SIGTERM 会被忽略直接杀
- C. 优雅停机与 K8s 探针无关
- D. 默认就是优雅停机
**答案：A**
**解析：** Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。原因：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep。
**来源：** SP-098 · 容器（Boot 2.3）

**Qspring-1851（判断·关闭）** Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器
**答案：对。** 解析：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep

**Qspring-1852（判断·关闭）** 默认就是优雅停机
**答案：错。** 正确表述：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。原因：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep

**Qspring-1853（判断·关闭）** SIGTERM 会被忽略直接杀
**答案：错。** 正确表述：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。原因：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep

**Qspring-1854（判断·关闭）** 优雅停机与 K8s 探针无关
**答案：错。** 正确表述：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。原因：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep

**Qspring-1855（场景单选·关闭）** 在工程实践中关于「优雅停机」，下列做法符合推荐实践的是？
- A. 默认就是优雅停机
- B. 发布零中断的基础配置
- C. SIGTERM 会被忽略直接杀
- D. 优雅停机与 K8s 探针无关
**答案：B**
**解析：** 推荐实践：发布零中断的基础配置。事实依据：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。

**Qspring-1856（场景判断·关闭）** 推荐实践：发布零中断的基础配置
**答案：对。** 解析：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。原因：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep

**Qspring-1857（填空·关闭）** Boot 2.3+ ______：server.shutdown=graceful 等待请求完成再关容器
**答案：优雅停机**。解析：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep

**Qspring-1858（简答·关闭）** 请说明「容器」中优雅停机的机制与使用要点。
**要点（标准答案）**：① Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器；② 原理：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep；③ 使用要点：发布零中断的基础配置。版本锚点：Boot 2.3。

**Qspring-1859（单选·正向·运维）** 关于「Boot」的说法，正确的是？
- A. 默认参数就是最优
- B. acceptCount 是最大并发数
- C. Web 容器关键参数：Tomcat maxThreads(默认 200)/acceptCount/maxConnections 按压测定
- D. Tomcat 线程数越大吞吐越高
**答案：C**
**解析：** Web 容器关键参数：Tomcat maxThreads(默认 200)/acceptCount/maxConnections 按压测定。原因：默认 200 线程 + 8192 accept 队列未必适配业务，慢接口占满线程池是雪崩起点，配合超时与舱壁隔离。
**来源：** SP-099 · Boot（Boot 文档）

**Qspring-1860（判断·运维）** Web 容器关键参数：Tomcat maxThreads(默认 200)/acceptCount/maxConnections 按压测定
**答案：对。** 解析：默认 200 线程 + 8192 accept 队列未必适配业务，慢接口占满线程池是雪崩起点，配合超时与舱壁隔离

**Qspring-1861（判断·运维）** Tomcat 线程数越大吞吐越高
**答案：错。** 正确表述：Web 容器关键参数：Tomcat maxThreads(默认 200)/acceptCount/maxConnections 按压测定。原因：默认 200 线程 + 8192 accept 队列未必适配业务，慢接口占满线程池是雪崩起点，配合超时与舱壁隔离

**Qspring-1862（判断·运维）** 默认参数就是最优
**答案：错。** 正确表述：Web 容器关键参数：Tomcat maxThreads(默认 200)/acceptCount/maxConnections 按压测定。原因：默认 200 线程 + 8192 accept 队列未必适配业务，慢接口占满线程池是雪崩起点，配合超时与舱壁隔离

**Qspring-1863（判断·运维）** acceptCount 是最大并发数
**答案：错。** 正确表述：Web 容器关键参数：Tomcat maxThreads(默认 200)/acceptCount/maxConnections 按压测定。原因：默认 200 线程 + 8192 accept 队列未必适配业务，慢接口占满线程池是雪崩起点，配合超时与舱壁隔离

**Qspring-1864（场景单选·运维）** 在工程实践中关于「压测参数」，下列做法符合推荐实践的是？
- A. 默认参数就是最优
- B. Tomcat 线程数越大吞吐越高
- C. acceptCount 是最大并发数
- D. 容量规划与雪崩防护
**答案：D**
**解析：** 推荐实践：容量规划与雪崩防护。事实依据：Web 容器关键参数：Tomcat maxThreads(默认 200)/acceptCount/maxConnections 按压测定。

**Qspring-1865（场景判断·运维）** 推荐实践：容量规划与雪崩防护
**答案：对。** 解析：Web 容器关键参数：Tomcat maxThreads(默认 200)/acceptCount/maxConnections 按压测定。原因：默认 200 线程 + 8192 accept 队列未必适配业务，慢接口占满线程池是雪崩起点，配合超时与舱壁隔离

**Qspring-1866（简答·运维）** 请说明「Boot」中压测参数的机制与使用要点。
**要点（标准答案）**：① Web 容器关键参数：Tomcat maxThreads(默认 200)/acceptCount/maxConnections 按压测定；② 原理：默认 200 线程 + 8192 accept 队列未必适配业务，慢接口占满线程池是雪崩起点，配合超时与舱壁隔离；③ 使用要点：容量规划与雪崩防护。版本锚点：Boot 文档。

**Qspring-1867（单选·正向·历史）** 关于「演进」的说法，正确的是？
- A. Boot 放弃了 XML（其实支持）
- B. Spring 演进：XML 配置→注解+JavaConfig→Spring Boot 自动配置→云原生
- C. 演进只是语法变化
- D. XML 配置当前仍是主流
**答案：B**
**解析：** Spring 演进：XML 配置→注解+JavaConfig→Spring Boot 自动配置→云原生。原因：每个阶段解决上一阶段的配置复杂度，理解演进脉络才能回答"为什么 Spring Boot 能流行"。
**来源：** SP-100 · 演进（历史共识）

**Qspring-1868（判断·历史）** Spring 演进：XML 配置→注解+JavaConfig→Spring Boot 自动配置→云原生
**答案：对。** 解析：每个阶段解决上一阶段的配置复杂度，理解演进脉络才能回答"为什么 Spring Boot 能流行"

**Qspring-1869（判断·历史）** XML 配置当前仍是主流
**答案：错。** 正确表述：Spring 演进：XML 配置→注解+JavaConfig→Spring Boot 自动配置→云原生。原因：每个阶段解决上一阶段的配置复杂度，理解演进脉络才能回答"为什么 Spring Boot 能流行"

**Qspring-1870（判断·历史）** Boot 放弃了 XML（其实支持）
**答案：错。** 正确表述：Spring 演进：XML 配置→注解+JavaConfig→Spring Boot 自动配置→云原生。原因：每个阶段解决上一阶段的配置复杂度，理解演进脉络才能回答"为什么 Spring Boot 能流行"

**Qspring-1871（判断·历史）** 演进只是语法变化
**答案：错。** 正确表述：Spring 演进：XML 配置→注解+JavaConfig→Spring Boot 自动配置→云原生。原因：每个阶段解决上一阶段的配置复杂度，理解演进脉络才能回答"为什么 Spring Boot 能流行"

**Qspring-1872（场景单选·历史）** 在工程实践中关于「XML→注解→Boot」，下列做法符合推荐实践的是？
- A. XML 配置当前仍是主流
- B. 演进只是语法变化
- C. Boot 放弃了 XML（其实支持）
- D. 体系化回答 Spring 是什么
**答案：D**
**解析：** 推荐实践：体系化回答 Spring 是什么。事实依据：Spring 演进：XML 配置→注解+JavaConfig→Spring Boot 自动配置→云原生。

**Qspring-1873（场景判断·历史）** 推荐实践：体系化回答 Spring 是什么
**答案：对。** 解析：Spring 演进：XML 配置→注解+JavaConfig→Spring Boot 自动配置→云原生。原因：每个阶段解决上一阶段的配置复杂度，理解演进脉络才能回答"为什么 Spring Boot 能流行"

**Qspring-1874（简答·历史）** 请说明「演进」中XML→注解→Boot的机制与使用要点。
**要点（标准答案）**：① Spring 演进：XML 配置→注解+JavaConfig→Spring Boot 自动配置→云原生；② 原理：每个阶段解决上一阶段的配置复杂度，理解演进脉络才能回答"为什么 Spring Boot 能流行"；③ 使用要点：体系化回答 Spring 是什么。版本锚点：历史共识。

**Qspring-1875（单选·正向·场景）** 关于「AOP」的说法，正确的是？
- A. 幂等注解必须配合事务
- B. 幂等靠数据库唯一键就够（也是方案之一但接口层先行）
- C. 幂等注解切面：@Idempotent + Redis setnx + 拦截器/AOP
- D. Redis 幂等绝对可靠（宕机窗口需 DB 兜底）
**答案：C**
**解析：** 幂等注解切面：@Idempotent + Redis setnx + 拦截器/AOP。原因：请求携带唯一键（token/参数 hash），切面前置检查已处理则拒绝，TTL 覆盖业务最长处理时间。
**来源：** SP-101 · AOP（实战共识）

**Qspring-1876（判断·场景）** 幂等注解切面：@Idempotent + Redis setnx + 拦截器/AOP
**答案：对。** 解析：请求携带唯一键（token/参数 hash），切面前置检查已处理则拒绝，TTL 覆盖业务最长处理时间

**Qspring-1877（判断·场景）** 幂等靠数据库唯一键就够（也是方案之一但接口层先行）
**答案：错。** 正确表述：幂等注解切面：@Idempotent + Redis setnx + 拦截器/AOP。原因：请求携带唯一键（token/参数 hash），切面前置检查已处理则拒绝，TTL 覆盖业务最长处理时间

**Qspring-1878（判断·场景）** 幂等注解必须配合事务
**答案：错。** 正确表述：幂等注解切面：@Idempotent + Redis setnx + 拦截器/AOP。原因：请求携带唯一键（token/参数 hash），切面前置检查已处理则拒绝，TTL 覆盖业务最长处理时间

**Qspring-1879（判断·场景）** Redis 幂等绝对可靠（宕机窗口需 DB 兜底）
**答案：错。** 正确表述：幂等注解切面：@Idempotent + Redis setnx + 拦截器/AOP。原因：请求携带唯一键（token/参数 hash），切面前置检查已处理则拒绝，TTL 覆盖业务最长处理时间

**Qspring-1880（场景单选·场景）** 在工程实践中关于「幂等」，下列做法符合推荐实践的是？
- A. 防重提交的通用架构
- B. Redis 幂等绝对可靠（宕机窗口需 DB 兜底）
- C. 幂等靠数据库唯一键就够（也是方案之一但接口层先行）
- D. 幂等注解必须配合事务
**答案：A**
**解析：** 推荐实践：防重提交的通用架构。事实依据：幂等注解切面：@Idempotent + Redis setnx + 拦截器/AOP。

**Qspring-1881（场景判断·场景）** 推荐实践：防重提交的通用架构
**答案：对。** 解析：幂等注解切面：@Idempotent + Redis setnx + 拦截器/AOP。原因：请求携带唯一键（token/参数 hash），切面前置检查已处理则拒绝，TTL 覆盖业务最长处理时间

**Qspring-1882（填空·场景）** ______注解切面：@Idempotent + Redis setnx + 拦截器/AOP
**答案：幂等**。解析：请求携带唯一键（token/参数 hash），切面前置检查已处理则拒绝，TTL 覆盖业务最长处理时间

**Qspring-1883（简答·场景）** 请说明「AOP」中幂等的机制与使用要点。
**要点（标准答案）**：① 幂等注解切面：@Idempotent + Redis setnx + 拦截器/AOP；② 原理：请求携带唯一键（token/参数 hash），切面前置检查已处理则拒绝，TTL 覆盖业务最长处理时间；③ 使用要点：防重提交的通用架构。版本锚点：实战共识。

**Qspring-1884（单选·正向·场景）** 关于「AOP」的说法，正确的是？
- A. 应用层限流可以替代网关限流
- B. 注解限流性能开销巨大
- C. 限流切面：Sentinel/@RateLimiter 注解 + 切面读取阈值
- D. 限流是单机概念无集群版
**答案：C**
**解析：** 限流切面：Sentinel/@RateLimiter 注解 + 切面读取阈值。原因：接口级限流注解化，底层令牌桶/滑动窗口，超限快速失败或降级，与网关层限流分层（网关粗粒度、应用细粒度）。
**来源：** SP-102 · AOP（实战共识）

**Qspring-1885（判断·场景）** 限流切面：Sentinel/@RateLimiter 注解 + 切面读取阈值
**答案：对。** 解析：接口级限流注解化，底层令牌桶/滑动窗口，超限快速失败或降级，与网关层限流分层（网关粗粒度、应用细粒度）

**Qspring-1886（判断·场景）** 应用层限流可以替代网关限流
**答案：错。** 正确表述：限流切面：Sentinel/@RateLimiter 注解 + 切面读取阈值。原因：接口级限流注解化，底层令牌桶/滑动窗口，超限快速失败或降级，与网关层限流分层（网关粗粒度、应用细粒度）

**Qspring-1887（判断·场景）** 限流是单机概念无集群版
**答案：错。** 正确表述：限流切面：Sentinel/@RateLimiter 注解 + 切面读取阈值。原因：接口级限流注解化，底层令牌桶/滑动窗口，超限快速失败或降级，与网关层限流分层（网关粗粒度、应用细粒度）

**Qspring-1888（判断·场景）** 注解限流性能开销巨大
**答案：错。** 正确表述：限流切面：Sentinel/@RateLimiter 注解 + 切面读取阈值。原因：接口级限流注解化，底层令牌桶/滑动窗口，超限快速失败或降级，与网关层限流分层（网关粗粒度、应用细粒度）

**Qspring-1889（场景单选·场景）** 在工程实践中关于「限流」，下列做法符合推荐实践的是？
- A. 接口 QPS 治理
- B. 限流是单机概念无集群版
- C. 应用层限流可以替代网关限流
- D. 注解限流性能开销巨大
**答案：A**
**解析：** 推荐实践：接口 QPS 治理。事实依据：限流切面：Sentinel/@RateLimiter 注解 + 切面读取阈值。

**Qspring-1890（场景判断·场景）** 推荐实践：接口 QPS 治理
**答案：对。** 解析：限流切面：Sentinel/@RateLimiter 注解 + 切面读取阈值。原因：接口级限流注解化，底层令牌桶/滑动窗口，超限快速失败或降级，与网关层限流分层（网关粗粒度、应用细粒度）

**Qspring-1891（填空·场景）** ______切面：Sentinel/@RateLimiter 注解 + 切面读取阈值
**答案：限流**。解析：接口级限流注解化，底层令牌桶/滑动窗口，超限快速失败或降级，与网关层限流分层（网关粗粒度、应用细粒度）

**Qspring-1892（简答·场景）** 请说明「AOP」中限流的机制与使用要点。
**要点（标准答案）**：① 限流切面：Sentinel/@RateLimiter 注解 + 切面读取阈值；② 原理：接口级限流注解化，底层令牌桶/滑动窗口，超限快速失败或降级，与网关层限流分层（网关粗粒度、应用细粒度）；③ 使用要点：接口 QPS 治理。版本锚点：实战共识。

**Qspring-1893（单选·正向·日志）** 关于「Boot」的说法，正确的是？
- A. Boot 默认 logback 按 spring.profile 加载 logback-spring.xml
- B. 日志不需要滚动配置
- C. 异步日志会丢日志
- D. Boot 默认 log4j
**答案：A**
**解析：** Boot 默认 logback 按 spring.profile 加载 logback-spring.xml。原因：生产配置滚动策略（按天+大小）、异步 Appender（AsyncAppender 防日志 IO 拖慢业务）、traceId 进 pattern。
**来源：** SP-103 · Boot（Boot 文档）

**Qspring-1894（判断·日志）** Boot 默认 logback 按 spring.profile 加载 logback-spring.xml
**答案：对。** 解析：生产配置滚动策略（按天+大小）、异步 Appender（AsyncAppender 防日志 IO 拖慢业务）、traceId 进 pattern

**Qspring-1895（判断·日志）** Boot 默认 log4j
**答案：错。** 正确表述：Boot 默认 logback 按 spring.profile 加载 logback-spring.xml。原因：生产配置滚动策略（按天+大小）、异步 Appender（AsyncAppender 防日志 IO 拖慢业务）、traceId 进 pattern

**Qspring-1896（判断·日志）** 异步日志会丢日志
**答案：错。** 正确表述：Boot 默认 logback 按 spring.profile 加载 logback-spring.xml。原因：生产配置滚动策略（按天+大小）、异步 Appender（AsyncAppender 防日志 IO 拖慢业务）、traceId 进 pattern

**Qspring-1897（判断·日志）** 日志不需要滚动配置
**答案：错。** 正确表述：Boot 默认 logback 按 spring.profile 加载 logback-spring.xml。原因：生产配置滚动策略（按天+大小）、异步 Appender（AsyncAppender 防日志 IO 拖慢业务）、traceId 进 pattern

**Qspring-1898（场景单选·日志）** 在工程实践中关于「logback」，下列做法符合推荐实践的是？
- A. 日志规范落地
- B. 日志不需要滚动配置
- C. 异步日志会丢日志
- D. Boot 默认 log4j
**答案：A**
**解析：** 推荐实践：日志规范落地。事实依据：Boot 默认 logback 按 spring.profile 加载 logback-spring.xml。

**Qspring-1899（场景判断·日志）** 推荐实践：日志规范落地
**答案：对。** 解析：Boot 默认 logback 按 spring.profile 加载 logback-spring.xml。原因：生产配置滚动策略（按天+大小）、异步 Appender（AsyncAppender 防日志 IO 拖慢业务）、traceId 进 pattern

**Qspring-1900（填空·日志）** Boot 默认 ______ 按 spring.profile 加载 logback-spring.xml
**答案：logback**。解析：生产配置滚动策略（按天+大小）、异步 Appender（AsyncAppender 防日志 IO 拖慢业务）、traceId 进 pattern

**Qspring-1901（简答·日志）** 请说明「Boot」中logback的机制与使用要点。
**要点（标准答案）**：① Boot 默认 logback 按 spring.profile 加载 logback-spring.xml；② 原理：生产配置滚动策略（按天+大小）、异步 Appender（AsyncAppender 防日志 IO 拖慢业务）、traceId 进 pattern；③ 使用要点：日志规范落地。版本锚点：Boot 文档。

**Qspring-1902（单选·正向·日志）** 关于「Boot」的说法，正确的是？
- A. 日志异步化用 AsyncAppender 或 Log4j2 async logger（Disruptor）
- B. logback 性能永远最优
- C. 同步日志不影响 RT
- D. 异步日志没有任何代价
**答案：A**
**解析：** 日志异步化用 AsyncAppender 或 Log4j2 async logger（Disruptor）。原因：同步日志在高并发下成为 IO 瓶颈（RT 上升），Log4j2 异步 logger 性能最优，丢弃策略按业务容忍度配置。
**来源：** SP-104 · Boot（实战共识）

**Qspring-1903（判断·日志）** 日志异步化用 AsyncAppender 或 Log4j2 async logger（Disruptor）
**答案：对。** 解析：同步日志在高并发下成为 IO 瓶颈（RT 上升），Log4j2 异步 logger 性能最优，丢弃策略按业务容忍度配置

**Qspring-1904（判断·日志）** 异步日志没有任何代价
**答案：错。** 正确表述：日志异步化用 AsyncAppender 或 Log4j2 async logger（Disruptor）。原因：同步日志在高并发下成为 IO 瓶颈（RT 上升），Log4j2 异步 logger 性能最优，丢弃策略按业务容忍度配置

**Qspring-1905（判断·日志）** logback 性能永远最优
**答案：错。** 正确表述：日志异步化用 AsyncAppender 或 Log4j2 async logger（Disruptor）。原因：同步日志在高并发下成为 IO 瓶颈（RT 上升），Log4j2 异步 logger 性能最优，丢弃策略按业务容忍度配置

**Qspring-1906（判断·日志）** 同步日志不影响 RT
**答案：错。** 正确表述：日志异步化用 AsyncAppender 或 Log4j2 async logger（Disruptor）。原因：同步日志在高并发下成为 IO 瓶颈（RT 上升），Log4j2 异步 logger 性能最优，丢弃策略按业务容忍度配置

**Qspring-1907（场景单选·日志）** 在工程实践中关于「异步」，下列做法符合推荐实践的是？
- A. logback 性能永远最优
- B. 异步日志没有任何代价
- C. 同步日志不影响 RT
- D. 高并发服务日志基线配置
**答案：D**
**解析：** 推荐实践：高并发服务日志基线配置。事实依据：日志异步化用 AsyncAppender 或 Log4j2 async logger（Disruptor）。

**Qspring-1908（场景判断·日志）** 推荐实践：高并发服务日志基线配置
**答案：对。** 解析：日志异步化用 AsyncAppender 或 Log4j2 async logger（Disruptor）。原因：同步日志在高并发下成为 IO 瓶颈（RT 上升），Log4j2 异步 logger 性能最优，丢弃策略按业务容忍度配置

**Qspring-1909（填空·日志）** 日志______化用 AsyncAppender 或 Log4j2 async logger（Disruptor）
**答案：异步**。解析：同步日志在高并发下成为 IO 瓶颈（RT 上升），Log4j2 异步 logger 性能最优，丢弃策略按业务容忍度配置

**Qspring-1910（简答·日志）** 请说明「Boot」中异步的机制与使用要点。
**要点（标准答案）**：① 日志异步化用 AsyncAppender 或 Log4j2 async logger（Disruptor）；② 原理：同步日志在高并发下成为 IO 瓶颈（RT 上升），Log4j2 异步 logger 性能最优，丢弃策略按业务容忍度配置；③ 使用要点：高并发服务日志基线配置。版本锚点：实战共识。

**Qspring-1911（单选·正向·面试）** 关于「IoC」的说法，正确的是？
- A. 源码细节面试不问
- B. 事务与 AOP 是两个独立体系
- C. Spring 高频面试主线：Bean 生命周期→三级缓存→AOP 代理时机→事务传播→自动配置
- D. 面试只考注解用法
**答案：C**
**解析：** Spring 高频面试主线：Bean 生命周期→三级缓存→AOP 代理时机→事务传播→自动配置。原因：这条链覆盖 80% Spring 面试题，每环都有源码级细节（本项目已逐环核对源码与文档）。
**来源：** SP-105 · IoC（复习方法论）

**Qspring-1912（判断·面试）** Spring 高频面试主线：Bean 生命周期→三级缓存→AOP 代理时机→事务传播→自动配置
**答案：对。** 解析：这条链覆盖 80% Spring 面试题，每环都有源码级细节（本项目已逐环核对源码与文档）

**Qspring-1913（判断·面试）** 面试只考注解用法
**答案：错。** 正确表述：Spring 高频面试主线：Bean 生命周期→三级缓存→AOP 代理时机→事务传播→自动配置。原因：这条链覆盖 80% Spring 面试题，每环都有源码级细节（本项目已逐环核对源码与文档）

**Qspring-1914（判断·面试）** 源码细节面试不问
**答案：错。** 正确表述：Spring 高频面试主线：Bean 生命周期→三级缓存→AOP 代理时机→事务传播→自动配置。原因：这条链覆盖 80% Spring 面试题，每环都有源码级细节（本项目已逐环核对源码与文档）

**Qspring-1915（判断·面试）** 事务与 AOP 是两个独立体系
**答案：错。** 正确表述：Spring 高频面试主线：Bean 生命周期→三级缓存→AOP 代理时机→事务传播→自动配置。原因：这条链覆盖 80% Spring 面试题，每环都有源码级细节（本项目已逐环核对源码与文档）

**Qspring-1916（场景单选·面试）** 在工程实践中关于「综合」，下列做法符合推荐实践的是？
- A. 面试只考注解用法
- B. 复习主线图
- C. 源码细节面试不问
- D. 事务与 AOP 是两个独立体系
**答案：B**
**解析：** 推荐实践：复习主线图。事实依据：Spring 高频面试主线：Bean 生命周期→三级缓存→AOP 代理时机→事务传播→自动配置。

**Qspring-1917（场景判断·面试）** 推荐实践：复习主线图
**答案：对。** 解析：Spring 高频面试主线：Bean 生命周期→三级缓存→AOP 代理时机→事务传播→自动配置。原因：这条链覆盖 80% Spring 面试题，每环都有源码级细节（本项目已逐环核对源码与文档）

**Qspring-1918（简答·面试）** 请说明「IoC」中综合的机制与使用要点。
**要点（标准答案）**：① Spring 高频面试主线：Bean 生命周期→三级缓存→AOP 代理时机→事务传播→自动配置；② 原理：这条链覆盖 80% Spring 面试题，每环都有源码级细节（本项目已逐环核对源码与文档）；③ 使用要点：复习主线图。版本锚点：复习方法论。

**Qspring-1919（单选·正向·升级）** 关于「Boot」的说法，正确的是？
- A. 升级路线：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级
- B. jakarta 迁移工具自动完成
- C. 升级只改父版本号
- D. 可直接从 1.5 跳 3.0
**答案：A**
**解析：** 升级路线：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级。原因：2.x 尾版 2.7 是迁移缓冲，先升 2.7 修废弃 API 再跨 3.0，spring-boot-properties-migrator 自动提示配置变更。
**来源：** SP-106 · Boot（Boot 官方迁移指南）

**Qspring-1920（判断·升级）** 升级路线：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级
**答案：对。** 解析：2.x 尾版 2.7 是迁移缓冲，先升 2.7 修废弃 API 再跨 3.0，spring-boot-properties-migrator 自动提示配置变更

**Qspring-1921（判断·升级）** 可直接从 1.5 跳 3.0
**答案：错。** 正确表述：升级路线：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级。原因：2.x 尾版 2.7 是迁移缓冲，先升 2.7 修废弃 API 再跨 3.0，spring-boot-properties-migrator 自动提示配置变更

**Qspring-1922（判断·升级）** 升级只改父版本号
**答案：错。** 正确表述：升级路线：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级。原因：2.x 尾版 2.7 是迁移缓冲，先升 2.7 修废弃 API 再跨 3.0，spring-boot-properties-migrator 自动提示配置变更

**Qspring-1923（判断·升级）** jakarta 迁移工具自动完成
**答案：错。** 正确表述：升级路线：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级。原因：2.x 尾版 2.7 是迁移缓冲，先升 2.7 修废弃 API 再跨 3.0，spring-boot-properties-migrator 自动提示配置变更

**Qspring-1924（场景单选·升级）** 在工程实践中关于「路线」，下列做法符合推荐实践的是？
- A. 可直接从 1.5 跳 3.0
- B. jakarta 迁移工具自动完成
- C. 升级只改父版本号
- D. 老系统升级路线图
**答案：D**
**解析：** 推荐实践：老系统升级路线图。事实依据：升级路线：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级。

**Qspring-1925（场景判断·升级）** 推荐实践：老系统升级路线图
**答案：对。** 解析：升级路线：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级。原因：2.x 尾版 2.7 是迁移缓冲，先升 2.7 修废弃 API 再跨 3.0，spring-boot-properties-migrator 自动提示配置变更

**Qspring-1926（填空·升级）** 升级______：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级
**答案：路线**。解析：2.x 尾版 2.7 是迁移缓冲，先升 2.7 修废弃 API 再跨 3.0，spring-boot-properties-migrator 自动提示配置变更

**Qspring-1927（简答·升级）** 请说明「Boot」中路线的机制与使用要点。
**要点（标准答案）**：① 升级路线：Boot 1.5（EOL）→2.7（过渡）→3.x（JDK17/jakarta），依赖版本同步升级；② 原理：2.x 尾版 2.7 是迁移缓冲，先升 2.7 修废弃 API 再跨 3.0，spring-boot-properties-migrator 自动提示配置变更；③ 使用要点：老系统升级路线图。版本锚点：Boot 官方迁移指南。

**Qspring-1928（单选·正向·坑）** 关于「IoC」的说法，正确的是？
- A. 依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）
- B. Maven 自动选最优版本无冲突
- C. 冲突报错都发生在启动时
- D. exclude 不是标准解法
**答案：A**
**解析：** 依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）。原因：同一库多版本导致 NoSuchMethodError/ClassNotFoundException，用 dependencyManagement 统一版本、BOM 管理第三方（如 spring-cloud-bom）。
**来源：** SP-107 · IoC（实战共识）

**Qspring-1929（判断·坑）** 依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）
**答案：对。** 解析：同一库多版本导致 NoSuchMethodError/ClassNotFoundException，用 dependencyManagement 统一版本、BOM 管理第三方（如 spring-cloud-bom）

**Qspring-1930（判断·坑）** Maven 自动选最优版本无冲突
**答案：错。** 正确表述：依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）。原因：同一库多版本导致 NoSuchMethodError/ClassNotFoundException，用 dependencyManagement 统一版本、BOM 管理第三方（如 spring-cloud-bom）

**Qspring-1931（判断·坑）** 冲突报错都发生在启动时
**答案：错。** 正确表述：依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）。原因：同一库多版本导致 NoSuchMethodError/ClassNotFoundException，用 dependencyManagement 统一版本、BOM 管理第三方（如 spring-cloud-bom）

**Qspring-1932（判断·坑）** exclude 不是标准解法
**答案：错。** 正确表述：依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）。原因：同一库多版本导致 NoSuchMethodError/ClassNotFoundException，用 dependencyManagement 统一版本、BOM 管理第三方（如 spring-cloud-bom）

**Qspring-1933（场景单选·坑）** 在工程实践中关于「jar 冲突」，下列做法符合推荐实践的是？
- A. 冲突报错都发生在启动时
- B. exclude 不是标准解法
- C. Maven 自动选最优版本无冲突
- D. 依赖治理是 Boot 工程师基本功
**答案：D**
**解析：** 推荐实践：依赖治理是 Boot 工程师基本功。事实依据：依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）。

**Qspring-1934（场景判断·坑）** 推荐实践：依赖治理是 Boot 工程师基本功
**答案：对。** 解析：依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）。原因：同一库多版本导致 NoSuchMethodError/ClassNotFoundException，用 dependencyManagement 统一版本、BOM 管理第三方（如 spring-cloud-bom）

**Qspring-1935（简答·坑）** 请说明「IoC」中jar 冲突的机制与使用要点。
**要点（标准答案）**：① 依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）；② 原理：同一库多版本导致 NoSuchMethodError/ClassNotFoundException，用 dependencyManagement 统一版本、BOM 管理第三方（如 spring-cloud-bom）；③ 使用要点：依赖治理是 Boot 工程师基本功。版本锚点：实战共识。

**Qspring-1936（单选·正向·契约）** 关于「测试」的说法，正确的是？
- A. H2 完全替代 MySQL 测试
- B. 测试配置隔离：test profile 独立数据源（H2/Testcontainers）与 Mock 外部依赖
- C. 外部依赖必须全部 Mock
- D. 测试环境用生产数据
**答案：B**
**解析：** 测试配置隔离：test profile 独立数据源（H2/Testcontainers）与 Mock 外部依赖。原因：Testcontainers 起真实 MySQL/Redis 容器比 H2 更真实（方言差异），CI 与本地一致。
**来源：** SP-108 · 测试（实战共识）

**Qspring-1937（判断·契约）** 测试配置隔离：test profile 独立数据源（H2/Testcontainers）与 Mock 外部依赖
**答案：对。** 解析：Testcontainers 起真实 MySQL/Redis 容器比 H2 更真实（方言差异），CI 与本地一致

**Qspring-1938（判断·契约）** H2 完全替代 MySQL 测试
**答案：错。** 正确表述：测试配置隔离：test profile 独立数据源（H2/Testcontainers）与 Mock 外部依赖。原因：Testcontainers 起真实 MySQL/Redis 容器比 H2 更真实（方言差异），CI 与本地一致

**Qspring-1939（判断·契约）** 外部依赖必须全部 Mock
**答案：错。** 正确表述：测试配置隔离：test profile 独立数据源（H2/Testcontainers）与 Mock 外部依赖。原因：Testcontainers 起真实 MySQL/Redis 容器比 H2 更真实（方言差异），CI 与本地一致

**Qspring-1940（判断·契约）** 测试环境用生产数据
**答案：错。** 正确表述：测试配置隔离：test profile 独立数据源（H2/Testcontainers）与 Mock 外部依赖。原因：Testcontainers 起真实 MySQL/Redis 容器比 H2 更真实（方言差异），CI 与本地一致

**Qspring-1941（场景单选·契约）** 在工程实践中关于「测试环境隔离」，下列做法符合推荐实践的是？
- A. 外部依赖必须全部 Mock
- B. H2 完全替代 MySQL 测试
- C. 集成测试环境标准
- D. 测试环境用生产数据
**答案：C**
**解析：** 推荐实践：集成测试环境标准。事实依据：测试配置隔离：test profile 独立数据源（H2/Testcontainers）与 Mock 外部依赖。

**Qspring-1942（场景判断·契约）** 推荐实践：集成测试环境标准
**答案：对。** 解析：测试配置隔离：test profile 独立数据源（H2/Testcontainers）与 Mock 外部依赖。原因：Testcontainers 起真实 MySQL/Redis 容器比 H2 更真实（方言差异），CI 与本地一致

**Qspring-1943（简答·契约）** 请说明「测试」中测试环境隔离的机制与使用要点。
**要点（标准答案）**：① 测试配置隔离：test profile 独立数据源（H2/Testcontainers）与 Mock 外部依赖；② 原理：Testcontainers 起真实 MySQL/Redis 容器比 H2 更真实（方言差异），CI 与本地一致；③ 使用要点：集成测试环境标准。版本锚点：实战共识。

**Qspring-1944（单选·正向·API）** 关于「IoC」的说法，正确的是？
- A. ApplicationContextAware 已废弃
- B. 获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean
- C. 手动 getBean 是推荐做法
- D. 静态获取 Bean 与注入等价
**答案：B**
**解析：** 获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean。原因：手动 getBean 隐藏依赖关系与静态耦合（ServiceLocator 反模式），例外：工具类/无法注入的场景。
**来源：** SP-109 · IoC（Spring 官方建议）

**Qspring-1945（判断·API）** 获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean
**答案：对。** 解析：手动 getBean 隐藏依赖关系与静态耦合（ServiceLocator 反模式），例外：工具类/无法注入的场景

**Qspring-1946（判断·API）** 手动 getBean 是推荐做法
**答案：错。** 正确表述：获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean。原因：手动 getBean 隐藏依赖关系与静态耦合（ServiceLocator 反模式），例外：工具类/无法注入的场景

**Qspring-1947（判断·API）** ApplicationContextAware 已废弃
**答案：错。** 正确表述：获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean。原因：手动 getBean 隐藏依赖关系与静态耦合（ServiceLocator 反模式），例外：工具类/无法注入的场景

**Qspring-1948（判断·API）** 静态获取 Bean 与注入等价
**答案：错。** 正确表述：获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean。原因：手动 getBean 隐藏依赖关系与静态耦合（ServiceLocator 反模式），例外：工具类/无法注入的场景

**Qspring-1949（场景单选·API）** 在工程实践中关于「ApplicationContext」，下列做法符合推荐实践的是？
- A. 代码 review 识别 ServiceLocator
- B. 静态获取 Bean 与注入等价
- C. ApplicationContextAware 已废弃
- D. 手动 getBean 是推荐做法
**答案：A**
**解析：** 推荐实践：代码 review 识别 ServiceLocator。事实依据：获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean。

**Qspring-1950（场景判断·API）** 推荐实践：代码 review 识别 ServiceLocator
**答案：对。** 解析：获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean。原因：手动 getBean 隐藏依赖关系与静态耦合（ServiceLocator 反模式），例外：工具类/无法注入的场景

**Qspring-1951（填空·API）** 获取容器内 Bean 的正道是注入而非 ______Aware 手动 getBean
**答案：ApplicationContext**。解析：手动 getBean 隐藏依赖关系与静态耦合（ServiceLocator 反模式），例外：工具类/无法注入的场景

**Qspring-1952（简答·API）** 请说明「IoC」中ApplicationContext的机制与使用要点。
**要点（标准答案）**：① 获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean；② 原理：手动 getBean 隐藏依赖关系与静态耦合（ServiceLocator 反模式），例外：工具类/无法注入的场景；③ 使用要点：代码 review 识别 ServiceLocator。版本锚点：Spring 官方建议。

**Qspring-1953（单选·正向·复习）** 关于「综合」的说法，正确的是？
- A. 自动配置占比最大
- B. Spring 复习优先级：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程
- C. MVC 流程最重要
- D. 事务不是重点
**答案：B**
**解析：** Spring 复习优先级：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程。原因：按面试命中率排序（P7 岗位 JD 高频），每块都配手写复述（不看书讲清楚）再进下一块。
**来源：** SP-110 · 综合（复习方法论）

**Qspring-1954（判断·复习）** Spring 复习优先级：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程
**答案：对。** 解析：按面试命中率排序（P7 岗位 JD 高频），每块都配手写复述（不看书讲清楚）再进下一块

**Qspring-1955（判断·复习）** MVC 流程最重要
**答案：错。** 正确表述：Spring 复习优先级：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程。原因：按面试命中率排序（P7 岗位 JD 高频），每块都配手写复述（不看书讲清楚）再进下一块

**Qspring-1956（判断·复习）** 自动配置占比最大
**答案：错。** 正确表述：Spring 复习优先级：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程。原因：按面试命中率排序（P7 岗位 JD 高频），每块都配手写复述（不看书讲清楚）再进下一块

**Qspring-1957（判断·复习）** 事务不是重点
**答案：错。** 正确表述：Spring 复习优先级：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程。原因：按面试命中率排序（P7 岗位 JD 高频），每块都配手写复述（不看书讲清楚）再进下一块

**Qspring-1958（场景单选·复习）** 在工程实践中关于「优先级」，下列做法符合推荐实践的是？
- A. MVC 流程最重要
- B. 复习时间分配依据
- C. 自动配置占比最大
- D. 事务不是重点
**答案：B**
**解析：** 推荐实践：复习时间分配依据。事实依据：Spring 复习优先级：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程。

**Qspring-1959（场景判断·复习）** 推荐实践：复习时间分配依据
**答案：对。** 解析：Spring 复习优先级：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程。原因：按面试命中率排序（P7 岗位 JD 高频），每块都配手写复述（不看书讲清楚）再进下一块

**Qspring-1960（填空·复习）** Spring 复习______：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程
**答案：优先级**。解析：按面试命中率排序（P7 岗位 JD 高频），每块都配手写复述（不看书讲清楚）再进下一块

**Qspring-1961（简答·复习）** 请说明「综合」中优先级的机制与使用要点。
**要点（标准答案）**：① Spring 复习优先级：事务失效与传播 > Bean 生命周期与三级缓存 > AOP 原理 > Boot 自动配置 > MVC 流程；② 原理：按面试命中率排序（P7 岗位 JD 高频），每块都配手写复述（不看书讲清楚）再进下一块；③ 使用要点：复习时间分配依据。版本锚点：复习方法论。

**Qspring-1962（单选·反向·IoC）** 以下关于「IoC」的说法，**错误**的是？
- A. singleton 中注入 prototype Bean 只注入一次失去多例语义
- B. Spring 单例是 JVM 全局唯一
- C. Spring Bean 默认作用域是 singleton 单例容器内唯一
- D. Web 作用域 request/session/application 依赖 Web 环境且注入 singleton 时需代理
**答案：B**
**解析：** 正确表述应为——Spring Bean 默认作用域是 singleton 单例容器内唯一。原因：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）。

**Qspring-1963（单选·反向·Bean 生命周期）** 以下关于「Bean 生命周期」的说法，**错误**的是？
- A. BeanPostProcessor 在初始化前后对每个 Bean 加工
- B. Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁
- C. 实例化与初始化是同一件事
- D. 初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method
**答案：C**
**解析：** 正确表述应为——Bean 生命周期主线：实例化、属性填充、Aware 回调、BeanPostProcessor 前后处理、初始化、使用、销毁。原因：实例化（构造）与初始化（init 回调）是两个阶段，属性填充在两者之间，记住主线再展开细节。

**Qspring-1964（单选·反向·AOP）** 以下关于「AOP」的说法，**错误**的是？
- A. AOP 代理在 postProcessBeforeInitialization 创建
- B. AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建
- C. Spring Boot 2.0 起 AOP 默认强制 CGLIB（proxy-target-class=true）
- D. JDK 动态代理要求目标实现接口，CGLIB 生成子类代理无接口要求
**答案：A**
**解析：** 正确表述应为——AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建。原因：AbstractAutoProxyCreator.wrapIfNecessary 在 After 阶段判断切点匹配生成代理（本项目源码级核对结论），代理创建晚于 init 回调。

**Qspring-1965（单选·反向·循环依赖）** 以下关于「循环依赖」的说法，**错误**的是？
- A. 三级缓存都是存 Bean 实例的
- B. 三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂
- C. 三级缓存存在的意义是让 AOP 场景能提前拿到代理引用
- D. 构造器注入的循环依赖 Spring 无法解决
**答案：A**
**解析：** 正确表述应为——三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。原因：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory。

**Qspring-1966（单选·反向·容器）** 以下关于「容器」的说法，**错误**的是？
- A. 容器启动核心是 AbstractApplicationContext.refresh 的 12 步模板
- B. ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化
- C. ApplicationContext 与 BeanFactory 无关
- D. ApplicationContext 是 BeanFactory 的超集增强版
**答案：C**
**解析：** 正确表述应为——ApplicationContext 是 BeanFactory 的超集增强版。原因：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton。

**Qspring-1967（单选·反向·扩展点）** 以下关于「扩展点」的说法，**错误**的是？
- A. BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition
- B. BFPP 在 Bean 创建后执行
- C. Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理
- D. BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition
**答案：B**
**解析：** 正确表述应为——BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition。原因：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP。

**Qspring-1968（单选·反向·Boot）** 以下关于「Boot」的说法，**错误**的是？
- A. @ConfigurationProperties 只能绑定 String
- B. 配置优先级：命令行参数 > 环境变量 > application-{profile} > application
- C. @Profile 按激活的 profile 决定 Bean 是否装配
- D. @ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据
**答案：A**
**解析：** 正确表述应为——@ConfigurationProperties 批量绑定前缀下的属性并支持校验与元数据。原因：relaxed binding 支持 kebab-case 与驼峰互转，配合 @Validated 做 JSR-303 校验，IDE 有元数据提示，优于散落的 @Value。

**Qspring-1969（单选·反向·事务）** 以下关于「事务」的说法，**错误**的是？
- A. @Transactional 基于 AOP 代理由 TransactionInterceptor 实现
- B. @Transactional 是 JDBC 驱动实现
- C. @Transactional 自调用失效是最高频事务坑
- D. Spring 6.0 之前 @Transactional 只对 public 方法生效
**答案：B**
**解析：** 正确表述应为——@Transactional 基于 AOP 代理由 TransactionInterceptor 实现。原因：开启事务（getConnection setAutoCommit false）、执行业务、按异常类型决定提交回滚，事务属性由 TransactionAttributeSource 解析。

**Qspring-1970（单选·反向·MyBatis）** 以下关于「MyBatis」的说法，**错误**的是？
- A. Mapper 接口由 JDK 反射直接调用
- B. MyBatis 一级缓存 SqlSession 级：非事务时每个 Mapper 方法独立 SqlSession（缓存基本无效），同一事务内共享 SqlSession（缓存生效）
- C. @MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean
- D. MyBatis 二级缓存 namespace 级多 SqlSession 共享但生产慎用
**答案：A**
**解析：** 正确表述应为——@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。原因：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理。

**Qspring-1971（单选·反向·缓存）** 以下关于「缓存」的说法，**错误**的是？
- A. 缓存注解同样受自调用失效影响
- B. Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合
- C. @CachePut 也先查缓存
- D. @Cacheable 默认不缓存 null 返回值（可配 allowNullValues）
**答案：C**
**解析：** 正确表述应为——Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合。原因：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）。

**Qspring-1972（单选·反向·安全）** 以下关于「安全」的说法，**错误**的是？
- A. Spring Security 是拦截器实现
- B. Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）
- C. 分布式会话两路线：Spring Session 集中存 Redis 或 JWT 自包含
- D. JWT 无状态认证：签发→携带→过滤链校验签名
**答案：A**
**解析：** 正确表述应为——Spring Security 基于 Servlet Filter 链（FilterChainProxy 代理一串安全过滤器）。原因：认证（AuthenticationManager）、授权（AuthorizationManager）、CSRF、会话管理各是一环，与业务拦截器（HandlerInterceptor）职责分层。

