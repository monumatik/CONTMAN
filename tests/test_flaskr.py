import pytest, re

def test_config(app):
    assert app.testing

def test_homepage(client):
    assert client.get('/').status == "200 OK"

def test_wrong_url_analyze(client):
    rv = client.post('/', data=dict(
        url='wp.pl'
    ), follow_redirects=True).data
    content = str(rv)
    find = re.findall('wrong url', content.lower())
    assert len(find) == 1

def test_wrong_url_analyze(client):
    rv = client.post('/', data=dict(
        url='https://google.pl'
    ), follow_redirects=True).data
    content = str(rv)
    find = re.findall('no keywords', content.lower())
    assert len(find) == 1

def test_correct_url_analyze(client):
    rv = client.post('/', data=dict(
        url='https://wp.pl'
    ), follow_redirects=True).data
    content = str(rv)
    find = re.findall('wirtualna polska -', content.lower())
    assert len(find) > 0
