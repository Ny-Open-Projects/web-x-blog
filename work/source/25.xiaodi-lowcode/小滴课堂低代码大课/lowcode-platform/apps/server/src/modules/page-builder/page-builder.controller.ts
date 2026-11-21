import {
  Controller,
  Get,
  Post,
  Put,
  Param,
  Body,
  Header,
  UseGuards,
} from '@nestjs/common';
import { IsString, IsObject, IsOptional } from 'class-validator';
import { TenantGuard } from '../workflow/guards/tenant.guard';
import { CurrentTenant } from '../workflow/decorators/current-tenant.decorator';
import { PageBuilderService } from './page-builder.service';
import { PageSchema } from '@lowcode/shared';

class CreatePageDto {
  @IsString() name!: string;
  @IsObject() schema!: PageSchema;
}

class UpdatePageDto {
  @IsOptional() @IsString() name?: string;
  @IsOptional() @IsObject() schema?: PageSchema;
}

/**
 * 可视化页面 CRUD + HTML 渲染。
 * 与 workflow 模块同级，复用 renderPageToHtml；租户隔离由 TenantGuard 统一提供。
 */
@Controller('pages')
@UseGuards(TenantGuard)
export class PageBuilderController {
  constructor(private readonly svc: PageBuilderService) {}

  @Post()
  create(@Body() dto: CreatePageDto, @CurrentTenant() tenantId: string | null) {
    return this.svc.create({ name: dto.name, schema: dto.schema, tenantId });
  }

  @Get()
  list(@CurrentTenant() tenantId: string | null) {
    return this.svc.list(tenantId);
  }

  @Get(':id')
  get(@Param('id') id: string, @CurrentTenant() tenantId: string | null) {
    return this.svc.get(id, tenantId);
  }

  @Put(':id')
  update(
    @Param('id') id: string,
    @Body() dto: UpdatePageDto,
    @CurrentTenant() tenantId: string | null,
  ) {
    return this.svc.update(id, dto, tenantId);
  }

  @Get(':id/render')
  @Header('Content-Type', 'text/html; charset=utf-8')
  render(@Param('id') id: string, @CurrentTenant() tenantId: string | null) {
    return this.svc.render(id, tenantId);
  }
}
