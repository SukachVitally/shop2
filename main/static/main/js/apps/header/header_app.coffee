ShopManager.module "HeaderApp", (Header, ShopManager, Backbone, Marionette, $, _)->
  API =
    listHeader: ->
      Header.List.Controller.listHeader()

  ShopManager.commands.setHandler "set:active:header", (name)->
    ShopManager.HeaderApp.List.Controller.setActiveHeader name

  Header.on "start", ->
    API.listHeader()

