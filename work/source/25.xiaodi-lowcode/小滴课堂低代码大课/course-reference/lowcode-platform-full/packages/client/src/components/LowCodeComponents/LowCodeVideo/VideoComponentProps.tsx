import type { IVideoComponentProps } from "@lowcode/share";
import {
  fillComponentPropsByConfig,
  videoComponentDefaultConfig,
} from "@lowcode/share";
import { Input, Switch } from "antd";
import { useMemo } from "react";
import { FormContainer, FormPropLabel, UploadEditOrChooiseInput } from "..";

export default function VideoComponentProps(_props: IVideoComponentProps) {
  // 将数据转换成深层对象，方便逻辑处理
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, videoComponentDefaultConfig);
  }, [_props]);

  return (
    <FormContainer layout="vertical" config={props}>
      <FormPropLabel prop={props.src} name="src" label="播放器地址：">
        <UploadEditOrChooiseInput propName="src" type="video" />
      </FormPropLabel>

      <FormPropLabel
        prop={props.startTime}
        name="startTime"
        label="初始播放时间（秒）："
      >
        <Input type="number" placeholder="请输入初始播放时间" />
      </FormPropLabel>

      <FormPropLabel
        prop={props.autoPlay}
        name="autoPlay"
        label="是否启用自动播放："
        valuePropName="checked"
      >
        <Switch />
      </FormPropLabel>

      <FormPropLabel
        prop={props.loop}
        name="loop"
        label="是否启用循环播放："
        valuePropName="checked"
      >
        <Switch />
      </FormPropLabel>

      <FormPropLabel
        prop={props.muted}
        name="muted"
        label="是否启用静音播放："
        valuePropName="checked"
      >
        <Switch />
      </FormPropLabel>
    </FormContainer>
  );
}
