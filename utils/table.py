from qgis.PyQt.QtWidgets import QTableWidgetItem
from qgis.PyQt.QtCore import Qt

def create_label_item(title):
    item = QTableWidgetItem(title)
    item.setTextAlignment(Qt.AlignCenter)
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