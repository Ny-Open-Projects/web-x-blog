import React, { useMemo } from 'react'
import { Input } from 'antd'
import { getDefaultValueByConfig } from '..'
import { type IInputComponentProps, inputComponentDefaultConfig } from '.'

export default function InputComponent(_props: IInputComponentProps) {
  const props = useMemo(() => {
    return { ...getDefaultValueByConfig(inputComponentDefaultConfig), ..._props }
  }, [_props])

  return (
    <div className="space-y-2 p-4">
      <span className="text-lg font-ld">{props.title}:</span><br />
      <Input placeholder={props.placeholder} value={props.text} onChange={event => props.onUpdate?.(event.target.value)} />
    </div>
  )
}
