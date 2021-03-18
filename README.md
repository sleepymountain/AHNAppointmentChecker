# AHN Appointment Checker
###### Checks for Appointments for COVID Vaccines every 5 minutes so you don't have to.


Checks the website for appointments every five minutes, in the background
and when it finds them it will send a windows notification and open the website in your default browser.


## Installation:
> Download and Extract the [newest release](https://github.com/sleepymountain/AHNAppointmentChecker/releases/tag/1.6b)
> 
> Everything is packed into the binary release so that you don't have to install any dependencies.
> 
> Extract to a directory and run AHN Appointment Checker v1.6b.exe


## Uses External Dependencies:
```
Selenium
Chromedriver
ToastNotifier
AutoPy2Exe
```

## Changelog:
```
New in 1.6b:
- Fatal bug fix (Crashed when appointments were found. Problem was due to if statement instead of using try with exceptions.)
- Removed ToastNotifier and Replaced with Plyer (due to issues during build)

New in v1.5b
- Better UI Formatting
- 12 hour time, instead of 24 hour time.
- Logging: All results are outputted into \log\log.txt (for easier analysis of appointment posting times)
- Added and then removed colorama, due to issues after compiling to an executable.
```

## Known Bugs:
None as of v1.6b :)

## Bug Reporting
Feel free to open any issues to report bugs :)
