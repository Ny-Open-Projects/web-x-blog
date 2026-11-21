import { makeAutoObservable } from "mobx";

export function createStoreAuth() {
  // mobx 导出makeAutoObservable 接受一个对象返回可观察的对象，该对象是响应式的
  return makeAutoObservable({
    token: localStorage.getItem("token") ?? "",
    details: null,
  });
}
