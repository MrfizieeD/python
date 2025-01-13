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


class V1ResourceRule(object):
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
        'api_groups': 'list[str]',
        'resource_names': 'list[str]',
        'resources': 'list[str]',
        'verbs': 'list[str]'
    }

    attribute_map = {
        'api_groups': 'apiGroups',
        'resource_names': 'resourceNames',
        'resources': 'resources',
        'verbs': 'verbs'
    }

    def __init__(self, api_groups=None, resource_names=None, resources=None, verbs=None, local_vars_configuration=None):  # noqa: E501
        """V1ResourceRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_groups = None
        self._resource_names = None
        self._resources = None
        self._verbs = None
        self.discriminator = None

        if api_groups is not None:
            self.api_groups = api_groups
        if resource_names is not None:
            self.resource_names = resource_names
        if resources is not None:
            self.resources = resources
        self.verbs = verbs

    @property
    def api_groups(self):
        """Gets the api_groups of this V1ResourceRule.  # noqa: E501

        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  \"*\" means all.  # noqa: E501

        :return: The api_groups of this V1ResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        """Sets the api_groups of this V1ResourceRule.

        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  \"*\" means all.  # noqa: E501

        :param api_groups: The api_groups of this V1ResourceRule.  # noqa: E501
        :type: list[str]
        """

        self._api_groups = api_groups

    @property
    def resource_names(self):
        """Gets the resource_names of this V1ResourceRule.  # noqa: E501

        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  \"*\" means all.  # noqa: E501

        :return: The resource_names of this V1ResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_names

    @resource_names.setter
    def resource_names(self, resource_names):
        """Sets the resource_names of this V1ResourceRule.

        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  \"*\" means all.  # noqa: E501

        :param resource_names: The resource_names of this V1ResourceRule.  # noqa: E501
        :type: list[str]
        """

        self._resource_names = resource_names

    @property
    def resources(self):
        """Gets the resources of this V1ResourceRule.  # noqa: E501

        Resources is a list of resources this rule applies to.  \"*\" means all in the specified apiGroups.  \"*/foo\" represents the subresource 'foo' for all resources in the specified apiGroups.  # noqa: E501

        :return: The resources of this V1ResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1ResourceRule.

        Resources is a list of resources this rule applies to.  \"*\" means all in the specified apiGroups.  \"*/foo\" represents the subresource 'foo' for all resources in the specified apiGroups.  # noqa: E501

        :param resources: The resources of this V1ResourceRule.  # noqa: E501
        :type: list[str]
        """

        self._resources = resources

    @property
    def verbs(self):
        """Gets the verbs of this V1ResourceRule.  # noqa: E501

        Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.  # noqa: E501

        :return: The verbs of this V1ResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """Sets the verbs of this V1ResourceRule.

        Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.  # noqa: E501

        :param verbs: The verbs of this V1ResourceRule.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and verbs is None:  # noqa: E501
            raise ValueError("Invalid value for `verbs`, must not be `None`")  # noqa: E501

        self._verbs = verbs

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
        if not isinstance(other, V1ResourceRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ResourceRule):
            return True

        return self.to_dict() != other.to_dict()
