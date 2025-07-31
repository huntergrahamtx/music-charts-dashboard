2025-07-30 12:18 PM

Tags: [[music dashboard project]] [[Python]] [[Programming]]

## ETL Scripts

**API response data template**

```python
api_data = {
	"[country]": { #TODO note placeholder variable
		"week_ending": week_ending_date,
		"tracks": [
			{
				"spotify_track_id": None,
				"week_ending": week_ending_date,
				"country_code": current_country_code,
				"spotify_artist_id": None,
				"track_name": None,
				"artist_name": None,
				"track_ranking": None,
				"track_popularity": None,
				"track_image_url": None,
				"track_preview_url": None
			}
			# loop x10 #TODO
		],
		"artists": [
			{
				"spotify_artist_id": None,
				"week_ending": week_ending_date,
				"country_code": current_country_code,
				"artist_name": None,
				"artist_ranking": None,
				"artist_popularity": None,
				"artist_image_url": None,
				"artist_preview_url": None
			}
			# loop x10 #TODO
		]
	}
}
```




## Connected Notes / References
[[1. Create and prepare data structure for the API calls and responses]]
