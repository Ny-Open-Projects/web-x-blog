# 多阶段构建：JDK 21 编译 + JRE 21 运行
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /build
COPY pom.xml .
RUN mvn -q dependency:go-offline -B
COPY src ./src
RUN mvn -q clean package -DskipTests -B

FROM eclipse-temurin:21-jre
RUN useradd -r -u 1001 appuser
WORKDIR /app
COPY --from=build /build/target/981-demo-1.0.0.jar app.jar
USER appuser
EXPOSE 8080
# 生产模式：SPRING_PROFILES_ACTIVE=prod（连接真实模型与 Nacos）
ENV SPRING_PROFILES_ACTIVE=default
ENTRYPOINT ["java", "-XX:+UseParallelGC", "-Xmx512m", "-jar", "app.jar"]
