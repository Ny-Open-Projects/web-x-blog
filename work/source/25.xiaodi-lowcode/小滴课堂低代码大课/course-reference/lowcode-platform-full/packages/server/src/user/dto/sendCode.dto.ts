import { IsString, IsNotEmpty } from 'class-validator';

export class SendCodeDto {
  @IsNotEmpty({ message: 'type限制不为空!' })
  @IsString({ message: 'type限制为string类型!' })
  type: string;

  @IsNotEmpty({ message: 'phone限制不为空!' })
  @IsString({ message: 'phone限制为string类型!' })
  phone: string;

  @IsNotEmpty({ message: 'captcha限制不为空!' })
  @IsString({ message: 'captcha限制为string类型!' })
  captcha: string;
}
