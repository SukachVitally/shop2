ShopManager.module "Entities", (Entities, ShopManager, Backbone, Marionette, $, _)->

  API =
    getSidebarList: ->
      defer = $.Deferred()

      links = new Entities.ProductGroupCollection()
      links.fetch
        success: (data)->
          defer.resolve data

      defer.promise()

  ShopManager.reqres.setHandler "sidebar:entities", ->
    API.getSidebarList()
