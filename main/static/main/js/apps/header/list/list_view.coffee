ShopManager.module "HeaderApp.List", (List, ShopManager, Backbone, Marionette, $, _)->

  class List.Link extends Marionette.ItemView
    template: "headerLink"
    tagName: "li"

  class List.Links extends Marionette.CompositeView
    className: "container-fluid"
    template: "headerLayout"
    childView: List.Link
    childViewContainer: "ul"
