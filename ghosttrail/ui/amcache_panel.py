from PyQt6.QtWidgets import QFrame, QFormLayout, QLabel, QVBoxLayout, QWidget


class AmcachePanel(QWidget):
    def __init__(self, amcache_data: dict, parent=None):
        super().__init__(parent)
        self.amcache_data = amcache_data
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        frame = QFrame()
        frame.setObjectName("panel")
        panel_layout = QVBoxLayout(frame)

        header = QLabel("Amcache Analysis - Amcache.hve")
        header.setStyleSheet("font-weight:bold;")
        panel_layout.addWidget(header)

        form = QFormLayout()
        form.addRow("Program Name:", QLabel(self.amcache_data["program_name"]))
        form.addRow("Original Path:", QLabel(self.amcache_data["original_path"]))
        form.addRow("File Size:", QLabel(self.amcache_data["file_size"]))
        form.addRow("First Seen:", QLabel(self.amcache_data["first_seen"]))
        form.addRow("Timestamp:", QLabel(self.amcache_data["timestamp"]))
        form.addRow("SHA-1 Hash:", QLabel(self.amcache_data["sha1"]))
        form.addRow("Entry Type:", QLabel(self.amcache_data["entry_type"]))
        panel_layout.addLayout(form)

        status = QLabel("Persistent Metadata Captured in Amcache")
        status.setObjectName("statusPositive")
        panel_layout.addWidget(status)

        layout.addWidget(frame)
