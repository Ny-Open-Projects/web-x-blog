import type {
  TCardComponentConfig,
  TVideoComponentConfig,
  TImageComponentConfig,
  TSwiperComponentConfig,
  TListComponentConfig,
  TTextComponentConfig,
  TSplitComponentConfig,
  TEmptyComponentConfig,
  TRichTextComponentConfig,
  TQrcodeComponentConfig,
  TAlertComponentConfig,
  TInputComponentConfig,
  TTextAreaComponentConfig,
  TRadioComponentConfig,
  TCheckboxComponentConfig,
} from "..";
// 组件的名称映射
export type TComponentTypes =
  | "video"
  | "swiper"
  | "qrcode"
  | "card"
  | "list"
  | "image"
  | "titleText"
  | "split"
  | "richText"
  | "input"
  | "textArea"
  | "radio"
  | "checkbox"
  | "empty"
  | "alert";

export interface IComponentPropWarpper<T> {
  value: T;
  defaultValue: T;
  isHidden: boolean;
}

// 组件通用属性类型
export interface TBasicComponentConfig<
  T extends TComponentTypes = TComponentTypes,
  P extends Record<string, any> = object
> {
  type: T;
  id: string;
  props: Partial<P>;
}

// 剔除类型里面的可选
export type TransformedComponentConfig<P extends Record<string, any>> = {
  [key in keyof P]-?: IComponentPropWarpper<P[key]>;
};

// 各个组件类型
export type TComponentPropsUnion =
  | TVideoComponentConfig
  | TImageComponentConfig
  | TSwiperComponentConfig
  | TCardComponentConfig
  | TTextComponentConfig
  | TSplitComponentConfig
  | TEmptyComponentConfig
  | TRichTextComponentConfig
  | TQrcodeComponentConfig
  | TAlertComponentConfig
  | TListComponentConfig
  | TTextAreaComponentConfig
  | TRadioComponentConfig
  | TInputComponentConfig
  | TCheckboxComponentConfig;
