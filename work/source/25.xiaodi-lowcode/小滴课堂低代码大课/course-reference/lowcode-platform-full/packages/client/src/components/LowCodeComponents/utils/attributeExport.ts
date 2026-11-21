import type { FC } from "react";
import {
  ImageComponentProps,
  SwiperComponentProps,
  VideoComponentProps,
  CardComponentProps,
  ListComponentProps,
  TextComponentProps,
  SplitComponentProps,
  EmptyComponentProps,
  RichTextComponentProps,
  QrcodeComponentProps,
  AlertComponentProps,
  InputComponentProps,
  CheckboxComponentProps,
  RadioComponentProps,
} from "..";
import type { TBasicComponentConfig } from "@lowcode/share";

// @ts-ignore
export const componentPropsList: Record<TComponentTypes, FC<any>> = {
  video: VideoComponentProps,
  image: ImageComponentProps,
  swiper: SwiperComponentProps,
  card: CardComponentProps,
  list: ListComponentProps,
  titleText: TextComponentProps,
  split: SplitComponentProps,
  empty: EmptyComponentProps,
  richText: RichTextComponentProps,
  qrcode: QrcodeComponentProps,
  alert: AlertComponentProps,
  input: InputComponentProps,
  textArea: InputComponentProps,
  radio: RadioComponentProps,
  checkbox: CheckboxComponentProps,
};

export function getComponentPropsByType(type: TBasicComponentConfig["type"]) {
  return componentPropsList[type];
}
