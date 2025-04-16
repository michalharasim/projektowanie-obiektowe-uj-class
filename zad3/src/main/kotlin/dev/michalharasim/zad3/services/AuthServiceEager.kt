package dev.michalharasim.zad3.services


import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder
import org.springframework.stereotype.Service

@Service
class AuthServiceEager {
    private val encoder = BCryptPasswordEncoder()

    private val users = mapOf("user3" to "password3", "user4" to encoder.encode("password4"))

    fun authenticate(username: String, password: String): Boolean {
        val hashPassword = users[username];
        return password == users[username];
//        return hashPassword != null && encoder.matches(password, hashPassword);
    }
}