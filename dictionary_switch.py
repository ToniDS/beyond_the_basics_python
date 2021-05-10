season = "Winter"
holiday = {'Winter': 'New Year\'s Day',
           'Spring': 'May Day',
           'Summer': 'Juneteenth',
           'Fall': 'Halloween'}.get(
               season, 'Personal day off')
print(holiday)

