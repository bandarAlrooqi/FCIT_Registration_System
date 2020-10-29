# this program was created by Bandar Abdullah  - 1855415-
import datetime

# this will help adding semesters next year or later and prevent users from adding wrong id -mostly used in
# def which semester:-
this_year = str(datetime.datetime.now().year)[2:4]
# if the date is Hijri convert it .
if str(datetime.datetime.now().year)[0] != '2':
    this_year = (float(datetime.datetime.now().year) * 0.97) + 622
    this_year = this_year[2:4]
# all the student will be here and after sorting based on weighted ratio students with index 15 or higher wont be
# accepted
male_students = dict()
female_students = dict()
# adding subjects with grades and semester here
subjects = dict()
# this to show all the semester from the registered date till now (this_year is used here to detect which year is this )
semesters = []
semester = ''


def validation_of_name_GPA_and_id(user_input, requirement_type):
    if requirement_type == str:
        if len(user_input) < 3:
            raise Exception("Invalid Name")
        for check in user_input:
            if str.isdigit(check):
                raise Exception(
                    "Name must not contains numbers in it .. please try again")
    elif requirement_type == int:
        for check in user_input:
            if not str.isdigit(check):
                raise Exception(
                    "ID must contains numbers only ... please try again")
        if user_input[0:2] == str(int(this_year)+1):
            raise Exception(
                "Oops you seem to be a new student of KAU ..come back later :)")
        if user_input[0] != "1" and int(user_input[0:2]) != int(this_year) or len(user_input) < 5 or len(
                user_input) > 8:
            raise Exception("Invalid ID number ... please try again")
    else:
        if user_input[0] == "p" and 0 < float(user_input[1:]) < 3.75:
            return
        if float(user_input) < 3.75 or float(user_input) > 5:
            raise Exception(
                "Unacceptable GPA ...please try again\nif you have you have a permission from college council please add \'p\' before your GPA\ne.g: p3.70")


def while_true(options, text, error):
    user_input = input(text).lower()
    while user_input.lower() not in options:
        print("\n\n"+str(error)+"\n\n")
        user_input = input(text).lower()

    return user_input


def add_semesters_based_on_id():
    semesters.clear()
    global semester
    semester = "please select the semester:\n"
    counter = int(student_id[0:2])
    choices = 0
    while counter <= int(this_year):
        choices += 1
        semester += str(choices) + ".20" + str(counter) + "-1\n"
        semesters.append("20" + str(counter) + "-1")
        choices += 1
        semester += str(choices) + ".20" + str(counter) + "-2\n"
        semesters.append("20" + str(counter) + "-2")
        choices += 1
        semester += str(choices) + ".20" + str(counter) + "-Summer\n"
        semesters.append("20" + str(counter) + "-3")
        counter += 1

    # because sometimes it happens you finished the first semester before the end of the year
    semester += str(choices + 1) + ".20" + str(counter) + "-1\n"
    semesters.append("20" + str(counter) + "-1")


def you_have_done(subject):
    _answer = while_true(['yes', '1', '2', ' no'], "Have you completed " +
                         subject + " ?\n1.Yes\n2.No\n", "Wrong choice ... please try again ").lower()
    return _answer == '1' or _answer == 'yes'


def add_subject(subject):
    grade = while_true(list(map(str, list(range(0, 101)))), "Enter your grade in " +
                       subject+":", "grade must be in a range of (0-100) please try again")
    selected_semester = while_true(list(map(str, list(
        range(1, len(semesters) + 1)))), semester, "Wrong choice ... please try again ")
    choice = semesters[int(selected_semester) - 1][0:4] + \
        semesters[int(selected_semester) - 1][5]
    subjects[subject] = (int(grade), int(choice))


def accepted():
    first_condition = False
    second_condition = False
    third_condition = False

    for i in list(subjects.items()):
        if i[0] == "CPIT 110" and int((i[1])[0]) >= 80:
            first_condition = True
        elif (i[0] == "CPCS 202" and int((i[1])[0]) >= 75) or (i[0] == "CPCS 203" and int((i[1])[0]) >= 75):
            first_condition = True
            second_condition = True
        elif i[0] == "MATH 110" and int((i[1])[0]) >= 85:
            second_condition = True
        elif (i[0] == "ELI 104" and int((i[1])[0]) >= 85) or (i[0] == "CPIT 201" and int((i[1])[0]) >= 80) or (
                i[0] == "CPIT 221" and int((i[1])[0]) >= 80):
            third_condition = True

    return first_condition and second_condition and third_condition


