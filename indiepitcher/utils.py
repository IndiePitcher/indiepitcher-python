import requests

from indiepitcher.models import BaseIndiePitcherModel, IndiePitcherResponseError


class ErrorResponse(BaseIndiePitcherModel):
    reason: str


def raise_for_invalid_status(response: requests.Response) -> None:
    if response.status_code >= 400:
        decodedResponse = ErrorResponse.model_validate_json(response.content)
        raise IndiePitcherResponseError(
            status_code=response.status_code, reason=decodedResponse.reason
        )
