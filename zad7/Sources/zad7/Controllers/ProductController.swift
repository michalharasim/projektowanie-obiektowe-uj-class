import Fluent
import Vapor

struct ProductController: RouteCollection {
    func boot(routes: any RoutesBuilder) throws {
        let products = routes.grouped("products")
        products.get(use: index)
        products.get("create", use: createView)
        products.post(use: create)
        products.get(":productID", "edit", use: editView)
        products.post(":productID", "edit", use: update)
        products.post(":productID", use: delete)
    }

    func index(req: Request) throws -> EventLoopFuture<View> {
        Product.query(on: req.db).all().flatMap { products in
            let outputs = products.compactMap { product -> ProductOutput? in
                guard let id = product.id else { return nil }
                return ProductOutput(id: id, name: product.name, price: product.price)
            }
            return req.view.render("products/home", ["products": outputs])
        }
    }

    func createView(req: Request) throws -> EventLoopFuture<View> {
        req.view.render("products/create")
    }

    func create(req: Request) throws -> EventLoopFuture<Response> {
        let input = try req.content.decode(ProductInput.self)
        let product = Product(name: input.name, price: input.price)
        return product.save(on: req.db).map { req.redirect(to: "/products") }
    }

    func editView(req: Request) throws -> EventLoopFuture<View> {
        Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                guard let id = product.id else {
                    return req.eventLoop.future(error: Abort(.internalServerError))
                }
                let output = ProductOutput(id: id, name: product.name, price: product.price)
                return req.view.render("products/edit", ["product": output])
            }
    }

    func update(req: Request) throws -> EventLoopFuture<Response> {
        let input = try req.content.decode(ProductInput.self)
        return Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                product.name = input.name
                product.price = input.price
                return product.save(on: req.db).map { req.redirect(to: "/products") }
            }
    }

    func delete(req: Request) throws -> EventLoopFuture<Response> {
        guard let idString = req.parameters.get("productID"),
              let uuid = UUID(uuidString: idString) else {
            throw Abort(.badRequest, reason: "Invalid product ID format")
        }
        return Product.find(uuid, on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { $0.delete(on: req.db) }
            .map { req.redirect(to: "/products") }
    }
}

struct ProductOutput: Content, Encodable {
    let id: UUID
    let name: String
    let price: Double
}

struct ProductInput: Content {
    let name: String
    let price: Double
}
