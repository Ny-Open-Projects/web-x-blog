---
title: "题 3.4a.2：元空间泄漏（Metaspace OOM）的成因与专案排查？"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 3.4a.2：元空间泄漏（Metaspace OOM）的成因与专案排查？

**【参考回答（可背）】** 成因清单（背 5 条）：① CGLIB/Javassist 动态代理类不断生成（每次增强都新类，如反复 refresh 的 Spring Bean）；② Groovy/JSP 等脚本引擎编译类；③ 反射滥用（频繁 Method.invoke 走膨胀路径生成字节码，JDK8 需 -Dsun.reflect.inflationThreshold 调优）；④ 自定义类加载器持有引用不释放；⑤ 脚本热更新（热部署框架每次重载都新加载器+新类）。排查：jstat 看 MC 列持续涨 → Arthas `classloader -t` 看加载器数量异常 → dump 后 MAT 看 Classes/ClassLoader 视图定位谁在生成类。
**【追问链】** ① 怎么从代码层根治？（代理对象缓存：同一目标类只生成一次增强类；脚本编译结果缓存）② 元空间参数怎么设？（MaxMetaspaceSize 设上限 fail-fast，初始 MetaspaceSize 与峰值接近减少 retrigger）。
**【P10 加分项】** 举真实事故模板："灰度发布系统每次热更都新建类加载器，累积 2 万个加载器撑爆元空间，Full GC 每分钟 3 次——修复：热更改为'复用加载器+redefine 类'，并给元空间水位加告警。动态能力要有配额意识。"
