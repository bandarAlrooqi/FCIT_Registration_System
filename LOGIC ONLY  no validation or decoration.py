def calculate():
    units = 0
    grades = 0.0
    checked = 0
    for i in sorted(subjects.items(), key=lambda x: (x[1])[1], reverse=True):
        if checked == 1:
            break
        if i[0] == "MATH 110" and int((i[1])[0]) >= 85:
            for j in subjects.items():
                if j[0] == "CPIT 110" and int((i[1])[0]) >= 80:
                    units += 6
                    grades += (int((i[1])[0]) * 3) + (int((j[1])[0]) * 3)
                    checked += 1
        elif i[0] == "MATH 110" and int((i[1])[0]) >= 85:
            for j in subjects.items():
                if j[0] == "CPIT 110" and int((i[1])[0]) >= 80:
                    units += 6
                    grades += (int((i[1])[0]) * 3) + (int((j[1])[0]) * 3)
                    checked += 1
        elif i[0] == "CPCS 202" and int((i[1])[0]) >= 75:
            units += 3
            grades += int((i[1])[0]) * 3
            checked += 1
        elif i[0] == "CPCS 203" and int((i[1])[0]) >= 75:
            units += 3
            grades += int((i[1])[0]) * 3
            checked += 1
    for i in sorted(subjects.items(), key=lambda x: (x[1])[1], reverse=True):
        if checked == 2:
            break
        if i[0] == "ELI 104" and int((i[1])[0]) >= 85:
            units += 2
            grades += int((i[1])[0]) * 2
            checked += 1
        elif i[0] == "CPIT 201" and int((i[1])[0]) >= 80:
            units += 3
            grades += int((i[1])[0]) * 3
            checked += 1
        elif i[0] == "CPIT 221" and int((i[1])[0]) >= 80:
            units += 3
            grades += int((i[1])[0]) * 3
            checked += 1

    return grades / units


def _print(_dict):
    count = 0
    for i in sorted(_dict.items(), key=lambda x: (x[1])[2], reverse=True):
        count += 1
        print(f"{(i[1])[0]},{i[0]},{(i[1])[1]},{(i[1])[2]},{(i[1])[3]}")
        if count == 15:
            break
    exit()


male = dict()
female = dict()

while True:

    name = input("Enter your name:")
    _id = input("Enter your ID:")
    gpa = input("Enter your GPA:")
    gender = input("Enter your gender (m,f) :")
    subjects = dict()
    requirements = [False, False, False, False]

    while True:
        subject = input("Enter your subject e.g (MATH 110): ")
        grade = input("Enter your grade:")
        term = input("Enter term e.g (2019-1)")
        subjects[subject.upper()] = (grade, (term[0:4] + term[5]))

        if input("Do you want to add more subjects ? (y,n)") == 'n':
            if 3.75 <= float(gpa) <= 5:
                requirements[0] = True
            if "MATH 110" in subjects and int((subjects["MATH 110"])[0]) >= 85:
                requirements[2] = True
            if "ELI 104" in subjects and int((subjects["ELI 104"])[0]) >= 85:
                requirements[3] = True
            if "CPCS 202" in subjects and int((subjects["CPCS 202"])[0]) >= 75:
                requirements[1] = True
                requirements[2] = True
            if "CPCS 203" in subjects and int((subjects["CPCS 203"])[0]) >= 75:
                requirements[1] = True
                requirements[2] = True
            if "CPIT 110" in subjects and int((subjects["CPIT 110"])[0]) >= 80:
                requirements[1] = True
            if "CPIT 201" in subjects and int((subjects["CPIT 201"])[0]) >= 80:
                requirements[3] = True
            if "CPIT 221" in subjects and int((subjects["CPIT 221"])[0]) >= 80:
                requirements[3] = True

            break

    if False not in requirements and gender == 'm':
        male[_id] = (name, gender.upper(), calculate(), "Accepted")

    elif False not in requirements and gender == 'f':
        female[_id] = (name, gender.upper(), calculate(), "Accepted")

    if input("Do you want to add more students ? (y,n)") == 'n':
        _print(male)
        _print(female)
    subjects.clear()
