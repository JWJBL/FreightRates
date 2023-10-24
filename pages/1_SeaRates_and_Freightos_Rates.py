import streamlit as st
import numpy as np
import requests
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.gridspec import GridSpec
import pandas as pd
from itertools import repeat

st.title('Freight Rates')

countries = ('Aba,NG',
'Abeokuta,NG',
'Abidjan,CI',
'Abobo,CI',
'Abu Dhabi,AE',
'Abu Ghurayb,IQ',
'Abuja,NG',
'Acapulco de Juarez,MX',
'Accra,GH',
'Adana,TR',
'Addis Ababa,ET',
'Adelaide,AU',
'Aden,YE',
'Agadir,MA',
'Agra,IN',
'Aguascalientes,MX',
'Ahmedabad,IN',
'Ahvaz,IR',
'Ajmer,IN',
'Aksu,CN',
'Al Ahmadi,KW',
'Al Ain City,AE',
'Al Basrah al Qadimah,IQ',
'Al Fayyum,EG',
'Al Hudaydah,YE',
'Al Mahallah al Kubra,EG',
'Al Mansurah,EG',
'Al Mawsil al Jadidah,IQ',
'Albuquerque,US',
'Aleppo,SY',
'Alexandria,EG',
'Algiers,DZ',
'Aligarh,IN',
'Almaty,KZ',
'Alvaro Obregon,MX',
'Amman,JO',
'Amravati,IN',
'Amritsar,IN',
'Amsterdam,NL',
'Ankang,CN',
'Ankara,TR',
'Anqing,CN',
'Ansan-si,KR',
'Anshan,CN',
'Anshun,CN',
'Antalya,TR',
'Antananarivo,MG',
'Antipolo,PH',
'Antwerpen,BE',
'Anyang,CN',
'Anyang-si,KR',
'Ar Raqqah,SY',
'Aracaju,BR',
'Arequipa,PE',
'As Sulaymaniyah,IQ',
'Ashgabat,TM',
'Asmara,ER',
'Astrakhan,RU',
'Asuncion,PY',
'Asyut,EG',
'Athens,GR',
'Austin,US',
'Azadshahr,IR',
'Bagcilar,TR',
'Baghdad,IQ',
'Bahawalpur,PK',
'Bahcelievler,TR',
'Baise,CN',
'Baku,AZ',
'Balikpapan,ID',
'Baltimore,US',
'Bamako,ML',
'Bandar Lampung,ID',
'Bandung,ID',
'Bangkok,TH',
'Bangui,CF',
'Banjarmasin,ID',
'Banqiao,TW',
'Baoding,CN',
'Baoji,CN',
'Baoshan,CN',
'Baotou,CN',
'Barcelona,ES',
'Barcelona,VE',
'Bareilly,IN',
'Barnaul,RU',
'Barquisimeto,VE',
'Barranquilla,CO',
'Basrah,IQ',
'Batam,ID',
'Battagram,PK',
'Bauchi,NG',
'Bayan Nur,CN',
'Beihai,CN',
'Beijing,CN',
'Beira,MZ',
'Beirut,LB',
'Bekasi,ID',
'Belem,BR',
'Belgrade,RS',
'Belo Horizonte,BR',
'Bengaluru,IN',
'Bengbu,CN',
'Benghazi,LY',
'Benin City,NG',
'Benoni,ZA',
'Benxi,CN',
'Berlin,DE',
'Bhavnagar,IN',
'Bhayandar,IN',
'Bhilai,IN',
'Bhiwandi,IN',
'Bhopal,IN',
'Bhubaneswar,IN',
'Bien Hoa,VN',
'Bijie,CN',
'Bikaner,IN',
'Binzhou,CN',
'Birmingham,GB',
'Bishkek,KG',
'Blantyre,MW',
'Bloemfontein,ZA',
'Bobo-Dioulasso,BF',
'Bogor,ID',
'Bogota,CO',
'Bokaro,IN',
'Borivli,IN',
'Boston,US',
'Bouake,CI',
'Boumerdas,DZ',
'Bozhou,CN',
'Brampton,CA',
'Brasilia,BR',
'Brazzaville,CG',
'Bremen,DE',
'Brisbane,AU',
'Brooklyn,US',
'Brussels,BE',
'Bucaramanga,CO',
'Bucharest,RO',
'Bucheon-si,KR',
'Budapest,HU',
'Budta,PH',
'Buenos Aires,AR',
'Bujumbura,BI',
'Bulawayo,ZW',
'Buraydah,SA',
'Bursa,TR',
'Busan,KR',
'Cairo,EG',
'Calamba,PH',
'Calgary,CA',
'Cali,CO',
'Callao,PE',
'Caloocan City,PH',
'Camayenne,GN',
'Campinas,BR',
'Campo Grande,BR',
'Can Tho,VN',
'Cancun,MX',
'Cangzhou,CN',
'Cankaya,TR',
'Cape Town,ZA',
'Caracas,VE',
'Cartagena,CO',
'Casablanca,MA',
'Cebu City,PH',
'Chandigarh,IN',
'Changchun,CN',
'Changde,CN',
'Changsha,CN',
'Changshu,CN',
'Changwon,KR',
'Changzhi,CN',
'Changzhi,CN',
'Changzhou,CN',
'Chaozhou,CN',
'Charlotte,US',
'Chattogram,BD',
'Chelyabinsk,RU',
'Chengdu,CN',
'Chennai,IN',
'Chenzhou,CN',
'Cheonan,KR',
'Cheongju-si,KR',
'Chiba,JP',
'Chicago,US',
'Chiclayo,PE',
'Chihuahua,MX',
'Chisinau,MD',
'Chizhou,CN',
'Chongqing,CN',
'Chuzhou,CN',
'Cimahi,ID',
'Ciudad Guayana,VE',
'Ciudad Juarez,MX',
'Ciudad Nezahualcoyotl,MX',
'Cixi,CN',
'Cochabamba,BO',
'Cochin,IN',
'Coimbatore,IN',
'Colombo,LK',
'Columbus,US',
'Comilla,BD',
'Conakry,GN',
'Contagem,BR',
'Copenhagen,DK',
'Cordoba,AR',
'Cotonou,BJ',
'Coyoacan,MX',
'Cuauhtemoc,MX',
'Cucuta,CO',
'Cuenca,EC',
'Cuiaba,BR',
'Culiacan,MX',
'Curitiba,BR',
'Cuttack,IN',
'Da Nang,VN',
'Daegu,KR',
'Daejeon,KR',
'Dakar,SN',
'Dalian,CN',
'Dallas,US',
'Damascus,SY',
'Dammam,SA',
'Dandong,CN',
'Daqing,CN',
'Dar es Salaam,TZ',
'Datong,CN',
'Davao,PH',
'Dazhou,CN',
'Dehra Dun,IN',
'Delhi,IN',
'Denpasar,ID',
'Denver,US',
'Depok,ID',
'Detroit,US',
'Deyang,CN',
'Dezhou,CN',
'Dhaka,BD',
'Dhanbad,IN',
'Diyarbakir,TR',
'Djibouti,DJ',
'Dnipro,UA',
'Dombivli,IN',
'Donetsk,UA',
'Dongguan,CN',
'Dongying,CN',
'Dortmund,DE',
'Douala,CM',
'Dresden,DE',
'Dubai,AE',
'Dublin,IE',
'Duesseldorf,DE',
'Duque de Caxias,BR',
'Durban,ZA',
'Durgapur,IN',
'Dushanbe,TJ',
'Ebute Ikorodu,NG',
'Ecatepec de Morelos,MX',
'Edmonton,CA',
'El Paso,US',
'Enugu,NG',
'Erbil,IQ',
'Erode,IN',
'Erzurum,TR',
'Esenler,TR',
'Eskisehir,TR',
'Essen,DE',
'E\'zhou,CN',
'Faisalabad,PK',
'Faridabad,IN',
'Feira de Santana,BR',
'Fes,MA',
'Fort Worth,US',
'Fortaleza,BR',
'Foshan,CN',
'Frankfurt am Main,DE',
'Freetown,SL',
'Fresno,US',
'Fukuoka,JP',
'Fushun,CN',
'Fuxin,CN',
'Fuyang,CN',
'Fuzhou,CN',
'Fuzhou,CN',
'Ganzhou,CN',
'Gaziantep,TR',
'General Santos,PH',
'Genoa,IT',
'Ghaziabad,IN',
'Giza,EG',
'Glasgow,GB',
'Goeteborg,SE',
'Goiania,BR',
'Gold Coast,AU',
'Gorakhpur,IN',
'Gorakhpur,IN',
'Goyang-si,KR',
'Grosszschocher,DE',
'Guadalajara,MX',
'Guadalupe,MX',
'Guang\'an,CN',
'Guangyuan,CN',
'Guangzhou,CN',
'Guankou,CN',
'Guarulhos,BR',
'Guatemala City,GT',
'Guayaquil,EC',
'Guigang,CN',
'Guilin,CN',
'Guiyang,CN',
'Gujranwala,PK',
'Guli,CN',
'Guntur,IN',
'Gustavo Adolfo Madero,MX',
'Guwahati,IN',
'Gwalior,IN',
'Gwangju,KR',
'Hachioji,JP',
'Haikou,CN',
'Ha\'il,SA',
'Haiphong,VN',
'Hamadan,IR',
'Hamamatsu,JP',
'Hamburg,DE',
'Hamhung,KP',
'Hamilton,CA',
'Handan,CN',
'Hangzhou,CN',
'Hannover,DE',
'Hanoi,VN',
'Hanzhong,CN',
'Haora,IN',
'Harare,ZW',
'Harbin,CN',
'Havana,CU',
'Hebi,CN',
'Hefei,CN',
'Hegang,CN',
'Helsinki,FI',
'Hengshui,CN',
'Hengyang,CN',
'Herat,AF',
'Hermosillo,MX',
'Heze,CN',
'Hezhou,CN',
'Himeji,JP',
'Hiroshima,JP',
'Ho Chi Minh City,VN',
'Hohhot,CN',
'Homs,SY',
'Homyel\',BY',
'Honcho,JP',
'Hong Kong,HK',
'Houston,US',
'Huai\'an,CN',
'Huaibei,CN',
'Huaihua,CN',
'Huainan,CN',
'Huangshi,CN',
'Hubli,IN',
'Huizhou,CN',
'Huzhou,CN',
'Hwaseong-si,KR',
'Hyderabad,IN',
'Hyderabad,PK',
'Ibadan,NG',
'Ibague,CO',
'Ilorin,NG',
'Incheon,KR',
'Indianapolis,US',
'Indore,IN',
'Ipoh,MY',
'Irbid,JO',
'Irkutsk,RU',
'Isfahan,IR',
'Islamabad,PK',
'Istanbul,TR',
'Izhevsk,RU',
'Izmir,TR',
'Iztapalapa,MX',
'Jabalpur,IN',
'Jaboatao dos Guararapes,BR',
'Jaboatao,BR',
'Jacksonville,US',
'Jaipur,IN',
'Jakarta,ID',
'Jalandhar,IN',
'Jambi City,ID',
'Jamshedpur,IN',
'Jeddah,SA',
'Jeonju,KR',
'Jepara,ID',
'Jerusalem,IL',
'Jiamusi,CN',
'Ji\'an,CN',
'Jiangmen,CN',
'Jiangyin,CN',
'Jiaozhou,CN',
'Jiaozuo,CN',
'Jiaxing,CN',
'Jieyang,CN',
'Jilin,CN',
'Jinan,CN',
'Jingmen,CN',
'Jingzhou,CN',
'Jinhua,CN',
'Jining,CN',
'Jinjiang,CN',
'Jinzhong,CN',
'Jinzhou,CN',
'Jiujiang,CN',
'Joao Pessoa,BR',
'Jodhpur,IN',
'Johannesburg,ZA',
'Johor Bahru,MY',
'Jos,NG',
'Juiz de Fora,BR',
'Kabul,AF',
'Kaduna,NG',
'Kagoshima,JP',
'Kahriz,IR',
'Kaifeng,CN',
'Kakamega,KE',
'Kallakurichi,IN',
'Kalyan,IN',
'Kampala,UG',
'Kampung Baru Subang,MY',
'Kanayannur,IN',
'Kandahar,AF',
'Kano,NG',
'Kanpur,IN',
'Kaohsiung,TW',
'Karachi,PK',
'Karaj,IR',
'Karbala,IQ',
'Kathmandu,NP',
'Kawaguchi,JP',
'Kawasaki,JP',
'Kayseri,TR',
'Kazan,RU',
'Kemerovo,RU',
'Kerman,IR',
'Kermanshah,IR',
'Khabarovsk Vtoroy,RU',
'Khabarovsk,RU',
'Kharkiv,UA',
'Khartoum,SD',
'Khulna,BD',
'Kigali,RW',
'Kimhae,KR',
'Kingston,JM',
'Kinshasa,CD',
'Kirkuk,IQ',
'Kisangani,CD',
'Kitakyushu,JP',
'Klang,MY',
'Kleinzschocher,DE',
'Kobe,JP',
'Koeln,DE',
'Kolhapur,IN',
'Kolkata,IN',
'Konya,TR',
'Korla,CN',
'Kota Bharu,MY',
'Kota,IN',
'Kotli,PK',
'Kowloon,HK',
'Kozhikode,IN',
'Krakow,PL',
'Krasnodar,RU',
'Krasnoyarsk,RU',
'Kryvyy Rih,UA',
'Kuala Lumpur,MY',
'Kuantan,MY',
'Kumamoto,JP',
'Kumasi,GH',
'Kunming,CN',
'Kunshan,CN',
'Kyiv,UA',
'Kyoto,JP',
'La Paz,BO',
'Lagos,NG',
'Lahore,PK',
'Laibin,CN',
'Laiwu,CN',
'Langfang,CN',
'Lanzhou,CN',
'Las Pinas,PH',
'Las Vegas,US',
'Latakia,SY',
'Leeds,GB',
'Leon de los Aldama,MX',
'Leshan,CN',
'Lianyungang,CN',
'Liaocheng,CN',
'Liaoyang,CN',
'Libreville,GA',
'Lilongwe,MW',
'Lima,PE',
'Linfen,CN',
'Linyi,CN',
'Lisbon,PT',
'Liupanshui,CN',
'Liuzhou,CN',
'Liverpool,GB',
'Lodz,PL',
'Lome,TG',
'London,GB',
'Londrina,BR',
'Longyan,CN',
'Los Angeles,US',
'Lu\'an,CN',
'Luancheng,CN',
'Luanda,AO',
'Lubumbashi,CD',
'Lucknow,IN',
'Ludhiana,IN',
'Luohe,CN',
'Luoyang,CN',
'Lusaka,ZM',
'Luzhou,CN',
'Lviv,UA',
'Lyon,FR',
'Ma\'anshan,CN',
'Macapa,BR',
'Macau,MO',
'Maceio,BR',
'Madinat an Nasr,EG',
'Madrid,ES',
'Madurai,IN',
'Maiduguri,NG',
'Makassar,ID',
'Makhachkala,RU',
'Malacca,MY',
'Malaga,ES',
'Malang,ID',
'Malatya,TR',
'Malingao,PH',
'Managua,NI',
'Manaus,BR',
'Mandalay,MM',
'Manhattan,US',
'Manila,PH',
'Maoming,CN',
'Maputo,MZ',
'Mar del Plata,AR',
'Maracaibo,VE',
'Maracay,VE',
'Marrakesh,MA',
'Marseille,FR',
'Mashhad,IR',
'Matola,MZ',
'Maturin,VE',
'Mazar-e Sharif,AF',
'Mbuji-Mayi,CD',
'Mecca,SA',
'Medan,ID',
'Medellin,CO',
'Medina,SA',
'Meerut,IN',
'Meishan,CN',
'Meizhou,CN',
'Meknes,MA',
'Melbourne,AU',
'Memphis,US',
'Merida,MX',
'Mersin,TR',
'Mexicali,MX',
'Mexico City,MX',
'Mianyang,CN',
'Milan,IT',
'Milwaukee,US',
'Minsk,BY',
'Mississauga,CA',
'Mogadishu,SO',
'Mombasa,KE',
'Monrovia,LR',
'Monterrey,MX',
'Montevideo,UY',
'Montreal,CA',
'Moradabad,IN',
'Morelia,MX',
'Moscow,RU',
'Mosul,IQ',
'Mudanjiang,CN',
'Mukalla,YE',
'Multan,PK',
'Mumbai,IN',
'Munich,DE',
'Muscat,OM',
'Muzaffarabad,PK',
'Mysore,IN',
'Nagoya,JP',
'Nagpur,IN',
'Nairobi,KE',
'Najafgarh,IN',
'Namangan,UZ',
'Nampula,MZ',
'Nanchang,CN',
'Nanchong,CN',
'Nanded,IN',
'Nanjing,CN',
'Nanning,CN',
'Nantong,CN',
'Nanyang,CN',
'Naples,IT',
'Narela,IN',
'Nashik,IN',
'Nashville,US',
'Nasiriyah,IQ',
'Natal,BR',
'Naucalpan de Juarez,MX',
'Navi Mumbai,IN',
'Nay Pyi Taw,MM',
'N\'Djamena,TD',
'Neijiang,CN',
'New Kingston,JM',
'New South Memphis,US',
'New York City,US',
'Niamey,NE',
'Niigata,JP',
'Ningbo,CN',
'Nizhniy Novgorod,RU',
'Nouakchott,MR',
'Nova Iguacu,BR',
'Novokuznetsk,RU',
'Novosibirsk,RU',
'Nowrangapur,IN',
'Nuernberg,DE',
'Nyala,SD',
'Odesa,UA',
'Okayama,JP',
'Oklahoma City,US',
'Omdurman,SD',
'Omsk,RU',
'Onitsha,NG',
'Oran,DZ',
'Ordos,CN',
'Orenburg,RU',
'Orumiyeh,IR',
'Osaka,JP',
'Osasco,BR',
'Oslo,NO',
'Ottawa,CA',
'Ouagadougou,BF',
'Oyo,NG',
'Padang,ID',
'Palembang,ID',
'Palermo,IT',
'Panshan,CN',
'Panzhihua,CN',
'Paranaque City,PH',
'Paris,FR',
'Pasig City,PH',
'Pasragad Branch,IR',
'Patna,IN',
'Pekanbaru,ID',
'Penza,RU',
'Perm,RU',
'Perth,AU',
'Peshawar,PK',
'Petaling Jaya,MY',
'Philadelphia,US',
'Phnom Penh,KH',
'Phoenix,US',
'Pietermaritzburg,ZA',
'Pikine,SN',
'Pimpri,IN',
'Pingdingshan,CN',
'Pingdu,CN',
'Pingxiang,CN',
'Pointe-Noire,CG',
'Pontianak,ID',
'Port Elizabeth,ZA',
'Port Harcourt,NG',
'Port Said,EG',
'Port-au-Prince,HT',
'Portland,US',
'Porto Alegre,BR',
'Porto Velho,BR',
'Poznan,PL',
'Prague,CZ',
'Prayagraj,IN',
'Pretoria,ZA',
'Pristina,XK',
'Puducherry,IN',
'Puebla,MX',
'Puente Alto,CL',
'Pune,IN',
'Puning,CN',
'Putian,CN',
'Puyang,CN',
'Puyang,CN',
'Pyongyang,KP',
'Qingdao,CN',
'Qingyuan,CN',
'Qinhuangdao,CN',
'Qinzhou,CN',
'Qionghai,CN',
'Qiqihar,CN',
'Qom,IR',
'Quanzhou,CN',
'Quebec,CA',
'Queens,US',
'Quetta,PK',
'Quezon City,PH',
'Quito,EC',
'Qujing,CN',
'Quzhou,CN',
'Rabat,MA',
'Rahim Yar Khan,PK',
'Raipur,IN',
'Rajkot,IN',
'Rajshahi,BD',
'Ranchi,IN',
'Rangpur,BD',
'Ra\'s Bayrut,LB',
'Rasht,IR',
'Raurkela,IN',
'Rawalpindi,PK',
'Recife,BR',
'Reynosa,MX',
'Ribeirao Preto,BR',
'Riga,LV',
'Rio de Janeiro,BR',
'Riyadh,SA',
'Rizhao,CN',
'Rohini,IN',
'Rome,IT',
'Rosario,AR',
'Rostov-na-Donu,RU',
'Rotterdam,NL',
'Rui\'an,CN',
'Ryazan\',RU',
'Saint Petersburg,RU',
'Saitama,JP',
'Sakai,JP',
'Sale,MA',
'Salem,IN',
'Salta,AR',
'Saltillo,MX',
'Salvador,BR',
'Samara,RU',
'Samarinda,ID',
'Samarkand,UZ',
'Sambhaji Nagar,IN',
'San Antonio,US',
'San Diego,US',
'San Francisco,US',
'San Jose,US',
'San Luis Potosi,MX',
'San Miguel de Tucuman,AR',
'San Pedro Sula,HN',
'San Salvador,SV',
'Sanaa,YE',
'Sangli,IN',
'Sanmenxia,CN',
'Sanming,CN',
'Santa Cruz de la Sierra,BO',
'Santa Maria Chimalhuacan,MX',
'Santiago de Cuba,CU',
'Santiago de los Caballeros,DO',
'Santiago de Queretaro,MX',
'Santiago,CL',
'Santo Andre,BR',
'Santo Domingo Este,DO',
'Santo Domingo Oeste,DO',
'Santo Domingo,DO',
'Sanya,CN',
'Sao Bernardo do Campo,BR',
'Sao Jose dos Campos,BR',
'Sao Luis,BR',
'Sao Paulo,BR',
'Sapporo,JP',
'Sarajevo,BA',
'Saratov,RU',
'Sargodha,PK',
'Seattle,US',
'Semarang,ID',
'Sendai,JP',
'Seongnam-si,KR',
'Seoul,KR',
'Serang,ID',
'Sevastopol,UA',
'Sevilla,ES',
'Shah Alam,MY',
'Shanghai,CN',
'Shangluo,CN',
'Shangqiu,CN',
'Shangrao,CN',
'Shangyu,CN',
'Shantou,CN',
'Shaoguan,CN',
'Shaoxing,CN',
'Shaoyang,CN',
'Sharjah,AE',
'Sheffield,GB',
'Shenyang,CN',
'Shenzhen,CN',
'Shihezi,CN',
'Shijiazhuang,CN',
'Shiraz,IR',
'Shivaji Nagar,IN',
'Shiyan,CN',
'Shizuoka,JP',
'Shuangyashan,CN',
'Shubra al Khaymah,EG',
'Shymkent,KZ',
'Siliguri,IN',
'Singapore,SG',
'Siping,CN',
'Situbondo,ID',
'Sofia,BG',
'Sokoto,NG',
'Solapur,IN',
'Sorocaba,BR',
'South Boston,US',
'South Tangerang,ID',
'Soweto,ZA',
'Srinagar,IN',
'Stockholm,SE',
'Stuttgart,DE',
'Subang Jaya,MY',
'Suez,EG',
'Suining,CN',
'Suizhou,CN',
'Sultanah,SA',
'Suqian,CN',
'Surabaya,ID',
'Surakarta,ID',
'Surat,IN',
'Suwon,KR',
'Suzhou,CN',
'Suzhou,CN',
'Sydney,AU',
'Tabriz,IR',
'Tabuk,SA',
'Taguig,PH',
'Tai\'an,CN',
'Taicang,CN',
'Taichung,TW',
'Ta\'if,SA',
'Tainan,TW',
'Taipei,TW',
'Taiyuan,CN',
'Taiz,YE',
'Taizhou,CN',
'Taizhou,CN',
'Takeo,KH',
'Tangerang,ID',
'Tanggu,CN',
'Tangier,MA',
'Tangshan,CN',
'Tanta,EG',
'Tashkent,UZ',
'Tbilisi,GE',
'Tebessa,DZ',
'Tegucigalpa,HN',
'Tehran,IR',
'Teni,IN',
'Teresina,BR',
'Thane,IN',
'The Bronx,US',
'Thiruvananthapuram,IN',
'Thuan An,VN',
'Tianjin,CN',
'Tianshui,CN',
'Tijuana,MX',
'Tiruchirappalli,IN',
'Tirunelveli,IN',
'Tiruppur,IN',
'Tlalnepantla,MX',
'Tlalpan,MX',
'Tlaquepaque,MX',
'Tokyo,JP',
'Tolyatti,RU',
'Tomsk,RU',
'Toronto,CA',
'Torreon,MX',
'Touba,SN',
'Tripoli,LY',
'Trujillo,PE',
'Tucson,US',
'Tunis,TN',
'Turin,IT',
'Tuxtla,MX',
'Tyumen,RU',
'Uberlandia,BR',
'UEruemqi,CN',
'UEskuedar,TR',
'Ufa,RU',
'Ulan Bator,MN',
'Ulhasnagar,IN',
'Ulsan,KR',
'Ulyanovsk,RU',
'Umraniye,TR',
'Vadodara,IN',
'Valencia,ES',
'Valencia,VE',
'Van,TR',
'Vancouver,CA',
'Varanasi,IN',
'Victoria de Durango,MX',
'Victoria,HK',
'Vienna,AT',
'Vijayawada,IN',
'Villa Nueva,GT',
'Vilnius,LT',
'Visakhapatnam,IN',
'Vladivostok,RU',
'Volgograd,RU',
'Voronezh,RU',
'Wanning,CN',
'Wanxian,CN',
'Wanzhou,CN',
'Warangal,IN',
'Warri,NG',
'Warsaw,PL',
'Washington,US',
'Weifang,CN',
'Weihai,CN',
'Weinan,CN',
'Wenchang,CN',
'Wenzhou,CN',
'Winnipeg,CA',
'Wroclaw,PL',
'Wuhan,CN',
'Wuhu,CN',
'Wuwei,CN',
'Wuxi,CN',
'Wuzhou,CN',
'Xiamen,CN',
'Xi\'an,CN',
'Xiangtan,CN',
'Xiangyang,CN',
'Xianyang,CN',
'Xiaogan,CN',
'Xingtai,CN',
'Xining,CN',
'Xinxiang,CN',
'Xinyang,CN',
'Xinyu,CN',
'Xinzhou,CN',
'Xuanzhou,CN',
'Xuchang,CN',
'Xuzhou,CN',
'Ya\'an,CN',
'Yancheng,CN',
'Yangjiang,CN',
'Yangon,MM',
'Yangquan,CN',
'Yangzhou,CN',
'Yantai,CN',
'Yaounde,CM',
'Yaroslavl,RU',
'Yekaterinburg,RU',
'Yerevan,AM',
'Yibin,CN',
'Yichang,CN',
'Yichun,CN',
'Yinchuan,CN',
'Yingkou,CN',
'Yiwu,CN',
'Yixing,CN',
'Yiyang,CN',
'Yokohama,JP',
'Yongzhou,CN',
'Yueyang,CN',
'Yulin,CN',
'Yuncheng,CN',
'Yunfu,CN',
'Zagreb,HR',
'Zahedan,IR',
'Zaozhuang,CN',
'Zapopan,MX',
'Zaporizhzhya,UA',
'Zaragoza,ES',
'Zaria,NG',
'Zarqa,JO',
'Zhabei,CN',
'Zhangjiagang,CN',
'Zhangjiakou,CN',
'Zhangzhou,CN',
'Zhanjiang,CN',
'Zhaoqing,CN',
'Zhaotong,CN',
'Zhengzhou,CN',
'Zhenjiang,CN',
'Zhongshan,CN',
'Zhoushan,CN',
'Zhu Cheng City,CN',
'Zhuhai,CN',
'Zhumadian,CN',
'Zhuzhou,CN',
'Zibo,CN',
'Zigong,CN',
'Ziyang,CN',
'Zunyi,CN')

