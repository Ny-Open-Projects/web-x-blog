import { IsString, IsNotEmpty } from 'class-validator';

export class CaptchaDto {
  @IsNotEmpty({ message: 'type限制不为空!' })
  @IsString({ message: 'type限制为string类型!' })
  type: string;
}
