from repositories.async_client import AsyncReqResClient


def test_get_requests():
    client = AsyncReqResClient()
    responses = client.get_requests(user_ids=[1, 2, 3])
    assert len(responses) == 3
    assert [response['data']['id'] for response in responses] == [1, 2, 3]
