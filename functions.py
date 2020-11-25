import csv

def getRegion():
    f = open("option.csv", "r", encoding="utf-8")
    file_data = csv.reader(f)

    region_data = ""

    flag = 0
    for line in file_data:
        if flag == 1:
            region_data = line[0]
        flag += 1

    if region_data == "서울특별시" or region_data == "서울":
        return "01"
    elif region_data == "부산광역시" or region_data == "부산":
        return "02"
    elif region_data == "대구광역시" or region_data == "대구":
        return "03"
    elif region_data == "인천광역시" or region_data == "인천":
        return "04"
    elif region_data == "광주광역시" or region_data == "광주":
        return "05"
    elif region_data == "대전광역시" or region_data == "대전":
        return "06"
    elif region_data == "울산광역시" or region_data == "울산":
        return "07"
    elif region_data == "세종특별자치시" or region_data == "세종":
        return "08"
    elif region_data == "경기도" or region_data == "경기":
        return "10"
    elif region_data == "강원도" or region_data == "강원":
        return "11"
    elif region_data == "충청북도":
        return "12"
    elif region_data == "충청남도":
        return "13"
    elif region_data == "전라북도":
        return "14"
    elif region_data == "전라남도":
        return "15"
    elif region_data == "경상북도":
        return "16"
    elif region_data == "경상남도":
        return "17"
    elif region_data == "제주특별자치도" or region_data == "제주" or region_data == "제주도":
        return "18"

def getSchoolLevel():
    f = open("option.csv", "r", encoding="utf-8")
    file_data = csv.reader(f)

    school_level = ""

    flag = 0
    for line in file_data:
        if flag == 1:
            school_level = line[1]
        flag += 1

    if school_level == "유치원":
        return "1"
    elif school_level == "초등학교":
        return "2"
    elif school_level == "중학교":
        return "3"
    elif school_level == "고등학교":
        return "4"
    elif school_level == "특수학교":
        return "5"

def getSchoolName():
    f = open("option.csv", "r", encoding="utf-8")
    file_data = csv.reader(f)

    school_name = ""

    flag = 0
    for line in file_data:
        if flag == 1:
            school_name = line[2]
        flag += 1

    return school_name

def getUserName():
    f = open("option.csv", "r", encoding="utf-8")
    file_data = csv.reader(f)

    user_name = ""

    flag = 0
    for line in file_data:
        if flag == 1:
            user_name = line[3]
        flag += 1

    return user_name

def getUserBirth():
    f = open("option.csv", "r", encoding="utf-8")
    file_data = csv.reader(f)

    user_birth = ""

    flag = 0
    for line in file_data:
        if flag == 1:
            user_birth = line[4]
        flag += 1

    return user_birth

def getUserPassword():
    f = open("option.csv", "r", encoding="utf-8")
    file_data = csv.reader(f)

    user_password = ""

    flag = 0
    for line in file_data:
        if flag == 1:
            user_password = line[5]
        flag += 1

    return user_password