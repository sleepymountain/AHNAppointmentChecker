# AHNAppointmentChecker
###### Checks for Appointments for COVID Vaccines every 5 minutes so you don't have to.


Checks the website for appointments every five minutes, in the background
and when it finds them it will send a windows notification and open the website in your default browser.


## Installation:
> Download and Extract the [newest release](https://github.com/sleepymountain/AHNAppointmentChecker/releases/tag/1.3b)
> 
> Everything is packed into the binary release so that you don't have to install any dependencies.
> 
> Extract to a directory and run AHN Appointment Checker v1.3b.exe


## Uses External Dependencies:
```
Selenium
Chromedriver
ToastNotifier
AutoPy2Exe
```

## Todo:
- [ ] Add colorama to make it easier to see whether appointments are/were available in the console window
- [ ] Add a logging system to log when appointments were available, making it easier to predict.
- [ ] 12 hour time instead of 24 hour time?

## Known Bugs:

Since appointments were not available at the time of creation, it needs more testing.

## Bug Reporting
Feel free to open any issues to report bugs :)
