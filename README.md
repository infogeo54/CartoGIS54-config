# CartoGIS54-config

A QGIS plugin to offer more customization to the [CartoGIS54](https://github.com/infogeo54/CartoGIS54.git) Web app. 

It allows you to indicate the geodata server host, customize the form or create modals.

Check the [config sample](https://github.com/infogeo54/CartoGIS54-config/blob/master/sample/app.config.json) to get an overview.

## Server

This section is used to configure the server part of the Web app.

### Host

You just have to type your WMS/WFS provider URL or IP in order to indicate the Web app where to send HTTP requests

### Query parameters

This part allows you to specify query parameters that will be applied to each HTTP requests sent to the host.

It can be usefull to add a `MAP` parameters in the case where your host is serving multiple projects for exemple.

#### Adding an entry

1. Click *Add row* to create a new entry
2. Fill every cells to configure the query parameter :
    * `key` : the parameter that you want to add (check available parameters for [WMS](fr.wikipedia.org/wiki/Web_Map_Service#Liste_des_paramètres_disponibles) and [WFS](https://fr.wikipedia.org/wiki/Web_Feature_Service))
    * `value` : the value of the parameter that you want to add

#### Removing an entry

1. Click on the line number or any cell of the entry that you want to remove (you can select multiple elements by holding `Ctrl` while clicking)
2. Click *Delete row* to remove selected entry

## Form

Using QGIS, you can use the Attributes form in order to create widgets that help you to edit data fields easily.

The idea there is to reuse those widgets in the Form component of the Carto54 Web app.

The main main action of this section is invisible for the user because the plugin is only retrieving data that have been specified by the user inside *Attribute form*.

Nevertheless, you can use the plugin to configure fields display rules.

### Display

Using the plugin, you can indicate which fields are disabled or hidden witinh the *Form* part of the Web app.

You just have to tick the corresponding checkbox of the field that you want to disable or hide.

## Modals

Modals can be configured inside the **Modals** section of the plugin.

By adding an entry, you'll tell the Web app to create a modal and add a button into the **Header** part of the interface.

### Adding an entry

1. Click *Add row* to create a new entry
2. Fill every cells to configure the modal :
    * `name` : this will be used to create the modal's HTML file and create the link between the modal and the button to toggle it
    * `title` : this will be displayed inside the modal's header
    * `icon` : the icon that will be associated to the modal trigger button inside the Web app header. Available icons are from FontAwesome can be found [here](https://fontawesome.com/icons?d=gallery) (check the [config sample](https://github.com/infogeo54/CartoGIS54-config/blob/master/sample/app.config.json) to know how to add an icon)
    * `visible` : this indicates to the Web app if this modal has to be visible by default. You won't often have to modify this option
    
### Removing an entry

1. Click on the line number or any cell of the entry that you want to remove (you can select multiple elements by holding `Ctrl` while clicking)
2. Click *Delete row* to remove selected entry

### Warning

1. Be sure that all the layers have undergone a modification, whatever it is, otherwise the plugin will not launch. The concerned layers will be marked by a warning message in QGIS.

2. You might encounter error messages due to the styling of certain attributes. Please correct it by applying a modification on the concerned attribute. Again, it will be displayed in QGIS.
