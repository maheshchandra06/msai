# Critical Thinking Assignment
if __name__ == '__main__':

    room_numbers = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    schedules = {
        "CSC101": "8:00 AM",
        "CSC102": "9:00 AM",
        "CSC103": "10:00 AM",
        "NET110": "11:00 AM",
        "COM241": "1:00 PM"
    }


    def add_course(course):
        if not course.strip():
            course = input("Enter a course number: ").upper()
        room = input("Enter room number: ")
        instructor = input("Enter instructor name: ")
        schedule = input("Enter schedule: ")

        room_numbers[course] = room
        instructors[course] = instructor
        schedules[course] = schedule

        print("Course added successfully.")
        print_course_schedule(course)


    def print_course_schedule(course):
        if course not in room_numbers:
            print("Course not yet added Yet.")
            new_course = input("Do you want to add new course? (yes/no): ")
            if new_course.lower() == "yes":
                add_course(course)
            return

        print("Course: {}\nRoom Number: {}\nInstructor: {}\nSchedule: {}"
              .format(course, room_numbers.get(course), instructors.get(course), schedules.get(course)))


    course_name = input("Enter a course number: ").upper()
    print_course_schedule(course_name)

