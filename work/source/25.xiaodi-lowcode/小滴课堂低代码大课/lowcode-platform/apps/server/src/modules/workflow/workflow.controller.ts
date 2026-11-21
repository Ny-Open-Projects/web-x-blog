import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  Post,
  Put,
  Header,
  UseGuards,
} from '@nestjs/common';
import { WorkflowService } from './workflow.service';
import { CreateWorkflowDto } from './dto/create-workflow.dto';
import { RunWorkflowDto } from './dto/run-workflow.dto';
import { TenantGuard } from './guards/tenant.guard';
import { CurrentTenant } from './decorators/current-tenant.decorator';

@UseGuards(TenantGuard)
@Controller('workflow')
export class WorkflowController {
  constructor(private readonly svc: WorkflowService) {}

  @Post()
  create(@Body() dto: CreateWorkflowDto, @CurrentTenant() tenantId: string | null) {
    return this.svc.create(dto, tenantId);
  }

  @Get()
  list(@CurrentTenant() tenantId: string | null) {
    return this.svc.list(tenantId);
  }

  @Get('nodes')
  nodes() {
    return this.svc.nodeCatalog();
  }

  @Get('pages')
  listPages(@CurrentTenant() tenantId: string | null) {
    return this.svc.listPages(tenantId);
  }

  @Get('stats')
  stats(@CurrentTenant() tenantId: string | null) {
    return this.svc.getStats(tenantId);
  }

  @Get('audit')
  audit(@CurrentTenant() tenantId: string | null) {
    return this.svc.listAudit(tenantId);
  }

  @Get('pages/:id')
  getPage(@Param('id') id: string) {
    return this.svc.getPage(id);
  }

  @Get('pages/:id/render')
  @Header('Content-Type', 'text/html; charset=utf-8')
  renderPage(@Param('id') id: string) {
    return this.svc.renderPage(id);
  }

  @Get(':id')
  get(@Param('id') id: string, @CurrentTenant() tenantId: string | null) {
    return this.svc.get(id, tenantId);
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() dto: CreateWorkflowDto) {
    return this.svc.update(id, dto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.svc.remove(id);
  }

  @Post(':id/run')
  run(
    @Param('id') id: string,
    @Body() dto: RunWorkflowDto,
    @CurrentTenant() tenantId: string | null,
  ) {
    return this.svc.run(id, dto, tenantId);
  }
}
