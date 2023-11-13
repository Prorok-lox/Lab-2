from csv import reader
import xml.etree.ElementTree as ET

list = []
with open('books-en.csv','r', encoding='windows-1251') as book:
    list = book.readlines()


# amount of lines
def count_books_with_length_more_than_30():
    count = 0
    for i in list:
        if len(i.split(';')[1]) > 30:
            count += 1
    print(count)



def search_for_author():
    name = input('what are you searching for: ')
    for i in list:
        if name in i.split(';')[3] or name in i.split(';')[4]:
            print(i.split(';')[1])

def links_to_the_20_books():
    with open('result.txt','w', encoding='windows-1251') as link :
        for i in range(20):
                link.write(list[i].split(';')[1] + '. ' + list[i].split(';')[2] +' - ' + list[i].split(';')[3] + '\n')

def XML():
    flag = 0
    output = open('result.txt', 'w')
    search = input('Search for: ')
    xml_output = ET.Element('currency_dict')

    with open('civic.csv', 'r', encoding='windows-1251') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        for row in table:
            lower_case = row[2].lower()
            index = lower_case.find(search.lower())
            price = float(row[8].replace(',', '.'))  # Assuming the price is in the 9th column (index 8)

            if index != -1 and price <= 200 and year in [2014, 2016, 2017] and nominal == 1:
                print(row[2])
                flag = 1
                output.write(f'{row[0]}. {row[2]}. Цена {row[8]} рублей.\n')

                # Create an XML element for each book with Name
                name_element = ET.SubElement(xml_output, 'Name')
                name_element.text = row[2]  # Assuming Name is in the 3rd column (index 2)

        if flag == 0:
            print('Nothing found.')

    # Save the XML tree to a file
    xml_tree = ET.ElementTree(xml_output)
    xml_tree.write('currency_dict.xml')

    output.close()

# print(count_books_with_length_more_than_30())
# print(search_for_author())
# print(links_to_the_20_books())
# print(XML())