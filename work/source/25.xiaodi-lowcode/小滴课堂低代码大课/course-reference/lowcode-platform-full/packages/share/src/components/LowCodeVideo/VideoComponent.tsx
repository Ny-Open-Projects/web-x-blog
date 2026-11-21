import React, { useMemo, useState } from "react";
import { getDefaultValueByConfig } from "..";
import { objectOmit } from "../..";
import { type IVideoComponentProps, videoComponentDefaultConfig } from ".";

export default function VideoComponent(_props: IVideoComponentProps) {
  // 当配置属性发生变化，重置属性并且重新渲染
  const props = useMemo(() => {
    return {
      ...getDefaultValueByConfig(videoComponentDefaultConfig),
      ..._props,
    };
  }, [_props]);

  // 控制器的显示与否
  const [isReady, setIsReady] = useState(false);

  // 视频加载成功后，设置展示控制器、开始播放的时间
  function handleLoadedMetadata(
    event: React.SyntheticEvent<HTMLVideoElement, Event>
  ) {
    setIsReady(true);
    event.currentTarget.currentTime = props.startTime;
  }

  return (
    <video
      controls={!!_props || isReady}
      onLoadedMetadata={handleLoadedMetadata}
      className="w-full h-[200px] object-cover outline-none"
      {...objectOmit(props, ["startTime"])}
    />
  );
}
