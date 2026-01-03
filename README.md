# pytime
Very simple and basic CLI tool to document your working hours written in Python.

## Capabilities
- Saves the start and end times of your working hours
- Lets you enter your (potential) break time in minutes (if you did not have a break, just enter 0)
- And saves all to "work_time.txt" in your home directory

Example content from work_time.txt:
```
Saturday, 03.01.2026
Started working: 2026-01-03 16:52:04.453577
Stopped working: 2026-01-03 16:59:04.880259
Break time: 2 minutes
Worktime: 0:05:00.426682
--------------------------------------------------
Saturday, 03.01.2026
Started working: 2026-01-03 16:59:20.246726
Stopped working: 2026-01-03 17:10:40.682876
Break time: 0 minutes
Worktime: 0:11:20.436150
--------------------------------------------------
```
## Additional comments
I initally wrote this as a very basic way to monitor my working hours. That's why it is missing a lot of features currently.
The way I used it was creating an autostart file for this script. That way it automatically started "recording" my work time.
Note that the script will fail and not append the work hours of a work day to the work_time.txt file, if you shutdown your device or close the script in any other unintended way before you entered your break time.


## Planned features
- Implement a feature which still saves the work hours to the work_time.txt file if you shutdown your device before the script script was able to save to the work_time.txt file.

## Installation & Usage
- Clone this repository
  ```
  git clone https://github.com/lulkaorg/pytime.git
  ```
- Create a pytime.desktop file in ~/.config/autostart and add something like this (assuming you did not change the location of the cloned repository):
  ```
  [Desktop Entry]
  Name=pytime
  Exec="~/pytime/time.py"
  Type=Application
  ```
