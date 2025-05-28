import Fluent
import Vapor

func routes(_ app: Application) throws {
    app.get { req async throws -> View in
        try await req.view.render("home", ["name": "Leaf"])
    }

    app.get("hello") { req async -> String in
        "Hello, world!"
    }


    try app.register(collection: ProductController())
}
