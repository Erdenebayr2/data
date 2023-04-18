from django.shortcuts import render
from django.http import FileResponse
from django.views import View
from django.http import Http404
import requests,os
from bs4 import BeautifulSoup
from datetime import date,datetime,timedelta
import xlsxwriter

class DownloadFileView(View):
    def get(self, request, *args, **kwargs):
        i = 1
        while i > 0:
            url = "https://www.unegui.mn/avto-mashin/-avtomashin-zarna/?page=" + str(i)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            links = soup.find_all('a',{"class": "announcement-block__title"})
            link_urls = [link.get("href") for link in links]
            for urls in link_urls:
                urls = "https://www.unegui.mn" + str(urls)
                with open('static/urls.txt', 'a') as f:
                    f.write(str(urls))
                    f.write("\n")
            i = i - 1
        with open("static/urls.txt", "r") as file:
            content = file.read().split("\n")
            content = [element for element in content if element != '']
            print(content)
            s = []
            l = len(content)
        for i in range(l):
            s.append(content)
        for ii in s:
            url = list(set(ii))

        main = []
        len_url = len(url)
        print(len_url)

        for i in range(0,len_url):
            get_url = url[i]
            print(url[i])
            response = requests.get(get_url)
            soup = BeautifulSoup(response.content,'html.parser')

            title = soup.find('h1').text.split('\n') # get title
            title = [element for element in title if element != '']
            title = [line.strip() for line in title if line.strip()][0].split(',')[0]

            data = soup.find('ul',class_='breadcrumbs').text.split('\n')
            data = [element for element in data if element != '']
            company = data[-2]
            mark = data[-1]

            main_data = soup.find('ul',class_='chars-column')
            main_data = main_data.text.split('\n')
            main_data = [element for element in main_data if element != '']
            main_data = [line.strip() for line in main_data if line.strip()]
            main_data[1] = main_data[1][:3]
            main_data[1] = float(main_data[1])*1000
            main_data[1] = str(main_data[1])
            main_data[-5] = main_data[-5][:-4]

            if 'Хаяг байршил:' not in main_data:
                main_data.insert(20,'Хаяг байршил:')
                main_data.insert(21,' ')

            data_dict = {}
            for i in range(0, len(main_data), 2):
                    data_dict[main_data[i]] = main_data[i+1]
                    print(data_dict)


            ogno = soup.select_one('span.date-meta').text[11:-6] if soup.select_one('span.date-meta') else None
            unuudr = 'Өнөөдөр'
            uchigdur = 'Өчигдөр'
            yester = datetime.now() - timedelta(days=1)
            yesterday = str(yester.date())
            today = str(date.today())

            if ogno == unuudr:
                ogno = today
            elif ogno == uchigdur:
                ogno = yesterday

            price = soup.find('meta', {'itemprop': 'price'})['content']

            desc = soup.find('div', class_='js-description').text.split('\n')
            desc = [element for element in desc if element != ''][0]

            data_dict['Үнэ'] = price
            dicts = {'Үйлдвэрлэгч':company,'Марк':mark,'Огноо':ogno}
            dicts.update(data_dict)
            main.append(dicts)

            workbook = xlsxwriter.Workbook("static/automashin-zarna.xlsx")
            worksheet = workbook.add_worksheet("firstSheet")

            col = ['Үйлдвэрлэгч','Марк','Зар тавьсан огноо','Мотор багтаамж:','Хурдны хайрцаг:','Хүрд:',
                'Төрөл:','Өнгө:','Үйлдвэрлэсэн он:','Орж ирсэн он:','Хөдөлгүүр:',
                'Дотор өнгө:','Лизинг:','Хаяг байршил:','Хөтлөгч:','Явсан:','Нөхцөл:',
                'Хаалга:','Үнэ']

            lcol = len(col)
            for i in range(0, lcol):
                worksheet.write(0,i,col[i])
            for index,entry in enumerate(main):
                worksheet.write(index+1, 0,entry['Үйлдвэрлэгч'])
                worksheet.write(index+1, 1,entry['Марк'])
                worksheet.write(index+1, 2,entry['Огноо'])
                worksheet.write(index+1, 3,entry['Мотор багтаамж:'])
                worksheet.write(index+1, 4,entry['Хурдны хайрцаг:'])
                worksheet.write(index+1, 5,entry['Хүрд:'])
                worksheet.write(index+1, 6,entry['Төрөл:'])
                worksheet.write(index+1, 7,entry['Өнгө:'])
                worksheet.write(index+1, 8,entry['Үйлдвэрлэсэн он:'])
                worksheet.write(index+1, 9,entry['Орж ирсэн он:'])
                worksheet.write(index+1, 10,entry['Хөдөлгүүр:'])
                worksheet.write(index+1, 11,entry['Дотор өнгө:'])
                worksheet.write(index+1, 12,entry['Лизинг:'])
                worksheet.write(index+1, 13,entry['Хаяг байршил:'])
                worksheet.write(index+1, 14,entry['Хөтлөгч:'])
                worksheet.write(index+1, 15,entry['Явсан:'])
                worksheet.write(index+1, 16,entry['Нөхцөл:'])
                worksheet.write(index+1, 17,entry['Хаалга:'])
                worksheet.write(index+1, 18,entry['Үнэ'])

            workbook.close()
        file_path = 'static/automashin-zarna.xlsx'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = FileResponse(fh.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
        raise Http404

def index(request):
    if request.method == 'GET':
        link = request.GET.get('link')
        print(link)
    return render(request, 'index.html')

def autoZ(request):
    mlink = "https://www.unegui.mn/avto-mashin/-avtomashin-zarna"
    return render(request, 'autoZ.html',context={'mlink':mlink})
