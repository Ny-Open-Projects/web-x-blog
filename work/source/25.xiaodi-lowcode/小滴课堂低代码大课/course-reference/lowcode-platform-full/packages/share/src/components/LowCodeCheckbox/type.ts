import type { TBasicComponentConfig, TransformedComponentConfig } from "..";

export interface ICheckboxComponentProps {
  id: string;
  title: string;
  defaultChecked: string[];
  options: {
    id: string;
    value: string;
  }[];
  onUpdate?: (value: any[]) => void;
}

export type TCheckboxComponentConfig = TBasicComponentConfig<
  "checkbox",
  ICheckboxComponentProps
>;

export type TCheckboxComponentConfigResult =
  TransformedComponentConfig<ICheckboxComponentProps>;

export const defaultCheckboxOptions = {
  id: "",
  value: "选项1",
};

export const checkboxComponentDefaultConfig: TCheckboxComponentConfigResult = {
  defaultChecked: {
    value: [defaultCheckboxOptions.id],
    defaultValue: [defaultCheckboxOptions.id],
    isHidden: false,
  },
  id: {
    value: "",
    defaultValue: "",
    isHidden: false,
  },
  options: {
    value: [defaultCheckboxOptions],
    defaultValue: [defaultCheckboxOptions],
    isHidden: false,
  },
  title: {
    value: "默认展示的标题",
    defaultValue: "默认展示的标题",
    isHidden: false,
  },
  onUpdate: {
    value: undefined,
    defaultValue: undefined,
    isHidden: false,
  },
};
