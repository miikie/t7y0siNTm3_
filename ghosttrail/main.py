import json
import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QTabWidget, QVBoxLayout, QWidget

from ui.amcache_panel import AmcachePanel
from ui.powershell_panel import PowerShellPanel
from ui.prefetch_panel import PrefetchPanel
from ui.srum_panel import SrumPanel
from ui.timeline_view import TimelineView


class GhostTrailWindow(QMainWindow):
    def __init__(self, scenario: dict):
        super().__init__()
        self.scenario = scenario
        self.setWindowTitle("GhostTrail Monitor – Specialized Forensic Software")
        self.resize(1220, 760)
        self._build_ui()

    def _build_ui(self):
        tabs = QTabWidget()
        tabs.addTab(self._scenario_timeline_tab(), "View 1 - Scenario Timeline")
        tabs.addTab(self._core_artifacts_tab(), "View 2 - Core Execution Artifacts")
        tabs.addTab(self._supplementary_artifacts_tab(), "View 3 - Supplementary Correlation")
        self.setCentralWidget(tabs)

    def _scenario_timeline_tab(self):
        return TimelineView(self.scenario)

    def _core_artifacts_tab(self):
        container = QWidget()
        layout = QVBoxLayout(container)

        title = QLabel("Core Execution Artifacts (Prefetch & Amcache Analysis)")
        title.setObjectName("banner")
        layout.addWidget(title)

        row = QHBoxLayout()
        row.addWidget(PrefetchPanel(self.scenario["prefetch"], self.scenario["executable"]))
        row.addWidget(AmcachePanel(self.scenario["amcache"]))
        layout.addLayout(row)
        return container

    def _supplementary_artifacts_tab(self):
        container = QWidget()
        layout = QVBoxLayout(container)

        title = QLabel("Supplementary & Procedural Artifacts (PowerShell Logs & SRUM)")
        title.setObjectName("banner")
        layout.addWidget(title)

        layout.addWidget(PowerShellPanel(self.scenario["powershell"]))
        layout.addWidget(SrumPanel(self.scenario["srum"]))
        return container


def load_scenario(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_stylesheet(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()


def main():
    base_dir = Path(__file__).resolve().parent
    scenario_path = base_dir / "data" / "scenario.json"
    css_path = base_dir / "assets" / "theme.css"

    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet(css_path))

    window = GhostTrailWindow(load_scenario(scenario_path))
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
