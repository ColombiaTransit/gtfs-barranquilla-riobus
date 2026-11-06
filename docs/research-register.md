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

## Municipal website survey — 2026-11-06

The following sources were identified on Barranquilla's municipal websites. Current and historical operating models must not be merged.

### Current tourism service

- [Visit Barranquilla — RíoBus Karakalí](https://visit.barranquilla.gov.co/planes/karakali): Muelle Puerta de Oro, Vía 40 #79B-06; sightseeing cruise approximately 45 minutes; Tuesday–Friday departures 14:00 and 17:00; Saturday, Sunday and public holidays 11:00, 14:00 and 17:00. The page does not explicitly specify Monday service or Tuesday-after-Monday-holiday maintenance. Ticket price is marked "consult prices"; do not reuse the 2023 fare.
- [Municipal Easter 2026 announcement](https://barranquilla.gov.co/mi-barranquilla/en-semana-santa-conecta-con-mallorquin-el-rio-magdalena-y-puerto-mocho), 2026-03-31: RíoBus Karakalí expected to operate normally during Holy Week 2026; Puerta de Oro boarding confirmed.
- [Gran Malecón ninth anniversary](https://barranquilla.gov.co/obraspublicas/aniversario-del-gran-malecon-9-anos-uniendo-el-corazon-de-barranquilleros-y-visitantes-con-el-rio-magdalena), 2026-07-17: >1,900 departures and 95,580 transported people reported; departure pier Puerta de Oro.
- [2025 year-end tourism announcement](https://barranquilla.gov.co/mi-barranquilla/barranquilla-se-prepara-para-despedir-el-2025-en-sus-principales-atractivos-turisticos-conectados-con-la-naturaleza), 2025-12-27: Karakalí expected to operate on normal hours during year-end season.
- [Municipal employee excursion](https://barranquilla.gov.co/intranet/embajadores-cheveres-navegaron-en-el-riobus-karakali), 2025-08-15: evidence of actual 2025 cruises, not a timetable.

### Historical service and waterway

- [Initial commercial operation announcement](https://barranquilla.gov.co/control-disciplinario/riobus-karakali-sera-operado-por-puerta-de-oro-iniciara-con-tres-rutas-diarias-de-lunes-a-viernes), 2023-12-16: Puerta de Oro Empresa de Desarrollo Caribe identified as responsible for operation; three weekday departures planned, weekends demand-responsive; initial free period; Puerta de Oro and Intendencia Fluvial docks. This schedule is superseded for current-feed modeling by the tourism site.
- [Preparations for navigation](https://barranquilla.gov.co/secretaria-general-del-distrito/karakali-en-preparativos-logisticos-para-conectarnos-mas-con-el-rio-magdalena), 2023-07-07: AQUAMAR S.A. named as selected operator at that stage, with a planned ~7 km Puerta de Oro–Intendencia route via Los Tramposos. Relationship to later Puerta de Oro operation unresolved.
- [Dredging Los Tramposos](https://barranquilla.gov.co/mi-barranquilla/dragado-del-cano-los-tramposos-se-suma-a-reactivacion-de-la-intendencia-fluvial-y-el-cabrito), 2023-09-19: ~1.7 km channel access section to Intendencia; channel was being cleared to allow passage. Do not infer a current cruise shape from this.
- [Launch announcement](https://barranquilla.gov.co/mi-barranquilla/el-riobus-esta-listo-para-empezar-a-navegar-en-barranquilla), 2023-06-27: planned ~7 km first phase (roughly 6 km river, 1 km Los Tramposos, per article); later ambitions Puerto Mocho and Suan were not evidence of operation.

### GTFS readiness after survey

- **Confirmed for preliminary schedule model:** tourist service, Puerta de Oro pier name/address, approximate 45-minute duration, weekday/weekend/holiday departure times.
- **Requires verification:** actual precise stop coordinates, shape, calendar treatment of holiday Mondays and following Tuesdays, operator identity in 2026, and exact return-to-pier time.
- **Do not include:** historic COP 6,000 fare as current, proposed Intendencia point-to-point trips, or unverified extended routes.

## Published fare, calendar exception and current operating model (2025)

- **Source:** [Alerta — Horarios y precios del Riobus Karakalí en Barranquilla desde el 15](https://www.alerta.com.co/bolsillo/horarios-y-precios-del-riobus-karakali-en-barranquilla-desde-el-15-227528). Secondary news report concerning fare introduction on **2025-11-15**.
- **Fare:** COP 15,000 per person from 2025-11-15; children under two free. Do not use the 2023 announced COP 6,000 fare for current operation.
- **Route pattern:** sightseeing cruise **departs from and returns to Muelle Puerta de Oro**. No Intendencia Fluvial stop is identified for this operation.
- **Departure times:** Tuesday–Friday 14:00 and 17:00; Saturday, Sunday and Colombian public holidays 11:00, 14:00 and 17:00. Regular Mondays closed except holidays.
- **Calendar exception:** when Monday is a public holiday, **the following Tuesday has no service**. This is explicitly reported and should be implemented as a GTFS calendar_dates exception.
- **Operating organization:** Puerta de Oro Empresa de Desarrollo Caribe operates the cruise.
- **Fare collection:** Transmetro S.A.S. handles ticket collection; cash and Transmetro card accepted at the Puerta de Oro ticket office. Do not conflate fare collector with operator in agency.txt.
- **Ticket-office hours:** weekdays 12:00–17:00; weekends and public holidays 09:00–11:30 and 12:30–17:00. These are **ticket office** hours, not trip departure times.
- **Evidence strength:** corroborates the Visit Barranquilla published schedule and confirms the Monday-holiday maintenance exception; operational changes after publication remain possible.
- **Remaining gaps:** precise pier GPS, defensible navigation shape, verified 45-minute scheduled round-trip duration, and official current fare policy.

## Route-direction evidence — Destination Barranquilla (2026-11-06 review)

- **Source:** [Destination Barranquilla — Karakalí River Bus](https://baq.com.co/iconic-places/karakali-river-bus/). The page describes the route as **“Gran Malecón – Puerto Mocho”**, a trip *towards Puerto Mocho*, and says the river bus links Gran Malecón with the historic river port / city beach.
- **Other fields:** Puerta de Oro / Gran Malecón pier; Tue–Fri 14:00 and 17:00, weekends and holidays 11:00, 14:00 and 17:00; approximately 45 minutes; COP 15,000; children under two free; capacity 60; reduced-mobility accessibility.
- **Critical ambiguity:** This route label does **not** establish that passengers may board/alight at Puerto Mocho, nor that the trip terminates there. It conflicts in emphasis with the previously documented 2025 report of a cruise departing and returning to Puerta de Oro.
- **GTFS action:** treat Puerto Mocho as a **candidate turnaround / navigation landmark**, not a verified stop. Do not create a Puerto Mocho stop or shape based solely on this page.
- **Follow-up:** seek operator map, ticketing details or first-hand evidence confirming whether Puerto Mocho is a scheduled passenger stop or merely the cruise's direction/turning point.
- **Distinct commercial tour:** [Costa Tours Group Karakalí package](https://baq.com.co/tours/sailing-the-great-river-karakali/) advertises a two-hour hotel-pickup excursion with guide (Tue–Sat 16:00–18:00), priced separately at COP 145,000 or COP 245,000 solo. Its package duration and price **must not** replace the RíoBus's 45-minute / COP 15,000 service data.
