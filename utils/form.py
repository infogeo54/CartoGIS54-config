"""
Utils functions to retrieve data from QGIS attributes from
"""

from qgis.PyQt.QtWidgets import QTableWidgetItem
from qgis.PyQt.QtCore import Qt

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

def field_options(widget, required=False):
    """
    Returns a formatted options attribute from a widget
    :param widget: QgsEditorWidgetSetup - A field's widget
    :param required: Bool - Indicates if this field is required
    :return: Dict
    """
    options, widget_type, widget_config = dict(), widget.type(), widget.config()
    options.update(widget_config)
    options.update({"disabled": False, "hidden": False, "required": required})
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
    widget, constraints = field.editorWidgetSetup(), field.constraints()
    required = constraints.constraintOrigin(constraints.ConstraintNotNull) != 0
    options = field_options(widget, required)
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

def create_label_item(title):
    item = QTableWidgetItem(title)
    item.setTextAlignment(Qt.AlignCenter)
    item.setFlags(Qt.NoItemFlags)
    return item

def create_checkbox_item(attribute):
    item = QTableWidgetItem()
    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
    item.setCheckState(Qt.Unchecked)
    item.setData(1, attribute)
    return item

def create_row(field):
    return dict(
        label=create_label_item(field["name"]),
        checkbox_hidden=create_checkbox_item('hidden'),
        checkbox_disabled=create_checkbox_item('disabled')
    )


def create_rows(fields):
    return list(map(lambda f: create_row(f), fields))


def fill_table(table, fields):
    rows = create_rows(fields)
    for index, row in enumerate(rows):
        table.setItem(index, 0, row["label"])
        table.setItem(index, 1, row["checkbox_disabled"])
        table.setItem(index, 2, row["checkbox_hidden"])

def fields_display(table):
    res = []
    for row in range(table.rowCount()):
        field_name = table.item(row, 0).text()
        disabled, hidden = table.item(row, 1).checkState() == Qt.Checked, table.item(row, 2).checkState() == Qt.Checked
        res.append(dict(field_name=field_name, disabled=disabled, hidden=hidden))
    return res