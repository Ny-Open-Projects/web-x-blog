import { makeAutoObservable } from "mobx";

interface IStorePage {
  title: string;
  description: string;
  tdk: string;
}

export function createStorePage() {
  return makeAutoObservable<IStorePage>({
    title: "小滴低代码开发页面",
    description: "小滴低代码开发页面详情",
    tdk: "xdclass,lowcode,低代码,小滴,小滴课堂",
  });
}

export type TStorePage = ReturnType<typeof createStorePage>;
