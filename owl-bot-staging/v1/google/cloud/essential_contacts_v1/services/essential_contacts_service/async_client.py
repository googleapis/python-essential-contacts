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
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union

from google.cloud.essential_contacts_v1 import gapic_version as package_version

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.essential_contacts_v1.services.essential_contacts_service import pagers
from google.cloud.essential_contacts_v1.types import enums
from google.cloud.essential_contacts_v1.types import service
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import EssentialContactsServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import EssentialContactsServiceGrpcAsyncIOTransport
from .client import EssentialContactsServiceClient


class EssentialContactsServiceAsyncClient:
    """Manages contacts for important Google Cloud notifications."""

    _client: EssentialContactsServiceClient

    DEFAULT_ENDPOINT = EssentialContactsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = EssentialContactsServiceClient.DEFAULT_MTLS_ENDPOINT

    contact_path = staticmethod(EssentialContactsServiceClient.contact_path)
    parse_contact_path = staticmethod(EssentialContactsServiceClient.parse_contact_path)
    common_billing_account_path = staticmethod(EssentialContactsServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(EssentialContactsServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(EssentialContactsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(EssentialContactsServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(EssentialContactsServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(EssentialContactsServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(EssentialContactsServiceClient.common_project_path)
    parse_common_project_path = staticmethod(EssentialContactsServiceClient.parse_common_project_path)
    common_location_path = staticmethod(EssentialContactsServiceClient.common_location_path)
    parse_common_location_path = staticmethod(EssentialContactsServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            EssentialContactsServiceAsyncClient: The constructed client.
        """
        return EssentialContactsServiceClient.from_service_account_info.__func__(EssentialContactsServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            EssentialContactsServiceAsyncClient: The constructed client.
        """
        return EssentialContactsServiceClient.from_service_account_file.__func__(EssentialContactsServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return EssentialContactsServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> EssentialContactsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            EssentialContactsServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(EssentialContactsServiceClient).get_transport_class, type(EssentialContactsServiceClient))

    def __init__(self, *,
            credentials: Optional[ga_credentials.Credentials] = None,
            transport: Union[str, EssentialContactsServiceTransport] = "grpc_asyncio",
            client_options: Optional[ClientOptions] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the essential contacts service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.EssentialContactsServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = EssentialContactsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def create_contact(self,
            request: Optional[Union[service.CreateContactRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            contact: Optional[service.Contact] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Contact:
        r"""Adds a new contact for a resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import essential_contacts_v1

            async def sample_create_contact():
                # Create a client
                client = essential_contacts_v1.EssentialContactsServiceAsyncClient()

                # Initialize request argument(s)
                request = essential_contacts_v1.CreateContactRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_contact(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.essential_contacts_v1.types.CreateContactRequest, dict]]):
                The request object. Request message for the CreateContact
                method.
            parent (:class:`str`):
                Required. The resource to save this contact for. Format:
                organizations/{organization_id}, folders/{folder_id} or
                projects/{project_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            contact (:class:`google.cloud.essential_contacts_v1.types.Contact`):
                Required. The contact to create. Must
                specify an email address and language
                tag.

                This corresponds to the ``contact`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.essential_contacts_v1.types.Contact:
                A contact that will receive
                notifications from Google Cloud.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, contact])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.CreateContactRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if contact is not None:
            request.contact = contact

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_contact,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_contact(self,
            request: Optional[Union[service.UpdateContactRequest, dict]] = None,
            *,
            contact: Optional[service.Contact] = None,
            update_mask: Optional[field_mask_pb2.FieldMask] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Contact:
        r"""Updates a contact.
        Note: A contact's email address cannot be changed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import essential_contacts_v1

            async def sample_update_contact():
                # Create a client
                client = essential_contacts_v1.EssentialContactsServiceAsyncClient()

                # Initialize request argument(s)
                request = essential_contacts_v1.UpdateContactRequest(
                )

                # Make the request
                response = await client.update_contact(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.essential_contacts_v1.types.UpdateContactRequest, dict]]):
                The request object. Request message for the UpdateContact
                method.
            contact (:class:`google.cloud.essential_contacts_v1.types.Contact`):
                Required. The contact resource to
                replace the existing saved contact.
                Note: the email address of the contact
                cannot be modified.

                This corresponds to the ``contact`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The update mask applied to the resource. For
                the ``FieldMask`` definition, see
                https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.essential_contacts_v1.types.Contact:
                A contact that will receive
                notifications from Google Cloud.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([contact, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.UpdateContactRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if contact is not None:
            request.contact = contact
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_contact,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("contact.name", request.contact.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_contacts(self,
            request: Optional[Union[service.ListContactsRequest, dict]] = None,
            *,
            parent: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListContactsAsyncPager:
        r"""Lists the contacts that have been set on a resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import essential_contacts_v1

            async def sample_list_contacts():
                # Create a client
                client = essential_contacts_v1.EssentialContactsServiceAsyncClient()

                # Initialize request argument(s)
                request = essential_contacts_v1.ListContactsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_contacts(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.essential_contacts_v1.types.ListContactsRequest, dict]]):
                The request object. Request message for the ListContacts
                method.
            parent (:class:`str`):
                Required. The parent resource name. Format:
                organizations/{organization_id}, folders/{folder_id} or
                projects/{project_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.essential_contacts_v1.services.essential_contacts_service.pagers.ListContactsAsyncPager:
                Response message for the ListContacts
                method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.ListContactsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_contacts,
            default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListContactsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_contact(self,
            request: Optional[Union[service.GetContactRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> service.Contact:
        r"""Gets a single contact.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import essential_contacts_v1

            async def sample_get_contact():
                # Create a client
                client = essential_contacts_v1.EssentialContactsServiceAsyncClient()

                # Initialize request argument(s)
                request = essential_contacts_v1.GetContactRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_contact(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.essential_contacts_v1.types.GetContactRequest, dict]]):
                The request object. Request message for the GetContact
                method.
            name (:class:`str`):
                Required. The name of the contact to retrieve. Format:
                organizations/{organization_id}/contacts/{contact_id},
                folders/{folder_id}/contacts/{contact_id} or
                projects/{project_id}/contacts/{contact_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.essential_contacts_v1.types.Contact:
                A contact that will receive
                notifications from Google Cloud.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.GetContactRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_contact,
            default_retry=retries.Retry(
initial=1.0,maximum=10.0,multiplier=1.3,                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_contact(self,
            request: Optional[Union[service.DeleteContactRequest, dict]] = None,
            *,
            name: Optional[str] = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Deletes a contact.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import essential_contacts_v1

            async def sample_delete_contact():
                # Create a client
                client = essential_contacts_v1.EssentialContactsServiceAsyncClient()

                # Initialize request argument(s)
                request = essential_contacts_v1.DeleteContactRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_contact(request=request)

        Args:
            request (Optional[Union[google.cloud.essential_contacts_v1.types.DeleteContactRequest, dict]]):
                The request object. Request message for the DeleteContact
                method.
            name (:class:`str`):
                Required. The name of the contact to delete. Format:
                organizations/{organization_id}/contacts/{contact_id},
                folders/{folder_id}/contacts/{contact_id} or
                projects/{project_id}/contacts/{contact_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = service.DeleteContactRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_contact,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def compute_contacts(self,
            request: Optional[Union[service.ComputeContactsRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ComputeContactsAsyncPager:
        r"""Lists all contacts for the resource that are
        subscribed to the specified notification categories,
        including contacts inherited from any parent resources.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import essential_contacts_v1

            async def sample_compute_contacts():
                # Create a client
                client = essential_contacts_v1.EssentialContactsServiceAsyncClient()

                # Initialize request argument(s)
                request = essential_contacts_v1.ComputeContactsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.compute_contacts(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.essential_contacts_v1.types.ComputeContactsRequest, dict]]):
                The request object. Request message for the
                ComputeContacts method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.essential_contacts_v1.services.essential_contacts_service.pagers.ComputeContactsAsyncPager:
                Response message for the
                ComputeContacts method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ComputeContactsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.compute_contacts,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ComputeContactsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def send_test_message(self,
            request: Optional[Union[service.SendTestMessageRequest, dict]] = None,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Allows a contact admin to send a test message to
        contact to verify that it has been configured correctly.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import essential_contacts_v1

            async def sample_send_test_message():
                # Create a client
                client = essential_contacts_v1.EssentialContactsServiceAsyncClient()

                # Initialize request argument(s)
                request = essential_contacts_v1.SendTestMessageRequest(
                    contacts=['contacts_value1', 'contacts_value2'],
                    resource="resource_value",
                    notification_category="TECHNICAL_INCIDENTS",
                )

                # Make the request
                await client.send_test_message(request=request)

        Args:
            request (Optional[Union[google.cloud.essential_contacts_v1.types.SendTestMessageRequest, dict]]):
                The request object. Request message for the
                SendTestMessage method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        request = service.SendTestMessageRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.send_test_message,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("resource", request.resource),
            )),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)


__all__ = (
    "EssentialContactsServiceAsyncClient",
)
