from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import ImdbRatingModel
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """This class defines the test suite for the imdbratingmodel model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.name = "Write world class code"
        self.popularity_99 = 83.0
        self.director = "Victor Fleming"
        self.genre = '["Adventure", " Family"," Fantasy", " Musical"]'
        self.imdb_score = 8.3
        # specify owner of a imdbratingmodel
        self.imdbratingmodel = ImdbRatingModel(name=self.name,
            popularity_99 = self.popularity_99,
            director = self.director,
            genre = self.genre,
            imdb_score = self.imdb_score,
            )

    def test_model_can_create_a_imdbratingmodel(self):
        """Test the imdbratingmodel model can create a imdbratingmodel."""
        old_count = ImdbRatingModel.objects.count()
        self.imdbratingmodel.save()
        new_count = ImdbRatingModel.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(self.imdbratingmodel), self.name)


class ViewsTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="deepak")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # Since user model instance is not serializable, use its Id/PK
        self.imdbratingmodel_data = {
                    "99popularity": 83.0,
                    "director": "Victor Fleming",
                    "genre": [
                      "Adventure",
                      " Family",
                      " Fantasy",
                      " Musical"
                    ],
                    "imdb_score": 8.3,
                    "name": "The Wizard of Oz"
                  }
        self.response = self.client.post(
            reverse('imdbratingcreate'),
            self.imdbratingmodel_data,
            format="json")

    def test_api_can_create_a_imdbratingmodel(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/imdbrating/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_imdbratingmodel(self):
        """Test the api can get a given imdbratingmodel."""
        imdbratingmodel = ImdbRatingModel.objects.get(id=1)
        response = self.client.get(
            '/imdbrating/',
            kwargs={'pk': imdbratingmodel.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, imdbratingmodel)

    def test_api_can_update_imdbratingmodel(self):
        """Test the api can update a given imdbratingmodel."""
        imdbratingmodel = ImdbRatingModel.objects.get(id=1)
        change_imdbratingmodel = {'name': 'Something new'}
        res = self.client.put(
            reverse('imdbratingdetails', kwargs={'pk': imdbratingmodel.id}),
            change_imdbratingmodel, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_imdbratingmodel(self):
        """Test the api can delete a imdbratingmodel."""
        imdbratingmodel = ImdbRatingModel.objects.get(id=1)
        response = self.client.delete(
            reverse('imdbratingdetails', kwargs={'pk': imdbratingmodel.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
