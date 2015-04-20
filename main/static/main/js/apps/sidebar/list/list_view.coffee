ShopManager.module "SidebarApp.List", (List, ShopManager, Backbone, Marionette, $, _)->

  class List.Link extends Marionette.ItemView
    template: "sidebarLink"
    tagName: "li"

  class List.Links extends Marionette.CompositeView
    className: "container-fluid"
    template: "sidebarLayout"
    childView: List.Link
    childViewContainer: "ul"
