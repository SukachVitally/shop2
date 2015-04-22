ShopManager.module "ProductsApp.Show", (Show, ShopManager, Backbone, Marionette, $, _)->
  Show.Controller =
    showProduct: (id)->
      loadingView = new ShopManager.Common.Views.Loading
        title: "Artificial Loading Delay"
        message: "Data loading is delayed to demonstrate using a loading view"

      ShopManager.mainRegion.show loadingView

      fetchingProduct = ShopManager.request "product:entity", id
      $.when(fetchingProduct).done (product)->
        unless product
          productView = new Show.MissingProduct()
        else
          productView = new Show.Product model: product

        productView.on "products:list", (childView, args)->
          ShopManager.trigger "products:list"

        ShopManager.execute "clear:active:group"
        ShopManager.mainRegion.show productView
