from qgis.PyQt.QtWidgets import QTableWidgetItem

def add_row(table):
    row = table.rowCount()
    table.setRowCount(table.rowCount() + 1)
    table.setItem(row, 0, QTableWidgetItem())
    table.setItem(row, 1, QTableWidgetItem())

def remove_rows(table):
    for item in table.selectedItems():
        table.removeRow(item.row())

def query_params(table):
    res = []
    for row in range(table.rowCount()):
        key, value = table.item(row, 0).text(), table.item(row, 1).text()
        res.append(dict(key=key, value=value))
    return res