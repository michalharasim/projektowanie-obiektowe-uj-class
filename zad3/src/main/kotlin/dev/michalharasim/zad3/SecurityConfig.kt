package dev.michalharasim.zad3

import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.security.config.annotation.web.builders.HttpSecurity
import org.springframework.security.web.SecurityFilterChain

@Configuration
class SecurityConfig {

    @Bean
    fun web(http: HttpSecurity): SecurityFilterChain {
        http.authorizeHttpRequests { authorizeRequests ->
            authorizeRequests
                .requestMatchers("/auth/eager").permitAll()
                .requestMatchers("/auth/lazy").permitAll()
                .anyRequest().authenticated()
        }
        http.csrf { csrf ->
            csrf.disable()
        }

        return http.build()
    }
}