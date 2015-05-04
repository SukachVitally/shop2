ShopManager.module "ProductsApp", (ProductsApp, ShopManager, Backbone, Marionette, $, _)->
  class ProductsApp.Router extends Marionette.AppRouter
    appRoutes:
      "products(/filter/criterion::criterion)(?p=:page)": "listProducts",
      "product/:id": "showProduct"
      "group/:id(?p=:page)": "listGroupProducts"

  API =
    listProducts: (criterion, page)->
      ShopManager.ProductsApp.List.Controller.listProducts criterion, page
      ShopManager.execute "set:filter:criterion", criterion

    showProduct: (id)->
      ShopManager.ProductsApp.Show.Controller.showProduct id

    listGroupProducts: (id)->
      ShopManager.ProductsApp.List.Controller.listGroupProducts id

  ShopManager.on "products:list", ->
    ShopManager.navigate "products"
    API.listProducts()

  ShopManager.on "products:filter", (criterion)->
    if criterion
      ShopManager.navigate "products/filter/criterion:#{criterion}"
    else
      ShopManager.navigate "products"
    API.listProducts criterion

  ShopManager.on "product:show", (id)->
    ShopManager.navigate "product/#{id}"
    API.showProduct id

  ShopManager.on "group:show", (id)->
    ShopManager.navigate "group/#{id}"
    API.listGroupProducts id

  ShopManager.addInitializer ->
    new ProductsApp.Router
      controller: API
