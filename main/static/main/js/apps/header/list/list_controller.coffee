ShopManager.module "HeaderApp.List", (List, ShopManager, Backbone, Marionette, $, _)->
  List.Controller =
    listHeader: ->
      loadingView = new ShopManager.Common.Views.Loading
      ShopManager.headerRegion.show loadingView

      links = ShopManager.request "header:entities"

      HeaderLinks = new List.Links collection: links

      HeaderLinks.on "products:filter", (filterCriterion)->
        ShopManager.trigger "products:filter", filterCriterion

      ShopManager.headerRegion.show HeaderLinks
