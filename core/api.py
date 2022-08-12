from ninja import NinjaAPI

api = NinjaAPI()

@api.get("random/")
def test(request):
    return {"random": "success"}

@api.get("all/")
def test(request):
    return {"all": "success"}