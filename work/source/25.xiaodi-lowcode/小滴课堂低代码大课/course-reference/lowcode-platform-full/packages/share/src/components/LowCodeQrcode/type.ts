import type { TBasicComponentConfig, TransformedComponentConfig } from "..";

// 二维码组件的属性
export interface IQrcodeComponentProps {
  icon: string;
  size: number;
  value: string;
  color: string;
  bgColor: string;
  iconSize: number;
  errorLevel: "L" | "M" | "Q" | "H";
}

export type TQrcodeComponentConfig = TBasicComponentConfig<
  "qrcode",
  IQrcodeComponentProps
>;

export type TQrcodeComponentConfigResult =
  TransformedComponentConfig<IQrcodeComponentProps>;

// 二维码表单数据的格式
export const qrcodeComponentDefaultConfig: TQrcodeComponentConfigResult = {
  value: {
    value: "-",
    defaultValue: "-",
    isHidden: false,
  },
  bgColor: {
    value: "white",
    defaultValue: "white",
    isHidden: false,
  },
  color: {
    value: "black",
    defaultValue: "black",
    isHidden: false,
  },
  errorLevel: {
    value: "L",
    defaultValue: "L",
    isHidden: false,
  },
  icon: {
    value: "",
    defaultValue: "",
    isHidden: true,
  },
  iconSize: {
    value: 12,
    defaultValue: 12,
    isHidden: true,
  },
  size: {
    value: 160,
    defaultValue: 160,
    isHidden: false,
  },
};
