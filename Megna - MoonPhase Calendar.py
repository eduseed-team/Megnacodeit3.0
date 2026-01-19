import ephem
from turtle import *
from datetime import datetime, timedelta

# Ask user for month and year
year = int(input("Enter the year (e.g. 2025): "))
month = int(input("Enter the month (1-12): "))

# Start and end dates
start_date = datetime(year, month, 1)
if month == 12:
    end_date = datetime(year + 1, 1, 1)
else:
    end_date = datetime(year, month + 1, 1)

# calculation of phases
def get_phase_name(date):
    obs = ephem.Observer()                
    obs.date = date.strftime("%Y/%m/%d")      #here, i get the date
    prev_new = ephem.previous_new_moon(obs.date)   #prev new moon
    next_new = ephem.next_new_moon(obs.date)   #next new moon
    age = obs.date - prev_new  # moon age (age=present date- last new moon)
    cycle_length = next_new - prev_new

    fraction = age / cycle_length    #which phase the moon is in

    if fraction < 0.01 or fraction >0.94: #if it is 1 or 0 approx
        return "New Moon"
    elif fraction < 0.22:   #these are all approcimate values
        return "Waxing Crescent"
    elif fraction < 0.28:
        return "First Quarter"
    elif fraction < 0.47:
        return "Waxing Gibbous"
    elif fraction < 0.53:
        return "Full Moon"
    elif fraction < 0.72:
        return "Waning Gibbous"
    elif fraction < 0.78:
        return "Last Quarter"
    else:
        return "Waning Crescent"

# using overlapping circles to draw moon
def draw_moon(phase, date_str, x, y):
    penup()
    goto(x, y)
    pendown()

    #white circle
    color("white")
    begin_fill()
    circle(25)
    end_fill()

    #black circle for shadow
    penup()
    goto(x, y)
    pendown()
    color("black")
    begin_fill()

    if phase == "New Moon":
        circle(25)
    elif phase == "Full Moon":
        pass  #fully white
    elif phase == "First Quarter":
        setheading(90)
        circle(25, 180)
        goto(x, y - 25)
    elif phase == "Last Quarter":
        setheading(270)
        circle(25, 180)
        goto(x, y - 25)
    elif "Crescent" in phase:
        offset = 10 if "Waxing" in phase else -10
        penup()
        goto(x + offset, y)
        pendown()
        circle(25)
    elif "Gibbous" in phase:
        offset = -10 if "Waxing" in phase else 10
        penup()
        goto(x + offset, y)
        pendown()
        circle(25)
    end_fill()

    # Writing info under (date and phase)
    penup()
    goto(x, y - 35)
    pencolor("white")
    write(date_str, align="center", font=("Arial", 8, "normal"))
    goto(x, y - 50)
    write(phase, align="center", font=("Arial", 7, "italic"))

bgcolor("black")
title("Moon Phase Calendar")
speed(0)
hideturtle()

# Draw moon phases
x, y = -300, 250
day = start_date
while day < end_date:
    phase_name = get_phase_name(day)
    date_str = day.strftime("%d/%m/%Y")

    draw_moon(phase_name, date_str, x, y)

    x += 120
    if x > 300:
        x = -300
        y -= 100

    day += timedelta(days=1)

#main code over 
penup()
goto(350, -300)
pencolor("white")
write("THANK YOU :)", font=("Courier New", 24, "bold"))

done()