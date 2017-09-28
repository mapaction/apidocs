.. title:: Field Reference

Field Reference
=========================================================================

Field-name
-------------------------------------------------------------------------

  :Data type: Data-type
  :Description: Description
  :Validation: Controlled-by
  :Example:  ``Example``



product-type
-------------------------------------------------------------------------

  :Data type: String
  :Description: A classification of the type of output/product. This can be used to filter products which are syndicated to different sites.
  :Validation: One of the following values: `mapsheet` = Single page map - our most common product. These are the ones that could be automatically syndicated to RW) `atlas` = [aka collection] (manual syndication to RW) `powerpoint-map` = manual syndication to RW? `webmap` = In a dataset the resources can point to webmaps hosted elsewhere. These could be automatically syndicated to RW. `dataproduct`  (syndicate to HDX and not RW). Using "dataproduct" rather than "datset" could help avoid confusion with the CKAN meaning of "dataset". `legacy` = Products with where produced prior to ~June2017, whose metadata might not comply with the updated and more tightly defined schema.
  :Example: 


country-iso3
-------------------------------------------------------------------------

  :Data type: String
  :Description: A comma seperated list of ISO3 country codes for all affected countries
  :Validation: Lookup for ISO 3166-1 alpha-3
  :Example: 


help
-------------------------------------------------------------------------

  :Data type: URL
  :Description: URL with help about the endpoint called
  :Validation: n/a
  :Example:  ``"https://maps.mapaction.org/api/3/action/help_show?name=package_show",``



