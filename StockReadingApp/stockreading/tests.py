from datetime import date, timedelta
from django.test import TestCase
from django.db.utils import IntegrityError

from stockreading.models import StockReading

class TestStockReadingModel(TestCase):
	def test_unicity(self):
		StockReading.objects.create(
			reference_id="1234567890123",
			expiry_date=date.today()
		)
		with self.assertRaises(IntegrityError):
			StockReading.objects.create(
				reference_id="1234567890123",
				expiry_date=date.today()
			)

	def test_model_manager_filters(self):
		current = StockReading.objects.create(
			reference_id="1234567890123",
			expiry_date=date.today()
		)
		StockReading.objects.create(
			reference_id="1234567890124",
			expiry_date=date.today()
		)
		historic = StockReading.objects.create(
			reference_id="1234567890123",
			expiry_date=date.today() - timedelta(days=1)
		)
		self.assertEquals(
			StockReading.objects.filter_current().count(),
			2
		)
		self.assertEquals(
			StockReading.objects.filter_current(
				reference_id="1234567890123").count(),
			1
		)
		self.assertEquals(
			StockReading.objects.filter_current(
				reference_id="1234567890123").first().id,
			current.id
		)
		self.assertEquals(
			StockReading.objects.filter_historic().count(),
			1
		)
		self.assertEquals(
			StockReading.objects.filter_historic(
				reference_id="1234567890123").first().id,
			historic.id
		)
