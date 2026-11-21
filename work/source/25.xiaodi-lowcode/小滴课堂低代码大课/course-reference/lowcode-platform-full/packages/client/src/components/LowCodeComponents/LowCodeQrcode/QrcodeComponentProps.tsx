import { ColorPicker, Input, Segmented } from "antd";
import { useMemo } from "react";
import type { ColorFactory } from "antd/es/color-picker/color";

import type {
  IQrcodeComponentProps,
  TQrcodeComponentConfig,
} from "@lowcode/share";
import {
  fillComponentPropsByConfig,
  qrcodeComponentDefaultConfig,
} from "@lowcode/share";
import { FormContainer, FormPropLabel } from "..";
import { useStoreComponents } from "~/hooks";

export default function QrcodeComponentProps(_props: IQrcodeComponentProps) {
  const { updateCurrentComponent } = useStoreComponents();
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, qrcodeComponentDefaultConfig);
  }, [_props]);

  // 判断是改变了二维码颜色和背景颜色的事件
  function handleValuesChangeAfter(
    changedValues: TQrcodeComponentConfig["props"]
  ) {
    if (changedValues["bgColor"] !== undefined) {
      console.log(changedValues["bgColor"]);

      updateCurrentComponent({
        bgColor: `#${(
          changedValues["bgColor"] as unknown as ColorFactory
        ).toHex()}`,
      });
    } else if (changedValues["color"] !== undefined) {
      updateCurrentComponent({
        color: `#${(
          changedValues["color"] as unknown as ColorFactory
        ).toHex()}`,
      });
    }
  }

  return (
    <FormContainer config={props} onValuesChangeAfter={handleValuesChangeAfter}>
      <FormPropLabel prop={props.value} name="value" label="二维码内容：">
        <Input />
      </FormPropLabel>
      <FormPropLabel
        prop={props.bgColor}
        name="bgColor"
        label="二维码背景颜色："
      >
        <ColorPicker showText />
      </FormPropLabel>
      <FormPropLabel prop={props.color} name="color" label="二维码颜色：">
        <ColorPicker showText />
      </FormPropLabel>
      <FormPropLabel
        prop={props.errorLevel}
        name="errorLevel"
        label="二维码容错率："
      >
        <Segmented options={["L", "M", "Q", "H"]} />
      </FormPropLabel>
      <FormPropLabel prop={props.size} name="size" label="二维码大小：">
        <Input type="number" max={375} min={80} />
      </FormPropLabel>
      {/* <FormPropLabel prop={props.icon} name="icon" label="二维码中间图标：">
        <span>TODO</span>
      </FormPropLabel>
      <FormPropLabel prop={props.iconSize} name="iconSize" label="二维码大小：">
        <Input type="number" />
      </FormPropLabel> */}
    </FormContainer>
  );
}
