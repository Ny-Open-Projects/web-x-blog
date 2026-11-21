import React, { useMemo } from 'react'
import { Input } from 'antd'
import { getDefaultValueByConfig, inputComponentDefaultConfig } from '..'
import { type ITextAreaComponentProps } from '.'

const { TextArea } = Input

export default function TextAreaComponent(_props: ITextAreaComponentProps) {
  const props = useMemo(() => {
    return { ...getDefaultValueByConfig(inputComponentDefaultConfig), ..._props }
  }, [_props])

  return (
    <div className="space-y-2 p-4">
      <span className="text-lg font-bold">{props.title}:</span> <br />
      <TextArea placeholder={props.placeholder} value={props.text} onChange={event => props.onUpdate?.(event.target.value)} />
    </div>
  )
}
