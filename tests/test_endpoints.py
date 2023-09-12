import json
import requests
import urllib.parse as urlparse
""" Generate unit test for endpoints.py FastAPI functions """


base_url = 'http://localhost:8889'

url = "https://bergum.medium.com/four-mistakes-when-introducing-embeddings-and-vector-search-d39478a568c5#tour"
payload = {"url": url}

# Unit test for create bookmart


# use requests to call /bookmark endpoint with jpage as payload
# check response status code
# check response content
def test_bookmark_end_to_end_workflow():
    response = requests.post(f"{base_url}/bookmark", json=payload)
    bookmark_id = response.json()['id']
    assert bookmark_id != None

    url = urlparse.quote(payload['url'], safe='')
    params = {"url": url}
    response = requests.get(f"{base_url}/bookmark", params=params)
    status_code = response.status_code
    assert status_code == 200

    response = requests.get(f"{base_url}/bookmark/{bookmark_id}/document")
    status_code = response.status_code
    assert status_code == 200
    # URL that is returned is was normalized
    # so it is not equal to the original URL
    # but it is a substring of the original URL
    doc = response.json()
    assert len(doc['url']) <= len(url)

    assert type(doc['summary_generated']) == str
    assert type(doc['summary_bullet_points']) == str
    assert type(doc['found_entities_raw']) == str

    assert len(doc['summary_generated']) > 10
    assert len(doc['summary_bullet_points']) > 10
    assert len(doc['found_entities_raw']) > 10

    response = requests.delete(f"{base_url}/bookmark/{bookmark_id}/document")
    status_code = response.status_code
    assert status_code == 204

    response = requests.get(f"{base_url}/bookmark/{bookmark_id}/document")
    status_code = response.status_code
    assert status_code == 404


def test_create_bookmark_not_found():
    url = urlparse.quote("https://www.google.com", safe='')
    payload = {"url": url}
    response = requests.post(f"{base_url}/bookmark", json=payload)
    status_code = response.status_code
    assert status_code == 404


def test_get_bookmark_not_found():
    url = urlparse.quote("https://www.google.com", safe='')
    params = {"url": url}
    response = requests.get(f"{base_url}/bookmark", params=params)
    print(f"Test get bookmark not found response {response.json()}")
    status_code = response.status_code
    assert status_code == 404


def test_get_document():
    response = requests.post(f"{base_url}/bookmark", json=payload)
    id = response.json()['document_id']
    response = None
    response = requests.get(f"{base_url}/document/{id}")
    assert response.status_code == 200