import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { getRepositoryToken } from '@nestjs/typeorm';
import { WorkflowController } from './workflow.controller';
import { WorkflowService } from './workflow.service';
import { WfGraph } from './entities/wf-graph.entity';
import { WfNodeDef } from './entities/wf-node-def.entity';
import { WfRun } from './entities/wf-run.entity';
import { WfRunNode } from './entities/wf-run-node.entity';
import { WfGeneratedPage } from './entities/wf-generated-page.entity';
import { WfAudit } from './entities/wf-audit.entity';
import { WfSubmission } from './entities/wf-submission.entity';
import { TenantGuard } from './guards/tenant.guard';
import { ConsoleSmsProvider, LocalOssProvider, DbFormStore, WorkflowServices } from './nodes/providers';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      WfGraph,
      WfNodeDef,
      WfRun,
      WfRunNode,
      WfGeneratedPage,
      WfAudit,
      WfSubmission,
    ]),
  ],
  controllers: [WorkflowController],
  providers: [
    WorkflowService,
    TenantGuard,
    // 副作用 Provider：生产在 WorkflowModule 替换 SMS/OSS 为云厂商实现即可，节点代码不动。
    {
      provide: 'WORKFLOW_SERVICES',
      useFactory: (subRepo: any) =>
        ({
          sms: new ConsoleSmsProvider(),
          oss: new LocalOssProvider(),
          formStore: new DbFormStore(subRepo),
        }) as WorkflowServices,
      inject: [getRepositoryToken(WfSubmission)],
    },
  ],
  exports: [WorkflowService],
})
export class WorkflowModule {}
