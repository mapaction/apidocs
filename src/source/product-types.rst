.. title:: Product Types

About Product Types
-------------------
MapAciton offer an number of different product types, which are summarised below. Each Product Type has a specific set of metadata fields, though there are many fields common to all product types.

.. tabularcolumns:: |p{1.5cm}|p{1.5cm}|L|

+------------------+--------------------------------------------------------------------+
| Product Type     |  Description                                                       |
+==================+====================================================================+
| `mapsheet`       | A single page map. This is our most commonly produced product.     |
|                  | A  mapsheet always consists of exactly one single page PDF,        |
|                  | one JPEG and a thumbnail. Typically these will also be published   |
|                  | on `ReliefWeb <https://reliefweb.int>`_ and                        |
|                  | `HumanitarianResponse.info <https://humanitarianresponse.info>`_.  |
+------------------+--------------------------------------------------------------------+
| `atlas`          | A multipage map. These may be either a single multiple PDF, or     |
|                  | multiple single page PDF, and typically dispaly a common theme for |
|                  | different geographical regions. There may be a thumbnail, but      |
|                  | there is not normally a JPEG associated with an atlas.             |
+------------------+--------------------------------------------------------------------+
| `powerpoint-map` | A map in a powerpoint presentation, allowing users to easily add   |
|                  | their own symbols and labels, without any GIS or map making        |
|                  | knowledge.                                                         |
+------------------+--------------------------------------------------------------------+
| `webmap`         | An interactive map. The API result will include the URL(s) within  |
|                  | the resources. In most cases this URL point to a seperate hosting  |
|                  | location.                                                          |
+------------------+--------------------------------------------------------------------+
| `dataproduct`    | A data product which would be of interest to an Information        |
|                  | Manager, such as a spreadsheet, shapefile, GeoJSON etc. Typically  |
|                  | these will also be published on `Humanitarian Data Exchange (HDX)  |
|                  | <https://data.humdata.org/organization/mapaction>`_. Note we use   |
|                  | the term "dataproduct" rather than "datset" could help avoid       |
|                  | confusion with the specifc CKAN meaning of the word "dataset".     |
+------------------+--------------------------------------------------------------------+
| `legacy`         | All products which are produced prior to ~ August 2017, when the   |
|                  | product-type field was introduced. We have not attempted to        |
|                  | retrofit the updated schema definition to existing products.       |
|                  | In some cases the relevant metadata fields may not be present to   |
|                  | fit the new schema.                                                |
+------------------+--------------------------------------------------------------------+
