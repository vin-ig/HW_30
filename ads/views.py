import json

from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView

from ads.models import Ad, Category


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
	def get(self, request):
		return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(ListView):
	model = Ad

	def get(self, request, *args, **kwargs):
		super().get(request, *args, **kwargs)

		ads = self.object_list

		result = []
		for ad in ads:
			result.append({
				'id': ad.id,
				'name': ad.name,
				'author': f'{ad.author.first_name} {ad.author.last_name}',
				'price': ad.price,
				'description': ad.description,
				# 'image': ad.image,
				'is_published': ad.is_published,
				'category': ad.category.name,
			})
		return JsonResponse(result, safe=False)


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


class AdCreateView(CreateView):
	model = Ad
	fields = ['name', 'author', 'price', 'description', 'image', 'is_published', 'category']

	def post(self, request, *args, **kwargs):
		super().post(request, *args, **kwargs)

		data = json.loads(request.body)

		ad = self.object.create(
			name=data.get('name'),
			author=data.get('author'),
			price=data.get('price'),
			description=data.get('description'),
			address=data.get('address'),
			is_published=data.get('is_published'),
			category=data.get('category'),
			image=data.get('image'),
		)

		return JsonResponse({
			'id': ad.id,
			'name': ad.name,
			'author': ad.author.name,
			'price': ad.price,
			'description': ad.description,
			# 'image': ad.image,
			'is_published': ad.is_published,
			'category': ad.category,
		}, safe=False)


class AdUpdateView(UpdateView):
	model = Ad
	fields = ['name', 'author', 'price', 'description', 'image', 'is_published', 'category']

	def patch(self, request, *args, **kwargs):
		super().post(request, *args, **kwargs)

		data = json.loads(request.body)
		ad = self.object

		ad.name = data.get('name')
		ad.author = data.get('author')
		ad.price = data.get('price')
		ad.description = data.get('description')
		ad.address = data.get('address')
		ad.is_published = data.get('is_published')
		ad.category = data.get('category')
		# ad.image = data.get('image')

		ad.save()

		return JsonResponse({
			'id': ad.id,
			'name': ad.name,
			'author': ad.author.name,
			'price': ad.price,
			'description': ad.description,
			# 'image': ad.image,
			'is_published': ad.is_published,
			'category': ad.category,
		}, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
	model = Ad
	success_url = '/'

	def delete(self, request, *args, **kwargs):
		super().delete(request, *args, **kwargs)

		return JsonResponse({'status': 'ok'})


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


class AdUpdate(UpdateView):
	pass
