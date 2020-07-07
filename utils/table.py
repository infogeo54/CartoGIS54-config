from qgis.PyQt.QtWidgets import QLabel, QCheckBox

def create_label_item(title):
    return QLabel(title)

def create_checkbox_item():
    return QCheckBox()

def create_row(field):
    return dict(
        label=create_label_item(field["name"]),
        checkbox_hidden=create_checkbox_item(),
        checkbox_disabled=create_checkbox_item()
    )


def create_rows(fields):
    return list(map(lambda f: create_row(f), fields))


def fill_table(table, fields):
    rows = create_rows(fields)
    for index, row in enumerate(rows):
        table.setCellWidget(index, 0, row["label"])
        table.setCellWidget(index, 1, row["checkbox_disabled"])
        table.setCellWidget(index, 2, row["checkbox_hidden"])