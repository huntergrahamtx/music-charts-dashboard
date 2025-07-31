
Tags: [[personal projects]] [[music dashboard project]] #programming 

## **Project Log**

#### 7/31/2025
- designed the basic data structure to be used for holding all data through the ETL process (dictionary per country, list of dictionaries for each record)
- built more pseudocode for the ETL process

#### 7/30/2025
- built more pseudocode for the ETL process
	- sketched out data structures for the ETL process - what kind to use, and where

#### 7/29/2025
- updated datatypes for tables in the database schema outline to reflect SQLite datatypes 
- built Time table in Excel and converted to .csv to be imported into the database
- created test data for each table to be ready for importation via .csv files
#### 7/24/2025
- Set up and obtained Google API credentials
- Starting documenting technical process for SQLite database
- Started building out test database (for MVP run)
#### 7/21/2025
 - Added `spotify_artist_id` foreign key to `track` table in database
	 - Added relationship in SQLite Schema visual in [[@Data Flow visual]]
#### 7/17/2025
- Polished [[@Data Flow visual]]
	- condensed entities
	- straightened and aligned boxes

#### 7/16/2025
- Finished [[@Data Flow visual]]
- Finished first draft of the database schema
#### 7/15/2025
- Started an ETL process visual

#### 7/9/2025
- Researched the `ytmusicapi` Python library and its capabilities. 
	- Unfortunately, a YouTube Music Premium subscription is going to be required to get song titles from global and by-country charts, and
	- Only artists and their standings will be able to be returned without a Premium subscription
- <font color="#00b050"> So obviously the question is, do I move forward using these limitations or reduce the scope of the dashboard?</font>
	- I think getting the top tracks is a pretty critical part of the dashboard and thus a subscription is going to have to be needed for a couple months to at least get some solid data to store
- 'Top Releases' as a feature dropped from the scope of the project - not feasible from data sources, and project needs to move on
- Confirmed the exact API calls and responses in the context of inputs and outputs for the dashboard. Theoretically, everything makes sense so far from a systems standpoint.

#### 6/26/2025
- made extensive additions to the [[Data Sources visual.canvas|Data Sources visual]] map
- found and used community plugins to enhance readability and design of the map
#### 6/25/2025 
- finally made the initial commit to GitHub
#### 6/23/2025
- started project outline on Canvas
- decided to separate out API notes into their own (atomic) notes for each call I want, so that they can be linked more efficiently and better visually
#### 6/18/2025
- finished dashboard concept - we'll call it the first draft
	- added track/release art space
	- moved some visualizations around
	- added a basic color scheme (white for headers, beige-yellow for values)
- **need to start pushing Git commits!**
#### 6/17/2025
- decided pursuing last.fm's genre tags wasn't going to be worth it. [[$Project Insights-Mistakes-Frustrations]]
- finished most of the dashboard's initial visual concept
#### 6/12/2025
- made an outline of visualizations and features for dashboard using other music streaming services' as inspiration
- explored MusicBrainz API and capability for enhancing the dashboard (namely artist country origin)

## **Backlog**

<span style="background:#fff88f">Use</span> #todo <span style="background:#fff88f">!</span>

- [ ] build test SQLite database in Python
	- [x] ~~build Time table in Excel and convert to .csv for import~~
- [ ] confirm pseudocode looks/sounds good
	- [x] ~~step [[1. Create and prepare data structure for the API calls and responses]]~~
	- [x] ~~step [[2. Make Get_Charts() YouTube Music API call and parse responses]]~~
	- [ ] step [[3. Search For Item() Spotify API Calls]]
	- [x] ~~step [[4. Get Track(), Get Artist() Spotify API Calls]]~~
	- [x] ~~step [[5. Assemble all stored API responses for insertion into the database]]~~
	- [ ] step [[6. Validate All API Responses]]
	- [ ] step [[7. Load assembled data into the database]]
	- [ ] step [[8. Query and ready data for the dashboard]]
- [ ] run Python script queries against test database
- [ ] move on to ETL scripts afterwards
- [x] ~~finish SQLite note [[__SQLite Notes]]~~
- [x] ~~adjust [[_SQLite Schema]] datatypes to reflect SQLite datatypes~~
- [x] ~~start building out first code snippet~~
- [x] ~~obtain YouTube Music API authorization credentials~~
- [x] ~~build technical map of how the APIs will be joined within visualizations~~
- [x] ~~build out database schema for storing API responses~~
- [x] ~~explore the 'ytmusicapi' Python library more and see if it'd be a net positive for the project ([sigma67/ytmusicapi: Unofficial API for YouTube Music](https://github.com/sigma67/ytmusicapi))~~
- [x] ~~sketch technical diagram of dashboard~~
- [x] ~~install last.fm~~
- [x] ~~take notes on last.fm API~~









## Connected Notes / References

[[_Project Scope]]
