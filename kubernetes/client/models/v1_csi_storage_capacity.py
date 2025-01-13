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


class V1CSIStorageCapacity(object):
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
        'capacity': 'str',
        'kind': 'str',
        'maximum_volume_size': 'str',
        'metadata': 'V1ObjectMeta',
        'node_topology': 'V1LabelSelector',
        'storage_class_name': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'capacity': 'capacity',
        'kind': 'kind',
        'maximum_volume_size': 'maximumVolumeSize',
        'metadata': 'metadata',
        'node_topology': 'nodeTopology',
        'storage_class_name': 'storageClassName'
    }

    def __init__(self, api_version=None, capacity=None, kind=None, maximum_volume_size=None, metadata=None, node_topology=None, storage_class_name=None, local_vars_configuration=None):  # noqa: E501
        """V1CSIStorageCapacity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._capacity = None
        self._kind = None
        self._maximum_volume_size = None
        self._metadata = None
        self._node_topology = None
        self._storage_class_name = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if capacity is not None:
            self.capacity = capacity
        if kind is not None:
            self.kind = kind
        if maximum_volume_size is not None:
            self.maximum_volume_size = maximum_volume_size
        if metadata is not None:
            self.metadata = metadata
        if node_topology is not None:
            self.node_topology = node_topology
        self.storage_class_name = storage_class_name

    @property
    def api_version(self):
        """Gets the api_version of this V1CSIStorageCapacity.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1CSIStorageCapacity.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1CSIStorageCapacity.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1CSIStorageCapacity.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def capacity(self):
        """Gets the capacity of this V1CSIStorageCapacity.  # noqa: E501

        capacity is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  The semantic is currently (CSI spec 1.2) defined as: The available capacity, in bytes, of the storage that can be used to provision volumes. If not set, that information is currently unavailable.  # noqa: E501

        :return: The capacity of this V1CSIStorageCapacity.  # noqa: E501
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this V1CSIStorageCapacity.

        capacity is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  The semantic is currently (CSI spec 1.2) defined as: The available capacity, in bytes, of the storage that can be used to provision volumes. If not set, that information is currently unavailable.  # noqa: E501

        :param capacity: The capacity of this V1CSIStorageCapacity.  # noqa: E501
        :type: str
        """

        self._capacity = capacity

    @property
    def kind(self):
        """Gets the kind of this V1CSIStorageCapacity.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1CSIStorageCapacity.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1CSIStorageCapacity.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1CSIStorageCapacity.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def maximum_volume_size(self):
        """Gets the maximum_volume_size of this V1CSIStorageCapacity.  # noqa: E501

        maximumVolumeSize is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  This is defined since CSI spec 1.4.0 as the largest size that may be used in a CreateVolumeRequest.capacity_range.required_bytes field to create a volume with the same parameters as those in GetCapacityRequest. The corresponding value in the Kubernetes API is ResourceRequirements.Requests in a volume claim.  # noqa: E501

        :return: The maximum_volume_size of this V1CSIStorageCapacity.  # noqa: E501
        :rtype: str
        """
        return self._maximum_volume_size

    @maximum_volume_size.setter
    def maximum_volume_size(self, maximum_volume_size):
        """Sets the maximum_volume_size of this V1CSIStorageCapacity.

        maximumVolumeSize is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.  This is defined since CSI spec 1.4.0 as the largest size that may be used in a CreateVolumeRequest.capacity_range.required_bytes field to create a volume with the same parameters as those in GetCapacityRequest. The corresponding value in the Kubernetes API is ResourceRequirements.Requests in a volume claim.  # noqa: E501

        :param maximum_volume_size: The maximum_volume_size of this V1CSIStorageCapacity.  # noqa: E501
        :type: str
        """

        self._maximum_volume_size = maximum_volume_size

    @property
    def metadata(self):
        """Gets the metadata of this V1CSIStorageCapacity.  # noqa: E501


        :return: The metadata of this V1CSIStorageCapacity.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1CSIStorageCapacity.


        :param metadata: The metadata of this V1CSIStorageCapacity.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def node_topology(self):
        """Gets the node_topology of this V1CSIStorageCapacity.  # noqa: E501


        :return: The node_topology of this V1CSIStorageCapacity.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._node_topology

    @node_topology.setter
    def node_topology(self, node_topology):
        """Sets the node_topology of this V1CSIStorageCapacity.


        :param node_topology: The node_topology of this V1CSIStorageCapacity.  # noqa: E501
        :type: V1LabelSelector
        """

        self._node_topology = node_topology

    @property
    def storage_class_name(self):
        """Gets the storage_class_name of this V1CSIStorageCapacity.  # noqa: E501

        storageClassName represents the name of the StorageClass that the reported capacity applies to. It must meet the same requirements as the name of a StorageClass object (non-empty, DNS subdomain). If that object no longer exists, the CSIStorageCapacity object is obsolete and should be removed by its creator. This field is immutable.  # noqa: E501

        :return: The storage_class_name of this V1CSIStorageCapacity.  # noqa: E501
        :rtype: str
        """
        return self._storage_class_name

    @storage_class_name.setter
    def storage_class_name(self, storage_class_name):
        """Sets the storage_class_name of this V1CSIStorageCapacity.

        storageClassName represents the name of the StorageClass that the reported capacity applies to. It must meet the same requirements as the name of a StorageClass object (non-empty, DNS subdomain). If that object no longer exists, the CSIStorageCapacity object is obsolete and should be removed by its creator. This field is immutable.  # noqa: E501

        :param storage_class_name: The storage_class_name of this V1CSIStorageCapacity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and storage_class_name is None:  # noqa: E501
            raise ValueError("Invalid value for `storage_class_name`, must not be `None`")  # noqa: E501

        self._storage_class_name = storage_class_name

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
        if not isinstance(other, V1CSIStorageCapacity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CSIStorageCapacity):
            return True

        return self.to_dict() != other.to_dict()
