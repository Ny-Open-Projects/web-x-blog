package com.social.ecom;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.social.ecom.mapper")
public class SocialecomApplication {

	public static void main(String[] args) {
		SpringApplication.run(SocialecomApplication.class, args);
	}

}
