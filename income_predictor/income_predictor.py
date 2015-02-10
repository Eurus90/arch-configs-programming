__author__ = 'lorcan'

'''
Process overview

    Create training set from data
    Create classifier using training dataset to determine separator values for each attribute
    Create test dataset
    Use classifier to classify data in test set while maintaining accuracy score



The data

The data is presented in the form of a comma-delimited text file (CSV) which has the following structure:

Listing of attributes:

1. Age: Number.
2. Workclass: Can be one of -- Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
3. fnlwgt: number. This is NOT NEEDED for our study.
4. Education: Can be one of -- Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool. This is NOT NEEDED for our study.
5. Education-number: Number -- indicates level of education.
6. Marital-status: Can be one of -- Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
7. Occupation: Can be one of -- Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
8. Relationship: Can be one of -- Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
9. Race: Can be one of -- White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
10. Sex: Either Female or Male.
11. Capital-gain: Number.
12. Capital-loss: Number.
13. Hours-per-week: Number.
14. Native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands. This is NOT NEEDED for our study.
15. Outcome for this record: Can be >50K or <=50K.
'''

import httplib2


def aboveBelowTestList(net_file):
    # get list of data for >50k, <=50k and a test data set
    list_count = 0
    total_count = 0
    above_list = []
    below_list = []
    test_list = []
    for linestring in net_file:
        total_count += 1
        list_total = int(len(net_file) * 0.75) # split data set 75, 25
        list_count += 1
        line_list = linestring.split(", ")
        if list_count < list_total:
            if line_list[-1] == ">50K":
                above_list.append(linestring)
            elif line_list[-1] == "<=50K":
                below_list.append(linestring)
        if list_total < total_count:
            test_list.append(linestring)

    return above_list, below_list, test_list


def specialTest(net_file):
    # Found extra data set to verify my results
    total_count = 0
    test_list = []
    for linestring in net_file:
        total_count += 1
        test_list.append(linestring)

    return test_list


def attribList(above_below_list, i):
    # get list of values for each attribute
    undef_list = []
    for linestring in above_below_list:
        line_list = linestring.split(", ")
        if len(line_list) == 15:
            for attrib in line_list:
                if i == 0 or i == 4 or i == 10 or i == 11 or i == 12:
                    # all int value attributes
                    if attrib == line_list[i]:
                        word = int(attrib)
                        undef_list.append(word)
                else:
                    # all str value attributes
                    if attrib == line_list[i]:
                        undef_list.append(attrib)

    return undef_list


def midPointInt(list_under, list_over):
    # find midpoint value for the int value attributes
    sum = 0
    avg_under = 0
    avg_over = 0
    for i in list_under:
        sum += i
        avg_under = sum // len(list_under)
    for i in list_over:
        sum += i
        avg_over = sum // len(list_over)

    mid_point = (avg_under + avg_over) // 2

    return mid_point


def strAboveValueList(list_under, list_over):
    # make list of str value attribute words that would make you more likely to be in the above 50k group
    counts_under = {}
    counts_over = {}
    above_list = []
    # count occurrences of words in the above list and the below list
    for word in list_under:
        if word in counts_under:
            counts_under[word] += 1 / len(list_under)
        else:
            counts_under[word] = 1 / len(list_under)
    for word in list_over:
        if word in counts_over:
            counts_over[word] += 1 / len(list_over)
        else:
            counts_over[word] = 1 / len(list_over)
    # add word to above list if it makes you more likely to be in the above 50k group
    for key in counts_under:
        try:
            if counts_under[key] < counts_over[key]:
                above_list.append(str(key))
        except KeyError:
            continue

    return above_list


def testAccuracy(test_list1, int_list, str_list):
    # test accuracy
    total_count = 0
    right_count = 0
    above_prediction = 0
    for linestring in test_list1:
        total_count += 1
        sum = 0
        new_linelist = []
        i_list_str = [1, 5, 6, 7, 8, 9]
        i_list_int = [0, 4, 10, 11, 12]
        line_list = linestring.split(", ")
        # account for difference in the SpecialTest data
        if line_list[-1] == ">50K.":
            line_list[-1] = ">50K"
        elif line_list[-1] == "<=50K.":
            line_list[-1] = "<=50K"
        # account for errors in the data
        if len(line_list) == 15:
            # create value to verify my prediction
            if line_list[-1] == ">50K":
                real_value = 1
            elif line_list[-1] == "<=50K":
                real_value = 0
            else:
                continue
            for i in range(15):
                if i in i_list_int:
                    # int values, if the value is greater than the attribute midpoint +1
                    if int(line_list[i]) >= int(int_list[i]):
                        new_linelist.append(1)
                    else:
                        new_linelist.append(0)
                if i in i_list_str:
                    # str values, if the the attribute word is in the list of word that make
                    # you more likely to be in the above 50k group +1
                    if line_list[i] in str_list[i]:
                        new_linelist.append(1)
                    else:
                        new_linelist.append(0)
            for i in new_linelist:
                num = int(i)
                sum += num
            if sum >= 6:
                above_prediction += 1
                prediction = 1
            else:
                prediction = 0
            if prediction == real_value:
                right_count += 1
    percentage = right_count / (total_count / 100)

    return percentage


