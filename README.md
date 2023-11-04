# iOS Battery Analytics

This Python script allows you to see the real battery capacity percentage and cycle count of your iPhone based on its Analytics data from iOS. 

## Usage

1. Clone this repository.
2. Get the latest Analytics data from your iPhone in Settings > Privacy > Analytics & Improvements > Analytics Data (Take the file with the most recent date and which starts with "Analytics-XXXX-XX-XX-...).
3. Share it with your computer and put it in the same folder as the script.
4. Run the script in a terminal window: `python real_battery_stats.py name_of_your_Analytics_file`.
5. The script will output the real battery capacity percentage of your iPhone.

## How it works

The script reads the battery data from the analytics file created by IOS. It gets the original maximum battery capacity and the current battery capacity of your iPhone. It then calculates the real battery capacity percentage : 100*current/original.

## Requirements

- Python
- Analytics enabled on your iPhone (Settings > Privacy > Analytics & Improvements > Share iPhone Analytics)

## Acknowledgements

This script is based on the following shortcut developed by DAVID LYNCH available [here](https://www.payetteforward.com/shortcut-check-your-iphones-battery-cycle-count/)

