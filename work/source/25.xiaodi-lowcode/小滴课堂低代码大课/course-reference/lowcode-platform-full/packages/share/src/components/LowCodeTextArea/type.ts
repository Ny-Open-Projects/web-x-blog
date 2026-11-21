import type { TBasicComponentConfig, TransformedComponentConfig } from '..'

export interface ITextAreaComponentProps {
  title: string
  text: string
  placeholder: string
  onUpdate?: (value: string) => void
}

export type TTextAreaComponentConfig = TBasicComponentConfig<'textArea', ITextAreaComponentProps>

export type TTextAreaComponentConfigResult = TransformedComponentConfig<ITextAreaComponentProps>
