
from rest_framework.test import APITestCase
from .models import MenuItem, TableBooking

class MenuItemTestCase(APITestCase):
    def test_create_menu_item(self):
        response = self.client.post('/api/menu/', {'name': 'Pizza', 'description': 'Cheese Pizza', 'price': 9.99})
        self.assertEqual(response.status_code, 201)

class TableBookingTestCase(APITestCase):
    def test_create_booking(self):
        response = self.client.post('/api/bookings/', {'customer_name': 'John Doe', 'booking_time': '2024-11-01T18:00:00Z', 'number_of_people': 4})
        self.assertEqual(response.status_code, 201)
