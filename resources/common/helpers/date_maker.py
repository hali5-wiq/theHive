import datetime

class DateMaker:

    def current_time(self):
        now = datetime.datetime.now()
        return now.strftime("%d%m%Y-%I%M%Sp")

    def get_formatted_date(self, date_to_format, pattern):
        try:
            formatted_date = date_to_format.strftime(pattern)
        except ValueError:
            # Handle cases where the pattern is invalid for the given date components
            formatted_date = "Invalid pattern or date components"
        return formatted_date

    def convert_to_datetime(self, date_to_convert, pattern):
        try:
            datetime_object = datetime.datetime.strptime(date_to_convert, pattern)
        except ValueError:
            # Handle cases where the date string or pattern is invalid
            datetime_object = None  # Or raise an exception if needed
        return datetime_object

    def convert_to_date(self, date_to_convert, pattern):
        try:
            date_object = datetime.datetime.strptime(date_to_convert, pattern).date()
        except ValueError:
            # Handle cases where the date string or pattern is invalid
            date_object = None  # Or raise an exception if needed
        return date_object