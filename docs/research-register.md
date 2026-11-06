# RíoBus Karakalí — research register

Last reviewed: 2026-11-06. Research status: **preliminary**. The operational claims below are leads from the previous project discussion and must be checked against current primary sources before GTFS publication.

| Topic | Preliminary information | Evidence status | GTFS implication |
| --- | --- | --- | --- |
| Service | RíoBus Karakalí, Barranquilla | Name identified in project discussion | Verify agency and route naming |
| Boarding point | Muelle Puerta de Oro, Gran Malecón | Secondary information; exact coordinates unverified | Stop point must be verified |
| Current service pattern | Tourist round trip starting and ending at Puerta de Oro | Preliminary information | Model as circular trip only if confirmed |
| Tue–Fri departures | 14:00, 17:00 | Preliminary published schedule; current validity unverified | Do not publish until verified |
| Weekend and public holiday departures | 11:00, 14:00, 17:00 | Preliminary published schedule; current validity unverified | Holiday exceptions require review |
| Mondays | Closed except public holidays | Preliminary published schedule | Confirm maintenance exceptions |
| Tuesday after holiday Monday | Closed | Preliminary published schedule | Confirm maintenance exceptions |
| Trip duration | Approximately 45 minutes | Preliminary estimate | Verify arrival time and whether 45 minutes is total loop |
| Fare | COP 15,000 | Preliminary published figure | Confirm if publishing fares |
| Historic river connection | Puerta de Oro–Intendencia Fluvial | Historical references | Do not conflate with current tourist loop |

## Open research tasks

1. Locate and archive current official RíoBus/Karakalí operating timetable, terms, calendar and operator.
2. Verify the exact Puerta de Oro embarkation point (coordinates, OSM features, signage).
3. Determine actual cruise route/turnaround geometry using official maps, OSM, GPX or other defensible geospatial data.
4. Verify whether a second boarding point or historical route is currently active.
5. Confirm vessel capacity and service duration if useful for metadata.
6. Decide GTFS route_type for water transport, implement reproducible generator, and validate with MobilityData.
7. Publish a versioned GitHub Release with a fixed asset name `gtfs-barranquilla-riobus.zip`.

## GTFS modeling principles

A round trip may use the same stop as first and last stop with increasing stop_sequence and distinct times. Do not invent intermediate stops. A shape must follow an evidenced navigable river path; do not reuse the historical point-to-point alignment without verification.

## Source leads (not yet verified for currency)

- Barranquilla tourism / Gran Malecón official publications
- RíoBus Karakalí operator announcements
- Historic Puerta de Oro–Intendencia Fluvial articles

All operational times remain provisional until the cited source material is captured and reviewed.

## Municipal evidence — Karakalí tourist operation (2023)

- **Source:** [Alcaldía de Barranquilla — RíoBús: Karakalí](https://barranquilla.gov.co/funcionarios/riobus-karakali), published **2023-10-25**.
- **Confirmed by source:** municipal employees took a Karakalí cruise on the Magdalena River; the article describes a guided sightseeing experience, music, traditional dances and wildlife observation.
- **Interpretation:** evidence of an actual tourism-oriented cruise in October 2023, distinct from the 2022 planned point-to-point service.
- **Not provided:** precise pier, itinerary/track, timetable, trip duration, fares, or proof of the current 2026 operating pattern.
- **GTFS use:** historical service context only; no new stop, trip or shape may be generated from this article alone.

## Municipal evidence — initial fare and intended route (2023-11-09)

- **Primary source:** [Alcaldía de Barranquilla — El RioBús Karakalí ya tiene su tarifa inicial definida](https://barranquilla.gov.co/funcionarios/el-riobus-karakali-ya-tiene-su-tarifa-inicial-definida), published **2023-11-09**.
- **Initial announced fare:** **COP 6,000** for the RíoBus journey. This is a historical launch fare, not evidence of the current fare.
- **Intended route:** embark at **Muelle Puerta de Oro / Gran Malecón** and connect to **Intendencia Fluvial** in central Barranquilla.
- **Operational context:** the mayor reported dredging of the canal to permit entry to Intendencia and comfort improvements following initial user feedback; the service was described as about to start operating.
- **Service characterization:** initially a tourist ride, with a longer-term sustainable water-transport ambition.
- **Evidence limitation:** this article does **not** establish a present-day operating route, departures, arrival times, current ticket price, or navigable shape. Do not create current GTFS trips or fares solely from it.
- **Research consequence:** keep the historic/planned Puerta de Oro–Intendencia connection separate from any verified contemporary tourist loop.
