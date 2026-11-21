import React, { useMemo } from 'react'
import { Card } from 'antd'
import { getDefaultValueByConfig } from '..'
import type { ICardComponentProps } from '.'
import { cardComponentDefaultConfig } from '.'

const { Meta } = Card

export default function CardComponent(_props: ICardComponentProps) {
  const props = useMemo(() => {
    return { ...getDefaultValueByConfig(cardComponentDefaultConfig), ..._props }
  }, [_props])

  return (
    <Card
      hoverable
      cover={<img alt="cover_img" src={props.coverImg} />}
    >
      <Meta title={props.title} description={props.description} />
    </Card>
  )
}
