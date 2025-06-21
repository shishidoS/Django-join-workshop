from django.shortcuts import render

# Create your views here.
def profile_view(request):
    # ここでHTMLに渡すデータを作成します
    context = {
        'name': 'IS13L宍戸翔大',
        'message': 'Djangoの世界へようこそ！一緒に頑張りましょう。'
    }
    return render(request, 'profile.html', context)