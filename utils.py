from db import get_all_patients,get_daily_summary
from models import format_patient_row
from pathlib import Path
import json
def export_daily_report_txt(path="daily_report.txt"):
    rows=get_daily_summary()
    lines=[]
    lines.append("Daily OPD Summary")
    lines.append("=================")
    for r in rows:
        lines.append(f"Department: {r['department']}, Total: {r['total']}, Consulted: {r['consulted']}")
    Path(path).write_text("\n".join(lines))
    return path

def export_patients_json(path="patients_export.json"):
    rows=get_all_patients()
    out=[format_patient_row(r) for r in rows]
    Path(path).write_text(json.dumps(out,indent=2,default=str))
    return path
