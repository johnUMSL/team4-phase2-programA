import copy
from log_entry import LogEntry
from report5_entities import MeetingEventBuilder, OfficialTeamMeeting, ReportedMeeting
from report5_helpers import build_official_team_meeting, build_report, finalize_reports_for_meeting, merge_meetings, sorter_by_start_date_time
from report5_validations import meetings_overlap_validation, validate_group_sizes
from test_print import print_main_data_struct


#main method for generating report 5
def report5(activity_logs_by_student: dict[str, list[LogEntry]]):
   
    activity_4_logs_by_student: dict[str, list[LogEntry]] = filter_for_code4(activity_logs_by_student)
   
    meetings_by_date: dict[str, list[ReportedMeeting]] = get_reported_meetings_by_date(activity_4_logs_by_student)
   
    unique_meetings_by_date: dict[str, list[MeetingEventBuilder]] = get_meetings_events_by_date(meetings_by_date)

    official_meetings: list[OfficialTeamMeeting] = generate_official_meetings_report(meetings_by_date, unique_meetings_by_date)
    
    validate_group_sizes(official_meetings)

    time_spent_meeting_minutes = meetings_overlap_validation(official_meetings)

    print_all_official_meetings(official_meetings)

    print(f"\n\n\nAmount Of Time This Team Spent Meeting: {time_spent_meeting_minutes} Minutes")
    
    return

#filters student;s log entries for only meeting activites (activity 4)
def filter_for_code4(activity_logs_by_student: dict[str, list[LogEntry]]):

    activity_4_logs_by_student: dict[str, list[LogEntry]] = {}
    for key in activity_logs_by_student:
        activity_code4_logs: list[LogEntry] = []
        for log_entry in activity_logs_by_student[key]:
            if(log_entry.activity_code == "4"):
                activity_code4_logs.append(log_entry)
        activity_4_logs_by_student[key] = activity_code4_logs
                   
    return activity_4_logs_by_student

#converts a log entries organized by student into reports organized by date.
#reports contain only neccessary information from logs for data processing
def get_reported_meetings_by_date(activity_4_logs_by_student: dict[str, list[LogEntry]]) ->  dict[str, list[ReportedMeeting]]:
    meetings_by_date: dict[str, list[ReportedMeeting]] = {}
    for key in activity_4_logs_by_student:    
        for log_entry in activity_4_logs_by_student[key]:
            if(log_entry.date not in meetings_by_date):
                meetings_by_date[log_entry.date] = []
            meetings_by_date[log_entry.date].append(build_report(log_entry, key))   
                   
    return meetings_by_date
#organizes log entry reports for each meeting day into a list builder objects to represent unique meetings
#uses merge algorithm to create unique meetings in long format (merge_meetings)
def get_meetings_events_by_date(meetings_by_date: dict[str, list[ReportedMeeting]]) ->  dict[str, list[MeetingEventBuilder]]:
       unique_meetings_by_date: dict[str, list[MeetingEventBuilder]] = {}
       for date_key in meetings_by_date: 
        reported_meeting_on_date: list[ReportedMeeting] = copy.deepcopy(meetings_by_date[date_key])
        meeting_events_on_date: list[MeetingEventBuilder] = merge_meetings(reported_meeting_on_date) 
        unique_meetings_by_date[date_key] = meeting_events_on_date 
         
       return unique_meetings_by_date
#generates list of official meetings
#log entry reports organized by date 
#and unique (long meeting format) meetings by date
def generate_official_meetings_report( meetings_by_date: dict[str, list[ReportedMeeting]], unique_meetings_by_date: dict[str, list[MeetingEventBuilder]]) -> list[OfficialTeamMeeting]:
    official_meetings: list[OfficialTeamMeeting] = []
    official_dates = list(meetings_by_date.keys())
    if(set(official_dates) != set(unique_meetings_by_date.keys())):
       raise Exception("Error: Mismatch in date key list between dict of all meetings by date and dict of unique meetings by date. Something Bad Occurred!")

    for date in official_dates:
        official_meetings_for_this_date: list[OfficialTeamMeeting] = []
        
        for event in unique_meetings_by_date[date]:
            official_meeting: OfficialTeamMeeting = build_official_team_meeting(date, event)  
            finalize_reports_for_meeting(official_meeting, date, meetings_by_date)
            official_meetings_for_this_date.append(official_meeting)

        official_meetings.extend(official_meetings_for_this_date)
    
    return official_meetings    
 #prints all official unique meetings and the log reports associated with them             
def print_all_official_meetings(official_meetings: list[OfficialTeamMeeting]):
    official_meetings_by_earliest_start_date_time = sorter_by_start_date_time(official_meetings)
    
    for meeting in official_meetings_by_earliest_start_date_time:
        print(f"\n\nTeam meeting occurred on {meeting.date} at {meeting.start_time} and ended at {meeting.end_time}. Team members collaborated for {meeting.get_time_meet()} minutes. {meeting.amount_of_participants} people attended the meeting.")
        print("Meeting Log Reports From Members:")
        for report in meeting.get_reports():
            print(f"\tTeam member {report.name} joined the meeting at {report.start_time} and left the meeting at {report.end_time}")
        print("\n")