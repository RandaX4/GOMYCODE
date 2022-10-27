df<-read.csv("C:/Users/EXTRA/Downloads/HR_comma_sep.csv")
cor(df$average_montly_hours,df$number_project)
linearMod <- lm(average_montly_hours~number_project,data=df)
print(linearMod)
