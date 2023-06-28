from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import StocksSerializer
from .models import Stocks
import json
import os
from dotenv import load_dotenv

load_dotenv()

save_path = os.path.realpath(
    os.path.join(
        os.path.dirname(__file__),
        "../src/output/individual_stock_data/2023-06-20/2023-06-20-MSFT-data.json",
    )
)

class StocksView(generics.CreateAPIView):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer


def read_json():
    with open(save_path, "r") as file:
        data_str = file.read()
        # formatted = json.load(file)
    return data_str
    # return formatted

# Create your views here.

def main(request):
    return HttpResponse(read_json())