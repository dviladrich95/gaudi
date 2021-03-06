#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############
# GaudiMM: Genetic Algorithms with Unrestricted
# Descriptors for Intuitive Molecular Modeling
# 
# https://github.com/insilichem/gaudi
#
# Copyright 2017 Jaime Rodriguez-Guerra, Jean-Didier Marechal
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############

from gaudi.base import Individual, Environment
from gaudi.parse import Settings
import logging
l = logging.getLogger()
l.addHandler(logging.StreamHandler())

cfg = Settings(path="/path/to/some/test.gaudi-input")

ind = Individual(cfg=cfg)
ind.express()
ind.unexpress()

gene = ind.genes['SomeGeneName']
gene.express()
gene.unexpress()

env = Environment(cfg)
env.evaluate(ind)

obj = env.objectives['SomeObjectiveName']
obj.evaluate(ind)