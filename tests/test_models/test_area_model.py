import pytest
from models import db, AreaModel

# Define a fixture to add sample data to the test database
@pytest.fixture
def sample_data(app):
    with app.app_context():
        area1 = AreaModel(name="Area1", surface=100.0)
        area2 = AreaModel(name="Area2", surface=200.0)
        db.session.add(area1)
        db.session.add(area2)
        db.session.commit()
        yield
        db.session.delete(area1)
        db.session.delete(area2)
        db.session.commit()


def test_area_model(client, sample_data):
    response = client.get('/areas')
    assert response.status_code == 200
    area1 = AreaModel.query.filter_by(name="Area1").first()
    area2 = AreaModel.query.filter_by(name="Area2").first()
    assert area1.name == 'Area1'
    assert area2.name == 'Area2'
    assert area1.surface == 100
    assert area2.surface == 200

def test_area_model_without_name(client, sample_data):
    area = AreaModel(surface=100.0)
    db.session.add(area)
    db.session.commit()

    response = client.get('/areas')
    assert response.status_code == 200
