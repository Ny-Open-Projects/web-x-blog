import type { TBasicComponentConfig, TransformedComponentConfig } from "..";

// 视频组件的属性
export interface IVideoComponentProps {
  src: string;
  poster: string;
  autoPlay: boolean;
  loop: boolean;
  muted: boolean;
  startTime: number;
}

export type TVideoComponentConfig = TBasicComponentConfig<
  "video",
  IVideoComponentProps
>;

export type TVideoComponentConfigResult =
  TransformedComponentConfig<IVideoComponentProps>;

// 视频表单配置属性的值
export const videoComponentDefaultConfig: TVideoComponentConfigResult = {
  autoPlay: {
    value: true,
    isHidden: true,
    defaultValue: false,
  },
  poster: {
    value: "",
    defaultValue: "",
    isHidden: false,
  },
  loop: {
    value: true,
    defaultValue: true,
    isHidden: false,
  },
  muted: {
    value: false,
    defaultValue: false,
    isHidden: false,
  },
  src: {
    value: "",
    defaultValue: "",
    isHidden: false,
  },
  startTime: {
    value: 0,
    defaultValue: 0,
    isHidden: false,
  },
};
