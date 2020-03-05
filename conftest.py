#!/usr/bin/env python3
# =========================================================================== #
#                              CONFTEST                                       #
# =========================================================================== #
# =========================================================================== #
# Project: Visualate                                                          #
# Version: 0.1.0                                                              #
# File: \conftest.py                                                          #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Thursday November 28th 2019, 6:40:29 am                        #
# Last Modified: Thursday November 28th 2019, 6:42:02 am                      #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2019 Decision Scients                                         #
# =========================================================================== #
"""Pytest fixtures"""
from pytest import fixture
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 

@fixture(scope="session")
def get_regression_data():
    X, y = datasets.load_boston(return_X_y=True)
    scaler = StandardScaler()    
    X = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                            random_state=50)
    return X_train, X_test, y_train, y_test