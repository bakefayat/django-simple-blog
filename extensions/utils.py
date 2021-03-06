import itertools
from django.http import HttpRequest, HttpResponse
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.utils.text import slugify
from .jalali import Gregorian, datetime_to_str, mounth_number_to_name, en_to_fa_numbers


# create unique slug.
def unique_slug(title, max_length, model_name):
    slug_candidate = slug_original = slugify(title, allow_unicode=True)[:max_length - 2]
    for i in itertools.count(1):
        if not model_name.objects.filter(slug=slug_candidate).exists():
            break
        slug_candidate = f'{slug_original}-{i}'
    return slug_candidate


def to_jalali(time):
    time = timezone.localtime(time)
    calender_to_str = datetime_to_str(time)
    jalali_format = Gregorian(calender_to_str).persian_tuple()
    month_name = mounth_number_to_name(jalali_format[1])
    combined_str = "{} {} {}, ساعت {}:{}".format(
        jalali_format[2],
        month_name,
        jalali_format[0],
        time.hour,
        time.minute,
    )
    final_str = en_to_fa_numbers(combined_str)
    return final_str


# being author/staff/superuser
def check_author_staff_superuser(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if (
            request.user.is_superuser
            or request.user.is_staff
            or request.user.is_author
        ):
            return True
    return False


# being owner of that article/staff/superuser
def check_owner_staff_superuser(request: HttpRequest, article) -> HttpResponse:
    if request.user.is_authenticated:
        if (request.user.is_superuser
            or request.user.is_staff
            or request.user.is_author
            and article.author == request.user
        ):
            request.is_ok = True
            return request
    raise PermissionDenied


def check_staff_superuser(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if (
            request.user.is_staff
            or request.user.is_superuser
        ):
            return True
    return False
