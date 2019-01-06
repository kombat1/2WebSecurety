
# 2WebSecurety
Python Web Securety 

Как юзать мой софт 

# python3 2WebSecurety --Функция -параметр1 -параметр2

```
  ______        __   _    ____                           _         
 |___ \ \      / /__| |__/ ___|  ___  ___ _   _ _ __ ___| |_ _   _ 
   __) \ \ /\ / / _ \ '_ \___ \ / _ \/ __| | | | '__/ _ \ __| | | |
  / __/ \ V  V /  __/ |_) |__) |  __/ (__| |_| | | |  __/ |_| |_| |
 |_____| \_/\_/ \___|_.__/____/ \___|\___|\__,_|_|  \___|\__|\__, |
                                                             |___/ 
```
# python3 2WebSecurety --scan -u [сайт]

![screenshot of sample](https://ibb.co/mGqhSSG)

# python3 2WebSecurety --DetailScan -u [сайт] 
Так же есть возможность использовать свой скрипты для этого нужно указать флаг и текстовый файл -f xss.txt
![screenshot of sample](https://ibb.co/SwLTsFt)
# python3 2WebSecurety --ScanPort -u [сайт]
Это самый простой сканер портов,если у вас все порты закрыты обратите внимание на сайт у сайта не должно быть открыты каталоги ```python 2WebSecurety --ScanPort -u www.google.com ```
![screenshot of sample](https://ibb.co/dPhPPKb)

:white_check_mark: www.google.com

:negative_squared_cross_mark: www.google.com/image

# python3 2WebSecurety --PhpScan -f [Файл.php]
Данная функция сканирует файлы на ```Shell code``` или ```BakcDoor``` иначе говоря 
![screenshot of sample](https://ibb.co/z7VXCDX)

# python3 2WebSecurety.py --sn1per -u [url] --input1 [name] --input2 [name]
Функция ```sn1per``` Тут вы наводите на поля где по вашему мнению может находится уязвимость ```xss``` так же тут есть фозможность импортировать свой скрипты флагом -f [xss.txt] 
![screenshot of sample](https://ibb.co/XLdp5Ld)

# python3 2WebSecurety.py --generatehash -a [md5|sha256|sha512] -k [key]
Самый простой криптографическая утилита для хеширования ключа,также можно за хешировать текстовый файл -f [file.txt]
![screenshot of sample](https://ibb.co/TRxX1F5)
