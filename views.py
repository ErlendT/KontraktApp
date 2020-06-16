from django.shortcuts import get_object_or_404, render
from django.views import View, generic

from .models import Contract, Customer
# Create your views here.

def index(request):
    return render(request, 'KontraktApp/index.html')

def login(request):
    return render(request, 'KontraktApp/login.html')

class OverviewView(generic.ListView):
    template_name = 'KontraktApp/overview.html'
    context_object_name = 'all_contracts'
    
    def get_queryset(self):
        """
        returns all contracts
        """
        return Contract.objects.order_by('title')[:5]

class AllCustomersView(generic.ListView):
    model = Customer
    template_name = 'KontraktApp/customers.html'
    context_object_name = 'all_customers'

class EditCustomerView(generic.DetailView):
    model = Customer
    template_name = 'KontraktApp/editCustomer.html'
    context_object_name = 'customer'

class AllContractsView(generic.ListView):
    model = Contract
    template_name = 'KontraktApp/contacts.html'
    context_object_name = 'all_contracts'

class EditContractView(generic.DetailView, generic.detail.SingleObjectTemplateResponseMixin):
    model = Contract
    template_name = 'KontraktApp/editContract.html'
    context_object_name = 'contract'
    
    
    def get_object(self):
        path = self.request.path         
        lastPartofPath = path.rsplit('/', 2)[1]
        
        if lastPartofPath == "new":
            newObject = Contract(title="New Contract")
            return newObject

        else:
            contractId = self.kwargs['pk']
            return get_object_or_404(Contract,pk=contractId)
        