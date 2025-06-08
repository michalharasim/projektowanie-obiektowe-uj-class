package dev.michalharasim.zad9.models

data class Product(
    val id: Int,
    val name: String,
    val price: Double,
    val categoryId: Int
)

data class Category(
    val id: Int,
    val name: String
)