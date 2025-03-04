# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .authorization_details import AuthorizationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OcicAuthorizationTokenDetails(AuthorizationDetails):
    """
    Auth Token and endpoint to access Oracle Cloud Infrastructure - Classic, which is the source environment from which you want to migrate the application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OcicAuthorizationTokenDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.application_migration.models.OcicAuthorizationTokenDetails.type` attribute
        of this class is ``OCIC_IDCS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this OcicAuthorizationTokenDetails.
            Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE", "OCC", "OCIC_IDCS"
        :type type: str

        :param client_app_url:
            The value to assign to the client_app_url property of this OcicAuthorizationTokenDetails.
        :type client_app_url: str

        :param access_token:
            The value to assign to the access_token property of this OcicAuthorizationTokenDetails.
        :type access_token: str

        """
        self.swagger_types = {
            'type': 'str',
            'client_app_url': 'str',
            'access_token': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'client_app_url': 'clientAppUrl',
            'access_token': 'accessToken'
        }

        self._type = None
        self._client_app_url = None
        self._access_token = None
        self._type = 'OCIC_IDCS'

    @property
    def client_app_url(self):
        """
        **[Required]** Gets the client_app_url of this OcicAuthorizationTokenDetails.
        AuthClient app url resource that the accesstoken is for.


        :return: The client_app_url of this OcicAuthorizationTokenDetails.
        :rtype: str
        """
        return self._client_app_url

    @client_app_url.setter
    def client_app_url(self, client_app_url):
        """
        Sets the client_app_url of this OcicAuthorizationTokenDetails.
        AuthClient app url resource that the accesstoken is for.


        :param client_app_url: The client_app_url of this OcicAuthorizationTokenDetails.
        :type: str
        """
        self._client_app_url = client_app_url

    @property
    def access_token(self):
        """
        **[Required]** Gets the access_token of this OcicAuthorizationTokenDetails.
        AccessToken to access the app endpoint.


        :return: The access_token of this OcicAuthorizationTokenDetails.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this OcicAuthorizationTokenDetails.
        AccessToken to access the app endpoint.


        :param access_token: The access_token of this OcicAuthorizationTokenDetails.
        :type: str
        """
        self._access_token = access_token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
