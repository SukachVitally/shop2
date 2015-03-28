ShopManager.module "ProductsApp.List", (List, ShopManager, Backbone, Marionette, $, _)->
  List.Controller =
    listProducts: ->
      loadingView = new ShopManager.Common.Views.Loading();
      ShopManager.mainRegion.show loadingView

      fetchingProducts = ShopManager.request "product:entities"

      $.when(fetchingProducts).done (products)->
        productsListView = new List.Products collection: products

        productsListView.on "childview:product:show", (childView, args)->
          ShopManager.trigger("product:show", args.model.get("id"))

        ShopManager.mainRegion.show productsListView