import sys
import os
import random
import time

# Range Parameter
RANGE_AGE_GROUP = 10
RANGE_EDUCATION = 4
RANGE_GENDER = 2
RANGE_HOME_COUNTRY = 100
RANGE_INTERESTED_IN = 3
RANGE_LANGUAGES = 50
RANGE_RELATIONSHIP_STATUS = 2
RANGE_RELIGION = 20
RANGE_WORK = 50
RANGE_POLITICAL = 10
# Mu Parameter
MU_AGE_GROUP = 5
MU_EDUCATION = 3
MU_HOME_COUNTRY = 50
MU_LANGUAGES = 25
MU_RELIGION = 10
MU_POLITICAL = 5
# Sigma Parameter
SIGMA_AGE_GROUP = 2.5
SIGMA_EDUCATION = 1.25
SIGMA_HOME_COUNTRY = 25
SIGMA_LANGUAGES = 12.5
SIGMA_RELIGION = 5
SIGMA_POLITICAL = 2.5
# Other Parameter
NUMBER_OF_USER = 1000000

# Variables Declaration
age_group_value = 0.0
education_value = 0.0
gender_value = 0
home_country_value = 0.0
interested_in_value = 0
languages_values = 0.0
relationship_status_value = 0
religion_value = 0.0
work_value = 0
political_value = 0.0

# Values for FD
valuesPolitical = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Generation Process

start = time.time()
outFile = open("out.csv", "w")
for i in range(1, NUMBER_OF_USER + 1):
    age_group_value = 0.0
    education_value = 0.0
    gender_value = 0
    home_country_value = 0.0
    interested_in_value = 0
    languages_values = 0.0
    relationship_status_value = 0
    religion_value = 0.0
    work_value = 0
    political_value = 0.0
    # Generation Age
    while age_group_value == 0 or age_group_value > RANGE_AGE_GROUP:
        age_group_value = random.normalvariate(MU_AGE_GROUP, SIGMA_AGE_GROUP)
    # Generation education
    while education_value == 0 or education_value > RANGE_EDUCATION:
        education_value = random.normalvariate(MU_EDUCATION, SIGMA_EDUCATION)
    # Generation gender
    gender_value = random.randrange(1, RANGE_GENDER + 1)
    # Generation home country
    while home_country_value == 0 or home_country_value > RANGE_HOME_COUNTRY:
        home_country_value = random.normalvariate(MU_HOME_COUNTRY, SIGMA_HOME_COUNTRY)
        # Generation interested in
        interested_in_value = random.randrange(0, RANGE_INTERESTED_IN + 1)
    # Generation languages
    while languages_values == 0 or languages_values > RANGE_LANGUAGES:
        languages_values = random.normalvariate(MU_LANGUAGES, SIGMA_LANGUAGES)
    # Generation relationship status
    relationship_status_value = random.randrange(1, 3)
    # Generation Work
    work_value = random.randrange(1, RANGE_WORK + 1)
    # Generation Religion
    while religion_value == 0 or religion_value > RANGE_RELIGION:
        religion_value = random.normalvariate(MU_RELIGION, SIGMA_RELIGION)
    # Generation Political
    political_value = valuesPolitical[int(age_group_value)]
    # while political_value == 0 or political_value > RANGE_POLITICAL:
    #     political_value = random.normalvariate(MU_POLITICAL, SIGMA_POLITICAL)
    outFile.write("%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d\n" % (
        i, age_group_value, education_value, gender_value, home_country_value, interested_in_value,
        languages_values, relationship_status_value, work_value, religion_value, political_value))
end = time.time()
elapsed_time = end - start
print("Time: %f" % elapsed_time)
