import type { ILowCode, IComponent, IComponentData } from "..";

export type PostReleaseRequest = Omit<
  ILowCode,
  "id" | "account_id" | "components"
> & { components: Omit<IComponent, "account_id" | "page_id">[] };

export type PostQuestionDataRequest = Pick<IComponentData, "page_id" | "props">;

export type GetReleaseDataResponse = Omit<ILowCode, "components"> & {
  componentIds: string[];
  components: IComponent[];
};

export type getQuestionDataByIdRequest = Pick<IComponent, "id">;
