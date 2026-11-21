import type { TBasicComponentConfig, TransformedComponentConfig } from "..";

// 文本组件的属性
export interface ITextComponentProps {
  title: string;
  size: "xs" | "sm" | "base" | "lg" | "xl";
}

// 转换成通用文本组件
export type TTextComponentConfig = TBasicComponentConfig<
  "titleText",
  ITextComponentProps
>;

// 剔除可选
export type TTextComponentConfigResult =
  TransformedComponentConfig<ITextComponentProps>;

// 文本表单属性
export const textComponentDefaultConfig: TTextComponentConfigResult = {
  size: {
    value: "base",
    defaultValue: "base",
    isHidden: false,
  },
  title: {
    value: "这里修改为你要的文字",
    defaultValue: "这里修改为你要的文字",
    isHidden: false,
  },
};
