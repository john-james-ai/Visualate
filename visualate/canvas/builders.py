#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# =========================================================================== #
# Project : Visualate                                                         #
# Version : 0.1.0                                                             #
# File    : builders.py                                                       #
# Python  : 3.8.1                                                             #
# --------------------------------------------------------------------------- #
# Author  : John James                                                        #
# Company : DecisionScients                                                   #
# Email   : jjames@decisionscients.com                                        #
# URL     : https://github.com/decisionscients/visualate                      #
# --------------------------------------------------------------------------- #
# Created       : Wednesday, March 4th 2020, 7:20:53 pm                       #
# Last Modified : Wednesday, March 4th 2020, 7:20:53 pm                       #
# Modified By   : John James (jjames@decisionscients.com>)                    #
# --------------------------------------------------------------------------- #
# License : BSD                                                               #
# Copyright (c) 2020 DecisionScients                                          #
# =========================================================================== #
""" Classes which build Canvas objects.

The configurable options for a ploltly plot are copious and it could be a 
burdonsome  to include these configuration options in each plot class. This 
would lead to bloated interfaces that are difficult to read, let alone 
maintain.

The components module contains individual components which encapsulate logical
groupings of parameters. The components are further aggregated into a 
Canvas component class.

This module contains director and builder objects which will server as 
the interface for constructing canvas objects. This module is comprised of:

    * CanvasBuilder : Interface for concrete builder objects.
    * DefaultCanvasBuilder : Concrete builder for the default Canvas object.
    * CanvasDirector : Constructs Canvas objects via concrete builders 
"""
from abc import ABC, abstractmethod, abstractproperty

from .components import Canvas, CanvasColorAxisBarBoundary
from .components import CanvasColorAxisBarNumbers, CanvasColorAxisBarPosition
from .components import CanvasColorAxisBarStyle, CanvasColorAxisBarTickFont
from .components import CanvasColorAxisBarTickStyle, CanvasColorAxisBarTicks
from .components import CanvasColorAxisBarTitle, CanvasColorAxisDomain
from .components import CanvasColorAxisScales, CanvasColorBackground
from .components import CanvasColorScale, CanvasFont, CanvasLegend
from .components import CanvasMargins, CanvasSize, CanvasTitle
# --------------------------------------------------------------------------- #
#                              CANVAS BUILDER                                 #
# --------------------------------------------------------------------------- #
class CanvasBuilder(ABC):
    """ Interface for concrete Canvas builders."""

    @abstractproperty
    def canvas(self):
        pass

    @abstractmethod
    def build_canvas_title(self):
        pass

    @abstractmethod
    def build_canvas_legend(self):
        pass

    @abstractmethod
    def build_canvas_margins(self):
        pass

    @abstractmethod
    def build_canvas_size(self):
        pass    

    @abstractmethod
    def build_canvas_font(self):
        pass    

    @abstractmethod
    def build_canvas_background(self):
        pass    

    @abstractmethod
    def build_canvas_color_scale(self):
        pass    

    @abstractmethod
    def build_canvas_color_axis_domain(self):
        pass    

    @abstractmethod
    def build_canvas_color_axis_scales(self):
        pass    

    @abstractmethod
    def build_canvas_color_axis_bar_style(self):
        pass        

    @abstractmethod
    def build_canvas_color_axis_bar_position(self):
        pass        

    @abstractmethod
    def build_canvas_color_axis_bar_boundary(self):
        pass        

    @abstractmethod
    def build_canvas_color_axis_bar_ticks(self):
        pass        

    @abstractmethod
    def build_canvas_color_axis_bar_tick_style(self):
        pass        

    @abstractmethod
    def build_canvas_color_axis_bar_tick_font(self):
        pass        

    @abstractmethod
    def build_canvas_color_axis_bar_numbers(self):
        pass        

    @abstractmethod
    def build_canvas_color_axis_bar_title(self):
        pass        

# --------------------------------------------------------------------------- #
#                            DEFAULT CANVAS BUILDER                           #
# --------------------------------------------------------------------------- #    
class DefaultCanvasBuilder(CanvasBuilder):
    """ Constructs the default Canvas object."""

    self._canvas = None

    def __init__(self):
        self.reset()

    def reset(self):
        self._canvas = Canvas()

    @property
    def canvas(self):
        canvas = self._canvas
        self.reset()
        return canvas
    
    def build_canvas_title(self):
        component = CanvasTitle()
        self._canvas.add_component(component)
    
    def build_canvas_legend(self):
        component = CanvasLegend()
        self._canvas.add_component(component)
    
    def build_canvas_margins(self):
        component = CanvasMargins()
        self._canvas.add_component(component)

    def build_canvas_size(self):
        component = CanvasSize()
        self._canvas.add_component(component)    
    
    def build_canvas_font(self):
        component = CanvasFont()
        self._canvas.add_component(component)
    
    def build_canvas_background(self):
        component = CanvasColorBackground()
        self._canvas.add_component(component)    
    
    def build_canvas_color_scale(self):
        component = CanvasColorScale()
        self._canvas.add_component(component)
    
    def build_canvas_color_axis_domain(self):
        component = CanvasColorAxisDomain()
        self._canvas.add_component(component)
    
    def build_canvas_color_axis_scales(self):
        component = CanvasColorAxisScales()
        self._canvas.add_component(component)
    
    def build_canvas_color_axis_bar_style(self):
        component = CanvasColorAxisBarStyle()
        self._canvas.add_component(component)
    
    def build_canvas_color_axis_bar_position(self):
        component = CanvasColorAxisBarPosition()
        self._canvas.add_component(component)
    
    def build_canvas_color_axis_bar_boundary(self):
        component = CanvasColorAxisBarBoundary()
        self._canvas.add_component(component)
    
    def build_canvas_color_axis_bar_ticks(self):
        component = CanvasColorAxisBarTicks()
        self._canvas.add_component(component)
    
    def build_canvas_color_axis_bar_tick_style(self):
        component = CanvasColorAxisBarTickStyle()
        self._canvas.add_component(component)

    def build_canvas_color_axis_bar_tick_font(self):
        component = CanvasColorAxisBarTickFont()
        self._canvas.add_component(component)
    
    def build_canvas_color_axis_bar_numbers(self):
        component = CanvasColorAxisBarNumbers()
        self._canvas.add_component(component)
    
    def build_canvas_color_axis_bar_title(self):
        component = CanvasColorAxisBarTitle()
        self._canvas.add_component(component)
