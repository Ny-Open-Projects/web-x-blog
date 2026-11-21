import {
  type IImageComponentProps,
  type TBasicComponentConfig,
  type TransformedComponentConfig,
  defaultImageInfo,
} from "..";

// 轮播图组件属性
export interface ISwiperComponentProps {
  id: string;
  interval: number;
  autoPlay: boolean;
  images: IImageComponentProps[];
  showIndicators: boolean;
  dotPosition: "bottom" | "top" | "left" | "right";
}

// 转换成通用组件类型
export type TSwiperComponentConfig = TBasicComponentConfig<
  "swiper",
  ISwiperComponentProps
>;

// 剔除可选属性
export type TSwiperComponentConfigResult =
  TransformedComponentConfig<ISwiperComponentProps>;

// 图片表单配置属性的值
export const swiperComponentDefaultConfig: TSwiperComponentConfigResult = {
  id: {
    value: "",
    defaultValue: "",
    isHidden: true,
  },
  autoPlay: {
    value: true,
    defaultValue: true,
    isHidden: false,
  },
  images: {
    value: [defaultImageInfo],
    defaultValue: [defaultImageInfo],
    isHidden: false,
  },
  interval: {
    value: 3000,
    defaultValue: 3000,
    isHidden: false,
  },
  showIndicators: {
    value: true,
    defaultValue: true,
    isHidden: false,
  },
  dotPosition: {
    value: "bottom",
    defaultValue: "bottom",
    isHidden: false,
  },
};
