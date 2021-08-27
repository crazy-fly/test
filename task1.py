


def student_count(ug1,ug2,ug3,pg1,pg2):

    return ug1+ug2+ug3+pg1+pg2
def sf_ratio(student,faculty):

    return student/faculty

def main_fun(year):
    print("Ender the data in u1 u2 u3 p1 p2 f")    
    data = input("Enter the data for the year",year)
    data = data.split()

    Total_students = student_count(int(data[0]),int(data[1]),int(data[2]),int(data[3]),int(data[4]))
    return sf_ratio(Total_students,int(data[5]))

SFR_val = { }



while (True):
    y = int(input("year"))
    if (y<1000):
        break
    SFR_val[y] = main_fun(y)

#print(SFR_val)
no_years = 0
sum_sfr = 0
for k in SFR_val:
    sum_sfr = sum_sfr + SFR_val[k]
    no_years = no_years + 1

print("Average of Student Faculty Ratio: ",sum_sfr/no_years)
