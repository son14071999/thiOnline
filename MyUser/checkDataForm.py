import re

def check(form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    phone_number = form.cleaned_data['phone_number']
    school = form.cleaned_data['school']
    if username == '' or username == None:
        return "Tên không được bỏ trống"
    if password == '' or password == None:
        return "Mật khẩu không được bỏ trống !"
    if phone_number != '' and phone_number != None:
        if re.search("^0[1-9][0-9]{4,9}$", phone_number):
            pass
        else:
            return "Số điện thoại không hợp lệ !"
    if school == None or school == '':
        return "Vui lòng chọn trường !"
    else:
        return "validate"