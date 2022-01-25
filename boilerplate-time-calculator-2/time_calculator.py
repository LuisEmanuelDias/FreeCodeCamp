def add_time(start, duration, day="None"):
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  start = start.split(" ")
  hour = int(start[0].split(":")[0])
  minute = int(start[0].split(":")[1])
  dhour = int(duration.split(":")[0])
  dminute = int(duration.split(":")[1])

  minute = minute + dminute
  hour = hour + dhour + (minute // 60)
  minute = minute % 60

  dhour = hour // 12
  hour = hour % 12


  if minute<10:
      minute = str(minute)
      minute = minute.zfill(2)
  dhour = ("PM" == start[1].strip()) + dhour

  if hour == 0:
      hour = 12  

  new_time = f"{hour}:{minute} {'AM' * (dhour % 2 == 0) + 'PM' * (dhour % 2 == 1)}"
  if day != "None":
      new_time = new_time + ", "+days[(days.index(day.strip().capitalize())+dhour//2)%7]

  if dhour//2 >1:
      new_time = new_time + f" ({dhour // 2} days later)"
  elif dhour//2 ==1:
      new_time = new_time + " (next day)"

  return new_time