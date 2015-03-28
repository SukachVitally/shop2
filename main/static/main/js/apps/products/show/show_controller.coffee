ShopManager.module "ProductsApp.Show", (Show, ContactManager, Backbone, Marionette, $, _)->
  Show.Controller =
    showProduct: (id)->
      loadingView = new ContactManager.Common.Views.Loading
        title: "Artificial Loading Delay"
        message: "Data loading is delayed to demonstrate using a loading view"

      ShopManager.mainRegion.show loadingView

      fetchingProduct = ShopManager.request "product:entity", id
      $.when(fetchingProduct).done (product)->
        unless product
          productView = new Show.MissingProduct()
        else
          productView = new Show.Product model: product

        ContactManager.mainRegion.show productView
