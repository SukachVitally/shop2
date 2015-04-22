ShopManager.module "SidebarApp.List", (List, ShopManager, Backbone, Marionette, $, _)->
  List.Controller =
    listSidebar: ->
      sidebarLinks = ShopManager.request "group:entities"
      $.when(sidebarLinks).done (links)->
        linkToSelect = null
        SidebarLinks = new List.Links collection: links

        SidebarLinks.on "childview:group:show", (childView, args)->
          groupId = args.model.get "id"
          ShopManager.trigger "group:show", groupId

        SidebarLinks.on "products:list", ->
          ShopManager.trigger "products:list"

        ShopManager.commands.setHandler "set:active:group", (id)->
          id = parseInt id, 10
          linkToSelect = links.findWhere id: id
          if linkToSelect
            linkToSelect.select()
            links.trigger "reset"

        ShopManager.commands.setHandler "clear:active:group", ->
          linkToSelect.deselect()
          links.trigger "reset"

        ShopManager.sidebarRegion.show SidebarLinks
