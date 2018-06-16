import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model as lm
from sklearn import model_selection
from sklearn import preprocessing as pp
from sklearn import svm, pipeline, ensemble, datasets, feature_selection

score_funs = ['explained_variance', 'neg_mean_squared_error', 'r2']


class ModelSelector:
    def __init__(self, canvas):
        self.canvas = canvas
        self.figure = canvas.figure
        self.show_only_best, self.scorer, self.scaler, self.X_scaled = None, None, None, None
        self.boston = datasets.load_boston()
        self.n_features = 5
        self.target_name = 'MEDV'
        df = pd.DataFrame(data=self.boston.data, columns=self.boston.feature_names)
        df[self.target_name] = self.boston.target

        self.X = df.iloc[:, :-1]
        self.y = df.iloc[:, -1]
        self.selected_features = None

        self.select_features()
        lr = lm.LinearRegression()
        svr = svm.SVR()
        ridge_reg = lm.RidgeCV(alphas=np.float_power(np.array([10] * 21), np.arange(-10, 11)))
        random_forest_reg = ensemble.RandomForestRegressor()
        poly_reg = pipeline.Pipeline([('poly', pp.PolynomialFeatures(degree=2)), ('linear', lm.LinearRegression())])
        self.models = {'OLS': lr, 'Ridge': ridge_reg, 'Support Vector': svr, 'Random forest': random_forest_reg,
                       'Polynomial': poly_reg}

        self.n_cols = self.n_features
        n_all_rows = len(self.models) + 2
        self.grid = plt.GridSpec(n_all_rows, self.n_cols)
        self.cur_row = -1

    def select_features(self):
        features = self.boston.feature_names
        feature_filter = feature_selection.SelectKBest(feature_selection.mutual_info_regression, k=self.n_features).fit(
            self.X, self.y)
        self.selected_features = [features[i] for i in feature_filter.get_support(indices=True)]
        self.X = feature_filter.transform(self.X)
        print(self.boston.DESCR)

        self.scaler = pp.StandardScaler().fit(self.X)
        self.X_scaled = self.scaler.transform(self.X)

    def select_model(self):
        self.cur_row = -1
        best_model = ''
        best_metric = - np.inf
        ind = np.arange(len(self.models))
        model_scores = []
        model_names = []
        for name in self.models:
            model_names.append(name)
            metric = self.use_model(self.models[name])
            model_scores.append(metric)
            if best_metric < metric:
                best_metric = metric
                best_model = name
        all_model_names = model_names
        if self.show_only_best:
            model_names = [best_model]
        for name in model_names:
            self.visualize(name, self.n_cols)
        # bar plot of model perfomance with selected metric
        self.cur_row += 1
        ax = self.figure.add_subplot(self.grid[self.cur_row: self.cur_row + 2, :])
        ax.barh(ind, model_scores)
        ax.set_xlabel(self.scorer)
        ax.set_yticks(ind)
        ax.set_yticklabels(all_model_names)
        self.canvas.draw()

    def visualize(self, model_name, n_cols):
        model = self.models[model_name]
        self.n_features = len(self.selected_features)

        means = [self.X[:, i].mean() for i in range(self.n_features)]
        for i in range(self.n_features):
            col = i % n_cols
            if col == 0:
                self.cur_row += 1
            ax = self.figure.add_subplot(self.grid[self.cur_row, col])
            ax.set_xlabel(self.selected_features[i])
            # subplots in a row share y labels
            if col == 0:
                ax.set_ylabel(self.target_name)
                ax.set_title(model_name)
            else:
                plt.setp(ax.get_yticklabels(), visible=False)
            cur_column = self.X[:, i]
            # actual data
            ax.scatter(cur_column, self.y)
            # prediction
            line_xs = np.linspace(cur_column.min(), cur_column.max())
            line_ys = []
            for x_ in line_xs:
                instance = [[0.] * self.n_features]
                instance[0][i] = x_
                for j in range(self.n_features):
                    if j != i:
                        instance[0][j] = means[j]
                line_ys.append(model.predict(self.scaler.transform(instance)))
            ax.plot(line_xs, line_ys, color='red')

    def use_model(self, model):
        model.fit(self.X_scaled, self.y)
        scores = model_selection.cross_val_score(model, self.X_scaled, self.y, cv=10, scoring=self.scorer)
        mean = scores.mean()
        return mean
