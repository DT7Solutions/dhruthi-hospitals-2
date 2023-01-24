import os
from django.shortcuts import render
from .models import HomeSlider,Popup
from googleapiclient.discovery import build
from google.oauth2 import service_account

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    slider = HomeSlider.objects.all()
    popup = Popup.objects.first()

    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        date = request.POST.get('date',"")
        branch = request.POST.get('branch',"")
        message = request.POST.get('message',"")
        obookinginfo = (name,email,phone,date,branch,message)
        print(obookinginfo)
        #addning data in gforms 
        SERVICE_ACCOUNT_FILE = os.path.join('keys.json')
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        creds = None
        creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        SAMPLE_SPREADSHEET_ID = '1zU-ISOdKyjVKWJM5zhI5qjBKx30CVYizjXLmd9QBLJY'
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
    
        name_sheet = ''
        if (branch == "1"):
            name_sheet = 'Lakshmipuram'
        elif (branch == "2"):
            name_sheet = 'Kothapeta'
        elif (branch == "3"):
            name_sheet = 'Cherila'
        else:
            name_sheet = 'Inkolu'


        aos = [[name,email,phone,name_sheet,message,date]]
        # print(type(aos))
        request1 = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                    range=name_sheet,valueInputOption="USER_ENTERED",insertDataOption="INSERT_ROWS", body={"values":aos}).execute()

        

    return render( request,'uifiles/index.html',{'slider':slider,'popup':popup})

def page_not_found_view(request, exception):
    return render(request, 'uifiles/404.html', status=404)


# def Booking_sheet(age,name,):
#     SERVICE_ACCOUNT_FILE = 'keys.json'
#     SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#     creds = None
#     creds = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)

#     # The ID and range of a sample spreadsheet.
#     SAMPLE_SPREADSHEET_ID = '1zU-ISOdKyjVKWJM5zhI5qjBKx30CVYizjXLmd9QBLJY'

#     service = build('sheets', 'v4', credentials=creds)

#     # Call the Sheets API
#     sheet = service.spreadsheets()

#     #get value from google sheets 
#     result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Sheet").execute()

#     values = result.get('values', [])
#     print(values)
#     shatename = input("enter shateet name:")
#     name_sheet = ''
#     if shatename == 'guntur':
#         name_sheet = "guntur"
#         print("guntur")
#     else:
#         name_sheet = "sheet"
#         print("sheet")

#     #update values 

#     aos = [[age,name]]
#     # request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
#     #                                     range=name_sheet,valueInputOption="USER_ENTERED", body={"values":aos}).execute()

#     request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
#                                     range=name_sheet,valueInputOption="USER_ENTERED",insertDataOption="INSERT_ROWS", body={"values":aos}).execute()


#     print(request)


def Chirala(request):
    return render(request,'uifiles/chirala-clininc.html')

def Harikrishna(request):
    return render(request,'uifiles/revuriharikrishna.html')