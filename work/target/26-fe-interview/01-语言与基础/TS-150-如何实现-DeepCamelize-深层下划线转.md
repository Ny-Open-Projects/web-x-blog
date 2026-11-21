---
title: [TS-150] 如何实现 DeepCamelize（深层下划线转驼峰）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-150：如何实现 DeepCamelize（深层下划线转驼峰）？
**答**：
- 字符串层：`a_b` 模式匹配出下划线后一个字符做 Uppercase，递归处理剩余。
- 对象层：映射类型 as 重映射键名；数组层：同态映射保元组；函数短路。
- 场景：后端 snake_case 接口到前端 camelCase 视图模型的规范化层。

```typescript
type UnderscoreToCamelCase<S extends string> =
  S extends `${infer Head}_${infer TailChar}${infer Rest}`
    ? `${Head}${Uppercase<TailChar>}${UnderscoreToCamelCase<Rest>}`
    : S;

type DeepCamelize<T> = T extends Function
  ? T
  : T extends readonly unknown[]
    ? { [K in keyof T]: DeepCamelize<T[K]> }
    : T extends object
      ? { [K in keyof T as UnderscoreToCamelCase<K & string>]: DeepCamelize<T[K]> }
      : T;

interface ApiUser {
  user_id: number;
  full_name: string;
  address_info: { street_name: string; zip_code: string };
}

type ViewModel = DeepCamelize<ApiUser>;
// { userId: number; fullName: string; addressInfo: { streetName: string; zipCode: string } }

const viewModel = (await res.json()) as ViewModel;
viewModel.addressInfo.zipCode; // 编译期即可用驼峰访问
```
