# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceDetails(object):
    """
    Specify one of the following values depending for the 'type' attribute based on the application that you want to migrate.

    Specify `OCIC` if you want to migrate Oracle Java Cloud Service, Oracle Analytics Cloud - Classic, Oracle Integration, and Oracle
    SOA Cloud Service applications from Oracle Cloud Infrastructure - Classic.

    Specify `INTERNAL_COMPUTE` if you have a traditional Oracle Cloud Infrastructure - Classic account and you want to migrate Oracle
    Process Cloud Service or Oracle Integration Cloud Service applications.

    Specify `OCC` if you want to migrate applications from Oracle Cloud@Customer.
    """

    #: A constant which can be used with the type property of a SourceDetails.
    #: This constant has a value of "OCIC"
    TYPE_OCIC = "OCIC"

    #: A constant which can be used with the type property of a SourceDetails.
    #: This constant has a value of "INTERNAL_COMPUTE"
    TYPE_INTERNAL_COMPUTE = "INTERNAL_COMPUTE"

    #: A constant which can be used with the type property of a SourceDetails.
    #: This constant has a value of "OCC"
    TYPE_OCC = "OCC"

    #: A constant which can be used with the type property of a SourceDetails.
    #: This constant has a value of "OCIC_IDCS"
    TYPE_OCIC_IDCS = "OCIC_IDCS"

    def __init__(self, **kwargs):
        """
        Initializes a new SourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.application_migration.models.OccSourceDetails`
        * :class:`~oci.application_migration.models.InternalSourceDetails`
        * :class:`~oci.application_migration.models.OcicSourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SourceDetails.
            Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE", "OCC", "OCIC_IDCS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'OCC':
            return 'OccSourceDetails'

        if type == 'INTERNAL_COMPUTE':
            return 'InternalSourceDetails'

        if type == 'OCIC':
            return 'OcicSourceDetails'
        else:
            return 'SourceDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SourceDetails.
        The type of source environment.

        Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE", "OCC", "OCIC_IDCS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this SourceDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SourceDetails.
        The type of source environment.


        :param type: The type of this SourceDetails.
        :type: str
        """
        allowed_values = ["OCIC", "INTERNAL_COMPUTE", "OCC", "OCIC_IDCS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
