import { TComponentTypes } from "../..";

// 页面表属性类型
export interface ILowCode {
  id: number;
  account_id: number;
  page_name: string;
  components: string[];
  tdk: string;
  desc: string;
}

// 组件表属性类型
export interface IComponent {
  id: number;
  account_id: number;
  page_id: number;
  type: TComponentTypes;
  options: Record<string, any>;
}

// 组件数据表属性类型
export interface IComponentData {
  id: number;
  user: string;
  page_id: number;
  props: Record<string, any>[];
}
