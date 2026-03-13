from PyQt6.QtWidgets import (
    QFrame,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class PowerShellPanel(QWidget):
    def __init__(self, ps_data: dict, parent=None):
        super().__init__(parent)
        self.ps_data = ps_data
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        frame = QFrame()
        frame.setObjectName("panel")
        panel_layout = QVBoxLayout(frame)

        header = QLabel("Event ID 4104 - Script Block Logging")
        header.setStyleSheet("font-weight:bold;")
        panel_layout.addWidget(header)

        table = QTableWidget(1, 4)
        table.setHorizontalHeaderLabels(["Time", "EventID", "Source", "Message"])
        table.verticalHeader().setVisible(False)
        table.setAlternatingRowColors(True)
        row = [
            self.ps_data["event_time"],
            str(self.ps_data["event_id"]),
            self.ps_data["source"],
            self.ps_data["message"],
        ]
        for col, value in enumerate(row):
            table.setItem(0, col, QTableWidgetItem(value))
        table.resizeColumnsToContents()
        panel_layout.addWidget(table)

        decoded = QTextEdit()
        decoded.setReadOnly(True)
        decoded.setText("\n".join(self.ps_data["decoded_script"]))
        panel_layout.addWidget(decoded)

        annotation = QLabel("Payload Downloaded and Executed")
        annotation.setObjectName("statusWarning")
        panel_layout.addWidget(annotation)

        layout.addWidget(frame)
