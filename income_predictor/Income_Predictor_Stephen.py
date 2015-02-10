__author__ = 'Stephen.Maguire'

''' The purpose of this code is create a predictor using a data-set from the UCI Machine-Learning Repository we can
predict based on a number of factors whether someone's income will be greater than or less than $50,000. In this
problem I will consider attributes of records and separate these into two classes < $50,000 and >= $50,000
'''
'''Create a training set from the given data on the net, this will allow me to look for patterns that will indicate
classification. These patterns can then be applied against new data to predict outcomes. '''

import httplib2

# Variable for data set URL
data_set_URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
# percent = 75

"""List of attributes:
There will be only two possible outcomes from my predictor: "Over 50,000" or "Under 50,000"

Listing of attributes:

1. Age, which is continuous
2. Workclass: which is one of either; Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov,
Without-pay, Never-worked.
3. fnlwgt: number. This is not included in my predictor.
4. Education: Can be one of -- Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th,
7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool. This is NOT NEEDED for our study.
5. Education-number: Number -- indicates level of education.
6. Marital-status: Can be one of -- Married-civ-spouse, Divorced, Never-married, Separated, Widowed,
Married-spouse-absent, Married-AF-spouse.
7. Occupation: Can be one of -- Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty,
Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv,
 Armed-Forces.
8. Relationship: Can be one of -- Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
9. Race: Can be one of -- White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
10. Sex: Either Female or Male.
11. Capital-gain: Number.
12. Capital-loss: Number.
13. Hours-per-week: Number.
14. Native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India,
 Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal,
  Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland,
  Thailand, Yugoslavia, El-Salvador, Trinidad & Tobago, Peru, Hong Kong, Holland-Netherlands. This is NOT NEEDED.
  """


# Create two dictionaries, one for over 50,000 and one for under 50,000 to each attribute that doesn't contain numbers
# Set counts

test_set_list = []
dict_working_class_over50k = {}
dict_marital_status_over50k = {}
dict_occupation_over50k = {}
dict_relationship_status_over50k = {}
dict_race_over50k = {}
dict_sex_over50k = {}

dict_working_class_under50k = {}
dict_marital_status_under50k = {}
dict_occupation_under50k = {}
dict_relationship_status_under50k = {}
dict_race_under50k = {}
dict_sex_under50k = {}

row_count = 0
over_count = 0
under_count = 0

"""Get data set from the net (bytes format) and change the numbers into ints and the rest into a string
and separate the attributes into over 50,000 and under 50,000"""
try:
    h = httplib2.Http(".cache")
    headers, fh = h.request(data_set_URL)
    fh = fh.decode().split("\n")

    for row in fh:
        try:
            row = row.strip()
            row = row.split(",")
            row[0] = int(row[0])
            row[2] = None
            row[3] = None
            row[4] = int(row[4])
            row[10] = int(row[10])
            row[11] = int(row[11])
            row[12] = int(row[12])
            row[13] = None

            if row[-1].lstrip() == "<=50,000":
                under_count += 1

            # Count the non-numeric attributes using dictionaries

                if row[1] in dict_working_class_over50k:
                    dict_working_class_over50k[row[1]] += 1
                else:
                    dict_working_class_over50k[row[1]] = 1

                if row[5] in dict_marital_status_over50k:
                    dict_marital_status_over50k[row[5]] += 1
                else:
                    dict_marital_status_over50k[row[5]] = 1

                if row[6] in dict_occupation_over50k:
                    dict_occupation_over50k[row[6]] += 1
                else:
                    dict_occupation_over50k[row[6]] = 1

                if row[7] in dict_relationship_status_over50k:
                    dict_relationship_status_over50k[row[7]] += 1
                else:
                    dict_relationship_status_over50k[row[7]] = 1

                if row[8] in dict_race_over50k:
                    dict_race_under50k[row[8]] += 1
                else:
                    dict_race_over50k[row[8]] = 1

                if row[9] in dict_sex_over50k:
                    dict_sex_over50k[row[9]] += 1
                else:
                    dict_sex_over50k[row[9]] = 1

            if row[-1].lstrip() == ">50,000":
                over_count += 1

                if row[1] in dict_working_class_under50k:
                    dict_working_class_under50k[row[1]] += 1
                else:
                    dict_working_class_under50k[row[1]] = 1

                if row[5] in dict_marital_status_under50k:
                    dict_marital_status_under50k[row[5]] += 1
                else:
                    dict_marital_status_under50k[row[5]] = 1

                if row[6] in dict_occupation_under50k:
                    dict_occupation_under50k[row[6]] += 1
                else:
                    dict_occupation_under50k[row[6]] += 1

                if row[7] in dict_relationship_status_under50k:
                    dict_relationship_status_under50k[row[7]] += 1
                else:
                    dict_relationship_status_under50k[row[7]] = 1

                if row[8] in dict_race_under50k:
                    dict_race_under50k[row[8]] += 1
                else:
                    dict_race_under50k[row[8]] = 1

                if row[9] in dict_sex_under50k:
                    dict_sex_under50k[row[9]] += 1
                else:
                    dict_sex_under50k[row[9]] = 1

                test_set_list.append(row)
                row_count += 1

                print(dict_marital_status_under50k)
        except ValueError as v:
            print(v)
    else:
        pass
        # Not sure if this is the right except function to have in here


except ValueError as v:
    print(v)

for row in test_set_list:
    if row[-1].lstrip() == "> 50,000":
        row[1] = dict_working_class_over50k[row[1]] / over_count
        row[5] = dict_marital_status_over50k[row[5]] / over_count
        row[6] = dict_occupation_over50k[row[6]] / over_count
        row[7] = dict_relationship_status_over50k[row[7]] / over_count
        row[8] = dict_race_over50k[row[8]] / over_count
        row[9] = dict_sex_over50k[row[9]] / over_count

    elif row[-1].lstrip() == "<= 50,000":
        row[1] = dict_working_class_under50k[row[1]] / under_count
        row[5] = dict_marital_status_under50k[row[5]] / under_count
        row[6] = dict_occupation_under50k[row[6]] / under_count
        row[7] = dict_relationship_status_under50k[row[7]] / under_count
        row[8] = dict_race_under50k[row[8]] / under_count
        row[9] = dict_sex_under50k[row[9]] / under_count

    else:
        pass

print(test_set_list)
return test_set_list

# From here on I don't really know how to tackle it at all

def main():

# make a list of tuples from the raw data
data_list = create_data(data_set_URL)
# break out our data set into a training and test set
# not sure if I'm right with this test_set_list = data_list[:int(len(data_list)*/ percent

"""Think this is what I need to do with for the classifier Average age / total number of count. Get the midpoint. Midpoint figure classifies it into under or over 50k.
 single row of averages for under and one for over. Average the rows with numbers and combine the ones for over and ones
 for under to form the midpoints
 splitting the difference in the value ... Create a single row that contains all the midpoint values"""

if __name__ == '__main__':
    main()























