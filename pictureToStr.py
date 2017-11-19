"""
图片转字符画
"""
import argparse
from PIL import Image

#输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("width_div")
parser.add_argument("height_div")
#定义rgb值转换成字符串
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha=256):
    if alpha==0:
        return " "
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    x = int((gray/(alpha+1.0))*len(ascii_char))
    return ascii_char[x]
	
#写文件，把字符串图片写出
def write_file(out_file_name,content):
    with open(out_file_name,"w") as f:
        f.write(content)

#主函数，把图片读入，并按照大小生成字符串图片
def main(input_file="text.jpg",width_div=1,height_div=1,out_file_name="out_file"):
    text=""
    im = Image.open(input_file)
    width = im.size[0]//width_div
    height = im.size[1]//height_div
    im = im.resize((width,height),Image.NEAREST)
    for i in range(height):
        for j in range(width):
            content = im.getpixel((j,i))
            text+=get_char(*content)
        text+="\n"
    print (text)
    write_file(out_file_name,text)

if __name__ == "__main__":
	args = parser.parse_args()
	file = args.file
	width_div = int(args.width_div)
	height_div = int(args.height_div)
	main(input_file=file,width_div=width_div,height_div=height_div,out_file_name=r"C:\Users\18825\Desktop\python\out_sheep.png")