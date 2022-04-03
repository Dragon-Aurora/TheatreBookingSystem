# Recreate pyton files from Qt ui files
# To run on linux:
#  source regenui.sh
pyuic5 -x ChoiceMenu.ui -o ChoiceMenu.py
pyuic5 -x Records.ui -o Records.py
pyuic5 -x SeatBooking.ui -o SeatBooking.py
pyuic5 -x SeatInfo.ui -o SeatInfo.py

