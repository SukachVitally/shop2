ShopManager.module "Entities", (Entities, ContactManager, Backbone, Marionette, $, _)->
  class Entities.Product extends  Backbone.Model
    urlRoot: "/product"

  class Entities.ProductCollection extends Backbone.Collection
    url: "/api/products"
    model: Entities.Product

  API =
    getProductEntities: ->
      products = new Entities.ProductCollection()
      defer = $.Deferred()
      products.fetch
        success: (data)->
          defer.resolve data

      defer.promise()

    getProductEntity: (productId)->
      product = new Entities.Product({id: productId});
      defer = $.Deferred()
      product.fetch
        success: (data)->
          defer.resolve data
        error: (data)->
          defer.resolve null
      defer.promise()


  ShopManager.reqres.setHandler "product:entities", ->
    API.getProductEntities()

  ContactManager.reqres.setHandler "product:entity", (id)->
    API.getProductEntity(id)
