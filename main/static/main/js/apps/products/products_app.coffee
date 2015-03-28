ShopManager.module "ProductsApp", (ProductsApp, ShopManager, Backbone, Marionette, $, _)->
  class ProductsApp.Router extends Marionette.AppRouter
    appRoutes:
      "products": "listProducts"
      "product/:id": "showProduct"

  API =
    listProducts: (criterion)->
      ShopManager.ProductsApp.List.Controller.listProducts criterion

    showProduct: (id)->
      ShopManager.ProductsApp.Show.Controller.showProduct id


  ShopManager.on "products:list", ->
    ShopManager.navigate "products"
    API.listProducts()

  ShopManager.on "product:show", (id)->
    ShopManager.navigate "product/#{id}"
    API.showProduct(id)

  ShopManager.addInitializer ->
    new ProductsApp.Router
      controller: API
