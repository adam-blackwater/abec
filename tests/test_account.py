class MockResponse():

    @staticmethod
    def json():
        return {'mock-key': 'mock-response'}


def test_first():
    response = MockResponse().json()
    assert response == {'mock-key': 'mock-response'}
