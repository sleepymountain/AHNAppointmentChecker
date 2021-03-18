# AHN Appointment Checker
###### Checks for Appointments for COVID Vaccines every 5 minutes so you don't have to.


Checks the website for appointments every five minutes, in the background
and when it finds them it will send a windows notification and open the website in your default browser.


## Installation:
> Download and Extract the [newest release](https://github.com/sleepymountain/AHNAppointmentChecker/releases/tag/1.5b)
> 
> Everything is packed into the binary release so that you don't have to install any dependencies.
> 
> Extract to a directory and run AHN Appointment Checker v1.5b.exe


## Uses External Dependencies:
```
Selenium
Chromedriver
ToastNotifier
AutoPy2Exe
```

## Changelog:
```
New in v1.5b
- Better UI Formatting
- 12 hour time, instead of 24 hour time.
- Logging: All results are outputted into \log\log.txt (for easier analysis of appointment posting times)
- Added and then removed colorama, due to issues after compiling to an executable.
```

## Known Bugs:
Crashes when appointments, are found -- currently fixing this. Problem due to if statement instead of using try with exceptions.
Since appointments were not available at the time of creation, it needs more testing.

## Bug Reporting
Feel free to open any issues to report bugs :)
