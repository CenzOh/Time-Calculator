def add_time(start, duration, day_of_week=False):
  #day of week parameter added for user to include
  
  #first associate day of week with number (index) then create actual array of days of week that will be displayed
  days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

  days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  duration_tuple = duration.partition(":") #we want to split the duration string into hours and minutes. Split by : -> '3'(0) ':'(1) '10'(2)
  duration_hours = int(duration_tuple[0]) #index 0 is hour
  duration_minutes = int(duration_tuple[2]) #index 2 is minute, index 1 is colon

  start_tuple = start.partition(":") #same ideas as before. '3'(0) ':'(1) '10 PM'(2)
  start_minutes_tuple = start_tuple[2].partition(" ") #split minutes by space '10'(0) ' '(1) 'PM'(2)
  start_hours = int(start_tuple[0])
  start_minutes = int(start_minutes_tuple[0])
  am_or_pm = start_minutes_tuple[2]
  am_and_pm_flip = {"AM": "PM", "PM": "AM"}

  amount_of_days = int(duration_hours / 24) # if not greater than 24, will be 0, if greater, will be 1

  end_minutes = start_minutes + duration_minutes #end is for the output
  if(end_minutes >= 60): #adds an hour if minutes are greater than 60
    start_hours +=1 
    end_minutes = end_minutes % 60 #% makes sure we do not exceed 60
  amount_of_am_pm_flips = int((start_hours + duration_hours) /12) #adds start and duration hour and divides by 12 since at the 12 mark AM or PM will flip
  end_hours = (start_hours + duration_hours) % 12 #% makes sure we do not go over 12 hours. Ex: 11+2 = 13/12 = 1 flip

  end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes) #end minutes equal itself if it is greater than 9 because we are accounting for two digits. The else makes it so the single digit minutes look like '05'
  end_hours = end_hours = 12 if end_hours == 0 else end_hours #if the hour is 0 that means we would display a 12. Works for either 12 PM or 12 AM
  if(am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12): #handles case of going into next day. 10 PM + 3 hours = 1 AM next day
    amount_of_days += 1

  am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm # we want to modular the amount of flips to equal 1 because if we go from 1 PM + 25 hours = 2 PM next day. Don't need to flip PM in this case

  new_time = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm #format of what will print
  if(day_of_week): #checking if user input day of week.
    day_of_week = day_of_week.lower() #makes text lowercase so the index can read it
    index = int((days_of_the_week_index[day_of_week]) + amount_of_days) % 7 #pass in days of week index dict. Add on amount of days variable. % 7 for the 7 days of week
    new_day = days_of_the_week_array[index] #get the new day here form passing in index to the array
    new_time += ", " + new_day #print out time and day

  if(amount_of_days == 1):
    return new_time + " " + "(next day)" #case for the next day, does not display date
  elif(amount_of_days > 1):
    return new_time + " (" + str(amount_of_days) + " days later)" #case for multiple days later, just pass in amount of days variable

  
  return new_time