# 多阶段构建：编译期用 Maven 镜像，运行期用精简 JRE 镜像
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /workspace
COPY pom.xml .
RUN mvn -q -B -DskipTests dependency:go-offline || true
COPY . .
RUN mvn -q -B -DskipTests clean package

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /workspace/target/*.jar app.jar
# 非 root 运行，降低容器逃逸风险
RUN useradd -m -s /usr/sbin/nologin appuser && chown -R appuser /app
USER appuser
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
