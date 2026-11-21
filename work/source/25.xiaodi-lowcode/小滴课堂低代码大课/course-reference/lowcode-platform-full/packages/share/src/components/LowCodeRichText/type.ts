import type { TBasicComponentConfig, TransformedComponentConfig } from "..";

// 富文本组件属性
export interface IRichTextComponentProps {
  content: string;
}

// 转换通用组件数据格式;
export type TRichTextComponentConfig = TBasicComponentConfig<
  "richText",
  IRichTextComponentProps
>;

export type TRichTextComponentConfigResult =
  TransformedComponentConfig<IRichTextComponentProps>;

// 富文本表单数据格式，默认值为空
export const richTextComponentDefaultConfig: TRichTextComponentConfigResult = {
  content: {
    value: "",
    defaultValue: "",
    isHidden: false,
  },
};
