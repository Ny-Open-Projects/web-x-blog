import {
  Controller,
  Post,
  UseGuards,
  UseInterceptors,
  UploadedFile,
  Body,
  Delete,
  Query,
  Get,
  BadRequestException,
} from '@nestjs/common';
import { ResourcesService } from './resources.service';
import { FileInterceptor } from '@nestjs/platform-express';
import { getUserMess, TCurrentUser } from 'src/utils/GetUserMessTool';
import type { ResourcesRequest, DeleteResourcesRequest } from '@lowcode/share';

// 上传安全:大小上限 200MB(视频),仅允许图片/视频 MIME
const UPLOAD_SIZE_LIMIT = 200 * 1024 * 1024;
const ALLOWED_MIME = /^(image|video)\//;

@Controller('resources')
export class ResourcesController {
  constructor(private readonly resourcesService: ResourcesService) {}

  /**
   * 资源上传控制器
   */
  @Post('upload')
  @UseInterceptors(
    FileInterceptor('file', {
      limits: { fileSize: UPLOAD_SIZE_LIMIT },
    }),
  )
  async upload(
    @UploadedFile() file: Express.Multer.File,
    @getUserMess() user: TCurrentUser,
    @Body() body: ResourcesRequest,
  ) {
    if (!file) throw new BadRequestException('请选择要上传的文件');
    if (!ALLOWED_MIME.test(file.mimetype))
      throw new BadRequestException('仅支持上传图片或视频文件');
    if (file.size > UPLOAD_SIZE_LIMIT)
      throw new BadRequestException('文件大小不能超过 200MB');
    return this.resourcesService.upload(file, body.type, user.id);
  }

  // 删除资源控制器
  @Delete()
  async deleteResource(
    @getUserMess() user: TCurrentUser,
    @Query() params: DeleteResourcesRequest,
  ) {
    return this.resourcesService.deleteResource(params.id, user.id);
  }

  // 资源获取的控制器
  @Get()
  async getResources(
    @getUserMess() user: TCurrentUser,
    @Query() params: ResourcesRequest,
  ) {
    return this.resourcesService.getResources(params.type, user.id);
  }
}
