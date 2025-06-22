from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def report_week(habit_dict, task_dict, file_name):
    print(f"\nWeekly Report for: {file_name}")
    print("=" * 50)

    print("\nHabit Completion Summary:")
    for habit, daily_status in habit_dict.items():
        completed = sum(daily_status[day] for day in days)
        print(f"{habit}: {completed}/7 days")

    print("\nTask Breakdown by Day:")
    for day in days:
        tasks_done = [task for task, done in task_dict.get(day, {}).items() if done]
        print(f"{day}: {', '.join(tasks_done) if tasks_done else 'No tasks completed'}")

    print("=" * 50)

file_list = [
    "dictionaries_1.txt",
    "dictionaries_2.txt",
    "dictionaries_3.txt",
    "dictionaries_4.txt",
    "dictionaries_5.txt",
    "dictionaries_6.txt",
    "dictionaries_7.txt",
    "dictionaries_8.txt",
    "dictionaries_9.txt",
    "dictionaries_10.txt"
]

for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        report_week(data[0], data[1], file_name)
