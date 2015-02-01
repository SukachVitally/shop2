ShopManager.module "ProductsApp.List", (List, ShopManager, Backbone, Marionette, $, _)->
  List.Controller =
    listProducts: (criterion)->
      loadingView = new ShopManager.Common.Views.Loading();
      ShopManager.mainRegion.show loadingView

      fetchingProducts = ShopManager.request "product:entities"

      productsListLayout = new List.Layout()
      productsListPanel = new List.Panel()

      $.when(fetchingProducts).done (products)->
#        criterion = null
#        filteredContacts = ContactManager.Entities.FilteredCollection
#          collection: contacts
#          filterFunction: (filterCriterion)->
#            criterion = filterCriterion.toLowerCase()
#            (contact)->
#              if contact.get("firstName").toLowerCase().indexOf(criterion) isnt -1 or
#              contact.get("lastName").toLowerCase().indexOf(criterion)  isnt -1 or
#              contact.get("phoneNumber").toLowerCase().indexOf(criterion) isnt -1
#                contact
#
#        if criterion
#          filteredContacts.filter criterion
#          contactsListPanel.once "show", ->
#            contactsListPanel.triggerMethod "set:filter:criterion", criterion


        contactsListView = new List.Products collection: products

        ShopManager.mainRegion.show contactsListView
