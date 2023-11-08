from app.unemployment import fetch_data

def test_fetch_data():
    data = fetch_data()
    #breakpoint()

    assert isinstance(data, list)
    assert len(data) > 100
    assert isinstance(data[0], dict)
    assert list(data[0].keys())  == ['date', 'value']