ShopManager.module "SidebarApp.List", (List, ShopManager, Backbone, Marionette, $, _)->
  List.Controller =
    listSidebar: ->
      sidebarLinks = ShopManager.request "sidebar:entities"
      $.when(sidebarLinks).done (links)->
        SidebarLinks = new List.Links collection: links
        ShopManager.sidebarRegion.show SidebarLinks
