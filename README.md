# Impact of Game Updates on Player Retention

## Project Overview
This project, undertaken by Dana, Chance, and Nathan, explores the impact of game updates on player retention and sentiment. We analyzed various games, focusing on the relationships between update frequency, content types, and player activity levels. The primary objective was to understand how updates influence player behavior and engagement across different games.

## Challenges Faced
One of the main challenges was gathering and integrating data from various sources to form a cohesive dataset. We had to scrape data, interpret update logs, and handle inconsistencies in the data formats.

### Future Enhancements
- **Direct Feed with STEAMAPI**: Establish a direct feed to store daily player counts and updates to streamline the data collection process.
- **Granular Player Stats**: Analyze more granular player statistics, such as character choices, to derive deeper insights.

## Major Questions and Analysis

### 1. General Impact of Updates on Player Retention
- **Findings**: Major updates typically result in an increase in player count in the days and weeks following the update. This is evident from the red dots in the plot, indicating major updates, which are often followed by a noticeable rise in average players.
- **Conclusion**: Player retention shows a significant increase immediately after major updates, suggesting that players return to the game to explore new content or changes.

### 2. Frequency of Updates and Player Activity
- **Update Frequency**: The data reveals that periods with more frequent updates (e.g., monthly) correlate with higher player activity levels. In the plot, we observe a steady increase in average players during periods with regular updates.
- **Engagement**: More frequent updates are associated with sustained player engagement between updates, as players are consistently drawn back to the game for new content or fixes.

### 3. Types of Updates and Their Effectiveness
- **New Content vs. Bug Fixes**: Major updates introducing new content have a more significant impact on player retention compared to minor updates or bug fixes. The plot demonstrates that player counts increase more substantially after major updates (red dots) than in months with no or minor updates (orange dots).
- **Long-term Engagement**: Updates that bring substantial new content tend to sustain long-term player engagement better than minor updates or bug fixes.

### 4. Comparative Analysis Across Multiple Games
- **Trends Comparison**: The plots for *The Isle*, *ARK: Survival Evolved*, and *No Man's Sky* show player retention trends across these games. Observing these trends reveals that frequent updates generally have a positive effect on player counts across different games.
- **Effectiveness of Updates**: By comparing the plots, we observe that the patterns of increased player engagement following major updates and frequent updates hold true across all the games analyzed. This helps us understand that frequent updates and major content releases universally lead to higher player retention across different games.

## Conclusion
The analysis indicates that major updates have a positive impact on player retention and engagement. Frequent updates, especially those introducing new content, are key to maintaining player activity levels. Comparative analysis across multiple games further validates these findings and provides deeper insights into update strategies that work best for player retention.

## Contributions
- **Dana**: Located update data, scraped player count data, cleaned update data, merged datasets, and created time series plots using DARTS.
- **Nathan**: Gathered review information, cleaned and analyzed it, providing unique insights into the games.
- **Chance**: Compared basic update data with scraped player count data, performed preliminary analysis on the relationships, and created the slideshow presentation.

## Lessons Learned
- **Data Gathering Challenges**: Obtaining and preparing data from multiple sources is complex and time-consuming. Specifically, update logs were difficult to interpret and not always clear or easily scrapeable.

## Credits
We extend our gratitude to the following resources for their data and support:

### Data Sources
- **The Isle**:
  - [The Isle Steam Charts](https://steamcharts.com/app/376210)
  - Steam API update history and reviews
- **Ark: Survival Evolved**:
  - [Ark: Survival Evolved Steam Charts](https://steamcharts.com/app/346110)
  - [Ark Update Logs](https://survivetheark.com/index.php?/forums/topic/166421-archived-pc-patch-notes/)
  - Steam API reviews
- **No Man's Sky**:
  - [No Man's Sky Steam Charts](https://steamcharts.com/app/275850)
  - Steam API update history and reviews
  - [No Man's Sky Update Logs](https://www.nomanssky.com/release-log/)

### Tools and Support
- **Sonnet 3.5 and ChatGPT**: For process support, debugging, and educational assistance throughout the project.

Thank you for reviewing our project. We hope our findings provide valuable insights into the impact of updates on player retention and sentiment.