import json

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView

from HW_28 import settings
from ad.models import Ad
from category.models import Category
from user.models import User


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
	def get(self, request):
		return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(ListView):
	model = Ad

	def get(self, request, *args, **kwargs):
		super().get(request, *args, **kwargs)

		ads = self.object_list.select_related('author', 'category').order_by('-price')

		paginator = Paginator(ads, settings.TOTAL_ON_PAGE)
		page_num = request.GET.get('page')
		page_obj = paginator.get_page(page_num)

		result = []
		for ad in page_obj:
			result.append({
				'id': ad.id,
				'name': ad.name,
				'author': ad.author.username,
				'price': ad.price,
				'description': ad.description,
				'image': ad.image.url if ad.image else None,
				'is_published': ad.is_published,
				'category': ad.category.name,
			})
		return JsonResponse({
			'items': result,
			'num_pages': paginator.num_pages,
			'total': paginator.count,
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
			'author': ad.author.username,
			'price': ad.price,
			'description': ad.description,
			'image': ad.image.url if ad.image else None,
			'is_published': ad.is_published,
			'category': ad.category.name,
		}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
	model = Ad
	fields = ['name', 'author', 'price', 'description', 'image', 'is_published', 'category']

	def post(self, request, *args, **kwargs):
		super().post(request, *args, **kwargs)

		data = json.loads(request.body)

		ad = Ad.objects.create(
			name=data.get('name'),
			author=get_object_or_404(User, pk=data.get('author')),
			price=data.get('price'),
			description=data.get('description'),
			is_published=data.get('is_published'),
			category=get_object_or_404(Category, pk=data.get('category')),
		)

		return JsonResponse({
			'id': ad.id,
			'name': ad.name,
			'author': ad.author.username,
			'price': ad.price,
			'description': ad.description,
			'image': ad.image.url if ad.image else None,
			'is_published': ad.is_published,
			'category': ad.category.name,
		}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
	model = Ad
	fields = ['name', 'author', 'price', 'description', 'image', 'is_published', 'category']

	def patch(self, request, *args, **kwargs):
		super().post(request, *args, **kwargs)

		data = json.loads(request.body)
		ad = self.object

		ad.name = data.get('name', ad.name)
		if data.get('author'):
			ad.author = get_object_or_404(User, pk=data.get('author'))
		ad.price = data.get('price', ad.price)
		ad.description = data.get('description', ad.description)
		ad.is_published = data.get('is_published', ad.is_published)
		if data.get('category'):
			ad.category = get_object_or_404(Category, pk=data.get('category'))

		ad.save()

		return JsonResponse({
			'id': ad.id,
			'name': ad.name,
			'author': ad.author.username,
			'price': ad.price,
			'description': ad.description,
			'image': ad.image.url if ad.image else None,
			'is_published': ad.is_published,
			'category': ad.category.name,
		}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
	model = Ad
	fields = ['name', 'author', 'price', 'description', 'image', 'is_published', 'category']

	def post(self, request, *args, **kwargs):
		ad = self.get_object()

		ad.image = request.FILES['image']
		ad.save()

		return JsonResponse({
			'id': ad.id,
			'name': ad.name,
			'author': ad.author.username,
			'price': ad.price,
			'description': ad.description,
			'image': ad.image.url if ad.image else None,
			'is_published': ad.is_published,
			'category': ad.category.name,
		}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
	model = Ad
	success_url = '/'

	def delete(self, request, *args, **kwargs):
		super().delete(request, *args, **kwargs)

		return JsonResponse({'status': 'ok'})
