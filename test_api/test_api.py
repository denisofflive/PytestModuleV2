import requests
import pytest

url = "https://jsonplaceholder.typicode.com/posts"

@pytest.mark.parametrize("test_input, expected_output", [
    ({}, 201),  # Successful POST request
    ({"title": "Test Title"}, 201),  # Successful POST request with data
    ({"body": "Test Body"}, 201),  # Successful POST request with data
    ({"title": "Test Title", "body": "Test Body"}, 201),  # Successful POST request with data
])
def test_post_request(test_input, expected_output):
    response = requests.post(url, json=test_input)
    assert response.status_code == expected_output

@pytest.mark.parametrize("post_id, expected_output", [
    (1, 200),  # Successful GET request
    (100, 200),  # GET request with non-existent post id
])
def test_get_request(post_id, expected_output):
    response = requests.get(f"{url}/{post_id}")
    assert response.status_code == expected_output

@pytest.mark.parametrize("post_id, test_input, expected_output", [
    (1, {"title": "Updated Title"}, 200),  # Successful PUT request
    (100, {"title": "Updated Title"}, 200),  # PUT request for non-existent post id
])
def test_put_request(post_id, test_input, expected_output):
    response = requests.put(f"{url}/{post_id}", json=test_input)
    assert response.status_code == expected_output

@pytest.mark.parametrize("post_id, expected_output", [
    (1, 200),  # Successful DELETE request
    (100, 200),  # DELETE request for non-existent post id
])
def test_delete_request(post_id, expected_output):
    response = requests.delete(f"{url}/{post_id}")
    assert response.status_code == expected_output

if __name__ == "__main__":
    pytest.main()
