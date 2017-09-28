MapAction API Documentation
===========================


Introduction
------------
MapAction Maps and Data are accessible for third partys through our API. 

The Map and Data Repository is based on the data sharing platform CKAN, hence the MapAction API is inherited from the CKAN API with a number of adaptations. One of the main adaptations of interest to third party's is that we have made extensive use of the fact that CKAN allows for customisation of the schema used to describe the various protucts it serves.

This is achieved using https://github.com/ckan/ckanext-scheming.

The CKAN API is already well doucmented and we are not attempting to reproduce that here. This document focuses on the specific adaptations for MapAction.  

Contents
--------
* Product Types
* Fields available by product type
* Field details
* Other differences to the CKAN API

Version
-------
This document is based on MapAction schema version XXXXX (link to specific release on https://github.com/mapaction/ckanext-mapactionschemas)
and CKAN v2.5.5 https://github.com/aptivate/ckan/releases/tag/ckan-2.5.5-mapaction

About Product Types
-------------------
MapAciton offer an number of different product types, which are summarised below. Each Product Type has a specific set of metadata fields, though there are many fields common to all product types.


| Product Type     |  Description                                                                                     |
|------------------|--------------------------------------------------------------------------------------------------|
| `mapsheet`       |  A single page map. This is our most commonly produced product. A  mapsheet always consists of exactly one single page PDF,  one JPEG and a thumbnail. Typically these will also be published on [ReliefWeb](http://reliefweb.int/) and [HumanitarianResponse.info](HumanitarianResponse.info).                                                               |
| `atlas`          |  A multipage map. These may be either a single multiple PDF, or multiple single page PDF, and typically dispaly a common theme for different geographical regions. There may be a thumbnail, but there is not normally a JPEG associated with an atlas.
| `powerpoint-map` |  A map in a powerpoint presentation, allowing users to easily add their own symbols and labels, without any GIS or map making knowledge.                                                                                                 |
| `webmap`         |  An interactive map. The API result will include the URL(s) within the resources. In most cases this URL point to a seperate hosting location.                                                                                            |
| `dataproduct`    |  A data product which would be of interest to an Information Manager, such as a spreadsheet, shapefile, GeoJSON etc. Typically these will also be published on [Humanitarian Data Exchange (HDX)](https://data.humdata.org/organization/mapaction). Note we use the term dataproduct" rather than "datset" could help avoid confusion with the specifc CKAN meaning of the word "dataset". |
| `legacy`         |  All products which are produced prior to ~ August 2017, when the product-type field was introduced. We have not attempted to retrofit the updated schema definition to existing products. In some cases the relevant metadata fields may not be present to fit the new schema.                                                                                                |



Fields available by product type
--------------------------------

This table:
<iframe src="https://docs.google.com/spreadsheets/d/1RUlQd3zSaeWkS-C33bBjcIpft9Y6arNeg_B5Bfk6GMg/pubhtml?gid=454102953&amp;single=true&amp;widget=true&amp;headers=false"></iframe>


Field details
-------------

This table:
<iframe src="https://docs.google.com/spreadsheets/d/1RUlQd3zSaeWkS-C33bBjcIpft9Y6arNeg_B5Bfk6GMg/pubhtml?gid=454102953&amp;single=true&amp;widget=true&amp;headers=false"></iframe>


Other differences to the CKAN API
---------------------------------
### Use of CKAN groups

We use CKAN's native groups feature to represent individual events (emergencies/crisis etc). We attempted to rename `groups` to `events` so the that name appears more consistantly in URLs etc:
`http://maps.mapaction.org/event/madagascar-2017` instead of `http://maps.mapaction.org/group/madagascar-2017`

This has had a slightly odd side effect on our API. To get a listing of all events you need to add the argument `type=event` to the `group_list` action. eg:
`http://maps.mapaction.org/api/3/action/group_list?type=event`
Or for more detail add the argument `all_fields=true`
`http://maps.mapaction.org/api/3/action/group_list?type=event&all_fields=true`

 



