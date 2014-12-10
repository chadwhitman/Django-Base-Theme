If you are customizing the base.html for your own app, then first create a new directory for your app and extend off the base.html template, like so:

templates/
     app1/ #### same name as your app
           base.html #### Inherits from main base.html
           list.html
     app2/ #### same name as your app
           base.html #### Inherits from main base.html 