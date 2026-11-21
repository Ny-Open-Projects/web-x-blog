import type { TComponentPropsUnion } from "@lowcode/share";
import { makeAutoObservable } from "mobx";

interface IStoreComponents {
  compConfigs: Record<string, TComponentPropsUnion>; // 所有组件属性信息
  sortableCompConfig: string[]; // 所有组件的排序
  currentCompConfig: string | null; // 当前选中的组件
  copyedCompConig: TComponentPropsUnion | null; // 复制组件
  itemsExpandIndex: number;
}

export function createStoreComponents() {
  return makeAutoObservable<IStoreComponents>({
    compConfigs: {},
    sortableCompConfig: [],
    currentCompConfig: null,
    copyedCompConig: null,
    itemsExpandIndex: 0,
  });
}

export type TStoreComponents = ReturnType<typeof createStoreComponents>;
