ShopManager.module "SidebarApp.List", (List, ShopManager, Backbone, Marionette, $, _)->

  class List.Link extends Marionette.ItemView
    template: "sidebarLink"
    tagName: "li"
    triggers:
      "click a.js-show-group": "group:show"

  class List.Links extends Marionette.CompositeView
    className: "container-fluid"
    template: "sidebarLayout"
    childView: List.Link
    childViewContainer: "ul.js-group-list"
    triggers:
      "click a.js-show-all-groups": "products:list"
