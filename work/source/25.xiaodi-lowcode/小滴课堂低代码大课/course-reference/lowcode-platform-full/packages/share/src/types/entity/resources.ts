import type { UploadType } from '..'

export interface IResources {
  id: number
  account_id: number
  url: string
  type: UploadType
  name: string
}
