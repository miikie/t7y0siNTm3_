# GhostTrail Monitor

GhostTrail Monitor is a minimal PyQt6 desktop visualization project for demonstrating forensic artifact correlation after ephemeral Windows executable activity.

## Scenario
The dashboard simulates a case where `evidence.exe` is executed from `C:\Users\Public\Downloads`, then deleted seconds later, while residual artifacts remain in:

- Prefetch
- Amcache
- PowerShell Operational logs (Event ID 4104)
- SRUM (`srudb.dat`)

> This project uses static JSON data and does **not** parse real forensic artifacts.

## Project Structure

```text
ghosttrail/
  main.py
  ui/
    timeline_view.py
    prefetch_panel.py
    amcache_panel.py
    powershell_panel.py
    srum_panel.py
  data/
    scenario.json
  assets/
    icons/
    theme.css
```

## Run

1. Install dependencies:
   ```bash
   pip install PyQt6
   ```
2. Launch:
   ```bash
   python ghosttrail/main.py
   ```
