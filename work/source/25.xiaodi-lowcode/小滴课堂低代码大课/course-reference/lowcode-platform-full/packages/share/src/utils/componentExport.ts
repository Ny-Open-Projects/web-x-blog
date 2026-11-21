import type { FC } from "react";
import type { TComponentTypes } from "..";
import {
  CardComponent,
  ImageComponent,
  ListComponent,
  SwiperComponent,
  VideoComponent,
  TextComponent,
  SplitComponent,
  EmptyComponent,
  RichTextComponent,
  QrcodeComponent,
  AlertComponent,
  InputComponent,
  TextAreaComponent,
  RadioComponent,
  CheckboxComponent,
} from "..";

// @ts-ignore
export const componentList: Record<TComponentTypes, FC<any>> = {
  video: VideoComponent,
  image: ImageComponent,
  swiper: SwiperComponent,
  card: CardComponent,
  list: ListComponent,
  titleText: TextComponent,
  split: SplitComponent,
  empty: EmptyComponent,
  richText: RichTextComponent,
  qrcode: QrcodeComponent,
  alert: AlertComponent,
  input: InputComponent,
  textArea: TextAreaComponent,
  radio: RadioComponent,
  checkbox: CheckboxComponent,
};
