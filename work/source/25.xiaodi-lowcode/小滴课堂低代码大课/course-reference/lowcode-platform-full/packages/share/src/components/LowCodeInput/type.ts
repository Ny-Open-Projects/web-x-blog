import type { TBasicComponentConfig, TransformedComponentConfig } from "..";

export interface IInputComponentProps {
  title: string;
  text: string;
  placeholder: string;
  onUpdate?: (value: string) => void;
}

export type TInputComponentConfig = TBasicComponentConfig<
  "input",
  IInputComponentProps
>;

export type TInputComponentConfigResult =
  TransformedComponentConfig<IInputComponentProps>;

export const inputComponentDefaultConfig: TInputComponentConfigResult = {
  placeholder: {
    value: "请输入内容……",
    defaultValue: "请输入内容……",
    isHidden: false,
  },
  text: {
    value: "",
    defaultValue: "",
    isHidden: false,
  },
  title: {
    value: "请输入标题……",
    defaultValue: "请输入标题……",
    isHidden: false,
  },
  onUpdate: {
    value: undefined,
    defaultValue: undefined,
    isHidden: true,
  },
};
