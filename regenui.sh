# Recreate pyton files from Qt ui files
#
# Open a Terminal window and enter the commands below depending on what
# you need to convert.
#
# To run on linux:
#   cd susie/Transfer\ Project
#   source regenui.sh
# 
# or to convert a single file:
#   cd susie/Transfer\ Project
#   pyuic5 -x SeatBooking.ui -o SeatBooking.py
#

pyuic5 -x ChoiceMenu.ui -o ChoiceMenu.py
pyuic5 -x Records.ui -o Records.py
pyuic5 -x SeatBooking.ui -o SeatBooking.py
pyuic5 -x SeatInfo.ui -o SeatInfo.py

