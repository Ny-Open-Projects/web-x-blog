---
title: [DP-029] ES 装饰器语法有哪些应用场景？（日志/鉴权/埋点）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-029：ES 装饰器语法有哪些应用场景？（日志/鉴权/埋点）
**答**：
- 装饰器是"声明式 AOP"：用 `@decorator` 给类/方法/属性/accessor 注入横切逻辑，业务方法保持干净。
- 类装饰器：修改/替换类构造器（加静态属性、注册路由）；方法装饰器：包裹原方法（日志、重试、鉴权、防抖）。
- 标准化进展：TC39 Stage 3 装饰器 + TypeScript 5 实验性支持；NestJS/Angular 重度使用。
- 面试手写点：方法装饰器拿到的是 `descriptor.value`，用高阶函数包装再放回去。

```typescript
// 方法装饰器：重试增强（对比手动包裹，声明式更整洁）
function Retry(times: number) {
  return function (target: object, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = async function (...args: unknown[]) {
      for (let i = 0; i <= times; i++) {
        try { return await original.apply(this, args); }
        catch (e) {
          if (i === times) throw e;
          console.warn(`重试 ${i + 1}/${times}`);
        }
      }
    };
    return descriptor;
  };
}
// 类装饰器：注册路由（NestJS 风格的最小示意）
const routes: Array<{ path: string; ctor: Function }> = [];
function Controller(path: string) {
  return function <T extends new (...args: any[]) => any>(ctor: T) {
    routes.push({ path, ctor });
    return ctor;
  };
}

@Controller('/users')
class UserService {
  @Retry(2)
  async fetchUser(id: number) {
    if (Math.random() < 0.6) throw new Error('network');
    return { id, name: 'Tom' };
  }
}
console.log(routes); // [{ path: '/users', ctor: UserService }]
new UserService().fetchUser(1).then((u) => console.log(u)).catch(() => console.log('最终失败'));

// 鉴权装饰器：方法执行前校验
function RequireRole(role: string) {
  return function (target: object, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function (...args: any[]) {
      const user = (this as any).currentUser;
      if (!user || !user.roles.includes(role)) throw new Error(`需要 ${role} 权限`);
      return original.apply(this, args);
    };
  };
}
class AdminService {
  currentUser = { roles: ['admin'] };
  @RequireRole('admin')
  deleteUser(id: number) { console.log('已删除', id); }
}
new AdminService().deleteUser(9); // 已删除 9
```
