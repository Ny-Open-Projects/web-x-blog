import { IsOptional, IsString } from 'class-validator';

export class RunWorkflowDto {
  @IsOptional() @IsString() trigger?: string;
  /** 多租户预留：后续按 tenantId 做隔离与计量 */
  @IsOptional() tenantId?: string;
}
