import lineTool
token = "ijw3dk8PWagr2oCvck0E2xKFV6XIUUtdsgcJ54umtsN"
msg = "Python 語言整合通訊軟體,恭喜您"
response=lineTool.lineNotify(token,msg)
if response == 200:
    print("傳送成功")
else:
    print("傳送失敗")