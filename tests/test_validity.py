#!/usr/bin/env python3
# =========================================================================== #
#                                  BASE                                       #
# =========================================================================== #
# =========================================================================== #
# Project: Visualate                                                          #
# Version: 0.1.0                                                              #
# File: \test_validity.py                                                     #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Thursday November 28th 2019, 6:34:05 am                        #
# Last Modified: Thursday November 28th 2019, 6:34:18 am                      #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2019 Decision Scients                                         #
# =========================================================================== #
"""Test validity visualizations"""
from pytest import mark
import numpy as np

from ml_studio.supervised_learning.regression import LinearRegression

from visualate.regression.validity import Residuals
# --------------------------------------------------------------------------- #
#                            RESIDUAL PLOT                                    #
# --------------------------------------------------------------------------- #
class ResidualPlotTests:

    @mark.validity
    def test_regression_plot(self, get_regression_data):
        X_train, X_test, y_train, y_test = get_regression_data
        model = LinearRegression(epochs=1000, metric='r2')                       
        v = Residuals(model=model)
        v.fit(X_train, y_train)
        v.score(X_test, y_test)
        v.show()