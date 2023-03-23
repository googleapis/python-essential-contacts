# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import dataclasses
import json  # type: ignore
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, path_template, rest_helpers, rest_streaming
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
import grpc  # type: ignore
from requests import __version__ as requests_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.protobuf import empty_pb2  # type: ignore

from google.cloud.essential_contacts_v1.types import service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .base import EssentialContactsServiceTransport

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class EssentialContactsServiceRestInterceptor:
    """Interceptor for EssentialContactsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EssentialContactsServiceRestTransport.

    .. code-block:: python
        class MyCustomEssentialContactsServiceInterceptor(EssentialContactsServiceRestInterceptor):
            def pre_compute_contacts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_compute_contacts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_contact(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_contact(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_contact(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_contact(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_contact(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_contacts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_contacts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_send_test_message(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_update_contact(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_contact(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EssentialContactsServiceRestTransport(interceptor=MyCustomEssentialContactsServiceInterceptor())
        client = EssentialContactsServiceClient(transport=transport)


    """

    def pre_compute_contacts(
        self,
        request: service.ComputeContactsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[service.ComputeContactsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for compute_contacts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EssentialContactsService server.
        """
        return request, metadata

    def post_compute_contacts(
        self, response: service.ComputeContactsResponse
    ) -> service.ComputeContactsResponse:
        """Post-rpc interceptor for compute_contacts

        Override in a subclass to manipulate the response
        after it is returned by the EssentialContactsService server but before
        it is returned to user code.
        """
        return response

    def pre_create_contact(
        self, request: service.CreateContactRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[service.CreateContactRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_contact

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EssentialContactsService server.
        """
        return request, metadata

    def post_create_contact(self, response: service.Contact) -> service.Contact:
        """Post-rpc interceptor for create_contact

        Override in a subclass to manipulate the response
        after it is returned by the EssentialContactsService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_contact(
        self, request: service.DeleteContactRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[service.DeleteContactRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_contact

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EssentialContactsService server.
        """
        return request, metadata

    def pre_get_contact(
        self, request: service.GetContactRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[service.GetContactRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_contact

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EssentialContactsService server.
        """
        return request, metadata

    def post_get_contact(self, response: service.Contact) -> service.Contact:
        """Post-rpc interceptor for get_contact

        Override in a subclass to manipulate the response
        after it is returned by the EssentialContactsService server but before
        it is returned to user code.
        """
        return response

    def pre_list_contacts(
        self, request: service.ListContactsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[service.ListContactsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_contacts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EssentialContactsService server.
        """
        return request, metadata

    def post_list_contacts(
        self, response: service.ListContactsResponse
    ) -> service.ListContactsResponse:
        """Post-rpc interceptor for list_contacts

        Override in a subclass to manipulate the response
        after it is returned by the EssentialContactsService server but before
        it is returned to user code.
        """
        return response

    def pre_send_test_message(
        self,
        request: service.SendTestMessageRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[service.SendTestMessageRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for send_test_message

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EssentialContactsService server.
        """
        return request, metadata

    def pre_update_contact(
        self, request: service.UpdateContactRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[service.UpdateContactRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_contact

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EssentialContactsService server.
        """
        return request, metadata

    def post_update_contact(self, response: service.Contact) -> service.Contact:
        """Post-rpc interceptor for update_contact

        Override in a subclass to manipulate the response
        after it is returned by the EssentialContactsService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class EssentialContactsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EssentialContactsServiceRestInterceptor


class EssentialContactsServiceRestTransport(EssentialContactsServiceTransport):
    """REST backend transport for EssentialContactsService.

    Manages contacts for important Google Cloud notifications.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(
        self,
        *,
        host: str = "essentialcontacts.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[EssentialContactsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or EssentialContactsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _ComputeContacts(EssentialContactsServiceRestStub):
        def __hash__(self):
            return hash("ComputeContacts")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: service.ComputeContactsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> service.ComputeContactsResponse:
            r"""Call the compute contacts method over HTTP.

            Args:
                request (~.service.ComputeContactsRequest):
                    The request object. Request message for the
                ComputeContacts method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.service.ComputeContactsResponse:
                    Response message for the
                ComputeContacts method.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*}/contacts:compute",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*}/contacts:compute",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*}/contacts:compute",
                },
            ]
            request, metadata = self._interceptor.pre_compute_contacts(
                request, metadata
            )
            pb_request = service.ComputeContactsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = service.ComputeContactsResponse()
            pb_resp = service.ComputeContactsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_compute_contacts(resp)
            return resp

    class _CreateContact(EssentialContactsServiceRestStub):
        def __hash__(self):
            return hash("CreateContact")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: service.CreateContactRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> service.Contact:
            r"""Call the create contact method over HTTP.

            Args:
                request (~.service.CreateContactRequest):
                    The request object. Request message for the CreateContact
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.service.Contact:
                    A contact that will receive
                notifications from Google Cloud.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*}/contacts",
                    "body": "contact",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*}/contacts",
                    "body": "contact",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*}/contacts",
                    "body": "contact",
                },
            ]
            request, metadata = self._interceptor.pre_create_contact(request, metadata)
            pb_request = service.CreateContactRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = service.Contact()
            pb_resp = service.Contact.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_contact(resp)
            return resp

    class _DeleteContact(EssentialContactsServiceRestStub):
        def __hash__(self):
            return hash("DeleteContact")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: service.DeleteContactRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ):
            r"""Call the delete contact method over HTTP.

            Args:
                request (~.service.DeleteContactRequest):
                    The request object. Request message for the DeleteContact
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/contacts/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/contacts/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/contacts/*}",
                },
            ]
            request, metadata = self._interceptor.pre_delete_contact(request, metadata)
            pb_request = service.DeleteContactRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _GetContact(EssentialContactsServiceRestStub):
        def __hash__(self):
            return hash("GetContact")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: service.GetContactRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> service.Contact:
            r"""Call the get contact method over HTTP.

            Args:
                request (~.service.GetContactRequest):
                    The request object. Request message for the GetContact
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.service.Contact:
                    A contact that will receive
                notifications from Google Cloud.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/contacts/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/contacts/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/contacts/*}",
                },
            ]
            request, metadata = self._interceptor.pre_get_contact(request, metadata)
            pb_request = service.GetContactRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = service.Contact()
            pb_resp = service.Contact.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_contact(resp)
            return resp

    class _ListContacts(EssentialContactsServiceRestStub):
        def __hash__(self):
            return hash("ListContacts")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: service.ListContactsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> service.ListContactsResponse:
            r"""Call the list contacts method over HTTP.

            Args:
                request (~.service.ListContactsRequest):
                    The request object. Request message for the ListContacts
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.service.ListContactsResponse:
                    Response message for the ListContacts
                method.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*}/contacts",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*}/contacts",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*}/contacts",
                },
            ]
            request, metadata = self._interceptor.pre_list_contacts(request, metadata)
            pb_request = service.ListContactsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = service.ListContactsResponse()
            pb_resp = service.ListContactsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_contacts(resp)
            return resp

    class _SendTestMessage(EssentialContactsServiceRestStub):
        def __hash__(self):
            return hash("SendTestMessage")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: service.SendTestMessageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ):
            r"""Call the send test message method over HTTP.

            Args:
                request (~.service.SendTestMessageRequest):
                    The request object. Request message for the
                SendTestMessage method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{resource=projects/*}/contacts:sendTestMessage",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{resource=folders/*}/contacts:sendTestMessage",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{resource=organizations/*}/contacts:sendTestMessage",
                    "body": "*",
                },
            ]
            request, metadata = self._interceptor.pre_send_test_message(
                request, metadata
            )
            pb_request = service.SendTestMessageRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _UpdateContact(EssentialContactsServiceRestStub):
        def __hash__(self):
            return hash("UpdateContact")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: service.UpdateContactRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> service.Contact:
            r"""Call the update contact method over HTTP.

            Args:
                request (~.service.UpdateContactRequest):
                    The request object. Request message for the UpdateContact
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.service.Contact:
                    A contact that will receive
                notifications from Google Cloud.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{contact.name=projects/*/contacts/*}",
                    "body": "contact",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{contact.name=folders/*/contacts/*}",
                    "body": "contact",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{contact.name=organizations/*/contacts/*}",
                    "body": "contact",
                },
            ]
            request, metadata = self._interceptor.pre_update_contact(request, metadata)
            pb_request = service.UpdateContactRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = service.Contact()
            pb_resp = service.Contact.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_contact(resp)
            return resp

    @property
    def compute_contacts(
        self,
    ) -> Callable[[service.ComputeContactsRequest], service.ComputeContactsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ComputeContacts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_contact(
        self,
    ) -> Callable[[service.CreateContactRequest], service.Contact]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateContact(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_contact(
        self,
    ) -> Callable[[service.DeleteContactRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteContact(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_contact(self) -> Callable[[service.GetContactRequest], service.Contact]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetContact(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_contacts(
        self,
    ) -> Callable[[service.ListContactsRequest], service.ListContactsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListContacts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def send_test_message(
        self,
    ) -> Callable[[service.SendTestMessageRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SendTestMessage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_contact(
        self,
    ) -> Callable[[service.UpdateContactRequest], service.Contact]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateContact(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("EssentialContactsServiceRestTransport",)
