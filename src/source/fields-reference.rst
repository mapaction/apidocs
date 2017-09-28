.. title:: Field Reference

Field Reference
=========================================================================

type
-------------------------------------------------------------------------

  :Data type: String
  :Description: A classification of the type of output/product. This can be used to filter products which are syndicated to different sites.  Possible values are: `mapsheet` = Single page map - our most common product. These are the ones that could be automatically syndicated to RW) `atlas` = [aka collection] (manual syndication to RW) `powerpoint-map` = manual syndication to RW? `webmap` = In a dataset the resources can point to webmaps hosted elsewhere. These could be automatically syndicated to RW. `dataproduct`  (syndicate to HDX and not RW). Using "dataproduct" rather than "datset" could help avoid confusion with the CKAN meaning of "dataset". `legacy` = Products with where produced prior to ~June2017, whose metadata might not comply with the updated and more tightly defined schema.
  :Validation: (mapsheet|atlas|powerpoint-map|webmap|dataproduct|legacy)
  :Example:  ``mapsheet``



mapNumber
-------------------------------------------------------------------------

  :Data type: String
  :Description: The Map Number describes a single map product for an emergency. * A map product may have multiple versions, each of which will have the same Map Number. To get an identifier for a specific version of a map use the `result.name` field. * A Map Number is only unique within an emergency. To get an unique indentifier accross all emergencies use the [proposed] `parentID` field.
  :Validation: n/a
  :Example:  ``MA013``



title
-------------------------------------------------------------------------

  :Data type: String
  :Description: Title of the map or dataproduct. Single line.
  :Validation: n/a
  :Example:  ``"Paraguay:Inundaciones - Zonas Afectadas (a 17 de Abril 2016)",``



notes
-------------------------------------------------------------------------

  :Data type: Multiline String
  :Description: Summary or abstract describing the map. This is normally extracted from a text box on the map itself.
  :Validation: n/a
  :Example:  ``"El mapa muestra la extension de la inundaciÃ³n conocida a 17 de abril de 2016. Los datos de las zonas afectadas provienen del OCHA. AdemÃ¡s el mapa muestra las Ã¡reas de administraciÃ³n y los rÃ­os principales.",``



summary
-------------------------------------------------------------------------

  :Data type: Multiline String
  :Description: Summary or abstract describing the map. This is normally extracted from a text box on the map itself.
  :Validation: n/a
  :Example:  ``Map shows the current number of displaced people (as of 17 Mar 2017) as per the data collected by BNGRC from Fokontany and other sources.``



name
-------------------------------------------------------------------------

  :Data type: String
  :Description: The version specific productID.   This version of the product can be access via the Web UI as: https://maps.mapaction.org/dataset/<productID> and via the API as: https://maps.mapaction.org/api/3/action/package_show?id=<productID>
  :Validation: n/a
  :Example:  ``"00246-ma001-v1"``



datasource
-------------------------------------------------------------------------

  :Data type: Multiline String
  :Description: A description of the datasources used to produce this dataset.
  :Validation: n/a
  :Example:  ``Situational data: BNGRCBoundaries: BNGRC``



url
-------------------------------------------------------------------------

  :Data type: String
  :Description: URL of the web UI related to this dataset
  :Validation: n/a
  :Example:  ``null``



glideno
-------------------------------------------------------------------------

  :Data type: String (N)
  :Description: This field can be a comma separated list of glidenos. This is becuase we do not always find that our operational responses match one-to-one with glidenos.
  :Validation: n/a
  :Example:  ``TC-2017-000306-MDG``



principal-country-iso3
-------------------------------------------------------------------------

  :Data type: String
  :Description: The ISO3 country for for the principal disaster affected country
  :Validation: http://vocabulary.unocha.org/json/beta-v1/countries.json, data/?/x-alpha-3
  :Example:  ``GBR``



all-countries-iso3
-------------------------------------------------------------------------

  :Data type: String
  :Description: A comma seperated list of ISO3 country codes for all affected countries
  :Validation: http://vocabulary.unocha.org/json/beta-v1/countries.json, data/?/x-alpha-3
  :Example:  ``GBR, IRL``



