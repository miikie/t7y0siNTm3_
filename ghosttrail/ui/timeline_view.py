from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)


class TimelineView(QWidget):
    def __init__(self, data: dict, parent=None):
        super().__init__(parent)
        self.data = data
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        banner = QLabel("START (T=0) -> EXECUTION -> DELETION (T=4s)")
        banner.setObjectName("banner")
        banner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(banner)

        content = QHBoxLayout()
        layout.addLayout(content)

        left_panel = self._create_left_panel()
        right_panel = self._create_right_panel()
        content.addWidget(left_panel)
        content.addWidget(right_panel)

    def _create_left_panel(self):
        panel = QFrame()
        panel.setObjectName("panel")
        left_layout = QVBoxLayout(panel)

        explorer_label = QLabel("Simulated Windows Explorer\nC:\\Users\\Public\\Downloads")
        explorer_label.setStyleSheet("font-weight:bold;")
        left_layout.addWidget(explorer_label)

        files = QListWidget()
        files.addItems(["Desktop", "Documents", "Security", "Tasktop", "Evidence.exe"])
        left_layout.addWidget(files)

        ps_label = QLabel("PowerShell Console")
        ps_label.setStyleSheet("font-weight:bold;")
        left_layout.addWidget(ps_label)

        ps_console = QPlainTextEdit()
        ps_console.setReadOnly(True)
        ps_console.setPlainText(
            'Start-Process -FilePath ".\\evidence.exe"\n'
            "evidence.exe starting... [PROCESS ID: 1234]\n\n"
            'Remove-Item -Path ".\\evidence.exe"\n'
            "evidence.exe removed successfully."
        )
        left_layout.addWidget(ps_console)

        return panel

    def _create_right_panel(self):
        panel = QFrame()
        panel.setObjectName("panel")
        right_layout = QVBoxLayout(panel)

        label = QLabel("Post-Activity Explorer Snapshot\nC:\\Users\\Public\\Downloads")
        label.setStyleSheet("font-weight:bold;")
        right_layout.addWidget(label)

        files = QListWidget()
        files.addItems(["Desktop", "Documents", "Security", "Tasktop"])
        right_layout.addWidget(files)

        overlay1 = QLabel("Post-Activity State - Evidence Missing")
        overlay1.setObjectName("statusWarning")
        overlay2 = QLabel("Post-Activity: File Deleted")
        overlay2.setObjectName("statusWarning")
        right_layout.addWidget(overlay1)
        right_layout.addWidget(overlay2)

        return panel
