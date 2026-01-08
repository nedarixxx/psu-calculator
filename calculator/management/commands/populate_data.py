from django.core.management.base import BaseCommand
from calculator.models import Category, Component


class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми компонентами ПК'

    def handle(self, *args, **options):
        # Очистка существующих данных (опционально)
        Category.objects.all().delete()

        # Создание категорий
        categories = {
            'CPU': Category.objects.get_or_create(
                name='Процессор',
                defaults={'slug': 'processor', 'description': 'Центральный процессор'}
            )[0],
            'GPU': Category.objects.get_or_create(
                name='Видеокарта',
                defaults={'slug': 'gpu', 'description': 'Графический процессор'}
            )[0],
            'RAM': Category.objects.get_or_create(
                name='Память',
                defaults={'slug': 'memory', 'description': 'Оперативная память'}
            )[0],
            'SSD': Category.objects.get_or_create(
                name='Накопитель',
                defaults={'slug': 'storage', 'description': 'SSD или HDD'}
            )[0],
            'PSU': Category.objects.get_or_create(
                name='Блок питания',
                defaults={'slug': 'psu', 'description': 'Power Supply Unit'}
            )[0],
            'COOLER': Category.objects.get_or_create(
                name='Система охлаждения',
                defaults={'slug': 'cooler', 'description': 'Система охлаждения CPU'}
            )[0],
        }

        # Процессоры
        processors = [
            # Intel 14th Gen (LGA1700)
            {'name': 'Intel Core i9-14900K', 'power_draw': 253, 'peak_power': 320, 'price': 60000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-14900KF', 'power_draw': 253, 'peak_power': 320, 'price': 58000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-14900', 'power_draw': 219, 'peak_power': 270, 'price': 53000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-14900F', 'power_draw': 219, 'peak_power': 270, 'price': 51000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-14700K', 'power_draw': 253, 'peak_power': 320, 'price': 42000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-14700KF', 'power_draw': 253, 'peak_power': 320, 'price': 40000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-14700', 'power_draw': 219, 'peak_power': 270, 'price': 38000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-14700F', 'power_draw': 219, 'peak_power': 270, 'price': 36000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-14600K', 'power_draw': 181, 'peak_power': 220, 'price': 28000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-14600KF', 'power_draw': 181, 'peak_power': 220, 'price': 26000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-14600', 'power_draw': 154, 'peak_power': 185, 'price': 25000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-14500', 'power_draw': 154, 'peak_power': 185, 'price': 23000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-14400', 'power_draw': 154, 'peak_power': 185, 'price': 20000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-14400F', 'power_draw': 148, 'peak_power': 180, 'price': 18000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-14100', 'power_draw': 89, 'peak_power': 110, 'price': 13000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-14100F', 'power_draw': 89, 'peak_power': 110, 'price': 12000, 'form_factor': 'LGA1700'},

            # Intel 13th Gen (LGA1700)
            {'name': 'Intel Core i9-13900KS', 'power_draw': 253, 'peak_power': 350, 'price': 70000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-13900K', 'power_draw': 253, 'peak_power': 320, 'price': 55000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-13900KF', 'power_draw': 253, 'peak_power': 320, 'price': 53000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-13900', 'power_draw': 219, 'peak_power': 270, 'price': 50000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-13900F', 'power_draw': 219, 'peak_power': 270, 'price': 48000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-13900T', 'power_draw': 106, 'peak_power': 130, 'price': 45000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-13700K', 'power_draw': 253, 'peak_power': 320, 'price': 45000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-13700KF', 'power_draw': 253, 'peak_power': 320, 'price': 43000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-13700', 'power_draw': 219, 'peak_power': 270, 'price': 40000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-13700F', 'power_draw': 219, 'peak_power': 270, 'price': 38000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-13700T', 'power_draw': 106, 'peak_power': 130, 'price': 35000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-13600K', 'power_draw': 181, 'peak_power': 220, 'price': 28000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-13600KF', 'power_draw': 181, 'peak_power': 220, 'price': 26000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-13600', 'power_draw': 154, 'peak_power': 185, 'price': 24000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-13600T', 'power_draw': 92, 'peak_power': 115, 'price': 22000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-13500', 'power_draw': 154, 'peak_power': 185, 'price': 21000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-13500T', 'power_draw': 92, 'peak_power': 115, 'price': 19000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-13400', 'power_draw': 154, 'peak_power': 185, 'price': 18000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-13400F', 'power_draw': 148, 'peak_power': 180, 'price': 16500, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-13400T', 'power_draw': 92, 'peak_power': 115, 'price': 15000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-13100', 'power_draw': 89, 'peak_power': 110, 'price': 12000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-13100F', 'power_draw': 89, 'peak_power': 110, 'price': 11000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-13100T', 'power_draw': 69, 'peak_power': 85, 'price': 10000, 'form_factor': 'LGA1700'},

            # Intel 12th Gen (LGA1700)
            {'name': 'Intel Core i9-12900KS', 'power_draw': 241, 'peak_power': 300, 'price': 60000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-12900K', 'power_draw': 241, 'peak_power': 300, 'price': 50000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-12900KF', 'power_draw': 241, 'peak_power': 300, 'price': 48000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-12900', 'power_draw': 202, 'peak_power': 250, 'price': 45000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-12900F', 'power_draw': 202, 'peak_power': 250, 'price': 43000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i9-12900T', 'power_draw': 106, 'peak_power': 130, 'price': 40000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-12700K', 'power_draw': 190, 'peak_power': 240, 'price': 38000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-12700KF', 'power_draw': 190, 'peak_power': 240, 'price': 36000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-12700', 'power_draw': 180, 'peak_power': 220, 'price': 33000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-12700F', 'power_draw': 180, 'peak_power': 220, 'price': 31000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i7-12700T', 'power_draw': 99, 'peak_power': 125, 'price': 28000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-12600K', 'power_draw': 150, 'peak_power': 185, 'price': 25000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-12600KF', 'power_draw': 150, 'peak_power': 185, 'price': 23000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-12600', 'power_draw': 117, 'peak_power': 145, 'price': 21000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-12600T', 'power_draw': 74, 'peak_power': 95, 'price': 19000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-12500', 'power_draw': 117, 'peak_power': 145, 'price': 18000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-12500T', 'power_draw': 74, 'peak_power': 95, 'price': 16000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-12400', 'power_draw': 117, 'peak_power': 145, 'price': 17000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-12400F', 'power_draw': 117, 'peak_power': 145, 'price': 15000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i5-12400T', 'power_draw': 74, 'peak_power': 95, 'price': 14000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-12300', 'power_draw': 89, 'peak_power': 110, 'price': 12500, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-12300T', 'power_draw': 69, 'peak_power': 85, 'price': 11000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-12100', 'power_draw': 89, 'peak_power': 110, 'price': 11000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-12100F', 'power_draw': 89, 'peak_power': 110, 'price': 9500, 'form_factor': 'LGA1700'},
            {'name': 'Intel Core i3-12100T', 'power_draw': 69, 'peak_power': 85, 'price': 9000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Pentium Gold G7400', 'power_draw': 46, 'peak_power': 60, 'price': 7000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Pentium Gold G7400T', 'power_draw': 35, 'peak_power': 45, 'price': 6500, 'form_factor': 'LGA1700'},
            {'name': 'Intel Celeron G6900', 'power_draw': 46, 'peak_power': 60, 'price': 5000, 'form_factor': 'LGA1700'},
            {'name': 'Intel Celeron G6900T', 'power_draw': 35, 'peak_power': 45, 'price': 4500, 'form_factor': 'LGA1700'},

            # Intel 11th Gen (LGA1200)
            {'name': 'Intel Core i9-11900K', 'power_draw': 250, 'peak_power': 310, 'price': 42000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i9-11900KF', 'power_draw': 250, 'peak_power': 310, 'price': 40000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i9-11900', 'power_draw': 224, 'peak_power': 280, 'price': 38000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i9-11900F', 'power_draw': 224, 'peak_power': 280, 'price': 36000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i9-11900T', 'power_draw': 115, 'peak_power': 145, 'price': 33000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-11700K', 'power_draw': 250, 'peak_power': 310, 'price': 33000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-11700KF', 'power_draw': 250, 'peak_power': 310, 'price': 31000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-11700', 'power_draw': 224, 'peak_power': 280, 'price': 29000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-11700F', 'power_draw': 224, 'peak_power': 280, 'price': 27000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-11700T', 'power_draw': 115, 'peak_power': 145, 'price': 25000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-11600K', 'power_draw': 250, 'peak_power': 310, 'price': 22000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-11600KF', 'power_draw': 250, 'peak_power': 310, 'price': 20000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-11600', 'power_draw': 154, 'peak_power': 190, 'price': 19000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-11600T', 'power_draw': 84, 'peak_power': 105, 'price': 17000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-11500', 'power_draw': 154, 'peak_power': 190, 'price': 16000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-11500T', 'power_draw': 84, 'peak_power': 105, 'price': 15000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-11400', 'power_draw': 154, 'peak_power': 190, 'price': 14000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-11400F', 'power_draw': 154, 'peak_power': 190, 'price': 12500, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-11400T', 'power_draw': 84, 'peak_power': 105, 'price': 11500, 'form_factor': 'LGA1200'},

            # Intel 10th Gen (LGA1200)
            {'name': 'Intel Core i9-10900K', 'power_draw': 250, 'peak_power': 310, 'price': 38000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i9-10900KF', 'power_draw': 250, 'peak_power': 310, 'price': 36000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i9-10900', 'power_draw': 224, 'peak_power': 280, 'price': 34000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i9-10900F', 'power_draw': 224, 'peak_power': 280, 'price': 32000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i9-10900T', 'power_draw': 123, 'peak_power': 155, 'price': 29000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i9-10850K', 'power_draw': 250, 'peak_power': 310, 'price': 35000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-10700K', 'power_draw': 229, 'peak_power': 285, 'price': 28000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-10700KF', 'power_draw': 229, 'peak_power': 285, 'price': 26000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-10700', 'power_draw': 224, 'peak_power': 280, 'price': 24000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-10700F', 'power_draw': 224, 'peak_power': 280, 'price': 22000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i7-10700T', 'power_draw': 123, 'peak_power': 155, 'price': 20000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-10600K', 'power_draw': 182, 'peak_power': 230, 'price': 19000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-10600KF', 'power_draw': 182, 'peak_power': 230, 'price': 17500, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-10600', 'power_draw': 134, 'peak_power': 170, 'price': 16000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-10600T', 'power_draw': 92, 'peak_power': 115, 'price': 14500, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-10500', 'power_draw': 134, 'peak_power': 170, 'price': 14000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-10500T', 'power_draw': 92, 'peak_power': 115, 'price': 12500, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-10400', 'power_draw': 134, 'peak_power': 170, 'price': 12000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-10400F', 'power_draw': 134, 'peak_power': 170, 'price': 10500, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i5-10400T', 'power_draw': 92, 'peak_power': 115, 'price': 9500, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i3-10300', 'power_draw': 90, 'peak_power': 115, 'price': 10000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i3-10300T', 'power_draw': 55, 'peak_power': 70, 'price': 9000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i3-10100', 'power_draw': 90, 'peak_power': 115, 'price': 8500, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i3-10100F', 'power_draw': 90, 'peak_power': 115, 'price': 7500, 'form_factor': 'LGA1200'},
            {'name': 'Intel Core i3-10100T', 'power_draw': 55, 'peak_power': 70, 'price': 7000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Pentium Gold G6600', 'power_draw': 58, 'peak_power': 75, 'price': 6000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Pentium Gold G6500', 'power_draw': 58, 'peak_power': 75, 'price': 5500, 'form_factor': 'LGA1200'},
            {'name': 'Intel Pentium Gold G6400', 'power_draw': 58, 'peak_power': 75, 'price': 5000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Celeron G5925', 'power_draw': 58, 'peak_power': 75, 'price': 4000, 'form_factor': 'LGA1200'},
            {'name': 'Intel Celeron G5920', 'power_draw': 58, 'peak_power': 75, 'price': 3800, 'form_factor': 'LGA1200'},
            {'name': 'Intel Celeron G5905', 'power_draw': 58, 'peak_power': 75, 'price': 3500, 'form_factor': 'LGA1200'},

            # Intel Core Ultra Series 2 (LGA1851)
            {'name': 'Intel Core Ultra 9 285K', 'power_draw': 250, 'peak_power': 310, 'price': 68000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 9 285', 'power_draw': 182, 'peak_power': 230, 'price': 62000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 7 265K', 'power_draw': 250, 'peak_power': 310, 'price': 48000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 7 265KF', 'power_draw': 250, 'peak_power': 310, 'price': 45000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 7 265', 'power_draw': 182, 'peak_power': 230, 'price': 46000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 7 265F', 'power_draw': 182, 'peak_power': 230, 'price': 43000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 5 245K', 'power_draw': 159, 'peak_power': 200, 'price': 38000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 5 245KF', 'power_draw': 159, 'peak_power': 200, 'price': 35000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 5 245', 'power_draw': 121, 'peak_power': 155, 'price': 32000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 5 235', 'power_draw': 121, 'peak_power': 155, 'price': 29000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 5 225', 'power_draw': 121, 'peak_power': 155, 'price': 27000, 'form_factor': 'LGA1851'},
            {'name': 'Intel Core Ultra 5 225F', 'power_draw': 121, 'peak_power': 155, 'price': 25000, 'form_factor': 'LGA1851'},

            # AMD Ryzen 9000 Series (AM5)
            {'name': 'AMD Ryzen 9 9950X', 'power_draw': 230, 'peak_power': 280, 'price': 75000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 9 9900X', 'power_draw': 162, 'peak_power': 200, 'price': 55000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 7 9800X3D', 'power_draw': 162, 'peak_power': 200, 'price': 65000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 7 9700X', 'power_draw': 88, 'peak_power': 120, 'price': 40000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 5 9600X', 'power_draw': 88, 'peak_power': 120, 'price': 30000, 'form_factor': 'AM5'},

            # AMD Ryzen 8000G Series (AM5)
            {'name': 'AMD Ryzen 7 8700G', 'power_draw': 88, 'peak_power': 120, 'price': 35000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 5 8600G', 'power_draw': 88, 'peak_power': 120, 'price': 24000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 5 8500G', 'power_draw': 88, 'peak_power': 120, 'price': 19000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 3 8300G', 'power_draw': 65, 'peak_power': 88, 'price': 14000, 'form_factor': 'AM5'},

            # AMD Ryzen 7000 Series (AM5)
            {'name': 'AMD Ryzen 9 7950X3D', 'power_draw': 162, 'peak_power': 200, 'price': 60000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 9 7950X', 'power_draw': 230, 'peak_power': 280, 'price': 52000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 9 7900X3D', 'power_draw': 162, 'peak_power': 200, 'price': 48000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 9 7900X', 'power_draw': 230, 'peak_power': 280, 'price': 42000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 9 7900', 'power_draw': 88, 'peak_power': 120, 'price': 38000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 7 7800X3D', 'power_draw': 162, 'peak_power': 200, 'price': 48000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 7 7700X', 'power_draw': 142, 'peak_power': 175, 'price': 32000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 7 7700', 'power_draw': 88, 'peak_power': 120, 'price': 28000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 5 7600X', 'power_draw': 142, 'peak_power': 175, 'price': 22000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 5 7600', 'power_draw': 88, 'peak_power': 120, 'price': 19000, 'form_factor': 'AM5'},
            {'name': 'AMD Ryzen 5 7500F', 'power_draw': 88, 'peak_power': 120, 'price': 17000, 'form_factor': 'AM5'},

            # AMD Ryzen 5000 Series (AM4)
            {'name': 'AMD Ryzen 9 5950X', 'power_draw': 142, 'peak_power': 175, 'price': 38000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 9 5900X', 'power_draw': 142, 'peak_power': 175, 'price': 28000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 7 5800X3D', 'power_draw': 142, 'peak_power': 175, 'price': 32000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 7 5700X3D', 'power_draw': 105, 'peak_power': 135, 'price': 24000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 7 5800X', 'power_draw': 142, 'peak_power': 175, 'price': 20000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 7 5700X', 'power_draw': 76, 'peak_power': 100, 'price': 17000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 7 5700G', 'power_draw': 88, 'peak_power': 120, 'price': 16000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 5 5600X3D', 'power_draw': 105, 'peak_power': 135, 'price': 22000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 5 5600X', 'power_draw': 76, 'peak_power': 100, 'price': 13000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 5 5600', 'power_draw': 76, 'peak_power': 100, 'price': 11000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 5 5600G', 'power_draw': 88, 'peak_power': 120, 'price': 11500, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 5 5600GT', 'power_draw': 88, 'peak_power': 120, 'price': 12000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 5 5500', 'power_draw': 65, 'peak_power': 88, 'price': 9000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 5 5500GT', 'power_draw': 65, 'peak_power': 88, 'price': 9500, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 5 4500', 'power_draw': 65, 'peak_power': 88, 'price': 7000, 'form_factor': 'AM4'},
            {'name': 'AMD Ryzen 3 4100', 'power_draw': 65, 'peak_power': 88, 'price': 5000, 'form_factor': 'AM4'},
        ]


        # Видеокарты
        gpus = [
            # --- NVIDIA Titan Series (Enthusiast / Prosumer) ---
            {'name': 'NVIDIA Titan RTX', 'power_draw': 280, 'peak_power': 330, 'recommended_psu': 650, 'price': 75000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA Titan V', 'power_draw': 250, 'peak_power': 300, 'recommended_psu': 600, 'price': 60000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA Titan Xp', 'power_draw': 250, 'peak_power': 300, 'recommended_psu': 600, 'price': 25000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA Titan X (Pascal)', 'power_draw': 250, 'peak_power': 300, 'recommended_psu': 600, 'price': 22000, 'form_factor': 'PCI Express x16 (x16)'},
            
            # --- NVIDIA GeForce RTX 50 Series (Blackwell) ---
            {'name': 'NVIDIA GeForce RTX 5090', 'power_draw': 500, 'peak_power': 650, 'recommended_psu': 1000, 'price': 280000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 5080', 'power_draw': 350, 'peak_power': 450, 'recommended_psu': 850, 'price': 160000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 5070 Ti', 'power_draw': 285, 'peak_power': 360, 'recommended_psu': 750, 'price': 110000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 5070', 'power_draw': 220, 'peak_power': 280, 'recommended_psu': 650, 'price': 85000, 'form_factor': 'PCI Express x16 (x16)'},

            # --- NVIDIA GeForce RTX 40 Series (Ada Lovelace) ---
            {'name': 'NVIDIA GeForce RTX 4090', 'power_draw': 450, 'peak_power': 550, 'recommended_psu': 1000, 'price': 210000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 4080 Super', 'power_draw': 320, 'peak_power': 400, 'recommended_psu': 850, 'price': 125000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 4080', 'power_draw': 320, 'peak_power': 400, 'recommended_psu': 850, 'price': 115000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 4070 Ti Super', 'power_draw': 285, 'peak_power': 360, 'recommended_psu': 750, 'price': 105000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 4070 Ti', 'power_draw': 285, 'peak_power': 360, 'recommended_psu': 750, 'price': 90000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 4070 Super', 'power_draw': 220, 'peak_power': 280, 'recommended_psu': 700, 'price': 75000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 4070', 'power_draw': 200, 'peak_power': 250, 'recommended_psu': 650, 'price': 65000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 4060 Ti 16GB', 'power_draw': 165, 'peak_power': 210, 'recommended_psu': 550, 'price': 55000, 'form_factor': 'PCI Express x16 (x8)'},
            {'name': 'NVIDIA GeForce RTX 4060 Ti 8GB', 'power_draw': 160, 'peak_power': 200, 'recommended_psu': 550, 'price': 45000, 'form_factor': 'PCI Express x16 (x8)'},
            {'name': 'NVIDIA GeForce RTX 4060', 'power_draw': 115, 'peak_power': 150, 'recommended_psu': 550, 'price': 35000, 'form_factor': 'PCI Express x16 (x8)'},

            # --- NVIDIA GeForce RTX 30 Series (Ampere) ---
            {'name': 'NVIDIA GeForce RTX 3090 Ti', 'power_draw': 450, 'peak_power': 550, 'recommended_psu': 850, 'price': 100000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3090', 'power_draw': 350, 'peak_power': 450, 'recommended_psu': 850, 'price': 85000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3080 Ti', 'power_draw': 350, 'peak_power': 450, 'recommended_psu': 850, 'price': 70000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3080 12GB', 'power_draw': 350, 'peak_power': 450, 'recommended_psu': 850, 'price': 60000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3080 10GB', 'power_draw': 320, 'peak_power': 420, 'recommended_psu': 750, 'price': 55000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3070 Ti', 'power_draw': 290, 'peak_power': 370, 'recommended_psu': 750, 'price': 45000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3070', 'power_draw': 220, 'peak_power': 280, 'recommended_psu': 650, 'price': 38000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3060 Ti', 'power_draw': 200, 'peak_power': 250, 'recommended_psu': 600, 'price': 32000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3060 12GB', 'power_draw': 170, 'peak_power': 220, 'recommended_psu': 550, 'price': 28000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3060 8GB', 'power_draw': 170, 'peak_power': 220, 'recommended_psu': 550, 'price': 24000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 3050 8GB', 'power_draw': 130, 'peak_power': 165, 'recommended_psu': 550, 'price': 23000, 'form_factor': 'PCI Express x16 (x8)'},
            {'name': 'NVIDIA GeForce RTX 3050 6GB', 'power_draw': 70, 'peak_power': 90, 'recommended_psu': 450, 'price': 19000, 'form_factor': 'PCI Express x16 (x8)'},

            # --- NVIDIA GeForce RTX 20 Series (Turing) ---
            {'name': 'NVIDIA GeForce RTX 2080 Ti', 'power_draw': 250, 'peak_power': 320, 'recommended_psu': 650, 'price': 35000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 2080 Super', 'power_draw': 250, 'peak_power': 320, 'recommended_psu': 650, 'price': 30000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 2080', 'power_draw': 215, 'peak_power': 280, 'recommended_psu': 650, 'price': 28000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 2070 Super', 'power_draw': 215, 'peak_power': 280, 'recommended_psu': 650, 'price': 26000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 2070', 'power_draw': 175, 'peak_power': 230, 'recommended_psu': 550, 'price': 24000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 2060 Super', 'power_draw': 175, 'peak_power': 230, 'recommended_psu': 550, 'price': 22000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 2060 12GB', 'power_draw': 185, 'peak_power': 240, 'recommended_psu': 550, 'price': 21000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce RTX 2060 6GB', 'power_draw': 160, 'peak_power': 210, 'recommended_psu': 500, 'price': 18000, 'form_factor': 'PCI Express x16 (x16)'},

            # --- NVIDIA GeForce GTX 16 Series (Turing w/o RTX) ---
            {'name': 'NVIDIA GeForce GTX 1660 Ti', 'power_draw': 120, 'peak_power': 150, 'recommended_psu': 450, 'price': 17000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1660 Super', 'power_draw': 125, 'peak_power': 160, 'recommended_psu': 450, 'price': 16000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1660', 'power_draw': 120, 'peak_power': 150, 'recommended_psu': 450, 'price': 14000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1650 Super', 'power_draw': 100, 'peak_power': 130, 'recommended_psu': 450, 'price': 12000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1650 G6', 'power_draw': 75, 'peak_power': 100, 'recommended_psu': 400, 'price': 11000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1650 (GDDR5)', 'power_draw': 75, 'peak_power': 100, 'recommended_psu': 400, 'price': 10000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1630', 'power_draw': 75, 'peak_power': 95, 'recommended_psu': 400, 'price': 8000, 'form_factor': 'PCI Express x16 (x8)'},

            # --- NVIDIA GeForce GTX 10 Series (Pascal) ---
            {'name': 'NVIDIA GeForce GTX 1080 Ti', 'power_draw': 250, 'peak_power': 320, 'recommended_psu': 600, 'price': 20000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1080', 'power_draw': 180, 'peak_power': 230, 'recommended_psu': 500, 'price': 15000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1070 Ti', 'power_draw': 180, 'peak_power': 230, 'recommended_psu': 500, 'price': 13000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1070', 'power_draw': 150, 'peak_power': 195, 'recommended_psu': 500, 'price': 11000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1060 6GB', 'power_draw': 120, 'peak_power': 155, 'recommended_psu': 400, 'price': 9000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1060 5GB', 'power_draw': 120, 'peak_power': 155, 'recommended_psu': 400, 'price': 8000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1060 3GB', 'power_draw': 120, 'peak_power': 155, 'recommended_psu': 400, 'price': 7000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1050 Ti', 'power_draw': 75, 'peak_power': 95, 'recommended_psu': 300, 'price': 6000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GTX 1050', 'power_draw': 75, 'peak_power': 95, 'recommended_psu': 300, 'price': 4500, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'NVIDIA GeForce GT 1030 (GDDR5)', 'power_draw': 30, 'peak_power': 40, 'recommended_psu': 300, 'price': 6500, 'form_factor': 'PCI Express x16 (x4)'},
            {'name': 'NVIDIA GeForce GT 1030 (DDR4)', 'power_draw': 20, 'peak_power': 30, 'recommended_psu': 300, 'price': 5000, 'form_factor': 'PCI Express x16 (x4)'},

            # --- AMD Radeon RX 9000 Series (RDNA 4, ожидаемые) ---
            {'name': 'AMD Radeon RX 9070 XT', 'power_draw': 300, 'peak_power': 380, 'recommended_psu': 750, 'price': 75000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 9070', 'power_draw': 250, 'peak_power': 320, 'recommended_psu': 700, 'price': 65000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 9060 XT', 'power_draw': 200, 'peak_power': 260, 'recommended_psu': 600, 'price': 45000, 'form_factor': 'PCI Express x16 (x8)'},
            {'name': 'AMD Radeon RX 9060', 'power_draw': 170, 'peak_power': 220, 'recommended_psu': 550, 'price': 35000, 'form_factor': 'PCI Express x16 (x8)'},

            # --- AMD Radeon RX 7000 Series (RDNA 3) ---
            {'name': 'AMD Radeon RX 7900 XTX', 'power_draw': 355, 'peak_power': 480, 'recommended_psu': 800, 'price': 115000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 7900 XT', 'power_draw': 315, 'peak_power': 420, 'recommended_psu': 750, 'price': 85000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 7900 GRE', 'power_draw': 260, 'peak_power': 340, 'recommended_psu': 700, 'price': 65000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 7800 XT', 'power_draw': 263, 'peak_power': 350, 'recommended_psu': 700, 'price': 55000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 7700 XT', 'power_draw': 245, 'peak_power': 320, 'recommended_psu': 700, 'price': 48000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 7600 XT', 'power_draw': 190, 'peak_power': 250, 'recommended_psu': 600, 'price': 38000, 'form_factor': 'PCI Express x16 (x8)'},
            {'name': 'AMD Radeon RX 7600', 'power_draw': 165, 'peak_power': 220, 'recommended_psu': 550, 'price': 30000, 'form_factor': 'PCI Express x16 (x8)'},

            # --- AMD Radeon RX 6000 Series (RDNA 2) ---
            {'name': 'AMD Radeon RX 6950 XT', 'power_draw': 335, 'peak_power': 450, 'recommended_psu': 850, 'price': 65000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 6900 XT', 'power_draw': 300, 'peak_power': 390, 'recommended_psu': 850, 'price': 55000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 6800 XT', 'power_draw': 300, 'peak_power': 390, 'recommended_psu': 850, 'price': 45000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 6800', 'power_draw': 250, 'peak_power': 330, 'recommended_psu': 650, 'price': 40000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 6750 XT', 'power_draw': 250, 'peak_power': 330, 'recommended_psu': 650, 'price': 38000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 6700 XT', 'power_draw': 230, 'peak_power': 300, 'recommended_psu': 650, 'price': 32000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 6700', 'power_draw': 175, 'peak_power': 230, 'recommended_psu': 550, 'price': 28000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 6650 XT', 'power_draw': 180, 'peak_power': 240, 'recommended_psu': 500, 'price': 26000, 'form_factor': 'PCI Express x16 (x8)'},
            {'name': 'AMD Radeon RX 6600 XT', 'power_draw': 160, 'peak_power': 210, 'recommended_psu': 500, 'price': 23000, 'form_factor': 'PCI Express x16 (x8)'},
            {'name': 'AMD Radeon RX 6600', 'power_draw': 132, 'peak_power': 175, 'recommended_psu': 450, 'price': 20000, 'form_factor': 'PCI Express x16 (x8)'},
            {'name': 'AMD Radeon RX 6500 XT', 'power_draw': 107, 'peak_power': 140, 'recommended_psu': 400, 'price': 15000, 'form_factor': 'PCI Express x16 (x4)'},
            {'name': 'AMD Radeon RX 6400', 'power_draw': 53, 'peak_power': 70, 'recommended_psu': 350, 'price': 12000, 'form_factor': 'PCI Express x16 (x4)'},

            # --- AMD Radeon RX 5000 Series (RDNA 1) ---
            {'name': 'AMD Radeon RX 5700 XT', 'power_draw': 225, 'peak_power': 290, 'recommended_psu': 600, 'price': 18000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 5700', 'power_draw': 180, 'peak_power': 235, 'recommended_psu': 600, 'price': 16000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 5600 XT', 'power_draw': 150, 'peak_power': 195, 'recommended_psu': 450, 'price': 14000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 5500 XT 8GB', 'power_draw': 130, 'peak_power': 170, 'recommended_psu': 450, 'price': 11000, 'form_factor': 'PCI Express x16 (x8)'},
            {'name': 'AMD Radeon RX 5500 XT 4GB', 'power_draw': 130, 'peak_power': 170, 'recommended_psu': 450, 'price': 9000, 'form_factor': 'PCI Express x16 (x8)'},

            # --- AMD Radeon RX Vega Series ---
            {'name': 'AMD Radeon RX Vega 64', 'power_draw': 295, 'peak_power': 380, 'recommended_psu': 750, 'price': 15000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX Vega 56', 'power_draw': 210, 'peak_power': 270, 'recommended_psu': 650, 'price': 12000, 'form_factor': 'PCI Express x16 (x16)'},

            # --- AMD Radeon RX 500 Series (Polaris Refresh) ---
            {'name': 'AMD Radeon RX 590', 'power_draw': 225, 'peak_power': 290, 'recommended_psu': 500, 'price': 10000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 580 8GB', 'power_draw': 185, 'peak_power': 240, 'recommended_psu': 500, 'price': 8000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 580 4GB', 'power_draw': 185, 'peak_power': 240, 'recommended_psu': 500, 'price': 6500, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 570 8GB', 'power_draw': 150, 'peak_power': 195, 'recommended_psu': 450, 'price': 7000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 570 4GB', 'power_draw': 150, 'peak_power': 195, 'recommended_psu': 450, 'price': 5500, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 560', 'power_draw': 75, 'peak_power': 100, 'recommended_psu': 400, 'price': 4500, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 550', 'power_draw': 50, 'peak_power': 70, 'recommended_psu': 400, 'price': 4000, 'form_factor': 'PCI Express x16 (x8)'},

            # --- AMD Radeon RX 400 Series (Polaris Original) ---
            {'name': 'AMD Radeon RX 480 8GB', 'power_draw': 150, 'peak_power': 195, 'recommended_psu': 500, 'price': 7000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 470', 'power_draw': 120, 'peak_power': 160, 'recommended_psu': 450, 'price': 5000, 'form_factor': 'PCI Express x16 (x16)'},
            {'name': 'AMD Radeon RX 460', 'power_draw': 75, 'peak_power': 100, 'recommended_psu': 400, 'price': 3500, 'form_factor': 'PCI Express x16 (x8)'},
        ]


        # Память
        memories = [
            # --- DDR5 ---
            
            # G.Skill (Топ производительность)
            {'name': 'G.Skill Trident Z5 RGB 64GB (2x32GB) DDR5-6400', 'power_draw': 12, 'peak_power': 15, 'price': 32000, 'form_factor': 'DIMM DDR5'},
            {'name': 'G.Skill Trident Z5 RGB 32GB (2x16GB) DDR5-6000', 'power_draw': 10, 'peak_power': 12, 'price': 18000, 'form_factor': 'DIMM DDR5'},
            {'name': 'G.Skill Ripjaws S5 32GB (2x16GB) DDR5-5600', 'power_draw': 8, 'peak_power': 10, 'price': 14000, 'form_factor': 'DIMM DDR5'},

            # Kingston (Народный выбор)
            {'name': 'Kingston FURY Beast RGB 64GB (2x32GB) DDR5-6000', 'power_draw': 12, 'peak_power': 15, 'price': 28000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Kingston FURY Beast 32GB (2x16GB) DDR5-6000', 'power_draw': 10, 'peak_power': 12, 'price': 16000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Kingston FURY Beast 32GB (2x16GB) DDR5-5200', 'power_draw': 8, 'peak_power': 10, 'price': 13000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Kingston FURY Renegade 32GB (2x16GB) DDR5-7200', 'power_draw': 14, 'peak_power': 17, 'price': 22000, 'form_factor': 'DIMM DDR5'},

            # ADATA / XPG
            {'name': 'XPG Lancer Blade RGB 32GB (2x16GB) DDR5-6000', 'power_draw': 10, 'peak_power': 12, 'price': 15500, 'form_factor': 'DIMM DDR5'},
            {'name': 'XPG Lancer 32GB (2x16GB) DDR5-5200', 'power_draw': 8, 'peak_power': 10, 'price': 12500, 'form_factor': 'DIMM DDR5'},
            {'name': 'ADATA XPG Caster RGB 32GB (2x16GB) DDR5-6400', 'power_draw': 12, 'peak_power': 15, 'price': 19000, 'form_factor': 'DIMM DDR5'},

            # Team Group (Стиль и разгон)
            {'name': 'Team Group T-Force Delta RGB 32GB (2x16GB) DDR5-6000', 'power_draw': 11, 'peak_power': 13, 'price': 16500, 'form_factor': 'DIMM DDR5'},
            {'name': 'Team Group T-Force Vulcan 32GB (2x16GB) DDR5-5600', 'power_draw': 9, 'peak_power': 11, 'price': 13500, 'form_factor': 'DIMM DDR5'},
            {'name': 'Team Group T-Create Expert 64GB (2x32GB) DDR5-6000', 'power_draw': 12, 'peak_power': 15, 'price': 27000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Team Group T-Force XTREEM ARGB 32GB (2x16GB) DDR5-7200', 'power_draw': 14, 'peak_power': 17, 'price': 25000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Team Group T-Create Classic 64GB (2x32GB) DDR5-5600', 'power_draw': 12, 'peak_power': 15, 'price': 23000, 'form_factor': 'DIMM DDR5'},

            # Patriot
            {'name': 'Patriot Viper Venom 32GB (2x16GB) DDR5-6200', 'power_draw': 11, 'peak_power': 13, 'price': 15000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Patriot Signature Line 16GB (2x8GB) DDR5-4800', 'power_draw': 6, 'peak_power': 8, 'price': 7000, 'form_factor': 'DIMM DDR5'},

            # Corsair
            {'name': 'Corsair Dominator Platinum RGB 32GB (2x16GB) DDR5-6200', 'power_draw': 12, 'peak_power': 15, 'price': 24000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Corsair Vengeance RGB 32GB (2x16GB) DDR5-6000', 'power_draw': 10, 'peak_power': 12, 'price': 17000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Corsair Vengeance 32GB (2x16GB) DDR5-5600', 'power_draw': 9, 'peak_power': 11, 'price': 14500, 'form_factor': 'DIMM DDR5'},
            {'name': 'Corsair Vengeance LPX 32GB (2x16GB) DDR5-5200', 'power_draw': 9, 'peak_power': 11, 'price': 13500, 'form_factor': 'DIMM DDR5'},

            # Netac (Бюджетный сегмент)
            {'name': 'Netac Shadow II DDR5 32GB (2x16GB) 6000MHz', 'power_draw': 10, 'peak_power': 12, 'price': 11000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Netac Basic DDR5 16GB (2x8GB) 4800MHz', 'power_draw': 6, 'peak_power': 8, 'price': 6000, 'form_factor': 'DIMM DDR5'},

            # G.Skill (Low Latency / AMD EXPO)
            {'name': 'G.Skill Flare X5 32GB (2x16GB) DDR5-6000 CL30', 'power_draw': 10, 'peak_power': 12, 'price': 17500, 'form_factor': 'DIMM DDR5'},
            {'name': 'G.Skill Trident Z5 Royal 32GB (2x16GB) DDR5-6400', 'power_draw': 12, 'peak_power': 15, 'price': 28000, 'form_factor': 'DIMM DDR5'},

            # Silicon Power
            {'name': 'Silicon Power XPOWER Zenith 32GB (2x16GB) DDR5-5600', 'power_draw': 10, 'peak_power': 12, 'price': 12000, 'form_factor': 'DIMM DDR5'},

            # Crucial
            {'name': 'Crucial Pro Overclocking 32GB (2x16GB) DDR5-6000', 'power_draw': 10, 'peak_power': 12, 'price': 14000, 'form_factor': 'DIMM DDR5'},

            # Samsung (OEM / Оригинал)
            {'name': 'Samsung Original 32GB (2x16GB) DDR5-4800', 'power_draw': 6, 'peak_power': 8, 'price': 12000, 'form_factor': 'DIMM DDR5'},
            {'name': 'Samsung Original 16GB (2x8GB) DDR5-5600', 'power_draw': 6, 'peak_power': 8, 'price': 7500, 'form_factor': 'DIMM DDR5'},

            # Server / ECC
            {'name': 'Kingston Server Premier 32GB DDR5-4800 ECC Reg', 'power_draw': 7, 'peak_power': 9, 'price': 18000, 'form_factor': 'RDIMM DDR5'},

            # --- DDR4 ---

            # G.Skill
            {'name': 'G.Skill Trident Z RGB 32GB (2x16GB) DDR4-3600', 'power_draw': 8, 'peak_power': 10, 'price': 11000, 'form_factor': 'DIMM DDR4'},
            {'name': 'G.Skill Ripjaws V 16GB (2x8GB) DDR4-3200', 'power_draw': 6, 'peak_power': 7, 'price': 4500, 'form_factor': 'DIMM DDR4'},
            {'name': 'G.Skill Aegis 16GB (2x8GB) DDR4-3000', 'power_draw': 6, 'peak_power': 7, 'price': 3800, 'form_factor': 'DIMM DDR4'},
            {'name': 'G.Skill Trident Z Royal 16GB (2x8GB) DDR4-3600', 'power_draw': 7, 'peak_power': 9, 'price': 13000, 'form_factor': 'DIMM DDR4'},

            # Kingston
            {'name': 'Kingston FURY Beast RGB 16GB (2x8GB) DDR4-3200', 'power_draw': 7, 'peak_power': 8, 'price': 5500, 'form_factor': 'DIMM DDR4'},
            {'name': 'Kingston FURY Beast 32GB (2x16GB) DDR4-3200', 'power_draw': 8, 'peak_power': 10, 'price': 9000, 'form_factor': 'DIMM DDR4'},
            {'name': 'Kingston FURY Renegade 16GB (2x8GB) DDR4-3600', 'power_draw': 7, 'peak_power': 9, 'price': 6000, 'form_factor': 'DIMM DDR4'},
            {'name': 'Kingston FURY Impact 32GB (2x16GB) DDR4-3200 SODIMM', 'power_draw': 5, 'peak_power': 6, 'price': 9000, 'form_factor': 'SODIMM DDR4'},
            {'name': 'Kingston FURY Impact 16GB (2x8GB) DDR4-2666 SODIMM', 'power_draw': 4, 'peak_power': 5, 'price': 5000, 'form_factor': 'SODIMM DDR4'},

            # ADATA / XPG
            {'name': 'XPG Spectrix D41 RGB 16GB (2x8GB) DDR4-3200', 'power_draw': 7, 'peak_power': 8, 'price': 5000, 'form_factor': 'DIMM DDR4'},
            {'name': 'XPG Gammix D10 16GB (2x8GB) DDR4-3200', 'power_draw': 6, 'peak_power': 7, 'price': 4200, 'form_factor': 'DIMM DDR4'},
            {'name': 'ADATA Premier 16GB (2x8GB) DDR4-2666', 'power_draw': 5, 'peak_power': 6, 'price': 3500, 'form_factor': 'DIMM DDR4'},
            {'name': 'ADATA XPG Spectrix D50 RGB 16GB (2x8GB) DDR4-3600', 'power_draw': 7, 'peak_power': 9, 'price': 6000, 'form_factor': 'DIMM DDR4'},

            # Patriot
            {'name': 'Patriot Viper Steel 16GB (2x8GB) DDR4-3600', 'power_draw': 7, 'peak_power': 8, 'price': 4800, 'form_factor': 'DIMM DDR4'},
            {'name': 'Patriot Viper Elite II 16GB (2x8GB) DDR4-2666', 'power_draw': 5, 'peak_power': 6, 'price': 3600, 'form_factor': 'DIMM DDR4'},
            {'name': 'Patriot Viper Steel RGB 16GB (2x8GB) DDR4-3600', 'power_draw': 7, 'peak_power': 9, 'price': 5200, 'form_factor': 'DIMM DDR4'},

            # Netac
            {'name': 'Netac Shadow II DDR4 16GB (2x8GB) 3200MHz', 'power_draw': 6, 'peak_power': 7, 'price': 3900, 'form_factor': 'DIMM DDR4'},
            {'name': 'Netac Basic DDR4 16GB (2x8GB) 2666MHz', 'power_draw': 5, 'peak_power': 6, 'price': 3200, 'form_factor': 'DIMM DDR4'},

            # Crucial
            {'name': 'Crucial Pro 32GB (2x16GB) DDR4-3200', 'power_draw': 7, 'peak_power': 9, 'price': 8500, 'form_factor': 'DIMM DDR4'},
            {'name': 'Crucial Ballistix 16GB (2x8GB) DDR4-3200', 'power_draw': 7, 'peak_power': 8, 'price': 5500, 'form_factor': 'DIMM DDR4'},

            # Team Group
            {'name': 'Team Group T-Force XTREEM ARGB 16GB (2x8GB) DDR4-3600 CL14', 'power_draw': 8, 'peak_power': 10, 'price': 12000, 'form_factor': 'DIMM DDR4'},
            {'name': 'Team Group T-Force Dark Za 32GB (2x16GB) DDR4-3600', 'power_draw': 8, 'peak_power': 10, 'price': 8500, 'form_factor': 'DIMM DDR4'},

            # Corsair
            {'name': 'Corsair Vengeance LPX 32GB (2x16GB) DDR4-3600', 'power_draw': 7, 'peak_power': 9, 'price': 9500, 'form_factor': 'DIMM DDR4'},

            # Samsung
            {'name': 'Samsung Original 16GB (2x8GB) DDR4-3200', 'power_draw': 5, 'peak_power': 6, 'price': 4000, 'form_factor': 'DIMM DDR4'},
            {'name': 'Samsung 32GB DDR4-3200 ECC Reg', 'power_draw': 6, 'peak_power': 8, 'price': 10000, 'form_factor': 'RDIMM DDR4'},
        ]


        # Накопители
        storages = [
            # === NVMe M.2 PCIe Gen5 (Самые быстрые, новейшие) ===
            {'name': 'Samsung 990 EVO Plus 1TB', 'power_draw': 6, 'peak_power': 8, 'price': 11000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Samsung 990 EVO Plus 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 19000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Samsung 9100 Pro 1TB', 'power_draw': 8, 'peak_power': 11, 'price': 22000, 'form_factor': 'M.2 NVMe PCIe 5.0'},
            {'name': 'Samsung 9100 Pro 2TB', 'power_draw': 9, 'peak_power': 12, 'price': 38000, 'form_factor': 'M.2 NVMe PCIe 5.0'},
            {'name': 'Samsung 9100 Pro 4TB', 'power_draw': 10, 'peak_power': 14, 'price': 68000, 'form_factor': 'M.2 NVMe PCIe 5.0'},
            {'name': 'Lexar NM1090 Pro 2TB', 'power_draw': 10, 'peak_power': 13, 'price': 33000, 'form_factor': 'M.2 NVMe PCIe 5.0'},
            {'name': 'Corsair MP700 PRO 1TB', 'power_draw': 10, 'peak_power': 13, 'price': 20000, 'form_factor': 'M.2 NVMe PCIe 5.0'},
            {'name': 'Corsair MP700 PRO 2TB', 'power_draw': 11, 'peak_power': 14, 'price': 35000, 'form_factor': 'M.2 NVMe PCIe 5.0'},

            # === NVMe M.2 PCIe Gen4 (Флагманы) ===
            {'name': 'Samsung 990 PRO 1TB', 'power_draw': 6, 'peak_power': 8, 'price': 13000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Samsung 990 PRO 2TB', 'power_draw': 7, 'peak_power': 9, 'price': 22000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Samsung 990 PRO 4TB', 'power_draw': 7, 'peak_power': 10, 'price': 42000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'WD Black SN850X 1TB', 'power_draw': 7, 'peak_power': 9, 'price': 12000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'WD Black SN850X 2TB', 'power_draw': 7, 'peak_power': 10, 'price': 20000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'WD Black SN850X 4TB', 'power_draw': 8, 'peak_power': 11, 'price': 38000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Solidigm P44 Pro 512GB', 'power_draw': 5, 'peak_power': 7, 'price': 8000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Solidigm P44 Pro 1TB', 'power_draw': 6, 'peak_power': 8, 'price': 14000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Solidigm P44 Pro 2TB', 'power_draw': 7, 'peak_power': 9, 'price': 26000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Seagate FireCuda 530 1TB', 'power_draw': 7, 'peak_power': 9, 'price': 13000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Seagate FireCuda 530 2TB', 'power_draw': 7, 'peak_power': 10, 'price': 22000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Seagate FireCuda 530 4TB', 'power_draw': 8, 'peak_power': 11, 'price': 42000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Corsair MP600 PRO XT 1TB', 'power_draw': 7, 'peak_power': 9, 'price': 11000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Corsair MP600 PRO XT 2TB', 'power_draw': 7, 'peak_power': 10, 'price': 19000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Corsair MP600 PRO XT 4TB', 'power_draw': 8, 'peak_power': 11, 'price': 36000, 'form_factor': 'M.2 NVMe PCIe 4.0'},

            # === NVMe M.2 PCIe Gen4 (Средний сегмент) ===
            {'name': 'Samsung 980 PRO 1TB', 'power_draw': 6, 'peak_power': 8, 'price': 10000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Samsung 980 PRO 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 17000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'ADATA Legend 960 1TB', 'power_draw': 5, 'peak_power': 7, 'price': 9000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'ADATA Legend 960 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 16000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'ADATA XPG Gammix S70 Blade 1TB', 'power_draw': 6, 'peak_power': 8, 'price': 9500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'ADATA XPG Gammix S70 Blade 2TB', 'power_draw': 7, 'peak_power': 9, 'price': 17000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Lexar NM790 1TB', 'power_draw': 5, 'peak_power': 7, 'price': 8500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Lexar NM790 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 15000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Lexar NM790 4TB', 'power_draw': 7, 'peak_power': 9, 'price': 28000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Kingston NV2 500GB', 'power_draw': 4, 'peak_power': 5, 'price': 4500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Kingston NV2 1TB', 'power_draw': 5, 'peak_power': 6, 'price': 7500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Kingston NV2 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 14000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Kingston KC3000 1TB', 'power_draw': 6, 'peak_power': 8, 'price': 10000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Kingston KC3000 2TB', 'power_draw': 7, 'peak_power': 9, 'price': 18000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Team Group MP44L 1TB', 'power_draw': 5, 'peak_power': 6, 'price': 7000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Team Group MP44L 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 13000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'MSI Spatium M450 500GB', 'power_draw': 4, 'peak_power': 5, 'price': 4800, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'MSI Spatium M450 1TB', 'power_draw': 5, 'peak_power': 6, 'price': 7500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'MSI Spatium M450 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 13500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'MSI Spatium M480 PRO 1TB', 'power_draw': 6, 'peak_power': 8, 'price': 10000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'MSI Spatium M480 PRO 2TB', 'power_draw': 7, 'peak_power': 9, 'price': 18000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Patriot Viper VP4300 1TB', 'power_draw': 6, 'peak_power': 8, 'price': 9000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Patriot Viper VP4300 2TB', 'power_draw': 7, 'peak_power': 9, 'price': 16000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Corsair MP600 Core XT 1TB', 'power_draw': 5, 'peak_power': 7, 'price': 7500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Corsair MP600 Core XT 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 13500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Corsair MP600 Core XT 4TB', 'power_draw': 7, 'peak_power': 9, 'price': 25000, 'form_factor': 'M.2 NVMe PCIe 4.0'},

            # === NVMe M.2 PCIe Gen4 (Бюджет) ===
            {'name': 'WD Blue SN580 500GB', 'power_draw': 4, 'peak_power': 5, 'price': 4500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'WD Blue SN580 1TB', 'power_draw': 5, 'peak_power': 6, 'price': 7000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'WD Blue SN580 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 13000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Crucial P3 Plus 500GB', 'power_draw': 4, 'peak_power': 5, 'price': 4200, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Crucial P3 Plus 1TB', 'power_draw': 5, 'peak_power': 6, 'price': 7200, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Crucial P3 Plus 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 13500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Crucial P3 Plus 4TB', 'power_draw': 7, 'peak_power': 9, 'price': 25000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Solidigm P41 Plus 512GB', 'power_draw': 4, 'peak_power': 5, 'price': 4000, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Solidigm P41 Plus 1TB', 'power_draw': 4, 'peak_power': 6, 'price': 6800, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Solidigm P41 Plus 2TB', 'power_draw': 5, 'peak_power': 7, 'price': 12500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Netac NV7000 1TB', 'power_draw': 5, 'peak_power': 6, 'price': 6500, 'form_factor': 'M.2 NVMe PCIe 4.0'},
            {'name': 'Netac NV7000 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 12000, 'form_factor': 'M.2 NVMe PCIe 4.0'},

            # === NVMe M.2 PCIe Gen3 (Старшее поколение, дешевле) ===
            {'name': 'Samsung 970 EVO Plus 500GB', 'power_draw': 5, 'peak_power': 6, 'price': 5500, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Samsung 970 EVO Plus 1TB', 'power_draw': 5, 'peak_power': 7, 'price': 9000, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Samsung 970 EVO Plus 2TB', 'power_draw': 6, 'peak_power': 8, 'price': 16000, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'WD Blue SN570 500GB', 'power_draw': 4, 'peak_power': 5, 'price': 4000, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'WD Blue SN570 1TB', 'power_draw': 5, 'peak_power': 6, 'price': 6500, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'WD Blue SN570 2TB', 'power_draw': 5, 'peak_power': 7, 'price': 12000, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Kingston NV1 500GB', 'power_draw': 4, 'peak_power': 5, 'price': 3500, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Kingston NV1 1TB', 'power_draw': 4, 'peak_power': 5, 'price': 6000, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Kingston NV1 2TB', 'power_draw': 5, 'peak_power': 6, 'price': 11000, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Lexar NM710 500GB', 'power_draw': 4, 'peak_power': 5, 'price': 3800, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Lexar NM710 1TB', 'power_draw': 5, 'peak_power': 6, 'price': 6500, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Crucial P2 500GB', 'power_draw': 4, 'peak_power': 5, 'price': 3500, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Crucial P2 1TB', 'power_draw': 5, 'peak_power': 6, 'price': 6200, 'form_factor': 'M.2 NVMe PCIe 3.0'},
            {'name': 'Crucial P2 2TB', 'power_draw': 5, 'peak_power': 7, 'price': 11500, 'form_factor': 'M.2 NVMe PCIe 3.0'},

            # === SATA SSD 2.5" (Универсальные, совместимы со старым железом) ===
            {'name': 'Samsung 870 EVO 500GB', 'power_draw': 3, 'peak_power': 4, 'price': 5500, 'form_factor': 'SATA 2.5"'},
            {'name': 'Samsung 870 EVO 1TB', 'power_draw': 3, 'peak_power': 4, 'price': 9000, 'form_factor': 'SATA 2.5"'},
            {'name': 'Samsung 870 EVO 2TB', 'power_draw': 3, 'peak_power': 4, 'price': 17000, 'form_factor': 'SATA 2.5"'},
            {'name': 'Samsung 870 EVO 4TB', 'power_draw': 4, 'peak_power': 5, 'price': 32000, 'form_factor': 'SATA 2.5"'},
            {'name': 'Crucial MX500 500GB', 'power_draw': 3, 'peak_power': 4, 'price': 4500, 'form_factor': 'SATA 2.5"'},
            {'name': 'Crucial MX500 1TB', 'power_draw': 3, 'peak_power': 4, 'price': 7500, 'form_factor': 'SATA 2.5"'},
            {'name': 'Crucial MX500 2TB', 'power_draw': 3, 'peak_power': 4, 'price': 14000, 'form_factor': 'SATA 2.5"'},
            {'name': 'Crucial MX500 4TB', 'power_draw': 4, 'peak_power': 5, 'price': 26000, 'form_factor': 'SATA 2.5"'},
            {'name': 'Kingston A400 480GB', 'power_draw': 2, 'peak_power': 3, 'price': 3800, 'form_factor': 'SATA 2.5"'},
            {'name': 'Kingston A400 960GB', 'power_draw': 3, 'peak_power': 4, 'price': 6500, 'form_factor': 'SATA 2.5"'},
            {'name': 'WD Blue 3D NAND 500GB', 'power_draw': 3, 'peak_power': 4, 'price': 4200, 'form_factor': 'SATA 2.5"'},
            {'name': 'WD Blue 3D NAND 1TB', 'power_draw': 3, 'peak_power': 4, 'price': 7000, 'form_factor': 'SATA 2.5"'},
            {'name': 'WD Blue 3D NAND 2TB', 'power_draw': 3, 'peak_power': 4, 'price': 13000, 'form_factor': 'SATA 2.5"'},
            {'name': 'ADATA SU650 480GB', 'power_draw': 2, 'peak_power': 3, 'price': 3500, 'form_factor': 'SATA 2.5"'},
            {'name': 'ADATA SU650 960GB', 'power_draw': 3, 'peak_power': 4, 'price': 6000, 'form_factor': 'SATA 2.5"'},
            {'name': 'Team Group GX2 512GB', 'power_draw': 3, 'peak_power': 4, 'price': 3600, 'form_factor': 'SATA 2.5"'},
            {'name': 'Team Group GX2 1TB', 'power_draw': 3, 'peak_power': 4, 'price': 6200, 'form_factor': 'SATA 2.5"'},
            {'name': 'Patriot Burst Elite 480GB', 'power_draw': 2, 'peak_power': 3, 'price': 3400, 'form_factor': 'SATA 2.5"'},
            {'name': 'Patriot Burst Elite 960GB', 'power_draw': 3, 'peak_power': 4, 'price': 5900, 'form_factor': 'SATA 2.5"'},
        ]

        # Блоки питания
        psus = [
            # --- 1000W - 1600W (High-End / Extreme) ---
            {'name': 'Corsair AX1600i 1600W', 'power_draw': 1600, 'price': 55000, 'form_factor': 'ATX 80+ Titanium'},
            {'name': 'Seasonic Prime TX-1600 1600W', 'power_draw': 1600, 'price': 60000, 'form_factor': 'ATX 80+ Titanium'},
            {'name': 'be quiet! Dark Power Pro 13 1600W', 'power_draw': 1600, 'price': 58000, 'form_factor': 'ATX 80+ Titanium'},
            {'name': 'ASUS ROG Thor 1600T Gaming', 'power_draw': 1600, 'price': 62000, 'form_factor': 'ATX 80+ Titanium'},
            {'name': 'Thermaltake Toughpower GF3 1650W', 'power_draw': 1650, 'price': 45000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Corsair HX1500i 1500W', 'power_draw': 1500, 'price': 42000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'Be Quiet! Straight Power 12 1500W', 'power_draw': 1500, 'price': 38000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'SilverStone HELA 1300R Platinum', 'power_draw': 1300, 'price': 35000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'MSI MEG Ai1300P PCIE5 1300W', 'power_draw': 1300, 'price': 40000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'Seasonic Vertex GX-1200 1200W', 'power_draw': 1200, 'price': 32000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Corsair RM1200x Shift 1200W', 'power_draw': 1200, 'price': 28000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'DeepCool PX1200G 1200W', 'power_draw': 1200, 'price': 24000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Montech Titan Gold 1200W', 'power_draw': 1200, 'price': 22000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'FSP Hydro PTM PRO 1200W', 'power_draw': 1200, 'price': 26000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'Thermaltake Toughpower GF3 1200W', 'power_draw': 1200, 'price': 25000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Corsair RM1000x 1000W', 'power_draw': 1000, 'price': 21000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Corsair RM1000e 1000W', 'power_draw': 1000, 'price': 19000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Seasonic Focus GX-1000 1000W', 'power_draw': 1000, 'price': 23000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'MSI MPG A1000G PCIE5 1000W', 'power_draw': 1000, 'price': 20000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'DeepCool PQ1000M 1000W', 'power_draw': 1000, 'price': 17000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'be quiet! Pure Power 12 M 1000W', 'power_draw': 1000, 'price': 19500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Chieftec Polaris Pro 1050W', 'power_draw': 1050, 'price': 16000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'XPG Cybercore 1000W', 'power_draw': 1000, 'price': 18000, 'form_factor': 'ATX 80+ Platinum'},

            # --- 900W - 950W (High-End) ---
            {'name': 'Corsair RM950x 950W', 'power_draw': 950, 'price': 19000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Corsair RM950e 950W', 'power_draw': 950, 'price': 17000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Seasonic Focus GX-950 950W', 'power_draw': 950, 'price': 20000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'MSI MPG A950G PCIE5 950W', 'power_draw': 950, 'price': 18000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'be quiet! Straight Power 11 Platinum 950W', 'power_draw': 950, 'price': 22000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'Thermaltake Toughpower GF1 950W', 'power_draw': 950, 'price': 16500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'DeepCool DQ950-M-V2L 950W', 'power_draw': 950, 'price': 15000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'ASUS TUF Gaming 950W', 'power_draw': 950, 'price': 17500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Gigabyte UD950GM 950W', 'power_draw': 950, 'price': 16000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Chieftec Polaris Pro 950W', 'power_draw': 950, 'price': 14000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'Cooler Master V950 Platinum', 'power_draw': 950, 'price': 21000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'XPG Core Reactor 950W', 'power_draw': 950, 'price': 18500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'FSP Hydro PTM PRO 950W', 'power_draw': 950, 'price': 19500, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'SilverStone HELA 900R Gold', 'power_draw': 900, 'price': 15000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Cougar GEX X3 950W', 'power_draw': 950, 'price': 14500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Montech Century 950W', 'power_draw': 950, 'price': 13500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Seasonic Prime PX-900 900W', 'power_draw': 900, 'price': 23000, 'form_factor': 'ATX 80+ Platinum'},
            {'name': 'Enermax Revolution D.F. X 900W', 'power_draw': 900, 'price': 16000, 'form_factor': 'ATX 80+ Gold'},

            # --- 750W - 850W (High-End / Mainstream) ---
            {'name': 'Corsair RM850x 850W', 'power_draw': 850, 'price': 16000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Corsair RM850e 850W', 'power_draw': 850, 'price': 14000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Seasonic Focus GX-850 850W', 'power_draw': 850, 'price': 17000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'MSI MPG A850G PCIE5 850W', 'power_draw': 850, 'price': 15500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'DeepCool DQ850-M-V2L 850W', 'power_draw': 850, 'price': 12000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'DeepCool PK850D 850W', 'power_draw': 850, 'price': 8000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Montech Century 850W', 'power_draw': 850, 'price': 11000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'be quiet! Pure Power 12 M 850W', 'power_draw': 850, 'price': 15000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Thermaltake Toughpower GF1 850W', 'power_draw': 850, 'price': 14000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Cougar GEX X2 850W', 'power_draw': 850, 'price': 12500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Chieftec Proton 850W', 'power_draw': 850, 'price': 9000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Gigabyte UD850GM 850W', 'power_draw': 850, 'price': 11500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Corsair RM750x 750W', 'power_draw': 750, 'price': 13000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Corsair RM750e 750W', 'power_draw': 750, 'price': 11500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Seasonic G12 GC-750 750W', 'power_draw': 750, 'price': 10000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'DeepCool PM750D 750W', 'power_draw': 750, 'price': 9000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'DeepCool PK750D 750W', 'power_draw': 750, 'price': 7000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'MSI MAG A750GL PCIE5 750W', 'power_draw': 750, 'price': 10500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'be quiet! System Power 10 750W', 'power_draw': 750, 'price': 8500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Cooler Master MWE Gold 750 V2', 'power_draw': 750, 'price': 11000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Chieftec Polaris 750W', 'power_draw': 750, 'price': 10000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'XPG Pylon 750W', 'power_draw': 750, 'price': 7500, 'form_factor': 'ATX 80+ Bronze'},

            # --- 600W - 700W (Mid-Range) ---
            {'name': 'Corsair CX750 750W', 'power_draw': 750, 'price': 8000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'FSP Hydro G PRO 750W', 'power_draw': 750, 'price': 13000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Seasonic B12 BC-750 750W', 'power_draw': 750, 'price': 8500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Be Quiet! Pure Power 11 700W', 'power_draw': 700, 'price': 9500, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'DeepCool PK700D 700W', 'power_draw': 700, 'price': 6500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Chieftec Proton 700W', 'power_draw': 700, 'price': 7000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'AeroCool KCAS PLUS 700W', 'power_draw': 700, 'price': 4500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Corsair RM650 650W', 'power_draw': 650, 'price': 10000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'MSI MAG A650BN 650W', 'power_draw': 650, 'price': 5500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'DeepCool PK650D 650W', 'power_draw': 650, 'price': 6000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'DeepCool PF650 650W', 'power_draw': 650, 'price': 4500, 'form_factor': 'ATX 80+'},
            {'name': 'Seasonic G12 GC-650 650W', 'power_draw': 650, 'price': 9000, 'form_factor': 'ATX 80+ Gold'},
            {'name': 'Cooler Master MWE Bronze 650 V2', 'power_draw': 650, 'price': 6500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'XPG Pylon 650W', 'power_draw': 650, 'price': 6500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'be quiet! System Power 10 650W', 'power_draw': 650, 'price': 7000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Chieftec Volt 650W', 'power_draw': 650, 'price': 4000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Cougar VTE 600W', 'power_draw': 600, 'price': 4200, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'DeepCool PF600 600W', 'power_draw': 600, 'price': 4000, 'form_factor': 'ATX 80+'},
            {'name': 'Zalman WattBit II 600W', 'power_draw': 600, 'price': 3500, 'form_factor': 'ATX'},

            # --- 450W - 550W (Budget / Entry-Level) ---
            {'name': 'DeepCool PK550D 550W', 'power_draw': 550, 'price': 5000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'MSI MAG A550BN 550W', 'power_draw': 550, 'price': 5000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Corsair CV550 550W', 'power_draw': 550, 'price': 5500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'be quiet! System Power 10 550W', 'power_draw': 550, 'price': 6000, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'FSP PNR PRO 500W', 'power_draw': 500, 'price': 3500, 'form_factor': 'ATX'},
            {'name': 'DeepCool PF550 550W', 'power_draw': 550, 'price': 3800, 'form_factor': 'ATX 80+'},
            {'name': 'Chieftec Value 500W', 'power_draw': 500, 'price': 3000, 'form_factor': 'ATX'},
            {'name': 'DeepCool PF500 500W', 'power_draw': 500, 'price': 3500, 'form_factor': 'ATX 80+'},
            {'name': 'Cooler Master MWE White 500W', 'power_draw': 500, 'price': 4000, 'form_factor': 'ATX 80+'},
            {'name': 'Aerocool VX PLUS 500W', 'power_draw': 500, 'price': 2500, 'form_factor': 'ATX'},
            {'name': 'Zalman WattBit II 500W', 'power_draw': 500, 'price': 3000, 'form_factor': 'ATX'},
            {'name': 'DeepCool DN500 500W', 'power_draw': 500, 'price': 4000, 'form_factor': 'ATX 80+'},
            {'name': 'XPG Pylon 550W', 'power_draw': 550, 'price': 5500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Seasonic S12III 500W', 'power_draw': 500, 'price': 6000, 'form_factor': 'ATX 80+ Bronze'},

            # --- 350W - 450W (Office / Low Power) ---
            {'name': 'DeepCool PF450 450W', 'power_draw': 450, 'price': 3200, 'form_factor': 'ATX 80+'},
            {'name': 'Corsair CV450 450W', 'power_draw': 450, 'price': 4500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'FSP PNR PRO 400W', 'power_draw': 400, 'price': 2800, 'form_factor': 'ATX'},
            {'name': 'DeepCool PF400 400W', 'power_draw': 400, 'price': 2900, 'form_factor': 'ATX 80+'},
            {'name': 'be quiet! System Power 9 400W', 'power_draw': 400, 'price': 4500, 'form_factor': 'ATX 80+ Bronze'},
            {'name': 'Aerocool VX PLUS 400W', 'power_draw': 400, 'price': 2000, 'form_factor': 'ATX'},
            {'name': 'Chieftec iArena 400W', 'power_draw': 400, 'price': 2500, 'form_factor': 'ATX'},
            {'name': 'DeepCool PF350 350W', 'power_draw': 350, 'price': 2500, 'form_factor': 'ATX 80+'},
            {'name': 'FSP PNR PRO 350W', 'power_draw': 350, 'price': 2200, 'form_factor': 'ATX'},
            {'name': 'Aerocool VX PLUS 350W', 'power_draw': 350, 'price': 1800, 'form_factor': 'ATX'},
        ]



        # Системы охлаждения
        coolers = [
            # === Воздушные кулеры (Top-Tier / Super Towers) ===
            {'name': 'Noctua NH-D15 G2', 'power_draw': 5, 'peak_power': 8, 'price': 13000, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'Noctua NH-D15 chromax.black', 'power_draw': 4, 'peak_power': 7, 'price': 11000, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'DeepCool Assassin IV', 'power_draw': 5, 'peak_power': 9, 'price': 9500, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'be quiet! Dark Rock Elite', 'power_draw': 5, 'peak_power': 8, 'price': 10500, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'be quiet! Dark Rock Pro 5', 'power_draw': 5, 'peak_power': 8, 'price': 9000, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'Thermalright Frost Commander 140', 'power_draw': 6, 'peak_power': 10, 'price': 5500, 'form_factor': 'Air Cooler (Dual Tower)'},

            # === Воздушные кулеры (Mid-Range / Best Value) ===
            {'name': 'DeepCool AK620 Digital', 'power_draw': 4, 'peak_power': 7, 'price': 7000, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'DeepCool AK620 Zero Dark', 'power_draw': 4, 'peak_power': 7, 'price': 6000, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'Thermalright Peerless Assassin 120 SE', 'power_draw': 4, 'peak_power': 7, 'price': 3500, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'Thermalright Phantom Spirit 120 SE', 'power_draw': 4, 'peak_power': 7, 'price': 4000, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'ID-Cooling SE-207-XT Black', 'power_draw': 5, 'peak_power': 8, 'price': 4500, 'form_factor': 'Air Cooler (Dual Tower)'},
            {'name': 'Jonsbo CR-3000 ARGB', 'power_draw': 5, 'peak_power': 8, 'price': 5000, 'form_factor': 'Air Cooler (Dual Tower)'},

            # === Воздушные кулеры (Single Tower / Budget) ===
            {'name': 'DeepCool AK500', 'power_draw': 3, 'peak_power': 5, 'price': 5000, 'form_factor': 'Air Cooler (Single Tower)'},
            {'name': 'DeepCool AK400', 'power_draw': 3, 'peak_power': 5, 'price': 3000, 'form_factor': 'Air Cooler (Single Tower)'},
            {'name': 'DeepCool AG400 BK ARGB', 'power_draw': 3, 'peak_power': 5, 'price': 2500, 'form_factor': 'Air Cooler (Single Tower)'},
            {'name': 'ID-Cooling SE-224-XTS Black', 'power_draw': 3, 'peak_power': 5, 'price': 2200, 'form_factor': 'Air Cooler (Single Tower)'},
            {'name': 'ID-Cooling SE-224-XTS ARGB', 'power_draw': 4, 'peak_power': 6, 'price': 2500, 'form_factor': 'Air Cooler (Single Tower)'},
            {'name': 'be quiet! Pure Rock 2 Black', 'power_draw': 3, 'peak_power': 5, 'price': 4500, 'form_factor': 'Air Cooler (Single Tower)'},
            {'name': 'Jonsbo CR-1000 EVO ARGB', 'power_draw': 3, 'peak_power': 5, 'price': 1800, 'form_factor': 'Air Cooler (Single Tower)'},
            {'name': 'PCCooler Paladin 400', 'power_draw': 3, 'peak_power': 5, 'price': 2300, 'form_factor': 'Air Cooler (Single Tower)'},

            # === СЖО 420mm (Extreme Performance) ===
            {'name': 'Arctic Liquid Freezer III 420', 'power_draw': 25, 'peak_power': 35, 'price': 15000, 'form_factor': 'Liquid AIO 420mm'},
            {'name': 'Arctic Liquid Freezer III 420 ARGB', 'power_draw': 28, 'peak_power': 38, 'price': 17000, 'form_factor': 'Liquid AIO 420mm'},
            {'name': 'Corsair iCUE H170i Elite LCD XT', 'power_draw': 30, 'peak_power': 40, 'price': 28000, 'form_factor': 'Liquid AIO 420mm'},
            {'name': 'Thermaltake TOUGHLIQUID 420 ARGB', 'power_draw': 25, 'peak_power': 35, 'price': 19000, 'form_factor': 'Liquid AIO 420mm'},

            # === СЖО 360mm (High-End / Popular) ===
            {'name': 'Arctic Liquid Freezer III 360', 'power_draw': 20, 'peak_power': 30, 'price': 12000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'DeepCool LS720', 'power_draw': 22, 'peak_power': 32, 'price': 11000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'DeepCool LT720', 'power_draw': 22, 'peak_power': 32, 'price': 12000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'DeepCool MYSTIQUE 360 LCD', 'power_draw': 25, 'peak_power': 35, 'price': 18000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'Lian Li Galahad II Trinity Performance 360', 'power_draw': 25, 'peak_power': 38, 'price': 19000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'Lian Li Galahad II LCD 360', 'power_draw': 28, 'peak_power': 40, 'price': 26000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'NZXT Kraken Elite 360 RGB', 'power_draw': 25, 'peak_power': 35, 'price': 29000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'Corsair iCUE H150i Elite Capellix XT', 'power_draw': 25, 'peak_power': 35, 'price': 22000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'ASUS ROG Ryujin III 360 ARGB', 'power_draw': 30, 'peak_power': 45, 'price': 35000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'MSI MAG CoreLiquid E360', 'power_draw': 20, 'peak_power': 30, 'price': 13000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'ID-Cooling DASHFLOW 360 XT', 'power_draw': 20, 'peak_power': 28, 'price': 8500, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'Cougar Poseidon GT 360', 'power_draw': 20, 'peak_power': 28, 'price': 9000, 'form_factor': 'Liquid AIO 360mm'},
            {'name': 'Team Group T-Force Siren GD360E', 'power_draw': 22, 'peak_power': 30, 'price': 10000, 'form_factor': 'Liquid AIO 360mm'},

            # === СЖО 280mm (Alternative to 360mm) ===
            {'name': 'Arctic Liquid Freezer III 280', 'power_draw': 18, 'peak_power': 25, 'price': 10000, 'form_factor': 'Liquid AIO 280mm'},
            {'name': 'NZXT Kraken 280', 'power_draw': 20, 'peak_power': 28, 'price': 16000, 'form_factor': 'Liquid AIO 280mm'},
            {'name': 'Be Quiet! Pure Loop 2 FX 280', 'power_draw': 18, 'peak_power': 25, 'price': 14000, 'form_factor': 'Liquid AIO 280mm'},
            {'name': 'Corsair H115i Elite Capellix', 'power_draw': 20, 'peak_power': 28, 'price': 17000, 'form_factor': 'Liquid AIO 280mm'},

            # === СЖО 240mm (Compact / Budget Liquid) ===
            {'name': 'DeepCool LS520', 'power_draw': 15, 'peak_power': 22, 'price': 8500, 'form_factor': 'Liquid AIO 240mm'},
            {'name': 'DeepCool LE520', 'power_draw': 15, 'peak_power': 20, 'price': 6500, 'form_factor': 'Liquid AIO 240mm'},
            {'name': 'Arctic Liquid Freezer III 240', 'power_draw': 15, 'peak_power': 22, 'price': 9000, 'form_factor': 'Liquid AIO 240mm'},
            {'name': 'ID-Cooling DASHFLOW 240 XT', 'power_draw': 15, 'peak_power': 20, 'price': 6000, 'form_factor': 'Liquid AIO 240mm'},
            {'name': 'ID-Cooling FROSTFLOW X 240', 'power_draw': 12, 'peak_power': 18, 'price': 4500, 'form_factor': 'Liquid AIO 240mm'},
            {'name': 'MSI MAG CoreLiquid C240', 'power_draw': 15, 'peak_power': 22, 'price': 9500, 'form_factor': 'Liquid AIO 240mm'},
            {'name': 'Cougar Poseidon Elite 240', 'power_draw': 15, 'peak_power': 20, 'price': 5500, 'form_factor': 'Liquid AIO 240mm'},
            {'name': 'Lian Li Galahad II Trinity 240', 'power_draw': 18, 'peak_power': 25, 'price': 13000, 'form_factor': 'Liquid AIO 240mm'},
        ]


        # Вставка данных
        all_components = [
            (categories['CPU'], processors),
            (categories['GPU'], gpus),
            (categories['RAM'], memories),
            (categories['SSD'], storages),
            (categories['PSU'], psus),
            (categories['COOLER'], coolers),
        ]

        count = 0
        for category, components_list in all_components:
            for comp_data in components_list:
                form_factor = comp_data.get('form_factor')
                
                component, created = Component.objects.get_or_create(
                    name=comp_data['name'],
                    category=category,
                    defaults={
                        'power_draw': comp_data['power_draw'],
                        'peak_power': comp_data.get('peak_power', 0),  # ✅ НОВОЕ
                        'recommended_psu': comp_data.get('recommended_psu', 0),  # ✅ НОВОЕ
                        'price': comp_data['price'],
                        'form_factor': form_factor,
                    }
                )
                if created:
                    count += 1

        self.stdout.write(
            self.style.SUCCESS(f'✓ Добавлено {count} новых компонентов')
        )