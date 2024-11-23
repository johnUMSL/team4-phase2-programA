import decimal
import copy
from constants import EMPTY_LIST
from log_entry import LogEntry
from report5_entities import MeetingEventBuilder, OfficialTeamMeeting, ReportedMeeting

#returns count of unique values in attendees so we can determine true amount of unique meeting participants
def count_unique_attendees(attendees:list[str]) -> int:
    unique_attendee = set(attendees)
    return len(unique_attendee)
#convert MeetingEventBuilder object to OfficialTeamMeeting object
def build_official_team_meeting(date:str, event: MeetingEventBuilder) -> OfficialTeamMeeting:
    result = OfficialTeamMeeting(
                date=date,
                start_time=event.start_time,
                 end_time=event.end_time,
                 amount_of_participants=count_unique_attendees(event.attendees)
                 )
    return result
#converts log entry object into a meeting report object
def build_report(log_entry: LogEntry, username) -> ReportedMeeting:
    result = ReportedMeeting(name=username, 
                     start_time=log_entry.start_time,
                     end_time=log_entry.end_time,
                     group_size=log_entry.group_size,
                     )
    return result
#converts 'HH:MM' string to decimal hh.mm for time comparing
def time_str_to_decimal(time: str) -> decimal:
    time_as_decimal_str = time.replace(':', '.') 
    return decimal.Decimal(time_as_decimal_str)
#convert Report object into a MeetingEventBuilder object
def build_event(reported_meeting: ReportedMeeting) -> MeetingEventBuilder:
   
    result = MeetingEventBuilder(attendees=[reported_meeting.name], 
                          start_time=reported_meeting.start_time, 
                          end_time=reported_meeting.end_time
                          )
    return result
#updates MeetingEventBuilder object if report falls within event start/end time. 
# adds name to attendees list
# replaces event end time with reports end time to ensure long meeting format
def update_meeting_event(new_report_details: ReportedMeeting, old_meeting_event: MeetingEventBuilder) -> MeetingEventBuilder:

    new_meeting_event = old_meeting_event
    
    
    new_meeting_event.attendees.append(new_report_details.name)

    if(new_meeting_event.end_time < new_report_details.end_time):
         new_meeting_event.end_time = new_report_details.end_time

    return new_meeting_event
#loops through all meetings on a given day
# converts them into a list of unqiue meetings as MeetingEventBuilder objects  
def merge_meetings(reported_meetings: list[ReportedMeeting]) -> list[MeetingEventBuilder]:
    unique_meetings: list[MeetingEventBuilder] = []
    while(len(reported_meetings) != EMPTY_LIST):
        current_earliest_reported_meeting = pull_earliest_reported_meeting(reported_meetings)

        for unqiue_meeting in unique_meetings:
            if(can_merge(current_earliest_reported_meeting.start_time, unqiue_meeting.end_time)):
               unqiue_meeting = update_meeting_event(current_earliest_reported_meeting, unqiue_meeting)
               break
        
        else: # this called if break is not called in for loop https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/   
            unique_meetings.append(build_event(current_earliest_reported_meeting))
            
    return unique_meetings
#finds earliest meeting from list of reported meetings
#then we delete earliest meeting from the list and return earliest reported meeting
def pull_earliest_reported_meeting(reported_meetings: list[ReportedMeeting]) -> ReportedMeeting:
    if(len(reported_meetings) == EMPTY_LIST):
        raise Exception("Error: No records exist to pull. (should never happen)")
    earliest_meeting: ReportedMeeting = copy.deepcopy(reported_meetings[0])
    for reported_meeting in reported_meetings:
        if(time_str_to_decimal(reported_meeting.start_time) <= time_str_to_decimal(earliest_meeting.start_time)):
            earliest_meeting = copy.deepcopy(reported_meeting)
  
    reported_meetings.remove(earliest_meeting)
        
    return earliest_meeting
#sees if we can merge a reported meeting into a unqiue meetingbuilder object.
#done by checking if reported start time is less than or equal to unqiue meeting builder's current end time
def can_merge(reported_start_time: str, event_end_time: str) -> bool:
     
     if(time_str_to_decimal(reported_start_time) <= time_str_to_decimal(event_end_time)):
         return True
     else:
         return False
#adds all log reports for a official meeting to the official meeting objects reported_details list
def finalize_reports_for_meeting(official_meeting: OfficialTeamMeeting,date: str, meetings_by_date: dict[str, list[ReportedMeeting]]):
    for report in meetings_by_date[date]:
        if((time_str_to_decimal(report.start_time) >= time_str_to_decimal(official_meeting.start_time)) and (time_str_to_decimal(report.end_time) <= time_str_to_decimal(official_meeting.end_time))):
            official_meeting.add_report(report)
    return
#sorts meetings using a date time object property. (earliest start time to latest start time)
#from https://stackoverflow.com/questions/14472795/how-do-i-sort-a-list-of-datetime-or-date-objects
def sorter_by_start_date_time(meetings: list[OfficialTeamMeeting]) -> list[OfficialTeamMeeting]:
    return sorted(meetings, key=lambda meeting: meeting.start_date_time)
