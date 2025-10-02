2025-05-30 15:43

Tags: [[music dashboard project]] [[databases]] 

## **Tables**
### `artist`
**`artist`** table

| attribute          | datatype              |
| ------------------ | --------------------- |
| spotify_artist_id  | `TEXT` **PK**         |
| week_ending        | `TEXT` **PK**, **FK** |
| country_code       | `TEXT` **PK**, **FK** |
| artist_name        | `TEXT`                |
| artist_rank        | `INTEGER`             |
| artist_popularity  | `INTEGER`             |
| artist_image_url   | `TEXT`                |
| artist_preview_url | `TEXT`                |


### `track`
**`track`** table

| attribute         | datatype          |
| ----------------- | ----------------- |
| spotify_track_id  | `TEXT` **PK**     |
| week_ending       | `TEXT` **PK, FK** |
| country_code      | `TEXT` **PK, FK** |
| spotify_artist_id | `TEXT` **FK**     |
| track_name        | `TEXT`            |
| artist_name       | `TEXT`            |
| track_rank        | `INTEGER`         |
| track_popularity  | `INTEGER`         |
| track_image_url   | `TEXT`            |
| track_preview_url | `TEXT`            |

### `time`
**`time`** table

| attribute   | datatype      |
| ----------- | ------------- |
| week_ending | `TEXT` **PK** |
| month       | `INTEGER`     |
| quarter     | `INTEGER`     |
| year        | `INTEGER`     |


<span style="background:#fff88f">^convert 'week_ending' values to *YYYY-MM-DD* to keep things easy for longevity</span>

### `country`

**`country`** table

| attribute    | datatype      |
| ------------ | ------------- |
| country_code | `TEXT` **PK** |
| country_name | `TEXT`        |


## Connected Notes / References

