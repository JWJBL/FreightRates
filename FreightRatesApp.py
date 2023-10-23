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

countries = ('Shanghai,CN',
'Beijing,CN',
'Shenzhen,CN',
'Guangzhou,CN',
'Lagos,NG',
'Istanbul,TR',
'Chengdu,CN',
'Mumbai,IN',
'Sao Paulo,BR',
'Mexico City,MX',
'Karachi,PK',
'Tianjin,CN',
'Delhi,IN',
'Wuhan,CN',
'Moscow,RU',
'Dhaka,BD',
'Seoul,KR',
'Dongguan,CN',
'Cairo,EG',
'Xi\'an,CN',
'Nanjing,CN',
'Hangzhou,CN',
'Foshan,CN',
'Ho Chi Minh City,VN',
'London,GB',
'New York City,US',
'Jakarta,ID',
'Bengaluru,IN',
'Tokyo,JP',
'Hanoi,VN',
'Taipei,TW',
'Kinshasa,CD',
'Lima,PE',
'Bogota,CO',
'Hong Kong,HK',
'Chongqing,CN',
'Baghdad,IQ',
'Qingdao,CN',
'Tehran,IR',
'Shenyang,CN',
'Hyderabad,IN',
'Rio de Janeiro,BR',
'Suzhou,CN',
'Ahmedabad,IN',
'Abidjan,CI',
'Lahore,PK',
'Singapore,SG',
'Johannesburg,ZA',
'Dar es Salaam,TZ',
'Saint Petersburg,RU',
'Alexandria,EG',
'Harbin,CN',
'Sydney,AU',
'Bangkok,TH',
'Hefei,CN',
'Melbourne,AU',
'Dalian,CN',
'Santiago,CL',
'Changchun,CN',
'Cape Town,ZA',
'Jeddah,SA',
'Chennai,IN',
'Kolkata,IN',
'Xiamen,CN',
'Surat,IN',
'Yangon,MM',
'Kabul,AF',
'Wuxi,CN',
'Giza,EG',
'Jinan,CN',
'Taiyuan,CN',
'Zhengzhou,CN',
'Riyadh,SA',
'Kano,NG',
'Shijiazhuang,CN',
'Chattogram,BD',
'Los Angeles,US',
'Kunming,CN',
'Zhongshan,CN',
'Nanning,CN',
'Shantou,CN',
'Yokohama,JP',
'Fuzhou,CN',
'Ningbo,CN',
'Busan,KR',
'Ibadan,NG',
'Puyang,CN',
'Ankara,TR',
'Dubai,AE',
'Shiyan,CN',
'Berlin,DE',
'Tangshan,CN',
'Changzhou,CN',
'Madrid,ES',
'Pyongyang,KP',
'Casablanca,MA',
'Zibo,CN',
'Pune,IN',
'Durban,ZA',
'Bursa,TR',
'Changsha,CN',
'Guiyang,CN',
'UEruemqi,CN',
'Caracas,VE',
'Lanzhou,CN',
'Incheon,KR',
'Huizhou,CN',
'Buenos Aires,AR',
'Surabaya,ID',
'Haikou,CN',
'Kanpur,IN',
'Kyiv,UA',
'Quito,EC',
'Luanda,AO',
'Quezon City,PH',
'Addis Ababa,ET',
'Osaka,JP',
'Nairobi,KE',
'Linyi,CN',
'Baoding,CN',
'Brooklyn,US',
'Guayaquil,EC',
'Belo Horizonte,BR',
'Salvador,BR',
'Jaipur,IN',
'Chicago,US',
'Wenzhou,CN',
'Yunfu,CN',
'Toronto,CA',
'Navi Mumbai,IN',
'Mogadishu,SO',
'Brisbane,AU',
'Daegu,KR',
'Bekasi,ID',
'Faisalabad,PK',
'Izmir,TR',
'Huai\'an,CN',
'Dakar,SN',
'Lucknow,IN',
'Bandung,ID',
'Medan,ID',
'Fortaleza,BR',
'Cali,CO',
'Nanchang,CN',
'Hohhot,CN',
'Rome,IT',
'Mashhad,IR',
'Houston,US',
'Kowloon,HK',
'Shaoxing,CN',
'Nantong,CN',
'Queens,US',
'Nagpur,IN',
'Yantai,CN',
'Maracaibo,VE',
'Manaus,BR',
'Brasilia,BR',
'Zhuhai,CN',
'Santo Domingo,DO',
'Perth,AU',
'Nagoya,JP',
'Havana,CU',
'Baotou,CN',
'Paris,FR',
'Coimbatore,IN',
'Aleppo,SY',
'Kunshan,CN',
'Al Mawsil al Jadidah,IQ',
'Depok,ID',
'Weifang,CN',
'Zunyi,CN',
'Al Basrah al Qadimah,IQ',
'La Paz,BO',
'Lianyungang,CN',
'Medellin,CO',
'Tashkent,UZ',
'Algiers,DZ',
'Ganzhou,CN',
'Almaty,KZ',
'Khartoum,SD',
'Sapporo,JP',
'Accra,GH',
'Curitiba,BR',
'Ordos,CN',
'Sanaa,YE',
'Tijuana,MX',
'Beirut,LB',
'Tangerang,ID',
'Jieyang,CN',
'Jilin,CN',
'Bucharest,RO',
'Camayenne,GN',
'Kakamega,KE',
'Port Harcourt,NG',
'Nanchong,CN',
'Datong,CN',
'Hamburg,DE',
'Indore,IN',
'Santa Cruz de la Sierra,BO',
'Vadodara,IN',
'Iztapalapa,MX',
'Nanyang,CN',
'Gaziantep,TR',
'Abu Dhabi,AE',
'Jiangmen,CN',
'Diyarbakir,TR',
'Benin City,NG',
'Jiangyin,CN',
'Adana,TR',
'Davao,PH',
'Fuyang,CN',
'Conakry,GN',
'Montreal,CA',
'Bayan Nur,CN',
'Maracay,VE',
'Chaozhou,CN',
'Rawalpindi,PK',
'Minsk,BY',
'Budapest,HU',
'Qingyuan,CN',
'Tai\'an,CN',
'Leon de los Aldama,MX',
'Warsaw,PL',
'Soweto,ZA',
'Puebla,MX',
'Vienna,AT',
'Mosul,IQ',
'Kallakurichi,IN',
'Xining,CN',
'Changshu,CN',
'Palembang,ID',
'Huainan,CN',
'Rabat,MA',
'Semarang,ID',
'Recife,BR',
'Suzhou,CN',
'Ecatepec de Morelos,MX',
'Lu\'an,CN',
'Barcelona,ES',
'Valencia,VE',
'Pretoria,ZA',
'Yancheng,CN',
'Novosibirsk,RU',
'Erbil,IQ',
'Phoenix,US',
'Taizhou,CN',
'Daqing,CN',
'Fukuoka,JP',
'Manila,PH',
'Patna,IN',
'Bhopal,IN',
'Wuhu,CN',
'Santiago de Queretaro,MX',
'Dazhou,CN',
'Yangzhou,CN',
'Kaduna,NG',
'Mecca,SA',
'Philadelphia,US',
'Phnom Penh,KH',
'Guilin,CN',
'Damascus,SY',
'Zhaoqing,CN',
'Onitsha,NG',
'Mianyang,CN',
'Isfahan,IR',
'Ludhiana,IN',
'Harare,ZW',
'Putian,CN',
'Shangqiu,CN',
'Goiania,BR',
'Kawasaki,JP',
'Kobe,JP',
'Kaohsiung,TW',
'Stockholm,SE',
'Ciudad Juarez,MX',
'Khulna,BD',
'Caloocan City,PH',
'Belem,BR',
'Yekaterinburg,RU',
'Gwangju,KR',
'Porto Alegre,BR',
'Yinchuan,CN',
'Manhattan,US',
'Taizhou,CN',
'Asuncion,PY',
'Yiwu,CN',
'Zapopan,MX',
'Daejeon,KR',
'Quanzhou,CN',
'Kumasi,GH',
'Madurai,IN',
'Jinhua,CN',
'Kyoto,JP',
'Cixi,CN',
'Changde,CN',
'Kuala Lumpur,MY',
'Kaifeng,CN',
'Anshan,CN',
'Karaj,IR',
'Kathmandu,NP',
'Baoji,CN',
'Suqian,CN',
'Multan,PK',
'Liuzhou,CN',
'Tirunelveli,IN',
'San Antonio,US',
'Kharkiv,UA',
'Zhangjiagang,CN',
'Agra,IN',
'Tabriz,IR',
'Makassar,ID',
'Jinjiang,CN',
'Bozhou,CN',
'Qujing,CN',
'Zhanjiang,CN',
'Fushun,CN',
'San Diego,US',
'Antananarivo,MG',
'Rajkot,IN',
'Luoyang,CN',
'Konya,TR',
'Adelaide,AU',
'Hyderabad,PK',
'Guadalajara,MX',
'The Bronx,US',
'Gujranwala,PK',
'Guankou,CN',
'Lubumbashi,CD',
'Milan,IT',
'South Tangerang,ID',
'Najafgarh,IN',
'Handan,CN',
'Kampala,UG',
'Yichang,CN',
'Heze,CN',
'Antalya,TR',
'Abobo,CI',
'Jamshedpur,IN',
'Douala,CM',
'Basrah,IQ',
'Saitama,JP',
'Gorakhpur,IN',
'Liupanshui,CN',
'Cordoba,AR',
'Maoming,CN',
'Dallas,US',
'Callao,PE',
'Medina,SA',
'Yaounde,CM',
'Bamako,ML',
'Qinzhou,CN',
'Luohe,CN',
'Xiangyang,CN',
'Yangjiang,CN',
'Nashik,IN',
'Yixing,CN',
'Brazzaville,CG',
'Pimpri,IN',
'Amman,JO',
'Sharjah,AE',
'Budta,PH',
'Belgrade,RS',
'Montevideo,UY',
'Lusaka,ZM',
'Xuchang,CN',
'Kalyan,IN',
'Zigong,CN',
'Thane,IN',
'Munich,DE',
'Nizhniy Novgorod,RU',
'Jepara,ID',
'Xuzhou,CN',
'Dammam,SA',
'Ra\'s Bayrut,LB',
'Neijiang,CN',
'Shiraz,IR',
'Yiyang,CN',
'Kazan,RU',
'Suwon,KR',
'Jining,CN',
'Barquisimeto,VE',
'Shubra al Khaymah,EG',
'Abuja,NG',
'Port-au-Prince,HT',
'Xinyang,CN',
'Liaocheng,CN',
'Jinzhong,CN',
'Meerut,IN',
'Nowrangapur,IN',
'Faridabad,IN',
'Peshawar,PK',
'Karbala,IQ',
'Changzhi,CN',
'Tianshui,CN',
'Mombasa,KE',
'Mandalay,MM',
'Barranquilla,CO',
'Kayseri,TR',
'Chelyabinsk,RU',
'Merida,MX',
'Bulawayo,ZW',
'Omdurman,SD',
'Santiago de los Caballeros,DO',
'Shymkent,KZ',
'Hiroshima,JP',
'Weinan,CN',
'Ghaziabad,IN',
'Dhanbad,IN',
'Dombivli,IN',
'Maputo,MZ',
'Gustavo Adolfo Madero,MX',
'Jiaxing,CN',
'Omsk,RU',
'Guarulhos,BR',
'Bandar Lampung,ID',
'Prague,CZ',
'Varanasi,IN',
'Batam,ID',
'Jiujiang,CN',
'Samara,RU',
'Copenhagen,DK',
'Sofia,BG',
'Tripoli,LY',
'Anyang,CN',
'Birmingham,GB',
'Bijie,CN',
'Monterrey,MX',
'Kigali,RW',
'Rostov-na-Donu,RU',
'Zhuzhou,CN',
'Malingao,PH',
'Ufa,RU',
'Ranchi,IN',
'Baku,AZ',
'Shangrao,CN',
'Huaibei,CN',
'Meishan,CN',
'Ciudad Nezahualcoyotl,MX',
'Bogor,ID',
'Sendai,JP',
'Yerevan,AM',
'Amritsar,IN',
'Krasnoyarsk,RU',
'Fuzhou,CN',
'Ouagadougou,BF',
'Guigang,CN',
'Pekanbaru,ID',
'Hengyang,CN',
'Prayagraj,IN',
'Goyang-si,KR',
'Visakhapatnam,IN',
'Yulin,CN',
'Jingzhou,CN',
'Tbilisi,GE',
'Voronezh,RU',
'Xinxiang,CN',
'Yichun,CN',
'Taichung,TW',
'Teni,IN',
'Xianyang,CN',
'Mexicali,MX',
'Matola,MZ',
'Seongnam-si,KR',
'Maceio,BR',
'Campinas,BR',
'Sanya,CN',
'Rangpur,BD',
'Kirkuk,IQ',
'Jabalpur,IN',
'Comilla,BD',
'Shaoguan,CN',
'Haora,IN',
'San Jose,US',
'Longyan,CN',
'Dublin,IE',
'Tiruchirappalli,IN',
'Yongzhou,CN',
'Calgary,CA',
'Brussels,BE',
'Sambhaji Nagar,IN',
'Huzhou,CN',
'Odesa,UA',
'Volgograd,RU',
'Edmonton,CA',
'Wuwei,CN',
'Namangan,UZ',
'Arequipa,PE',
'Hanzhong,CN',
'Hezhou,CN',
'Bujumbura,BI',
'Zhu Cheng City,CN',
'Shivaji Nagar,IN',
'Dongying,CN',
'Luzhou,CN',
'Solapur,IN',
'Guatemala City,GT',
'Meizhou,CN',
'Yueyang,CN',
'Laiwu,CN',
'Da Nang,VN',
'Benxi,CN',
'Perm,RU',
'Chiba,JP',
'Pingdingshan,CN',
'Srinagar,IN',
'Zaria,NG',
'Managua,NI',
'Bengbu,CN',
'Jerusalem,IL',
'Dnipro,UA',
'Port Elizabeth,ZA',
'Fes,MA',
'Cebu City,PH',
'Koeln,DE',
'Tiruppur,IN',
'Ulsan,KR',
'Chandigarh,IN',
'Xiangtan,CN',
'Linfen,CN',
'Victoria,HK',
'Jacksonville,US',
'Zhenjiang,CN',
'Ciudad Guayana,VE',
'Rosario,AR',
'Sultanah,SA',
'Kitakyushu,JP',
'Monrovia,LR',
'Kingston,JM',
'Baoshan,CN',
'Austin,US',
'Rui\'an,CN',
'Chihuahua,MX',
'Nay Pyi Taw,MM',
'Jodhpur,IN',
'Trujillo,PE',
'Fort Worth,US',
'Salem,IN',
'Sao Luis,BR',
'Cartagena,CO',
'Laibin,CN',
'Naples,IT',
'Padang,ID',
'Xiaogan,CN',
'Campo Grande,BR',
'Columbus,US',
'Ziyang,CN',
'Bobo-Dioulasso,BF',
'Sale,MA',
'Quzhou,CN',
'Petaling Jaya,MY',
'Donetsk,UA',
'Abu Ghurayb,IQ',
'Bishkek,KG',
'Qom,IR',
'Zaozhuang,CN',
'Krasnodar,RU',
'Guwahati,IN',
'Eskisehir,TR',
'Aba,NG',
'Natal,BR',
'Pingxiang,CN',
'Indianapolis,US',
'Zhoushan,CN',
'Gwalior,IN',
'Qiqihar,CN',
'Klang,MY',
'As Sulaymaniyah,IQ',
'Puning,CN',
'Mbuji-Mayi,CD',
'Vijayawada,IN',
'Charlotte,US',
'Pikine,SN',
'Bhiwandi,IN',
'Teresina,BR',
'Marseille,FR',
'Ankang,CN',
'Mysore,IN',
'Langfang,CN',
'Jiaozuo,CN',
'San Francisco,US',
'Liverpool,GB',
'Aden,YE',
'Rohini,IN',
'Wanxian,CN',
'Guang\'an,CN',
'Johor Bahru,MY',
'Kanayannur,IN',
'Tegucigalpa,HN',
'Bucheon-si,KR',
'Turin,IT',
'Al Ain City,AE',
'Cheongju-si,KR',
'Saratov,RU',
'Ulan Bator,MN',
'Weihai,CN',
'Takeo,KH',
'Malang,ID',
'Haiphong,VN',
'Cochabamba,BO',
'Ahvaz,IR',
'Hubli,IN',
'Zhabei,CN',
'Ipoh,MY',
'Xinyu,CN',
'Marrakesh,MA',
'Bhubaneswar,IN',
'Yibin,CN',
'Kampung Baru Subang,MY',
'Bouake,CI',
'Samarinda,ID',
'Taicang,CN',
'Bien Hoa,VN',
'Nova Iguacu,BR',
'Chenzhou,CN',
'Duque de Caxias,BR',
'Joao Pessoa,BR',
'Jos,NG',
'Barcelona,VE',
'Ilorin,NG',
'Hermosillo,MX',
'Ottawa,CA',
'Can Tho,VN',
'Culiacan,MX',
'Benghazi,LY',
'Malatya,TR',
'Anqing,CN',
'Freetown,SL',
'San Pedro Sula,HN',
'Narela,IN',
'Xingtai,CN',
'Niigata,JP',
'Muscat,OM',
'Zarqa,JO',
'Naucalpan de Juarez,MX',
'Cankaya,TR',
'Hamamatsu,JP',
'Valencia,ES',
'Rahim Yar Khan,PK',
'Pasragad Branch,IR',
'Zhaotong,CN',
'Panzhihua,CN',
'Boumerdas,DZ',
'Jalandhar,IN',
'Thiruvananthapuram,IN',
'Chuzhou,CN',
'Sakai,JP',
'Port Said,EG',
'Cotonou,BJ',
'Cucuta,CO',
'Homs,SY',
'Xuanzhou,CN',
'Niamey,NE',
'Tainan,TW',
'Shangyu,CN',
'Lodz,PL',
'Tyumen,RU',
'Erzurum,TR',
'Kahriz,IR',
'Anshun,CN',
'Rajshahi,BD',
'Kota,IN',
'Wuzhou,CN',
'Qinhuangdao,CN',
'Maiduguri,NG',
'Krakow,PL',
'Aligarh,IN',
'Shaoyang,CN',
'Pietermaritzburg,ZA',
'Lome,TG',
'Winnipeg,CA',
'Bagcilar,TR',
'Bareilly,IN',
'Buraydah,SA',
'Sao Bernardo do Campo,BR',
'Hegang,CN',
'Morelia,MX',
'Nampula,MZ',
'Riga,LV',
'Amsterdam,NL',
'Ma\'anshan,CN',
'Shah Alam,MY',
'Kumamoto,JP',
'Seattle,US',
'Oyo,NG',
'Torreon,MX',
'Deyang,CN',
'Quetta,PK',
'Yangquan,CN',
'Sao Jose dos Campos,BR',
'Ashgabat,TM',
'Alvaro Obregon,MX',
'Denpasar,ID',
'Muzaffarabad,PK',
'Wanzhou,CN',
'San Luis Potosi,MX',
'Aguascalientes,MX',
'Zhumadian,CN',
'Moradabad,IN',
'N\'Djamena,TD',
'Okayama,JP',
'Lviv,UA',
'Ansan-si,KR',
'Denver,US',
'Ribeirao Preto,BR',
'Zaporizhzhya,UA',
'Saltillo,MX',
'Latakia,SY',
'Subang Jaya,MY',
'Tolyatti,RU',
'Jaboatao,BR',
'Santo Domingo Oeste,DO',
'Santo Domingo Este,DO',
'Battagram,PK',
'Suez,EG',
'Changzhi,CN',
'Agadir,MA',
'Sarajevo,BA',
'Balikpapan,ID',
'Bauchi,NG',
'Tunis,TN',
'Zhangjiakou,CN',
'Serang,ID',
'Shizuoka,JP',
'Paranaque City,PH',
'Washington,US',
'Nashville,US',
'Fuxin,CN',
'Enugu,NG',
'Ta\'if,SA',
'Tangier,MA',
'Huangshi,CN',
'Liaoyang,CN',
'Sorocaba,BR',
'Baise,CN',
'Situbondo,ID',
'Sevilla,ES',
'Binzhou,CN',
'El Paso,US',
'Oklahoma City,US',
'Yuncheng,CN',
'Raipur,IN',
'General Santos,PH',
'Dezhou,CN',
'Dushanbe,TJ',
'Osasco,BR',
'Detroit,US',
'Boston,US',
'Zaragoza,ES',
'Gorakhpur,IN',
'Guadalupe,MX',
'Acapulco de Juarez,MX',
'Sanmenxia,CN',
'E\'zhou,CN',
'Mississauga,CA',
'Madinat an Nasr,EG',
'Tabuk,SA',
'Cheonan,KR',
'Mudanjiang,CN',
'Aracaju,BR',
'Athens,GR',
'Zagreb,HR',
'Leshan,CN',
'Santo Andre,BR',
'Rizhao,CN',
'Nouakchott,MR',
'Pointe-Noire,CG',
'Helsinki,FI',
'Pontianak,ID',
'Banjarmasin,ID',
'Puducherry,IN',
'Suining,CN',
'Puyang,CN',
'Tlalnepantla,MX',
'Portland,US',
'Jeonju,KR',
'Frankfurt am Main,DE',
'Macau,MO',
'Palermo,IT',
'Izhevsk,RU',
'Colombo,LK',
'Maturin,VE',
'Lilongwe,MW',
'Oran,DZ',
'Honcho,JP',
'Taguig,PH',
'New South Memphis,US',
'Hwaseong-si,KR',
'Gold Coast,AU',
'Kotli,PK',
'Al Ahmadi,KW',
'Cuenca,EC',
'Chisinau,MD',
'Wroclaw,PL',
'Hebi,CN',
'Tebessa,DZ',
'Memphis,US',
'Jingmen,CN',
'Barnaul,RU',
'Dandong,CN',
'Stuttgart,DE',
'Jaboatao dos Guararapes,BR',
'Cancun,MX',
'Contagem,BR',
'Ulyanovsk,RU',
'Glasgow,GB',
'Bhilai,IN',
'Panshan,CN',
'Djibouti,DJ',
'Irkutsk,RU',
'Las Vegas,US',
'Al Mansurah,EG',
'Kermanshah,IR',
'Duesseldorf,DE',
'Coyoacan,MX',
'Feira de Santana,BR',
'Jiaozhou,CN',
'Suizhou,CN',
'Villa Nueva,GT',
'Khabarovsk,RU',
'Cuiaba,BR',
'Al Hudaydah,YE',
'Pasig City,PH',
'Chizhou,CN',
'Taiz,YE',
'Santa Maria Chimalhuacan,MX',
'Ya\'an,CN',
'Borivli,IN',
'Yaroslavl,RU',
'Kawaguchi,JP',
'Jambi City,ID',
'Ha\'il,SA',
'Bhavnagar,IN',
'Benoni,ZA',
'Vladivostok,RU',
'Cochin,IN',
'Jinzhou,CN',
'Tuxtla,MX',
'Kryvyy Rih,UA',
'Amravati,IN',
'Sanming,CN',
'Islamabad,PK',
'Sangli,IN',
'Milwaukee,US',
'Vancouver,CA',
'Shuangyashan,CN',
'Rotterdam,NL',
'Grosszschocher,DE',
'Kleinzschocher,DE',
'Luancheng,CN',
'Makhachkala,RU',
'Anyang-si,KR',
'Kagoshima,JP',
'Rasht,IR',
'Brampton,CA',
'Mar del Plata,AR',
'Abeokuta,NG',
'Essen,DE',
'Al Mahallah al Kubra,EG',
'Yingkou,CN',
'Las Pinas,PH',
'Zhangzhou,CN',
'Reynosa,MX',
'Thuan An,VN',
'Dortmund,DE',
'Londrina,BR',
'Goeteborg,SE',
'Blantyre,MW',
'New Kingston,JM',
'UEskuedar,TR',
'Bucaramanga,CO',
'Genoa,IT',
'Oslo,NO',
'Cuttack,IN',
'Malacca,MY',
'Malaga,ES',
'Khabarovsk Vtoroy,RU',
'Libreville,GA',
'Kerman,IR',
'Orumiyeh,IR',
'Bahcelievler,TR',
'Tanta,EG',
'Baltimore,US',
'Bikaner,IN',
'Tlaquepaque,MX',
'Tlalpan,MX',
'Herat,AF',
'Tomsk,RU',
'Juiz de Fora,BR',
'Umraniye,TR',
'Shihezi,CN',
'South Boston,US',
'Poznan,PL',
'Irbid,JO',
'Kota Bharu,MY',
'Cimahi,ID',
'Puente Alto,CL',
'Mukalla,YE',
'Nyala,SD',
'Orenburg,RU',
'Bokaro,IN',
'Asmara,ER',
'Sokoto,NG',
'Uberlandia,BR',
'Hachioji,JP',
'Wenchang,CN',
'Albuquerque,US',
'Hamhung,KP',
'Kemerovo,RU',
'Nasiriyah,IQ',
'Warangal,IN',
'Sheffield,GB',
'Dresden,DE',
'Bloemfontein,ZA',
'Santiago de Cuba,CU',
'Siping,CN',
'Huaihua,CN',
'Bahawalpur,PK',
'Chiclayo,PE',
'Zahedan,IR',
'Kimhae,KR',
'Nanded,IN',
'Kozhikode,IN',
'Changwon,KR',
'Pristina,XK',
'Jiamusi,CN',
'Antipolo,PH',
'Korla,CN',
'Porto Velho,BR',
'San Miguel de Tucuman,AR',
'Kuantan,MY',
'Sevastopol,UA',
'Bremen,DE',
'Wanning,CN',
'Meknes,MA',
'Xinzhou,CN',
'Banqiao,TW',
'Sargodha,PK',
'Bangui,CF',
'Vilnius,LT',
'Pingdu,CN',
'Calamba,PH',
'Novokuznetsk,RU',
'Kisangani,CD',
'Ryazan\',RU',
'Ji\'an,CN',
'Mersin,TR',
'Raurkela,IN',
'Warri,NG',
'Guli,CN',
'Aksu,CN',
'Ebute Ikorodu,NG',
'Tanggu,CN',
'Astrakhan,RU',
'Beira,MZ',
'Ar Raqqah,SY',
'Quebec,CA',
'Cuauhtemoc,MX',
'Shangluo,CN',
'Tucson,US',
'Guntur,IN',
'Ibague,CO',
'Antwerpen,BE',
'Touba,SN',
'Asyut,EG',
'Hamadan,IR',
'Qionghai,CN',
'Cangzhou,CN',
'Homyel\',BY',
'San Salvador,SV',
'Himeji,JP',
'Beihai,CN',
'Van,TR',
'Penza,RU',
'Mazar-e Sharif,AF',
'Kandahar,AF',
'Lyon,FR',
'Surakarta,ID',
'Hengshui,CN',
'Dehra Dun,IN',
'Erode,IN',
'Salta,AR',
'Bhayandar,IN',
'Esenler,TR',
'Fresno,US',
'Hamilton,CA',
'Al Fayyum,EG',
'Durgapur,IN',
'Victoria de Durango,MX',
'Ajmer,IN',
'Lisbon,PT',
'Ulhasnagar,IN',
'Guangyuan,CN',
'Leeds,GB',
'Kolhapur,IN',
'Siliguri,IN',
'Nuernberg,DE',
'Hannover,DE',
'Azadshahr,IR',
'Samarkand,UZ',
'Macapa,BR')

