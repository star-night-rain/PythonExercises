sum = 0
scores = []
credits = []
for i in range(5):
    project, score, credit = map(str,input().split())
    scores.append(int(score))
    credits.append(int(credit))
    sum += int(credit)
GPA = 0
for i in range(5):
    GPA += 4.0*(90 if scores[i] > 90 else scores[i])/90*credits[i]/sum
print("GPA:{:.2f}".format(GPA))