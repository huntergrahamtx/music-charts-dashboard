2025-05-30 15:43

Tags: [[music dashboard project]] [[databases]]

## Tables
### `artist`
**`artist`** table

| attribute          | datatype               |
| ------------------ | ---------------------- |
| spotify_artist_id  | char **PK**            |
| week_ending        | date **PK**, **FK**    |
| country            | char(2) **PK**, **FK** |
| artist_name        | char                   |
| artist_ranking     | int                    |
| artist_popularity  | int                    |
| artist_image_url   | text                   |
| artist_preview_url | text                   |


### `track`
**`track`** table

| attribute         | datatype           |
| ----------------- | ------------------ |
| spotify_track_id  | char **PK**        |
| week_ending       | date **PK, FK**    |
| country           | char(2) **PK, FK** |
| track_name        | char               |
| artist_name       | char               |
| track_ranking     | int                |
| track_popularity  | int                |
| track_image_url   | text               |
| track_preview_url | text               |

### `time`
**`time`** table

| attribute   | datatype    |
| ----------- | ----------- |
| week_ending | date **PK** |
| month       | char        |
| quarter     | char        |
| year        | char        |

### `country`

**`country`** table

| attribute    | datatype       |
| ------------ | -------------- |
| country_code | char(2) **PK** |
| country_name | char           |


## Connected Notes / References

