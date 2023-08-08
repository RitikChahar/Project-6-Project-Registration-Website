from mega import Mega
mega = Mega()

email = "hixafe6822@lukaat.com"
password = "#burnitdown"

m = mega.login(email, password)

def upload_resume(uid):
    file_path = f"StudentForm/functions/resumes/{uid}.pdf"
    folder = m.find('Resumes')
    resume = m.upload(file_path, folder[0])
    link = m.get_upload_link(resume)
    return {
        "success":True,
        "link": link
        }

if __name__ == "__main__":
    print(check_user('21bcs9733'))