# 分层 jar + 非 root 用户（eclipse-temurin:21-jre）
FROM eclipse-temurin:21-jre AS build
WORKDIR /app
COPY . .
RUN ./mvnw -q -DskipTests clean package || mvn -q -DskipTests clean package

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
# 非 root 运行
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qO- http://localhost:8080/actuator/health || exit 1
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
