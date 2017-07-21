import numpy as np
import pylab as pl
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor


from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.neighbors import NearestNeighbors


def load_data():


    boston = datasets.load_boston()
    return boston


def explore_city_data(city_data):

    housing_prices = city_data.target
    housing_features = city_data.data


    print
    'size of data:', housing_features.shape[0]


    print
    'number of features:', housing_features.shape[1]


    print
    'minimum value:', np.min(housing_prices)


    print
    'maximum value:', np.max(housing_prices)


    print
    'mean value:', np.mean(housing_prices)


    print
    'median value:', np.median(housing_prices)


    print
    'standard deviation:', np.std(housing_prices)


def performance_metric(label, prediction):



    return mean_squared_error(label, prediction)


def split_data(city_data):

    X, y = city_data.data, city_data.target


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, y_train, X_test, y_test


def learning_curve(depth, X_train, y_train, X_test, y_test):

    sizes = np.linspace(1, len(X_train), 50)
    train_err = np.zeros(len(sizes))
    test_err = np.zeros(len(sizes))

    print
    "Decision Tree with Max Depth: "
    print
    depth

    for i, s in enumerate(sizes):

        regressor = DecisionTreeRegressor(max_depth=depth)
        regressor.fit(X_train[:s], y_train[:s])


        train_err[i] = performance_metric(y_train[:s], regressor.predict(X_train[:s]))
        test_err[i] = performance_metric(y_test, regressor.predict(X_test))


    learning_curve_graph(sizes, train_err, test_err, depth)


def learning_curve_graph(sizes, train_err, test_err, depth):


    pl.figure()
    pl.title('Decision Trees: Performance vs Training Size (Max Depth: %d)' % depth)
    pl.plot(sizes, test_err, lw=2, label='test error')
    pl.plot(sizes, train_err, lw=2, label='training error')
    pl.legend()
    pl.xlabel('Training Size')
    pl.ylabel('Error')
    pl.show()


def model_complexity(X_train, y_train, X_test, y_test):

    print
    "Model Complexity: "


    max_depth = np.arange(1, 25)
    train_err = np.zeros(len(max_depth))
    test_err = np.zeros(len(max_depth))

    for i, d in enumerate(max_depth):

        regressor = DecisionTreeRegressor(max_depth=d)


        regressor.fit(X_train, y_train)


        train_err[i] = performance_metric(y_train, regressor.predict(X_train))


        test_err[i] = performance_metric(y_test, regressor.predict(X_test))


    model_complexity_graph(max_depth, train_err, test_err)


def model_complexity_graph(max_depth, train_err, test_err):


    pl.figure()
    pl.title('Decision Trees: Performance vs Max Depth')
    pl.plot(max_depth, test_err, lw=2, label='test error')
    pl.plot(max_depth, train_err, lw=2, label='training error')
    pl.legend()
    pl.xlabel('Max Depth')
    pl.ylabel('Error')
    pl.show()


def find_nearest_neighbor_indexes(x, X):  # x is your vector and X is the data set.
    neigh = NearestNeighbors(n_neighbors=10)
    neigh.fit(X)
    distance, indexes = neigh.kneighbors(x)
    return indexes


def fit_predict_model(city_data):

    X, y = city_data.data, city_data.target


    regressor = DecisionTreeRegressor()

    parameters = {'max_depth': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}


    scorer = make_scorer(mean_squared_error, greater_is_better=False)


    reg = GridSearchCV(regressor, parameters, scoring=scorer)


    print
    "Final Model"
    print
    reg.fit(X, y)
    print
    "Best Estimator"
    print
    reg.best_estimator_
    print
    "Best Score"
    print
    reg.best_score_
    print
    "Best Parameters"
    print
    reg.best_params_


    x = [11.95, 0.00, 18.100, 0, 0.6590, 5.6090, 90.00, 1.385, 24, 680.0, 20.20, 332.09, 12.13]
    est = reg.best_estimator_
    print
    "House: " + str(x)
    print
    "Prediction: " + str(est.predict(x))

    pred = reg.predict(X)
    print
    "Min", np.min(pred)
    print
    "Max", np.max(pred)
    print
    "Mean", np.mean(pred)
    print
    "Median", np.median(pred)
    print
    "Standard deviation", np.std(pred)

    indexes = find_nearest_neighbor_indexes(x, X)
    sum_prices = []
    for i in indexes:
        sum_prices.append(y[i])
        neighbor_avg = np.mean(sum_prices)
    print
    "Nearest Neighbors average: " + str(neighbor_avg)


def main():



    city_data = load_data()


    explore_city_data(city_data)


    X_train, y_train, X_test, y_test = split_data(city_data)


    max_depths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for max_depth in max_depths:
        learning_curve(max_depth, X_train, y_train, X_test, y_test)


    model_complexity(X_train, y_train, X_test, y_test)

    
    fit_predict_model(city_data)


if __name__ == "__main__":
    main()