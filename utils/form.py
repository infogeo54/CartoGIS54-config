"""
Utils functions to retrieve data from QGIS attributes from
"""



def field_config(field):
    """
    Returns a layer's field configuration
    :param field: QgsField - The concerned field
    :return: Dict
    """
    widget = field.editorWidgetSetup()
    return dict(
        name=field.name(),
        alias=field.alias(),
        type=widget.type(),
        options=widget.config(),
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

