from flask import url_for
from flask_testing import TestCase
from application import app, db

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app
   
class TestViews(TestBase):
    # Test whether we get a successful response from our routes
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
    
    def test_create_award_get(self):
        response = self.client.get(url_for('create_award'))
        self.assert200(response)

    def test_read_awards_get(self):
        response = self.client.get(url_for('read_awards'))
        self.assert200(response)

    def test_update_award_get(self):
        response = self.client.get(url_for('update_award', id=1))
        self.assert200(response)

class TestRead(TestBase):

    def test_read_home_awards(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Run unit tests", response.data)
    
    def test_read_awards_dictionary(self):
        response = self.client.get(url_for('read_awards'))
        self.assertIn(b"Run unit tests", response.data)

class TestCreate(TestBase):

    def test_create_award(self):
        response = self.client.post(
            url_for('create_award'),
            data={"description": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
    
class TestUpdate(TestBase):

    def test_update_award(self):
        response = self.client.post(
            url_for('update_award', id=1),
            data={"description": "Testing update functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing update functionality", response.data)
    
    #def test_complete_award(self):
    #    response = self.client.get(url_for('complete_award', id=1), follow_redirects=True)
    #    self.assertEqual(awards.query.get(1).completed, True)
    
    #def test_incomplete_award(self):
     #   response = self.client.get(url_for('incomplete_award', id=1), follow_redirects=True)
    #    self.assertEqual(awards.query.get(1).completed, False)
        
class TestDelete(TestBase):

    def test_delete_award(self):
        response = self.client.get(
            url_for('delete_award', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data)
