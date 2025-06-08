package dev.michalharasim.zad9

import dev.michalharasim.zad9.models.Category
import dev.michalharasim.zad9.models.Product

object FakeData {
    val categories = listOf(
        Category(1, "Gaming"),
        Category(2, "Kitchen Essentials"),
        Category(3, "Music Instruments"),
        Category(4, "Office Supplies"),
        Category(5, "Pet Supplies"),
        Category(6, "Photography"),
        Category(7, "Travel Accessories"),
        Category(8, "Fitness Equipment"),
        Category(9, "Smart Home"),
        Category(10, "Crafts & DIY")
    )

    val products = listOf(
        Product(1, "Gaming Chair", 350.0, 1),
        Product(2, "Mechanical Keyboard", 150.0, 1),
        Product(3, "4K Gaming Monitor", 600.0, 1),
        Product(4, "Gaming Mouse", 90.0, 1),
        Product(5, "VR Headset", 450.0, 1),

        Product(6, "Air Fryer", 200.0, 2),
        Product(7, "Chef's Knife", 75.0, 2),
        Product(8, "Blender", 120.0, 2),
        Product(9, "Cutting Board Set", 40.0, 2),
        Product(10, "Non-Stick Pan", 60.0, 2),

        Product(11, "Acoustic Guitar", 300.0, 3),
        Product(12, "Digital Piano", 900.0, 3),
        Product(13, "Drum Pad", 250.0, 3),
        Product(14, "Violin", 180.0, 3),
        Product(15, "Ukulele", 80.0, 3),

        Product(16, "Ergonomic Office Chair", 400.0, 4),
        Product(17, "Standing Desk", 700.0, 4),
        Product(18, "Desk Organizer", 50.0, 4),
        Product(19, "LED Desk Lamp", 45.0, 4),
        Product(20, "Wireless Printer", 250.0, 4),

        Product(21, "Cat Tree", 150.0, 5),
        Product(22, "Dog Bed", 80.0, 5),
        Product(23, "Automatic Pet Feeder", 100.0, 5),
        Product(24, "Aquarium Filter", 60.0, 5),
        Product(25, "Bird Cage", 130.0, 5),

        Product(26, "Mirrorless Camera", 1200.0, 6),
        Product(27, "Tripod", 90.0, 6),
        Product(28, "Camera Bag", 60.0, 6),
        Product(29, "Lighting Kit", 150.0, 6),
        Product(30, "Lens Cleaner Kit", 25.0, 6),

        Product(31, "Hard Shell Suitcase", 180.0, 7),
        Product(32, "Neck Pillow", 30.0, 7),
        Product(33, "Packing Cubes", 35.0, 7),
        Product(34, "Portable Luggage Scale", 25.0, 7),
        Product(35, "Travel Adapter", 20.0, 7),

        Product(36, "Adjustable Dumbbells", 300.0, 8),
        Product(37, "Pull-Up Bar", 50.0, 8),
        Product(38, "Resistance Bands Set", 40.0, 8),
        Product(39, "Treadmill", 1000.0, 8),
        Product(40, "Kettlebell Set", 200.0, 8),

        Product(41, "Smart Thermostat", 250.0, 9),
        Product(42, "Smart Light Bulbs (4-pack)", 80.0, 9),
        Product(43, "Smart Doorbell", 180.0, 9),
        Product(44, "Voice Assistant Speaker", 100.0, 9),
        Product(45, "Smart Plug", 30.0, 9),

        Product(46, "3D Printing Pen", 70.0, 10),
        Product(47, "Sewing Machine", 220.0, 10),
        Product(48, "Acrylic Paint Set", 45.0, 10),
        Product(49, "Wood Carving Tools", 90.0, 10),
        Product(50, "DIY Jewelry Kit", 55.0, 10)
    )
}
