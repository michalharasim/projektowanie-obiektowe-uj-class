package dev.michalharasim.zad3

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.ComponentScan

@SpringBootApplication
@ComponentScan(basePackages = ["dev.michalharasim.zad3"])
class Zad3Application

fun main(args: Array<String>) {
	runApplication<Zad3Application>(*args)
}
