from qgis.PyQt.QtWidgets import QTableWidgetItem
from qgis.PyQt.QtCore import Qt

def checkbox():
    item = QTableWidgetItem()
    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
    item.setCheckState(Qt.Unchecked)
    return item


def add_row(table):
    row = table.rowCount()
    table.setRowCount(table.rowCount() + 1)
    table.setItem(row, 0, QTableWidgetItem())
    table.setItem(row, 1, QTableWidgetItem())
    table.setItem(row, 2, QTableWidgetItem())
    table.setItem(row, 3, checkbox())

def remove_rows(table):
    for item in table.selectedItems():
        table.removeRow(item.row())

def get_all(table):
    res = []
    for row in range(table.rowCount()):
        name, title, icon = table.item(row, 0).text(), table.item(row, 1).text(), table.item(row, 2).text()
        visible = table.item(row, 3).checkState() == Qt.Checked
        res.append(dict(name=name, title=title, icon=icon, visible=visible))
    return res