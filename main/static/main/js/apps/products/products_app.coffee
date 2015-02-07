ShopManager.module "ProductsApp", (ProductsApp, ShopManager, Backbone, Marionette, $, _)->
  class ProductsApp.Router extends Marionette.AppRouter
    appRoutes:
      "products": "listProducts"

  API =
    listProducts: (criterion)->
      ShopManager.ProductsApp.List.Controller.listProducts criterion


  ShopManager.on "products:list", ->
    ShopManager.navigate "products"
    API.listProducts()


  ShopManager.addInitializer ->
    new ProductsApp.Router
      controller: API
