from PyQt6.QtWidgets import QFrame, QFormLayout, QLabel, QVBoxLayout, QWidget


class PrefetchPanel(QWidget):
    def __init__(self, prefetch_data: dict, executable: str, parent=None):
        super().__init__(parent)
        self.prefetch_data = prefetch_data
        self.executable = executable
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        frame = QFrame()
        frame.setObjectName("panel")
        panel_layout = QVBoxLayout(frame)

        header = QLabel("Prefetch Analysis - EVIDENCE.EXE")
        header.setStyleSheet("font-weight:bold;")
        panel_layout.addWidget(header)

        form = QFormLayout()
        form.addRow("Executable Name:", QLabel(self.executable.upper()))
        form.addRow("Prefetch File:", QLabel(self.prefetch_data["file"]))
        form.addRow("Run Count:", QLabel(str(self.prefetch_data["run_count"])))
        form.addRow("Last Run Time:", QLabel(self.prefetch_data["last_run"]))
        form.addRow("Prefetch Path:", QLabel(self.prefetch_data["path"]))
        form.addRow("File Size:", QLabel(self.prefetch_data["file_size"]))
        panel_layout.addLayout(form)

        status = QLabel("Evidence of Execution: FOUND (Post-Deletion)")
        status.setObjectName("statusPositive")
        panel_layout.addWidget(status)

        layout.addWidget(frame)
