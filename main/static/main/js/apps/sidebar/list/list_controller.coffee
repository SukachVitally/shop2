ShopManager.module "SidebarApp.List", (List, ShopManager, Backbone, Marionette, $, _)->
  List.Controller =
    listSidebar: ->
      sidebarLinks = ShopManager.request "sidebar:entities"
      $.when(sidebarLinks).done (links)->
        SidebarLinks = new List.Links collection: links

        SidebarLinks.on "childview:group:show", (childView, args)->
          ShopManager.trigger "group:show", args.model.get("id")

        SidebarLinks.on "products:list", ->
          ShopManager.trigger "products:list"

        ShopManager.sidebarRegion.show SidebarLinks
