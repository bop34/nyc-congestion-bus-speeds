# Congestion Pricing and NYC Bus Speeds

How far beyond the toll zone did NYC congestion pricing speed up buses, and did the gains last?


## Background

On January 5, 2025, New York City began charging a toll for vehicles entering Manhattan south of 60th Street, known as congestion pricing. The toll is highest during peak hours (weekdays 5am–9pm, weekends 9am–9pm) and reduced overnight.

The MTA has reported that buses inside the zone got faster. This project looks at how far beyond the zone the speedup reached, and whether it lasted.

## Data

The MTA publishes average bus travel times and speeds for every route segment on data.ny.gov, split across two datasets:

| Dataset                                      | Covers                              | Link                            |
|----------------------------------------------|-------------------------------------|---------------------------------|
| MTA Bus Route Segment Speeds: 2023–2024      | Jan 2023 – Dec 2024                 | https://data.ny.gov/d/58t6-89vi |
| MTA Bus Route Segment Speeds: Beginning 2025 | Jan 2025 – present, updated monthly | https://data.ny.gov/d/kufs-yh3x |

Each row is one segment, for one hour of the day and one day of the week, averaged over a month. It includes the segment's road distance (miles), average travel time (minutes), average speed (mph), and total number of bus trips across the period which the averages are based on.

The files used here were downloaded on 2026-10-17. Because the 2025 dataset grows every month, the analysis only uses data through August 2026.

## Definitions

- Timepoint: a stop the MTA uses as a timing checkpoint. Not all stops are timepoints.
- Segment: the stretch of a route between two consecutive timepoints, in one direction.

## How to reproduce

1. Clone this repository and run `uv sync` to install the environment.
2. Download both datasets above (Export → CSV → Download) and save them to `data/raw/` as `segment_speeds_2023_24.csv` and `segment_speeds_2025.csv`.
3. Run the notebooks in `notebooks/` in numbered order.

No data files are included in this repository.

## Notebooks

- `01_explore.ipynb`: checks on one route (M15) whether the two datasets can be compared segment by segment. Roughly 88% of trips are on segments present in both years. The unmatched come from a moved timepoint and a renumbered stop ID.
- `02_process.ipynb`: combines the two raw CSVs into a single parquet file of weekday peak-hour rows, from January 2023 to August 2026, leaving about 12M rows. It is relatively slow to run since it reads the full CSVs.