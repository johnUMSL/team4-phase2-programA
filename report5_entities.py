from datetime import datetime
#https://docs.python.org/3/tutorial/classes.html
#individual activity 4 (meeting) log   
class ReportedMeeting:
    #constructor
    def __init__(self,name:str, start_time:str, end_time:str, group_size:int) -> None:
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.group_size = group_size
    #to string method
    def __repr__(self) -> str:
        return f"\n\t\t\tLog Details:: Name: {self.name}, Start Time: {self.start_time}, End Time: {self.end_time}, Group Size: {self.group_size}\n"
    #equality overload (==)
    def __eq__(self, other):
    
        return (
            self.name == other.name
            and self.start_time == other.start_time
            and self.end_time == other.end_time
            and self.group_size == other.group_size
        )
#builds a unique meeting entity. attendees is names of team members who particpated
# long meeting format. 
# so start_time is earliest start time reported by member for this meeting
# and end_time is latest end time reported by member for this meeting    
class MeetingEventBuilder:
    #constructor
    def __init__(self, attendees: list[str], start_time:str, end_time:str) -> None:
        self.attendees = attendees
        self.start_time = start_time
        self.end_time = end_time
    #to string method    
    def __repr__(self) -> str:
        return f"\nEvent:: Attendees: {self.attendees}, Start Time: {self.start_time}, End Time: {self.end_time}\n"
#details of a meeting provided by user from thier log file
class OfficialUserReportDetails:
      #constructor
      def __init__(self, name:str, reported_start_time:str, reported_end_time:str, reported_group_size: int) -> None:
        self.name = name
        self.reported_start_time = reported_start_time
        self.reported_end_time = reported_end_time
        self.reported_group_size = reported_group_size
      #to string method
      def __repr__(self) -> str:
        return f"\n\t\t\tLog Details:: Name: {self.name}, Start Time: {self.reported_start_time}, End Time: {self.reported_end_time}, Group Size: {self.reported_group_size}\n"
#official meeting report
#start_date_time is time meeting started. (used for sorting alg)
# long meeting format
# so start_time is earliest start time reported by member for this meeting
# and end_time is latest end time reported by member for this meeting 
#time_meet is time during meeting where 2 or more people were in the meeting
#reported_details list of team member logs associated with meeting
class OfficialTeamMeeting:
      #constructor
      def __init__(self, date:str, start_time:str, end_time:str, amount_of_participants: int) -> None:
        self.start_date_time = datetime.strptime(date + " " + start_time, "%m/%d/%Y %H:%M")
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.amount_of_participants = amount_of_participants
        self.reported_details: list[ReportedMeeting] = []
        self.time_meet = 0
      #setter for time_meet
      def set_time_meet(self,meeting_overlap:int):
         self.time_meet = meeting_overlap
      #getter for time_meet
      def get_time_meet(self) -> int:
         return self.time_meet
      #getter for reported_details list
      def get_reports(self) -> list[ReportedMeeting]:
        return self.reported_details
      #append to reported_details list 
      def add_report(self, detailed_report:ReportedMeeting):
        self.reported_details.append(detailed_report)  
          #to string method
      def __repr__(self) -> str:
        return f"\n\tTeam Meeting:: Date Occurred: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}, Amount Of Participants: {self.amount_of_participants}\n"
