"""
---------------------------------KOMMENTLƏR------------------------------------------
təksətirli və çoxsətirli
"""

"""
----------------------------------DƏYİŞKƏNLƏR----------------------------------------

Dəyişkən adları:
    - Hərf və ya alt xətt ilə başlamalıdır.
    - Hərflər, rəqəmlər və alt xəttlərdən ibarət ola bilər (xüsusi simvol və ya boşluq yoxdur).
    - Böyük hərfə həssasdır (myVar və myvar fərqlidir).
    
Dəyişkənlərin təyini
    - Dəyişkənlər "=" operatorundan istifadə etməklə təyin edilir.
    - Daha sonra dəyişənin dəyərini dəyişə bilərsiniz.
    - Python eyni anda çoxlu təyinata imkan verir:
    
Dəyişkən adları
    - Dəyişkəndə saxlanan dəyəri əks etdirən mənalı adlar seçin.
    - Dəyişən adları üçün snake_case istifadə edin (məsələn, first_name, total_price).
    - if, else, while, for kimi açar sözlərdən istifadə etməyin.
"""

"""
Dəyişkən dəyərini yazdırmaq: print()
"""

CONSTANT = 100
BIR_GUNDE_SAAT = 24

"""
-----------------------------------SABİTLƏR-----------------------------------------
"""
int_var = -5
float_var = -0.528
f_var = -58.5
is_student = True

"""
----------------------------------DATA TİPLƏRİ--------------------------------------
Ümumi data tipləri: 
    - int (tam sayı)
    - float (onluq sayı)
    - str (sətir)
    - bool (boolean: doğru və yanlış)
    
    - list, tuple, dict, set (bunlar haqqında daha sonrakı dərslərdə)
"""

my_var = ""
my_str = str(my_var)
my_bool = bool(my_str)

print(my_bool)

"""
Sətir əməliyyatları:
    - Birləşdirmə: "+" operatorundan istifadə edərək sətirləri birləşdirin.
    - Təkrarlama: "*" operatorundan istifadə edərək sətri təkrarlayın.
    - İndeksləmə: İndeks mövqelərindən istifadə edərək müəyyən hərfləri əldə edin.
    - Dilimləmə: İndekslərdən istifadə edərək sub-sətir çıxarın.
    - Funksiya və metodlar:
        - len()
        - upper()
        - lower()
        - title()
        - capitalize()
        - count()
        - find()
        - replace()
        - split()
        daha ətraflı aşağıda
"""

"""
type() funksiyası
int()
float() və round()
str() və f-string
bool()
"""

"""
Tip çevirmədə əsas xətalar: ValueError, TypeError, IndexError
"""

"""
Riyazi operatorlar:
    - Toplama:      +   2 + 3   (=5)      
    - Çıxma:        -   5 - 3   (=2)
    - Vurma:        *   2 * 3   (=6)
    - Bölmə:        /   7 / 2   (=3.5)
    - Qalıq:        %   11 % 4  (=3)   
    - Üst:          **  2 ** 3  (=8)
    - Tam qismət:   //  14 // 3 (=4)
"""

"""
METOD / FUNKSIYA	    AÇIQLAMA
------------------------------------------------------------------------------------------
capitalize()	        İlk hərfi böyük hərfə çevirir
casefold()	            Sətiri kiçik hərflərə çevirir
center()	            Sətiri ortada yerləşdirir
count()	                Müəyyən bir dəyərin sətirdə neçə dəfə göründüyünü qaytarır
encode()	            Sətirin kodlaşdırılmış versiyasını qaytarır
endswith()	            Sətirin müəyyən bir dəyər ilə bitib-bitmədiyini yoxlayır
expandtabs()	        Sətirin tab boşluğunu təyin edir
find()	                Müəyyən bir dəyəri axtarır və ilk tapılan mövqeyi qaytarır
format()	            Müəyyən edilmiş dəyərləri sətirdə formatlaşdırır
format_map()	        Müəyyən edilmiş dəyərləri sətirdə formatlaşdırır
index()	                Müəyyən bir dəyəri axtarır və ilk tapılan mövqeyi qaytarır
isalnum()	            Sətirin bütün simvollarının hərf və ya rəqəm olub-olmadığını yoxlayır
isalpha()	            Sətirin bütün simvollarının yalnız hərf olub-olmadığını yoxlayır
isascii()	            Sətirin bütün simvollarının ASCII simvolları olub-olmadığını yoxlayır
isdecimal()	            Sətirin bütün simvollarının onluq rəqəmlər olub-olmadığını yoxlayır
isdigit()	            Sətirin bütün simvollarının rəqəm olub-olmadığını yoxlayır
isidentifier()	        Sətirin identifikator olub-olmadığını yoxlayır
islower()	            Sətirin bütün hərflərinin kiçik olub-olmadığını yoxlayır
isnumeric()	            Sətirin bütün simvollarının rəqəm olub-olmadığını yoxlayır
isprintable()	        Sətirin bütün simvollarının çap edilə bilər olub-olmadığını yoxlayır
isspace()	            Sətirin bütün simvollarının boşluq olub-olmadığını yoxlayır
istitle()	            Sətirin başlıq qaydalarına uyğun olub-olmadığını yoxlayır
isupper()	            Sətirin bütün hərflərinin böyük hərf olub-olmadığını yoxlayır
join()	                Təkrarlanan elementləri sətirə çevirir
ljust()	                Sətirin sola uyğunlaşdırılmış versiyasını qaytarır
lower()	                Sətiri kiçik hərflərə çevirir
lstrip()	            Sol tərəfdən boşluqları silir
maketrans()	            Tərcümə cədvəli qaytarır
partition()	            Sətiri üç hissəyə ayırıb tuple şəklində qaytarır
replace()	            Müəyyən edilmiş dəyəri başqası ilə əvəz edir
rfind()	                Müəyyən bir dəyəri axtarır və son tapılan mövqeyi qaytarır
rindex()	            Müəyyən bir dəyəri axtarır və son tapılan mövqeyi qaytarır
rjust()	                Sətirin sağa uyğunlaşdırılmış versiyasını qaytarır
rpartition()	        Sətiri üç hissəyə ayırıb tuple şəklində qaytarır
rsplit()	            Sətiri verilmiş separator üzrə bölür və siyahı qaytarır
rstrip()	            Sağ tərəfdən boşluqları silir
split()	                Sətiri verilmiş separator üzrə bölür və siyahı qaytarır
splitlines()	        Sətiri sətir qırılmalarına görə bölür və siyahı qaytarır
startswith()	        Sətirin müəyyən bir dəyər ilə başlayıb-başlamadığını yoxlayır
strip()	                Sətirdəki boşluqları silir
swapcase()	            Böyük hərfləri kiçik, kiçikləri isə böyük edir
title()	                Hər sözün ilk hərfini böyük edir
translate()	            Tərcümə edilmiş sətiri qaytarır
upper()	                Sətiri böyük hərflərə çevirir
zfill()	                Sətiri başlanğıcda sıfırlarla doldurur
"""
