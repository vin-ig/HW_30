import json

from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import DetailView, UpdateView

from ads.models import Ad, Category


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
	def get(self, request):
		return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
	def get(self, request):

		response = Ad.objects.all()
		result = []
		for elem in response:
			result.append({
				'id': elem.id,
				'name': elem.name,
				'author': elem.author,
				'price': elem.price,
				'description': elem.description,
				'address': elem.address,
				'is_published': elem.is_published,
			})
		return JsonResponse(result, safe=False)

	def post(self, request):
		data = json.loads(request.body)

		ad = Ad()

		ad.name = data.get('name')
		ad.author = data.get('author')
		ad.price = data.get('price')
		ad.description = data.get('description')
		ad.address = data.get('address')
		ad.is_published = data.get('is_published')

		ad.save()

		return JsonResponse({
				'id': ad.id,
				'name': ad.name,
				'author': ad.author,
				'price': ad.price,
				'description': ad.description,
				'address': ad.address,
				'is_published': ad.is_published,

		}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
	model = Category

	def get(self, request):
		response = Category.objects.all()
		result = []
		for elem in response:
			result.append({
				'id': elem.id,
				'name': elem.name,
			})
		return JsonResponse(result, safe=False)

	def post(self, request):
		data = json.loads(request.body)

		category = Category()
		category.name = data.get('name')

		category.save()

		return JsonResponse({
				'id': category.id,
				'name': category.name,
			}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(DetailView):
	model = Category

	def get(self, request, *args, **kwargs):
		super().get(request, *args, **kwargs)
		category = self.get_object()

		return JsonResponse({
				'id': category.id,
				'name': category.name,
			}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
	model = Ad

	def get(self, request, *args, **kwargs):
		super().get(request, *args, **kwargs)
		ad = self.get_object()

		return JsonResponse({
				'id': ad.id,
				'name': ad.name,
				'author': ad.author,
				'price': ad.price,
				'description': ad.description,
				'address': ad.address,
				'is_published': ad.is_published,
			}, safe=False)


class AdUpdate(UpdateView):
	pass