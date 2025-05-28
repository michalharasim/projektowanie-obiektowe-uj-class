import Fluent
import struct Foundation.UUID
import Vapor

/// Property wrappers interact poorly with `Sendable` checking, causing a warning for the `@ID` property
/// It is recommended you write your model with sendability checking on and then suppress the warning
/// afterwards with `@unchecked Sendable`.
final class Product: Model, @unchecked Sendable {
    static let schema = "products"
    
    @ID(key: .id)
    var id: UUID?

    @Field(key: "name")
    var name: String
    
    @Field(key: "price")
    var price: Double

    init() { }

    init(id: UUID? = nil, name: String, price: Double) {
        self.id = id
        self.name = name
        self.price = price
    }

}
