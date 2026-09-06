# AGENTS.md

## Project

Employee shift data management app (`data_perusahaan`). Tech stack: Python/Flask backend, CSS/JS/Bootstrap frontend, Firebase database, Vercel hosting.

## Project Rules (from plan.md)

- **Max 50 lines per file** — split code aggressively
- Function names must match their primary function
- Frontend: reusable component structure
- Core logic → `controller/`, DB models → `models/`, templates → `templates/` (matching endpoints)
- Entry point: `main.py`

## Project Structure

```
main.py          # Entry point
controller/      # App logic
models/          # Database logic / data types
templates/       # Frontend templates
wireframe/       # HTML reference designs (NOT implementation)
```

## Setup

```bash
python -m venv env
env\Scripts\activate   # Windows
pip install flask
```

## Running

```bash
flask --app main run --debug --port 5000
```

## Frontend Reference

Wireframes in `wireframe/` are **reference designs only** — they use Tailwind but the actual implementation must use **Bootstrap**. Convert Tailwind classes to Bootstrap equivalents when building templates.

### Wireframe Pages (4 modules)

| Folder | Page | Route hint |
|---|---|---|
| `master_roster_jadwal_shift/` | Master Roster / Jadwal Kerja & Shift | `/roster` |
| `pengajuan_tukar_shift/` | Pengajuan Tukar Shift (swap requests) | `/tukar-shift` |
| `pengaturan_master_shift/` | Pengaturan Master Shift (config) | `/master-shift` |
| `rekap_presensi_lembur/` | Rekap Presensi & Lembur (attendance/overtime) | `/rekap` |

Additional assets: `shiftmaster_logo/` (SVG logo), `sistem_penjadwalan_kerja_enterprise/DESIGN.md` (design tokens).

### Design Tokens (from DESIGN.md)

Use these exact values when building templates:

- **Font:** Source Sans 3 (400/600/700)
- **Primary:** `#0059bb` — action drivers, active tabs, CTAs
- **Tertiary:** `#006574` — secondary actions, accent
- **Error:** `#ba1a1a` — alerts, understaffed warnings
- **Surface bg:** `#f7f9ff`, card bg: `#ffffff`, border: `#c1c6d7`
- **Border radius:** `0.25rem` (cards), `0.125rem` (inputs), full (badges/chips)
- **Shift color coding:** Pagi=`#0059bb`, Siang=`#008093`, Malam=`#2b3137`, Off=`#dde3eb`
- **Spacing scale:** `spacer-1`=4px, `spacer-2`=8px, `spacer-3`=16px, `spacer-4`=24px

### Bootstrap Conversion Notes

- Wireframe uses utility classes (e.g. `flex`, `rounded`, `shadow-sm`) → use Bootstrap equivalents
- Modals in wireframes are vanilla JS toggle → use Bootstrap Modal component
- Tables use sticky columns → use Bootstrap `table-responsive` + custom CSS for pinned columns
- Badges/chips use inline color coding → map to Bootstrap badge/bg utility classes

## Conventions

- Use Flask blueprints to keep files under the 50-line limit
- Firebase is the database — no SQLAlchemy/ORM needed
- Reference skill: `skill.md` (Flask patterns and examples)
- Hosted on Vercel — check `vercel.json` for routing config when it exists
- Templates match routes: `templates/roster.html`, `templates/tukar-shift.html`, etc.
