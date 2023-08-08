from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from StudentForm.functions.connection import upload_otp_name_uid, check_user, get_all_data, verify_user, update_otp, update_details
from StudentForm.functions.generate_otp import generate_otp
from StudentForm.functions.upload_resume import upload_resume
from StudentForm.functions.send_mail import send_otp
import json
import os

@csrf_exempt
def get_otp(request):
    if (request.method=="POST"):
        request_data=json.loads(request.body)
        name = str.upper(request_data['name'])
        uid = str.upper(request_data['uid'])
        user = check_user(uid)
        if(user['status'] == 'not-exists'):
            otp = generate_otp()
            data = {
                'name': name,
                'uid': uid,
                'otp': otp,
                'verified': False
            }

            send_otp(uid, name, otp)
            upload_otp_name_uid(data)
            return JsonResponse ({
                "status":True,
                "message":f"Enter the 6 Digit OTP sent at {uid}@cuchd.in"
                })
        elif(user['status'] == 'exists-not-verified'):
            otp = generate_otp()
            send_otp(uid, name, otp)
            update_otp(uid, otp)
            return JsonResponse ({
                "status":True,
                "message":f"Enter the 6 Digit OTP sent at {uid}@cuchd.in"
                })
        elif(user['status'] == 'exists'):
            return JsonResponse({
                "status":False,
                "message": f"{uid} is already registered!"
                })
        else:
            return {}
    else:
        return HttpResponse("Method Not Allowed")   

@csrf_exempt
def verify_otp(request):
    if (request.method == "POST"):
        request_data=json.loads(request.body)
        otp = str(request_data['otp'])
        uid = request_data['uid']
        stored_otp = get_all_data(str.upper(uid))['otp']
        if(stored_otp == otp):
            verify_user(str.upper(uid))
            return JsonResponse({
                'status':True,
                'message':'Congratulations, you are verified!'
            })
        else:
            return JsonResponse({
                'status':False,
                'message':'OTP is not correct!'
            })
    else:
        return HttpResponse("Method Not Allowed")   

@csrf_exempt
def handle_resume_upload(request):
    if (request.method == "POST"):
        request_data=json.loads(request.body)
        uid = request_data['uid']
        resume = request_data['resumeFile']
        section = request_data['section']
        contactNumber = request_data['contactNumber']
        email = request_data['email']
        introduction = request_data['introduction']
        whyWorkWithUs = request_data['whyWorkWithUs']
        update_details({
            "uid":uid,
            "section":section,
            "contact":contactNumber,
            "email":email,
            "introduction":introduction,
            "whyWorkWithUs": whyWorkWithUs,
            "resume":resume       
        })
        return JsonResponse({
            "success":True,
            "message":"Resume Uploaded Successfully"
            })
    else:
        return HttpResponse("Method Not Allowed")   

@csrf_exempt
def get_all_details(request):
    if (request.method == "POST"):
        request_data=json.loads(request.body)
        uid = request_data['uid']
        output = get_all_data(str.upper(uid))
        if(output != None):
            output.pop('_id')
            return JsonResponse(output)
        else:
            return JsonResponse({
                "message":f"{str.upper(uid)} doesn't exist!"
            })
    else:
        return HttpResponse("Method Not Allowed")   