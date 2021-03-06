.. GaudiMM: Genetic Algorithms with Unrestricted
   Descriptors for Intuitive Molecular Modeling
   
   https://github.com/insilichem/gaudi
  
   Copyright 2017 Jaime Rodriguez-Guerra, Jean-Didier Marechal
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
   
        http://www.apache.org/licenses/LICENSE-2.0
   
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

.. _input:

===========
Input files
===========

GaudiMM uses YAML-formatted files for both input and output files. YAML is a human-readable serialization format, already implemented in a broad range of languages. Input files must contain these five sections:

- **output**. Project options. Configure it to your liking
- **ga**. Genetic algorithm configuration. Normally, you don't have to touch this, except maybe the number of generations and population size.
- **similarity**. The similarity function to compare potentially redundant solutions.
- **genes**. List of descriptors used to define an individual
- **objectives**. The list of functions that will evaluate your individuals.
  
You can check some sample input files in the ``examples`` directory.

How to create GaudiMM input files
=================================

If you don't mind installing `GAUDInspect <https://github.com/insilichem/gaudinspect>`_, it provides a full GUI to create GAUDI input files, step by step. Add genes and objectives, configure the paths, number of generations and population size, and run it. Simple and easy.

.. note::

  The development of GAUDInspect is currently *stalled*.  

However, you can also edit them manually, since they are just plain text files. Create a copy of one of the examples and edit them to your convenience. While you can check the API documentation of :ref:`api.gaudi.genes` and :ref:`api.gaudi.objectives` to find a list of available components, we really recommend checking the beginners tutorial:

- :ref:`tutorial`.
