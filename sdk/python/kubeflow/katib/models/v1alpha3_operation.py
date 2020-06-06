# coding: utf-8

"""
    katib

    swagger description for katib  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha3Operation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'operation_type': 'str',
        'parameters': 'list[V1alpha3ParameterSpec]'
    }

    attribute_map = {
        'operation_type': 'operationType',
        'parameters': 'parameters'
    }

    def __init__(self, operation_type=None, parameters=None):  # noqa: E501
        """V1alpha3Operation - a model defined in Swagger"""  # noqa: E501

        self._operation_type = None
        self._parameters = None
        self.discriminator = None

        if operation_type is not None:
            self.operation_type = operation_type
        if parameters is not None:
            self.parameters = parameters

    @property
    def operation_type(self):
        """Gets the operation_type of this V1alpha3Operation.  # noqa: E501


        :return: The operation_type of this V1alpha3Operation.  # noqa: E501
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this V1alpha3Operation.


        :param operation_type: The operation_type of this V1alpha3Operation.  # noqa: E501
        :type: str
        """

        self._operation_type = operation_type

    @property
    def parameters(self):
        """Gets the parameters of this V1alpha3Operation.  # noqa: E501


        :return: The parameters of this V1alpha3Operation.  # noqa: E501
        :rtype: list[V1alpha3ParameterSpec]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this V1alpha3Operation.


        :param parameters: The parameters of this V1alpha3Operation.  # noqa: E501
        :type: list[V1alpha3ParameterSpec]
        """

        self._parameters = parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(V1alpha3Operation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha3Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other