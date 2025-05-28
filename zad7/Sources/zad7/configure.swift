import NIOSSL
import Fluent
import FluentPostgresDriver
import Leaf
import Vapor

// configures your application
public func configure(_ app: Application) async throws {
    // uncomment to serve files from /Public folder
    // app.middleware.use(FileMiddleware(publicDirectory: app.directory.publicDirectory))

    app.databases.use(
        .postgres(
            configuration: .init(
                hostname: "localhost",
                username: "postgres",
                password: "",
                database: "zad7",
                tls: .disable
            )
        ),
        as: .psql
    )

    app.migrations.add(CreateProduct())

    app.views.use(.leaf)

    // register routes
    try routes(app)
}
