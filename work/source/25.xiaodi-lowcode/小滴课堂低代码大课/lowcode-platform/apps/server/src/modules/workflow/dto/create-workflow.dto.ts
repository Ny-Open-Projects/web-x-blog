import { IsArray, IsInt, IsObject, IsOptional, IsString, ValidateNested } from 'class-validator';
import { Type } from 'class-transformer';

class GraphNodeDto {
  @IsString() id!: string;
  @IsString() type!: string;
  @IsObject() params!: Record<string, unknown>;
  @IsOptional() @IsObject() position?: { x: number; y: number };
}

class GraphEdgeDto {
  @IsString() id!: string;
  @IsString() from!: string;
  @IsString() fromPort!: string;
  @IsString() to!: string;
  @IsString() toPort!: string;
}

export class CreateWorkflowDto {
  @IsString() name!: string;

  @IsInt() @IsOptional() version?: number;

  @IsArray() @ValidateNested({ each: true }) @Type(() => GraphNodeDto)
  nodes!: GraphNodeDto[];

  @IsArray() @ValidateNested({ each: true }) @Type(() => GraphEdgeDto)
  edges!: GraphEdgeDto[];
}
