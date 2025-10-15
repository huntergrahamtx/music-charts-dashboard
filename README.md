## Music Charts Dashboard
This project is an end-to-end analytics pipeline and dashboard that tracks weekly global music trends. It combines YouTube Music’s weekly Top 10 artist charts with Spotify artist metadata to create a richer, unified dataset supported by interactive visualizations.

[**View the dashboard here.**](https://app.powerbi.com/view?r=eyJrIjoiODc5OTQyOWQtMTkzZS00NjI5LTlmM2YtMDVkNGEyODA1ZDZkIiwidCI6IjY4ZjM4MWUzLTQ2ZGEtNDdiOS1iYTU3LTZmMzIyYjhmMGRhMSIsImMiOjN9)


  
## How it works
1. **Extract:** Python code calls the YouTube Music API to pull the top 10 artists per country each week, then enriches that data with Spotify’s API (artist ID, popularity score, images, preview links) to build out a more comprehensive view of top artists.
2. **Transform & Validate:** Records are normalized, checked for proper diacritic representation (accent marks and related) in artist names, and logged to ensure transparent data processing.
3. **Load:** Data is stored in a normalized SQLite schema with tables for artists, countries, and time.
4. **Visualize:** The data is transformed further via Power Query in Power BI into a proper star schema. A dashboard pulls the data to show:
   - Global and Country-level Top 10 artists by stream volume
   - Week-over-week changes in artist popularity
   - Global and Country-level trending artists by popularity
   - Top Artist image and their recent popularity history  
  
## Project Latest
#### Current Progress as of 10/2/2025
- Completed A-Z data processing for Artist data
- Artist music dashboard iteration #1 completed and published  

#### Next Step
- Build the "driver" script to automate project code weekly

