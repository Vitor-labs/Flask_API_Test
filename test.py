import requests

BASE = "http://127.0.0.1:5000/"


def test_get():
    response = requests.get(BASE + "users/1")
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'John',
        'password': '123',
        'email': 'johndoe@gmail.com',
        'password': '123', 'fone': '123456789'}


def test_put():
    response = requests.put(BASE + "users/1", json={
        'name': 'John',
        'password': '123',
        'email': 'john@hotmail.com',
        'fone': '123456789'})
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'John',
        'password': '123',
        'email': 'john@hotmail.com',
        'fone': '123456789'}


def test_patch():
    response = requests.patch(BASE + "users/1", json={
        'name': 'John',
        'password': '12346',
        'email': 'test'})
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'John',
        'password': '12346',
        'email': 'test',
        'fone': '123456789'}


def test_post():
    response = requests.post(BASE + "users", json={
        'name': 'John',
        'password': '12346',
        'email': 'test',
        'fone': '123456789'})
    assert response.status_code == 201
    assert response.json() == {
        'id': 4,
        'name': 'John',
        'password': '12346',
        'email': 'test',
        'fone': '123456789'}


def test_delete():
    response = requests.delete(BASE + "users/1")
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'John',
        'password': '12346',
        'email': 'test',
        'fone': '123456789'}


def test_get_all():
    response = requests.get(BASE + "users")
    assert response.status_code == 200
    assert response.json() == [{
        'id': 1,
        'name': 'John',
        'password': '12346',
        'email': 'test',
        'fone': '123456789'}, {
        'id': 2,
        'name': 'Jane',
        'password': '12346',
        'email': 'test',
        'fone': '123456789'}, {
        'id': 3,
        'name': 'Mary',
        'password': '12346',
        'email': 'test',
        'fone': '123456789'}]


print("Testing...")
test_get()
test_put()
test_patch()
test_post()
test_delete()
test_get_all()
print("Done!")
