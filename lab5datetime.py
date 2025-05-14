from datetime import date, datetime, timedelta

# Function to calculate days between two dates
def get_days_between(start: date, end: date) -> int:
    return (end - start).days

# Current date and datetime
current_date = date.today()
current_datetime = datetime.now()
print("Current date:", current_date)
print("Current datetime:", current_datetime)

# Parse date string and format
date_str = "2024-05-10"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
print("Parsed date:", parsed_date)

formatted = parsed_date.strftime("%d %b %Y")
print("Formatted date:", formatted)

# Add/Subtract days
plus_days = parsed_date + timedelta(days=5)
minus_days = parsed_date - timedelta(days=3)
print("Add 5 days:", plus_days)
print("Subtract 3 days:", minus_days)

# Get year/month/day
print(f"Year: {parsed_date.year}, Month: {parsed_date.month}, Day: {parsed_date.day}")

# Difference in days
end_date = date(2024, 5, 20)
diff_days = get_days_between(parsed_date, end_date)
print(f"Difference between {parsed_date} and {end_date} is: {diff_days} days")

# LocalDateTime difference
dt1 = datetime(2024, 5, 1, 10, 30)
dt2 = datetime(2024, 5, 14, 5, 0)
diff_datetime = (dt2 - dt1).days
print(f"datetime (LocalDateTime) difference: {diff_datetime} days")
