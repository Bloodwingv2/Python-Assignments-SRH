def to_minutes(time):
    """Converts time in String to minutes as int for comparisons"""
    parts = time.split(':')    # we split "9:30" into ['9', '30'] as its a string and we can't use strings for comparison 
    hours = int(parts[0])      # Store first part i.e: '9' → 9 as an int
    mins = int(parts[1])       # Get second part: '30' → 30 and store it as int as well
    
    return hours * 60 + mins 

def to_hours(time):
    """Converts time in minutes back to hours in string format"""
    meetings_in_hours = []
    for gaps in time:
        start = gaps[0]  # Get first element
        end = gaps[1]    # Get second element
        hours_1 = start // 60
        mins_1 = start % 60
        hours_2 = end // 60
        mins_2 = end % 60
        meetings_in_hours.append([f"{hours_1}:{mins_1:02d}", f"{hours_2}:{mins_2:02d}"]) # use 02d to add zeros to mins
        
    return meetings_in_hours

def concatenate_calendars(YourCalendar, YourCoWorkersCalendar):
    """Concatenate both calendars into one for processing/comparison"""
    merged_calendar = YourCalendar + YourCoWorkersCalendar
    for meeting in merged_calendar:
        start = meeting[0]  # Get first element
        end = meeting[1]    # Get second element
        res.append([to_minutes(start), to_minutes(end)])
    
    return res

def merge_time(time):
    """Merge overlapping time slots in the calendar"""
    compare_variable = [time[0]] # keep it as lists of lists for iteration
    for start, end in time[1:]:
        compare_END = compare_variable[-1][1] # End of freshly added time
        if start <= compare_END:
            compare_variable[-1][1] = max(compare_END,end)
        else:
            compare_variable.append([start,end])

    return compare_variable
        
def meeting_scheduler(time, your_hours, coworker_hours):
    """Find available meeting slots by subtracting end-times and by factoring both users working hours"""
    overlap_start = max(to_minutes(your_hours[0]), to_minutes(coworker_hours[0]))
    overlap_end = min(to_minutes(your_hours[1]), to_minutes(coworker_hours[1]))
    
    meetings = []
    compare_variable = [time[0]]
    
    for start, end in time[1:]:
        compare_END = compare_variable[-1][1]
        if start - compare_END >= meetingDuration:
            meetings.append([compare_END, start])
        compare_variable.append([start, end])
    
    # Add final gap from last meeting to end of workday
    last_meeting_end = compare_variable[-1][1]
    if overlap_end - last_meeting_end >= meetingDuration:
        meetings.append([last_meeting_end, overlap_end])
    
    return meetings


res = []
YourCalendar = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
YourWorkingHours = ['9:00', '20:00']
YourCoWorkersCalendar = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30','15:00'], ['16:00', '17:00']]
YourCoWorkersWorkingHours = ['10:00', '18:30']
meetingDuration = 30

if __name__ == "__main__":
    
    res = concatenate_calendars(YourCalendar, YourCoWorkersCalendar) # First things first lets concatenate both calendars so that we can properly process them
    res.sort() # sort the merged calendar using standard sort to avoid inconsistencies and easier linear processing
    res = merge_time(res) # Now we merge the overlapping time slots in the merged calendar to get proper busy slots for both users
    res = meeting_scheduler(res, YourWorkingHours, YourCoWorkersWorkingHours) # Finally we find the gaps in between the merged calendar considering both users working hours
    res = to_hours(res) # As the output is required in a hours format we can just reverse the process of converting to minutes back to hours
    print(res) # print the final result


    
    
""" Legacy code for meeting_scheduler function without working hours consideration
def meeting_scheduler(time):
    meetings = []
    compare_variable = [time[0]] # keep it as lists of lists for iteration
    for start, end in time[1:]:
        compare_END = compare_variable[-1][1] # End of freshly added time
        if start - compare_END >= meetingDuration:
            meetings.append([compare_END, start])
            compare_variable.append([start,end])

    return meetings"""
