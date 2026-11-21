package com.riskbot.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;

/**
 * 安全管控：actuator / prometheus 端点不裸奔。
 * <ul>
 *   <li>{@code /actuator/health}、{@code /actuator/health/**} 放行：K8s 探针 / 负载均衡健康检查必须匿名可达；</li>
 *   <li>其余 {@code /actuator/**}（info/metrics/prometheus…）Basic Auth：指标可反推业务量与内部拓扑，生产不能匿名；</li>
 *   <li>业务 API（/api/**）全部放行：本 demo 无用户体系，演示与课程联调保持开箱即用；</li>
 *   <li>CSRF 关闭：纯 REST 服务，无 Cookie 会话，开启只会挡掉合法的 POST 探针。</li>
 * </ul>
 * 凭证走环境变量 {@code ACTUATOR_USER} / {@code ACTUATOR_PASSWORD}，默认值仅供离线演示，生产必须覆盖。
 */
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
                .csrf(csrf -> csrf.disable())
                .authorizeHttpRequests(auth -> auth
                        .requestMatchers("/actuator/health", "/actuator/health/**").permitAll()
                        .requestMatchers("/actuator/**").authenticated()
                        .anyRequest().permitAll())
                .httpBasic(basic -> {
                });
        return http.build();
    }

    /**
     * actuator 管控账号（内存用户）。
     * 密码启动时 bcrypt 编码，不明文落内存常量；默认值仅 demo 用。
     */
    @Bean
    public InMemoryUserDetailsManager userDetailsService(
            @Value("${ACTUATOR_USER:admin}") String actuatorUser,
            @Value("${ACTUATOR_PASSWORD:riskbot-actuator}") String actuatorPassword) {
        UserDetails user = User.builder()
                .username(actuatorUser)
                .password(passwordEncoder().encode(actuatorPassword))
                .roles("ACTUATOR")
                .build();
        return new InMemoryUserDetailsManager(user);
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
