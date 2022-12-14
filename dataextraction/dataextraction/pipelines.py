# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import xlsxwriter
import pandas as pd

class DataextractionPipeline:
    def process_item(self, item, spider):
        print("pipeline= "+item['url'])
        pos = 0
        with open('././positive-words.txt', 'r') as f:
            for line in f:
                if 'abound' in line:
                    pos+=1

        # for line in open('positive-words.txt').readlines():
        #     if 'abound' in line:
        #         pos += 1
        #     print("line= ",line)
        #
        # print('pos= ',pos)
        # workbook = xlsxwriter.Workbook('output.xlsx')
        # worksheet = workbook.add_worksheet()
        # worksheet.write('A2', pos)
        # worksheet.write('B1', 'Geeks')
        # worksheet.write('C1', 'For')
        # worksheet.write('D1', 'Geeks')
        #
        # Finally, close the Excel file
        # via the close() method.
        # workbook.close()

        # new_list = [["first", "second"], ["third", "four"], ["five", "six"]]
        # df = pd.DataFrame(new_list)

        df = pd.DataFrame({'URL': item[0]})
        writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
        df.to_excel(writer)

        writer.save()
        return item
