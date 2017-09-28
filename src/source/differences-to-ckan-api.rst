.. title:: Other differences to the CKAN API

Other differences to the CKAN API
---------------------------------

Use of CKAN groups
^^^^^^^^^^^^^^^^^^^

We use CKAN's native groups feature to represent individual events (emergencies/crisis etc). We have renamed ``groups`` to ``events`` so the that name appears more consistantly in URLs:
``http://maps.mapaction.org/event/madagascar-2017`` instead of ``http://maps.mapaction.org/group/madagascar-2017``

This has had a slightly odd side effect on our API. To get a listing of all events you need to add the argument ``type=event`` to the ``group_list`` action. eg::

    http://maps.mapaction.org/api/3/action/group_list?type=event

Or for more detail add the argument ``all_fields=true``::

    http://maps.mapaction.org/api/3/action/group_list?type=event&all_fields=true
