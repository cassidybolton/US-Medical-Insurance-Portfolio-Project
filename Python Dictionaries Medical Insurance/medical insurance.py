import csv

# set up variables and import csv into lists

ages = []
sexes = []
bmis = []
children = []
smoker_status = []
regions = []
charges = []

with open('insurance.csv', newline='') as insurance_csv:
    insurance_dict = csv.DictReader(insurance_csv)
    for row in insurance_dict:
        ages.append(int(row['age']))
        sexes.append(row['sex'])
        bmis.append(float(row['bmi']))
        children.append(int(row['children']))
        smoker_status.append(row['smoker'])
        regions.append(row['region'])
        charges.append(float(row['charges']))

# print(bmis)

# find the average age of the patients

avg_age = round(sum(ages) / len(ages), 2)
print("The average age of patients in the dataset is " + str(avg_age))

# count the number of men and women in the dataset
num_women = 0
num_men = 0

for sex in sexes:
    if sex == 'female':
        num_women += 1
    if sex == 'male':
        num_men += 1

print("There are " + str(num_women) + " women and " + str(num_men) + " men in the dataset")

# find the average bmi of all patients, just men, and just women

avg_bmi = round(sum(bmis) / len(bmis), 2)
tot_men_bmi = 0
tot_women_bmi = 0

for index, sex in enumerate(sexes):
    if sex == 'male':
        tot_men_bmi += bmis[index]
    if sex == 'female':
        tot_women_bmi += bmis[index]

avg_men_bmi = round(tot_men_bmi / num_men, 2)
avg_women_bmi = round(tot_women_bmi / num_women, 2)

print("The overall average BMI is " + str(avg_bmi) + ". The average BMI for men is " + str(round(avg_men_bmi, 2)) + " and the average BMI for women is " + str(round(avg_women_bmi, 2)) + ".")

# count the total number of children that the patients have, and the average number of children

total_children = 0

for child in children:
    total_children += child

avg_children = round(total_children / len(children), 2)

print("There are a total of " + str(total_children) + " children among all patients, with the average patient having " + str(avg_children) + " children.")

# how many patients are smokers
num_smokers = 0

for smoker in smoker_status:
    if smoker == 'yes':
        num_smokers += 1

per_smoker = round((num_smokers / len(smoker_status))* 100, 2)

print("There are " + str(num_smokers) + " smokers in the dataset, out of " + str(len(smoker_status)) + " total patients (" + str(per_smoker) + "%)")

# what is the largest region? smallest?
regions_count = {}
for region in regions:
    if region not in regions_count:
        regions_count[region] = 0
    regions_count[region] += 1

print("There are " + str(regions_count['northeast']) + " patients in the Northeast, " + str(regions_count['northwest']) + " patients in the Northwest, " + str(regions_count['southeast']) + " patients in the Southeast, and " + str(regions_count['southwest']) + " patients in the Southwest.")

max_region = ''
max_region_count = 0
min_region = ''
min_region_count = float('inf')


for key, value in regions_count.items():
    if value > max_region_count:
        max_region_count = value
        max_region = key
    if value < min_region_count:
        min_region_count = value
        min_region = key

print("The largest region is the " + max_region + " region, and the smallest region is the " + min_region + " region.")

# find the average insurance charge overall, by region, by smoker status, by number of children

total_insurance = 0
for num in charges:
    total_insurance += num

avg_insurance = round(total_insurance / len(charges), 2)

print("The average cost of insurance for all patients is $" + str(avg_insurance))

totalcost_byregion = {}
avgcost_byregion = {}

for index, region in enumerate(regions):
    if region not in totalcost_byregion:
        totalcost_byregion[region] = 0
    totalcost_byregion[region] += charges[index]

#print(totalcost_byregion)

for region, total in totalcost_byregion.items():
    avgcost_byregion[region] = round(total / regions_count[region], 2)

#print(avgcost_byregion)

for region, avg in avgcost_byregion.items():
    print("The average cost for patients in the " + region + " region is $" + str(avg))

totalcost_smoker = 0
totalcost_nonsmoker = 0

# print(smoker_status)

for index, status in enumerate(smoker_status):
    if status == 'yes':
        totalcost_smoker += charges[index]
    if status == 'no':
        totalcost_nonsmoker += charges[index]

avgcost_smoker = round(totalcost_smoker / smoker_status.count('yes'), 2)
avgcost_nonsmoker = round(totalcost_nonsmoker / smoker_status.count('no'), 2)

print("The average cost for a patient who smokes is $" + str(avgcost_smoker) + " and $" + str(avgcost_nonsmoker) + " for patients who do not smoke")

# average by num of children

cost_bychildren = {}
avgcost_bychildren = {}

for index, child in enumerate(children):
    if child not in cost_bychildren:
        cost_bychildren[child] = 0
    cost_bychildren[child] += charges[index]

for num, cost in cost_bychildren.items():
    avgcost_bychildren[num] = round(cost / children.count(num), 2)
    print("The average cost for a patient with " + str(num) + " children is $" + str(avgcost_bychildren[num]))