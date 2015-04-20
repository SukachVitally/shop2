ShopManager.module "Entities", (Entities, ShopManager, Backbone, Marionette, $, _)->

  class Entities.SidebarLink extends  Backbone.Model

  class Entities.SidebarLinkCollection extends Backbone.Collection
    url: "/shop/groups/"
    model: Entities.SidebarLink

  API =
    getSidebarList: ->
      defer = $.Deferred()

      links = new Entities.SidebarLinkCollection()
      links.fetch
        success: (data)->
          defer.resolve data

      defer.promise()

  ShopManager.reqres.setHandler "sidebar:entities", ->
    API.getSidebarList()
