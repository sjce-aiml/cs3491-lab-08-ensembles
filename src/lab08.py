"""Lab 8 starter code: ensembling techniques."""
import numpy as np
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier, StackingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

def majority_vote(predictions):
    """predictions: array (n_models, n_samples) of int labels. Ties -> smallest label."""
    raise NotImplementedError('TODO: implement this')

def build_ensembles(X, y, seed=0):
    """Return dict with fitted 'bagging', 'boosting', 'stacking', 'voting' models."""
    raise NotImplementedError('TODO: implement this')
