# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.32
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1ControllerRevision(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'api_version': 'str',
        'data': 'object',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'revision': 'int'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'data': 'data',
        'kind': 'kind',
        'metadata': 'metadata',
        'revision': 'revision'
    }

    def __init__(self, api_version=None, data=None, kind=None, metadata=None, revision=None, local_vars_configuration=None):  # noqa: E501
        """V1ControllerRevision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._data = None
        self._kind = None
        self._metadata = None
        self._revision = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if data is not None:
            self.data = data
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        self.revision = revision

    @property
    def api_version(self):
        """Gets the api_version of this V1ControllerRevision.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1ControllerRevision.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1ControllerRevision.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1ControllerRevision.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def data(self):
        """Gets the data of this V1ControllerRevision.  # noqa: E501

        Data is the serialized representation of the state.  # noqa: E501

        :return: The data of this V1ControllerRevision.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this V1ControllerRevision.

        Data is the serialized representation of the state.  # noqa: E501

        :param data: The data of this V1ControllerRevision.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def kind(self):
        """Gets the kind of this V1ControllerRevision.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1ControllerRevision.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1ControllerRevision.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1ControllerRevision.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1ControllerRevision.  # noqa: E501


        :return: The metadata of this V1ControllerRevision.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1ControllerRevision.


        :param metadata: The metadata of this V1ControllerRevision.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def revision(self):
        """Gets the revision of this V1ControllerRevision.  # noqa: E501

        Revision indicates the revision of the state represented by Data.  # noqa: E501

        :return: The revision of this V1ControllerRevision.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this V1ControllerRevision.

        Revision indicates the revision of the state represented by Data.  # noqa: E501

        :param revision: The revision of this V1ControllerRevision.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ControllerRevision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ControllerRevision):
            return True

        return self.to_dict() != other.to_dict()
