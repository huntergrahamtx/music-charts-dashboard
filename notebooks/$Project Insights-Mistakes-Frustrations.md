2025-06-17 4:29 PM


Tags: [[personal projects]] [[music dashboard project]] #programming 

## **Insights**

### 10/2/2025
- After finally completing the A-Z code for the Artist data portion of the project, looking back using pseudocode was helpful and worth the effort, but didn't replace being in an IDE like VS Code where I could iteratively run actual Python. Next time I'd prefer to build out a project with pseudocode or actual Python code with dummy variables, rather than do it in a text editor-style environment like Obsidian.
### 8/28/2025
- The JSON response from Spotify's  `Search_For_Item()` call (wrapped within `spotipy`'s `spotipy.search()` method) contains everything I thought I'd need to get in further steps - `popularity`, the artist/track image URL, and the `id` - so I'm going to work on cutting out those steps and having all those items retrieved in one step.
### 7/16/2025
- After a lot of testing, the Excalidraw community plugin for Obsidian, a mindmapping plugin, is definitely superior to Obsidian's native Canvas feature, which is much more limiting. I played around and spent too much time going back and forth between the two to build out the Data Flow visual, but I'm really happy with how it turned out, at least for a first pass, in Excalidraw; I wouldn't have been able to make it look so clean in Canvas.
### 6/26/2025
- I am thoroughly enjoying Obsidian and its Canvas note type for visualization the project coming together. I wouldn't be surprised if multiple canvases are made. I wish I had used this software sooner!

### 6/17/2025
- I need to start taking more notes on my thoughts/feelings/insights/mistakes throughout this project's journey, not only to help me learn better, but also for:
	- posterity's sake, so that I can retain the lessons in the future
	- show potential employers more about how I think
	- using Obsidian more extensively through additional note-taking. I'm committing to using Obsidian for at least the next 12 months, because I hear that it's not until you start accumulating significant amounts of notes that you start seeing it's true potential in helping you learn (I hope that's correct...)
- I really wanted to incorporate genre tagging but last.fm's tag system is very imperfect for what I want to do (there's no hierarchy, namely). I'm going to do more research on what could replace it, but I might just drop genre tagging altogether. 
- I just noticed that there's an "unofficial" API for YouTube Music via a Python library, and there might be some useful features or complement or replace existing ones I've sketched out.

## **Decisions**

### 9/30/2025 
- In order to publish a completed product (as part of the greater scope of the project), the Power BI dashboard will have to run as an artist-only dashboard for right now. Track data will be added in the coming weeks.

### 7/16/2025
- Using Excalidraw, not Canvas, for all visual sketching go-forward

### 7/9/2025
- Viewing Top Releases as a feature unfortunately needs to be abandoned as the YouTube Music API doesn't have a Top Releases chart. As much as I wanted to included this feature it's not critical to the project and I need to move on.

### 6/17/2025
- Abandoned genre tagging with last.fm. Too unreliable (last.fm tagging), no evidence that it's well-correlated with Spotify's popularity metric. The juice ain't worth the squeeze for this feature, at least as of now.

## **Struggles/Frustrations**
### 7/31/2025
- I accidentally committed the file containing my API keys to the repo...rookie mistake.

### 7/9/2025
- The `ytmusicapi` library is great but YouTube Music itself is limiting only top artists by country or globally for free; a YouTube Music Premium subscription is required to fetch the songs. I don't mind paying $15 for the next few months for the project, but my intention was to have this project live as long as possible. So, a decision needs to be made about how to music forward, and time is of the essence.

## **Mistakes**

### 9/25/2025
- I spent hours thinking I need to have Google Cloud API authentication credentials and its flawless usage with the 'ytmusicapi' package, but after making a mistake, it's clear that this was entirely necessary just to pull public charts data.
### 6/25/2025
- I wish I committed to GitHub earlier!






## Connected Notes / References
[[$Development Notes]]
[[$Project Log]]

