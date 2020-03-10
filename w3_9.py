# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
exam_st_date_str = str(exam_st_date[0]) + "/" + str(exam_st_date[1]) + "/" + str(exam_st_date[2])
print(exam_st_date_str)


exam_st_date_str2 = "{0}/{1}/{2}".format(*exam_st_date)
print(exam_st_date_str2)
