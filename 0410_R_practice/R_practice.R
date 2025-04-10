data() # 기본 제공 데이터 보기 위해
iris # iris 데이터 다운로드
summary(iris)
iris$Sepal.Length_grp = ifelse(iris$Sepal.Length<=5.843,1,2)
iris$Sepal.Width_grp = ifelse(iris$Sepal.Width<=3.057,1,2)

# 두 모집단의 분산이 다를때
t.test(iris$Sepal.Width ~iris$Sepal.Length_grp, var.equal=F) # var.equal=F 생략가능
# t = 2.3979, df = 135.08, p-value = 0.01786

# 두 모집단의 분산이 같을때
t.test(iris$Sepal.Width ~iris$Sepal.Length_grp, var.equal=T)
# t = 2.3293, df = 148, p-value = 0.02119

# 두 집단의 평균은 0.16 차이, 통계적 유의하다(대립가설 채택)
# 두 집단의 평균이 차이가 있다

chisq = iris[,c("Sepal.Length_grp","Sepal.Width_grp")]
a = table(chisq)
chisq.test(a)
# X-squared = 3.604, df = 1, p-value = 0.05764
# X-squared 차이가 없으면 0, 제곱이라서 0~양수만 존재하지만, 그냥 정규분포 생각하고 해도 된다
# df는 자유도
# p-value = 0.05764 유의수준 5%가 넘으므로 귀무가설 채택
# 통계적으로 유의하지 않다
# 추후 확인해볼 필요가 있다.(Reference, 전문가 의견 확인 필요)

lm(iris$Sepal.Length~iris$Sepal.Width) # linear model의 약자 lm
lm(iris$Sepal.Length~iris$Species)

summary(lm(iris$Sepal.Length~iris$Sepal.Width)) # width에 따른 Length의 변화
# F-statistic: 5.426 on 1 and 148 DF,  p-value: 0.02119

summary(lm(iris$Sepal.Length~iris$Species)) # Species에 따른 Length의 변화
# F-statistic:    81 on 2 and 147 DF,  p-value: < 2.2e-16
# 2 and = 2는 집단수(3) -1 이라서 2가 맞다

summary(lm(iris$Sepal.Length~as.factor(iris$Species))) # Species가 숫자형이었을때 문자형으로 바꿀때 as.factor

summary(lm(iris$Sepal.Length~iris$Sepal.Length_grp))
summary(lm(iris$Sepal.Length~as.factor(iris$Sepal.Length_grp)))
# 분산분석과 회귀분석의 차이
# summary(lm(y~x))
# x는 3개 이상의 집단이냐 연속형(무한개집단) 이냐에 따라
# 분산분석과 회귀분석으로 나뉘어진다
# x는 분산분석인 경우 x는 문자형이거나 factor형 이어야 한다