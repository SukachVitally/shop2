ShopManager.module "ContactsApp.Show", (Show, ContactManager, Backbone, Marionette, $, _)->
  Show.Controller =
    showContact: (id)->
      loadingView = new ContactManager.Common.Views.Loading
        title: "Artificial Loading Delay"
        message: "Data loading is delayed to demonstrate using a loading view"

      ContactManager.mainRegion.show loadingView

      fetchingContact = ContactManager.request "contact:entity", id
      $.when(fetchingContact).done (contact)->
        unless contact
          contactView = new Show.MissingContact()
        else
          contactView = new Show.Contact model: contact
          contactView.on "contact:edit", (contact)->
            ContactManager.trigger "contact:edit", contact.get("id")

        ContactManager.mainRegion.show contactView
