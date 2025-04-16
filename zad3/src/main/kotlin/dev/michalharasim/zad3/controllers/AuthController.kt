package dev.michalharasim.zad3.controllers

import dev.michalharasim.zad3.models.LoginRequest
import dev.michalharasim.zad3.services.AuthServiceEager
import dev.michalharasim.zad3.services.AuthServiceLazy
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/auth")
class AuthController {

    private var mockData = listOf(
        Product("Product 1", 10.0),
        Product("Product 2", 20.0),
        Product("Product 3", 30.0)
    )

    @Autowired
    private lateinit var authServiceEager: AuthServiceEager

    @Autowired
    private lateinit var authServiceLazy: AuthServiceLazy

    @PostMapping("/eager")
    fun authenticateEager(@RequestBody loginRequest: LoginRequest): ResponseEntity<List<Product>> {
        return if (authServiceEager.authenticate(loginRequest.username, loginRequest.password)) {
            ResponseEntity(mockData, HttpStatus.OK)
        } else {
            ResponseEntity(null, HttpStatus.UNAUTHORIZED)
        }
    }

    @PostMapping("/lazy")
    fun authenticateLazy(@RequestBody loginRequest: LoginRequest): ResponseEntity<List<Product>> {
        return if (authServiceLazy.authenticate(loginRequest.username, loginRequest.password)) {
            ResponseEntity(mockData, HttpStatus.OK)
        } else {
            ResponseEntity(null, HttpStatus.UNAUTHORIZED)
        }
    }
}

data class Product(val name: String, val price: Double)