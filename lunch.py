#!/usr/bin/python
#
# Script reminds me with a random message to take lunch at 11:30AM Monday - Friday
# I'm using cron to send notifications
#

import time
import datetime
import random

# Display the day of the week
print "Day of the week: ", datetime.date.today().strftime("%A")

# Randomly select a message to send
myList=["Go outside for lunch","Take a break for lunch","Buy lunch at the caf","Meet up with a friend for lunch","Is it friday yet? well at least its lunch time"]
print(random.choice(myList))
