"""
Utils functions to retrieve data from QGIS attributes from
"""

def format_map(widget_map):
    """
    Returns a JSON-like version of a ValueMap widget's map option
    :param widget_map: Dict - The Valuemap to format
    :return: List
    """
    res = []
    for option in widget_map:
        key = list(option.keys())[0]
        val = option[key]
        res.append({"text": key, "value": val})
    return res

def field_options(widget):
    """
    Returns a formatted options attribute from a widget
    :param widget: QgsEditorWidgetSetup - A field's widget
    :return: Dict
    """
    options, widget_type, widget_config = dict(), widget.type(), widget.config()
    options.update(widget_config)
    options.update({"disabled": False, "hidden": False})
    if widget_type == "ValueMap":
        formatted_map = format_map(widget_config["map"])
        options.update({"map": formatted_map})
    return options


def field_config(field):
    """
    Returns a layer's field configuration
    :param field: QgsField - The concerned field
    :return: Dict
    """
    widget = field.editorWidgetSetup()
    options = field_options(widget)
    return dict(
        name=field.name(),
        alias=field.alias(),
        type=widget.type(),
        options=options,
        default=field.defaultValueDefinition().expression()
    )


def layer_fields(layer):
    """
    Returns a layer's fields list containing their configuration
    :param layer: QgsVectorLayer - The concerned lyer
    :return: List
    """
    fields = layer.fields().toList()
    return list(map(field_config, fields))


def layers_configs(layers):
    """
    Returns a list containg layers' attributes form configurations
    :param layers: List - Current project's layers
    :return: List
    """
    configs = list(map(layer_fields, layers))
    flat_configs = [field for config in configs for field in config]
    return list(
        {config["name"]: config for config in flat_configs}.values()
    )

