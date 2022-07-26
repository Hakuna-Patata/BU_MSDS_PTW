import pandas as _pd
from pandas import DataFrame as _DF
from functools import reduce as _reduce
from sklearn.preprocessing import FunctionTransformer as _FunctionTransformer
from sklearn.base import TransformerMixin as _TransformerMixin, BaseEstimator as _BaseEstimator
from sklearn.feature_extraction import DictVectorizer as _DictVectorizer


class DFFunctionTransformer(_TransformerMixin):
    def __init__(self, *args, **kwargs):
        self.FT = _FunctionTransformer(*args, **kwargs)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_xfrm = self.FT.transform(X) 
        X_xfrm = _DF(X_xfrm, index=X.index, columns=X.columns)
        return X_xfrm


class DFFeatureUnion(_TransformerMixin, _BaseEstimator):
    def __init__(self, transformer_list):
        self.transformer_list = transformer_list

    def fit(self, X, y=None):
        for (name, transformer) in self.transformer_list:
            transformer.fit(X, y)
        return self

    def transform(self, X):
        X_xfrm = [transformer.transform(X) for _, transformer in self.transformer_list]
        X_union = _reduce(lambda X1, X2: _pd.merge(X1, X2, left_index=True, right_index=True), X_xfrm)
        return X_union


class DFColumnExtractor(_TransformerMixin, _BaseEstimator):
    def __init__(self, cols):
        self.cols = cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        Xcols = X[self.cols]
        return Xcols


class DFColumnDropper(_TransformerMixin, _BaseEstimator):
    def __init__(self, cols):
        self.cols = cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(self.cols, axis=1)


class DFDummyTransformer(_TransformerMixin, _BaseEstimator):
    def __init__(self):
        self.dv = None

    def fit(self, X, y=None):
        X_dict = X.to_dict('records')
        self.dv = _DictVectorizer(sparse=False)
        self.dv.fit(X_dict)
        return self

    def transform(self, X):
        X_dict = X.to_dict('records')
        X_xfrm = self.dv.transform(X_dict)
        xfrm_cols = self.dv.get_feature_names_out()
        X_dum = _DF(X_xfrm, index=X.index, columns=xfrm_cols)
        nan_cols = [c for c in xfrm_cols if '=' not in c]
        X_dum = X_dum.drop(nan_cols, axis=1)
        return X_dum


class DFStringTransformer(_TransformerMixin, _BaseEstimator):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_str = X.applymap(str)
        return X_str


class DFImputer(_TransformerMixin, _BaseEstimator):
    def __init__(self, imputer):
        self.imputer = imputer
        self.stats_ = None

    def fit(self, X, y=None):
        self.imputer.fit(X)
        self.stats_ = _pd.Series(self.imputer.statistics_, index=X.columns)
        return self

    def transform(self, X):
        X_imputed_array = self.imputer.transform(X)
        X_imputed_df = _DF(X_imputed_array, index=X.index, columns=X.columns)
        return X_imputed_df


class DFScaler(_TransformerMixin, _BaseEstimator):
    def __init__(self, scaler):
        self.scaler = scaler

    def fit(self, X, y=None):
        self.scaler.fit(X)
        return self 

    def transform(self, X):
        X_scaled_data = self.scaler.transform(X)
        X_scaled_df = _DF(X_scaled_data, index=X.index, columns=X.columns)
        return X_scaled_df


class DFDropNaN():
    def fit(self, X, y=None):
        return self 

    def transform(self, X, *args, **kwargs):
        return X.dropna(*args, **kwargs)
        