from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtWidgets import QFrame, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class MiniLineGraph(QWidget):
    def __init__(self, values: list[float], title: str, color: QColor, parent=None):
        super().__init__(parent)
        self.values = values
        self.title = title
        self.color = color
        self.setMinimumHeight(90)

    def paintEvent(self, event):  # noqa: N802
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rect = self.rect().adjusted(8, 22, -8, -8)

        painter.setPen(QPen(QColor("#2b466b"), 1, Qt.PenStyle.DashLine))
        painter.drawRect(rect)
        painter.setPen(QColor("#b9d5ff"))
        painter.drawText(8, 16, self.title)

        if not self.values:
            return

        max_val = max(self.values) if max(self.values) > 0 else 1
        count = len(self.values)
        points = []

        for i, value in enumerate(self.values):
            x = rect.left() + (i / max(1, count - 1)) * rect.width()
            y = rect.bottom() - (value / max_val) * rect.height()
            points.append(QPointF(x, y))

        painter.setPen(QPen(self.color, 2))
        for i in range(len(points) - 1):
            painter.drawLine(points[i], points[i + 1])

        painter.setBrush(self.color)
        for point in points:
            painter.drawEllipse(point, 3, 3)


class SrumPanel(QWidget):
    def __init__(self, srum_data: dict, parent=None):
        super().__init__(parent)
        self.srum_data = srum_data
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        frame = QFrame()
        frame.setObjectName("panel")
        panel_layout = QVBoxLayout(frame)

        header = QLabel("SRUM Database - srudb.dat (System Resource Usage Monitor)")
        header.setStyleSheet("font-weight:bold;")
        panel_layout.addWidget(header)

        table = QTableWidget(len(self.srum_data["rows"]), 4)
        table.setHorizontalHeaderLabels(["Process Name", "CPU Usage", "Network Usage", "Start Time"])
        table.verticalHeader().setVisible(False)
        table.setAlternatingRowColors(True)

        for row_idx, row in enumerate(self.srum_data["rows"]):
            table.setItem(row_idx, 0, QTableWidgetItem(row["process"]))
            table.setItem(row_idx, 1, QTableWidgetItem(f"{row['cpu']}%"))
            table.setItem(row_idx, 2, QTableWidgetItem(f"{row['network']} KB"))
            table.setItem(row_idx, 3, QTableWidgetItem(row["start"]))

        table.resizeColumnsToContents()
        panel_layout.addWidget(table)

        panel_layout.addWidget(MiniLineGraph(self.srum_data["cpu"], "CPU Usage", QColor("#4bc0ff")))
        panel_layout.addWidget(MiniLineGraph(self.srum_data["network"], "Network Usage", QColor("#7ef7b0")))

        analysis = QLabel(
            "• Application activity entries recorded in the SRUM database\n"
            "• Application usage metadata detected\n"
            "• Possible network usage information available"
        )
        panel_layout.addWidget(analysis)

        result = QLabel("SRUM provided supplementary evidence about application usage over time.")
        result.setObjectName("statusPositive")
        panel_layout.addWidget(result)

        layout.addWidget(frame)
