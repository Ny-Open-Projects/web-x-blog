import type { TBasicComponentConfig, TransformedComponentConfig } from "..";

// 单选框组件属性
export interface IRadioComponentProps {
  id: string;
  title: string;
  defaultRadio: string;
  options: {
    id: string;
    value: string;
  }[];
  onUpdate?: (value: string[]) => void;
}

export type TRadioComponentConfig = TBasicComponentConfig<
  "radio",
  IRadioComponentProps
>;

export type TRadioComponentConfigResult =
  TransformedComponentConfig<IRadioComponentProps>;

export const defaultRadioOptions = {
  id: "",
  value: "选项1",
};

export const radioComponentDefaultConfig: TRadioComponentConfigResult = {
  id: {
    value: "",
    defaultValue: "",
    isHidden: true,
  },
  title: {
    value: "默认展示的标题",
    defaultValue: "默认展示的标题",
    isHidden: false,
  },
  options: {
    value: [defaultRadioOptions],
    defaultValue: [defaultRadioOptions],
    isHidden: false,
  },
  defaultRadio: {
    value: defaultRadioOptions.id,
    defaultValue: defaultRadioOptions.id,
    isHidden: false,
  },
  onUpdate: {
    value: undefined,
    defaultValue: undefined,
    isHidden: false,
  },
};
