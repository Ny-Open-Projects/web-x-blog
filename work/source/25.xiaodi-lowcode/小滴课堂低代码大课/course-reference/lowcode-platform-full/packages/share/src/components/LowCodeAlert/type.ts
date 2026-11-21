import type { TBasicComponentConfig, TransformedComponentConfig } from "..";

export interface IAlertComponentProps {
  title: string;
  showIcon: boolean;
  showClose: boolean;
  type: "success" | "info" | "warning" | "error";
}

// 转换成通用组件类型
export type TAlertComponentConfig = {
  type: "alert";
  id: string;
  props: {
    title: string;
    description: string;
    showIcon: boolean;
    showClose: boolean;
    isBanner: boolean;
    type: "success" | "info" | "warning" | "error";
  };
};

export type TAlertComponentConfigResult =
  TransformedComponentConfig<IAlertComponentProps>;

export const alertComponentDefaultConfig = {
  title: {
    defaultValue: "",
    value: "",
    isHidden: false,
  },
  showIcon: {
    defaultValue: true,
    value: true,
    isHidden: false,
  },
  showClose: {
    defaultValue: true,
    value: true,
    isHidden: false,
  },
  type: {
    defaultValue: "warning",
    value: "warning",
    isHidden: false,
  },
};
