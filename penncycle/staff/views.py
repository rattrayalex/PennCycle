# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from app.models import Bike


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "staff/index.html"

    def get_context_data(self):
        context = super(Dashboard, self).get_context_data()
        try:
            station_name = self.request.user.groups.exclude(name='Associate')[0].name
        except IndexError:
            station_name = "No Station"
        bikes_for_checkout = [b for b in Bike.objects.all() if b.location.name == station_name and b.status == 'available']
        bikes_for_checkin = [b for b in Bike.objects.all() if b.status == 'checked out']
        context['location'] = station_name
        context['bikes_for_checkout'] = bikes_for_checkout
        context['bikes_for_checkin'] = bikes_for_checkin
