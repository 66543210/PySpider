#encoding=utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('out.html','w')
        fout.write("<html>")
        fout.write("<head>")
        fout.write(r'<meta charset="utf-8">')
        fout.write(r'<style type="text/css">th,td{border: thin dotted grey;padding: 5px;text-align: center;}')
        fout.write("</style>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr><th>标题</th><th>简介</th><th>链接</th></tr>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("<td ><a href=\"%s\">%s</a></td>" % (data['url'], data['url']))  # py默认编码为AscII，因此要转换为UTF-8
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

    def test(self):
        fout = open('out1.html', 'w')
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<title>123测试</title>")
        fout.write("</head>")
        fout.write("<body>")

        fout.write("</body>")
        fout.write("</html>")

if __name__=="__main__":
    HtmlOutputer().test()