def ratio():
    if not accepted():
        return 0.0
    # sorting subjects based on what the student studied last
    sort_subjects_based_on_last_studied = sorted(
        subjects.items(), key=lambda x: (x[1])[1], reverse=True)
    sum_grades = 0.0
    sum_units = 0
    # to check both (MATH and CPIT 100 or CPCS 202 or CPCS 203) and (ELI 104 or CPIT 201 or CPIT 221)
    check_twice = 0
    for i in sort_subjects_based_on_last_studied:
        # here we change the the subject we calculated to "" to not calculate it again
        if i == "":
            continue
        # if we check (MATH and CPIT 100 or CPCS 202 or CPCS 203) we simply break out of the loop
        if check_twice == 1:
            break
        if i[0] == "MATH 110" and int((i[1])[0]) >= 85:
            for j in sort_subjects_based_on_last_studied:
                if j == "":
                    continue
                if j[0] == "CPIT 110" and int((j[1])[0]) >= 80:
                    sum_grades += int((i[1])[0]) * 3 + int((j[1])[0]) * 3
                    sum_units += 6
                    sort_subjects_based_on_last_studied[sort_subjects_based_on_last_studied.index(
                        i)] = ""
                    check_twice += 1

        elif i[0] == "CPIT 110" and int((i[1])[0]) >= 80:
            for j in sort_subjects_based_on_last_studied:
                if j == "":
                    continue
                if j[0] == "MATH 110" and int((j[1])[0]) >= 85:
                    sum_grades += int((i[1])[0]) * 3 + int((j[1])[0]) * 3
                    sum_units += 6
                    sort_subjects_based_on_last_studied[sort_subjects_based_on_last_studied.index(
                        i)] = ""
                    check_twice += 1
        elif i[0] == "CPCS 202" and int((i[1])[0]) >= 75:
            sum_grades += int((i[1])[0]) * 3
            sum_units += 3
            sort_subjects_based_on_last_studied[sort_subjects_based_on_last_studied.index(
                i)] = ""
            check_twice += 1
        elif i[0] == "CPCS 203" and int((i[1])[0]) >= 75:
            sum_grades += int((i[1])[0]) * 3
            sum_units += 3
            sort_subjects_based_on_last_studied[sort_subjects_based_on_last_studied.index(
                i)] = ""
            check_twice += 1

    for j in sort_subjects_based_on_last_studied:
        if j == "":
            continue
        if check_twice == 2:
            break
        if j[0] == "ELI 104" and int((j[1])[0]) >= 85:
            sum_grades += int((j[1])[0]) * 2
            sum_units += 2
            check_twice += 1
        elif j[0] == "CPIT 221" and int((j[1])[0]) >= 80:
            sum_grades += int((j[1])[0]) * 3
            sum_units += 3
            check_twice += 1
        elif j[0] == "CPIT 201" and int((j[1])[0]) >= 80:
            sum_grades += int((j[1])[0]) * 3
            sum_units += 3
            check_twice += 1
    if check_twice == 2:
        return sum_grades / sum_units
    # very rare case
    else:
        raise Exception(
            "Ooh it seems like you have made a mistake entering your data.. please try again ")


