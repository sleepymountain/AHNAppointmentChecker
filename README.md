# AHNAppointmentChecker
###### Checks for Appointments for COVID Vaccines every 5 minutes so you don't have to.

Checks the website for appointments every five minutes, in the background
and when it finds them it will send a windows notification and open the website in your default browser.

Everything is packed into the binary release so that you don't have to install any dependencies.

Uses External Dependencies:
```
Selenium
Chromedriver
ToastNotifier
AutoPy2Exe
```

Known Bugs:
```
Time is not updating, because it declared at the namespace, fixing in next release.
Since appointments were not available at the time of creation, it needs more testing.
```

