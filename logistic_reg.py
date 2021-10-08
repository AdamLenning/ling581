from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.33, random_state=42)

parameters = {'penalty':('l1', 'l2'), 'multi_class':('ovr', 'multinomial')}
svc = LogisticRegression(random_state=0, max_iter=1000000)

clf = GridSearchCV(svc, parameters, verbose=4)
clf.fit(X_train, y_train)

print('best fit coefficients:', clf.best_estimator_.coef_)
print('grid train acc:', clf.score(X_train, y_train))
print('grid test acc:', clf.score(X_test, y_test))


final_model = LogisticRegression(multi_class='multinomial', penalty='l2').fit(X_train, y_train)
print("train acc:", final_model.score(X_train, y_train))
print("test acc:", final_model.score(X_test, y_test))