def show(students, gender):
    sorted_students = sorted(
        students.items(), key=lambda x: (x[1])[2], reverse=True)
    # make the box of name has the same len as the longest name if all the names are less than 15 then 15 is the size :)
    maximum_len = 15
    count = 0
    for j in sorted_students:
        if len((j[1])[0]) > maximum_len:
            maximum_len = len((j[1])[0])

    if len(students) > 0 and gender == "male":
        print('\n\n' + '-' * 2 + '|' + '-' * (
            maximum_len + 1) + '|' + '-' * 11 + '|' + '-' * 11 + '|' + '-' * 21 + '|' + '-' * 16 + '|')
        print(("{:<2}| {:<" + str(maximum_len) + "}| {:<10} {:<15} {:<17}| {:<15}|").format("", '', '', 'MALE SECTION',
                                                                                            '', ''))
    elif len(students) > 0:
        print('\n\n' + '-' * 2 + '|' + '-' * (
            maximum_len + 1) + '|' + '-' * 11 + '|' + '-' * 11 + '|' + '-' * 21 + '|' + '-' * 16 + '|')
        print(("{:<2}| {:<" + str(maximum_len) + "}| {:<10} {:<15} {:<17}| {:<15}|").format(" ", ' ', ' ',
                                                                                            'FEMALE SECTION',
                                                                                            ' ',
                                                                                            ''))
    else:
        return
    print('-' * 2 + '|' + '-' * (
        maximum_len + 1) + '|' + '-' * 11 + '|' + '-' * 11 + '|' + '-' * 21 + '|' + '-' * 16 + '|')
    print(("{:<2}| {:<" + str(maximum_len) + "}| {:<10}| {:<10}| {:<20}| {:<15}|").format(" ", 'Name', 'ID', 'GPA',
                                                                                          'Weighted ratio',
                                                                                          'Status'))
    print('-' * 2 + '|' + '-' * (
        maximum_len + 1) + '|' + '-' * 11 + '|' + '-' * 11 + '|' + '-' * 21 + '|' + '-' * 16 + '|')

    for i in sorted_students:
        count += 1
        if count < 16 and (i[1])[2] > 0.0:
            print(("{:<2}| {:<" + str(maximum_len) + "}| {:<10}| {:<10}| {:<20}| {:<15}|").format(count, (i[1])[0],
                                                                                                  i[0], (i[1])[
                1],
                (i[1])[
                2],
                'Accepted'))
            print('-' * 2 + '|' + '-' * (
                maximum_len + 1) + '|' + '-' * 11 + '|' + '-' * 11 + '|' + '-' * 21 + '|' + '-' * 16 + '|')
        elif count > 16 and (i[1])[2] > 0.0:
            print(("{:<2}| {:<" + str(maximum_len) + "}| {:<10}| {:<10}| {:<20}| {:<15}|").format(count, (i[1])[0],
                                                                                                  i[0], (i[1])[
                1],
                (i[1])[
                2],
                'Not Accepted'))
            print('-' * 2 + '|' + '-' * (
                maximum_len + 1) + '|' + '-' * 11 + '|' + '-' * 11 + '|' + '-' * 21 + '|' + '-' * 16 + '|')
        else:
            print(("{:<2}| {:<" + str(maximum_len) + "}| {:<10}| {:<10}| {:<20}| {:<15}|").format(count, (i[1])[0],
                                                                                                  i[0], (i[1])[
                1],
                'Not Available',
                'Not Accepted'))
            print('-' * 2 + '|' + '-' * (
                maximum_len + 1) + '|' + '-' * 11 + '|' + '-' * 11 + '|' + '-' * 21 + '|' + '-' * 16 + '|')


print('=' * 10 + ' Welcome To FCIT Transferring Students System ' + '=' * 10)
more_student = True
while more_student:
    print('-'*66)
    try:
        student_name = input("Enter your name:")
        validation_of_name_GPA_and_id(student_name, str)

        student_id = input("Enter your id: ")
        validation_of_name_GPA_and_id(student_id, int)
        add_semesters_based_on_id()

        student_gpa = input("Enter your GPA: ")
        validation_of_name_GPA_and_id(student_gpa, "GPA")

        student_gender = while_true(
            ['male', 'female', '1', '2'], "Select your gender :\n1.Male\n2.Female\n", "Wrong Choice")

        if you_have_done("CPIT 201"):
            add_subject("CPIT 201")
        if you_have_done("CPIT 221"):
            add_subject("CPIT 221")
        if you_have_done("CPCS 202"):
            add_subject("CPCS 202")
        if you_have_done("CPCS 203"):
            add_subject("CPCS 203")
        if you_have_done("CPIT 110"):
            add_subject("CPIT 110")
        if you_have_done("MATH 110"):
            add_subject("MATH 110")
        if you_have_done("ELI 104"):
            add_subject("ELI 104")

        if student_gender == '1' or student_gender.lower() == "male":
            male_students[student_id] = (student_name, student_gpa, ratio())
        else:
            female_students[student_id] = (student_name, student_gpa, ratio())
        subjects.clear()

        answer = while_true(['yes', '1', 'no', '2'],
                            "\nDo you want to add more student ? selecting \'2\' will show the result of all student"
                            "\n1.Yes\n2.No\n",
                            "Wrong choice ... please try again ")

        more_student = answer == 'yes' or answer == '1'
        if not more_student:
            show(male_students, 'male')
            show(female_students, 'female')

    except ValueError:
        print("*" * 15)
        print("\nOops that was not a number... please try again\n")
        print("*" * 15)
        pass
    except Exception as e:
        print("*" * 15)
        print("\n" + str(e) + "\n")
        print("*" * 15)
        pass
