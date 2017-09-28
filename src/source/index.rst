.. maapi documentation master file, created by
   sphinx-quickstart on Tue Aug 29 18:57:06 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. title:: API docs for MapAction's Map and Data
   
MapAction API Documentation
=============================================

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:

   self
   product-types
   fields-by-product-types
   fields-reference
   differences-to-ckan-api

   
Introduction
------------
MapAction Maps and Data API makes `MapAction's maps and data <https://maps.mapaction.org/>`_ programically accessible for third partys. 

The Map and Data Repository is based on the data sharing platform CKAN, hence the MapAction API is inherited from the CKAN API with a number of adaptations. One of the main adaptations of interest to third party's is that we have made extensive use of the fact that CKAN allows for customisation of the schema used to describe the various protucts it serves. This is achieved using `CKAN's schemimg extension <https://github.com/ckan/ckanext-scheming>`_.

The `CKAN API <http://docs.ckan.org/en/ckan-2.5.6/api/index.html>`_ is already well doucmented and we are not attempting to reproduce that here. This document focuses on the specific adaptations for MapAction.  


Versions
---------
This document is for the current `MapAction schema <https://github.com/mapaction/ckanext-mapactionschemas>`_ version |version| (release |release|), which is hosted on 
and `CKAN v2.5.5 <https://github.com/aptivate/ckan/releases/tag/ckan-2.5.5-mapaction>`_.