today = datetime.today()
today = today.strftime('%Y-%m-%d')

def get_auth_token():
    print("Getting auth token")
    url = "https://www.searates.com/auth/platform-token?id=1"
    files=[]
    headers = {}
    payload = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response_json = response.json()
    auth_token = response_json['s-token']
    return auth_token


def get_place_id(location):
    print("Getting place id for ",location)
    url = "https://www.searates.com/search/google-autocomplete"
    files=[]
    headers = {}

    payload = {'input': location}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response_json = response.json()
    place_id = response_json[0]['place_id']

    return place_id

def get_coordinates(location):
    print("Getting coordinates for ",location)
    url = "https://www.searates.com/search/google-geocode"
    files=[]
    headers = {}

    payload = {'input': get_place_id(location),
    'type': 'place_id'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response_json = response.json()
    lat =  response_json['results'][0]['geometry']['location']['lat']
    lng =  response_json['results'][0]['geometry']['location']['lng']
    return (lat,lng)

def get_rates(origin_lat,origin_lng,destination_lat,destination_lng,size,type,weight,volume,auth_token, today):
    try:
        url = "https://www.searates.com/graphql_rates"
        headers = {
        'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwcm9maWxlIjpudWxsLCJwbGF0Zm9ybSI6MSwibmFtZSI6IiIsImlzcyI6InNlYXJhdGVzLmNvbSIsImlhdCI6MTY5NjkwMzQxNywiZXhwIjoxNjk2OTM5NDE3LCJ0b2tlbiI6bnVsbH0.xNnoeqpbXDCZFkbnru3vN_VXlEqEY9yGcOGB0DtrnPE"
        }
        headers = {
        'Authorization': 'Bearer '+auth_token
        }
        if type == "FCL":
            payload = f"{{\"query\":\"\\n{{\\n  shipment: fcl(from: [{origin_lat}, {origin_lng}], to: [{destination_lat}, {destination_lng}], ST{size}: 1, typeFrom: city, typeTo: city, currency: USD, date: \\\"{today}\\\", source: \\\"le\\\", ) {{\\n    shipmentId\\n    transportationMode\\n    incoterms\\n    currency\\n    cityFrom: city(mode: EXPORT) {{\\n      ...cityFields\\n    }}\\n    cityTo: city(mode: IMPORT) {{\\n      ...cityFields\\n    }}\\n    portFrom: port(mode: EXPORT) {{\\n      ...portFields\\n    }}\\n    portTo: port(mode: IMPORT) {{\\n      ...portFields\\n    }}\\n    freight: oceanFreight {{\\n      ...ratesFields\\n    }}\\n  }}\\n  default {{\\n    services\\n    bookingViaEmail\\n    advertising\\n  }}\\n  identity {{\\n    first_name\\n    last_name\\n    admin\\n    carrier\\n    dfa\\n    dfa_premium\\n    email\\n    phone\\n  }}\\n}}\\n\\nfragment ratesFields on OceanFreight {{\\n  shippingLine\\n  logo\\n  containerCode\\n  validTo\\n  containerType\\n  quantity\\n  linerTerms\\n  originalPrice\\n  originalCurrency\\n  price\\n  distance\\n  transitTime\\n  transportFrom\\n  transportTo\\n  alternative\\n  overdue\\n  co2\\n  co2Price\\n  comment\\n  rateOwner\\n  indicative\\n  portFeesFrom: portFees(mode: EXPORT) {{\\n    ...portFeesFields\\n  }}\\n  portFeesTo: portFees(mode: IMPORT) {{\\n    ...portFeesFields\\n  }}\\n  truckFrom: truck(mode: EXPORT) {{\\n    originalPrice\\n    originalCurrency\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    co2\\n    comment\\n    rateOwner\\n  }}\\n  truckTo: truck(mode: IMPORT) {{\\n    originalPrice\\n    originalCurrency\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    co2\\n    comment\\n    rateOwner\\n  }}\\n  railFrom: rail(mode: EXPORT) {{\\n    originalPrice\\n    originalCurrency\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    co2\\n    comment\\n    rateOwner\\n  }}\\n  railTo: rail(mode: IMPORT) {{\\n    originalPrice\\n    originalCurrency\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    co2\\n    comment\\n    rateOwner\\n  }}\\n  dryFrom: dry(mode: EXPORT) {{\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    city(mode: EXPORT) {{\\n      ...cityFields\\n    }}\\n  }}\\n  dryTo: dry(mode: IMPORT) {{\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    city(mode: IMPORT) {{\\n      ...cityFields\\n    }}\\n  }}\\n    bargeFrom: barge(mode: EXPORT) {{\\n    price\\n    distance\\n    transitTime\\n    validTo\\n    currency\\n    co2\\n    port: portFrom {{\\n      ...portFields\\n    }}\\n  }}\\n  bargeTo: barge(mode: IMPORT) {{\\n    price\\n    distance\\n    transitTime\\n    validTo\\n    currency\\n    co2\\n    port: portTo {{\\n      ...portFields\\n    }}\\n  }}\\n}}\\n\\nfragment cityFields on City {{\\n  id\\n  name\\n  code\\n  countryCode\\n  lat\\n  lng\\n}}\\n\\nfragment portFields on Port {{\\n  id\\n  name\\n  code\\n  countryCode\\n  lat\\n  lng\\n  inaccessible\\n}}\\n\\nfragment portFeesFields on PortFees {{\\n  abbr\\n  title\\n  text\\n  originalPrice\\n  originalCurrency\\n  price\\n  perLot\\n  co2\\n  included\\n}}\\n\",\"variables\":{{}}}}"
            response = requests.request("POST", url, headers=headers, data=payload)
            response_json = response.json()
            num_options = len(response_json['data']['shipment'])
            if num_options ==0:
                min_price = None
                max_price = None
                max_tt = None
                min_tt = None
            for n in range(num_options):
                freight = response_json['data']['shipment'][n]['freight'][0]['price']
                num_port_fees_from = len(response_json['data']['shipment'][n]['freight'][0]['portFeesFrom'])
                port_fees_from = 0
                for w in range(num_port_fees_from):
                    port_fees_from += response_json['data']['shipment'][n]['freight'][0]['portFeesFrom'][w]['price']
                    
                num_port_fees_to = len(response_json['data']['shipment'][n]['freight'][0]['portFeesTo'])
                port_fees_to = 0  
                for x in range(num_port_fees_to):
                    port_fees_to += response_json['data']['shipment'][n]['freight'][0]['portFeesTo'][x]['price']

                truck_from = response_json['data']['shipment'][n]['freight'][0]['truckFrom']['price']
                truck_from_tt = response_json['data']['shipment'][n]['freight'][0]['truckFrom']['transitTime']
                truck_to = response_json['data']['shipment'][n]['freight'][0]['truckTo']['price']
                truck_to_tt = response_json['data']['shipment'][n]['freight'][0]['truckTo']['transitTime']

                total_price = (0 if port_fees_from==None else port_fees_from)+ (0 if port_fees_to==None else port_fees_to)+(0 if freight==None else freight) + (0 if truck_from==None else truck_from) + (0 if truck_to==None else truck_to)
                transit_time = response_json['data']['shipment'][n]['freight'][0]['transitTime']
                if transit_time!=None:
                    for i,c in enumerate(transit_time):
                        if not c.isdigit():
                            break
                    transit_time = int(transit_time[:i])
                else:
                    transit_time=0
                if truck_from_tt!= None:
                    for i,c in enumerate(truck_from_tt):
                        if not c.isdigit():
                            break
                    truck_from_tt = int(truck_from_tt[:i])
                else:
                    truck_from_tt=0
                if truck_to_tt!=None:
                    for i,c in enumerate(truck_to_tt):
                        if not c.isdigit():
                            break
                    truck_to_tt = int(truck_to_tt[:i])
                else:
                    truck_to_tt=0
                transit_time = transit_time + truck_from_tt+truck_to_tt
                if n==0 or total_price <= min_price:
                    min_price = total_price
                if n==0 or total_price >= max_price:
                    max_price = total_price
                if n==0 or transit_time <= min_tt:
                    min_tt = transit_time
                if n==0 or transit_time >= max_tt:
                    max_tt = transit_time
        elif type == "LCL":
            payload = "{\"query\":\"\\n{\\n  shipment: lcl(from: [{origin_lat}, {origin_lng}], to: [{destination_lat}, {destination_lng}], weight: {weight}, volume: {volume}, typeFrom: city, typeTo: city, currency: USD, date: \\\"{today}\\\", source: \\\"le\\\", ) {\\n  shipmentId\\n    transportationMode\\n    currency\\n    cityFrom: city(mode: EXPORT) {\\n      ...cityFields\\n    }\\n    cityTo: city(mode: IMPORT) {\\n      ...cityFields\\n    }\\n    portFrom: port(mode: EXPORT) {\\n      ...portFields\\n    }\\n    portTo: port(mode: IMPORT) {\\n      ...portFields\\n    }\\n    freight: oceanFreight {\\n      ...ratesFields\\n    }\\n  }\\n  default {\\n    services\\n    bookingViaEmail\\n    advertising\\n  }\\n  identity {\\n    first_name\\n    last_name\\n    admin\\n    carrier\\n    dfa\\n    dfa_premium\\n    email\\n    phone\\n  }\\n}\\n\\nfragment ratesFields on OceanFreight {\\n  shippingLine\\n  logo\\n  originalPrice\\n  originalCurrency\\n  price\\n  distance\\n  transitTime\\n  validTo\\n  alternative\\n  overdue\\n  co2\\n  co2Price\\n  comment\\n  rateOwner\\n  indicative\\n  shippingLineId\\n  portFeesFrom: portFees(mode: EXPORT) {\\n    ...portFeesFields\\n  }\\n  portFeesTo: portFees(mode: IMPORT) {\\n    ...portFeesFields\\n  }\\n  truckFrom: truck(mode: EXPORT) {\\n    originalPrice\\n    originalCurrency\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    co2\\n    comment\\n    rateOwner\\n  }\\n  truckTo: truck(mode: IMPORT) {\\n    originalPrice\\n    originalCurrency\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    co2\\n    comment\\n    rateOwner\\n  }\\n}\\n\\nfragment cityFields on City {\\n  id\\n  name\\n  code\\n  countryCode\\n  lat\\n  lng\\n}\\n\\nfragment portFields on Port {\\n  id\\n  name\\n  code\\n  countryCode\\n  lat\\n  lng\\n  inaccessible\\n}\\n\\nfragment portFeesFields on PortFees {\\n  abbr\\n  title\\n  text\\n  originalPrice\\n  originalCurrency\\n  price\\n  perLot\\n  co2\\n  included\\n}\\n\",\"variables\":{}}"
            response = requests.request("POST", url, headers=headers, data=payload)
            response_json = response.json()
            num_options = len(response_json['data']['shipment'])
            if num_options ==0:
                min_price = None
                max_price = None
                max_tt = None
                min_tt = None
            for n in range(num_options):
                freight = response_json['data']['shipment'][n]['freight'][0]['price']
                num_port_fees_from = len(response_json['data']['shipment'][n]['freight'][0]['portFeesFrom'])
                port_fees_from = 0
                for w in range(num_port_fees_from):
                    port_fees_from += response_json['data']['shipment'][n]['freight'][0]['portFeesFrom'][w]['price']
                    
                num_port_fees_to = len(response_json['data']['shipment'][n]['freight'][0]['portFeesTo'])
                port_fees_to = 0  
                for x in range(num_port_fees_to):
                    port_fees_to += response_json['data']['shipment'][n]['freight'][0]['portFeesTo'][x]['price']

                truck_from = response_json['data']['shipment'][n]['freight'][0]['truckFrom']['price']
                truck_from_tt = response_json['data']['shipment'][n]['freight'][0]['truckFrom']['transitTime']
                truck_to = response_json['data']['shipment'][n]['freight'][0]['truckTo']['price']
                truck_to_tt = response_json['data']['shipment'][n]['freight'][0]['truckTo']['transitTime']

                total_price = (0 if port_fees_from==None else port_fees_from)+ (0 if port_fees_to==None else port_fees_to)+(0 if freight==None else freight) + (0 if truck_from==None else truck_from) + (0 if truck_to==None else truck_to)
                transit_time = response_json['data']['shipment'][n]['freight'][0]['transitTime']
                if transit_time!=None:
                    for i,c in enumerate(transit_time):
                        if not c.isdigit():
                            break
                    transit_time = int(transit_time[:i])
                else:
                    transit_time=0
                if truck_from_tt!= None:
                    for i,c in enumerate(truck_from_tt):
                        if not c.isdigit():
                            break
                    truck_from_tt = int(truck_from_tt[:i])
                else:
                    truck_from_tt=0
                if truck_to_tt!=None:
                    for i,c in enumerate(truck_to_tt):
                        if not c.isdigit():
                            break
                    truck_to_tt = int(truck_to_tt[:i])
                else:
                    truck_to_tt=0
                transit_time = transit_time + truck_from_tt+truck_to_tt
                if n==0 or total_price <= min_price:
                    min_price = total_price
                if n==0 or total_price >= max_price:
                    max_price = total_price
                if n==0 or transit_time <= min_tt:
                    min_tt = transit_time
                if n==0 or transit_time >= max_tt:
                    max_tt = transit_time
        elif type == "Air":
            payload = f"{{\"query\":\"\\n{{\\n  shipment: air(from: [{origin_lat}, {origin_lng}], to: [{destination_lat}, {destination_lng}], weight: {weight}, volume: {volume}, typeFrom: city, typeTo: city, currency: USD, date: \\\"{today}\\\", source: \\\"le\\\", ) {{\\n  shipmentId\\n    transportationMode\\n    currency\\n    cityFrom: city(mode: EXPORT) {{\\n      ...cityFields\\n    }}\\n    cityTo: city(mode: IMPORT) {{\\n      ...cityFields\\n    }}\\n    portFrom: port(mode: EXPORT) {{\\n      ...portFields\\n    }}\\n    portTo: port(mode: IMPORT) {{\\n      ...portFields\\n    }}\\n    freight: airFreight {{\\n      ...ratesFields\\n    }}\\n  }}\\n  default {{\\n    services\\n    bookingViaEmail\\n  }}\\n  identity {{\\n    first_name\\n    last_name\\n    admin\\n    carrier\\n    dfa\\n    dfa_premium\\n    email\\n    phone\\n  }}\\n}}\\n\\nfragment ratesFields on OceanFreight {{\\n  shippingLine\\n  logo\\n  originalPrice\\n  originalCurrency\\n  price\\n  freightPrices\\n  distance\\n  transitTime\\n  validTo\\n  co2\\n  co2Price\\n  alternative\\n  overdue\\n  comment\\n  rateOwner\\n  indicative\\n  portFeesFrom: portFees(mode: EXPORT) {{\\n    ...portFeesFields\\n  }}\\n  portFeesTo: portFees(mode: IMPORT) {{\\n    ...portFeesFields\\n  }}\\n  truckFrom: truck(mode: EXPORT) {{\\n    originalPrice\\n    originalCurrency\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    co2\\n    comment\\n    rateOwner\\n  }}\\n  truckTo: truck(mode: IMPORT) {{\\n    originalPrice\\n    originalCurrency\\n    price\\n    distance\\n    transitTime\\n    interpolation\\n    co2\\n    comment\\n    rateOwner\\n  }}\\n}}\\n\\nfragment cityFields on City {{\\n  id\\n  name\\n  code\\n  countryCode\\n  lat\\n  lng\\n}}\\n\\nfragment portFields on Port {{\\n  id\\n  name\\n  code\\n  countryCode\\n  lat\\n  lng\\n}}\\n\\nfragment portFeesFields on PortFees {{\\n  originalPrice\\n  originalCurrency\\n  abbr\\n  title\\n  text\\n  price\\n  perLot\\n  co2\\n  included\\n}}\\n\",\"variables\":{{}}}}"
            response = requests.request("POST", url, headers=headers, data=payload)
            response_json = response.json()
            num_options = len(response_json['data']['shipment'])
            if num_options ==0:
                min_price = None
                max_price = None
                max_tt = None
                min_tt = None
            for n in range(num_options):
                freight = response_json['data']['shipment'][n]['freight']['price']
                num_port_fees_from = len(response_json['data']['shipment'][n]['freight']['portFeesFrom'])
                port_fees_from = 0
                for w in range(num_port_fees_from):
                    port_fees_from += response_json['data']['shipment'][n]['freight']['portFeesFrom'][w]['price']
                    
                num_port_fees_to = len(response_json['data']['shipment'][n]['freight']['portFeesTo'])
                port_fees_to = 0  
                for x in range(num_port_fees_to):
                    port_fees_to += response_json['data']['shipment'][n]['freight']['portFeesTo'][x]['price']

                truck_from = response_json['data']['shipment'][n]['freight']['truckFrom']['price']
                truck_from_tt = response_json['data']['shipment'][n]['freight']['truckFrom']['transitTime']
                truck_to = response_json['data']['shipment'][n]['freight']['truckTo']['price']
                truck_to_tt = response_json['data']['shipment'][n]['freight']['truckTo']['transitTime']

                total_price = port_fees_from+port_fees_to+freight+truck_from+truck_to
                transit_time = response_json['data']['shipment'][n]['freight']['transitTime']
                for i,c in enumerate(transit_time):
                    if not c.isdigit():
                        break
                transit_time = int(transit_time[:i])
                for i,c in enumerate(truck_from_tt):
                    if not c.isdigit():
                        break
                truck_from_tt = int(truck_from_tt[:i])
                for i,c in enumerate(truck_to_tt):
                    if not c.isdigit():
                        break
                truck_to_tt = int(truck_to_tt[:i])
                transit_time = transit_time + truck_from_tt+truck_to_tt
                if n==0 or total_price <= min_price:
                    min_price = total_price
                if n==0 or total_price >= max_price:
                    max_price = total_price
                if n==0 or transit_time <= min_tt:
                    min_tt = transit_time
                if n==0 or transit_time >= max_tt:
                    max_tt = transit_time
        elif type == "FTL":
            payload = f"{{\"query\":\"\\n{{\\n  shipment: ftl(from: [{origin_lat}, {origin_lng}], to: [{destination_lat}, {destination_lng}], volume: {volume} typeFrom: city, typeTo: city, currency: USD, date: \\\"{today}\\\", source: \\\"le\\\", ) {{\\n    shipmentId\\n    currency\\n    transportationMode\\n    validTo\\n    freight: landFreight {{\\n      co2\\n      co2Price\\n      originalPrice\\n      originalCurrency\\n      price,\\n      distance,\\n      transitTime,\\n      interpolation,\\n      shippingLine,\\n      logo\\n      comment\\n      rateOwner\\n      overdue\\n      indicative\\n    }}\\n  }}\\n  default {{\\n    bookingViaEmail\\n  }}\\n  identity {{\\n    first_name\\n    last_name\\n    admin\\n    carrier\\n    dfa\\n    dfa_premium\\n    email\\n    phone\\n  }}\\n}}\\n\",\"variables\":{{}}}}"
            response = requests.request("POST", url, headers=headers, data=payload)
            response_json = response.json()
            num_options = len(response_json['data']['shipment'])
            if num_options ==0:
                min_price = None
                max_price = None
                max_tt = None
                min_tt = None
            for n in range(num_options):
                freight = response_json['data']['shipment'][n]['freight']['price']

                total_price = freight
                transit_time = response_json['data']['shipment'][n]['freight']['transitTime']
                for i,c in enumerate(transit_time):
                    if not c.isdigit():
                        break
                transit_time = int(transit_time[:i])
                if n==0 or total_price <= min_price:
                    min_price = total_price
                if n==0 or total_price >= max_price:
                    max_price = total_price
                if n==0 or transit_time <= min_tt:
                    min_tt = transit_time
                if n==0 or transit_time >= max_tt:
                    max_tt = transit_time
        elif type == "LTL":
            payload = f"{{\"query\":\"\\n{{\\n  shipment: ltl(from: [{origin_lat}, {origin_lng}], to: [{destination_lat}, {destination_lng}], weight: {weight}, volume: {volume}, typeFrom: city, typeTo: city, currency: USD, date: \\\"2023-10-09\\\", source: \\\"le\\\", ) {{\\n    shipmentId\\n    currency\\n    transportationMode\\n    validTo\\n    freight: landFreight {{\\n       co2\\n       co2Price\\n       originalPrice\\n       originalCurrency\\n       price,\\n       distance,\\n       transitTime,\\n       interpolation,\\n       comment\\n       rateOwner\\n       overdue\\n       indicative\\n    }}\\n  }}\\n  default {{\\n    bookingViaEmail\\n  }}\\n  identity {{\\n    first_name\\n    last_name\\n    admin\\n    carrier\\n    dfa\\n    dfa_premium\\n    email\\n    phone\\n  }}\\n}}\\n\",\"variables\":{{}}}}"
            response = requests.request("POST", url, headers=headers, data=payload)
            response_json = response.json()
            num_options = len(response_json['data']['shipment'])
            if num_options ==0:
                min_price = None
                max_price = None
                max_tt = None
                min_tt = None
            for n in range(num_options):
                freight = response_json['data']['shipment'][n]['freight']['price']

                total_price = freight
                transit_time = response_json['data']['shipment'][n]['freight']['transitTime']
                for i,c in enumerate(transit_time):
                    if not c.isdigit():
                        break
                transit_time = int(transit_time[:i])
                if n==0 or total_price <= min_price:
                    min_price = total_price
                if n==0 or total_price >= max_price:
                    max_price = total_price
                if n==0 or transit_time <= min_tt:
                    min_tt = transit_time
                if n==0 or transit_time >= max_tt:
                    max_tt = transit_time

    except:
        min_price = None
        max_price = None
        max_tt = None
        min_tt = None
    return (min_price,max_price,min_tt,max_tt)

origin = st.selectbox('Origin',countries, index = 788)
destination = st.selectbox( 'Destination',countries, index = 512)

with st.expander("SeaRates Parameters"):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        air_volume = str(st.number_input('Air Cu M', 0, 1000, 5))
        air_weight = str(st.number_input('Air Kg', 0, 10000, 1000))
    with c2:
        LCL_volume = str(st.number_input('LCL Cu M', 0, 1000, 5))
        LCL_weight = str(st.number_input('LCL Kg', 0, 10000, 1000))
    with c3:
        LTL_volume = str(st.number_input('LTL Cu M', 0, 1000, 5))
        LTL_weight = str(st.number_input('LTL Kg', 0, 10000, 1000))
    with c4:
        FTL_volume = str(st.number_input('FTL Cu M', 0, 1000, 86))

with st.expander("Freightos Parameters"):
    c1, c2, c3 = st.columns(3)
    with c1:
        fcl_40_weight = st.number_input('40\' FCL Kg', 0, 10000, 4000)
        fcl_20_weight = st.number_input('20\' FCL Kg', 0, 10000, 2000)
    with c2:
        pallet_count = st.number_input('Pallet Count', 0, 1000, 5)
        pallet_volume = st.number_input('Cu M / Pallet', 0, 1000, 1)
        pallet_weight = st.number_input('Kg / Pallet', 0, 10000, 200)
    with c3:
        FCL_volume = st.number_input('FCL Cu M', 0, 1000, 86)


try:
    with st.spinner('Loading SeaRates Rates...'):
        auth_token = get_auth_token()
        origin_lat,origin_lng = get_coordinates(origin)
        destination_lat,destination_lng  = get_coordinates(destination)

        df = pd.DataFrame()
    #20' container
    with st.spinner('Loading SeaRates Rates: FCL 20\' Rates...'):
        print("Getting SeaRates FCL 20' Rates")
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"20","FCL","","",auth_token,today)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df=pd.DataFrame({"Type":['20ft FCL'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
    #40' container
    with st.spinner('Loading SeaRates Rates: FCL 40\' Rates...'):
        print("Getting SeaRates FCL 40' Rates")
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"40","FCL","","",auth_token,today)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df2=pd.DataFrame({"Type":['40ft FCL'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df2])
            else:
                df = df2
    #LCL
    with st.spinner('Loading SeaRates Rates: LCL Rates...'):
        print("Getting SeaRates LCL Rates")
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"","LCL",LCL_weight,LCL_volume,auth_token,today)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df3=pd.DataFrame({"Type":['LCL'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df3])
            else:
                df = df3
    #Air
    with st.spinner('Loading SeaRates Rates: Air Rates...'):
        print("Getting SeaRates Air Rates")
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"","Air",air_weight,air_volume,auth_token,today)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df4=pd.DataFrame({"Type":['Air'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df4])
            else:
                df = df4
    #FTL
    with st.spinner('Loading SeaRates Rates: FTL Rates...'):
        print("Getting SeaRates FTL Rates")
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"","FTL","",FTL_volume,auth_token,today)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df4=pd.DataFrame({"Type":['FTL'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df4])
            else:
                df = df4
    #LTL
    with st.spinner('Loading SeaRates Rates: LTL Rates...'):
        print("Getting SeaRates LTL Rates")
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"","LTL",LTL_weight,LTL_volume,auth_token,today)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df5=pd.DataFrame({"Type":['LTL'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df5])
            else:
                df = df5
    with st.spinner('Loading SeaRates Rates...'):
        fig = plt.figure(figsize=(24,4))
        gs = GridSpec(nrows=2, ncols=1, height_ratios=[1,1])
        ax0 = fig.add_subplot(gs[0, :])
        ax0.axis('off')
        ax0.set_title("SeaRates", fontsize=24)
        table0= ax0.table( 
            cellText = df.values,
            colLabels= df.columns,
            rowLoc = 'left',
            cellLoc ='center',  
            loc ='upper left')
        table0.auto_set_font_size(False)     
        table0.set_fontsize(24)
        table0.scale(1,3.5)

        st.pyplot(plt.gcf())
except:
    with st.spinner('Loading SeaRates Rates...'):
        fig = plt.figure(figsize=(24,5))
        gs = GridSpec(nrows=2, ncols=1, height_ratios=[1,1])
        ax0 = fig.add_subplot(gs[0, :])
        ax0.axis('off')
        ax0.set_title("SeaRates", fontsize=24)
        table0= ax0.table( 
            cellText = pd.DataFrame({"result":["No Rates Found"]}).values,
            rowLoc = 'left',
            cellLoc ='center',  
            loc ='upper left')
        table0.auto_set_font_size(False)     
        table0.set_fontsize(24)
        table0.scale(1,3.5)

        st.pyplot(plt.gcf())

API_BASE_URL = 'https://ship.freightos.com/api/shippingCalculator'

def get_freight_estimate(origin, destination, weight, length, width, height,loadtype,quantity,type,volume):
    headers = {}
    if type == 'FCL':
        params = {
            'loadtype': loadtype,
            'weight': weight,
            'width': width,
            'length': length,
            'height': height,
            'origin': origin,
            'quantity': quantity,
            'destination': destination,
            'volume':volume
        }
    else:
        params = {
            'loadtype': loadtype,
            'weight': weight,
            'width': width,
            'length': length,
            'height': height,
            'origin': origin,
            'quantity': quantity,
            'destination': destination,
            'volume':volume
        }

    try:
        response = requests.request("GET", API_BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

def get_results(origin,destination,loadtype,weight,quantity,type,volume):
    length = None
    width = None
    height = None
    result = pd.DataFrame()

    try:
        json_response = get_freight_estimate(origin, destination, weight, length, width, height,loadtype,quantity,type,volume)
        if json_response['response']['estimatedFreightRates']['numQuotes']==0:
            result['mode']= [None]
            result['price.min.moneyAmount.amount']= [None]
            result['price.min.moneyAmount.currency']= [None]
            result['price.max.moneyAmount.amount']= [None]
            result['price.max.moneyAmount.currency']= [None]
            result['transitTimes.unit']= [None]
            result['transitTimes.min']= [None]
            result['transitTimes.max']= [None]
            result['loadtype']= loadtype
            result['weight']= weight
            result['width']= width
            result['length']= length
            result['height']= height
            result['origin']= origin
            result['quantity']= quantity
            result['destination']= destination
        else:
            estimated_data = json_response['response']['estimatedFreightRates']['mode']
            result = pd.json_normalize(estimated_data)
            result['loadtype']= loadtype
            result['weight']= weight
            result['width']= width
            result['length']= length
            result['height']= height
            result['origin']= origin
            result['quantity']= quantity
            result['destination']= destination
    except:
        result['mode']= [None]
        result['price.min.moneyAmount.amount']= [None]
        result['price.min.moneyAmount.currency']= [None]
        result['price.max.moneyAmount.amount']= [None]
        result['price.max.moneyAmount.currency']= [None]
        result['transitTimes.unit']= [None]
        result['transitTimes.min']= [None]
        result['transitTimes.max']= [None]
        result['loadtype']= loadtype
        result['weight']= weight
        result['width']= width
        result['length']= length
        result['height']= height
        result['origin']= origin
        result['quantity']= quantity
        result['destination']= destination
        

    result = result[['mode','price.min.moneyAmount.amount','price.max.moneyAmount.amount','transitTimes.min','transitTimes.max']]
    result.columns = ['Mode','Min Price','Max Price','Min Transit Time','Max Transit Time']
    result['Mode']=result['Mode'].str.upper()
    result['Min Price']=result['Min Price'].apply(lambda x: "${:,.0f}".format(x) if x!=None else None)
    result['Max Price']=result['Max Price'].apply(lambda x: "${:,.0f}".format(x) if x!=None else None)
    return result

with st.spinner('Loading Freightos Rates: FCL 40\' Rates...'):
    print("Getting Freightos FCL 40' Rates")
    loadtype = 'container40'
    weight = fcl_40_weight  # weight in kilograms
    quantity = 1
    results=get_results(origin,destination,loadtype,weight,quantity,'FCL','')
    nrow = len(results)
    results.insert(loc=0, column='Type', value =list(repeat('40ft', nrow)))


with st.spinner('Loading Freightos Rates: FCL 20\' Rates...'):
    print("Getting Freightos FCL 20' Rates")
    loadtype = 'container20'
    weight = fcl_20_weight  # weight in kilograms
    quantity = 1
    results2=get_results(origin,destination,loadtype,weight,quantity,'FCL','')
    nrow = len(results2)
    results2.insert(loc=0, column='Type', value =list(repeat('20ft', nrow)))
    results = pd.concat([results,results2])

with st.spinner('Loading Freightos Rates: LCL Rates...'):
    print("Getting Freightos LCL Rates")
    loadtype = 'pallets'
    weight = pallet_weight  # weight in kilograms
    quantity = pallet_count
    results3=get_results(origin,destination,loadtype,weight,quantity,'LCL','1')
    nrow = len(results3)
    results3.insert(loc=0, column='Type', value =list(repeat('Pallets', nrow)))
    results = pd.concat([results,results3])

with st.spinner('Loading Freightos Rates...'):
    if results['Min Price'].isnull().all():
        fig = plt.figure(figsize=(24,4))
        gs = GridSpec(nrows=2, ncols=1, height_ratios=[1,1])
        ax0 = fig.add_subplot(gs[0, :])
        ax0.axis('off')
        ax0.set_title("Freightos", fontsize=24)
        table0= ax0.table( 
            cellText = pd.DataFrame({"result":["No Rates Found"]}).values,
            rowLoc = 'left',
            cellLoc ='center',  
            loc ='upper left')
        table0.auto_set_font_size(False)     
        table0.set_fontsize(24)
        table0.scale(1,3.5)

        st.pyplot(plt.gcf())

    else:
        results=results[results['Min Price'].isnull()==False]
        fig = plt.figure(figsize=(24,4))
        ax0 = fig.add_subplot()
        ax0.axis('off')
        ax0.set_title("Freightos", fontsize=24)
        table1= ax0.table( 
            cellText = results.values,
            colLabels= results.columns,
            rowLoc = 'left',
            cellLoc ='center',  
            loc ='upper left')
        table1.auto_set_font_size(False)     
        table1.set_fontsize(24)
        table1.scale(1,3.5)
        st.pyplot(plt.gcf())