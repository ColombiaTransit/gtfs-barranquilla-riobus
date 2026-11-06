# Barranquilla RíoBus — GTFS

Open-source research and reproducible GTFS production for the **RíoBus Karakalí** river service in Barranquilla, Colombia.

**Status: research / pre-release.** No timetable or route geometry has yet been verified sufficiently to publish a static GTFS feed. This repository deliberately distinguishes the current tourist cruise from historical proposed or operated river connections.

## Repository structure

- `docs/research-register.md` — evidence, assumptions and open questions.
- `data/` — reviewed input data (no invented geometry).
- `scripts/` — GTFS generator and validation helpers, to be implemented after data review.
- `.github/workflows/` — validation and release automation, to be added when a reproducible feed exists.

## Proposed feed

- Fixed release asset name: `gtfs-barranquilla-riobus.zip`
- Route mode: water transport, subject to a compatible GTFS route type decision.
- Operating model: subject to verification of boarding location, trip pattern, calendar and river geometry.

## Data quality policy

Do not fabricate a route shape, boarding coordinates, or timetable. Document published information and explicitly label model assumptions. Run the MobilityData GTFS Validator before publishing a release.

## Source references

See [the research register](docs/research-register.md).
