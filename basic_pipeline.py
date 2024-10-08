from zenml import step
from typing_extensions import Annotated
import pandas as pd
from typing import Tuple
import numpy as np 
from sklearn.base import ClassifierMixin
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

@step
def importer() -> Tuple[
    Annotated[np.ndarray, "X_train"],
    Annotated[np.ndarray, "X_test"],
    Annotated[np.ndarray, "y_train"],
    Annotated[np.ndarray, "y_test"],
]: # Annotated is used to ensure the data type of the results of the return statement of the function
    "Load the digits dataset as numpy array"
    digits = load_digits()
    data = digits.images.reshape(len(digits.images),-1)
    X_train,X_test,y_train,y_test= train_test_split(
        data,digits.target,test_size=0.2,shuffle=False
    )
    
    return X_train,X_test,y_train,y_test
    
@step
def svc_trainer(
    X_train: np.ndarray,
    y_train: np.ndarray,
) -> ClassifierMixin:
    """Train an sklearn SVC classifier"""
    model=SVC(gamma=0.001)
    model.fit(X_train,y_train)
    
    return model

@step
def evaluator(
    X_test: np.ndarray,
    y_test: np.ndarray,
    model: ClassifierMixin,
) -> float:
    
    """Calculate test set accuracy"""
    test_acc=model.score(X_test,y_test)
    print(f"Test accuracy : {test_acc}")
    
    return test_acc
    
from zenml import pipeline

@pipeline
def digits_pipeline():
    """Links all steps together in a pipeline"""
    X_train,X_test,y_train,y_test= importer()
    model=svc_trainer(X_train=X_train,y_train=y_train)
    evaluator(X_test=X_test,y_test=y_test,model=model)
    
    
digits_pipeline()