def main():
    data_set_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"   # Variable to hold file
    test_set_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test"   # URLs

    h = httplib2.Http(".cache")
    data_set_headers, data_set = h.request(data_set_url)
    test_set_headers, test_set = h.request(test_set_url)

    data_set = data_set.decode().split("\n")   # Making list of lines by splitting on the newline character
    test_set = test_set.decode().split("\n")

    above_list, below_list, test_list = aboveBelowTestList(data_set)   # make list of lines with above 50k, below 50k
    special_test_list = specialTest(test_set)                          # and for testing


    age_list_over = attribList(above_list, 0)  # make list of ages with above 50k value
    age_list_under = attribList(below_list, 0)  # make list of ages with below 50k value
    age_mid = midPointInt(age_list_under, age_list_over)  # get the midpoint value for age to use for testing

    workclass_list_over = attribList(above_list, 1)
    workclass_list_under = attribList(below_list, 1)
    workclass_above_value_list = strAboveValueList(workclass_list_under, workclass_list_over)
    # make a list of all the workclass variables that would make someone more likely to be in the above 50k bracket

    education_list_over = attribList(above_list, 4)
    education_list_under = attribList(below_list, 4)
    education_mid = midPointInt(education_list_under, education_list_over)

    marital_status_list_over = attribList(above_list, 5)
    marital_status_list_under = attribList(below_list, 5)
    marital_status_above_value_list = strAboveValueList(marital_status_list_under, marital_status_list_over)

    occupation_list_over = attribList(above_list, 6)
    occupation_list_under = attribList(below_list, 6)
    occupation_above_value_list = strAboveValueList(occupation_list_under, occupation_list_over)

    relationship_list_over = attribList(above_list, 7)
    relationship_list_under = attribList(below_list, 7)
    relationship_above_value_list = strAboveValueList(relationship_list_under, relationship_list_over)

    race_list_over = attribList(above_list, 8)
    race_list_under = attribList(below_list, 8)
    race_above_value_list = strAboveValueList(race_list_under, race_list_over)

    gender_list_over = attribList(above_list, 9)
    gender_list_under = attribList(below_list, 9)
    gender_above_value_list = strAboveValueList(gender_list_under, gender_list_over)

    capital_gain_list_over = attribList(above_list, 10)
    capital_gain_list_under = attribList(below_list, 10)
    capital_gain_mid = midPointInt(capital_gain_list_under, capital_gain_list_over)

    capital_loss_list_over = attribList(above_list, 11)
    capital_loss_list_under = attribList(below_list, 11)
    capital_loss_mid = midPointInt(capital_loss_list_under, capital_loss_list_over)

    hours_per_week_list_over = attribList(above_list, 12)
    hours_per_week_list_under = attribList(below_list, 12)
    hours_per_week_mid = midPointInt(hours_per_week_list_under, hours_per_week_list_over)

    int_list = [age_mid, 21, 22, 23, education_mid, 25, 26, 27, 28, 29, capital_gain_mid, capital_loss_mid,
                hours_per_week_mid]
    # make a list of the midpoint values, the numbers fill in empty space in the list, used for referencing in the
    # testAccuracy function
    str_list = [20, workclass_above_value_list, 22, 23, 24, marital_status_above_value_list,
                occupation_above_value_list, relationship_above_value_list, race_above_value_list, 
                gender_above_value_list]  # same as int_list but it is a list of the above_value_lists

    accuracy = testAccuracy(test_list, int_list, str_list)  # get the accuracy of my testing as a percentage
    special = testAccuracy(special_test_list, int_list, str_list)  # separate test data accuracy
    dataset_accur = testAccuracy(data_set, int_list, str_list)
    # print accuracy
    print("\n##################################################################\n\n!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!\n\n\n         Test 25% list Accuracy:   %",
          accuracy, "\n\n\n!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!\n\n##################################################################")
    print("\n!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!\n\n\n         Separate Test Set Accuracy:   %",
          special, "\n\n\n!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!\n\n##################################################################")
    print("\n!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!\n\n\n         Data Set Accuracy:   %",
          dataset_accur, "\n\n\n!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!\n\n##################################################################")

if __name__ == '__main__':
    main()

