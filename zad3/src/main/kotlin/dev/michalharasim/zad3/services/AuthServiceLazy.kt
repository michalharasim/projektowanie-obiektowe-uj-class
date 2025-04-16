package dev.michalharasim.zad3.services

import org.springframework.context.annotation.Lazy
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder
import org.springframework.stereotype.Service

@Service
@Lazy
class AuthServiceLazy {
    private val encoder = BCryptPasswordEncoder()

    private val users = mapOf("user3" to encoder.encode("password3"), "user4" to encoder.encode("password4"))

    fun authenticate(username: String, password: String): Boolean {
        val hashPassword = users[username];
        return hashPassword != null && encoder.matches(password, hashPassword);
    }}