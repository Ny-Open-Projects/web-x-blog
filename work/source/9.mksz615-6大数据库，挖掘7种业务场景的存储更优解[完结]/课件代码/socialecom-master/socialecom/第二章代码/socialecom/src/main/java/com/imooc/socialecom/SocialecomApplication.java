package com.imooc.socialecom;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.imooc.socialecom.mapper")
public class SocialecomApplication {

	public static void main(String[] args) {
		SpringApplication.run(SocialecomApplication.class, args);
	}

}
