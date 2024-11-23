from typing import Tuple
from constants import HOUR_INDEX, MINUTE_INDEX, MINUTES_IN_HOUR, ONLY_ONE_PERSON_IN_MEETING
from report5_entities import OfficialTeamMeeting
#converts 'HH:MM' string to a tuple of two ints    (hour_int, minute_int)
#https://www.w3schools.com/python/python_tuples.asp
def convert_time_to_hours_minutes(time: str) -> Tuple[int,int]:
      split_hours_mins = time.split(':')
      hour_counter = int(split_hours_mins[HOUR_INDEX])
      minute_counter = int(split_hours_mins[MINUTE_INDEX])

      return (hour_counter, minute_counter)
#checks to see if hour and minute counter equal end time of official meeting so we can exit while loop
def has_finished_validating_meeting_overlap(official_end_time:str,hour_counter: int, minute_counter:int)-> bool:
     end_hour, end_min = convert_time_to_hours_minutes(official_end_time)

     if(hour_counter >= end_hour and minute_counter > end_min):
         return True
     return False
#checks to if the current time falls between the time of report start/end time passed to parameters
#if so name associated with report was the team member active at this time
def is_in_meeting_atm(reported_start_time:str, reported_end_time:str, hour_counter:int, minute_counter:int) -> bool:
     start_hour,start_min = convert_time_to_hours_minutes(reported_start_time)   
     end_hour, end_min = convert_time_to_hours_minutes(reported_end_time)
     if((start_hour == end_hour) and (start_min == end_min)):
          return False
     if((hour_counter > start_hour) or (hour_counter == start_hour and minute_counter >= start_min)):
          if((hour_counter < end_hour) or (hour_counter == end_hour and minute_counter < end_min)):
               return True
     return False
#checks if more time was spent not collaborting then collaborting in a meeting's report
# checks every minute from start to end in a meeting
# for each minute count how many people were active in that meeting according to their log report
#  if 2 or more people were active in a meeting during a given minute, add 1 to overlapped minutes variable
#  use report_names to check if the same person is active more than once at any given minute (sign of duplicate logs)
def meeting_overlap_validation(official_meeting: OfficialTeamMeeting):
    
     hour_counter,minute_counter = convert_time_to_hours_minutes(official_meeting.start_time)
     overlapped_minutes = 0
     report_names:list[str] = []
     while(not has_finished_validating_meeting_overlap(official_meeting.end_time,hour_counter,minute_counter)):
       
            people_in_meeting_for_this_minute = 0
            
            for report in official_meeting.get_reports():
                 
                 if(is_in_meeting_atm(report.start_time, report.end_time, hour_counter, minute_counter)):
                      people_in_meeting_for_this_minute += 1
                      if(report.name in report_names):
                           print_duplicate_users_present_err(report.name, official_meeting)
                      report_names.append(report.name)        
           
            if(people_in_meeting_for_this_minute > ONLY_ONE_PERSON_IN_MEETING):
                 overlapped_minutes += 1
           
            minute_counter += 1
           
            if(minute_counter >= MINUTES_IN_HOUR):
                 minute_counter = 0
                 hour_counter += 1

            report_names = []

     time_elapse = total_meeting_time(official_meeting.start_time, official_meeting.end_time)
     non_overlap_time = time_elapse - overlapped_minutes
     if(non_overlap_time > overlapped_minutes):     
                 print_lack_of_overlap_err(official_meeting, non_overlap_time, overlapped_minutes)

     official_meeting.set_time_meet(overlapped_minutes)
def total_meeting_time(s_time:str, e_time:str):
     start_hour,start_min = convert_time_to_hours_minutes(s_time)
     end_hour, end_min = convert_time_to_hours_minutes(e_time)
     s_minutes = time_to_minutes(start_hour,start_min)
     e_minutes = time_to_minutes(end_hour, end_min)
     return (e_minutes - s_minutes)

def time_to_minutes(hour, minutes):
     return (hour * 60) + minutes
#checks if more time was spent not collaborting then collaborting in a meeting      
def meetings_overlap_validation(official_meetings: list[OfficialTeamMeeting]):
    total_overlap = 0
    for meeting in official_meetings:      
        meeting_overlap_validation(meeting)
        total_overlap += meeting.get_time_meet()
    return total_overlap     
#prints anomaly error message for team member logged being at the same meeting during the same time more than once          
def print_duplicate_users_present_err(name:str, meeting: OfficialTeamMeeting):
     print("Report 5 Meeting Anomaly Error:")
     print(f"\tTeam Member {name} logged being at the same meeting during the same time more than once. (likely duplicate logs)")
     print_meeting_with_anomaly(meeting)
     exit()  
#prints anomaly error message for not having enough collaboration time
def print_lack_of_overlap_err(meeting: OfficialTeamMeeting, not_overlapped: int, overlapped: int):
     print("Report 5 Meeting Anomaly Error:")
     print("\tMore Minutes Spent With Only One Person Being In The Meeting Than Minutes Spent With Other Attendees. " + 
           " Please Look At The Meeting Details To Confirm Meeting Accuracy\n")
     print(f"\tTime Spent Working Together: {overlapped} Minutes")
     print('\tvs')
     print(f"\tTime Spent With Only One Person In The Meeting: {not_overlapped} Minutes")
     print_meeting_with_anomaly(meeting)
     exit()
#validates to see if only one member was in a meeting (anomaly)
#and if a member logs a group size that was not accurate (anomaly)
def validate_group_sizes(official_meetings: list[OfficialTeamMeeting]):
     for meeting in official_meetings:
          actual_attendee_amount = meeting.amount_of_participants
          for report in meeting.get_reports():
               if(actual_attendee_amount == ONLY_ONE_PERSON_IN_MEETING):
                    msg = f"Team member {report.name} participated in a meeting alone, {report.name} logged group size {report.group_size}. Meetings cant be solo!"
                    print_inconsistent_group_size_reports_err(meeting, msg)
               if(report.group_size != meeting.amount_of_participants):
                    msg = f"Team member {report.name} claims that the group size for a meeting on {meeting.date} between {meeting.start_time} - {meeting.end_time} was {report.group_size}. The actual amount of people in that meeting was {meeting.amount_of_participants}"
                    print_inconsistent_group_size_reports_err(meeting, msg)
          
#prints anomaly error message for inconsistent group sizes
def print_inconsistent_group_size_reports_err(meeting: OfficialTeamMeeting,msg:str):
     print("Report 5 Meeting Anomaly Error:")
     print("\t"+ msg)
     print_meeting_with_anomaly(meeting)
     exit()
#prints anomaly error message details
def print_meeting_with_anomaly(meeting: OfficialTeamMeeting):
     print("\n\tOfficial meeting in question: ")
     print(meeting)
     print("\t\tDetails logged by each user in the meeting: ")
     for report in meeting.get_reports():
          print(report)