lanaguage-iso2
-------------------------------------------------------------------------

  :Data type: String
  :Description: ISO 639-1 two letter code for the lanuage used in the product (see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
  :Validation: Lookup for ISO 639-1
  :Example: 


parentID
-------------------------------------------------------------------------

  :Data type: String
  :Description: The parentID is common to all versions of a dataset. If either the web UI or API is querried with the parentID the lastest version is returned. The parentID forms the base of the identifier for each specific version, (returned in the field `result.name`).  The parentID is constructed by the syntax: <operationID>-<mapNumber> eg `vanuatu-2017-ma003`  The identifier of an specific version of an individual map is given by the syntax: <operationID>-<mapNumber>-v<versionNumber> eg `vanuatu-2017-ma003-v1` An array of all the identifiers for all versions of an individual map is provided in the  "_versions" field.  
  :Validation: None, though we could potentially enforce that:  <parentID>=<operationID>-<mapNumber>
  :Example: 


prinicpal-country-iso3
-------------------------------------------------------------------------

  :Data type: String
  :Description: The ISO3 country for for the principal disaster affected country
  :Validation: Lookup for ISO 3166-1 alpha-3
  :Example: 


result._versions
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
    


result.author
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Internal CKAN field - not used
  :Validation: n/a
  :Example:  ``null``



result.author_email
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Internal CKAN field - not used
  :Validation: n/a
  :Example:  ``null``



result.creator_user_id
-------------------------------------------------------------------------

  :Data type: GUID
  :Description: Internal CKAN field - not used exturnally
  :Validation: n/a
  :Example:  ``959f68c9-0fe4-43fc-aece-fb401654d847``



result.extras
-------------------------------------------------------------------------

  :Data type: Array (key, value)
  :Description: Additional metadata
  :Validation: n/a
  :Example: 


result.extras.access
-------------------------------------------------------------------------

  :Data type: String
  :Description: Describes the indended audience for the product.  Note that this is not releated to whether or not CKAN makes the dataset available publicly/anomymously. 
  :Validation: Possible values: * "Public" * "MapAction" * "Selected partners" See line 1161 here: https://github.com/mapaction/mapaction-toolbox/blob/master/arcgis10_mapping_tools/MapActionToolbars/frmExportMain.Designer.cs
  :Example:  ``Public``



result.extras.countries
-------------------------------------------------------------------------

  :Data type: String (N)
  :Description: A comma seperated list of country names (in English) to which map or dataproduct applies. At present the control list of this field is here: https://github.com/mapaction/mapaction-toolbox/blob/master/arcgis10_mapping_tools/MapActionToolbars/frmConfigMain.Designer.cs (starting line 285).
  :Validation: n/a
  :Example:  ``MADAGASCAR``



result.extras.createdate
-------------------------------------------------------------------------

  :Data type: String
  :Description: This is the timestamp that the map/dataset was produced. This may have been in an offline environment.  This is the timestamp that will be shown on the map itself.
  :Validation: n/a
  :Example:  ``18/03/2017 11:18``



result.extras.createtime
-------------------------------------------------------------------------

  :Data type: String
  :Description: This is the date and time that the map was produced. Typically it is the date and time that appear in the marginalia of the map itself.
  :Validation: 
  :Example:  ``11:18``



result.extras.datasource
-------------------------------------------------------------------------

  :Data type: String
  :Description: A description of the datasources used to produce this dataset.
  :Validation: n/a
  :Example:  ``Situational data: BNGRCBoundaries: BNGRC``



result.extras.datum
-------------------------------------------------------------------------

  :Data type: String
  :Description: The datum used in the map
  :Validation: 
  :Example:  ``WGS 1984``



result.extras.glideno
-------------------------------------------------------------------------

  :Data type: String (N)
  :Description: This field can be a comma separated list of glidenos. This is becuase we do not always find that our operational responses match one-to-one with glidenos.
  :Validation: n/a
  :Example:  ``TC-2017-000306-MDG``



result.extras.jpgfilename
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename of the first jpeg file (is one exists). Note that `resources.name` where resources.format=="JPEG" is more reliable.
  :Validation: 
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct-300dpi.jpeg``



result.extras.jpgfilesize
-------------------------------------------------------------------------

  :Data type: String
  :Description: Size in bytes, of the JPEG file (if it exists). The acuracy of this value is not garenteed. It is known to be incorrect in the case of atlases.
  :Validation: 
  :Example:  ``953554``



result.extras.jpgresolutiondpi
-------------------------------------------------------------------------

  :Data type: integer
  :Description: The DPI used to produce the jpeg file (if one exists).
  :Validation: 
  :Example:  ``300``



result.extras.kmlresolutiondpi
-------------------------------------------------------------------------

  :Data type: integer
  :Description: The DPI used to produce any raster elements with the KMZ file (if one exists). Note that normally KMZ files are produce rather than KMLs desipte the fieldname
  :Validation: 
  :Example:  ``50``



result.extras.kmzfilename
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename of the first KML file (is one exists). Note that `resources.name` where resources.format=="KML" is more reliable.
  :Validation: 
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct.kmz``



result.extras.language
-------------------------------------------------------------------------

  :Data type: String
  :Description: Natural language(s) used within the map or dataproduct 
  :Validation: Yes
  :Example:  ``English``



result.extras.mapNumber
-------------------------------------------------------------------------

  :Data type: String
  :Description: The Map Number describes a single map product for an emergency. * A map product may have multiple versions, each of which will have the same Map Number. To get an identifier for a specific version of a map use the `result.name` field. * A Map Number is only unique within an emergency. To get an unique indentifier accross all emergencies use the [proposed] `parentID` field.
  :Validation: n/a
  :Example:  ``MA013``



result.extras.mxdfilename
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename base (ie minus it's extension) of the map's source .mxd file (presuming it was produced in ArcGIS)
  :Validation: 
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct``



result.extras.papersize
-------------------------------------------------------------------------

  :Data type: String
  :Description: The papersize for which the map was optimised.
  :Validation: 
  :Example:  ``A3``



result.extras.pdffilename
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename of the main PDF file associated with the dataset. 
  :Validation: n/a
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct-300dpi.pdf``



result.extras.pdffilesize
-------------------------------------------------------------------------

  :Data type: integer
  :Description: Size in bytes, of the PDF file (if it exists). The acuracy of this value is not garenteed. It is known to be incorrect in the case of atlases.
  :Validation: 
  :Example:  ``1193663``



result.extras.pdfresolutiondpi
-------------------------------------------------------------------------

  :Data type: integer
  :Description: The DPI used to produce the pdf file (if one exists).
  :Validation: 
  :Example:  ``300``



result.extras.qclevel
-------------------------------------------------------------------------

  :Data type: String
  :Description: Freetext description of the Quality Control process the map as been subjected to.
  :Validation: 
  :Example:  ``Local``



result.extras.ref
-------------------------------------------------------------------------

  :Data type: String
  :Description: The filename base (ie minus it's extension) of the map's source .mxd file (presuming it was produced in ArcGIS)
  :Validation: 
  :Example:  ``MA013v4_ImpactMap_BNGRCData_District_DispAct``



result.extras.reliefweb_theme_id_hint
-------------------------------------------------------------------------

  :Data type: integer
  :Description: The ID of the ReliefWeb theme, which the MapAction field team presume is appropriate for the map. This is provided exclusively for the convenience of the ReliefWeb editorial team. Note that the ReliefWeb editorial team, may choose to override this value, hence it may not reflect the actual value used by ReliefWeb, if and when they republish this map.
  :Validation: https://api.reliefweb.int/v1/references/themes?appname=vocabulary
  :Example: 


result.extras.scale
-------------------------------------------------------------------------

  :Data type: String
  :Description: The nominal map scale, when printed at the size specified in "papersize"
  :Validation: 
  :Example:  ``1: 5,000,000``



result.extras.sourceorg
-------------------------------------------------------------------------

  :Data type: String
  :Description: Name of the publishing organisation. This will always return the value "MapAction"
  :Validation: 
  :Example:  ``MapAction``



result.extras.summary
-------------------------------------------------------------------------

  :Data type: String
  :Description: Summary or abstract describing the map. This is normally extracted from a text box on the map itself.
  :Validation: 
  :Example:  ``Map shows the current number of displaced people (as of 17 Mar 2017) as per the data collected by BNGRC from Fokontany and other sources.``



result.extras.vunerablepeople
-------------------------------------------------------------------------

  :Data type: String
  :Description: 
  :Validation: ?
  :Example: 


result.extras.xmax
-------------------------------------------------------------------------

  :Data type: decimal
  :Description: Eastern edge of bounding box for the dataset, Given in Decimal Degrees, WGS1984. Used for GeoRSS <georss:box> element
  :Validation: xmin â‰¤ xmax â‰¤ 180
  :Example:  ``51.73``



result.extras.xmin
-------------------------------------------------------------------------

  :Data type: decimal
  :Description: Western edge of bounding box for the dataset, Given in Decimal Degrees, WGS1984. Used for GeoRSS <georss:box> element
  :Validation: -180 â‰¤ xmin â‰¤ xmax
  :Example:  ``39.27``



result.extras.ymax
-------------------------------------------------------------------------

  :Data type: decimal
  :Description: Northern edge of bounding box for the dataset, Given in Decimal Degrees, WGS1984. Used for GeoRSS <georss:box> element
  :Validation: ymin â‰¤ ymax â‰¤ 90
  :Example:  ``-11.09``



result.extras.ymin
-------------------------------------------------------------------------

  :Data type: decimal
  :Description: Southern edge of bounding box for the dataset, Given in Decimal Degrees, WGS1984. Used for GeoRSS <georss:box> element
  :Validation: -90 â‰¤ ymin â‰¤ ymax
  :Example:  ``-26.15``



result.groups
-------------------------------------------------------------------------

  :Data type: Array
  :Description: Disasters related to this dataset Note that `groups` and `events` are synonimous. Typically a dataset will only be a member of a single group, but this is by convention and not enforced.
  :Validation: http://maps.mapaction.org/api/3/action/group_list?type=event&all_fields=true
  :Example: 


result.id
-------------------------------------------------------------------------

  :Data type: String
  :Description: Internal CKAN field, which provides a unique identifier for a specific version of the dataset. Its use outside MapAction is not recommended.
  :Validation: n/a
  :Example:  ``2e7f94f9-0c6a-43c5-a09a-1d7d807deefc``



result.isopen
-------------------------------------------------------------------------

  :Data type: boolean
  :Description: Internal CKAN field - "boolean indication of whether dataset is open according to Open Knowledge Definition, based on other fields". See http://docs.ckan.org/en/latest/api/legacy-api.html
  :Validation: n/a
  :Example:  ``false``



result.license_id
-------------------------------------------------------------------------

  :Data type: String
  :Description: The ID of license group under which the map or dataproduct is published. License definitions and additional information can be found at http://opendefinition.org/
  :Validation: See `id` field in http://licenses.opendefinition.org/licenses/groups/ckan.json
  :Example:  ``"notspecified",``



result.license_title
-------------------------------------------------------------------------

  :Data type: String
  :Description: The title of license group under which the map or dataproduct is published. License definitions and additional information can be found at http://opendefinition.org/
  :Validation: See `title` field in http://licenses.opendefinition.org/licenses/groups/ckan.json
  :Example:  ``"License not specified"``



result.maintainer
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Internal CKAN field - not used
  :Validation: n/a
  :Example:  ``null``



result.maintainer_email
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Internal CKAN field - not used
  :Validation: n/a
  :Example:  ``null``



result.metadata_created
-------------------------------------------------------------------------

  :Data type: Date
  :Description: Internal CKAN field - This is the timestamp that the map was uploaded into CKAN. In general this is the date/time that it was published.
  :Validation: n/a
  :Example:  ``March 19, 2017, 7:41 AM (UTC-04:00)``



result.metadata_modified
-------------------------------------------------------------------------

  :Data type: Date
  :Description: Internal CKAN field - timestamp when the dataset's metadata was last modified
  :Validation: n/a
  :Example:  ``2016-12-19T12:31:21.742889``



result.name
-------------------------------------------------------------------------

  :Data type: String
  :Description: The version specific productID.   This version of the product can be access via the Web UI as: https://maps.mapaction.org/dataset/<productID> and via the API as: https://maps.mapaction.org/api/3/action/package_show?id=<productID>
  :Validation: n/a
  :Example:  ``"00246-ma001-v1"``



result.notes
-------------------------------------------------------------------------

  :Data type: String
  :Description: Summary or abstract describing the map. This is normally extracted from a text box on the map itself.
  :Validation: no
  :Example:  ``"El mapa muestra la extension de la inundaciÃ³n conocida a 17 de abril de 2016. Los datos de las zonas afectadas provienen del OCHA. AdemÃ¡s el mapa muestra las Ã¡reas de administraciÃ³n y los rÃ­os principales.",``



result.notes
-------------------------------------------------------------------------

  :Data type: String
  :Description: Summary or abstract describing the map. This is normally extracted from a text box on the map itself.
  :Validation: n/a
  :Example:  ``"El mapa muestra la extension de la inundaciÃ³n conocida a 17 de abril de 2016. Los datos de las zonas afectadas provienen del OCHA. AdemÃ¡s el mapa muestra las Ã¡reas de administraciÃ³n y los rÃ­os principales.",``



result.num_resources
-------------------------------------------------------------------------

  :Data type: Integer
  :Description: The length of the result.resources array.
  :Validation: n/a
  :Example:  ``3``



result.num_tags
-------------------------------------------------------------------------

  :Data type: Integer
  :Description: Internal CKAN field - in general this appears to be equal to the length of the `product_themes` array
  :Validation: n/a
  :Example:  ``0``



result.organization
-------------------------------------------------------------------------

  :Data type: Array
  :Description: An Organization object, describing MapAction. Note that unlike most other CKAN instances, there is only ever one organisation object on MapAction's Map and Data Repository.
  :Validation: https://maps.mapaction.org/api/3/action/organization_list?all_fields=true
  :Example: 


result.owner_org
-------------------------------------------------------------------------

  :Data type: GUID
  :Description: Internal CKAN field - not used exturnally
  :Validation: n/a
  :Example:  ``"0a9ee200-c088-402a-b02d-b3cd053a9781"``



result.private
-------------------------------------------------------------------------

  :Data type: boolean
  :Description: Boolean indicating whether or not the dataset is private to MapAction members only.  Will always be false for anything accessable via the public/anonymous API
  :Validation: n/a
  :Example:  ``false``



result.product_themes
-------------------------------------------------------------------------

  :Data type: Array
  :Description: A list of zero or more humanitarian themes to which the product relates.
  :Validation: https://maps.mapaction.org/api/3/action/vocabulary_list
  :Example:  ``[ ]``



result.resources
-------------------------------------------------------------------------

  :Data type: Array
  :Description: List of files attached to this specific version of the dataset
  :Validation: n/a
  :Example: 


result.resources.cache_last_updated
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Not currently used
  :Validation: n/a
  :Example:  ``null``



result.resources.cache_url
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Not currently used
  :Validation: n/a
  :Example:  ``null``



result.resources.created
-------------------------------------------------------------------------

  :Data type: Date
  :Description: Internal CKAN field
  :Validation: n/a
  :Example:  ``"2016-12-19T11:34:30.879070"``



result.resources.description
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Not currently used
  :Validation: n/a
  :Example:  ``""``



result.resources.format
-------------------------------------------------------------------------

  :Data type: String
  :Description: Link to CKAN docs to follow
  :Validation: n/a
  :Example:  ``"PDF"``



result.resources.hash
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Not currently used
  :Validation: 
  :Example:  ``""``



result.resources.id
-------------------------------------------------------------------------

  :Data type: GUID
  :Description: Internal CKAN field
  :Validation: n/a
  :Example:  ``"fcac5699-abf3-4db7-8cd8-dfcbedf34995"``



result.resources.last_modified
-------------------------------------------------------------------------

  :Data type: Date
  :Description: Internal CKAN field
  :Validation: n/a
  :Example:  ``"2016-12-19T11:34:30.812332"``



result.resources.mimetype
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Not currently used
  :Validation: n/a
  :Example:  ``null``



result.resources.mimetype_inner
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Internal CKAN field - not used
  :Validation: n/a
  :Example:  ``null``



result.resources.name
-------------------------------------------------------------------------

  :Data type: String
  :Description: Link to CKAN docs to follow
  :Validation: n/a
  :Example:  ``"MA001_Paraguay_Zonas_Afectadas-300dpi.pdf",``



result.resources.package_id
-------------------------------------------------------------------------

  :Data type: GUID
  :Description: Internal CKAN field
  :Validation: n/a
  :Example:  ``"2e7f94f9-0c6a-43c5-a09a-1d7d807deefc"``



result.resources.position
-------------------------------------------------------------------------

  :Data type: Integer
  :Description: Internal CKAN Field - Sort order of the resource
  :Validation: n/a
  :Example:  ``0``



result.resources.resource_type
-------------------------------------------------------------------------

  :Data type: String
  :Description: Link to CKAN docs to follow
  :Validation: n/a
  :Example:  ``null``



result.resources.revision_id
-------------------------------------------------------------------------

  :Data type: GUID
  :Description: Internal CKAN field
  :Validation: n/a
  :Example:  ``"079cc44b-9a03-469e-8185-1b865f77b4cd"``



result.resources.size
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Link to CKAN docs to follow
  :Validation: n/a
  :Example:  ``null``



result.resources.state
-------------------------------------------------------------------------

  :Data type: String
  :Description: Internal CKAN field
  :Validation: "active" or "deleted"
  :Example:  ``"active"``



result.resources.url
-------------------------------------------------------------------------

  :Data type: String
  :Description: URL where the specific resource can be accessed.
  :Validation: 
  :Example:  ``"https://maps.mapaction.org/dataset/2e7f94f9-0c6a-43c5-a09a-1d7d807deefc/resource/fcac5699-abf3-4db7-8cd8-dfcbedf34995/download/ma001paraguayzonasafectadas-300dpi.pdf"``



result.resources.url_type
-------------------------------------------------------------------------

  :Data type: String
  :Description: Link to CKAN docs to follow
  :Validation: 
  :Example:  ``"upload"``



result.resources.webstore_last_updated
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Internal CKAN field - not used
  :Validation: n/a
  :Example:  ``null``



result.resources.webstore_url
-------------------------------------------------------------------------

  :Data type: n/a
  :Description: Internal CKAN field - not used
  :Validation: n/a
  :Example:  ``null``



result.revision_id
-------------------------------------------------------------------------

  :Data type: GUID
  :Description: Internal CKAN field - not used exturnally
  :Validation: n/a
  :Example:  ``"c22092f6-341f-4d8b-9551-fc3c90fae078"``



result.state
-------------------------------------------------------------------------

  :Data type: String
  :Description: Indicates whether or note a dataset is extant or deleted. Possible values are "active" or "deleted" Will always be "active" for anything accessable via the public/anonymous API
  :Validation: n/a
  :Example:  ``"active"``



result.tags
-------------------------------------------------------------------------

  :Data type: Array
  :Description: Not currently used
  :Validation: n/a
  :Example:  ``[]``



result.title
-------------------------------------------------------------------------

  :Data type: String
  :Description: Title of the map or dataproduct. Single line.
  :Validation: Not enforced, but generally compliant with RW title specification.
  :Example:  ``"Paraguay:Inundaciones - Zonas Afectadas (a 17 de Abril 2016)",``



result.type
-------------------------------------------------------------------------

  :Data type: String
  :Description: Internal CKAN field - not used
  :Validation: n/a
  :Example:  ``dataset``



result.url
-------------------------------------------------------------------------

  :Data type: String
  :Description: Internal CKAN field - not used
  :Validation: 
  :Example:  ``null``



result.version
-------------------------------------------------------------------------

  :Data type: Integer
  :Description: The version number of the specific dataset
  :Validation: n/a
  :Example:  ``4``



success
-------------------------------------------------------------------------

  :Data type: boolean
  :Description: If the endpoint called generates results or not
  :Validation: n/a
  :Example:  ``true``