today = datetime.today()- timedelta(days=1)
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

def get_rates(origin_lat,origin_lng,destination_lat,destination_lng,size,type,weight,volume,auth_token):
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

                total_price = port_fees_from+port_fees_to+freight+truck_from+truck_to
                transit_time = response_json['data']['shipment'][n]['freight'][0]['transitTime'] + truck_from_tt+truck_to_tt
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

                total_price = port_fees_from+port_fees_to+freight+truck_from+truck_to
                transit_time = response_json['data']['shipment'][n]['freight'][0]['transitTime'] + truck_from_tt+truck_to_tt
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

origin = st.selectbox('Origin',countries)
destination = st.selectbox( 'Destination',countries, index = 76)
with st.spinner('Loading SeaRates Rates...'):
    try:
        auth_token = get_auth_token()
        origin_lat,origin_lng = get_coordinates(origin)
        destination_lat,destination_lng  = get_coordinates(destination)

        df = pd.DataFrame()
        #20' container
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"20","FCL","","",auth_token)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df=pd.DataFrame({"Type":['20ft FCL'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})

        #40' container
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"40","FCL","","",auth_token)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df2=pd.DataFrame({"Type":['40ft FCL'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df2])
            else:
                df = df2

        #LCL
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"","LCL","1000","5",auth_token)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df3=pd.DataFrame({"Type":['LCL (1,000 Kg)'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df3])
            else:
                df = df3

        #Air
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"","Air","1000","5",auth_token)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df4=pd.DataFrame({"Type":['Air (1,000 Kg)'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df4])
            else:
                df = df4
        #FTL
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"","FTL","","86",auth_token)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df4=pd.DataFrame({"Type":['FTL (86 CBM)'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df4])
            else:
                df = df4
        #LTL
        min_price,max_price,min_tt,max_tt = get_rates(origin_lat,origin_lng,destination_lat,destination_lng,"","LTL","1000","5",auth_token)
        if min_price != None:
            min_price = "${:,.0f}".format(min_price)
            max_price = "${:,.0f}".format(max_price)
            df5=pd.DataFrame({"Type":['LTL (1,000 Kg)'], "Min Price":[min_price],"Max Price":[max_price],"Min Transit Time":[min_tt],"Max Transit Time":[max_tt]})
            if len(df)>0:
                df = pd.concat([df,df5])
            else:
                df = df5

        fig = plt.figure(figsize=(24,4))
        plt.rcParams['font.family'] = 'Segoe UI'
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
        fig = plt.figure(figsize=(24,5))
        plt.rcParams['font.family'] = 'Segoe UI'
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

with st.spinner('Loading Freightos Rates...'):
    loadtype = 'container40'
    weight = 4000  # weight in kilograms
    quantity = 1
    results=get_results(origin,destination,loadtype,weight,quantity,'FCL','')
    nrow = len(results)
    results.insert(loc=0, column='Type', value =list(repeat('40ft', nrow)))

    loadtype = 'container20'
    weight = 2000  # weight in kilograms
    quantity = 1
    results2=get_results(origin,destination,loadtype,weight,quantity,'FCL','')
    nrow = len(results2)
    results2.insert(loc=0, column='Type', value =list(repeat('20ft', nrow)))
    results = pd.concat([results,results2])

    loadtype = 'pallets'
    weight = 200  # weight in kilograms
    quantity = 5
    results3=get_results(origin,destination,loadtype,weight,quantity,'LCL','1')
    nrow = len(results3)
    results3.insert(loc=0, column='Type', value =list(repeat('200kg Pallets (5)', nrow)))
    results = pd.concat([results,results3])

    if results['Min Price'].isnull().all():
        fig = plt.figure(figsize=(24,4))
        plt.rcParams['font.family'] = 'Segoe UI'
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
        plt.rcParams['font.family'] = 'Segoe UI'
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