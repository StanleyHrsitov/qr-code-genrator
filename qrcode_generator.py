import qrcode
image  = input("add the date you want ur qrcode to display")
img = qrcode.make(image)
type(img)
img.save("file.png")