countries
-------------------------------------------------------------------------

  :Data type: String (N)
  :Description: A comma seperated list of country names (in English) to which map or dataproduct applies. At present the control list of this field is here: https://github.com/mapaction/mapaction-toolbox/blob/master/arcgis10_mapping_tools/MapActionToolbars/frmConfigMain.Designer.cs (starting line 285).
  :Validation: n/a
  :Example:  ``MADAGASCAR``



language-iso2
-------------------------------------------------------------------------

  :Data type: String
  :Description: ISO 639-1 two letter code for the lanuage used in the product (see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
  :Validation: n/a
  :Example:  ``EN``



language
-------------------------------------------------------------------------

  :Data type: String
  :Description: Natural language(s) used within the map or dataproduct 
  :Validation: n/a
  :Example:  ``English``



createdate
-------------------------------------------------------------------------

  :Data type: String
  :Description: This is the timestamp that the map/dataset was produced. This may have been in an offline environment.  This is the timestamp that will be shown on the map itself.
  :Validation: n/a
  :Example:  ``18/03/2017 11:18``



createtime
-------------------------------------------------------------------------

  :Data type: String
  :Description: This is the date and time that the map was produced. Typically it is the date and time that appear in the marginalia of the map itself.
  :Validation: n/a
  :Example:  ``11:18``



reliefweb_theme_id_hint
-------------------------------------------------------------------------

  :Data type: integer
  :Description: The ID of the ReliefWeb theme, which the MapAction field team presume is appropriate for the map. This is provided exclusively for the convenience of the ReliefWeb editorial team. Note that the ReliefWeb editorial team, may choose to override this value, hence it may not reflect the actual value used by ReliefWeb, if and when they republish this map.
  :Validation: https://api.reliefweb.int/v1/references/themes?appname=vocabulary
  :Example:  ``4591``



vunerablepeople
-------------------------------------------------------------------------

  :Data type: String
  :Description: Contains the ID of terms used by ReliefWeb to label content according to vulnerable groups such as Aged Persons, Children, IDPs, Persons with Disabilities, Refugees, and Women. See here for futher details https://reliefweb.int/taxonomy-descriptions#groups
  :Validation: https://api.reliefweb.int/v1/references/vulnerable-groups?appname=vocabulary, /data/?/id
  :Example:  ``6874``



product_themes
-------------------------------------------------------------------------

  :Data type: Array
  :Description: A list of zero or more humanitarian themes to which the product relates.
  :Validation: https://maps.mapaction.org/api/3/action/vocabulary_list
  :Example:  ``[ ]``



groups
-------------------------------------------------------------------------

  :Data type: Array
  :Description: Disasters related to this dataset Note that `groups` and `events` are synonimous. Typically a dataset will only be a member of a single group, but this is by convention and not enforced.
  :Validation: http://maps.mapaction.org/api/3/action/group_list?type=event&all_fields=true
  :Example: 

  ::

        "groups": [
          {
            "display_name": "Sierra Leone Landslides, August 2017",
            "description": "A  seven person UNDAC team deployed on 18 August including three members of MapAction. Their role has been to provide support to the damage assessments, assistance in identifying the humanitarian caseload, and support to the 4W mapping process, mapping who is doing what, where.",
            "image_display_url": "https://maps.mapaction.org/uploads/group/2017-08-17-110806.150269sierraleone.png",
            "title": "Sierra Leone Landslides, August 2017",
            "id": "9013d553-a7e4-4987-8ab4-c126310022d2",
            "name": "sierra-leone-landslides"
          }
        ],


tags
-------------------------------------------------------------------------

  :Data type: Array
  :Description: Not currently used
  :Validation: n/a
  :Example:  ``[]``



xmax
-------------------------------------------------------------------------

  :Data type: decimal
  :Description: Eastern edge of bounding box for the dataset, Given in Decimal Degrees, WGS1984. Used for GeoRSS <georss:box> element
  :Validation: xmin â‰¤ xmax â‰¤ 180
  :Example:  ``51.73``



xmin
-------------------------------------------------------------------------

  :Data type: decimal
  :Description: Western edge of bounding box for the dataset, Given in Decimal Degrees, WGS1984. Used for GeoRSS <georss:box> element
  :Validation: -180 â‰¤ xmin â‰¤ xmax
  :Example:  ``39.27``



ymax
-------------------------------------------------------------------------

  :Data type: decimal
  :Description: Northern edge of bounding box for the dataset, Given in Decimal Degrees, WGS1984. Used for GeoRSS <georss:box> element
  :Validation: ymin â‰¤ ymax â‰¤ 90
  :Example:  ``-11.09``



ymin
-------------------------------------------------------------------------

  :Data type: decimal
  :Description: Southern edge of bounding box for the dataset, Given in Decimal Degrees, WGS1984. Used for GeoRSS <georss:box> element
  :Validation: -90 â‰¤ ymin â‰¤ ymax
  :Example:  ``-26.15``



datum
-------------------------------------------------------------------------

  :Data type: String
  :Description: The datum used in the map
  :Validation: n/a
  :Example:  ``WGS 1984``



scale
-------------------------------------------------------------------------

  :Data type: String
  :Description: The nominal map scale, when printed at the size specified in "papersize"
  :Validation: n/a
  :Example:  ``1: 5,000,000``



access
-------------------------------------------------------------------------

  :Data type: String
  :Description: Describes the indended audience for the product. Possible values: * "Public" * "MapAction" * "Selected partners"  Note that this is not releated to whether or not CKAN makes the dataset available publicly/anomymously or the legal licence for the data. 
  :Validation: (Public|MapAction|Selected partners)
  :Example:  ``Public``



license_id
-------------------------------------------------------------------------

  :Data type: String
  :Description: The ID of license group under which the map or dataproduct is published. License definitions and additional information can be found at http://opendefinition.org/
  :Validation: http://licenses.opendefinition.org/licenses/groups/ckan.json, /?/id
  :Example:  ``"notspecified",``



license_title
-------------------------------------------------------------------------

  :Data type: String
  :Description: The title of license group under which the map or dataproduct is published. License definitions and additional information can be found at http://opendefinition.org/
  :Validation: http://licenses.opendefinition.org/licenses/groups/ckan.json, /?/title
  :Example:  ``"License not specified"``



syndicate
-------------------------------------------------------------------------

  :Data type: Boolean
  :Description: Indicates whether or not a dataset should be syndicated to HDX
  :Validation: boolean
  :Example:  ``TRUE``



data_update_frequency
-------------------------------------------------------------------------

  :Data type: String
  :Description: A verbal description of the expected frequency by which the underlying data is updated.
  :Validation: n/a
  :Example:  ``"Every two weeks"``



methodology
-------------------------------------------------------------------------

  :Data type: String
  :Description: ??
  :Validation: n/a
  :Example:  ``UNDAC field survey``



methodology_other
-------------------------------------------------------------------------

  :Data type: String
  :Description: ??
  :Validation: n/a
  :Example: 


number_of_pages
-------------------------------------------------------------------------

  :Data type: Integer
  :Description: For multiple page products (eg atlases and powerpoint maps) this indicates the number of pages
  :Validation: Integer
  :Example:  ``17``



papersize
-------------------------------------------------------------------------

  :Data type: String
  :Description: The papersize for which the map was optimised.
  :Validation: n/a
  :Example:  ``A3``



jpgfilename
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename of the first jpeg file (is one exists). Note that `resources.name` where resources.format=="JPEG" is more reliable.
  :Validation: n/a
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct-300dpi.jpeg``



jpgfilesize
-------------------------------------------------------------------------

  :Data type: String
  :Description: Size in bytes, of the JPEG file (if it exists). The acuracy of this value is not garenteed. It is known to be incorrect in the case of atlases.
  :Validation: int
  :Example:  ``953554``



jpgresolutiondpi
-------------------------------------------------------------------------

  :Data type: integer
  :Description: The DPI used to produce the jpeg file (if one exists).
  :Validation: int
  :Example:  ``300``



pdffilename
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename of the main PDF file associated with the dataset. 
  :Validation: n/a
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct-300dpi.pdf``



pdffilesize
-------------------------------------------------------------------------

  :Data type: integer
  :Description: Size in bytes, of the PDF file (if it exists). The acuracy of this value is not garenteed. It is known to be incorrect in the case of atlases.
  :Validation: int
  :Example:  ``1193663``



pdfresolutiondpi
-------------------------------------------------------------------------

  :Data type: integer
  :Description: The DPI used to produce the pdf file (if one exists).
  :Validation: int
  :Example:  ``300``



kmzfilename
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename of the first KML file (is one exists). Note that `resources.name` where resources.format=="KML" is more reliable.
  :Validation: n/a
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct.kmz``



kmlresolutiondpi
-------------------------------------------------------------------------

  :Data type: integer
  :Description: The DPI used to produce any raster elements with the KMZ file (if one exists). Note that normally KMZ files are produce rather than KMLs desipte the fieldname
  :Validation: int
  :Example:  ``50``



mxdfilename
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename base (ie minus it's extension) of the map's source .mxd file (presuming it was produced in ArcGIS)
  :Validation: n/a
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct``



ref
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename base (ie minus it's extension) of the map's source .mxd file (presuming it was produced in ArcGIS)
  :Validation: n/a
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct``



qclevel
-------------------------------------------------------------------------

  :Data type: String
  :Description: Freetext description of the Quality Control process the map as been subjected to.
  :Validation: n/a
  :Example:  ``Local``



sourceorg
-------------------------------------------------------------------------

  :Data type: String
  :Description: Name of the publishing organisation. This will always return the value "MapAction"
  :Validation: MapAction'
  :Example:  ``MapAction``



organization
-------------------------------------------------------------------------

  :Data type: Array
  :Description: An Organization object, describing MapAction. Note that unlike most other CKAN instances, there is only ever one organisation object on MapAction's Map and Data Repository.
  :Validation: https://maps.mapaction.org/api/3/action/organization_list?all_fields=true
  :Example: 

  ::

      "organization": {
          "description": "MapAction is a humanitarian mapping charity that works through skilled volunteers. Our specialist teams help to save lives and minimise suffering by making the response to humanitarian emergencies as targeted, efficient and effective as possible.",
          "created": "2016-06-21T14:57:26.038392",
          "title": "MapAction",
          "name": "mapaction",
          "is_organization": true,
          "state": "active",
          "image_url": "https://maps.mapaction.org/logo.svg",
          "revision_id": "7ff25d00-f5ca-4e0d-b88c-3d004cbd1e8f",
          "type": "organization",
          "id": "0a9ee200-c088-402a-b02d-b3cd053a9781",
          "approval_status": "approved"
        },


version
-------------------------------------------------------------------------

  :Data type: Integer
  :Description: The version number of the specific dataset
  :Validation: Integer
  :Example:  ``4``



parentID
-------------------------------------------------------------------------

  :Data type: String
  :Description: The parentID is common to all versions of a dataset. If either the web UI or API is querried with the parentID the lastest version is returned. The parentID forms the base of the identifier for each specific version, (returned in the field `result.name`).  The parentID is constructed by the syntax: <operationID>-<mapNumber> eg `vanuatu-2017-ma003`  The identifier of an specific version of an individual map is given by the syntax: <operationID>-<mapNumber>-v<versionNumber> eg `vanuatu-2017-ma003-v1` An array of all the identifiers for all versions of an individual map is provided in the  "_versions" field.  
  :Validation: n/a
  :Example:  ``vanuatu-2017-ma003-v1``



_versions
-------------------------------------------------------------------------

  :Data type: Array
  :Description: Array with all the version names of this resource. 
  :Validation: n/a
  :Example: 

  ::

    _versions: [
    [
    "00246-ma001-v3",
    "00246-ma001"
    ],
    [
    "00246-ma001-v2",
    "00246-ma001-v2"
    ],
    [
    "00246-ma001-v1",
    "00246-ma001-v1"
    ]
    ],
    
