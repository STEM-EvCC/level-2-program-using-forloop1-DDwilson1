mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]# Space Mission Analyzer Program by a beginner
how_many_total_missions_there_are = 0 # Start counting things
how_many_were_successful_missions = 0
list_of_old_mission_names = []
for index_of_current_mission in range(len(mission_names)): # Go through all missions one at a time
    how_many_total_missions_there_are = how_many_total_missions_there_are + 1
    mission_names[index_of_current_mission]
how_many_were_successful_missions = how_many_were_successful_missions + 1
if mission_years[index_of_current_mission] < 2000:
        list_of_old_mission_names.append(mission_names[index_of_current_mission])
success_percentage_as_float = (how_many_were_successful_missions / how_many_total_missions_there_are) * 100 # Doing math for success percent
print("Total number of missions: " + str(how_many_total_missions_there_are)) # Print everything like the assignment said
print("Number of successful missions: " + str(how_many_were_successful_missions))
print("Success rate: {:.2f}%".format(success_percentage_as_float)) #This was hard to figure out and find an example of.
print("Missions launched before the year 2000:")
for each_mission_before_2000 in list_of_old_mission_names:
    print("- " + each_mission_before_2000)
